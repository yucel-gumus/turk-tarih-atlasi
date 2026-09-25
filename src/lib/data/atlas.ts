import { StateSchema, type State, type Milestone, type Region } from '../../schemas/atlas.schema';
export type { State, Milestone, Region };

export const PX = 8;
export const MIN_YEAR = -280;
export const MAX_YEAR = 1930;
export const ORIGIN_X = 48;
export const TOP = 36;

export interface RegionInfo {
  id: Region;
  name: string;
  color: string;
  glow: string;
}

export const REGIONS: RegionInfo[] = [
  { id: 'giris', name: 'Nasıl okunur', color: '#e0c48a', glow: 'rgba(224, 196, 138, 0.25)' },
  { id: 'bozkir', name: 'Bozkır ve İç Asya', color: '#d08a45', glow: 'rgba(208, 138, 69, 0.25)' },
  { id: 'turkistan', name: 'Türkistan', color: '#3c9a8c', glow: 'rgba(60, 154, 140, 0.25)' },
  { id: 'bati', name: 'Hazar, Karadeniz, Avrupa', color: '#6a8cbf', glow: 'rgba(106, 140, 191, 0.25)' },
  { id: 'kuzey', name: 'İdil, Kırım, kuzey hanlıkları', color: '#7da36a', glow: 'rgba(125, 163, 106, 0.25)' },
  { id: 'iran', name: 'İran, Horasan, Hindistan', color: '#c46b86', glow: 'rgba(196, 107, 134, 0.25)' },
  { id: 'anadolu', name: 'Anadolu, Ortadoğu, Mısır', color: '#d4b06a', glow: 'rgba(212, 176, 106, 0.25)' },
  { id: 'diger', name: 'Sınırda ve ilişkili yapılar', color: '#9a8f82', glow: 'rgba(154, 143, 130, 0.25)' },
];

export const REGION_MAP = Object.fromEntries(REGIONS.map((r) => [r.id, r]));

export const MILESTONES: Milestone[] = [
  { year: -209, label: 'Mete' },
  { year: 552, label: 'Göktürk' },
  { year: 630, label: 'Batı Göktürk' },
  { year: 744, label: 'Uygur' },
  { year: 840, label: 'Karahanlı' },
  { year: 963, label: 'Gazneli' },
  { year: 1040, label: 'Selçuklu' },
  { year: 1071, label: 'Malazgirt' },
  { year: 1096, label: 'Haçlı' },
  { year: 1206, label: 'Moğol' },
  { year: 1243, label: 'Kösedağ' },
  { year: 1299, label: 'Osmanlı' },
  { year: 1402, label: 'Ankara' },
  { year: 1453, label: 'İstanbul' },
  { year: 1514, label: 'Çaldıran' },
  { year: 1517, label: 'Mısır' },
  { year: 1526, label: 'Babür' },
  { year: 1571, label: 'İnebahtı' },
  { year: 1683, label: 'Viyana' },
  { year: 1699, label: 'Karlofça' },
  { year: 1774, label: 'Küçük Kaynarca' },
  { year: 1839, label: 'Tanzimat' },
  { year: 1911, label: 'Trablusgarp' },
  { year: 1922, label: 'Saltanat' },
];

export const RESULT_MAP: Record<string, { label: string; color: string }> = {
  zafer: { label: 'Zafer', color: '#5cb85c' },
  yenilgi: { label: 'Yenilgi', color: '#d9534f' },
  sonucsuz: { label: 'Sonuçsuz', color: '#f0ad4e' },
  belirsiz: { label: 'Belirsiz', color: '#888888' },
  antlasma: { label: 'Antlaşma', color: '#5bc0de' },
};

export const CERTAINTY_MAP: Record<string, string> = {
  kesin: 'Kesin',
  olasi: 'Olası',
  muhtemel: 'Muhtemel',
  tartismali: 'Tartışmalı',
  rivayet: 'Rivayet',
};

export function yearLabel(n: number): string {
  return n < 0 ? `MÖ ${-n}` : String(n);
}

export function xOf(year: number): number {
  return ORIGIN_X + (year - MIN_YEAR) * PX;
}

