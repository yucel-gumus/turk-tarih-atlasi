<script lang="ts">
  import type { State } from '../../schemas/atlas.schema';
  import { yearLabel } from '../../lib/data/atlas';
  import { hrefState } from '../../lib/router/route';

  /** Etiketin sığması için gereken en kısa çubuk genişliği (taşma olmasın). */
  const LABEL_MIN_PX = 110;

  let {
    state,
    color,
    left,
    width,
    top,
    height,
    onHover,
    onLeave,
    onSelect,
  }: {
    state: State;
    color: string;
    left: number;
    width: number;
    top: number;
    height: number;
    onHover?: (state: State, pos: { clientX: number; clientY: number }) => void;
    onLeave?: () => void;
    onSelect?: (state: State) => void;
  } = $props();

  const rulerCount = $derived(state.rulers.length);
  const warCount = $derived(state.rulers.reduce((n, r) => n + r.wars.length, 0));
  const showsLabel = $derived(width >= LABEL_MIN_PX);
  const showsCompactLabel = $derived(width >= 38 && width < LABEL_MIN_PX);

  function handleMouse(e: MouseEvent) {
    onHover?.(state, { clientX: e.clientX, clientY: e.clientY });
  }

  function handleFocus(e: FocusEvent) {
    const el = e.currentTarget as HTMLElement;
    const rect = el.getBoundingClientRect();
    onHover?.(state, {
      clientX: rect.left + Math.min(rect.width / 2, 60),
      clientY: rect.top,
    });
  }
</script>

<!-- Çubuğun uzunluğu her zaman devletin gerçek süresidir. Etiket sığmadığında
     çubuk uzatılmaz; kimlik `title` ile okunur, etiket yakınlaşınca görünür. -->
<a
  class="timeline-bar"
  href={hrefState(state.id)}
  style="left: {left}px; width: {width}px; top: {top}px; height: {height}px; --bar-color: {color};"
  title="{state.name} ({yearLabel(state.start)} – {yearLabel(state.end)}) · {rulerCount} hükümdar · {warCount} savaş kaydı"
  aria-label={!showsLabel && !showsCompactLabel ? `${state.name} (${yearLabel(state.start)} – ${yearLabel(state.end)}), ${rulerCount} hükümdar, ${warCount} savaş kaydı` : undefined}
  onclick={(event) => { if (window.matchMedia('(pointer: coarse)').matches && onSelect) { event.preventDefault(); onSelect(state); } }}
  ondragstart={(e) => e.preventDefault()}
  onmouseenter={handleMouse}
  onmousemove={handleMouse}
  onmouseleave={() => onLeave?.()}
  onfocus={handleFocus}
  onblur={() => onLeave?.()}
>
  {#if showsLabel}
    <span class="bar-name">{state.name}</span>
    <span class="bar-meta">
      {yearLabel(state.start)} – {yearLabel(state.end)} · {rulerCount} hükümdar
      {#if warCount > 0}
        <span class="sr-only"> · {warCount} savaş kaydı</span>
      {/if}
    </span>
  {:else if showsCompactLabel}
    <span class="bar-name compact">{state.name}</span>
    <span class="sr-only"> ({yearLabel(state.start)} – {yearLabel(state.end)}), {rulerCount} hükümdar</span>
  {/if}
</a>

<style>
  .timeline-bar {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 2px;
    padding: 2px 6px 2px 7px;
    min-width: 24px;
    border-radius: 7px;
    overflow: hidden;
    white-space: nowrap;
    background: color-mix(in srgb, var(--bar-color) 13%, #ffffff);
    border: 1px solid color-mix(in srgb, var(--bar-color) 32%, transparent);
    box-shadow: inset 3.5px 0 0 0 var(--bar-color);
    transition: background 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
    user-select: none;
    -webkit-user-drag: none;
    outline: none;
  }

  .timeline-bar:hover,
  .timeline-bar:focus-visible {
    background: color-mix(in srgb, var(--bar-color) 24%, #ffffff);
    border-color: var(--bar-color);
    box-shadow: inset 3.5px 0 0 0 var(--bar-color), 0 4px 12px -2px color-mix(in srgb, var(--bar-color) 50%, transparent);
    transform: translateY(-1px);
    z-index: 5;
  }

  .timeline-bar:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
    z-index: 10;
  }

  .bar-name {
    font-size: 11px;
    font-weight: 700;
    color: var(--ink);
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.15;
  }

  .bar-name.compact {
    font-size: 10px;
    font-weight: 700;
    line-height: 1.1;
  }

  .bar-meta {
    font-size: 9.5px;
    font-weight: 500;
    color: var(--ink-muted);
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.15;
  }
</style>
