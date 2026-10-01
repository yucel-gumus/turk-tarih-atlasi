// Atlas metin yardımcıları: arama karşılaştırması, URL parçası üretimi ve
// "kayıtlarda adı geçmiyor" gibi yer tutucu adların ayıklanması tek kaynaktan
// yürür. `route.ts` slug'a, `lookup.ts` eşleştirmeye ihtiyaç duyar; bu yüzden
// ayrı modüldür — aksi halde yönlendirme katmanı ile veri katmanı dairesel
// olarak birbirine bağlanırdı.

/** Türkçe harfleri ASCII karşılıklarına indirger. Modül içi: yalnız `canon` kullanır. */
function fold(s: string): string {
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

/**
 * Arama ve eşleştirme anahtarı: aksanlar indirgenir, kaynaklarda farklı yazılmış
 * ama aynı kişiyi gösteren adlar birleştirilir (Kök-Türk/Göktürk, Vahdettin/
 * Vahdeddin, Mehmet/Mehmed, Beyazıt/Bayezid).
 */
export function canon(s: string): string {
  return fold(s)
    .replaceAll('kokturk', 'gokturk')
    .replaceAll('vahdettin', 'vahdeddin')
    .replaceAll('vahideddin', 'vahdeddin')
    .replaceAll('mehmet', 'mehmed')
    .replaceAll('beyazit', 'bayezid');
}

/**
 * URL parçası: adı küçültür, aksanları indirger, harf ve rakam dışındaki her
 * şeyi tireye çevirir ("Laoshang (Jiyu / Ki-ok)" → "laoshang-jiyu-ki-ok").
 * Savaş ve kişi kayıtlarının id'si olmadığı için paylaşılan bağlantının
 * doğrulanabilir kimliği bu slug'dır. Veri denetimi boş ve çakışan slugları
 * reddeder; her kaydın okunabilir bir URL parçası bulunur.
 */
export function slug(s: string): string {
  return fold(s)
    .replaceAll("'", '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Parantezli ek ve soru işaretini atarak gevşek eşleştirme anahtarı üretir.
 * Anne adı kayıtlarda farklı ayrıntı düzeyinde yazılabiliyor ("Mal Hatun?" ve
 * "Mal Hatun bint Ömer Bey" aynı kişidir).
 */
export function looseKey(s: string): string {
  return canon(s.replace(/\(.*?\)/g, '').replace(/\?/g, ''));
}

const PLACEHOLDER_RE = /(^|\s)(adi gecmiyor|adi yok|bilinmiyor|kayitli degil|isimsiz)(\s|$)/;

/**
 * Yer tutucu adlar bağlantıya dönüşmemelidir. Ölçüm: "kayıtlarda adı geçmiyor"
 * adı 13 kayıtta geçiyor — 7 hükümdar, 3 eş, 3 çocuk. Ad eşitliğine dayanan
 * çapraz bağlantı bunları birbirine bağlarsa okuyucuya anlamsız bir aday listesi
 * sunulur.
 */
export function isPlaceholderName(s: string): boolean {
  return PLACEHOLDER_RE.test(fold(s));
}
