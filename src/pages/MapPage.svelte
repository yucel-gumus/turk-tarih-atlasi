<script lang="ts">
  import { getAllStateGeoMarkers, type GeoStateMarker } from '../lib/data/geo';
  import { DEVLET_REGIONS, REGION_MAP, yearLabel } from '../lib/data/atlas';
  import { hrefHome, hrefState } from '../lib/router/route';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import Compass from '@lucide/svelte/icons/compass';
  import MapPin from '@lucide/svelte/icons/map-pin';
  import Landmark from '@lucide/svelte/icons/landmark';
  import Crown from '@lucide/svelte/icons/crown';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import Clock from '@lucide/svelte/icons/clock';

  const allMarkers = getAllStateGeoMarkers();

  let selectedRegion = $state<string | 'all'>('all');
  let filterByYear = $state(false);
  let currentYear = $state(1299);
  let activeMarker = $state<GeoStateMarker | null>(null);

  const filteredMarkers = $derived.by(() => {
    return allMarkers.filter((m) => {
      if (selectedRegion !== 'all' && m.state.region !== selectedRegion) return false;
      if (filterByYear) {
        const startOk = m.state.start <= currentYear;
        const endOk = m.state.end === null || m.state.end >= currentYear;
        if (!startOk || !endOk) return false;
      }
      return true;
    });
  });

  function selectMarker(m: GeoStateMarker) {
    activeMarker = m;
  }
</script>

<Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: 'Coğrafi Harita' }]} />

<PageHeader
  eyebrow="Jeopolitik Boyut"
  title="Avrasya Coğrafi Tarih Haritası"
  subtitle="80 Türk devletinin başkentleri, odak coğrafyaları ve Avrasya bozkırlarındaki göç yolları"
