// Veri erişim katmanı: bütün kayıtlar bir kez okunur, kimlik ve ad aramaları
// bir kez kurulur, sonra önbellekten sunulur. Sayfalar `atlasIndex()` çağırır;
// her render'da yeniden hesaplama yapılmaz.
//
// Veride yabancı anahtar yoktur: adlar, savaşlar ve kişiler başka bir kayda
// referans taşımaz. Bu yüzden bütün çapraz bağlantılar (kişi ↔ hükümdar,
// çocuk → anne) ad eşitliğinden çıkarılır ve eşleşmeyen durumlar gizlenmez.

import type { BattleResult, Person, Region, Ruler, State, War } from '../../schemas/atlas.schema';
import { canon, isPlaceholderName, looseKey, slug } from '../text';
import { hrefGuide, hrefPerson, hrefRuler, hrefState, hrefWar, type PersonRole } from '../router/route';
import { loadAllStates, yearLabel } from './atlas';

export interface SearchItem {
  id: string;
  kind: 'Devlet' | 'Hükümdar' | 'Savaş' | 'Eş' | 'Çocuk' | 'Rehber';
  title: string;
  sub: string;
  /** Aranan metnin katlanmış anahtarı. */
  key: string;
  /** Hazır adres; arama sonucu doğrudan ilgili sayfaya iner. */
  href: string;
}

/** Başlık eşleşmelerini önce gösterir; not içinde geçen sözcükler arkaya kalır. */
export function searchItems(items: SearchItem[], query: string): SearchItem[] {
  const wanted = canon(query.trim());
  if (wanted.length < 2) return [];
  const kindRank: Record<SearchItem['kind'], number> = {
    Devlet: 0,
    Hükümdar: 1,
    Savaş: 2,
    Eş: 3,
    Çocuk: 4,
    Rehber: 5,
  };
  function rank(item: SearchItem): number {
    const title = canon(item.title);
    if (item.kind === 'Devlet' && title.includes(wanted)) return 0;
    if (item.kind === 'Hükümdar' && title.includes(wanted)) return 1;
    if (title === wanted) return 2;
    if (title.startsWith(wanted)) return 3;
    if (title.includes(wanted)) return 4;
    if (canon(item.sub).includes(wanted)) return 5;
    return 6;
  }
  return items
    .filter((item) => item.key.includes(wanted))
    .sort((a, b) => rank(a) - rank(b) || kindRank[a.kind] - kindRank[b.kind] || a.title.localeCompare(b.title, 'tr'));
}

export interface AtlasTotals {
  devlet: number;
  rehber: number;
  hukumdar: number;
  /** Kaydında hiç savaş bulunmayan hükümdar sayısı — "boş liste" ile "savaşmadı" ayrımı için. */
  savassizHukumdar: number;
  /** Adı yer tutucu olan hükümdar sayısı ("kayıtlarda adı geçmiyor" gibi). */
  yerTutucuHukumdar: number;
  savas: number;
  es: number;
  cocuk: number;
  /**
   * Annesi yazılı eş kaydı sayısı. Şema anne alanını eş kayıtları için de tanımlar
   * (aynı `PersonSchema`), ama mevcut eş kayıtlarının hiçbirinde doldurulmamış: boşluk
   * şemadan değil veriden gelir.
   */
  esAnneli: number;
}

export interface AtlasIndex {
  /** Bütün kayıtlar (rehber dahil). */
  states: State[];
  /** Rehber hariç Türk devletleri. */
  devletler: State[];
  rehber: State | null;
  statesById: Map<string, State>;
  rulersById: Map<string, Ruler>;
  rulerStateById: Map<string, State>;
  /** Katlanmış hükümdar adı → kayıtlar. Aynı ad birden çok devlette geçebilir. */
  rulerByName: Map<string, { state: State; ruler: Ruler }[]>;
  arama: SearchItem[];
  /** Sayılar sayılarak elde edilir; hiçbir yerde sabit yazılmaz. */
  toplam: AtlasTotals;
}

let cached: AtlasIndex | null = null;

