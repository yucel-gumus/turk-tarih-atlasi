<script lang="ts">
  import type { State } from '../schemas/atlas.schema';
  import { atlasIndex, filterStates } from '../lib/data/lookup';
  import { DEVLET_REGIONS, MILESTONES, yearLabel, type RealRegion } from '../lib/data/atlas';
  import { hrefGuide, hrefHome } from '../lib/router/route';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import TimelineSurface, { type Bar, type Lane } from '../components/ui/TimelineSurface.svelte';
  import TimelineToolbar, { type EraPreset } from '../components/ui/TimelineToolbar.svelte';
  import TimelineMinimap from '../components/ui/TimelineMinimap.svelte';
  import TimelineTooltip from '../components/ui/TimelineTooltip.svelte';
  import StateGrid from '../components/ui/StateGrid.svelte';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import Search from '@lucide/svelte/icons/search';
  import { tick, onDestroy } from 'svelte';

  let { region }: { region: RealRegion | null } = $props();

  const index = atlasIndex();

  /**
   * Genişletilmiş yakınlaştırma katsayıları (1×'den 24×'e kadar akıcı adımlar).
   * 1× tüm tarihi ekrana sığdırır; 24× en kısa ömürlü beylikleri bile rahatça inceler.
   */
  const SCALES = [1, 1.5, 2, 3, 5, 8, 12, 16, 24];
  const BAR_H = 34;
  const BAR_GAP = 4;
  const LANE_PAD = 6;
  /** Kısa süren devletler erişilebilir dokunma/tıklama boyutu kazansın diye en küçük çubuk genişliği (WCAG 2.5.8). */
  const MIN_BAR_PX = 24;
  const END_PAD = 16;
  /** Yüzyıl etiketinin sığması için gereken yüz yıllık genişlik. */
  const CENTURY_LABEL_PX = 46;
  /** Kilometre taşı etiketlerinin açıldığı yakınlık (px/yıl). */
  const MILESTONE_LABEL_PX_PER_YEAR = 1.8;
  /** Sol kulvar adları sütunu ile şeridin üst satırları; ikisi aynı yüksekliği paylaşır. */
  const HEAD_H = 40;

  let scaleIndex = $state(0);
  let activeEraId = $state<string>('all');
  let query = $state('');
  let scroller = $state<HTMLDivElement | null>(null);
  let laneWidth = $state(0);
  let scrollLeft = $state(0);

  // Fareyle sürükleme durumu (Pan/Drag)
  let isPointerDown = false;
  let isDragging = $state(false);
  let startX = 0;
  let startY = 0;
  let startScrollLeft = 0;
  let startScrollTop = 0;
  let dragDistance = 0;
  let suppressClick = false;
  let lastWheelTime = 0;
  let cachedScrollerRect: DOMRect | null = null;
  let activeCaptureTarget: HTMLElement | null = null;

  // Kürsör kılavuz çizgisi ve yıl göstergesi
  let hoverYear = $state<number | null>(null);
  let hoverX = $state<number | null>(null);

  // Zengin önizleme tooltip'i
  let hoveredState = $state<State | null>(null);
  let tooltipX = $state(0);
  let tooltipY = $state(0);
  let tooltipVisible = $state(false);

  // rAF Throttling
  let rafPointerId: number | null = null;
  let pendingPointerEvent: PointerEvent | null = null;

  const filtered = $derived(filterStates(index.devletler, { region, query }));

  /** Sınırlar bütün devletlerden türetilir; süzgeç ekseni kaydırmasın. */
  const bounds = $derived.by(() => {
    let min = Infinity;
    let max = -Infinity;
    for (const state of index.devletler) {
      if (state.start < min) min = state.start;
      if (state.end > max) max = state.end;
    }
    return { min, max };
  });

  const spanYears = $derived(Math.max(1, bounds.max - bounds.min));

  const pxPerYear = $derived.by(() => {
    if (laneWidth <= 0 || spanYears <= 0) return 0;
    return (laneWidth / spanYears) * SCALES[scaleIndex];
  });

  const surfaceWidth = $derived(spanYears * pxPerYear + END_PAD);

  /**
   * Görünür yıl aralığı (Minimap ve başlık için reaktif)
   */
  const viewportStartYear = $derived.by(() => {
    if (pxPerYear <= 0) return bounds.min;
    return bounds.min + scrollLeft / pxPerYear;
  });

  const viewportEndYear = $derived.by(() => {
    if (pxPerYear <= 0 || laneWidth <= 0) return bounds.max;
    return bounds.min + (scrollLeft + laneWidth) / pxPerYear;
  });

  /**
   * Bölge kulvarları. Yoğun bölgelerde çubuklar alt satırlara paketlenir.
   */
  const lanes = $derived.by(() => {
    if (pxPerYear <= 0) return [] as Lane[];
    const out: Lane[] = [];
    for (const info of DEVLET_REGIONS) {
      const items = filtered.filter((state) => state.region === info.id);
      if (items.length === 0) continue;
      const rowEnds: number[] = [];
      const bars: Bar[] = [];
      for (const state of items) {
        const left = (state.start - bounds.min) * pxPerYear;
        const width = Math.max(MIN_BAR_PX, (state.end - state.start) * pxPerYear);
        let row = rowEnds.findIndex((end) => end <= left);
        if (row < 0) {
          rowEnds.push(0);
          row = rowEnds.length - 1;
        }
        rowEnds[row] = left + width;
        bars.push({ state, left, width, top: row * (BAR_H + BAR_GAP), height: BAR_H });
      }
      const rowsHeight = rowEnds.length * (BAR_H + BAR_GAP) - BAR_GAP;
      out.push({ info, bars, height: Math.max(BAR_H, rowsHeight) + LANE_PAD * 2 });
    }
    return out;
  });

  const centuries = $derived.by(() => {
    if (pxPerYear <= 0) return [];
    const list: { year: number; left: number; label: string }[] = [];
    for (let year = Math.ceil(bounds.min / 100) * 100; year <= bounds.max; year += 100) {
      list.push({ year, left: (year - bounds.min) * pxPerYear, label: yearLabel(year) });
    }
    return list;
  });
  const showCenturyLabels = $derived(pxPerYear * 100 >= CENTURY_LABEL_PX);

  const milestones = $derived.by(() => {
    if (pxPerYear <= 0) return [];
    return MILESTONES.filter((m) => m.year >= bounds.min && m.year <= bounds.max).map((m) => ({
      year: m.year,
      label: m.label,
      left: (m.year - bounds.min) * pxPerYear,
    }));
  });
  const showMilestoneLabels = $derived(pxPerYear >= MILESTONE_LABEL_PX_PER_YEAR);

  const regionCounts = $derived(
    DEVLET_REGIONS.map((info) => ({
      info,
      count: index.devletler.filter((state) => state.region === info.id).length,
    }))
  );

  /**
   * Kürsör odaklı yakınlaştırma:
   * Fare nerede duruyorsa o yıl yakınlaşırken / uzaklaşırken imlecin altında sabit kalır!
   */
  async function setScale(next: number, clientX?: number) {
    const clamped = Math.max(0, Math.min(SCALES.length - 1, next));
    if (clamped === scaleIndex || !scroller) return;

    const node = scroller;
    const rect = node.getBoundingClientRect();

    // Fare imlecinin veya ekran merkezinin koordinatı
    const viewportX = clientX !== undefined ? clientX - rect.left : node.clientWidth / 2;
    const currentContentX = node.scrollLeft + viewportX;
    const yearUnderPoint = bounds.min + (pxPerYear > 0 ? currentContentX / pxPerYear : 0);

    scaleIndex = clamped;
    await tick();

    if (!node) return;
    const newPxPerYear = (laneWidth / spanYears) * SCALES[scaleIndex];
    const newContentX = (yearUnderPoint - bounds.min) * newPxPerYear;
    node.scrollLeft = Math.max(0, newContentX - viewportX);
    scrollLeft = node.scrollLeft;
  }

  /**
   * Fare tekerleğiyle yakınlaştırma / kaydırma işleyicisi:
   * - Dikey tekerlek: Fare imlecinin olduğu yıla akıcı biçimde yakınlaşır / uzaklaşır.
   * - Shift + tekerlek veya trackpad yatay kaydırma: Doğal yatay kaydırmaya izin verir.
   */
  function handleWheel(e: WheelEvent) {
    if (!scroller) return;

    if (e.shiftKey || (Math.abs(e.deltaX) > Math.abs(e.deltaY) && Math.abs(e.deltaX) > 4)) {
      return;
    }

    const now = performance.now();
    if (now - lastWheelTime < 60) {
      e.preventDefault();
      return;
    }

    if (Math.abs(e.deltaY) > 2) {
      e.preventDefault();
      lastWheelTime = now;
      if (e.deltaY < 0) {
        setScale(scaleIndex + 1, e.clientX);
      } else {
        setScale(scaleIndex - 1, e.clientX);
      }
    }
  }

  /**
   * Fare ile basılı tutup sürükleyerek 2 boyutlu kaydırma (2D Pointer Drag-to-Pan)
   * Yatayda zaman eksenini, dikeyde kulvarları/sayfayı kaydırır.
   * rAF ile 60 FPS'e kilitlenir ve layout thrashing önlenir.
   */
  function handlePointerDown(e: PointerEvent) {
    if (e.pointerType !== 'mouse' || e.button !== 0 || !scroller) return;
    isPointerDown = true;
    startX = e.clientX;
    startY = e.clientY;
    startScrollLeft = scroller.scrollLeft;
    startScrollTop = window.scrollY;
    dragDistance = 0;
    cachedScrollerRect = scroller.getBoundingClientRect();
    activeCaptureTarget = (e.currentTarget as HTMLElement) ?? scroller;
  }

  function handlePointerMove(e: PointerEvent) {
    pendingPointerEvent = e;
    if (rafPointerId === null) {
      rafPointerId = requestAnimationFrame(processPointerMove);
    }
  }

  function processPointerMove() {
    rafPointerId = null;
    const e = pendingPointerEvent;
    if (!e || !scroller) return;

    // Kılavuz çizgisi güncelleme
    if (!isDragging) {
      const rect = cachedScrollerRect ?? scroller.getBoundingClientRect();
      const surfaceX = e.clientX - rect.left + scroller.scrollLeft;
      if (pxPerYear > 0 && surfaceX >= 0 && surfaceX <= surfaceWidth) {
        hoverYear = Math.round(bounds.min + surfaceX / pxPerYear);
        hoverX = surfaceX;
      }
    }

    if (!isPointerDown) return;

    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    dragDistance = Math.hypot(dx, dy);

    if (dragDistance > 4) {
      if (!isDragging) {
        isDragging = true;
        tooltipVisible = false;
        hoveredState = null;
        try {
          activeCaptureTarget?.setPointerCapture(e.pointerId);
        } catch {
          // ignore
        }
      }
      scroller.scrollLeft = startScrollLeft - dx;
      scrollLeft = scroller.scrollLeft;
      window.scrollTo(0, Math.max(0, startScrollTop - dy));
    }
  }

  function handlePointerUp(e: PointerEvent) {
    if (!isPointerDown) return;
    isPointerDown = false;
    cachedScrollerRect = null;
    if (rafPointerId !== null) {
      cancelAnimationFrame(rafPointerId);
      rafPointerId = null;
    }

    if (isDragging) {
      if (activeCaptureTarget && activeCaptureTarget.hasPointerCapture(e.pointerId)) {
        try {
          activeCaptureTarget.releasePointerCapture(e.pointerId);
        } catch {
          // ignore
        }
      }
      activeCaptureTarget = null;
      suppressClick = true;
      isDragging = false;
      setTimeout(() => {
        suppressClick = false;
      }, 60);
    }
  }


  /**
   * Sürükleme bittiğinde bağlantının kazara açılmasını önler
   */
  function handleClickCapture(e: MouseEvent) {
    if (suppressClick) {
      e.preventDefault();
      e.stopPropagation();
      suppressClick = false;
    }
  }

  function handleScroll() {
    if (scroller) {
      scrollLeft = scroller.scrollLeft;
    }
  }

  function handlePanBy(pixels: number) {
    if (!scroller) return;
    scroller.scrollBy({ left: pixels, behavior: 'smooth' });
  }

  function handlePanByRatio(ratioDelta: number) {
    if (!scroller) return;
    scroller.scrollLeft += ratioDelta * surfaceWidth;
    scrollLeft = scroller.scrollLeft;
  }

  async function handleJumpToYear(targetYear: number, targetScaleIndex?: number) {
    if (targetScaleIndex !== undefined && targetScaleIndex !== scaleIndex) {
      scaleIndex = targetScaleIndex;
      await tick();
    }
    if (!scroller) return;
    const targetX = (targetYear - bounds.min) * pxPerYear;
    const targetScroll = Math.max(0, targetX - scroller.clientWidth / 2);
    scroller.scrollTo({ left: targetScroll, behavior: 'smooth' });
  }

  function handleJumpToEra(era: EraPreset) {
    activeEraId = era.id;
    handleJumpToYear(era.year, era.scaleIndex);
  }

  function handleBarHover(state: State, pos: { clientX: number; clientY: number }) {
    if (isDragging) return;
    hoveredState = state;
    const pad = 16;
    const tooltipW = 280;
    const tooltipH = 180;
    let tx = pos.clientX + 16;
    let ty = pos.clientY + 16;
    if (tx + tooltipW > window.innerWidth - pad) {
      tx = pos.clientX - tooltipW - 16;
    }
    if (ty + tooltipH > window.innerHeight - pad) {
      ty = pos.clientY - tooltipH - 16;
    }
    tooltipX = tx;
    tooltipY = ty;
    tooltipVisible = true;
  }

  function handleBarLeave() {
    tooltipVisible = false;
    hoveredState = null;
  }

  function handleSurfaceMouseLeave() {
    hoverYear = null;
    hoverX = null;
    tooltipVisible = false;
  }

  function handleKeyDown(e: KeyboardEvent) {
    const target = e.target as HTMLElement;
    if (!scroller?.contains(target)) return;
    if (target && (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA')) {
      return;
    }

    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      handlePanBy(e.shiftKey ? -450 : -150);
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      handlePanBy(e.shiftKey ? 450 : 150);
    } else if (e.key === '+' || e.key === '=') {
      e.preventDefault();
      setScale(scaleIndex + 1);
    } else if (e.key === '-' || e.key === '_') {
      e.preventDefault();
      setScale(scaleIndex - 1);
    } else if (e.key === 'Home') {
      e.preventDefault();
      scroller?.scrollTo({ left: 0, behavior: 'smooth' });
    } else if (e.key === 'End') {
      e.preventDefault();
      if (scroller) scroller.scrollTo({ left: scroller.scrollWidth, behavior: 'smooth' });
    } else if (e.key === '0') {
      e.preventDefault();
      setScale(0);
    }
  }
  onDestroy(() => { if (rafPointerId !== null) cancelAnimationFrame(rafPointerId); });
