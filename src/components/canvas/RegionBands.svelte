<script lang="ts">
  import type { PositionedRegion } from '../../lib/data/atlas';

  let { regions, worldW }: { regions: PositionedRegion[]; worldW: number } = $props();
</script>

<div class="region-bands" aria-hidden="true">
  {#each regions as r (r.id)}
    <div
      class="region-band"
      style="
        top: {r.y}px;
        height: {r.h}px;
        width: {worldW - 48}px;
        --band-color: {r.color};
      "
    >
      <div class="band-tag" style="background: {r.color}18; border-color: {r.color}40; color: {r.color};">
        <span class="band-dot" style="background: {r.color};"></span>
        <span class="band-title">{r.name}</span>
      </div>
    </div>
  {/each}
</div>

<style>
  .region-bands {
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 0;
  }

  .region-band {
    position: absolute;
    left: 24px;
    border: 1px solid rgba(255, 255, 255, 0.04);
    border-left: 3px solid var(--band-color);
    background: linear-gradient(90deg, rgba(255, 255, 255, 0.012) 0%, transparent 40%);
    border-radius: 12px;
  }

  .band-tag {
    position: absolute;
    left: 16px;
    top: 14px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 4px 12px;
    border-radius: 9999px;
    border: 1px solid;
    font-family: var(--font-serif);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.02em;
    backdrop-filter: blur(8px);
  }

  .band-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }
</style>
