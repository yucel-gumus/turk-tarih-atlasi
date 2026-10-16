<script lang="ts">
  import { onMount } from 'svelte';
  import { buildTree, REGION_COLORS, spanLabel, getState, type TreeNode } from '../lib/data/atlas';
  import { layoutTree, edgePath, NODE_W, NODE_H, type Placed } from '../lib/tree/layout';
  import { modals } from '../lib/modals.svelte';

  const { root } = buildTree();
  const layout = layoutTree(root);
  const edges = layout.placed
    .filter((p) => p.node.parent)
    .map((p) => ({ from: layout.byId.get(p.node.parent!.id)!, to: p }));

  let viewport: HTMLDivElement;
  let scale = $state(0.9);
  let tx = $state(0);
  let ty = $state(0);

  const MAX = 2;
  /** En uzak görünüm: ağacın tamamı ekrana sığar. */
  function minScale() {
    const r = viewport.getBoundingClientRect();
    return Math.min(0.3, Math.min(r.width / layout.width, r.height / layout.height) * 0.9);
  }

  function color(node: TreeNode): string {
    return node.region ? REGION_COLORS[node.region] : 'var(--ink-muted)';
  }

  function rulerCount(node: TreeNode): number {
    return node.kind === 'state' ? (getState(node.id)?.rulers.length ?? 0) : 0;
  }

  /** Ağacın ekrandan tamamen kaçmasını engeller: her zaman bir kısmı görünür kalır. */
  function clamp() {
    const r = viewport.getBoundingClientRect();
    const keep = 160;
    tx = Math.min(r.width - keep, Math.max(keep - layout.width * scale, tx));
    ty = Math.min(r.height - keep, Math.max(keep - layout.height * scale, ty));
  }

  function zoomAt(factor: number, cx: number, cy: number) {
    const next = Math.min(MAX, Math.max(minScale(), scale * factor));
    const k = next / scale;
    tx = cx - (cx - tx) * k;
    ty = cy - (cy - ty) * k;
    scale = next;
    clamp();
  }

  function focusOn(p: Placed) {
    const r = viewport.getBoundingClientRect();
    tx = r.width / 2 - (p.x + NODE_W / 2) * scale;
    ty = r.height / 2 - (p.y + NODE_H / 2) * scale;
    clamp();
  }

  function start() {
    const r = viewport.getBoundingClientRect();
    const s = r.width < 700 ? 0.72 : 0.9;
    const p = layout.byId.get(root.id)!;
    scale = s;
    tx = r.width / 2 - (p.x + NODE_W / 2) * s;
    ty = (r.width < 700 ? 120 : 104) - (p.y - 20) * s;
  }

  onMount(start);

  /* ---- fare ve dokunma: sürükle, tekerlek/kıstırma, çift tık/çift dokunma ---- */
  const pointers = new Map<number, { x: number; y: number }>();
  let dragStart: { x: number; y: number; tx: number; ty: number } | null = null;
  let pinch: { dist: number; scale: number } | null = null;
  let moved = false;
  let lastTap = { time: 0, x: 0, y: 0 };

  function local(e: { clientX: number; clientY: number }) {
    const r = viewport.getBoundingClientRect();
    return { x: e.clientX - r.left, y: e.clientY - r.top };
  }

  function onPointerDown(e: PointerEvent) {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 1) {
      moved = false;
      dragStart = { x: e.clientX, y: e.clientY, tx, ty };
    }
    if (pointers.size === 2) {
      const [a, b] = [...pointers.values()];
      pinch = { dist: Math.hypot(a.x - b.x, a.y - b.y), scale };
      dragStart = null;
      moved = true;
    }
  }

  function onPointerMove(e: PointerEvent) {
    if (!pointers.has(e.pointerId)) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pinch && pointers.size === 2) {
      const [a, b] = [...pointers.values()];
      const dist = Math.hypot(a.x - b.x, a.y - b.y);
      const mid = local({ clientX: (a.x + b.x) / 2, clientY: (a.y + b.y) / 2 });
      zoomAt((pinch.scale * dist) / pinch.dist / scale, mid.x, mid.y);
      return;
    }
    if (!dragStart) return;
    const dx = e.clientX - dragStart.x;
    const dy = e.clientY - dragStart.y;
    if (!moved && Math.hypot(dx, dy) < 6) return;
    if (!moved) viewport.setPointerCapture(e.pointerId);
    moved = true;
    tx = dragStart.tx + dx;
    ty = dragStart.ty + dy;
    clamp();
  }

  function onPointerUp(e: PointerEvent) {
    if (!pointers.has(e.pointerId)) return;
    pointers.delete(e.pointerId);
    if (pointers.size < 2) pinch = null;
    if (pointers.size === 1) {
      // Kıstırmadan kalan parmakla kaydırmaya sorunsuz devam et.
      const [p] = [...pointers.values()];
      dragStart = { x: p.x, y: p.y, tx, ty };
    }
    if (pointers.size === 0) {
      dragStart = null;
      // Dokunmatikte boş alana çift dokunma: oraya yakınlaş.
      if (e.pointerType !== 'mouse' && !moved && !(e.target as Element).closest('.node')) {
        const now = performance.now();
        if (now - lastTap.time < 320 && Math.hypot(e.clientX - lastTap.x, e.clientY - lastTap.y) < 30) {
          const p = local(e);
          zoomAt(1.8, p.x, p.y);
          lastTap.time = 0;
        } else lastTap = { time: now, x: e.clientX, y: e.clientY };
      }
    }
  }

  /** Tekerlek: imlecin bulunduğu noktaya yakınlaş/uzaklaş (dokunmatik yüzeyde kıstırma da). */
  function onWheel(e: WheelEvent) {
    e.preventDefault();
    const p = local(e);
    const delta = e.deltaMode === 1 ? e.deltaY * 16 : e.deltaY;
    zoomAt(Math.exp(-delta * (e.ctrlKey ? 0.01 : 0.0015)), p.x, p.y);
  }

  /** Fareyle boş alana çift tıklama: oraya yakınlaş. */
  function onDblClick(e: MouseEvent) {
    if ((e.target as Element).closest('.node')) return;
    const p = local(e);
    zoomAt(1.8, p.x, p.y);
  }

  function openNode(e: MouseEvent, node: TreeNode) {
    if (moved) {
      e.preventDefault();
      return;
    }
    modals.open(node.kind === 'state' ? { kind: 'state', id: node.id } : { kind: 'context', id: node.id });
  }

  /** Klavyeyle (Tab) odaklanan düğüm görünür alanın dışındaysa ona kay; fare tıklaması görünümü oynatmaz. */
  function onNodeFocus(e: FocusEvent, p: Placed) {
    if (!(e.currentTarget as Element).matches(':focus-visible')) return;
    const r = viewport.getBoundingClientRect();
    const x = p.x * scale + tx;
    const y = p.y * scale + ty;
    if (x < 0 || y < 0 || x + NODE_W * scale > r.width || y + NODE_H * scale > r.height) focusOn(p);
  }
