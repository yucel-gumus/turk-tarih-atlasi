<script lang="ts">
  import { clampAtlasYear } from '../lib/data/dates';
  import { onMount, onDestroy, tick } from 'svelte';
  import L from 'leaflet';
  import worldGeoURL from '../lib/data/world.geo.json?url';
  import type { GeoJsonObject } from 'geojson';
  import 'leaflet/dist/leaflet.css';
  import { getAllStateGeoMarkers, type GeoStateMarker } from '../lib/data/geo';
  import { DEVLET_REGIONS, REGION_MAP, yearLabel } from '../lib/data/atlas';
  import { hrefHome, hrefState } from '../lib/router/route';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import Compass from '@lucide/svelte/icons/compass';
  import MapPin from '@lucide/svelte/icons/map-pin';
  import Crown from '@lucide/svelte/icons/crown';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import Clock from '@lucide/svelte/icons/clock';
  import RotateCcw from '@lucide/svelte/icons/rotate-ccw';

  const allMarkers = getAllStateGeoMarkers();

  let mapElement: HTMLDivElement | null = $state(null);
  let map: L.Map | null = null;
  let markersLayer: L.LayerGroup | null = null;

  let selectedRegion = $state<string | 'all'>('all');
  let filterByYear = $state(false);
  let currentYear = $state(1299);
  let basemapError = $state(false);
  let basemapReady = $state(false);
  const basemapController = new AbortController();
  let resizeObserver: ResizeObserver | null = null;
  let activeMarker = $state<GeoStateMarker | null>(null);

  // Önemli dönüm noktası yılları
  const timePresets = [
    { year: -209, label: 'MÖ 209', desc: 'Asya Hun' },
    { year: 552, label: '552', desc: 'Göktürk' },
    { year: 751, label: '751', desc: 'Talas' },
    { year: 840, label: '840', desc: 'Uygur/Karahanlı' },
    { year: 1071, label: '1071', desc: 'Malazgirt' },
    { year: 1243, label: '1243', desc: 'Kösedağ' },
    { year: 1299, label: '1299', desc: 'Osmanlı' },
    { year: 1402, label: '1402', desc: 'Ankara' },
    { year: 1453, label: '1453', desc: 'İstanbul' },
    { year: 1526, label: '1526', desc: 'Mohaç / Babür' },
    { year: 1922, label: '1922', desc: 'Kurtuluş' },
  ];

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

  function renderMarkers() {
    if (!map || !markersLayer) return;

    markersLayer.clearLayers();

    for (const m of filteredMarkers) {
      const color = REGION_MAP[m.state.region]?.color ?? '#b5651d';
      const isSelected = activeMarker?.state.id === m.state.id;

      const customIcon = L.divIcon({
        className: 'atlas-custom-pin-wrap',
        html: `
          <div class="atlas-pin-node ${isSelected ? 'selected' : ''}" style="--pin-color: ${color};">
            <div class="pin-ring"></div>
            <div class="pin-dot"></div>
          </div>
        `,
        iconSize: [22, 22],
        iconAnchor: [11, 11],
        popupAnchor: [0, -12],
      });

      const leafletMarker = L.marker([m.geo.lat, m.geo.lon], { icon: customIcon, title: m.state.name, alt: m.state.name });

      // Şık, minimalist tooltip (üzerine gelince belirir, haritayı boğmaz)
      const tooltip = document.createElement('div');
      const name = document.createElement('strong');
      name.textContent = m.state.name;
      const capital = document.createElement('div');
      capital.textContent = m.geo.capitalName;
      tooltip.append(name, capital);
      leafletMarker.bindTooltip(tooltip, {
        direction: 'top', offset: [0, -10], className: 'atlas-map-tooltip',
      });

      leafletMarker.on('click', () => {
        activeMarker = m;
      });

      markersLayer.addLayer(leafletMarker);
    }
  }

  // Bölge değişince kamera otomatik uçsun
  function handleRegionChange(regId: string | 'all') {
    selectedRegion = regId;
    if (!map) return;

    const regionCenters: Record<string, { center: [number, number]; zoom: number }> = {
      anadolu: { center: [38.8, 35.5], zoom: 6 },
      turkistan: { center: [41.5, 68.0], zoom: 5 },
      bozkir: { center: [46.5, 100.0], zoom: 4.5 },
      bati: { center: [47.0, 32.0], zoom: 5 },
      kuzey: { center: [52.0, 52.0], zoom: 4.5 },
      iran: { center: [33.0, 58.0], zoom: 5 },
      all: { center: [41.0, 55.0], zoom: 3.5 },
    };

    const target = regionCenters[regId] ?? regionCenters.all;
    map.flyTo(target.center, target.zoom, { duration: 1.2, animate: !window.matchMedia('(prefers-reduced-motion: reduce)').matches });
  }

  function resetView() {
    selectedRegion = 'all';
    filterByYear = false;
    activeMarker = null;
    if (map) {
      map.flyTo([41.0, 55.0], 3.5, { duration: 1.0, animate: !window.matchMedia('(prefers-reduced-motion: reduce)').matches });
    }
  }

  onMount(() => {
    if (!mapElement) return;

    map = L.map(mapElement, {
      center: [41.0, 55.0],
      zoom: 3.5,
      minZoom: 2.5,
      maxZoom: 7,
      zoomControl: true,
      scrollWheelZoom: true,
    });

    map.attributionControl.addAttribution('<a href="https://www.naturalearthdata.com/about/terms-of-use/">Natural Earth</a> · günümüz sınırları');
    // Local vector data prevents a tile provider's HTTP 200 watermark from
    // silently replacing the actual map. Abort the request on navigation.
    void fetch(worldGeoURL, { signal: basemapController.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error('Basemap request failed');
        const geography = await response.json() as GeoJsonObject;
        if (!map) return;
        L.geoJSON(geography, {
          style: { color: '#b9b2a3', weight: 0.8, fillColor: '#f1eee5', fillOpacity: 1, className: 'atlas-base-land' },
          onEachFeature(feature, layer) {
            const label = document.createElement('span');
            label.textContent = String(feature.properties?.name ?? '');
            layer.bindTooltip(label, { sticky: true, className: 'atlas-map-tooltip' });
          },
        }).addTo(map);
        basemapReady = true;
      })
      .catch(() => { if (!basemapController.signal.aborted) basemapError = true; });

    resizeObserver = new ResizeObserver(() => map?.invalidateSize());
    resizeObserver.observe(mapElement);
    markersLayer = L.layerGroup().addTo(map);
    renderMarkers();
  });

  onDestroy(() => {
    basemapController.abort();
    resizeObserver?.disconnect();
    if (map) {
      map.remove();
      map = null;
    }
  });

  // Reaktif olarak filtre değişimlerinde pinleri güncelle
  $effect(() => {
    // Svelte 5 dependency tracking
    const _ = filteredMarkers;
    const __ = activeMarker;
    if (activeMarker && !filteredMarkers.some((m) => m.state.id === activeMarker?.state.id)) {
      activeMarker = null;
    }
    renderMarkers();
  });