export function atlasIndex(): AtlasIndex {
  if (cached) return cached;

  const states = loadAllStates();
  const devletler = states.filter((s) => s.region !== 'giris');
  const rehber = states.find((s) => s.region === 'giris') ?? null;

  const statesById = new Map<string, State>();
  const rulersById = new Map<string, Ruler>();
  const rulerStateById = new Map<string, State>();
  const rulerByName = new Map<string, { state: State; ruler: Ruler }[]>();
  const toplam: AtlasTotals = {
    // Rehber kaydı sayılmaz: hükümdarı yoktur.
    devlet: devletler.length,
    rehber: rehber ? 1 : 0,
    hukumdar: 0,
    savassizHukumdar: 0,
    yerTutucuHukumdar: 0,
    savas: 0,
    es: 0,
    cocuk: 0,
    esAnneli: 0,
  };

  for (const state of states) {
    statesById.set(state.id, state);
    for (const ruler of state.rulers ?? []) {
      // Hükümdar adresi yalnız id ile çözülür; bu yüzden id tekilliği bir
      // varsayım değil, adres gramerinin dayanağıdır. Bozulursa sessizce
      // yanlış hükümdar gösterilmesin diye burada görünür hale getirilir.
      if (rulersById.has(ruler.id)) {
        console.error(`[AtlasIndex] Hükümdar id'si tekil değil: ${ruler.id}`);
      }
      rulersById.set(ruler.id, ruler);
      rulerStateById.set(ruler.id, state);

      const key = canon(ruler.name);
      const named = rulerByName.get(key);
      if (named) named.push({ state, ruler });
      else rulerByName.set(key, [{ state, ruler }]);

      toplam.hukumdar += 1;
      if (!ruler.wars?.length) toplam.savassizHukumdar += 1;
      if (isPlaceholderName(ruler.name)) toplam.yerTutucuHukumdar += 1;
      toplam.savas += ruler.wars?.length ?? 0;
      toplam.es += ruler.wives?.length ?? 0;
      toplam.esAnneli += (ruler.wives ?? []).filter((wife) => wife.mother).length;
      toplam.cocuk += ruler.children?.length ?? 0;
    }
  }

  cached = {
    states,
    devletler,
    rehber,
    statesById,
    rulersById,
    rulerStateById,
    rulerByName,
    arama: buildSearchIndex(states),
    toplam,
  };
  return cached;
}

/** Saltanat aralığı metni; sınır bilinmiyorsa '?' yazılır, yıl uydurulmaz. */
export function reignLabel(ruler: Ruler): string {
  const [start, end] = ruler.reign;
  if (start == null && end == null) return '';
  return `${start != null ? yearLabel(start) : '?'} – ${end != null ? yearLabel(end) : '?'}`;
}

function buildSearchIndex(states: State[]): SearchItem[] {
  const index: SearchItem[] = [];

  for (const state of states) {
    if (state.region === 'giris') {
      index.push({
        id: `guide-${state.id}`,
        kind: 'Rehber',
        title: state.name,
        sub: `Atlas rehberi · ${(state.essay ?? []).length} bölüm`,
        key: canon(`${state.name} ${state.short ?? ''} ${(state.aliases ?? []).join(' ')}`),
        href: hrefGuide(),
      });
      continue;
    }

    index.push({
      id: `state-${state.id}`,
      kind: 'Devlet',
      title: state.name,
      sub: `${yearLabel(state.start)} – ${yearLabel(state.end)}`,
      key: canon(`${state.name} ${state.short ?? ''} ${(state.aliases ?? []).join(' ')}`),
      href: hrefState(state.id),
    });

    for (const ruler of state.rulers ?? []) {
      index.push({
        id: `ruler-${ruler.id}`,
        kind: 'Hükümdar',
        title: ruler.name,
        sub: `${state.name} · ${reignLabel(ruler) || ruler.title}`,
        key: canon(
          `${ruler.name} ${(ruler.aliases ?? []).join(' ')} ${state.name} ${ruler.title} ${(ruler.traits ?? []).join(' ')}`
        ),
        href: hrefRuler(state.id, ruler.id),
      });

      (ruler.wars ?? []).forEach((war, i) => {
        index.push({
          id: `war-${ruler.id}-${i}`,
          kind: 'Savaş',
          title: war.name,
          // `when` boş olabilir (kayıtta tarih ifadesi yok): boş parantez
          // çıkmasın diye yalnız dolu alanlar birleştirilir.
          sub: [`${ruler.name}${war.when ? ` (${war.when})` : ''}`, war.foe]
            .filter(Boolean)
            .join(' · '),
          key: canon(`${war.name} ${war.foe} ${war.when} ${ruler.name} ${state.name} ${war.note}`),
          href: hrefWar(state.id, ruler.id, i + 1, war.name),
        });
      });

      const personGroups: { role: PersonRole; people: Person[] }[] = [
        { role: 'es', people: ruler.wives ?? [] },
        { role: 'cocuk', people: ruler.children ?? [] },
      ];
      for (const { role, people } of personGroups) {
        people.forEach((person, i) => {
          // Notu boş olan kişide ayraç sarkmasın: ölçüm 4 kişide not yok.
          const note = person.note.trim();
          index.push({
            id: `person-${ruler.id}-${role}-${i}`,
            kind: role === 'es' ? 'Eş' : 'Çocuk',
            title: person.name,
            sub: note ? `${ruler.name} ailesi · ${note}` : `${ruler.name} ailesi · not yazılmamış`,
            key: canon(`${person.name} ${ruler.name} ${state.name} ${person.note}`),
            href: hrefPerson(state.id, ruler.id, role, i + 1, person.name),
          });
        });
      }
    }
  }

  return index;
}

