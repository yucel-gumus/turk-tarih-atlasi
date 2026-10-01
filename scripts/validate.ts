import fs from 'node:fs';
import path from 'node:path';
import { StateSchema, type State } from '../src/schemas/atlas.schema.ts';
import { slug } from '../src/lib/text.ts';

const rawDir = path.resolve(import.meta.dirname, '../data/raw');
const files = fs.readdirSync(rawDir).filter((f) => f.endsWith('.json')).sort();

// Rehber kaydı (region: 'giris') ayrı sayılır: Türk devleti değildir, hükümdarı
// yoktur ve sayımlara girmemelidir. Ayrım yapılmadan "77 devlet" deniyordu.
let totalDevlet = 0;
let totalRehber = 0;
let totalRulers = 0;
let totalWars = 0;
let totalWives = 0;
let totalChildren = 0;
let hasError = false;
const stateIds = new Set<string>();
const rulerIds = new Set<string>();
const collectivePersonName = /^(?:diğer(?:leri|\s)|toplam\s|çok sayıda\s|küçük yaşta ölen\s|yedi kız$|iki kız evlat$)/i;

function error(location: string, message: string) {
  console.error(`❌ [${location}] ${message}`);
  hasError = true;
}

function checkSources(location: string, sources: State['sources']) {
  if (sources.length === 0) error(location, 'En az bir kaynak gerekli.');
  for (const [index, source] of sources.entries()) {
    if (!source.title.trim()) error(location, `${index + 1}. kaynağın başlığı boş.`);
    try {
      if (new URL(source.url).protocol !== 'https:') {
        error(location, `${index + 1}. kaynak URL adresi HTTPS olmalı: ${source.url}`);
      }
    } catch {
      error(location, `${index + 1}. kaynak URL adresi geçersiz: ${source.url}`);
    }
  }
}

function checkSlugs(location: string, names: string[]) {
  const seen = new Set<string>();
  for (const name of names) {
    if (!name.trim()) error(location, 'Adı boş kayıt var.');
    const key = slug(name);
    if (!key) error(location, `Adres için geçerli slug üretilemedi: ${name}`);
    if (seen.has(key)) error(location, `Aynı slug birden çok kayıtta geçiyor: ${key}`);
    seen.add(key);
  }
}

for (const file of files) {
  const filePath = path.join(rawDir, file);
  let content: unknown;
  try {
    content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  } catch (cause) {
    error(file, `JSON okunamadı: ${String(cause)}`);
    continue;
  }
  const items: unknown[] = Array.isArray(content) ? content : [content];

  let fileDevlet = 0;
  let fileRehber = 0;
  let fileRulers = 0;
  let fileWars = 0;
  let fileWives = 0;
  let fileChildren = 0;

  for (const item of items) {
    const result = StateSchema.safeParse(item);
    if (!result.success) {
      const stateObj = item as Record<string, unknown>;
      console.error(`❌ [${file}] Hata (${stateObj?.name || stateObj?.id}):`, result.error.issues);
      hasError = true;
      continue;
    }
    const state: State = result.data;
    const location = `${file}/${state.id}`;
    if (stateIds.has(state.id)) error(location, `Devlet kimliği tekrar ediyor: ${state.id}`);
    stateIds.add(state.id);
    if (!state.name.trim() || !state.short?.trim()) error(location, 'Devlet adı veya kısa adı boş.');
    if (!state.summary.trim()) error(location, 'Devlet özeti boş.');
    if (state.start > state.end) error(location, 'Başlangıç yılı bitiş yılından sonra.');
    checkSources(location, state.sources);
    if (state.region === 'giris') fileRehber++;
    else fileDevlet++;
    const rulers = state.rulers || [];
    fileRulers += rulers.length;
    for (const r of rulers) {
      const rulerLocation = `${location}/${r.id}`;
      if (rulerIds.has(r.id)) error(rulerLocation, `Hükümdar kimliği tekrar ediyor: ${r.id}`);
      rulerIds.add(r.id);
      if (!r.name.trim() || !r.summary.trim()) error(rulerLocation, 'Hükümdar adı veya özeti boş.');
      if (r.reign[0] != null && r.reign[1] != null && r.reign[0] > r.reign[1]) {
        error(rulerLocation, 'Saltanat başlangıcı bitişinden sonra.');
      }
      checkSources(rulerLocation, r.sources);
      checkSlugs(`${rulerLocation}/savas`, r.wars.map((war) => war.name));
      checkSlugs(`${rulerLocation}/es`, r.wives.map((wife) => wife.name));
      checkSlugs(`${rulerLocation}/cocuk`, r.children.map((child) => child.name));
      for (const person of [...r.wives, ...r.children]) {
        if (collectivePersonName.test(person.name)) {
          error(rulerLocation, `Toplu kayıt kişi adı olarak kullanılamaz: ${person.name}`);
        }
      }
      for (const note of r.familyNotes) {
        if (!note.trim()) error(rulerLocation, 'Boş aile notu var.');
      }
      fileWars += r.wars?.length || 0;
      fileWives += r.wives?.length || 0;
      fileChildren += r.children?.length || 0;
    }
  }

  totalDevlet += fileDevlet;
  totalRehber += fileRehber;
  totalRulers += fileRulers;
  totalWars += fileWars;
  totalWives += fileWives;
  totalChildren += fileChildren;

  const rehberPart = fileRehber > 0 ? ` + ${fileRehber} rehber` : '';
  console.log(
    `${file}: ${fileDevlet} devlet${rehberPart}, ${fileRulers} hükümdar, ${fileWars} savaş, ${fileWives} eş, ${fileChildren} çocuk`
  );
}

if (totalRehber !== 1) error('atlas', `Tam olarak bir rehber bekleniyor; bulunan: ${totalRehber}`);

console.log(
  `\nTOPLAM: ${totalDevlet} devlet + ${totalRehber} rehber (${totalDevlet + totalRehber} kayıt), ` +
    `${totalRulers} hükümdar, ${totalWars} savaş, ${totalWives} eş, ${totalChildren} çocuk`
);

if (hasError) {
  console.error('\nDoğrulama başarısız!');
  process.exit(1);
} else {
  console.log('✅ Şema, tekil kimlikler, bağlantı slugları, tarihler ve kaynaklar doğrulandı.');
  process.exit(0);
}