</script>

<!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
<div
  class="viewport"
  bind:this={viewport}
  role="application"
  aria-label="Türk devletleri soy ağacı. Sürükleyerek gezin, tekerlek veya iki parmakla yakınlaşın, bir devlete tıklayarak ayrıntısını açın."
  onpointerdown={onPointerDown}
  onpointermove={onPointerMove}
  onpointerup={onPointerUp}
  onpointercancel={onPointerUp}
  onwheel={onWheel}
  ondblclick={onDblClick}
>
  <div
    class="layer"
    style:width="{layout.width}px"
    style:height="{layout.height}px"
    style:transform="translate({tx}px, {ty}px) scale({scale})"
  >
    <svg width={layout.width} height={layout.height} aria-hidden="true">
      {#each edges as e (e.to.node.id)}
        <path d={edgePath(e.from, e.to)} class="edge" />
      {/each}
    </svg>

    {#each layout.placed as p (p.node.id)}
      <button
        type="button"
        class="node"
        class:context={p.node.kind === 'context'}
        class:modern={p.node.ongoing}
        style:left="{p.x}px"
        style:top="{p.y}px"
        style:width="{NODE_W}px"
        style:height="{NODE_H}px"
        style:--c={color(p.node)}
        data-id={p.node.id}
        onclick={(e) => openNode(e, p.node)}
        onfocus={(e) => onNodeFocus(e, p)}
      >
        <span class="name">{p.node.short}</span>
        <span class="years">
          {spanLabel(p.node.start, p.node.end, p.node.ongoing)}
          {#if rulerCount(p.node)}<span class="count"> · {rulerCount(p.node)} {p.node.ongoing ? 'lider' : 'hükümdar'}</span>{/if}
        </span>
      </button>
    {/each}
  </div>
</div>

<header class="title">
  <h1>Türk Devletleri Soy Ağacı</h1>
  <p class="hint-mouse">Sürükleyin · tekerlekle yakınlaşın · bir devlete tıklayın</p>
  <p class="hint-touch">Kaydırın · iki parmakla yakınlaşın · bir devlete dokunun</p>
</header>


<style>
  .viewport {
    position: fixed;
    inset: 0;
    overflow: hidden;
    touch-action: none;
    cursor: grab;
    background-color: var(--paper);
    user-select: none;
    -webkit-user-select: none;
  }
  .viewport:active {
    cursor: grabbing;
  }
  .layer {
    position: absolute;
    left: 0;
    top: 0;
    transform-origin: 0 0;
    will-change: transform;
  }
  svg {
    position: absolute;
    inset: 0;
    overflow: visible;
  }
  .edge {
    fill: none;
    stroke: var(--edge);
    stroke-width: 2;
  }

  .node {
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1px;
    padding: 6px 12px 6px 16px;
    text-align: left;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
    box-shadow: var(--shadow);
    cursor: pointer;
    overflow: hidden;
    transition: transform 0.12s, box-shadow 0.12s, opacity 0.15s, border-color 0.15s;
  }
  .node::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 5px;
    background: var(--c);
  }
  .node:hover {
    border-color: var(--c);
  }
  .node:hover {
    transform: translateY(-1px);
    box-shadow: var(--shadow), 0 0 0 3px color-mix(in srgb, var(--c) 18%, transparent);
  }
  .node.context {
    background: var(--surface-2);
    border-style: dashed;
  }
  .node.modern {
    border-color: color-mix(in srgb, var(--c) 45%, var(--line));
    background: color-mix(in srgb, var(--c) 7%, var(--surface));
  }
  .name {
    font-family: var(--serif);
    font-weight: 700;
    font-size: 15.5px;
    line-height: 1.2;
    color: var(--ink);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .years {
    font-size: 11.5px;
    color: var(--ink-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-variant-numeric: tabular-nums;
  }

  .title {
    position: fixed;
    top: 14px;
    left: 16px;
    padding: 10px 16px 11px;
    background: color-mix(in srgb, var(--surface) 88%, transparent);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border: 1px solid var(--line);
    border-radius: 12px;
    box-shadow: var(--shadow);
    pointer-events: none;
    max-width: calc(100vw - 32px);
  }
  .title h1 {
    margin: 0;
    font-family: var(--serif);
    font-size: 19px;
    line-height: 1.2;
  }
  .hint-touch {
    display: none;
  }
  @media (pointer: coarse) {
    .hint-mouse {
      display: none;
    }
    .hint-touch {
      display: block;
    }
  }
  .title p {
    margin: 2px 0 0;
    font-size: 12.5px;
    color: var(--ink-muted);
  }

</style>
