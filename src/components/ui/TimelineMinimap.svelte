<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { DEVLET_REGIONS, yearLabel } from '../../lib/data/atlas';
  import Compass from '@lucide/svelte/icons/compass';

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

  let cachedTrackWidth = 0;
  let rafLensId: number | null = null;
  let pendingDeltaRatio = 0;

  /** Harita üzerinde tıklanan yıla atla */
  function handleTrackClick(e: MouseEvent) {
    if (isDraggingLens || !trackNode) return;
    // Lens bırakıldığında tarayıcı lens üzerinde click üretir ve bu track'e kabarır;
    // yoksayılmazsa sürükleme sonrası şerit tıklanan yıla geri sıçrar.
    if ((e.target as Element).closest('.viewport-lens')) return;
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
    cachedTrackWidth = trackNode.getBoundingClientRect().width || 1;
    pendingDeltaRatio = 0;
    (e.currentTarget as HTMLElement).setPointerCapture(e.pointerId);
  }

  function handleLensPointerMove(e: PointerEvent) {
    if (!isDraggingLens || cachedTrackWidth <= 0) return;
    const dx = e.clientX - startX;
    startX = e.clientX;
    pendingDeltaRatio += dx / cachedTrackWidth;
    if (rafLensId === null) {
      rafLensId = requestAnimationFrame(() => {
        rafLensId = null;
        if (pendingDeltaRatio !== 0) {
          onPanByRatio(pendingDeltaRatio);
          pendingDeltaRatio = 0;
        }
      });
    }
  }

  function handleLensPointerUp(e: PointerEvent) {
    if (!isDraggingLens) return;
    isDraggingLens = false;
    if (rafLensId !== null) {
      cancelAnimationFrame(rafLensId);
      rafLensId = null;
    }
    if (pendingDeltaRatio !== 0) {
      onPanByRatio(pendingDeltaRatio);
      pendingDeltaRatio = 0;
    }
    try {
      (e.currentTarget as HTMLElement).releasePointerCapture(e.pointerId);
    } catch {
      // Ignore if capture was already released
    }
  }
</script>

<div class="minimap-container no-print" role="group" aria-label="Zaman gezgini ve genel bakış">
  <div class="minimap-header">
    <div class="header-left">
      <span class="minimap-title">
        <Compass size={12} aria-hidden="true" />
        Zaman Gezgini
      </span>
      <span class="minimap-hint">Tarih ekseninde kaydırmak için sürükleyin</span>
    </div>
    <div class="header-right">
      <span class="visible-range">
        <span class="visible-range-label">Görünen:</span> <strong class="range-badge">{yearLabel(Math.round(viewportStartYear))} – {yearLabel(Math.round(viewportEndYear))}</strong>
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
    aria-valuetext={`${yearLabel(Math.round(viewportStartYear))} ile ${yearLabel(Math.round(viewportEndYear))} arası`}
    tabindex="0"
    onkeydown={(e) => {
      if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
      // Sayfanın global ok-tuşu kaydırması da tetiklenmesin (çift kaydırma).
      e.preventDefault();
      e.stopPropagation();
      onPanByRatio(e.key === 'ArrowLeft' ? -0.05 : 0.05);
    }}
  >
    <!-- Yüzyıl çizgileri -->
    {#each keyTicks as tick (tick.year)}
      <div class="track-tick" style="left: {tick.pct}%;">
        <span class="tick-label">{tick.label}</span>
      </div>
    {/each}

    <!-- 7 Bölgesel Mini Spektrogram Kulvarı -->
    <div class="density-bars" aria-hidden="true">
      {#each states as state (state.id)}
        {@const leftPct = ((state.start - bounds.min) / span) * 100}
        {@const widthPct = Math.max(0.4, ((state.end - state.start) / span) * 100)}
        {@const regionIndex = DEVLET_REGIONS.findIndex((r) => r.id === state.region)}
        {@const color = DEVLET_REGIONS[regionIndex]?.color ?? '#96601a'}
        {@const topPx = (regionIndex >= 0 ? regionIndex : 0) * 3.4 + 2}
        <span
          class="density-bar"
          style="left: {leftPct}%; width: {widthPct}%; top: {topPx}px; background-color: {color};"
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
      aria-hidden="true"
      title="Sürükleyerek şeridi kaydırın"
    >
      <div class="lens-border-l"></div>
      <div class="lens-grip" aria-hidden="true">
        <span></span>
        <span></span>
      </div>
      <div class="lens-border-r"></div>
    </div>
  </div>
</div>

<style>
  .minimap-container {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 6px 0 12px;
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
    gap: 8px;
  }

  .minimap-title {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-weight: 700;
    color: var(--ink);
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  .minimap-hint {
    color: var(--ink-dim);
    font-size: 11px;
  }

  .visible-range {
    color: var(--ink-muted);
    font-size: 11.5px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  .range-badge {
    color: var(--accent-strong);
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2px 7px;
    font-family: var(--font-serif);
    font-size: 12px;
    font-weight: 600;
    font-variant-numeric: tabular-nums;
  }

  .minimap-track {
    position: relative;
    height: 28px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 8px;
    cursor: pointer;
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(25, 23, 19, 0.05);
  }

  .track-tick {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--border-strong);
    pointer-events: none;
    z-index: 3;
    opacity: 0.7;
  }

  .tick-label {
    position: absolute;
    bottom: 2px;
    left: 4px;
    font-size: 9.5px;
    font-weight: 600;
    color: var(--ink-dim);
    white-space: nowrap;
    line-height: 1;
    padding: 1px 3px;
    border-radius: 3px;
    background: rgba(255, 255, 255, 0.75);
  }

  .density-bars {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 2;
  }

  .density-bar {
    position: absolute;
    height: 2px;
    border-radius: 1px;
    opacity: 0.85;
  }

  .viewport-lens {
    position: absolute;
    top: 0;
    bottom: 0;
    background: rgba(150, 96, 26, 0.14);
    border: 1.5px solid var(--accent);
    border-radius: 6px;
    cursor: grab;
    z-index: 10;
    transition: background 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 3px;
    box-shadow: 0 1px 5px rgba(150, 96, 26, 0.2);
  }

  .viewport-lens:hover {
    background: rgba(150, 96, 26, 0.22);
    border-color: var(--accent-strong);
    box-shadow: 0 2px 8px rgba(150, 96, 26, 0.28);
  }

  .viewport-lens.is-dragging {
    cursor: grabbing;
    background: rgba(150, 96, 26, 0.28);
    border-color: var(--accent-strong);
  }

  .lens-border-l,
  .lens-border-r {
    width: 2px;
    height: 12px;
    background: var(--accent-strong);
    border-radius: 1px;
    opacity: 0.7;
  }

  .lens-grip {
    display: flex;
    align-items: center;
    gap: 2px;
    opacity: 0.6;
  }

  .lens-grip span {
    width: 1px;
    height: 8px;
    background: var(--accent-strong);
    border-radius: 1px;
  }

  @media (max-width: 768px) {
    .minimap-hint {
      display: none;
    }
    .visible-range {
      font-size: 10.5px;
    }
    .range-badge {
      font-size: 11px;
      padding: 1px 5px;
    }
  }

  @media (max-width: 480px) {
    .visible-range-label {
      display: none;
    }
  }
</style>
