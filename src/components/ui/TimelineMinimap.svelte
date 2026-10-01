<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { DEVLET_REGIONS, yearLabel } from '../../lib/data/atlas';
  import { Compass } from '@lucide/svelte';

  let {
    bounds,
    states,
    viewportStartYear,
    viewportEndYear,
    onJumpToYear,
    onPanByRatio,
  }: {
    bounds: { min: number; max: number };
    states: State[];
    viewportStartYear: number;
    viewportEndYear: number;
    onJumpToYear: (year: number) => void;
    onPanByRatio: (ratioDelta: number) => void;
  } = $props();

  let trackNode = $state<HTMLDivElement | null>(null);
  let isDraggingLens = $state(false);
  let startX = 0;

  const span = $derived(Math.max(1, bounds.max - bounds.min));

  /** Önemli yüzyıl işaretleri */
  const keyTicks = $derived.by(() => {
    const ticks: { year: number; pct: number; label: string }[] = [];
    const step = 500;
    const start = Math.ceil(bounds.min / step) * step;
    for (let y = start; y <= bounds.max; y += step) {
      const pct = ((y - bounds.min) / span) * 100;
      ticks.push({ year: y, pct, label: yearLabel(y) });
    }
    return ticks;
  });

  /** Görüş penceresi konumu ve genişliği (%) */
  const lensLeftPct = $derived.by(() => {
    const raw = ((viewportStartYear - bounds.min) / span) * 100;
    return Math.max(0, Math.min(100, raw));
  });

  const lensWidthPct = $derived.by(() => {
    const raw = ((viewportEndYear - viewportStartYear) / span) * 100;
    return Math.max(1.5, Math.min(100 - lensLeftPct, raw));
  });

  /** Harita üzerinde tıklanan yıla atla */
  function handleTrackClick(e: MouseEvent) {
    if (isDraggingLens || !trackNode) return;
    const rect = trackNode.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const ratio = Math.max(0, Math.min(1, clickX / rect.width));
    const targetYear = Math.round(bounds.min + ratio * span);
    onJumpToYear(targetYear);
  }

  function handleLensPointerDown(e: PointerEvent) {
    e.stopPropagation();
    if (e.button !== 0 || !trackNode) return;
    isDraggingLens = true;
    startX = e.clientX;
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  }

  function handleLensPointerMove(e: PointerEvent) {
    if (!isDraggingLens || !trackNode) return;
    const dx = e.clientX - startX;
    startX = e.clientX;
    const rect = trackNode.getBoundingClientRect();
    const ratioDelta = dx / rect.width;
    onPanByRatio(ratioDelta);
  }

  function handleLensPointerUp(e: PointerEvent) {
    if (!isDraggingLens) return;
    isDraggingLens = false;
    try {
      (e.currentTarget as HTMLElement).releasePointerCapture(e.pointerId);
    } catch {
      // Ignore if capture was already released
    }
  }
</script>