export function yearOf(x: number): number {
  return Math.round(MIN_YEAR + (x - ORIGIN_X) / PX);
}

export function clamp(v: number, min: number, max: number): number {
  return Math.max(min, Math.min(max, v));
}

export function fold(s: string): string {
  return s
    .toLocaleLowerCase('tr')
    .replaceAll('ı', 'i')
    .replaceAll('ş', 's')
    .replaceAll('ğ', 'g')
    .replaceAll('ü', 'u')
    .replaceAll('ö', 'o')
    .replaceAll('ç', 'c')
    .replaceAll('â', 'a')
    .replaceAll('î', 'i')
    .replaceAll('û', 'u');
}

export function canon(s: string): string {
  return fold(s)
    .replaceAll('kokturk', 'gokturk')
    .replaceAll('vahdettin', 'vahdeddin')
    .replaceAll('vahideddin', 'vahdeddin')
    .replaceAll('mehmet', 'mehmed')
    .replaceAll('beyazit', 'bayezid');
}

export function stateWidth(s: State): number {
  const span = Math.max(1, (s.end ?? s.start) - s.start);
  let w = Math.max(88, span * PX);
  const n = (s.rulers || []).length;
  if ((s.essay || []).length) w = Math.max(w, 760);
  if (n) w = Math.max(w, 332);
  return w;
}

export function colsFor(width: number, n: number): number {
  if (n <= 1) return 1;
  const inner = Math.max(280, width - 28);
  const cols = Math.floor((inner + 12) / 312);
  return clamp(cols, 1, n);
}

// Deterministic layout height calculation to completely eliminate startup reflow / long tasks
export function estimateStateHeight(s: State, width: number): number {
  const n = s.rulers?.length || 0;
  if (n === 0) {
    // Info card like 'okuma'
    return 340;
  }
  const cols = colsFor(width, n);
  const rows = Math.ceil(n / cols);
  // Header: ~60px, Essay/summary: ~45px, each ruler row: ~230px, gaps: ~16px
  const headerH = 64;
  const summaryH = s.summary ? 50 : 0;
  const rulersH = rows * 240 + (rows - 1) * 16;
  return Math.max(160, headerH + summaryH + rulersH + 32);
}

export interface PositionedState {
  state: State;
  x: number;
  y: number;
  w: number;
  h: number;
  lane: number;
  cols: number;
}

export interface PositionedRegion {
  id: Region;
  name: string;
  color: string;
  glow: string;
  y: number;
  h: number;
}

export interface AtlasLayout {
  states: PositionedState[];
  regions: PositionedRegion[];
  worldW: number;
  worldH: number;
}

export function computeLayout(rawStates: State[]): AtlasLayout {
  const positionedStates: PositionedState[] = [];
  const positionedRegions: PositionedRegion[] = [];
  let cursorY = TOP;

  for (const region of REGIONS) {
    const list = rawStates.filter((s) => s.region === region.id);
    if (!list.length) continue;

    const items = list
      .map((s) => {
        const w = stateWidth(s);
        const h = estimateStateHeight(s, w);
        const cols = colsFor(w, s.rulers?.length || 1);
        return {
          state: s,
          x: xOf(s.start),
          w,
          h,
          cols,
          lane: 0,
        };
      })
      .sort((a, b) => a.x - b.x || a.w - b.w);

    const laneEnds: number[] = [];
    for (const it of items) {
      let lane = laneEnds.findIndex((end) => end + 20 <= it.x);
      if (lane < 0) {
        lane = laneEnds.length;
        laneEnds.push(it.x + it.w);
      } else {
        laneEnds[lane] = it.x + it.w;
      }
      it.lane = lane;
    }

    const laneH: number[] = [];
    for (const it of items) {
      laneH[it.lane] = Math.max(laneH[it.lane] || 0, it.h);
    }

    const laneY: number[] = [];
    let acc = 32;
    for (let i = 0; i < laneH.length; i++) {
      laneY[i] = acc;
      acc += laneH[i] + 20;
    }
    const regionH = acc + 16;

    for (const it of items) {
      const top = cursorY + laneY[it.lane];
      positionedStates.push({
        state: it.state,
        x: it.x,
        y: top,
        w: it.w,
        h: it.h,
        lane: it.lane,
        cols: it.cols,
      });
    }

    positionedRegions.push({
      id: region.id,
      name: region.name,
      color: region.color,
      glow: region.glow,
      y: cursorY,
      h: regionH,
    });

    cursorY += regionH + 28;
  }

  let maxX = xOf(MAX_YEAR);
  for (const ps of positionedStates) {
    maxX = Math.max(maxX, ps.x + ps.w);
  }

  const worldW = maxX + 120;
  const worldH = cursorY + 60;

  return {
    states: positionedStates,
    regions: positionedRegions,
    worldW,
    worldH,
  };
}