</script>

<Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: 'Coğrafi Harita' }]} />

<PageHeader
  eyebrow="Gerçek Dünya Kartografisi"
  title="Avrasya Coğrafi Tarih Haritası"
  subtitle={`${allMarkers.length} devletin başkent veya odak konumu; işaretler yaklaşık konumları gösterir.`}
>
  {#snippet badges()}
    <span class="meta-pill"><Compass size={13} aria-hidden="true" /> {filteredMarkers.length} Konum Gösteriliyor</span>
    {#if filterByYear}
      <span class="meta-pill"><Clock size={13} aria-hidden="true" /> {yearLabel(currentYear)} Yılı Odaklı</span>
    {/if}
  {/snippet}
</PageHeader>

<!-- Harita Kontrol Araç Çubuğu -->
<SectionBox title="Harita Süzgeçleri ve Zaman Makinesi">
  <div class="map-controls">
    <!-- Bölge Seçici & Hızlı Uçuş -->
    <div class="control-row">
      <span class="control-label">Bölgeye Odaklan:</span>
      <div class="pills-scroll">
        <button
          type="button"
          class="map-pill"
          class:active={selectedRegion === 'all'}
          aria-pressed={selectedRegion === 'all'}
          onclick={() => handleRegionChange('all')}
        >
          Tüm Avrasya ({allMarkers.length})
        </button>
        {#each DEVLET_REGIONS as reg (reg.id)}
          <button
            type="button"
            class="map-pill"
            class:active={selectedRegion === reg.id}
          aria-pressed={selectedRegion === reg.id}
            onclick={() => handleRegionChange(reg.id)}
          >
            <span class="pill-dot" style="background: {reg.color}"></span>
            {reg.name}
          </button>
        {/each}
        <button type="button" class="reset-view-btn" onclick={resetView} title="Görünümü Sıfırla">
          <RotateCcw size={12} aria-hidden="true" /> Sıfırla
        </button>
      </div>
    </div>

    <!-- Tarihe Göre Canlı Süzgeç (Zaman Kaydırıcısı) -->
    <div class="control-row year-toggle-row">
      <label class="checkbox-label">
        <input type="checkbox" bind:checked={filterByYear} />
        <span class="toggle-text">Zaman filtresini etkinleştir (O yılda var olan devletler)</span>
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
            value={currentYear}
            oninput={(e) => currentYear = clampAtlasYear(Number(e.currentTarget.value))}
            aria-label="Harita zaman filtresi yılı"
            aria-valuetext={yearLabel(currentYear)}
          />
        </div>

        <div class="presets-row">
          {#each timePresets as p (p.year)}
            <button
              type="button"
              class="preset-pill"
              class:active={currentYear === p.year}
          aria-pressed={currentYear === p.year}
              onclick={() => (currentYear = p.year)}
              title={p.desc}
            >
              {p.label}
            </button>
          {/each}
        </div>
      {/if}
    </div>
  </div>
</SectionBox>

<p class="honesty-note">Her devlet için bir başkent veya odak konumu gösterilir. Başkent değişimleri, tarihî sınırlar ve yaklaşık konumların belirsizliği bu haritada modellenmez; zemin haritası günümüz coğrafyasını gösterir. Aynı konumdaki devletlere aşağıdaki listeden erişebilirsiniz.</p>
{#if !basemapReady && !basemapError}
  <p role="status">Coğrafi zemin yükleniyor…</p>
{/if}
{#if basemapError}
  <p class="honesty-note" role="status">Harita zemini yüklenemedi. Devlet konumları ve aşağıdaki liste kullanılabilir. Yeniden denemek için sayfayı yenileyin.</p>
{/if}
<!-- Leaflet Harita Sahnesi -->
<div class="map-stage-wrapper">
  <div class="leaflet-container-box" bind:this={mapElement}></div>

  <!-- Seçili Devlet Bilgi Kartı (Floating Drawer) -->
  {#if activeMarker}
    <div class="active-state-drawer" role="region" aria-labelledby="map-state-title">
      <div class="drawer-header">
        <div class="drawer-title-group">
          <span
            class="drawer-badge"
            style="background: {REGION_MAP[activeMarker.state.region]?.color ?? '#b5651d'}"
          ></span>
          <div>
            <h3 class="drawer-title" id="map-state-title" tabindex="-1">{activeMarker.state.name}</h3>
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
          <span class="meta-name"><MapPin size={12} aria-hidden="true" /> Başkent:</span>
          <span class="meta-val"><b>{activeMarker.geo.capitalName}</b></span>
        </div>

        <div class="drawer-meta-item">
          <span class="meta-name">Günümüz Ülkesi:</span>
          <span class="meta-val">{activeMarker.geo.modernCountry}</span>
        </div>

        {#if activeMarker.state.rulers && activeMarker.state.rulers.length > 0}
          <div class="drawer-meta-item">
            <span class="meta-name"><Crown size={12} aria-hidden="true" /> Hükümdar:</span>
            <span class="meta-val">{activeMarker.state.rulers.length} hükümdar</span>
          </div>
        {/if}

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

<SectionBox title={`Haritadaki Devletler · ${filteredMarkers.length}`}>
  <div class="map-state-list">
    {#each filteredMarkers as marker (marker.state.id)}
      <button type="button" aria-pressed={activeMarker?.state.id === marker.state.id} onclick={() => {
        activeMarker = marker;
        map?.setView([marker.geo.lat, marker.geo.lon], 6);
        mapElement?.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'center' });
        void tick().then(() => document.getElementById('map-state-title')?.focus({ preventScroll: true }));
      }}>{marker.state.name} · {marker.geo.capitalName}</button>
    {:else}
      <p role="status">Bu bölge ve yıl için devlet kaydı bulunamadı.</p>
    {/each}
  </div>
</SectionBox>

<style>
  .map-state-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: 6px; }
  .map-state-list button { text-align: left; padding: 10px; background: var(--surface-2); border: 1px solid var(--border); border-radius: 8px; color: var(--ink); }
  .map-state-list button[aria-pressed="true"] { border-color: var(--accent); }

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
    min-width: 0;
    max-width: 100%;
    align-items: center;
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

  .reset-view-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 5px 10px;
    font-size: 11px;
    background: var(--surface-3);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--ink-dim);
    cursor: pointer;
    margin-left: auto;
  }

  .reset-view-btn:hover {
    background: var(--surface-2);
    color: var(--ink);
  }

  .year-toggle-row {
    padding-top: 10px;
    border-top: 1px solid var(--border);
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
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
    gap: 12px;
    width: 100%;
    max-width: 480px;
  }

  .active-year-display {
    font-family: var(--font-serif);
    font-size: 16px;
    font-weight: 700;
    color: var(--accent);
    min-width: 75px;
  }

  .map-slider {
    width: 100%;
    accent-color: var(--accent);
    cursor: pointer;
  }

  .presets-row {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }

  .preset-pill {
    padding: 3px 8px;
    font-size: 11px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 4px;
    color: var(--ink-soft);
    cursor: pointer;
  }

  .preset-pill.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #ffffff;
  }

  .map-stage-wrapper {
    position: relative;
    isolation: isolate;
    width: 100%;
    height: 600px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: var(--shadow-md);
  }

  .leaflet-container-box {
    width: 100%;
    height: 100%;
    background: #e8eef3;
  }

  /* SVG paths receive mouse focus in Chromium; their native outline spans
     the country's entire bounding box. Retain the keyboard focus indicator. */
  :global(.atlas-base-land:focus:not(:focus-visible)) {
    outline: none;
  }

  /* Custom Leaflet Pin Styling */
  :global(.atlas-custom-pin-wrap) {
    background: transparent;
    border: none;
  }

  :global(.atlas-pin-node) {
    width: 16px;
    height: 16px;
    border-radius: 50%;
    position: relative;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  :global(.atlas-pin-node:hover),
  :global(.atlas-pin-node.selected) {
    transform: scale(1.4);
    z-index: 1000 !important;
  }

  :global(.atlas-pin-node .pin-dot) {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--pin-color, #b5651d);
    border: 2px solid #ffffff;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.35);
  }

  :global(.atlas-pin-node .pin-ring) {
    position: absolute;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    border: 1.5px solid var(--pin-color, #b5651d);
    opacity: 0.4;
    pointer-events: none;
  }

  :global(.atlas-pin-node.selected .pin-ring) {
    border-width: 2.5px;
    opacity: 0.9;
    animation: pulse 1.8s infinite;
  }

  @keyframes pulse {
    0% { transform: scale(1); opacity: 0.9; }
    50% { transform: scale(1.4); opacity: 0.2; }
    100% { transform: scale(1); opacity: 0.9; }
  }

  :global(.atlas-map-tooltip) {
    font-family: var(--font-sans);
    font-size: 12px;
    background: var(--surface-1);
    color: var(--ink);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px 8px;
    box-shadow: var(--shadow-sm);
  }

  /* Aktif Devlet Bilgi Kartı */
  .active-state-drawer {
    position: absolute;
    bottom: 20px;
    right: 20px;
    width: 330px;
    max-width: calc(100% - 40px);
    background: var(--surface-translucent);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid var(--border-strong);
    border-radius: 12px;
    padding: 14px 16px;
    box-shadow: var(--shadow-lg);
    z-index: 1000;
    max-height: calc(100% - 40px);
    overflow-y: auto;
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
    padding: 7px 12px;
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

  @media (max-width: 700px) {
    .map-stage-wrapper {
      height: 480px;
    }
    .active-state-drawer {
      bottom: 10px;
      right: 10px;
      left: 10px;
      width: auto;
      max-width: none;
    }
  }
</style>
