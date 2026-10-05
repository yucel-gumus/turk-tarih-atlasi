<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { DEVLET_REGIONS, yearLabel } from '../../lib/data/atlas';
  import Crown from '@lucide/svelte/icons/crown';
  import Swords from '@lucide/svelte/icons/swords';
  import Landmark from '@lucide/svelte/icons/landmark';
  import ArrowRight from '@lucide/svelte/icons/arrow-right';

  let {
    state,
    x = 0,
    y = 0,
    visible = false,
  }: {
    state: State | null;
    x: number;
    y: number;
    visible: boolean;
  } = $props();

  const regionInfo = $derived(
    state ? DEVLET_REGIONS.find((r) => r.id === state.region) : null
  );

  const durationYears = $derived(
    state ? Math.max(1, state.end - state.start) : 0
  );

  const rulerCount = $derived(state ? state.rulers.length : 0);
  const warCount = $derived(
    state ? state.rulers.reduce((acc, r) => acc + r.wars.length, 0) : 0
  );
</script>

{#if visible && state}
  <div
    class="timeline-tooltip glass-panel"
    style="left: {x}px; top: {y}px;"
    role="tooltip"
    aria-hidden={!visible}
  >
    <div class="tooltip-header">
      <div class="header-main">
        <span
          class="region-dot"
          style="background: {regionInfo?.color ?? '#96601a'}"
        ></span>
        <span class="state-name">{state.name}</span>
      </div>
      {#if regionInfo}
        <span class="region-badge" style="color: {regionInfo.color}">
          {regionInfo.name}
        </span>
      {/if}
    </div>

    <div class="tooltip-dates">
      <span class="date-range">
        {yearLabel(state.start)} – {yearLabel(state.end)}
      </span>
      <span class="duration-pill">{durationYears} yıl</span>
    </div>

    <div class="tooltip-stats">
      <span class="stat-item" title="Hükümdar sayısı">
        <Crown size={12} class="icon-ruler" aria-hidden="true" />
        {rulerCount} hükümdar
      </span>
      <span class="stat-item" title="Kayıtlı savaş sayısı">
        <Swords size={12} class="icon-war" aria-hidden="true" />
        {warCount} savaş
      </span>
      {#if state.capital}
        <span class="stat-item capital" title="Başkent">
          <Landmark size={12} class="icon-state" aria-hidden="true" />
          {state.capital}
        </span>
      {/if}
    </div>

    {#if state.summary}
      <p class="tooltip-summary">{state.summary}</p>
    {/if}

    <div class="tooltip-footer">
      <span>Devlet sayfasına git</span>
      <ArrowRight size={11} aria-hidden="true" />
    </div>
  </div>
{/if}

<style>
  .timeline-tooltip {
    position: fixed;
    z-index: 1000;
    pointer-events: none;
    transform: translate(14px, 14px);
    width: 280px;
    max-width: calc(100vw - 32px);
    padding: 12px 14px;
    border-radius: 12px;
    background: var(--surface-1);
    border: 1px solid var(--border-strong);
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    gap: 8px;
    user-select: none;
    animation: tooltip-fade-in 0.12s ease-out;
  }

  @keyframes tooltip-fade-in {
    from {
      opacity: 0;
      transform: translate(14px, 18px) scale(0.96);
    }
    to {
      opacity: 1;
      transform: translate(14px, 14px) scale(1);
    }
  }

  .tooltip-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 8px;
  }

  .header-main {
    display: flex;
    align-items: center;
    gap: 7px;
    min-width: 0;
  }

  .region-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .state-name {
    font-family: var(--font-serif);
    font-size: 14px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.25;
  }

  .region-badge {
    font-size: 9px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    background: var(--surface-2);
    padding: 2px 6px;
    border-radius: 5px;
    white-space: nowrap;
  }

  .tooltip-dates {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 11px;
  }

  .date-range {
    color: var(--accent-strong);
    font-weight: 600;
    font-family: var(--font-serif);
  }

  .duration-pill {
    font-size: 10px;
    color: var(--ink-dim);
    background: var(--surface-2);
    padding: 1px 7px;
    border-radius: 9999px;
  }

  .tooltip-stats {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    padding: 7px 0;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
  }

  .stat-item {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 10px;
    color: var(--ink-muted);
  }

  .stat-item.capital {
    color: var(--accent-strong);
  }

  .tooltip-summary {
    margin: 0;
    font-size: 11px;
    line-height: 1.45;
    color: var(--ink-muted);
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    overflow: hidden;
  }

  .tooltip-footer {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 4px;
    font-size: 10px;
    color: var(--accent-strong);
    font-weight: 600;
  }
</style>
