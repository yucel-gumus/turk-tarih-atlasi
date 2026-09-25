<script lang="ts">
  import { camera } from '../../lib/stores/camera.svelte';
  import { MIN_YEAR, MAX_YEAR, xOf, yearLabel } from '../../lib/data/atlas';

  const step = $derived(camera.scale < 0.12 ? 200 : 100);
  const startYear = $derived(Math.ceil(MIN_YEAR / step) * step);
  const endYear = $derived(Math.floor(MAX_YEAR / step) * step);

  const ticks = $derived.by(() => {
    const list: { year: number; sx: number }[] = [];
    let lastTick = -9999;
    for (let yr = startYear; yr <= endYear; yr += step) {
      const sx = camera.x + xOf(yr) * camera.scale;
      if (sx < -40 || sx > camera.viewportW + 40) continue;
      if (sx - lastTick < 68) continue;
      lastTick = sx;
      list.push({ year: yr, sx });
    }
    return list;
  });

  const rangeReadout = $derived(
    `${yearLabel(camera.visibleRange.startYear)} – ${yearLabel(camera.visibleRange.endYear)}`
  );
</script>

<footer class="timebar-root no-print">
  <!-- Legend hints -->
  <div class="legend-group glass-pill">
    <span class="legend-item"><b class="dot dot-win"></b> Zafer</span>
    <span class="legend-item"><b class="dot dot-loss"></b> Yenilgi</span>
    <span class="legend-item"><b class="dot dot-dispute"></b> Tartışmalı</span>
  </div>

  <!-- Visible Date Range Live Status -->
  <div class="range-badge glass-pill" aria-live="polite" aria-atomic="true">
    <span class="range-text">{rangeReadout}</span>
  </div>

  <!-- Interactive Ticks Line -->
  <div class="ticks-track" aria-hidden="true">
    {#each ticks as tick (tick.year)}
      <button
        type="button"
        tabindex="-1"
        class="tick-btn"
        style="left: {tick.sx}px;"
        onclick={() => camera.focusYear(tick.year)}
      >
        <span class="tick-line"></span>
        <span class="tick-label">{yearLabel(tick.year)}</span>
      </button>
    {/each}
  </div>
</footer>

<style>
  .timebar-root {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 48px;
    background: rgba(14, 18, 23, 0.78);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-top: 1px solid var(--border-glass);
    z-index: 45;
    display: flex;
    align-items: center;
    padding: 0 20px;
    overflow: hidden;
  }

  .legend-group {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 4px 12px;
    font-size: 11px;
    color: var(--text-muted);
    z-index: 2;
  }

  .legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }
  .dot-win { background: var(--accent-victory); box-shadow: 0 0 6px var(--accent-victory); }
  .dot-loss { background: var(--accent-defeat); box-shadow: 0 0 6px var(--accent-defeat); }
  .dot-dispute { background: var(--accent-stalemate); box-shadow: 0 0 6px var(--accent-stalemate); }

  .range-badge {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    padding: 4px 14px;
    font-family: var(--font-serif);
    font-size: 13px;
    font-weight: 700;
    color: var(--gold-primary);
    z-index: 2;
    letter-spacing: 0.02em;
  }

  .ticks-track {
    position: absolute;
    inset: 0;
    pointer-events: auto;
  }

  .tick-btn {
    position: absolute;
    top: 0;
    bottom: 0;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 4px;
    color: var(--text-dim);
    font-size: 10px;
    font-family: var(--font-serif);
    transition: color 0.15s ease;
  }

  .tick-btn:hover {
    color: var(--gold-primary);
  }

  .tick-line {
    width: 1px;
    height: 6px;
    background: var(--border-glass-bright);
    margin-bottom: 3px;
  }

  .tick-btn:hover .tick-line {
    background: var(--gold-primary);
    height: 10px;
  }
</style>
