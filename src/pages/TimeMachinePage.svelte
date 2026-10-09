<script lang="ts">
  import { router } from '../lib/router/router.svelte';
  import { battleOccursInYear, clampAtlasYear } from '../lib/data/dates';
  import { atlasIndex, reignLabel } from '../lib/data/lookup';
  import { hrefHome, hrefRuler, hrefState, hrefTimeMachine } from '../lib/router/route';
  import { REGION_MAP, RESULT_MAP, yearLabel } from '../lib/data/atlas';
  import { getAllBattles } from '../lib/data/battles';
  import type { Ruler, State } from '../schemas/atlas.schema';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import Clock from '@lucide/svelte/icons/clock';
  import Landmark from '@lucide/svelte/icons/landmark';
  import Crown from '@lucide/svelte/icons/crown';
  import Swords from '@lucide/svelte/icons/swords';
  import ChevronLeft from '@lucide/svelte/icons/chevron-left';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';

  let { year: initialYear }: { year?: number } = $props();

  const index = atlasIndex();
  const allBattles = getAllBattles();

  let selectedYear = $state(1453);

  $effect(() => {
    selectedYear = initialYear ?? 1453;
  });

  // Önemli tarihsel dönemeçler listesi
  const milestones = [
    { year: -209, label: 'MÖ 209', desc: 'Mete Han / Asya Hun' },
    { year: 552, label: '552', desc: 'I. Göktürk Kağanlığı' },
    { year: 751, label: '751', desc: 'Talas Savaşı' },
    { year: 840, label: '840', desc: 'Karahanlılar / Uygur' },
    { year: 1040, label: '1040', desc: 'Dandanakan Zaferi' },
    { year: 1071, label: '1071', desc: 'Malazgirt Zaferi' },
    { year: 1176, label: '1176', desc: 'Miryokefalon Zaferi' },
    { year: 1243, label: '1243', desc: 'Kösedağ Savaşı' },
    { year: 1299, label: '1299', desc: 'Osmanlı Beyliği' },
    { year: 1402, label: '1402', desc: 'Ankara Savaşı' },
    { year: 1453, label: '1453', desc: "İstanbul'un Fethi" },
    { year: 1514, label: '1514', desc: 'Çaldıran Zaferi' },
    { year: 1526, label: '1526', desc: 'Mohaç / Babür' },
    { year: 1683, label: '1683', desc: 'II. Viyana Kuşatması' },
    { year: 1774, label: '1774', desc: 'Küçük Kaynarca' },
    { year: 1922, label: '1922', desc: 'Kurtuluş & Saltanatın Sonu' },
  ];

  function setYear(y: number) {
    if (!Number.isFinite(y)) return;
    selectedYear = clampAtlasYear(y);
    router.replace(hrefTimeMachine(selectedYear));
  }

  function stepYear(delta: number) {
    setYear(selectedYear === -1 && delta === 1 ? 1 : selectedYear === 1 && delta === -1 ? -1 : selectedYear + delta);
  }

  // Seçilen yılda varlığını sürdüren devletler
  const activeStates = $derived.by(() => {
    return index.devletler.filter((s) => {
      const startOk = s.start <= selectedYear;
      const endOk = s.end === null || s.end >= selectedYear;
      return startOk && endOk;
    });
  });

  // Seçilen yılda tahtta olan hükümdarlar
  interface ActiveRulerItem {
    ruler: Ruler;
    state: State;
  }

  const activeRulers = $derived.by(() => {
    const list: ActiveRulerItem[] = [];
    for (const state of activeStates) {
      for (const ruler of state.rulers ?? []) {
        const [rStart, rEnd] = ruler.reign;
        if (rStart !== null && rEnd !== null) {
          if (rStart <= selectedYear && rEnd >= selectedYear) {
            list.push({ ruler, state });
          }
        }
      }
    }
    return list;
  });

  // Seçilen yılda (veya civarında) yapılan savaşlar
  const yearBattles = $derived.by(() => {
    return allBattles.filter((b) => {
      return battleOccursInYear(b.date, selectedYear);
    });
  });
</script>

<Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: 'Zaman Makinesi' }]} />