export interface StateFilter {
  region: Region | null;
  query: string;
}

/**
 * Devlet süzgeci: ad, diğer adlar ve başkent ile hükümdar adları üzerinden
 * arar. Açılış sayfasının bölge pilleri ve metin kutusu bunu sürer. Arama
 * önerileri bu işlevi kullanmaz; kendi anahtar eşleştirmesini yapar
 * (`buildSearchIndex`).
 */
export function filterStates(states: State[], filter: StateFilter): State[] {
  const query = canon(filter.query.trim());
  return states.filter((state) => {
    if (filter.region && state.region !== filter.region) return false;
    if (!query) return true;
    const stateKey = canon(`${state.name} ${(state.aliases ?? []).join(' ')} ${state.capital}`);
    const rulerMatch = (state.rulers ?? []).some((r) =>
      canon(`${r.name} ${(r.aliases ?? []).join(' ')}`).includes(query)
    );
    return stateKey.includes(query) || rulerMatch;
  });
}

/**
 * Çocuk kaydındaki `mother` metnini eş listesindeki bir kayda bağlar. Ölçüm:
 * anne adı dolu 105 çocuk kaydının 45'i eşleşiyor, 60'ı eşleşmiyor
 * (ör. "Mal Hatun?" ↔ "Mal Hatun bint Ömer Bey"). Eşleşmeyen durumda null
 * döner; çağıran ham metni gösterip eşleşmediğini yazmalıdır.
 */
export function resolveWife(ruler: Ruler, mother: string): Person | null {
  const raw = mother.trim();
  if (!raw) return null;
  // Yer tutucu metin ("kayıtlarda adı geçmiyor") gerçek bir kişiyi göstermez;
  // eşitlik kurulursa gerçek olmayan bir "annesi bu kayıt" iddiası doğardı.
  // Ölçüm: bugün 3 eşin adı yer tutucu, hiçbir çocuğun anne alanı değil (0/105),
  // yani bu dal veriyle tetiklenmiyor; kayıt değişirse sessizce yanlış bağ kurulmaz.
  if (isPlaceholderName(raw)) return null;
  const wives = ruler.wives ?? [];
  const exact = wives.filter((wife) => canon(wife.name) === canon(raw));
  if (exact.length) return exact.length === 1 ? exact[0] : null;
  const loose = looseKey(raw);
  const matches = loose ? wives.filter((wife) => looseKey(wife.name) === loose) : [];
  return matches.length === 1 ? matches[0] : null;
}

/**
 * Sıra+slug adresini listeye çözer. Gramer iki adımlıdır: önce adresteki sıra
 * denenir (`liste[sıra-1]`), slug tutmuyorsa listede **tekil** slug eşleşmesi
 * aranır. Slug birden çok kayıtta tekrarlıyorsa sıra dışında seçim yapılmaz ve
 * -1 döner: paylaşılan bağlantının sessizce başka bir kaydı göstermesi,
 * "bulunamadı" demekten kötüdür. Ölçüm: bugün aynı hükümdarın listesinde slug'ı
 * tekrar eden iki kayıt yok (mevcut veri denetimi bunu doğrular), yani bu dal veriyle
 * tetiklenmiyor.
 */
