<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { REGION_MAP, yearLabel } from '../../lib/data/atlas';
  import { hrefState } from '../../lib/router/route';
  import SectionBox from './SectionBox.svelte';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';

  let { states }: { states: State[] } = $props();
</script>

<SectionBox id="devlet-listesi" title={`Devletler · ${states.length}`}>
  <div class="state-list">
    {#each states as state (state.id)}
      <a
        class="state-list-item"
        href={hrefState(state.id)}
        style="--state-color: {REGION_MAP[state.region]?.color ?? '#96601a'}"
      >
        <span class="state-list-top">
          <span class="state-list-name">{state.name}</span>
          <ChevronRight size={15} aria-hidden="true" />
        </span>
        <span class="state-list-meta">
          {yearLabel(state.start)} – {yearLabel(state.end)} · {state.rulers.length} hükümdar
        </span>
        <span class="state-list-summary">{state.summary}</span>
      </a>
    {/each}
  </div>
</SectionBox>

<style>
  .state-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 10px;
  }

  .state-list-item {
    display: flex;
    flex-direction: column;
    gap: 6px;
    min-width: 0;
    padding: 15px;
    border: 1px solid var(--border);
    border-left: 4px solid var(--state-color);
    border-radius: 12px;
    background: var(--surface-1);
    box-shadow: var(--shadow-sm);
    transition: background 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
  }

  .state-list-item:hover {
    background: color-mix(in srgb, var(--state-color) 4%, #ffffff);
    border-color: var(--state-color);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }

  .state-list-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 8px;
    color: var(--ink);
  }

  .state-list-name {
    font-family: var(--font-serif);
    font-size: 16px;
    font-weight: 600;
  }

  .state-list-meta {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent-strong);
  }

  .state-list-summary {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    overflow: hidden;
    font-size: 12.5px;
    line-height: 1.55;
    color: var(--ink-soft);
  }
</style>
