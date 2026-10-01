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
