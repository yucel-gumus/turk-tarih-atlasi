<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import type { RegionInfo } from '../../lib/data/atlas';
  import { yearLabel } from '../../lib/data/atlas';
  import TimelineBar from './TimelineBar.svelte';

  export interface Bar {
    state: State;
    left: number;
    width: number;
    top: number;
    height: number;
  }

  export interface Lane {
    info: RegionInfo;
    bars: Bar[];
    height: number;
  }

  let {
    surfaceWidth,
    headHeight,
    hoverX,
    hoverYear,
    isDragging,
    milestones,
    showMilestoneLabels,
    centuries,
    showCenturyLabels,
    lanes,
    onBarHover,
    onBarLeave,
  }: {
    surfaceWidth: number;
    headHeight: number;
    hoverX: number | null;
    hoverYear: number | null;
    isDragging: boolean;
    milestones: { year: number; label: string; left: number }[];
    showMilestoneLabels: boolean;
    centuries: { year: number; left: number; label: string }[];
    showCenturyLabels: boolean;
    lanes: Lane[];
    onBarHover: (state: State, pos: { clientX: number; clientY: number }) => void;
    onBarLeave: () => void;
  } = $props();
</script>

<div class="timeline-surface" style="width: {surfaceWidth}px">
  <!-- Canlı Kürsör Kılavuz Çizgisi -->
  {#if hoverX !== null && hoverYear !== null && !isDragging}
    <div class="hover-guideline" style="left: {hoverX}px;" aria-hidden="true">
      <span class="hover-year-pill">{yearLabel(hoverYear)}</span>
    </div>
  {/if}

  <div class="milestone-lines" aria-hidden="true">
    {#each milestones as m (m.year)}
      <span class="milestone-line" style="left: {m.left}px"></span>
    {/each}
  </div>

  <div class="head-rows" style="height: {headHeight}px">
    <div class="century-ruler">
      {#each centuries as c (c.year)}
        <span class="century-tick" style="left: {c.left}px">
          {#if showCenturyLabels}
            <span class="century-label">{c.label}</span>
          {/if}
        </span>
      {/each}
    </div>
    <div class="milestone-row">
      {#if showMilestoneLabels}
        {#each milestones as m (m.year)}
          <span class="milestone-label" style="left: {m.left}px">{m.label} · {yearLabel(m.year)}</span>
        {/each}
      {/if}
    </div>
  </div>

  <div class="lanes">
    {#each lanes as lane (lane.info.id)}
      <div class="lane" style="height: {lane.height}px">
        {#each lane.bars as bar (bar.state.id)}
          <TimelineBar
            state={bar.state}
            color={lane.info.color}
            left={bar.left}
            width={bar.width}
            top={bar.top}
            height={bar.height}
            onHover={onBarHover}
            onLeave={onBarLeave}
          />
        {/each}
      </div>
    {/each}
  </div>
</div>

<style>
  .timeline-surface {
    position: relative;
    padding-left: 8px;
  }

  /* Kürsör Kılavuz Çizgisi */
  .hover-guideline {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: var(--gold-primary);
    box-shadow: 0 0 8px var(--gold-glow);
    z-index: 8;
    pointer-events: none;
    transform: translateX(-50%);
  }

  .hover-year-pill {
    position: sticky;
    top: 2px;
    display: inline-block;
    transform: translateX(-50%);
    background: var(--accent);
    color: #ffffff;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 9999px;
    box-shadow: var(--shadow-sm);
    white-space: nowrap;
  }

  .milestone-lines {
    position: absolute;
    inset: 0;
    z-index: 0;
  }

  .milestone-line {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 1px;
    background: rgba(150, 96, 26, 0.16);
  }

  .head-rows {
    position: relative;
    z-index: 1;
  }

  .century-ruler {
    position: relative;
    height: 22px;
  }

  .century-tick {
    position: absolute;
    bottom: 0;
    width: 1px;
    height: 6px;
    background: var(--border-strong);
  }

  .century-label {
    position: absolute;
    bottom: 8px;
    left: 0;
    transform: translateX(-50%);
    font-size: 10px;
    color: var(--ink-dim);
    white-space: nowrap;
  }

  .milestone-row {
    position: relative;
    height: 18px;
  }

  .milestone-label {
    position: absolute;
    top: 2px;
    transform: translateX(-50%);
    font-size: 9px;
    color: var(--gold-primary);
    white-space: nowrap;
  }

  .lanes {
    position: relative;
    z-index: 1;
  }

  .lane {
    position: relative;
    border-bottom: 1px solid var(--border);
  }

  .lane:last-child {
    border-bottom: none;
  }
</style>