function resolveIndex<T>(
  list: readonly T[],
  position: number,
  wanted: string,
  nameOf: (item: T) => string
): number {
  if (position >= 1 && position <= list.length && slug(nameOf(list[position - 1])) === wanted) {
    return position - 1;
  }
  let hit = -1;
  for (let i = 0; i < list.length; i += 1) {
    if (slug(nameOf(list[i])) !== wanted) continue;
    if (hit >= 0) return -1;
    hit = i;
  }
  return hit;
}

/**
 * Savaşı adresteki sıra ve slug'dan çözer. Slug kaydın doğrulanabilir kimliğidir:
 * paylaşılan bağlantı, kayıt sırası değişse bile doğru savaşa düşer. Dönen
 * `index` kanonik sıradır; adresteki sıradan farklıysa çağıran adresi düzeltir.
 * Çözülemeyen adres için null döner; sayfa "bulunamadı" der.
 */
export function resolveWar(
  ruler: Ruler,
  position: number,
  slugPart: string
): { war: War; index: number } | null {
  const wars = ruler.wars ?? [];
  const at = resolveIndex(wars, position, slug(slugPart), (war) => war.name);
  return at < 0 ? null : { war: wars[at], index: at + 1 };
}

/** Kişiyi rolü, sırası ve slug'ından çözer; sözleşmesi `resolveWar` ile aynıdır. */
export function resolvePerson(
  ruler: Ruler,
  role: PersonRole,
  position: number,
  slugPart: string
): { person: Person; index: number } | null {
  const people = role === 'es' ? (ruler.wives ?? []) : (ruler.children ?? []);
  const at = resolveIndex(people, position, slug(slugPart), (person) => person.name);
  return at < 0 ? null : { person: people[at], index: at + 1 };
}

export type PersonRulerLink =
  | { kind: 'single'; state: State; ruler: Ruler }
  | { kind: 'ambiguous'; candidates: { state: State; ruler: Ruler }[] }
  | { kind: 'placeholder' }
  | { kind: 'none' };

/**
 * Kişi adı bir hükümdar adıyla aynıysa köprü kurar. Yer tutucu adlar
 * ("kayıtlarda adı geçmiyor") gerçek bir kişiyi göstermediği için bağlanmaz.
 */
export function personRulerLink(index: AtlasIndex, name: string): PersonRulerLink {
  if (isPlaceholderName(name)) return { kind: 'placeholder' };
  const matches = index.rulerByName.get(canon(name)) ?? [];
  if (matches.length === 0) return { kind: 'none' };
  if (matches.length === 1) return { kind: 'single', ...matches[0] };
  return { kind: 'ambiguous', candidates: matches };
}

export interface AttributedWar {
  ruler: Ruler;
  /** Savaşın hükümdarın listesindeki 1 tabanlı sırası (adres için). */
  index: number;
  war: War;
}

/**
 * Devletin bütün savaşları, hükümdar sırasına göre. `when` serbest metin
 * olduğu için (ölçüm: 504 savaşın 172'si tek bir yıl değil) tarihe göre
 * sıralanmaz.
 */
export function stateWars(state: State): AttributedWar[] {
  const list: AttributedWar[] = [];
  for (const ruler of state.rulers ?? []) {
    (ruler.wars ?? []).forEach((war, i) => list.push({ ruler, index: i + 1, war }));
  }
  return list;
}

export interface WarRecord {
  total: number;
  byResult: Record<BattleResult, number>;
}

/** Gösterim sırası; rozetler her yüzeyde aynı sırayla çıksın diye tek kaynak. */
export const RESULT_ORDER: BattleResult[] = ['zafer', 'yenilgi', 'sonucsuz', 'antlasma', 'belirsiz'];

export function warRecord(wars: War[]): WarRecord {
  const byResult: Record<BattleResult, number> = {
    zafer: 0,
    yenilgi: 0,
    sonucsuz: 0,
    antlasma: 0,
    belirsiz: 0,
  };
  for (const war of wars) byResult[war.result] += 1;
  return { total: wars.length, byResult };
}

export function stateWarRecord(state: State): WarRecord {
  return warRecord(stateWars(state).map((entry) => entry.war));
}
