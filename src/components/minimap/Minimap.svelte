<script lang="ts">
  import { onMount } from 'svelte';
  import { camera } from '../../lib/stores/camera.svelte';
  import type { AtlasLayout } from '../../lib/data/atlas';

  let { layout }: { layout: AtlasLayout } = $props();

  let canvasEl: HTMLCanvasElement | null = null;
  const MAP_W = 200;
  const MAP_H = 120;

  function draw() {
    if (!canvasEl) return;
    const ctx = canvasEl.getContext('2d');
    if (!ctx) return;

    ctx.clearRect(0, 0, MAP_W, MAP_H);

    // Background base
    ctx.fillStyle = '#0c1015';
    ctx.fillRect(0, 0, MAP_W, MAP_H);

    const scaleX = MAP_W / layout.worldW;
    const scaleY = MAP_H / layout.worldH;

    // Draw region horizontal indicators
    for (const r of layout.regions) {
      ctx.fillStyle = `${r.color}33`;
      ctx.fillRect(4, r.y * scaleY, MAP_W - 8, Math.max(2, r.h * scaleY));
    }

    // Draw state dots/blocks
    for (const s of layout.states) {
      ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
      ctx.fillRect(s.x * scaleX, s.y * scaleY, Math.max(2, s.w * scaleX), Math.max(2, s.h * scaleY));
    }

    // Draw viewport radar rectangle
    const vx = (-camera.x / camera.scale) * scaleX;
    const vy = (-camera.y / camera.scale) * scaleY;
    const vw = (camera.viewportW / camera.scale) * scaleX;
    const vh = (camera.viewportH / camera.scale) * scaleY;

    ctx.strokeStyle = '#e5c378';
    ctx.lineWidth = 1.5;
    ctx.strokeRect(vx, vy, vw, vh);

    ctx.fillStyle = 'rgba(229, 195, 120, 0.15)';
    ctx.fillRect(vx, vy, vw, vh);
  }

  $effect(() => {
    // Re-draw whenever camera values change
    const _ = [camera.x, camera.y, camera.scale, camera.viewportW, camera.viewportH];
    draw();
  });

  function onMapClick(e: MouseEvent) {
    const rect = canvasEl?.getBoundingClientRect();
    if (!rect) return;
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;

    const targetWorldX = (mx / MAP_W) * layout.worldW;
    const targetWorldY = (my / MAP_H) * layout.worldH;

    const targetX = camera.viewportW / 2 - targetWorldX * camera.scale;
    const targetY = camera.viewportH / 2 - targetWorldY * camera.scale;

    camera.flyTo(targetX, targetY, camera.scale, 350);
  }

  onMount(() => {
    draw();
  });
</script>

<!-- svelte-ignore a11y_click_events_have_key_events -->
<div class="minimap-container glass-panel no-print" onclick={onMapClick} role="button" tabindex="0" aria-label="Küçük radar harita">
  <canvas bind:this={canvasEl} width={MAP_W} height={MAP_H}></canvas>
  <div class="map-label">RADAR</div>
</div>

<style>
  .minimap-container {
    position: fixed;
    bottom: 44px;
    right: 20px;
    width: 200px;
    height: 120px;
    border-radius: 12px;
    overflow: hidden;
    z-index: 40;
    cursor: crosshair;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }

  .minimap-container:hover {
    transform: scale(1.04);
    border-color: var(--border-glass-bright);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6), 0 0 16px var(--gold-glow);
  }

  canvas {
    display: block;
    width: 100%;
    height: 100%;
  }

  .map-label {
    position: absolute;
    bottom: 4px;
    right: 6px;
    font-size: 8px;
    font-weight: 700;
    color: var(--text-dim);
    letter-spacing: 0.1em;
    pointer-events: none;
  }
</style>
