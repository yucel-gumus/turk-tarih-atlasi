<script lang="ts">
  import type { PositionedState } from '../../lib/data/atlas';
  import { yearLabel, REGION_MAP } from '../../lib/data/atlas';
  import { camera } from '../../lib/stores/camera.svelte';
  import { ui } from '../../lib/stores/ui.svelte';
  import RulerCard from './RulerCard.svelte';
  import { Landmark, Compass, Scroll } from '@lucide/svelte';

  let { item }: { item: PositionedState } = $props();
  const state = $derived(item.state);
  const region = $derived(REGION_MAP[state.region]);

  function openState() {
    ui.openStateDetail(state);
  }
</script>

<div
  class="state-group"
  id="state-{state.id}"
  style="
    left: {item.x}px;
    top: {item.y}px;
    width: {item.w}px;
    min-height: {item.h}px;
    --region-color: {region?.color || '#e0c48a'};
    --region-glow: {region?.glow || 'rgba(224, 196, 138, 0.2)'};
  "
>
  <!-- State Top Banner -->
  <div class="state-header" onclick={openState} role="button" tabindex="0" onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && openState()}>
    <div class="title-row">
      <div class="state-indicator" style="background: var(--region-color); box-shadow: 0 0 10px var(--region-glow);"></div>
      <h3 class="state-name">{state.name}</h3>
      {#if state.short && state.short !== state.name}
        <span class="state-short">({state.short})</span>
      {/if}

      <div class="dates-tag">
        {yearLabel(state.start)}&thinsp;–&thinsp;{yearLabel(state.end)}
      </div>

      {#if state.confidence && state.confidence !== 'kayit'}
        <span class="confidence-tag {state.confidence}">
          {state.confidence === 'tartismali' ? 'Tartışmalı' : 'Rivayet'}
        </span>
      {/if}
    </div>

    <!-- State metadata pills -->
    <div class="meta-pills">
      {#if state.capital}
        <span class="meta-pill">
          <Landmark size={12} />
          <span>{state.capital}</span>
        </span>
      {/if}

      {#if state.religion}
        <span class="meta-pill">
          <Compass size={12} />
          <span>{state.religion}</span>
        </span>
      {/if}

      {#if state.rulers && state.rulers.length > 0}
        <span class="meta-pill rulers-count">
          <span>{state.rulers.length} Hükümdar</span>
        </span>
      {/if}
    </div>

    {#if state.summary}
      <p class="state-summary">
        {state.summary}
      </p>
    {/if}
  </div>

  <!-- Rulers Grid: Visibility controlled by camera detail level -->
  {#if state.rulers && state.rulers.length > 0}
    <div
      class="rulers-grid"
      class:visible={camera.detailActive}
      style="
        grid-template-columns: repeat({item.cols}, minmax(280px, 1fr));
        opacity: {camera.detail};
      "
    >
      {#each state.rulers as ruler (ruler.id)}
        <RulerCard {ruler} {state} />
      {/each}
    </div>
  {:else if state.essay && state.essay.length > 0}
    <!-- Content card (e.g. Okuma rehberi) -->
    <div class="essay-box" class:visible={camera.detailActive} style="opacity: {camera.detail};">
      {#each state.essay as p}
        <p>{p}</p>
      {/each}
    </div>
  {/if}
</div>

<style>
  .state-group {
    position: absolute;
    background: rgba(14, 18, 23, 0.45);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-top: 2px solid var(--region-color);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35);
    contain: layout style;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .state-header {
    cursor: pointer;
    border-radius: 8px;
    padding: 6px 8px;
    margin: -6px -8px;
    transition: background 0.2s ease;
    outline: none;
  }

  .state-header:hover {
    background: rgba(255, 255, 255, 0.03);
  }

  .state-header:focus-visible {
    box-shadow: 0 0 0 2px var(--gold-primary);
  }

  .title-row {
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }

  .state-indicator {
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }

  .state-name {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 22px;
    font-weight: 700;
    color: var(--text-main);
    letter-spacing: -0.01em;
  }

  .state-short {
    font-size: 13px;
    color: var(--text-muted);
  }

  .dates-tag {
    margin-left: auto;
    font-family: var(--font-serif);
    font-size: 13px;
    font-weight: 600;
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.08);
    border: 1px solid rgba(229, 195, 120, 0.2);
    padding: 2px 8px;
    border-radius: 6px;
  }

  .confidence-tag {
    font-size: 10px;
    padding: 1px 6px;
    border-radius: 4px;
  }
  .confidence-tag.tartismali {
    background: rgba(251, 191, 36, 0.15);
    border: 1px solid rgba(251, 191, 36, 0.3);
    color: #fde047;
  }
  .confidence-tag.rivayet {
    background: rgba(168, 85, 247, 0.15);
    border: 1px solid rgba(168, 85, 247, 0.3);
    color: #d8b4fe;
  }

  .meta-pills {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
    flex-wrap: wrap;
  }

  .meta-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    padding: 3px 8px;
    border-radius: 6px;
  }

  .rulers-count {
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.08);
    font-weight: 600;
  }

  .state-summary {
    margin: 8px 0 0;
    font-size: 12px;
    color: var(--text-muted);
    line-height: 1.5;
  }

  .rulers-grid {
    display: grid;
    gap: 12px;
    transition: opacity 0.25s ease, visibility 0.25s ease;
    visibility: hidden;
    pointer-events: none;
  }

  .rulers-grid.visible {
    visibility: visible;
    pointer-events: auto;
  }

  .essay-box {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 16px;
    font-size: 13px;
    line-height: 1.7;
    color: var(--text-muted);
    visibility: hidden;
    pointer-events: none;
  }
  .essay-box.visible {
    visibility: visible;
    pointer-events: auto;
  }
</style>