>
  {#snippet badges()}
    <span class="meta-pill"><Compass size={13} aria-hidden="true" /> {filteredMarkers.length} Başkent & Merkez</span>
    {#if filterByYear}
      <span class="meta-pill"><Clock size={13} aria-hidden="true" /> {yearLabel(currentYear)} Yılı Odaklı</span>
    {/if}
  {/snippet}
</PageHeader>

<!-- Harita Kontrol Araç Çubuğu -->
<SectionBox title="Harita Süzgeçleri ve Zaman Kaydırıcısı">
  <div class="map-controls">
    <!-- Bölge Seçici -->
    <div class="control-row">
      <span class="control-label">Bölge:</span>
      <div class="pills-scroll">
        <button
          type="button"
          class="map-pill"
          class:active={selectedRegion === 'all'}
          onclick={() => (selectedRegion = 'all')}
        >
          Tüm Coğrafya ({allMarkers.length})
        </button>
        {#each DEVLET_REGIONS as reg (reg.id)}
          <button
            type="button"
            class="map-pill"
            class:active={selectedRegion === reg.id}
            onclick={() => (selectedRegion = reg.id)}
          >
            <span class="pill-dot" style="background: {reg.color}"></span>
            {reg.name}
          </button>
        {/each}
      </div>
    </div>

    <!-- Tarihe Göre Canlı Filtre -->
    <div class="control-row year-toggle-row">
      <label class="checkbox-label">
        <input type="checkbox" bind:checked={filterByYear} />
        <span class="toggle-text">Zaman filtresini etkinleştir (O yılda var olan başkentler)</span>
      </label>

      {#if filterByYear}
        <div class="year-slider-box">
          <span class="active-year-display">{yearLabel(currentYear)}</span>
          <input
            type="range"
            class="map-slider"
            min="-220"
            max="1925"
            step="1"
            bind:value={currentYear}
          />
        </div>
      {/if}
    </div>
  </div>
</SectionBox>

<!-- İnteraktif SVG Harita -->
<div class="map-stage-wrapper">
  <div class="map-viewport">
    <svg viewBox="0 0 1000 550" class="historical-svg-map" preserveAspectRatio="xMidYMid meet">
      <defs>
        <!-- Su zemin deseni / gölgesi -->
        <filter id="pin-glow" x="-50%" y="-50%" width="200%" height="200%">
          <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="rgba(0,0,0,0.4)" />
        </filter>
      </defs>

      <!-- Deniz / Su Tabanı -->
      <rect width="1000" height="550" class="ocean-bg" />

      <!-- Stilize Avrasya ve Kuzey Afrika Kara Kütleleri -->
      <g class="landmasses">
        <!-- Avrupa ve İskandinavya -->
        <path d="M 50,80 Q 120,60 180,90 T 260,130 L 250,220 L 160,250 L 100,200 Z" class="land-path" />
        <!-- Akdeniz Kuzeyi ve Balkanlar -->
        <path d="M 120,240 Q 200,220 280,250 L 250,330 L 140,320 Z" class="land-path" />
        <!-- Anadolu -->
        <path d="M 230,280 Q 320,270 380,290 L 370,350 L 250,340 Z" class="land-path focus-anatolia" />
        <!-- Kafkaslar ve Hazar Çevresi -->
        <path d="M 370,240 Q 450,220 480,270 L 450,340 L 360,320 Z" class="land-path" />
        <!-- Orta Asya / Maveraünnehir / Bozkır -->
        <path d="M 450,150 Q 650,120 850,140 L 820,320 L 520,340 L 450,260 Z" class="land-path focus-steppe" />
        <!-- Moğolistan / Orhun / İç Asya -->
        <path d="M 780,120 Q 920,110 980,160 L 960,280 L 800,280 Z" class="land-path focus-mongolia" />
        <!-- İran ve Horasan -->
        <path d="M 380,330 Q 550,320 620,360 L 580,450 L 420,430 Z" class="land-path" />
        <!-- Hint Alt Kıtası -->
        <path d="M 580,390 Q 680,380 720,450 L 650,530 L 570,460 Z" class="land-path" />
        <!-- Mısır ve Kuzey Afrika -->
        <path d="M 60,360 Q 200,350 260,370 L 250,470 L 80,480 Z" class="land-path" />
        <!-- Çin İçleri -->
        <path d="M 820,280 Q 960,270 990,360 L 920,460 L 760,400 Z" class="land-path" />

        <!-- Göller & İç Denizler -->
        <!-- Karadeniz -->
        <ellipse cx="270" cy="270" rx="42" ry="18" class="water-body" />
        <!-- Hazar Denizi -->
        <ellipse cx="420" cy="275" rx="22" ry="48" class="water-body" />
        <!-- Aral Gölü -->
        <ellipse cx="505" cy="265" rx="14" ry="20" class="water-body" />
        <!-- Balkaş Gölü -->
        <ellipse cx="650" cy="225" rx="26" ry="9" class="water-body" />
        <!-- Baykal Gölü -->
        <ellipse cx="820" cy="140" rx="8" ry="24" class="water-body" />
        <!-- Isık Göl -->
        <ellipse cx="650" cy="275" rx="10" ry="6" class="water-body" />
      </g>

      <!-- Coğrafi Bölge Etiketleri (Silik) -->
      <g class="geo-labels" aria-hidden="true">
        <text x="820" y="195">ÖTÜKEN / ORHUN</text>
        <text x="610" y="240">TÜRKİSTAN</text>
        <text x="510" y="220">DEŞT-İ KIPÇAK</text>
        <text x="280" y="315">ANADOLU</text>
        <text x="470" y="380">İRAN & HORASAN</text>
        <text x="620" y="440">HİNDİSTAN</text>
        <text x="180" y="410">MISIR</text>
        <text x="170" y="190">AVRUPA / BALKAN</text>
      </g>

      <!-- Başkent ve Odak Noktası İşaretçileri (Pins) -->
      <g class="pins-layer">
        {#each filteredMarkers as m (m.state.id)}
          {@const isSelected = activeMarker?.state.id === m.state.id}
          {@const color = REGION_MAP[m.state.region]?.color ?? '#b5651d'}
          <g
            class="pin-group"
            class:selected={isSelected}
            transform="translate({m.svgPos.x}, {m.svgPos.y})"
            onclick={() => selectMarker(m)}
            onkeydown={(e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                selectMarker(m);
              }
            }}
            role="button"
            tabindex="0"
            aria-label="{m.state.name} ({m.geo.capitalName})"
          >
            <!-- Tıklama / Dokunma Alanı (Görünmez Geniş Daire) -->
            <circle r="14" class="hit-area" />

            <!-- Dış Halka -->
            <circle
              r={isSelected ? 9 : 5}
              fill={color}
              stroke="#ffffff"
              stroke-width={isSelected ? 2.5 : 1.5}
              filter="url(#pin-glow)"
              class="pin-circle"
            />

            <!-- Merkez Nokta -->
            {#if isSelected}
              <circle r="3" fill="#ffffff" />
            {/if}

            <!-- Başkent Adı Etiketi -->
            <text
              y={isSelected ? -12 : -8}
              text-anchor="middle"
              class="pin-label"
              class:selected-label={isSelected}
            >
              {m.state.short || m.state.name}
            </text>
          </g>
        {/each}
      </g>
    </svg>
  </div>

  <!-- Seçili Devlet Bilgi Kartı (Floating Drawer / Card) -->
  {#if activeMarker}
    <div class="active-state-drawer">
      <div class="drawer-header">
        <div class="drawer-title-group">
          <span
            class="drawer-badge"
            style="background: {REGION_MAP[activeMarker.state.region]?.color ?? '#b5651d'}"
          ></span>
          <div>
            <h3 class="drawer-title">{activeMarker.state.name}</h3>
            <span class="drawer-region">{REGION_MAP[activeMarker.state.region]?.name}</span>
          </div>
        </div>
        <button
          type="button"
          class="close-drawer-btn"
          onclick={() => (activeMarker = null)}
          aria-label="Kapat"
        >
          ✕
        </button>
      </div>

      <div class="drawer-body">
        <div class="drawer-meta-item">
          <span class="meta-name">Tarih Aralığı:</span>
          <span class="meta-val">{yearLabel(activeMarker.state.start)} – {yearLabel(activeMarker.state.end)}</span>
        </div>

        <div class="drawer-meta-item">
          <span class="meta-name"><MapPin size={12} aria-hidden="true" /> Başkent / Merkez:</span>
          <span class="meta-val"><b>{activeMarker.geo.capitalName}</b></span>
        </div>

        <div class="drawer-meta-item">
          <span class="meta-name">Günümüz Konumu:</span>
          <span class="meta-val">{activeMarker.geo.modernCountry}</span>
        </div>

        {#if activeMarker.state.summary}
          <p class="drawer-summary">{activeMarker.state.summary}</p>
        {/if}

        <div class="drawer-actions">
          <a class="drawer-link-btn" href={hrefState(activeMarker.state.id)}>
            Devlet Sayfasına Git <ChevronRight size={14} aria-hidden="true" />
          </a>
        </div>
      </div>
    </div>
  {/if}
</div>

<style>
  .map-controls {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .control-row {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }

  .control-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--ink-dim);
    letter-spacing: 0.04em;
    flex-shrink: 0;
  }

  .pills-scroll {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 2px;
    flex-grow: 1;
  }

  .map-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 11px;
    font-size: 11.5px;
    font-weight: 500;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--surface-1);
    color: var(--ink-soft);
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.18s ease;
  }

  .map-pill:hover {
    background: var(--surface-2);
    border-color: var(--border-strong);
  }

  .map-pill.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #ffffff;
  }

  .pill-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
  }

  .year-toggle-row {
    padding-top: 10px;
    border-top: 1px solid var(--border);
    justify-content: space-between;
  }

  .checkbox-label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12.5px;
    font-weight: 600;
    color: var(--ink);
    cursor: pointer;
  }

  .year-slider-box {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-grow: 1;
    max-width: 320px;
  }

  .active-year-display {
    font-family: var(--font-serif);
    font-size: 14px;
    font-weight: 700;
    color: var(--accent);
    min-width: 70px;
    text-align: right;
  }

  .map-slider {
    width: 100%;
    accent-color: var(--accent);
    cursor: pointer;
  }

  .map-stage-wrapper {
    position: relative;
    width: 100%;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: var(--shadow-md);
  }

  .map-viewport {
    width: 100%;
    height: auto;
    position: relative;
  }

  .historical-svg-map {
    width: 100%;
    height: auto;
    display: block;
  }

  .ocean-bg {
    fill: #e8eef3;
  }

  .landmasses .land-path {
    fill: #f5f1e8;
    stroke: #d9d1c1;
    stroke-width: 1.5;
  }

  .focus-anatolia {
    fill: #f4ecdc;
  }

  .focus-steppe {
    fill: #f7efe1;
  }

  .focus-mongolia {
    fill: #f3ebd8;
  }

  .water-body {
    fill: #dbe4ec;
    stroke: #ccd9e3;
    stroke-width: 1;
  }

  .geo-labels text {
    font-family: var(--font-sans);
    font-size: 11px;
    font-weight: 700;
    fill: #b3a996;
    letter-spacing: 0.12em;
    user-select: none;
    pointer-events: none;
  }

  .pin-group {
    cursor: pointer;
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  .pin-group:hover {
    transform: scale(1.3);
  }

  .hit-area {
    fill: transparent;
  }

  .pin-circle {
    transition: all 0.2s ease;
  }

  .pin-label {
    font-family: var(--font-sans);
    font-size: 8.5px;
    font-weight: 600;
    fill: var(--ink);
    opacity: 0.85;
    pointer-events: none;
    text-shadow: 0 1px 2px #ffffff, 0 -1px 2px #ffffff, 1px 0 2px #ffffff, -1px 0 2px #ffffff;
  }

  .pin-group:hover .pin-label,
  .selected-label {
    font-size: 10.5px;
    font-weight: 700;
    opacity: 1;
    fill: var(--accent-strong);
  }

  /* Aktif Devlet Bilgi Kartı */
  .active-state-drawer {
    position: absolute;
    bottom: 16px;
    right: 16px;
    width: 320px;
    max-width: calc(100% - 32px);
    background: var(--surface-translucent);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: var(--shadow-lg);
    z-index: 10;
  }

  .drawer-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
  }

  .drawer-title-group {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .drawer-badge {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .drawer-title {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 700;
    color: var(--ink);
  }

  .drawer-region {
    font-size: 10.5px;
    color: var(--ink-dim);
  }

  .close-drawer-btn {
    background: none;
    border: none;
    font-size: 14px;
    color: var(--ink-dim);
    cursor: pointer;
    padding: 2px 6px;
    border-radius: 4px;
  }

  .drawer-body {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 10px;
  }

  .drawer-meta-item {
    display: flex;
    justify-content: space-between;
    font-size: 11.5px;
  }

  .meta-name {
    color: var(--ink-dim);
    display: flex;
    align-items: center;
    gap: 4px;
  }

  .meta-val {
    color: var(--ink);
  }

  .drawer-summary {
    margin: 6px 0 0;
    font-size: 11.5px;
    line-height: 1.4;
    color: var(--ink-soft);
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .drawer-actions {
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
  }

  .drawer-link-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    padding: 6px 12px;
    background: var(--accent);
    color: #ffffff;
    border-radius: 6px;
    text-decoration: none;
    font-size: 12px;
    font-weight: 600;
    transition: background 0.18s ease;
  }

  .drawer-link-btn:hover {
    background: var(--accent-strong);
  }
</style>
