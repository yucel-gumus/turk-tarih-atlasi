import { StateSchema, LineageSchema } from '../../schemas/atlas.schema';
import type {
  State,
  Ruler,
  War,
  Region,
  BattleResult,
  Certainty,
  Confidence,
  EdgeKind,
  ContextNode,
  Lineage,
} from '../../schemas/atlas.schema';
import lineageRaw from '../../../data/lineage.json';
import { canon } from '../text';
import { parseHistoricalDate } from './dates';

export const REGION_COLORS: Record<Region, string> = {
  bozkir: '#b5651d',
  turkistan: '#14776b',
  bati: '#35558a',
  kuzey: '#4f7a33',
  iran: '#a83a5b',
  anadolu: '#977a1c',
  diger: '#6b6357',
  gunumuz: '#c0392b',
};

export const REGION_NAMES: Record<Region, string> = {
  bozkir: 'Bozkır ve İç Asya',
  turkistan: 'Türkistan',
  bati: 'Hazar, Karadeniz, Avrupa',
  kuzey: 'İdil, Kırım, kuzey hanlıkları',
  iran: 'İran, Horasan, Hindistan',
  anadolu: 'Anadolu',
  diger: 'Mısır, Suriye, Hindistan',
  gunumuz: 'Günümüz',
};

export const RESULT_LABEL: Record<BattleResult, string> = {
  zafer: 'Zafer',
  yenilgi: 'Yenilgi',
  sonucsuz: 'Sonuçsuz',
  belirsiz: 'Belirsiz',
  antlasma: 'Antlaşma',
};

export const CERTAINTY_LABEL: Record<Certainty, string> = {
  kesin: 'Kesin',
  olasi: 'Olası',
  muhtemel: 'Muhtemel',
  tartismali: 'Tartışmalı',
  rivayet: 'Rivayet',
};

export const CONFIDENCE_LABEL: Record<Confidence, string> = {
  kayit: 'Kayıtlarla sabit',
  tartismali: 'Tartışmalı',
  rivayet: 'Rivayete dayalı',
};

export const EDGE_LABEL: Record<EdgeKind, string> = {
  devam: 'Doğrudan devamı',
  kol: 'Ayrılan kol',
  miras: 'Halk ve toprak mirası',
};

export function yearLabel(n: number): string {
  return n < 0 ? `MÖ ${-n}` : String(n);
}

export const CURRENT_YEAR = 2026;

export function spanLabel(start: number, end: number | null, ongoing = false): string {
  if (ongoing || end === null) return `${yearLabel(start)} – günümüz`;
  return `${yearLabel(start)} – ${yearLabel(end)}`;
}

/* ------------------------------------------------------------------ yükleme */

const modules = import.meta.glob('../../../data/raw/*.json') as Record<string, () => Promise<{ default: unknown }>>;

let states: Map<string, State> | null = null;
export const lineage: Lineage = LineageSchema.parse(lineageRaw);
const contextById = new Map(lineage.contextNodes.map((c) => [c.id, c]));

export async function preloadAtlas(): Promise<void> {
  if (states) return;
  const loaded = await Promise.all(Object.values(modules).map((load) => load()));
  const map = new Map<string, State>();
  for (const mod of loaded) {
    const items = Array.isArray(mod.default) ? mod.default : [mod.default];
    for (const item of items) {
      const state = StateSchema.parse(item);
      map.set(state.id, state);
    }
  }
  states = map;
}

function all(): Map<string, State> {
  if (!states) throw new Error('Atlas verisi yüklenmeden okunamaz; önce preloadAtlas() beklenmeli.');
  return states;
}

export function allStates(): State[] {
  return [...all().values()];
}

export function getState(id: string): State | undefined {
  return all().get(id);
}

export function getContext(id: string): ContextNode | undefined {
  return contextById.get(id);
}

export function getRuler(stateId: string, rulerId: string): Ruler | undefined {
  return getState(stateId)?.rulers.find((r) => r.id === rulerId);
}

export function isOngoing(state: State): boolean {
  return state.region === 'gunumuz';
}

