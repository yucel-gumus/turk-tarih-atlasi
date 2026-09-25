<script lang="ts">
  import { onMount } from 'svelte';
  import { loadAllStates, computeLayout, buildSearchIndex } from './lib/data/atlas';
  import { camera } from './lib/stores/camera.svelte';
  import { ui } from './lib/stores/ui.svelte';
  import Viewport from './components/canvas/Viewport.svelte';
  import HUD from './components/hud/HUD.svelte';
  import DetailDrawer from './components/drawer/DetailDrawer.svelte';
  import IndexModal from './components/hud/IndexModal.svelte';
  import Minimap from './components/minimap/Minimap.svelte';
  import TimebarScrubber from './components/timebar/TimebarScrubber.svelte';

  const states = loadAllStates();
  const layout = computeLayout(states);
  const searchItems = buildSearchIndex(states);

  function onGlobalKeyDown(e: KeyboardEvent) {
    const isInput = (e.target as HTMLElement)?.closest('input, textarea, select, [contenteditable="true"]');
    const isButton = (e.target as HTMLElement)?.closest('button, [role="button"]');
    const inDialog = (e.target as HTMLElement)?.closest('[role="dialog"]');

    if (e.key === 'Escape') {
      if (ui.isIndexOpen) {
        ui.toggleIndex(false);
        return;
      }
      if (ui.isDetailDrawerOpen) {
        ui.closeDetail();
        return;
      }
      return;
    }

    // Do not hijack typing or button interactions
    if (isInput || isButton || inDialog) return;

    const step = e.shiftKey ? 180 : 90;
    if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', '+', '=', '-', '_', '0'].includes(e.key)) {
      e.preventDefault();
    }

    if (e.key === 'ArrowLeft') camera.panBy(step, 0);
    if (e.key === 'ArrowRight') camera.panBy(-step, 0);
    if (e.key === 'ArrowUp') camera.panBy(0, step);
    if (e.key === 'ArrowDown') camera.panBy(0, -step);
    if (e.key === '+' || e.key === '=') {
      camera.zoomAt(camera.viewportW / 2, camera.viewportH / 2, camera.scale * 1.25);
    }
    if (e.key === '-' || e.key === '_') {
      camera.zoomAt(camera.viewportW / 2, camera.viewportH / 2, camera.scale / 1.25);
    }
    if (e.key === '0') {
      camera.fit(true);
    }
  }
</script>

<svelte:window onkeydown={onGlobalKeyDown} />

<div class="atlas-app" inert={ui.isIndexOpen ? true : undefined}>
  <!-- Top Global Header -->
  <HUD {searchItems} states={layout.states} />

  <!-- Infinite Canvas Viewport -->
  <Viewport {layout} />

  <!-- Radar Minimap -->
  <Minimap {layout} />

  <!-- Bottom Timeline Scrubber -->
  <TimebarScrubber />
</div>

<!-- Slide-over Drawer for Rulers & States -->
<DetailDrawer />

<!-- Comprehensive Full Index Modal Dialog -->
<IndexModal states={layout.states} />

<style>
  .atlas-app {
    position: fixed;
    inset: 0;
    overflow: hidden;
  }
</style>
