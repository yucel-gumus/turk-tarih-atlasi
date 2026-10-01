<script lang="ts">
  import type { State } from '../schemas/atlas.schema';
  import { atlasIndex, filterStates } from '../lib/data/lookup';
  import { DEVLET_REGIONS, MILESTONES, yearLabel, type RealRegion, type RegionInfo } from '../lib/data/atlas';
  import { hrefGuide, hrefHome, hrefState } from '../lib/router/route';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import TimelineBar from '../components/ui/TimelineBar.svelte';
  import TimelineToolbar, { type EraPreset } from '../components/ui/TimelineToolbar.svelte';
  import TimelineMinimap from '../components/ui/TimelineMinimap.svelte';
  import TimelineTooltip from '../components/ui/TimelineTooltip.svelte';
  import { ChevronRight, Search } from '@lucide/svelte';
  import { tick } from 'svelte';

  let { region }: { region: RealRegion | null } = $props();

  const index = atlasIndex();

  /**
   * Genişletilmiş yakınlaştırma katsayıları (1×'den 24×'e kadar akıcı adımlar).
   * 1× tüm tarihi ekrana sığdırır; 24× en kısa ömürlü beylikleri bile rahatça inceler.
   */
  const SCALES = [1, 1.5, 2, 3, 5, 8, 12, 16, 24];
  const BAR_H = 26;
  const BAR_GAP = 3;
  const LANE_PAD = 6;
  /** Çok kısa süren devletler kaybolmasın diye en küçük çubuk genişliği. */
  const MIN_BAR_PX = 4;
  const END_PAD = 16;
  /** Yüzyıl etiketinin sığması için gereken yüz yıllık genişlik. */
  const CENTURY_LABEL_PX = 46;
  /** Kilometre taşı etiketlerinin açıldığı yakınlık (px/yıl). */
  const MILESTONE_LABEL_PX_PER_YEAR = 1.8;
  /** Sol kulvar adları sütunu ile şeridin üst satırları; ikisi aynı yüksekliği paylaşır. */
  const HEAD_H = 40;

  interface Bar {
    state: State;
    left: number;
    width: number;
    top: number;
    height: number;
  }

  interface Lane {
    info: RegionInfo;
    bars: Bar[];
    height: number;
  }

  let scaleIndex = $state(0);
  let query = $state('');
  let scroller = $state<HTMLDivElement | null>(null);
  let laneWidth = $state(0);
  let scrollLeft = $state(0);

  // Fareyle sürükleme durumu (Pan/Drag)
  let isPointerDown = false;
  let isDragging = $state(false);
  let startX = 0;
  let startScrollLeft = 0;
  let dragDistance = 0;
  let suppressClick = false;
  let lastWheelTime = 0;

  // Kürsör kılavuz çizgisi ve yıl göstergesi
  let hoverYear = $state<number | null>(null);
  let hoverX = $state<number | null>(null);

  // Zengin önizleme tooltip'i
  let hoveredState = $state<State | null>(null);
  let tooltipX = $state(0);
  let tooltipY = $state(0);
  let tooltipVisible = $state(false);

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

    // Shift tuşu veya touchpad yatay kaydırma hareketi varsa doğal kaydırmaya bırak
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
   * Fare ile basılı tutup sürükleyerek kaydırma (Pointer Drag-to-Pan)
   */
  function handlePointerDown(e: PointerEvent) {
    if (e.button !== 0 || !scroller) return;
    isPointerDown = true;
    startX = e.clientX;
    startScrollLeft = scroller.scrollLeft;
    dragDistance = 0;
  }

  function handlePointerMove(e: PointerEvent) {
    // Kılavuz çizgisi güncelleme
    if (!isDragging && scroller) {
      const rect = scroller.getBoundingClientRect();
      const surfaceX = e.clientX - rect.left + scroller.scrollLeft;
      if (pxPerYear > 0 && surfaceX >= 0 && surfaceX <= surfaceWidth) {
        hoverYear = Math.round(bounds.min + surfaceX / pxPerYear);
        hoverX = surfaceX;
      }
    }

    if (!isPointerDown || !scroller) return;

    const dx = e.clientX - startX;
    dragDistance = Math.abs(dx);

    if (dragDistance > 4) {
      if (!isDragging) {
        isDragging = true;
        tooltipVisible = false;
        hoveredState = null;
        try {
          scroller.setPointerCapture(e.pointerId);
        } catch {
          // ignore
        }
      }
      scroller.scrollLeft = startScrollLeft - dx;
      scrollLeft = scroller.scrollLeft;
    }
  }

  function handlePointerUp(e: PointerEvent) {
    if (!isPointerDown) return;
    isPointerDown = false;

    if (isDragging) {
      if (scroller && scroller.hasPointerCapture(e.pointerId)) {
        try {
          scroller.releasePointerCapture(e.pointerId);
        } catch {
          // ignore
        }
      }
      suppressClick = true;
      isDragging = false;
      setTimeout(() => {
        suppressClick = false;
      }, 60);
    }
  }

  function handlePointerCancel(e: PointerEvent) {
    if (!isPointerDown) return;
    isPointerDown = false;
    if (isDragging && scroller && scroller.hasPointerCapture(e.pointerId)) {
      try {
        scroller.releasePointerCapture(e.pointerId);
      } catch {
        // ignore
      }
    }
    isDragging = false;
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
    handleJumpToYear(era.year, era.scaleIndex);
  }

  function handleBarHover(state: State, e: MouseEvent) {
    if (isDragging) return;
    hoveredState = state;
    const pad = 16;
    const tooltipW = 280;
    const tooltipH = 180;
    let tx = e.clientX + 16;
    let ty = e.clientY + 16;
    if (tx + tooltipW > window.innerWidth - pad) {
      tx = e.clientX - tooltipW - 16;
    }
    if (ty + tooltipH > window.innerHeight - pad) {
      ty = e.clientY - tooltipH - 16;
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
    <div class="lane-labels" style="padding-top: {HEAD_H}px">
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
      onpointercancel={handlePointerCancel}
      onclickcapture={handleClickCapture}
      onmouseleave={handleSurfaceMouseLeave}
      tabindex="0"
      role="application"
      aria-label="Zaman şeridi tuvali. Fareyle sürükleyebilir veya yön tuşlarıyla gezinebilirsiniz."
    >
      <div class="timeline-surface" style="width: {surfaceWidth}px">
        <!-- Canlı Kürsör Kılavuz Çizgisi -->
        {#if hoverX !== null && hoverYear !== null && !isDragging}
          <div class="hover-guideline" style="left: {hoverX}px;" aria-hidden="true">
            <span class="hover-year-pill">{yearLabel(hoverYear)}</span>
          </div>
        {/if}

        <div class="milestone-lines" aria-hidden="true">
          {#each milestones as m (m.year)}
            <span class="milestone-line" style="left: {m.left}px"></span>
          {/each}
        </div>

        <div class="head-rows" style="height: {HEAD_H}px">
          <div class="century-ruler">
            {#each centuries as c (c.year)}
              <span class="century-tick" style="left: {c.left}px">
                {#if showCenturyLabels}
                  <span class="century-label">{c.label}</span>
                {/if}
              </span>
            {/each}
          </div>
          <div class="milestone-row">
            {#if showMilestoneLabels}
              {#each milestones as m (m.year)}
                <span class="milestone-label" style="left: {m.left}px">{m.label} · {yearLabel(m.year)}</span>
              {/each}
            {/if}
          </div>
        </div>

        <div class="lanes">
          {#each lanes as lane (lane.info.id)}
            <div class="lane" style="height: {lane.height}px">
              {#each lane.bars as bar (bar.state.id)}
                <TimelineBar
                  state={bar.state}
                  color={lane.info.color}
                  left={bar.left}
                  width={bar.width}
                  top={bar.top}
                  height={bar.height}
                  onHover={handleBarHover}
                  onLeave={handleBarLeave}
                />
              {/each}
            </div>
          {/each}
        </div>
      </div>
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

<SectionBox title={`Devletler · ${filtered.length}`}>
  <div id="devlet-listesi" class="state-list">
    {#each filtered as state (state.id)}
      <a
        class="state-list-item"
        href={hrefState(state.id)}
        style="--state-color: {DEVLET_REGIONS.find((r) => r.id === state.region)?.color ?? '#e5c378'}"
      >
        <span class="state-list-top">
          <span class="state-list-name">{state.name}</span>
          <ChevronRight size={15} aria-hidden="true" />
        </span>
        <span class="state-list-meta">
          {yearLabel(state.start)} – {yearLabel(state.end)} · {state.rulers.length} hükümdar
        </span>
        <span class="state-list-summary">{state.summary}</span>
      </a>
    {/each}
  </div>
</SectionBox>

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
    border-color: var(--border-glass-bright);
    background: rgba(229, 195, 120, 0.06);
  }

  .guide-eyebrow {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    background: rgba(229, 195, 120, 0.12);
    border-radius: 4px;
    padding: 2px 6px;
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
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 9999px;
    padding: 5px 11px;
    transition: all 0.18s ease;
  }

  .region-pill:hover {
    color: var(--text-main);
    border-color: var(--border-glass-bright);
  }

  .region-pill.active {
    color: var(--text-main);
    border-color: var(--region-color, var(--gold-primary));
    background: rgba(229, 195, 120, 0.08);
  }

  .search-box {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 12px;
    border-radius: 9999px;
    border: 1px solid var(--border-glass);
    background: rgba(255, 255, 255, 0.03);
    color: var(--text-dim);
    min-width: 260px;
  }

  .search-box input {
    flex: 1;
    background: none;
    border: none;
    outline: none;
    color: var(--text-main);
    font-family: inherit;
    font-size: 12px;
  }

  .timeline {
    display: flex;
    flex-direction: column;
    min-width: 0;
    width: 100%;
    gap: 10px;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 14px;
    padding: 14px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  }

  .state-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 10px;
    scroll-margin-top: 90px;
  }

  .state-list-item {
    display: flex;
    flex-direction: column;
    gap: 6px;
    min-width: 0;
    padding: 14px;
    border: 1px solid var(--border-glass);
    border-left: 3px solid var(--state-color);
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.025);
    transition: background 0.18s ease, border-color 0.18s ease;
  }

  .state-list-item:hover {
    background: rgba(255, 255, 255, 0.07);
    border-color: var(--state-color);
  }

  .state-list-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    color: var(--text-main);
  }

  .state-list-name {
    font-family: var(--font-serif);
    font-size: 16px;
    font-weight: 600;
  }

  .state-list-meta {
    font-size: 11px;
    color: var(--gold-primary);
  }

  .state-list-summary {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    overflow: hidden;
    font-size: 12px;
    line-height: 1.5;
    color: var(--text-muted);
  }

  .timeline-body {
    display: flex;
    align-items: flex-start;
  }

  .lane-labels {
    flex-shrink: 0;
    width: 132px;
  }

  .lane-label {
    display: flex;
    align-items: center;
    gap: 6px;
    padding-right: 10px;
    font-size: 10px;
    color: var(--text-muted);
    line-height: 1.3;
  }

  .lane-name {
    flex: 1;
    min-width: 0;
  }

  .lane-count {
    color: var(--text-dim);
  }

  .timeline-scroll {
    flex: 1;
    min-width: 0;
    overflow-x: auto;
    overflow-y: hidden;
    padding-bottom: 6px;
    cursor: grab;
    touch-action: pan-y;
  }

  .timeline-scroll.is-dragging {
    cursor: grabbing !important;
    user-select: none !important;
  }

  .timeline-scroll:focus-visible {
    outline: 2px solid var(--gold-primary);
    outline-offset: -2px;
    border-radius: 8px;
  }

  .timeline-surface {
    position: relative;
  }

  /* Kürsör Kılavuz Çizgisi */
  .hover-guideline {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--gold-primary);
    box-shadow: 0 0 8px var(--gold-glow);
    z-index: 8;
    pointer-events: none;
    transform: translateX(-50%);
  }

  .hover-year-pill {
    position: sticky;
    top: 2px;
    display: inline-block;
    transform: translateX(-50%);
    background: var(--gold-primary);
    color: #080a0d;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 9999px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4);
    white-space: nowrap;
  }

  .milestone-lines {
    position: absolute;
    inset: 0;
    z-index: 0;
  }

  .milestone-line {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: rgba(229, 195, 120, 0.13);
  }

  .head-rows {
    position: relative;
    z-index: 1;
  }

  .century-ruler {
    position: relative;
    height: 22px;
  }

  .century-tick {
    position: absolute;
    bottom: 0;
    width: 1px;
    height: 6px;
    background: rgba(255, 255, 255, 0.22);
  }

  .century-label {
    position: absolute;
    bottom: 8px;
    left: 0;
    transform: translateX(-50%);
    font-size: 10px;
    color: var(--text-dim);
    white-space: nowrap;
  }

  .milestone-row {
    position: relative;
    height: 18px;
  }

  .milestone-label {
    position: absolute;
    top: 2px;
    transform: translateX(-50%);
    font-size: 9px;
    color: var(--gold-primary);
    white-space: nowrap;
  }

  .lanes {
    position: relative;
    z-index: 1;
  }

  .lane {
    position: relative;
  }
</style>