/* --------------------------------------------------------------- soy ağacı */

export interface TreeNode {
  id: string;
  kind: 'state' | 'context';
  name: string;
  short: string;
  start: number;
  end: number;
  ongoing: boolean;
  region: Region | null;
  parent: TreeNode | null;
  edgeKind: EdgeKind | null;
  edgeNote: string;
  children: TreeNode[];
}

let treeCache: { root: TreeNode; byId: Map<string, TreeNode> } | null = null;

export function buildTree(): { root: TreeNode; byId: Map<string, TreeNode> } {
  if (treeCache) return treeCache;
  const byId = new Map<string, TreeNode>();
  for (const s of all().values()) {
    byId.set(s.id, {
      id: s.id,
      kind: 'state',
      name: s.name,
      short: (s.short || s.name).replace(/\s*\(.*\)$/, ''),
      start: s.start,
      end: s.end,
      ongoing: isOngoing(s),
      region: s.region,
      parent: null,
      edgeKind: null,
      edgeNote: '',
      children: [],
    });
  }
  for (const c of lineage.contextNodes) {
    byId.set(c.id, {
      id: c.id,
      kind: 'context',
      name: c.name,
      short: c.short,
      start: c.start,
      end: c.end,
      ongoing: false,
      region: null,
      parent: null,
      edgeKind: null,
      edgeNote: '',
      children: [],
    });
  }
  for (const e of lineage.edges) {
    const parent = byId.get(e.parent);
    const child = byId.get(e.child);
    if (!parent || !child) throw new Error(`Soy ağacı bağı bilinmeyen düğüme gidiyor: ${e.parent} → ${e.child}`);
    if (child.parent) throw new Error(`${e.child} düğümünün iki üst düğümü var.`);
    child.parent = parent;
    child.edgeKind = e.kind;
    child.edgeNote = e.note;
    parent.children.push(child);
  }
  const root = byId.get(lineage.root);
  if (!root) throw new Error(`Soy ağacı kökü bulunamadı: ${lineage.root}`);
  treeCache = { root, byId };
  return treeCache;
}

/* ----------------------------------------------------------- savaş ilişkileri */

export interface WarRef {
  stateId: string;
  rulerId: string;
  index: number;
}

export interface WarEntry extends WarRef {
  war: War;
  state: State;
  ruler: Ruler;
  start: number | null;
  end: number | null;
}

let warsCache: WarEntry[] | null = null;

function allWars(): WarEntry[] {
  if (warsCache) return warsCache;
  const list: WarEntry[] = [];
  for (const state of all().values()) {
    for (const ruler of state.rulers) {
      ruler.wars.forEach((war, index) => {
        const d = parseHistoricalDate(war.when);
        list.push({ stateId: state.id, rulerId: ruler.id, index, war, state, ruler, start: d.start, end: d.end ?? d.start });
      });
    }
  }
  warsCache = list;
  return list;
}

export function getWar(ref: WarRef): WarEntry | undefined {
  return allWars().find((w) => w.stateId === ref.stateId && w.rulerId === ref.rulerId && w.index === ref.index);
}

export function stateWars(stateId: string): WarEntry[] {
  return allWars()
    .filter((w) => w.stateId === stateId)
    .sort((a, b) => (a.start ?? Infinity) - (b.start ?? Infinity));
}

const BATTLE_WORDS = /\b(savasi|savas|muharebesi|muharebe|kusatmasi|kusatma|seferi|sefer|meydan|zaferi|bozgunu|baskini|catismasi|ve|ile|i|ii|iii)\b/g;

