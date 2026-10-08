// Adres grameri. Uygulamada yönlendirme kütüphanesi yok; gezinme tamamen
// `#/...` bağlantıları ve `hashchange` olayı üzerinden yürür. Bu dosya saf
// tutulur (Svelte importu yok) ki adres ayrıştırma tek başına sınanabilsin.
//
// Yol parçaları Türkçe (kullanıcıya görünür), alan adları İngilizce.

import { DEVLET_REGIONS, type RealRegion } from '../data/atlas';
import { slug } from '../text';

/** Kişi kaydının iki rolü; hem URL parçası hem sayfa etiketi buradan türer. */
export type PersonRole = 'es' | 'cocuk';

/** Kişi sayfasının rol başlığı. Tek kaynak: sayfa başlığı ve rozet buradan okur. */
export const PERSON_ROLE_LABEL: Record<PersonRole, string> = {
  es: 'Eş / Hatun',
  cocuk: 'Çocuk / Şehzade',
};

export type Route =
  | { name: 'home'; region: RealRegion | null }
  | { name: 'search'; query: string }
  | { name: 'guide' }
  | { name: 'battles' }
  | { name: 'timeMachine'; year?: number }
  | { name: 'map' }
  | { name: 'state'; stateId: string }
  | { name: 'ruler'; stateId: string; rulerId: string }
  | { name: 'war'; stateId: string; rulerId: string; index: number; slug: string }
  | { name: 'person'; stateId: string; rulerId: string; role: PersonRole; index: number; slug: string }
  | { name: 'notFound'; raw: string };

export const SEG = {
  state: 'devlet',
  ruler: 'hukumdar',
  war: 'savas',
  person: 'kisi',
  guide: 'rehber',
  search: 'arama',
  battles: 'savaslar',
  timeMachine: 'zaman-makinesi',
  map: 'harita',
} as const;

function decode(segment: string): string {
  try {
    return decodeURIComponent(segment);
  } catch {
    // Bozuk yüzde kodlamalı bir bağlantı uygulamayı çökertmesin; ham parça
    // çözümlemede eşleşmez ve sayfa "bulunamadı" gösterir.
    return segment;
  }
}

/** `<sıra>-<slug>` parçasını ayrıştırır. Sıra 1 tabanlıdır. */
function parseIndexSlug(segment: string): { index: number; slug: string } | null {
  const m = /^(\d+)-(.+)$/.exec(segment);
  if (!m) return null;
  const index = Number(m[1]);
  return index >= 1 ? { index, slug: m[2] } : null;
}

/** `?bolge=` süzgeci: tanınmayan bölge hata değil, süzgeçsiz açılış demektir. */
function parseRegion(query: string): RealRegion | null {
  const value = new URLSearchParams(query).get('bolge');
  return DEVLET_REGIONS.some((r) => r.id === value) ? (value as RealRegion) : null;
}

function notFound(hash: string): Route {
  return { name: 'notFound', raw: hash };
}

/**
 * Adresi çözer. Savaş ve kişi adreslerinde hem sıra hem slug zorunludur: sıra
 * tek başına gönderilseydi, veriye bir kayıt eklendiğinde paylaşılmış bağlantı
 * sessizce başka bir kaydı gösterirdi. Slug, kaydın doğrulanabilir kimliğidir;
 * sıra yalnız okunabilirlik ve kanonik adres içindir (bkz. `lookup.ts`).
 */
export function parseHash(hash: string): Route {
  const raw = hash.replace(/^#/, '');
  const queryAt = raw.indexOf('?');
  const path = queryAt < 0 ? raw : raw.slice(0, queryAt);
  const query = queryAt < 0 ? '' : raw.slice(queryAt + 1);
  const parts = path.split('/').filter(Boolean).map(decode);

  if (parts.length === 0) return { name: 'home', region: parseRegion(query) };

  const [head, ...rest] = parts;

  if (head === SEG.guide) {
    return rest.length === 0 ? { name: 'guide' } : notFound(hash);
  }

  if (head === SEG.battles) {
    return rest.length === 0 ? { name: 'battles' } : notFound(hash);
  }

  if (head === SEG.map) {
    return rest.length === 0 ? { name: 'map' } : notFound(hash);
  }

  if (head === SEG.timeMachine) {
    if (rest.length === 0) return { name: 'timeMachine' };
    const parsedYear = Number(rest[0]);
    return Number.isFinite(parsedYear) ? { name: 'timeMachine', year: parsedYear } : { name: 'timeMachine' };
  }

  if (head === SEG.search) {
    return rest.length === 0
      ? { name: 'search', query: new URLSearchParams(query).get('q') ?? '' }
      : notFound(hash);
  }

  if (head !== SEG.state || rest.length === 0) return notFound(hash);

  const [stateId] = rest;
  if (rest.length === 1) return { name: 'state', stateId };
  if (rest[1] !== SEG.ruler || !rest[2]) return notFound(hash);

  const rulerId = rest[2];
  if (rest.length === 3) return { name: 'ruler', stateId, rulerId };

  if (rest.length === 5 && rest[3] === SEG.war) {
    const parsed = parseIndexSlug(rest[4]);
    return parsed ? { name: 'war', stateId, rulerId, ...parsed } : notFound(hash);
  }

  if (rest.length === 6 && rest[3] === SEG.person) {
    const role = rest[4];
    if (role !== 'es' && role !== 'cocuk') return notFound(hash);
    const parsed = parseIndexSlug(rest[5]);
    return parsed ? { name: 'person', stateId, rulerId, role, ...parsed } : notFound(hash);
  }

  return notFound(hash);
}

// ---------------------------------------------------------------------------
// Adres üreticileri. Her bağlantı buradan geçer; slug biçimi tek kaynakta kalır.
// ---------------------------------------------------------------------------

export function hrefHome(region?: RealRegion | null): string {
  return region ? `#/?bolge=${region}` : '#/';
}

export function hrefGuide(): string {
  return `#/${SEG.guide}`;
}

export function hrefBattles(): string {
  return `#/${SEG.battles}`;
}

export function hrefMap(): string {
  return `#/${SEG.map}`;
}

export function hrefTimeMachine(year?: number): string {
  return year !== undefined ? `#/${SEG.timeMachine}/${year}` : `#/${SEG.timeMachine}`;
}

export function hrefSearch(query: string): string {
  return `#/${SEG.search}?${new URLSearchParams({ q: query.trim() })}`;
}

export function hrefState(stateId: string): string {
  return `#/${SEG.state}/${stateId}`;
}

export function hrefRuler(stateId: string, rulerId: string): string {
  return `#/${SEG.state}/${stateId}/${SEG.ruler}/${rulerId}`;
}

export function hrefWar(stateId: string, rulerId: string, index: number, warName: string): string {
  return `${hrefRuler(stateId, rulerId)}/${SEG.war}/${index}-${slug(warName)}`;
}

export function hrefPerson(
  stateId: string,
  rulerId: string,
  role: PersonRole,
  index: number,
  personName: string
): string {
  return `${hrefRuler(stateId, rulerId)}/${SEG.person}/${role}/${index}-${slug(personName)}`;
}
