import type { TreeNode } from '../data/atlas';

export const NODE_W = 196;
export const NODE_H = 54;
/** Dikey ızgara birimi: bir kuşak iki birimdir, alt alta dizilen kardeşler birer birim iner. */
const UNIT = 66;
const GEN = 2;
/** Yan yana iki düğüm (ya da alt ağaç) arasındaki en az yatay boşluk. */
const SEP = 28;
const PAD = 60;
/** Alt alta dizilen (dalı olmayan) kardeşlerde sütun başına en çok düğüm. */
const STACK_MAX = 6;
/** Yığın sütununun solundan inen ortak çizginin düğüme uzaklığı. */
const STACK_RAIL = 14;

export interface Placed {
  node: TreeNode;
  x: number;
  y: number;
  /** Dalı olmayan kardeşlerle alt alta dizildi; bağ çizgisi soldan gelir. */
  stacked: boolean;
}

export interface Layout {
  placed: Placed[];
  byId: Map<string, Placed>;
  width: number;
  height: number;
}

/** Her ızgara satırında alt ağacın en sol ve en sağ kenarı. */
type Contour = Map<number, [number, number]>;

interface Block {
  /** Bloğun "kökünün" yatay merkezi (bağ çizgisi buraya iner). */
  anchor: number;
  contour: Contour;
  nodes: { node: TreeNode; x: number; level: number; stacked: boolean }[];
}

function extend(c: Contour, level: number, l: number, r: number) {
  const cur = c.get(level);
  if (cur) c.set(level, [Math.min(cur[0], l), Math.max(cur[1], r)]);
  else c.set(level, [l, r]);
}

function shiftBlock(b: Block, dx: number): Block {
  const contour: Contour = new Map();
  for (const [lvl, [l, r]] of b.contour) contour.set(lvl, [l + dx, r + dx]);
  return { anchor: b.anchor + dx, contour, nodes: b.nodes.map((n) => ({ ...n, x: n.x + dx })) };
}

/** Yeni bloğu, birikmiş bloklarla hiçbir satırda çakışmayacak kadar sağa iter. */
function gapNeeded(acc: Contour, b: Block): number {
  let dx = -Infinity;
  for (const [lvl, [l]] of b.contour) {
    const other = acc.get(lvl);
    if (other) dx = Math.max(dx, other[1] + SEP - l);
  }
  return dx;
}

/** Üst devlet, çocuğun kuruluşundan sonra da (10 yıldan uzun) ayakta kaldı mı? */
function outlives(parent: TreeNode, child: TreeNode): boolean {
  return parent.ongoing || parent.end - child.start > 10;
}

/**
 * Piramit soy ağacı: kök en tepede ortadadır, her kuşak kendi satırındadır ve
 * her üst düğüm çocuklarının tam ortasının üstünde durur. Alt ağaçlar sol-sağ
 * kenar çizgilerine (contour) göre birbirine en yakın biçimde yerleştirilir.
 * Dalı olmayan kardeşler üç ve fazlaysa (ör. Anadolu beylikleri) yan yana
 * yayılmak yerine alt alta listelenir; böylece piramit gereksiz genişlemez.
 * Düz aşağı inen çizgi yalnız ardıllığı (üst devlet bitti, çocuk devraldı)
 * gösterir; üst devlet yaşarken doğan çocuk yana açılan dal olarak çizilir.
 */