function battleKey(name: string): string {
  return canon(name)
    .replace(/\(.*?\)/g, ' ')
    .replace(/[^a-z0-9 ]+/g, ' ')
    .replace(BATTLE_WORDS, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Aynı savaşın karşı tarafta (başka bir devletin hükümdarında) tutulan kaydı. */
export function counterpartWars(entry: WarEntry): WarEntry[] {
  const key = battleKey(entry.war.name);
  if (key.length < 3) return [];
  return allWars().filter((w) => {
    if (w.stateId === entry.stateId) return false;
    if (battleKey(w.war.name) !== key) return false;
    if (entry.start === null || w.start === null) return true;
    const aEnd = entry.end ?? entry.start;
    const bEnd = w.end ?? w.start;
    return w.start <= aEnd + 1 && entry.start <= bEnd + 1;
  });
}

/** Savaşın karşı tarafındaki adın atlasta bir devlete ve mümkünse hükümdara karşılık gelip gelmediği. */
export function foeMatches(entry: WarEntry): { state: State; ruler: Ruler | null }[] {
  const foe = ` ${canon(entry.war.foe).replace(/[^a-z0-9]+/g, ' ')} `;
  if (!foe.trim()) return [];
  const found: { state: State; ruler: Ruler | null }[] = [];
  for (const state of all().values()) {
    if (state.id === entry.stateId) continue;
    const keys = new Set<string>();
    for (const n of [state.name, state.short ?? '', ...state.aliases]) {
      const k = canon(n).replace(/\(.*?\)/g, ' ').replace(/[^a-z0-9]+/g, ' ').trim();
      if (!k) continue;
      keys.add(k);
      keys.add(k.replace(/\b(devleti|hanligi|kaganligi|imparatorlugu|sultanligi|beyligi|birligi|ordasi)\b/g, '').trim());
      keys.add(k.replace(/(lar|ler|lari|leri)$/, ''));
      keys.add(k.replace(/ogullari$/, 'oglu'));
    }
    const hit = [...keys].some((k) => k.length >= 5 && foe.includes(` ${k}`));
    if (!hit) continue;
    const year = entry.start;
    const ruler =
      state.rulers.find((r) => {
        const rn = canon(r.name).replace(/[^a-z0-9]+/g, ' ').trim();
        if (rn.length < 5 || !foe.includes(` ${rn} `) && !foe.includes(` ${rn}`)) return false;
        if (year === null) return true;
        const [a, b] = r.reign;
        return (a === null || a - 1 <= year) && (b === null || year <= b + 1);
      }) ?? null;
    found.push({ state, ruler });
  }
  return found;
}

/** Çocuk kaydının aynı devlette sonradan hükümdar olup olmadığı. */
export function childAsRuler(state: State, father: Ruler, childName: string): Ruler | null {
  const name = canon(childName).replace(/\(.*?\)/g, ' ').replace(/[^a-z0-9]+/g, ' ').trim();
  if (name.length < 3) return null;
  const from = father.reign[0] ?? -Infinity;
  const until = (father.reign[1] ?? father.death ?? from) + 40;
  const re = new RegExp(`(^| )${name}( |$)`);
  return (
    state.rulers.find((r) => {
      if (r.id === father.id || r.reign[0] === null) return false;
      if (r.reign[0] < from || r.reign[0] > until) return false;
      return re.test(canon(r.name).replace(/[^a-z0-9]+/g, ' ').trim());
    }) ?? null
  );
}

export function warStats(wars: War[]): Record<BattleResult, number> {
  const s: Record<BattleResult, number> = { zafer: 0, yenilgi: 0, sonucsuz: 0, belirsiz: 0, antlasma: 0 };
  for (const w of wars) s[w.result]++;
  return s;
}

export function durationLabel(start: number | null, end: number | null): string {
  if (start === null) return 'Kayıtta kesin tarih yok';
  if (end === null) return `${yearLabel(start)} dolayı; süre kayıtlarda yok`;
  if (end === start) return `${yearLabel(start)} yılı içinde`;
  const n = end - start;
  return `${yearLabel(start)} – ${yearLabel(end)} · yaklaşık ${n} yıl`;
}

export function reignLabel(r: Ruler, ongoing = false): string {
  const [a, b] = r.reign;
  if (a === null) return 'Saltanat yılları kayıtlarda yok';
  if (b === null) return ongoing ? `${yearLabel(a)} – günümüz` : `${yearLabel(a)} – ?`;
  return a === b ? yearLabel(a) : `${yearLabel(a)} – ${yearLabel(b)}`;
}
