<script lang="ts">
  import type { SearchItem, PositionedState } from '../../lib/data/atlas';
  import { camera } from '../../lib/stores/camera.svelte';
  import { ui } from '../../lib/stores/ui.svelte';
  import SearchSuggest from './SearchSuggest.svelte';
  import { ZoomIn, ZoomOut, Maximize2, BookOpen, Layers } from '@lucide/svelte';

  let { searchItems, states }: { searchItems: SearchItem[]; states: PositionedState[] } = $props();

  const ERAS = [
    { label: 'Hunlar', year: -209 },
    { label: 'Göktürkler', year: 552 },
    { label: 'Selçuklular', year: 1040 },
    { label: 'Beylikler', year: 1300 },
    { label: 'Osmanlı', year: 1453 },
  ];

  function onSliderInput(e: Event) {
    const target = e.target as HTMLInputElement;
    const t = Number(target.value) / 1000;
    const next = Math.exp(
      Math.log(camera.minScale) + t * (Math.log(camera.maxScale) - Math.log(camera.minScale))
    );
    camera.zoomAt(camera.viewportW / 2, camera.viewportH / 2, next);
  }

  const sliderVal = $derived.by(() => {
    const t =
      (Math.log(camera.scale) - Math.log(camera.minScale)) /
      (Math.log(camera.maxScale) - Math.log(camera.minScale));
    return Math.round(t * 1000);
  });
</script>

<header class="hud-root no-print">
  <!-- Brand & Subtitle -->
  <div class="brand-group">
    <div class="logo-mark">
      <div class="inner-circle"></div>
    </div>
    <div class="brand-titles">
      <h1 class="brand-title">TÜRK DEVLETLERİ ATLASI</h1>
      <p class="brand-subtitle">MÖ 220 Teoman'dan 1922 Vahdettin'e Kesintisiz Soyağacı ve Hükümdarlar</p>
    </div>
  </div>

  <!-- Quick Era Navigation Pills -->
  <div class="era-pills">
    {#each ERAS as era}
      <button
        type="button"
        class="era-pill"
        onclick={() => camera.focusYear(era.year)}
        aria-label="{era.label} dönemine atla"
      >
        <span>{era.label}</span>
      </button>
    {/each}
  </div>

  <!-- Global Autocomplete Search -->
  <SearchSuggest items={searchItems} {states} />

  <!-- Zoom & Viewport Controls -->
  <div class="controls-group">
    <div class="zoom-stepper glass-pill">
      <button
        type="button"
        class="icon-btn"
        onclick={() => camera.zoomAt(camera.viewportW / 2, camera.viewportH / 2, camera.scale / 1.25)}
        aria-label="Uzaklaş"
      >
        <ZoomOut size={15} />
      </button>

      <input
        id="zoomSlider"
        name="zoomSlider"
        type="range"
        min="0"
        max="1000"
        value={sliderVal}
        oninput={onSliderInput}
        class="zoom-slider"
        aria-label="Yakınlaştırma ölçeği"
      />

      <button
        type="button"
        class="icon-btn"
        onclick={() => camera.zoomAt(camera.viewportW / 2, camera.viewportH / 2, camera.scale * 1.25)}
        aria-label="Yakınlaş"
      >
        <ZoomIn size={15} />
      </button>
    </div>

    <!-- Fit to screen -->
    <button type="button" class="btn-fit glass-pill" onclick={() => camera.fit(true)} aria-label="Tüm atlası ekrana sığdır">
      <Maximize2 size={13} />
      <span>Tümü</span>
    </button>

    <!-- Index modal trigger -->
    <button
      type="button"
      class="btn-index glass-pill"
      onclick={() => ui.toggleIndex(true)}
      aria-expanded={ui.isIndexOpen}
      aria-haspopup="dialog"
    >
      <BookOpen size={14} />
      <span>Dizin</span>
    </button>

    <!-- Dynamic Zoom Scale Pill -->
    <div class="zoom-status glass-pill" aria-live="polite" aria-atomic="true">
      <span class="status-indicator"></span>
      <span class="zoom-text">{camera.zoomLabel}</span>
    </div>
  </div>
</header>

<style>
  .hud-root {
    position: fixed;
    top: 14px;
    left: 20px;
    right: 20px;
    height: 58px;
    background: rgba(14, 18, 23, 0.72);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    padding: 0 18px;
    display: flex;
    align-items: center;
    gap: 16px;
    z-index: 50;
    box-shadow: 0 16px 36px -6px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.08);
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .logo-mark {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: linear-gradient(135deg, #e5c378 0%, #b88628 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 14px var(--gold-glow);
  }

  .inner-circle {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    border: 2px solid #080a0d;
  }

  .brand-title {
    margin: 0;
    font-family: var(--font-display);
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.06em;
    background: linear-gradient(180deg, #ffffff 20%, #e5c378 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.15;
  }

  .brand-subtitle {
    margin: 2px 0 0;
    font-size: 10px;
    color: var(--text-dim);
    letter-spacing: 0.01em;
  }

  .era-pills {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-left: 8px;
  }

  .era-pill {
    font-size: 11px;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 4px 10px;
    border-radius: 9999px;
    transition: all 0.2s ease;
  }

  .era-pill:hover {
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.1);
    border-color: rgba(229, 195, 120, 0.25);
  }

  .controls-group {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .zoom-stepper {
    display: flex;
    align-items: center;
    padding: 2px 6px;
    gap: 4px;
  }

  .icon-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    color: var(--text-muted);
    transition: all 0.2s ease;
  }

  .icon-btn:hover {
    color: var(--gold-primary);
    background: rgba(255, 255, 255, 0.08);
  }

  .zoom-slider {
    width: 80px;
    height: 4px;
    accent-color: var(--gold-primary);
    cursor: pointer;
  }

  .btn-fit, .btn-index {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-main);
  }

  .zoom-status {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    font-size: 11px;
    color: var(--text-muted);
  }

  .status-indicator {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: var(--gold-primary);
    box-shadow: 0 0 8px var(--gold-glow);
  }

  .zoom-text {
    white-space: nowrap;
  }
</style>