</script>

<svelte:window onkeydown={handleKeyDown} />

<PageHeader
  eyebrow="Kronolojik şerit"
  title="Türk Devletleri Atlası"
  subtitle={`${yearLabel(bounds.min)} – ${yearLabel(bounds.max)} arasındaki devletleri zaman ve bölgeye göre keşfedin.`}
>
  {#snippet badges()}
    <span class="meta-pill rulers-count">{index.toplam.devlet} devlet</span>
    <span class="meta-pill">{index.toplam.hukumdar} hükümdar</span>
    <span class="meta-pill">{index.toplam.savas} savaş</span>
    <span class="meta-pill">{index.toplam.es + index.toplam.cocuk} aile kaydı</span>
  {/snippet}
</PageHeader>

{#if index.rehber}
  <a class="guide-strip glass-panel" href={hrefGuide()}>
    <span class="guide-eyebrow">Rehber</span>
    <span class="guide-title">{index.rehber.name}</span>
    <span class="guide-sub">
      Kapsam, kaynaklar ve tarihsel belirsizlikler
    </span>
    <ChevronRight size={16} aria-hidden="true" />
  </a>
{/if}

<div class="filters no-print">
  <div class="region-pills">
    <a class="region-pill" class:active={region === null} href={hrefHome()}>
      Tüm bölgeler · {index.devletler.length}
    </a>
    {#each regionCounts as { info, count } (info.id)}
      <a
        class="region-pill"
        class:active={region === info.id}
        href={hrefHome(info.id)}
        style="--region-color: {info.color}"
      >
        <span class="state-indicator" style="background: {info.color}"></span>
        {info.name} · {count}
      </a>
    {/each}
  </div>

  <label class="search-box">
    <Search size={14} aria-hidden="true" />
    <input
      id="timeline-search-filter"
      name="timeline-search"
      type="search"
      aria-label="Şeritteki devletleri süz"
      placeholder="Devlet, diğer ad ya da hükümdar ara"
      bind:value={query}
    />
  </label>
</div>

<div class="timeline" role="region" aria-label="Kronolojik zaman şeridi">
  <!-- Gelişmiş Araç Çubuğu (Pan, Zoom, Dönem Çipleri) -->
  <TimelineToolbar
    filteredCount={filtered.length}
    minYearLabel={yearLabel(bounds.min)}
    maxYearLabel={yearLabel(bounds.max)}
    scales={SCALES}
    {scaleIndex}
    {activeEraId}
    onSetScale={setScale}
    onPanBy={handlePanBy}
    onJumpToEra={handleJumpToEra}
  />

  <!-- Zaman Gezgini (İnteraktif Minimap) -->
  <TimelineMinimap
    {bounds}
    states={index.devletler}
    {viewportStartYear}
    {viewportEndYear}
    onJumpToYear={handleJumpToYear}
    onPanByRatio={handlePanByRatio}
  />

  <!-- Zaman Şeridi Gövdesi -->
  <div class="timeline-body">
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div
      class="lane-labels"
      class:is-dragging={isDragging}
      style="padding-top: {HEAD_H}px"
      onpointerdown={handlePointerDown}
      onpointermove={handlePointerMove}
      onpointerup={handlePointerUp}
      onpointercancel={handlePointerUp}
      onclickcapture={handleClickCapture}
    >
      {#each lanes as lane (lane.info.id)}
        <div class="lane-label" style="height: {lane.height}px">
          <span class="state-indicator" style="background: {lane.info.color}"></span>
          <span class="lane-name">{lane.info.name}</span>
          <span class="lane-count">{lane.bars.length}</span>
        </div>
      {/each}
    </div>

    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <!-- svelte-ignore a11y_no_noninteractive_tabindex -->
    <div
      class="timeline-scroll"
      class:is-dragging={isDragging}
      bind:this={scroller}
      bind:clientWidth={laneWidth}
      onscroll={handleScroll}
      onwheel={handleWheel}
      onpointerdown={handlePointerDown}
      onpointermove={handlePointerMove}
      onpointerup={handlePointerUp}
      onpointercancel={handlePointerUp}
      onclickcapture={handleClickCapture}
      onmouseleave={handleSurfaceMouseLeave}
      tabindex="0"
      role="region"
      aria-label="Zaman şeridi tuvali. Fareyle sürükleyebilir veya yön tuşlarıyla gezinebilirsiniz."
    >
      <TimelineSurface
        {surfaceWidth}
        headHeight={HEAD_H}
        {hoverX}
        {hoverYear}
        {isDragging}
        {milestones}
        {showMilestoneLabels}
        {centuries}
        {showCenturyLabels}
        {lanes}
        onBarHover={handleBarHover}
        onBarLeave={handleBarLeave}
      />
    </div>
  </div>

  {#if filtered.length === 0}
    <p class="honesty-note">
      Bu süzgeçle eşleşen devlet yok. Sonuç boş çıktı; kayıtlarda veri eksik olduğu
      anlamına gelmez, arama ölçütü hiçbir kayda uymadı.
    </p>
  {/if}
</div>

<!-- Zengin Devlet Önizleme Kartı -->
<TimelineTooltip
  state={hoveredState}
  x={tooltipX}
  y={tooltipY}
  visible={tooltipVisible && !isDragging}
/>

<!-- Ayrıştırılmış Devletler Listesi Izgarası -->
<StateGrid states={filtered} />

<style>
  .guide-strip {
    display: flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
    padding: 12px 16px;
    border-radius: 12px;
    color: var(--gold-primary);
    transition: border-color 0.2s ease, background 0.2s ease;
  }

  .guide-strip:hover {
    border-color: var(--accent-line);
    background: var(--accent-soft);
  }

  .guide-eyebrow {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--accent-strong);
    background: var(--accent-soft);
    border: 1px solid var(--accent-line);
    border-radius: 5px;
    padding: 2px 7px;
  }

  .guide-title {
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 600;
    color: var(--text-main);
  }

  .guide-sub {
    font-size: 11px;
    color: var(--text-muted);
    min-width: 0;
  }

  .filters {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    align-items: center;
    justify-content: space-between;
  }

  .region-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .region-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    font-weight: 500;
    color: var(--ink-muted);
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 9999px;
    padding: 5px 12px;
    transition: all 0.18s ease;
  }

  .region-pill:hover {
    color: var(--ink);
    border-color: var(--border-strong);
  }

  .region-pill.active {
    color: var(--ink);
    border-color: var(--region-color, var(--accent));
    background: color-mix(in srgb, var(--region-color, var(--accent)) 12%, #ffffff);
    font-weight: 600;
  }

  .search-box {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 13px;
    border-radius: 9999px;
    border: 1px solid var(--border);
    background: var(--surface-1);
    color: var(--ink-dim);
    min-width: 260px;
    transition: border-color 0.18s ease, box-shadow 0.18s ease;
  }

  .search-box:focus-within {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-soft);
  }

  .search-box input {
    flex: 1;
    background: none;
    border: none;
    outline: none;
    color: var(--ink);
    font-family: inherit;
    font-size: 12px;
  }

  .timeline {
    display: flex;
    flex-direction: column;
    min-width: 0;
    width: 100%;
    gap: 12px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 16px 20px 20px;
    box-shadow: var(--shadow-md);
    scroll-margin-top: 80px;
  }

  .timeline-body {
    display: flex;
    align-items: flex-start;
  }

  .lane-labels {
    flex-shrink: 0;
    width: 152px;
    border-right: 1px solid var(--border);
    margin-right: -1px;
    z-index: 2;
    cursor: grab;
    user-select: none;
    touch-action: pan-x pan-y;
  }

  .lane-label {
    display: flex;
    align-items: center;
    gap: 7px;
    padding-right: 10px;
    padding-left: 2px;
    font-size: 11px;
    font-weight: 500;
    color: var(--ink-muted);
    line-height: 1.3;
    border-bottom: 1px solid var(--border);
    box-sizing: border-box;
  }

  .lane-label:last-child {
    border-bottom: none;
  }

  .lane-label .state-indicator {
    width: 7px;
    height: 7px;
    border-radius: 9999px;
    flex-shrink: 0;
  }

  .lane-name {
    flex: 1;
    min-width: 0;
    font-size: 11px;
    font-weight: 600;
    color: var(--ink);
    letter-spacing: -0.01em;
    line-height: 1.25;
    line-clamp: 2;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .lane-count {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
    color: var(--ink-dim);
    background: var(--surface-2);
    padding: 1px 6px;
    border-radius: 9999px;
    border: 1px solid var(--border);
    flex-shrink: 0;
  }

  .timeline-scroll {
    flex: 1;
    min-width: 0;
    overflow-x: auto;
    overflow-y: hidden;
    padding-bottom: 6px;
    cursor: grab;
    touch-action: pan-x pan-y;
  }

  .lane-labels.is-dragging,
  .timeline-scroll.is-dragging {
    cursor: grabbing !important;
    user-select: none !important;
  }

  .timeline-scroll:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: -2px;
    border-radius: 8px;
  }

  .honesty-note {
    font-size: 12.5px;
    line-height: 1.55;
    color: var(--ink-muted);
    margin: 8px 0 0;
    padding: 12px 14px;
    border-radius: 8px;
    background: var(--surface-2);
    border: 1px solid var(--border);
  }

  @media (max-width: 700px) {
    .filters {
      gap: 8px;
    }

    .search-box {
      width: 100%;
      min-width: 0;
    }

    .timeline {
      padding: 12px 10px 14px;
      border-radius: 12px;
    }

    .lane-labels {
      width: 104px;
    }

    .lane-label {
      padding-right: 6px;
      padding-left: 0;
      gap: 5px;
      font-size: 9.5px;
    }

    .lane-name {
      font-size: 9.5px;
    }

    .lane-count {
      font-size: 9px;
      padding: 0 4px;
    }
  }
</style>
