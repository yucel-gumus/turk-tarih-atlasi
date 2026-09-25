<script lang="ts">
  import { onMount } from 'svelte';
  import { camera } from '../../lib/stores/camera.svelte';
  import { clamp, type AtlasLayout } from '../../lib/data/atlas';
  import RegionBands from './RegionBands.svelte';
  import TimeGrid from './TimeGrid.svelte';
  import StateGroup from './StateGroup.svelte';

  let { layout }: { layout: AtlasLayout } = $props();

  let viewportEl = $state<HTMLElement | null>(null);

  // Dragging state
  let isDragging = false;
  let startX = 0;
  let startY = 0;
  let lastX = 0;
  let lastY = 0;
  let touchStartDist = 0;
  let touchStartScale = 1;

  function onPointerDown(e: PointerEvent) {
    if ((e.target as HTMLElement)?.closest('button, a, input, textarea, .ruler-card, .state-header')) {
      return;
    }
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
    lastX = e.clientX;
    lastY = e.clientY;
    viewportEl?.setPointerCapture(e.pointerId);
  }

  function onPointerMove(e: PointerEvent) {
    if (!isDragging) return;
    const dx = e.clientX - lastX;
    const dy = e.clientY - lastY;
    lastX = e.clientX;
    lastY = e.clientY;
    camera.panBy(dx, dy);
  }

  function onPointerUp(e: PointerEvent) {
    if (!isDragging) return;
    isDragging = false;
    try {
      viewportEl?.releasePointerCapture(e.pointerId);
    } catch {
      // ignore
    }
  }

  function onWheel(e: WheelEvent) {
    e.preventDefault();
    if ((e.target as HTMLElement)?.closest('input, textarea, .ix-body, .drawer-content')) {
      return;
    }
    const rect = viewportEl?.getBoundingClientRect();
    if (!rect) return;

    const dy = e.deltaMode === 1 ? e.deltaY * 16 : e.deltaMode === 2 ? e.deltaY * rect.height : e.deltaY;
    const capped = clamp(dy, -90, 90);
    const strength = e.ctrlKey ? 0.01 : 0.0018;

    const sx = clamp(e.clientX - rect.left, 0, rect.width);
    const sy = clamp(e.clientY - rect.top, 0, rect.height);

    const nextScale = camera.scale * Math.exp(-capped * strength);
    camera.zoomAt(sx, sy, nextScale);
  }

  // Touch pinch support
  function onTouchStart(e: TouchEvent) {
    if (e.touches.length === 2) {
      const dx = e.touches[0].clientX - e.touches[1].clientX;
      const dy = e.touches[0].clientY - e.touches[1].clientY;
      touchStartDist = Math.hypot(dx, dy);
      touchStartScale = camera.scale;
    }
  }

  function onTouchMove(e: TouchEvent) {
    if (e.touches.length === 2 && touchStartDist > 0) {
      e.preventDefault();
      const dx = e.touches[0].clientX - e.touches[1].clientX;
      const dy = e.touches[0].clientY - e.touches[1].clientY;
      const dist = Math.hypot(dx, dy);
      const ratio = dist / touchStartDist;
      const midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      camera.zoomAt(midX, midY, touchStartScale * ratio);
    }
  }

  onMount(() => {
    const handleResize = () => {
      if (viewportEl) {
        camera.updateDimensions(
          viewportEl.clientWidth,
          viewportEl.clientHeight,
          layout.worldW,
          layout.worldH
        );
      }
    };

    handleResize();
    camera.fit(false);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  });
</script>

<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<main
  bind:this={viewportEl}
  class="viewport-root"
  onpointerdown={onPointerDown}
  onpointermove={onPointerMove}
  onpointerup={onPointerUp}
  onwheel={onWheel}
  ontouchstart={onTouchStart}
  ontouchmove={onTouchMove}
  aria-label="Tarih atlası görsel tuvali"
>
  <div
    class="world-plane"
    style="
      width: {layout.worldW}px;
      height: {layout.worldH}px;
      transform: translate3d({camera.x}px, {camera.y}px, 0) scale({camera.scale});
    "
  >
    <!-- Background Region Bands -->
    <RegionBands regions={layout.regions} worldW={layout.worldW} />

    <!-- Century Lines & Historical Milestones -->
    <TimeGrid worldH={layout.worldH} />

    <!-- States & Rulers Layer -->
    <div class="states-layer">
      {#each layout.states as item (item.state.id)}
        <StateGroup {item} />
      {/each}
    </div>
  </div>
</main>

<style>
  .viewport-root {
    position: fixed;
    inset: 0;
    overflow: hidden;
    cursor: grab;
    touch-action: none;
    z-index: 1;
  }

  .viewport-root:active {
    cursor: grabbing;
  }

  .world-plane {
    position: absolute;
    left: 0;
    top: 0;
    transform-origin: 0 0;
    will-change: transform;
    pointer-events: auto;
  }

  .states-layer {
    position: absolute;
    inset: 0;
    z-index: 2;
  }
</style>
