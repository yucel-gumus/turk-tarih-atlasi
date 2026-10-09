import type { BattleResult, Region } from '../../schemas/atlas.schema';
import { atlasIndex } from './lookup';
import { hrefWar } from '../router/route';
import { parseHistoricalDate, compareBattleYears, type HistoricalDate } from './dates';
import { canon } from '../text';

export type FoeCategory =
  | 'Bizans'
  | 'Haçlılar'
  | 'Moğollar'
  | 'Çin'
  | 'Rus'
  | 'Safevî / İran'
  | 'Avrupa / Balkan'
  | 'Türk / İç Mücadele'
  | 'Diğer';

export interface BattleItem {
  id: string;
  name: string;
  when: string;
  year: number | null;
  date: HistoricalDate;
  foe: string;
  foeCategory: FoeCategory;
  result: BattleResult;
  note: string;
  stateId: string;
  stateName: string;
  stateColor: string;
  region: Region;
  rulerId: string;
  rulerName: string;
  index: number;
  href: string;
}

/** Returns a sorting hint, never a guessed reign year. */
export function parseWhenYear(when: string): number | null {
  return parseHistoricalDate(when).start;
}

export function categorizeFoe(foe: string, stateName: string): FoeCategory {
  const f = canon(foe);
  if (/\b(?:bizans|rum|dogu roma|trabzon)\b/.test(f)) return 'Bizans';
  if (f.includes('hacli') || f.includes('frank') || f.includes('antakya prens') || f.includes('trablus kont') || f.includes('kudus kral')) return 'Haçlılar';
  if (f.includes('mogol') || f.includes('ilhanli') || f.includes('culgu') || f.includes('kalmuk') || f.includes('cungar') || f.includes('cuci')) return 'Moğollar';
  if (/\b(?:cin|tang|song|ming|qing|wei|tabgac)\b/.test(f)) return 'Çin';
  if (f.includes('rus') || f.includes('kiev') || f.includes('moskova') || f.includes('kazak knez') || f.includes('novgorod')) return 'Rus';
  if (f.includes('safevi') || f.includes('iran') || f.includes('sasani') || f.includes('samani') || f.includes('buye') || f.includes('kacar') || f.includes('avsar')) return 'Safevî / İran';
  if (
    f.includes('avusturya') ||
    f.includes('macar') ||
    f.includes('venedik') ||
    f.includes('ceneviz') ||
    f.includes('sirp') ||
    f.includes('bulgar') ||
    f.includes('leh') ||
    f.includes('polonya') ||
    f.includes('ingiliz') ||
    f.includes('fransiz') ||
    f.includes('yunan') ||
    f.includes('roma') ||
    f.includes('kutsal ittifak')
  ) {
    return 'Avrupa / Balkan';
  }
  if (
    f.includes('selcuk') ||
    f.includes('osmanli') ||
    f.includes('timur') ||
    f.includes('karaman') ||
    f.includes('akkoyunlu') ||
    f.includes('karakoyunlu') ||
    f.includes('harzem') ||
    f.includes('gazneli') ||
    f.includes('oguz') ||
    f.includes('karluk') ||
    f.includes('uygur') ||
    f.includes('gokturk') ||
    f.includes('turk') ||
    f.includes('beylig')
  ) {
    return 'Türk / İç Mücadele';
  }
  return 'Diğer';
}

let cachedBattles: BattleItem[] | null = null;

export function getAllBattles(): BattleItem[] {
  if (cachedBattles) return cachedBattles;

  const index = atlasIndex();
  const list: BattleItem[] = [];

  for (const state of index.devletler) {
    for (const ruler of state.rulers ?? []) {
      (ruler.wars ?? []).forEach((war, i) => {
        const warIndex = i + 1;
        const year = parseWhenYear(war.when);
        const foeCategory = categorizeFoe(war.foe, state.name);

        list.push({
          id: `battle-${ruler.id}-${warIndex}`,
          name: war.name,
          when: war.when,
          year,
          date: parseHistoricalDate(war.when),
          foe: war.foe,
          foeCategory,
          result: war.result,
          note: war.note,
          stateId: state.id,
          stateName: state.name,
          stateColor: state.region ? '#b5651d' : '#8a6a30',
          region: state.region,
          rulerId: ruler.id,
          rulerName: ruler.name,
          index: warIndex,
          href: hrefWar(state.id, ruler.id, warIndex, war.name),
        });
      });
    }
  }

  // Varsayılan: kronolojik sıra (en eskiden en yeniye)
  list.sort((a, b) => compareBattleYears(a.year, b.year) || a.name.localeCompare(b.name, 'tr'));
  cachedBattles = list;
  return list;
}

export interface BattleStats {
  total: number;
  byResult: Record<BattleResult, number>;
  byFoe: Record<FoeCategory, number>;
}

export function getBattleStats(): BattleStats {
  const battles = getAllBattles();
  const byResult: Record<BattleResult, number> = {
    zafer: 0,
    yenilgi: 0,
    antlasma: 0,
    sonucsuz: 0,
    belirsiz: 0,
  };
  const byFoe: Record<FoeCategory, number> = {
    Bizans: 0,
    Haçlılar: 0,
    Moğollar: 0,
    Çin: 0,
    Rus: 0,
    'Safevî / İran': 0,
    'Avrupa / Balkan': 0,
    'Türk / İç Mücadele': 0,
    Diğer: 0,
  };

  for (const b of battles) {
    byResult[b.result] = (byResult[b.result] ?? 0) + 1;
    byFoe[b.foeCategory] = (byFoe[b.foeCategory] ?? 0) + 1;
  }

  return {
    total: battles.length,
    byResult,
    byFoe,
  };
}