export interface SearchItem {
  id: string;
  kind: 'Devlet' | 'Hükümdar' | 'Savaş' | 'Eş/Çocuk';
  title: string;
  sub: string;
  key: string;
  stateId: string;
  rulerId?: string;
  year?: number;
}

export function buildSearchIndex(states: State[]): SearchItem[] {
  const index: SearchItem[] = [];

  for (const s of states) {
    const when = `${yearLabel(s.start)} – ${yearLabel(s.end)}`;
    index.push({
      id: `state-${s.id}`,
      kind: 'Devlet',
      title: s.name,
      sub: when,
      key: canon(`${s.name} ${s.short || ''} ${(s.aliases || []).join(' ')} ${s.summary || ''}`),
      stateId: s.id,
      year: s.start,
    });

    for (const r of s.rulers || []) {
      const reignStr =
        r.reign && (r.reign[0] != null || r.reign[1] != null)
          ? `${r.reign[0] != null ? yearLabel(r.reign[0]) : '?'} – ${r.reign[1] != null ? yearLabel(r.reign[1]) : '?'}`
          : '';
      index.push({
        id: `ruler-${r.id}`,
        kind: 'Hükümdar',
        title: r.name,
        sub: `${s.name} · ${reignStr || r.title || ''}`,
        key: canon(`${r.name} ${(r.aliases || []).join(' ')} ${s.name} ${r.title || ''} ${(r.traits || []).join(' ')}`),
        stateId: s.id,
        rulerId: r.id,
        year: r.reign?.[0] ?? s.start,
      });

      for (const w of r.wars || []) {
        index.push({
          id: `war-${r.id}-${w.name}`,
          kind: 'Savaş',
          title: w.name,
          sub: `${r.name} (${w.when || ''}) · ${w.foe || ''}`,
          key: canon(`${w.name} ${w.foe || ''} ${w.when || ''} ${r.name} ${s.name} ${w.note || ''}`),
          stateId: s.id,
          rulerId: r.id,
          year: (parseInt(w.when, 10) || r.reign?.[0]) ?? s.start,
        });
      }

      for (const p of [...(r.wives || []), ...(r.children || [])]) {
        index.push({
          id: `person-${r.id}-${p.name}`,
          kind: 'Eş/Çocuk',
          title: p.name,
          sub: `${r.name} ailesi · ${p.note || ''}`,
          key: canon(`${p.name} ${r.name} ${s.name} ${p.note || ''}`),
          stateId: s.id,
          rulerId: r.id,
        });
      }
    }
  }

  return index;
}

// Eager load all 16 JSON files
export function loadAllStates(): State[] {
  const modules = import.meta.glob('../../../data/raw/*.json', { eager: true });
  const allStates: State[] = [];

  for (const path in modules) {
    const rawContent = (modules[path] as { default: unknown }).default;
    const array = Array.isArray(rawContent) ? rawContent : [rawContent];
    for (const item of array) {
      const parsed = StateSchema.safeParse(item);
      if (parsed.success) {
        allStates.push(parsed.data);
      } else {
        console.error(`[AtlasLoader] Şema hatası (${path}):`, JSON.stringify(parsed.error.issues));
      }
    }
  }

  // Sort by region order then start year
  const regionOrder = REGIONS.map((r) => r.id);
  allStates.sort((a, b) => {
    const ra = regionOrder.indexOf(a.region);
    const rb = regionOrder.indexOf(b.region);
    if (ra !== rb) return ra - rb;
    return a.start - b.start || a.id.localeCompare(b.id);
  });

  return allStates;
}