export function layoutTree(root: TreeNode): Layout {
  const build = (node: TreeNode, level: number): Block => {
    const self: Block = {
      anchor: NODE_W / 2,
      contour: new Map([[level, [0, NODE_W]]]),
      nodes: [{ node, x: 0, level, stacked: false }],
    };
    if (node.children.length === 0) return self;

    const childLevel = level + GEN;
    const leaves = node.children.filter((c) => c.children.length === 0);
    const stack = leaves.length >= 3 && node.children.length > 3;
    const parts: Block[] = [];
    for (const c of node.children) if (!stack || c.children.length > 0) parts.push(build(c, childLevel));
    if (stack) {
      const sorted = [...leaves].sort((a, b) => a.start - b.start);
      for (let i = 0; i < sorted.length; i += STACK_MAX) {
        const group = sorted.slice(i, i + STACK_MAX);
        const b: Block = { anchor: -STACK_RAIL, contour: new Map(), nodes: [] };
        group.forEach((c, k) => {
          b.nodes.push({ node: c, x: 0, level: childLevel + k, stacked: true });
          extend(b.contour, childLevel + k, -STACK_RAIL, NODE_W);
        });
        parts.push(b);
      }
    }

    // Kardeş blokları soldan sağa sıkıca yan yana koy.
    const acc: Contour = new Map();
    const placedParts: Block[] = [];
    for (const part of parts) {
      const dx = placedParts.length === 0 ? 0 : gapNeeded(acc, part);
      const moved = shiftBlock(part, dx === -Infinity ? placedParts[placedParts.length - 1].anchor + NODE_W + SEP : dx);
      for (const [lvl, [l, r]] of moved.contour) extend(acc, lvl, l, r);
      placedParts.push(moved);
    }

    // Üst düğümü çocuklarının ortasına koy; dağıtım çizgisini de kenar çizgisine kat.
    const first = placedParts[0].anchor;
    const last = placedParts[placedParts.length - 1].anchor;
    // Tek çocuk tam alta konursa "üst devlet yıkıldı, yerine bu kuruldu" diye
    // okunur. Üst devlet çocuk kurulduktan sonra da yaşadıysa çocuk yana açılır.
    const only = node.children.length === 1 ? node.children[0] : null;
    const branch = only !== null && outlives(node, only);
    const center = branch ? first - (NODE_W + SEP) / 2 : (first + last) / 2;
    const x = center - NODE_W / 2;
    const contour = acc;
    extend(contour, level, x, x + NODE_W);
    extend(contour, level + 1, Math.min(first, center), Math.max(last, center));
    const nodes = [{ node, x, level, stacked: false }, ...placedParts.flatMap((p) => p.nodes)];
    return { anchor: center, contour, nodes };
  };

  const block = build(root, 0);
  const minX = Math.min(...[...block.contour.values()].map(([l]) => l));
  const byId = new Map<string, Placed>();
  for (const n of block.nodes) {
    byId.set(n.node.id, { node: n.node, x: n.x - minX + PAD, y: n.level * UNIT + PAD, stacked: n.stacked });
  }
  const placed = [...byId.values()];
  const width = Math.max(...placed.map((p) => p.x)) + NODE_W + PAD;
  const height = Math.max(...placed.map((p) => p.y)) + NODE_H + PAD;
  return { placed, byId, width, height };
}

/** Üst düğümün alt ortasından dağıtım çizgisine, oradan çocuğun üst ortasına inen köşeli bağ. */
export function edgePath(from: Placed, to: Placed): string {
  const x1 = from.x + NODE_W / 2;
  const y1 = from.y + NODE_H;
  const t = from.y + NODE_H + (GEN * UNIT - NODE_H) / 2;
  const r = 8;
  const turn = (x: number, dir: number) => `Q${x},${t} ${x + dir * r},${t}`;
  if (to.stacked) {
    const rail = to.x - STACK_RAIL;
    const ym = to.y + NODE_H / 2;
    const dir = rail > x1 ? 1 : -1;
    return `M${x1},${y1} V${t - r} ${turn(x1, dir)} H${rail - dir * r} Q${rail},${t} ${rail},${t + r} V${ym - r} Q${rail},${ym} ${rail + r},${ym} H${to.x}`;
  }
  const x2 = to.x + NODE_W / 2;
  const y2 = to.y;
  if (Math.abs(x1 - x2) < 1) return `M${x1},${y1} V${y2}`;
  const dir = x2 > x1 ? 1 : -1;
  return `M${x1},${y1} V${t - r} ${turn(x1, dir)} H${x2 - dir * r} Q${x2},${t} ${x2},${t + r} V${y2}`;
}