<div class="minimap-container no-print" aria-label="Zaman gezgini ve genel bakış">
  <div class="minimap-header">
    <div class="header-left">
      <Compass size={13} color="var(--gold-primary)" aria-hidden="true" />
      <span class="minimap-title">Zaman Gezgini</span>
      <span class="minimap-hint">Haritaya tıklayarak veya görüş kutusunu sürükleyerek tarihte gezinin</span>
    </div>
    <div class="header-right">
      <span class="visible-range">
        Görünen: <strong>{yearLabel(Math.round(viewportStartYear))} – {yearLabel(Math.round(viewportEndYear))}</strong>
      </span>
    </div>
  </div>

  <div
    class="minimap-track"
    bind:this={trackNode}
    onclick={handleTrackClick}
    role="slider"
    aria-label="Tarih gezgini zaman ekseni"
    aria-valuemin={bounds.min}
    aria-valuemax={bounds.max}
    aria-valuenow={Math.round(viewportStartYear)}
    tabindex="0"
    onkeydown={(e) => {
      if (e.key === 'ArrowLeft') onPanByRatio(-0.05);
      if (e.key === 'ArrowRight') onPanByRatio(0.05);
    }}
  >
    <!-- Yüzyıl çizgileri -->
    {#each keyTicks as tick (tick.year)}
      <div class="track-tick" style="left: {tick.pct}%;">
        <span class="tick-label">{tick.label}</span>
      </div>
    {/each}

    <!-- Küçük devlet yoğunluğu çizgileri -->
    <div class="density-bars" aria-hidden="true">
      {#each states as state (state.id)}
        {@const leftPct = ((state.start - bounds.min) / span) * 100}
        {@const widthPct = Math.max(0.4, ((state.end - state.start) / span) * 100)}
        {@const color = DEVLET_REGIONS.find((r) => r.id === state.region)?.color ?? '#96601a'}
        <span
          class="density-bar"
          style="left: {leftPct}%; width: {widthPct}%; background-color: {color};"
        ></span>
      {/each}
    </div>

    <!-- Görüş Penceresi Kutusu (Draggable Lens) -->
    <div
      class="viewport-lens"
      class:is-dragging={isDraggingLens}
      style="left: {lensLeftPct}%; width: {lensWidthPct}%;"
      onpointerdown={handleLensPointerDown}
      onpointermove={handleLensPointerMove}
      onpointerup={handleLensPointerUp}
      onpointercancel={handleLensPointerUp}
      role="button"
      tabindex="-1"
      aria-label="Görüş penceresini sürükleyin"
      title="Sürükleyerek şeridi kaydırın"
    >
      <div class="lens-handle-left"></div>
      <div class="lens-center"></div>
      <div class="lens-handle-right"></div>
    </div>
  </div>
</div>

<style>
  .minimap-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 4px 0 12px;
    border-bottom: 1px solid var(--border);
    user-select: none;
  }

  .minimap-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .minimap-title {
    font-weight: 700;
    color: var(--ink);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
  }

  .minimap-hint {
    color: var(--ink-dim);
    font-size: 10.5px;
  }

  .visible-range {
    color: var(--ink-muted);
    font-size: 11.5px;
  }

  .visible-range strong {
    color: var(--ink);
    font-family: var(--font-serif);
  }

  .minimap-track {
    position: relative;
    height: 24px;
    background: var(--surface-2);
    border-radius: 99px;
    cursor: pointer;
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.04);
  }

  .track-tick {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--border-strong);
    pointer-events: none;
    z-index: 1;
  }

  .tick-label {
    position: absolute;
    bottom: 2px;
    left: 4px;
    font-size: 8.5px;
    font-weight: 600;
    color: var(--ink-dim);
    white-space: nowrap;
    opacity: 0.85;
  }

  .density-bars {
    position: absolute;
    inset: 4px 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    pointer-events: none;
    z-index: 2;
  }

  .density-bar {
    position: absolute;
    height: 4px;
    border-radius: 2px;
    opacity: 0.8;
  }

  .viewport-lens {
    position: absolute;
    top: 0;
    bottom: 0;
    background: var(--accent-soft);
    border: 1.5px solid var(--accent);
    border-radius: 99px;
    cursor: grab;
    z-index: 10;
    transition: background 0.15s ease, border-color 0.15s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 4px;
  }

  .viewport-lens:hover {
    background: rgba(150, 96, 26, 0.18);
    border-color: var(--accent-strong);
  }

  .viewport-lens.is-dragging {
    cursor: grabbing;
    background: rgba(150, 96, 26, 0.26);
  }

  .lens-handle-left,
  .lens-handle-right {
    width: 2px;
    height: 10px;
    background: var(--accent-strong);
    border-radius: 1px;
  }

  .lens-center {
    flex: 1;
    height: 100%;
  }

  @media (max-width: 768px) {
    .minimap-hint {
      display: none;
    }
  }
</style>