<PageHeader
  eyebrow="Eşzamanlı Tarih Gezgini"
  title="Tarihsel Zaman Makinesi"
  subtitle="Seçilen tek bir yılda Avrasya'da aynı anda hüküm süren Türk devletleri, tahttaki hükümdarlar ve yaşanan savaşlar"
>
  {#snippet badges()}
    <span class="meta-pill"><Clock size={13} aria-hidden="true" /> Yıl: {yearLabel(selectedYear)}</span>
    <span class="meta-pill"><Landmark size={13} aria-hidden="true" /> {activeStates.length} Aktif Devlet</span>
    <span class="meta-pill"><Crown size={13} aria-hidden="true" /> {activeRulers.length} Hükümdar Tahtta</span>
    {#if yearBattles.length > 0}
      <span class="result-badge zafer"><Swords size={12} aria-hidden="true" /> {yearBattles.length} Savaş</span>
    {/if}
  {/snippet}
</PageHeader>

<p class="honesty-note">Devlet ve saltanat tarihleri yıl düzeyindedir; geçiş yılında birden fazla hükümdar görünebilir. İki saltanat sınırı da kayıtlı hükümdarlar listelenir. Savaşlarda açık yıllar ve yıl aralıkları kullanılır; yaklaşık tarihler bir yıla atanmaz. Tarihsel takvimde yıl sıfır yoktur.</p>

<!-- Zaman Seçici Panel -->
<SectionBox title="Tarih Çizelgesi ve Yıl Seçimi">
  <div class="time-machine-controls">
    <div class="year-display-row">
      <div class="year-stepper">
        <button type="button" class="step-btn" title="10 Yıl Geri" onclick={() => stepYear(-10)}>-10</button>
        <button type="button" class="step-btn" title="1 Yıl Geri" onclick={() => stepYear(-1)}>
          <ChevronLeft size={16} aria-hidden="true" />
        </button>
      </div>

      <div class="current-year-badge">
        <span class="year-huge">{yearLabel(selectedYear)}</span>
        <span class="year-note">Avrasya Panoraması</span>
      </div>

      <div class="year-stepper">
        <button type="button" class="step-btn" title="1 Yıl İleri" onclick={() => stepYear(1)}>
          <ChevronRight size={16} aria-hidden="true" />
        </button>
        <button type="button" class="step-btn" title="10 Yıl İleri" onclick={() => stepYear(10)}>+10</button>
      </div>
    </div>

    <!-- Kaydırıcı -->
    <div class="slider-wrapper">
      <input
        type="range"
        class="year-slider"
        aria-label="Tarih yılı"
        aria-valuetext={yearLabel(selectedYear)}
        min="-220"
        max="1925"
        step="1"
        value={selectedYear}
        oninput={(e) => setYear(Number((e.target as HTMLInputElement).value))}
      />
      <div class="slider-ticks">
        <span>MÖ 220</span>
        <span>MS 1</span>
        <span>500</span>
        <span>1000</span>
        <span>1500</span>
        <span>1925</span>
      </div>
    </div>

    <!-- Önemli Dönemeçler -->
    <div class="milestones-row">
      <span class="milestones-label">Önemli Tarihler:</span>
      <div class="milestones-pills">
        {#each milestones as m (m.year)}
          <button
            type="button"
            class="milestone-pill"
            class:active={selectedYear === m.year}
          aria-pressed={selectedYear === m.year}
            title={m.desc}
            onclick={() => setYear(m.year)}
          >
            <b>{m.label}</b>
            <span class="pill-desc">{m.desc}</span>
          </button>
        {/each}
      </div>
    </div>
  </div>
</SectionBox>

<!-- O Yılda Yaşanan Savaşlar -->
{#if yearBattles.length > 0}
  <SectionBox title={`${yearLabel(selectedYear)} Yılını Kapsayan Savaş Kayıtları · ${yearBattles.length}`}>
    {#snippet icon()}
      <Swords size={14} class="icon-war" aria-hidden="true" />
    {/snippet}
    <div class="battles-mini-grid">
      {#each yearBattles as b (b.id)}
        <a class="battle-mini-card" href={b.href}>
          <div class="mini-header">
            <span class="mini-name">{b.name}</span>
            <small>{b.when}{!b.date.exact ? ' · tarih aralığı' : ''}</small>
            <span class="result-badge {b.result}">{RESULT_MAP[b.result]}</span>
          </div>
          <div class="mini-parties">
            <span>{b.stateName} (<b>{b.rulerName}</b>)</span>
            <span class="vs">vs</span>
            <span class="foe-text"><b>{b.foe}</b></span>
          </div>
          {#if b.note}
            <p class="mini-note">{b.note}</p>
          {/if}
        </a>
      {/each}
    </div>
  </SectionBox>
{/if}

<!-- O Yılda Tahtta Olan Hükümdarlar -->
<SectionBox title={`${yearLabel(selectedYear)} Yılında Tahtta Olan Hükümdarlar · ${activeRulers.length}`}>
  {#snippet icon()}
    <Crown size={14} class="icon-ruler" aria-hidden="true" />
  {/snippet}
  {#if activeRulers.length === 0}
    <p class="empty-notice">
      {yearLabel(selectedYear)} yılında kayıtlara geçmiş başlangıç ve bitiş yılları bilinen bir hükümdar bulunmuyor veya bu yıl geçiş/fetret dönemine denk geliyor.
    </p>
  {:else}
    <div class="rulers-grid">
      {#each activeRulers as { ruler, state } (state.id + ruler.id)}
        <a class="ruler-live-card" href={hrefRuler(state.id, ruler.id)}>
          <div class="card-head">
            <div class="ruler-identity">
              <h3 class="ruler-name">{ruler.name}</h3>
              <span class="ruler-title">{ruler.title || 'Hükümdar'}</span>
            </div>
            <span class="state-pill" style="border-left: 3px solid {REGION_MAP[state.region]?.color ?? '#b5651d'}">
              {state.name}
            </span>
          </div>

          <div class="reign-tag">
            Saltanat: <b>{reignLabel(ruler)}</b>
          </div>

          {#if ruler.summary}
            <p class="ruler-summary">{ruler.summary}</p>
          {/if}

          {#if ruler.wars && ruler.wars.length > 0}
            <div class="ruler-wars-count">
              <Swords size={12} aria-hidden="true" /> {ruler.wars.length} Savaş
            </div>
          {/if}
        </a>
      {/each}
    </div>
  {/if}
</SectionBox>

<!-- O Yılda Avrasya'da Yaşayan Türk Devletleri -->
<SectionBox title={`${yearLabel(selectedYear)} Yılında Aktif Türk Devletleri · ${activeStates.length}`}>
  {#snippet icon()}
    <Landmark size={14} class="icon-state" aria-hidden="true" />
  {/snippet}
  {#if activeStates.length === 0}
    <p class="empty-notice">{yearLabel(selectedYear)} yılında aktif Türk devleti kaydı bulunmuyor.</p>
  {:else}
    <div class="states-grid">
      {#each activeStates as state (state.id)}
        <a class="state-snapshot-card" href={hrefState(state.id)}>
          <div class="state-head">
            <span class="region-indicator" style="background: {REGION_MAP[state.region]?.color ?? '#b5651d'}"></span>
            <h4 class="state-title">{state.name}</h4>
          </div>

          <div class="state-period">
            {yearLabel(state.start)} – {yearLabel(state.end)}
          </div>

          <div class="state-capital">
            Başkent: <b>{state.capital || 'Kayıtlarda yok'}</b>
          </div>

          {#if state.summary}
            <p class="state-desc">{state.summary}</p>
          {/if}
        </a>
      {/each}
    </div>
  {/if}
</SectionBox>

<style>
  .time-machine-controls {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .year-display-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    padding: 12px 0;
  }

  .year-stepper {
    display: flex;
    gap: 6px;
  }

  .step-btn {
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 8px;
    font-size: 12px;
    font-weight: 600;
    color: var(--ink);
    cursor: pointer;
    box-shadow: var(--shadow-sm);
    transition: all 0.18s ease;
  }

  .step-btn:hover {
    background: var(--surface-2);
    border-color: var(--accent-line);
  }

  .current-year-badge {
    text-align: center;
    min-width: 170px;
  }

  .year-huge {
    display: block;
    font-family: var(--font-serif);
    font-size: 38px;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
    letter-spacing: -0.02em;
  }

  .year-note {
    font-size: 11px;
    color: var(--ink-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
    display: block;
  }

  .slider-wrapper {
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding: 0 8px;
  }

  .year-slider {
    width: 100%;
    height: 8px;
    border-radius: 4px;
    background: var(--surface-3);
    outline: none;
    cursor: pointer;
    accent-color: var(--accent);
  }

  .slider-ticks {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    color: var(--ink-dim);
  }

  .milestones-row {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding-top: 10px;
    border-top: 1px solid var(--border);
  }

  .milestones-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--ink-dim);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .milestones-pills {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 4px;
  }

  .milestone-pill {
    padding: 6px 10px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 2px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.18s ease;
  }

  .milestone-pill:hover {
    background: var(--surface-2);
    border-color: var(--accent-line);
  }

  .milestone-pill.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #ffffff;
  }

  .milestone-pill.active .pill-desc {
    color: #ffffff;
  }

  .pill-desc {
    font-size: 10px;
    color: var(--ink-dim);
  }

  .battles-mini-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(min(100%, 320px), 1fr));
    gap: 10px;
  }

  .battle-mini-card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.18s ease, box-shadow 0.18s ease;
  }

  .battle-mini-card:hover {
    border-color: var(--accent-line);
    box-shadow: var(--shadow-sm);
  }

  .mini-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .mini-name {
    font-size: 13px;
    font-weight: 700;
    color: var(--ink);
  }

  .mini-parties {
    font-size: 12px;
    color: var(--ink-soft);
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 6px;
  }

  .vs {
    font-size: 10px;
    color: var(--accent);
    font-weight: 700;
  }

  .foe-text {
    color: var(--defeat-ink);
  }

  .mini-note {
    font-size: 11.5px;
    color: var(--ink-dim);
    margin: 0;
    line-height: 1.4;
  }

  .rulers-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 12px;
  }

  .ruler-live-card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    text-decoration: none;
    color: inherit;
    transition: all 0.18s ease;
  }

  .ruler-live-card:hover {
    border-color: var(--accent-line);
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
  }

  .card-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
  }

  .ruler-name {
    margin: 0;
    font-size: 14px;
    font-weight: 700;
    color: var(--ink);
  }

  .ruler-title {
    font-size: 11px;
    color: var(--ink-dim);
  }

  .state-pill {
    font-size: 11px;
    font-weight: 600;
    padding: 2px 8px;
    background: var(--surface-2);
    border-radius: 4px;
    color: var(--ink);
    max-width: 140px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .reign-tag {
    font-size: 11px;
    color: var(--ink-soft);
  }

  .ruler-summary {
    margin: 0;
    font-size: 12px;
    line-height: 1.4;
    color: var(--ink-soft);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .ruler-wars-count {
    margin-top: auto;
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 4px;
    padding-top: 6px;
    border-top: 1px solid var(--border);
  }

  .states-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 12px;
  }

  .state-snapshot-card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    text-decoration: none;
    color: inherit;
    transition: all 0.18s ease;
  }

  .state-snapshot-card:hover {
    border-color: var(--accent-line);
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
  }

  .state-head {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .region-indicator {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .state-title {
    margin: 0;
    font-size: 14px;
    font-weight: 700;
    color: var(--ink);
  }

  .state-period {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
  }

  .state-capital {
    font-size: 11.5px;
    color: var(--ink-dim);
  }

  .state-desc {
    margin: 4px 0 0;
    font-size: 12px;
    line-height: 1.4;
    color: var(--ink-soft);
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .empty-notice {
    color: var(--ink-dim);
    font-style: italic;
    padding: 16px 0;
  }
  @media (max-width: 480px) {
    .year-display-row { gap: 8px; }
    .current-year-badge { min-width: 90px; }
    .year-huge { font-size: 28px; }
    .step-btn { width: 32px; }
    .year-stepper { gap: 3px; }
    .mini-header { flex-wrap: wrap; gap: 6px; }
  }
</style>
