<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { yearLabel } from '../../lib/data/atlas';
  import { hrefState } from '../../lib/router/route';

  /** Etiketin sığması için gereken en kısa çubuk genişliği. */
  const LABEL_MIN_PX = 90;

  let {
    state,
    color,
    left,
    width,
    top,
    height,
    onHover,
    onLeave,
  }: {
    state: State;
    color: string;
    left: number;
    width: number;
    top: number;
    height: number;
    onHover?: (state: State, e: MouseEvent) => void;
    onLeave?: () => void;
  } = $props();

  const rulerCount = $derived(state.rulers.length);
  const warCount = $derived(state.rulers.reduce((n, r) => n + r.wars.length, 0));
  const showsLabel = $derived(width >= LABEL_MIN_PX);

  function handleMouseEnter(e: MouseEvent) {
    onHover?.(state, e);
  }

  function handleMouseMove(e: MouseEvent) {
    onHover?.(state, e);
  }

  function handleMouseLeave() {
    onLeave?.();
  }
</script>

<!-- Çubuğun uzunluğu her zaman devletin gerçek süresidir. Etiket sığmadığında
     çubuk uzatılmaz; kimlik `title` ile okunur, etiket yakınlaşınca görünür. -->
<a
  class="timeline-bar"
  href={hrefState(state.id)}
  style="left: {left}px; width: {width}px; top: {top}px; height: {height}px; --bar-color: {color};"
  title="{state.name} ({yearLabel(state.start)} – {yearLabel(state.end)}) · {rulerCount} hükümdar · {warCount} savaş"
  ondragstart={(e) => e.preventDefault()}
  onmouseenter={handleMouseEnter}
  onmousemove={handleMouseMove}
  onmouseleave={handleMouseLeave}
>
  {#if showsLabel}
    <span class="bar-name">{state.name}</span>
    <span class="bar-meta">
      {yearLabel(state.start)} – {yearLabel(state.end)} · {rulerCount} hükümdar
    </span>
  {/if}
</a>

<style>
  .timeline-bar {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 1px;
    padding: 3px 7px;
    border-radius: 5px;
    overflow: hidden;
    white-space: nowrap;
    background: color-mix(in srgb, var(--bar-color) 34%, transparent);
    border: 1px solid color-mix(in srgb, var(--bar-color) 62%, transparent);
    transition: background 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
    user-select: none;
    -webkit-user-drag: none;
  }

  .timeline-bar:hover {
    background: color-mix(in srgb, var(--bar-color) 58%, transparent);
    border-color: var(--bar-color);
    box-shadow: 0 0 12px color-mix(in srgb, var(--bar-color) 40%, transparent);
    z-index: 5;
  }

  .bar-name {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-main);
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .bar-meta {
    font-size: 9px;
    color: var(--text-muted);
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>
