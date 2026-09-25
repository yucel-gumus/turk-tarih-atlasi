<script lang="ts">
  import { MILESTONES, MIN_YEAR, MAX_YEAR, xOf, yearLabel } from '../../lib/data/atlas';
  import { camera } from '../../lib/stores/camera.svelte';

  let { worldH }: { worldH: number } = $props();

  const centuries = $derived.by(() => {
    const list: number[] = [];
    const start = Math.ceil(MIN_YEAR / 100) * 100;
    for (let y = start; y <= MAX_YEAR; y += 100) {
      list.push(y);
    }
    return list;
  });
</script>

<div class="time-grid" aria-hidden="true">
  <!-- Century Vertical Grid Lines -->
  {#each centuries as yr (yr)}
    {@const x = xOf(yr)}
    <div class="grid-line" style="left: {x}px; height: {worldH}px;">
      <span class="century-label">{yearLabel(yr)}</span>
    </div>
  {/each}

  <!-- Historical Milestones (Flags / Pins) -->
  <div class="milestones-track" class:visible={camera.milestoneActive}>
    {#each MILESTONES as ms (ms.year + ms.label)}
      {@const mx = xOf(ms.year)}
      <div class="milestone-pin" style="left: {mx}px;">
        <div class="milestone-line" style="height: {worldH}px;"></div>
        <div class="milestone-badge">
          <span class="ms-year">{yearLabel(ms.year)}</span>
          <span class="ms-label">{ms.label}</span>
        </div>
      </div>
    {/each}
  </div>
</div>

<style>
  .time-grid {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 1;
  }

  .grid-line {
    position: absolute;
    top: 0;
    width: 1px;
    background: repeating-linear-gradient(
      to bottom,
      rgba(255, 255, 255, 0.05),
      rgba(255, 255, 255, 0.05) 6px,
      transparent 6px,
      transparent 12px
    );
  }

  .century-label {
    position: sticky;
    top: 56px;
    display: block;
    transform: translateX(-50%);
    font-family: var(--font-serif);
    font-size: 11px;
    font-weight: 600;
    color: var(--text-dim);
    background: var(--bg-deep);
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid rgba(255, 255, 255, 0.05);
  }

  .milestones-track {
    position: absolute;
    inset: 0;
    transition: opacity 0.3s ease;
    opacity: 0;
    visibility: hidden;
  }

  .milestones-track.visible {
    opacity: 1;
    visibility: visible;
  }

  .milestone-pin {
    position: absolute;
    top: 0;
  }

  .milestone-line {
    position: absolute;
    top: 0;
    left: 0;
    width: 1px;
    background: linear-gradient(
      to bottom,
      rgba(229, 195, 120, 0.45) 0%,
      rgba(229, 195, 120, 0.15) 30%,
      rgba(229, 195, 120, 0.02) 100%
    );
  }

  .milestone-badge {
    position: sticky;
    top: 86px;
    transform: translateX(-50%);
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    background: rgba(18, 24, 32, 0.92);
    border: 1px solid var(--border-glass-bright);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6), 0 0 12px var(--gold-glow);
    padding: 3px 8px;
    border-radius: 6px;
    white-space: nowrap;
    backdrop-filter: blur(8px);
  }

  .ms-year {
    font-size: 9px;
    font-weight: 700;
    color: var(--gold-primary);
  }

  .ms-label {
    font-family: var(--font-serif);
    font-size: 11px;
    font-weight: 600;
    color: var(--text-main);
  }
</style>
