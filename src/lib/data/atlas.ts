import {
  StateSchema,
  type State,
  type Milestone,
  type Region,
  type BattleResult,
  type Certainty,
  type Confidence,
} from '../../schemas/atlas.schema';

export interface RegionInfo {
  id: Region;
  name: string;
  color: string;
  glow: string;
}

const REGIONS: RegionInfo[] = [
  { id: 'giris', name: 'Nasıl okunur', color: '#8a6a30', glow: 'rgba(138, 106, 48, 0.20)' },
  { id: 'bozkir', name: 'Bozkır ve İç Asya', color: '#b5651d', glow: 'rgba(181, 101, 29, 0.20)' },
  { id: 'turkistan', name: 'Türkistan', color: '#14776b', glow: 'rgba(20, 119, 107, 0.20)' },
  { id: 'bati', name: 'Hazar, Karadeniz, Avrupa', color: '#35558a', glow: 'rgba(53, 85, 138, 0.20)' },
  { id: 'kuzey', name: 'İdil, Kırım, kuzey hanlıkları', color: '#4f7a33', glow: 'rgba(79, 122, 51, 0.20)' },
  { id: 'iran', name: 'İran, Horasan, Hindistan', color: '#a83a5b', glow: 'rgba(168, 58, 91, 0.20)' },
  { id: 'anadolu', name: 'Anadolu, Ortadoğu, Mısır', color: '#977a1c', glow: 'rgba(151, 122, 28, 0.20)' },
  { id: 'diger', name: 'Sınırda ve ilişkili yapılar', color: '#6b6357', glow: 'rgba(107, 99, 87, 0.20)' },
];

export const REGION_MAP = Object.fromEntries(REGIONS.map((r) => [r.id, r]));

/**
 * Rehber kaydı ("Bu atlas nasıl okunur") bir Türk devleti değildir: hükümdarı,
 * başkenti, tarih aralığı yoktur ve JSON'daki start/end değerleri uydurmadır.
 * Bu ayrımı tip düzeyinde tutuyoruz ki sayımlar ve zaman şeridi yanlışlıkla
 * onu bir devlet gibi ele alamasın.
 */
export type RealRegion = Exclude<Region, 'giris'>;

export const DEVLET_REGIONS = REGIONS.filter(
  (r): r is RegionInfo & { id: RealRegion } => r.id !== 'giris'
);

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

export const RESULT_MAP: Record<BattleResult, string> = {
  zafer: 'Zafer',
  yenilgi: 'Yenilgi',
  sonucsuz: 'Sonuçsuz',
  belirsiz: 'Belirsiz',
  antlasma: 'Antlaşma',
};

/** Kişi kaydının kesinlik derecesi etiketleri. */
export const CERTAINTY_MAP: Record<Certainty, string> = {
  kesin: 'Kesin',
  olasi: 'Olası',
  muhtemel: 'Muhtemel',
  tartismali: 'Tartışmalı',
  rivayet: 'Rivayet',
};

/** Devlet kaydının güvenilirlik derecesi etiketleri; devlet sayfası gösterir. */
export const CONFIDENCE_MAP: Record<Confidence, string> = {
  kayit: 'Kayıt',
  tartismali: 'Tartışmalı',
  rivayet: 'Rivayet',
};

export function yearLabel(n: number): string {
  return n < 0 ? `MÖ ${-n}` : String(n);
}

/**
 * `data/raw` altındaki bütün JSON dosyaları tek yükleme yolundan okunur.
 *
 * Dosyalar `import.meta.glob` ile **tembel** (eager olmayan) içe aktarılır: Vite
 * her JSON dosyasını ayrı bir parça (chunk) üretir, böylece girdi JavaScript
 * paketi 1,2 MB tarih verisini gömmez. `preloadAtlas()` bütün parçaları paralel
 * indirir ve sonucu önbelleğe alır; ondan sonraki okumalar senkrondur.
 */
const modules = import.meta.glob('../../../data/raw/*.json') as Record<
  string,
  () => Promise<{ default: unknown }>
>;
let cachedStates: State[] | null = null;

/** Veriyi bir kez yükler; ikinci çağrı önbellekten döner. */
export async function preloadAtlas(): Promise<void> {
  if (cachedStates) return;

  const loaded = await Promise.all(
    Object.entries(modules).map(async ([path, load]) => ({ path, mod: await load() }))
  );

  const allStates: State[] = [];
  for (const { path, mod } of loaded) {
    const rawContent = mod.default;
    const array = Array.isArray(rawContent) ? rawContent : [rawContent];
    for (const item of array) {
      const parsed = StateSchema.safeParse(item);
      if (parsed.success) {
        allStates.push(parsed.data);
      } else {
        // Şemaya uymayan kayıt sessizce atlanmaz, konsola yazılır.
        console.error(`[AtlasLoader] Şema hatası (${path}):`, JSON.stringify(parsed.error.issues));
      }
    }
  }

  // Bölge sırasına, sonra başlangıç yılına göre sırala
  const regionOrder = REGIONS.map((r) => r.id);
  allStates.sort((a, b) => {
    const ra = regionOrder.indexOf(a.region);
    const rb = regionOrder.indexOf(b.region);
    if (ra !== rb) return ra - rb;
    return a.start - b.start || a.id.localeCompare(b.id);
  });

  cachedStates = allStates;
}

/** Önbellekteki kayıtları döndürür; `preloadAtlas()` beklenmeden çağrılamaz. */
export function loadAllStates(): State[] {
  if (!cachedStates) {
    throw new Error(
      '[AtlasLoader] Veri yüklenmeden loadAllStates() çağrıldı; önce preloadAtlas() beklenmelidir.'
    );
  }
  return cachedStates;
}
