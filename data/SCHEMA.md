# Atlas veri şeması

Bu klasördeki `raw/*.json` dosyalarının her biri **devlet nesnelerinden oluşan bir dizi**
(`[ {...}, {...} ]`) içerir. Uygulama (`src/lib/data/atlas.ts`), bu dosyaları doğrudan `import.meta.glob` ile yükler ve Zod şemasıyla (`src/schemas/atlas.schema.ts`) doğrular. Veri şeması bu belgede sabittir.

## Dil ve üslup kuralları

- Her metin **Türkçe**. Sade, ders kitabı klişesi olmayan, ansiklopedik üslup.
- Uydurma yok. Bir isim, yıl veya olay kaynakta yoksa `null` / boş dizi bırak ve
  `...Note` alanına "kayıtlarda yok" gibi bir açıklama yaz. **Asla tahminle isim üretme.**
- Rivayet ve tartışma ayrı yerde durur: `legends` (rivayet), `certainty` (kişi için),
  `confidence` / `confidenceNote` (devlet için), `result: "belirsiz"` (savaş için).
- Yıl: sayı. MÖ için negatif (`-220`). Yaklaşık yıl negatif/sayı olarak verilir,
  yaklaşıklık `startNote`/`reignNote` içinde yazılır.
- Kaynak zorunlu: her devlette en az 1, her hükümdarda en az 1 kaynak. Tercih sırası:
  TDV İslâm Ansiklopedisi (`https://islamansiklopedisi.org.tr/...`), Britannica,
  İngilizce/Türkçe akademik maddeler, üniversite sayfaları, ansiklopedik maddeler.

## Devlet nesnesi

| alan | tip | zorunlu | not |
|---|---|---|---|
| `id` | string | ✓ | küçük harf, tireli, dosya içinde ve tüm atlasta tekil (`gokturk`, `kirim-hanligi`) |
| `name` | string | ✓ | tam ad |
| `short` | string | ✓ | haritada/etiketlerde çıkacak kısa ad |
| `aliases` | string[] | | arama için diğer adlar |
| `region` | string | ✓ | `giris` (atlas rehberi için), `bozkir`, `turkistan`, `bati`, `kuzey`, `iran`, `anadolu`, `diger` |
| `start`, `end` | number | ✓ | kuruluş / yıkılış yılı (MÖ negatif) |
| `startNote`, `endNote` | string | | tarih tartışmalıysa alternatifler |
| `capital` | string | | merkez; yoksa "sabit merkez kayıtlarda yok" gibi |
| `religion` | string | | inanç; zorlama yok |
| `confidence` | string | | `kayit` (varsayılan), `tartismali`, `rivayet` |
| `confidenceNote` | string | | neden tartışmalı |
| `summary` | string | ✓ | 2-4 cümle, kuruluş-yükseliş-yıkılış |
| `legacy` | string | | tarihe bıraktığı iz |
| `essay` | string[] | | uzun anlatı paragrafları (büyük devletlerde ve kurucu dönüm noktası yapılarda, 2-6 paragraf) |
| `sources` | kaynak[] | ✓ | `{title, url}` |
| `rulers` | hükümdar[] | ✓ | kronolojik sıra (yalnızca `giris` kartında boş olabilir) |

## Hükümdar nesnesi

| alan | tip | zorunlu | not |
|---|---|---|---|
| `id` | string | ✓ | `devlet-id` + `-` + kısa ad (`osmanli-fatih`) veya tekil tarihsel slug (`osman-i`, `ertugrul`) |
| `name` | string | ✓ | kaynakta geçtiği biçim |
| `aliases` | string[] | | arama için |
| `title` | string | | kağan, han, sultan, padişah, bey, yabgu… |
| `birth`, `death` | number\|null | | bilinmiyorsa `null` |
| `birthNote`, `deathNote` | string | | "kayıtlarda yok" / "yaklaşık 1495" |
| `reign` | [number, number\|null] | ✓ | başlangıç ve bitiş (sürüyorsa/ölümde bitmişse `null`) |
| `reignNote` | string | | hükümdarlık tartışması |
| `summary` | string | ✓ | 1-3 cümle |
| `traits` | string[] | | bilinen özellikler (kısa etiket ya da kısa cümle), boşsa `[]` |
| `contribution` | string | | ülkesine katkısı |
| `harm` | string | | bedeli/zararı |
| `wives` | kişi[] | ✓ | `children` ile aynı `kişi` yapısı; kayıtlarda `mother` alanı hiç doldurulmamıştır |
| `children` | kişi[] | ✓ | `{name, mother, note, certainty}` |
| `familyNotes` | string[] | – | Sayı veya akrabalık bilgisi var ama kimliği ayrı kişi kaydı olarak doğrulanamayan aile bilgileri; eş/çocuk sayısına katılmaz |
| `wars` | savaş[] | ✓ | aşağıdaki tablo |
| `legends` | string[] | | rivayetler, sonradan eklenen anlatılar |
| `claim` | boolean | | taht iddiası olup klasik sıralamaya girmeyen kişi (ör. Cem Sultan) |
| `sources` | kaynak[] | ✓ | `{title, url}` |

`kişi`: `mother` ve `note` boş olabilir, `certainty` verilmezse `kesin` sayılır;
değerleri `kesin`, `olasi`, `muhtemel`, `tartismali`, `rivayet`.

`savaş`: `{name, when, foe, result, note}` — `result` şunlardan biri:
`zafer`, `yenilgi`, `sonucsuz`, `belirsiz`, `antlasma`.

## Örnek (kısaltılmış)

```json
[
  {
    "id": "ornek-devlet",
    "name": "Örnek Devleti",
    "short": "Örnek",
    "aliases": ["Alternatif ad"],
    "region": "bozkir",
    "start": 552,
    "end": 630,
    "startNote": "Kuruluş 552; bazı kaynaklar 551 der.",
    "capital": "Ötüken",
    "religion": "Gök Tanrı inancı",
    "confidence": "kayit",
    "summary": "İki cümlelik özet.",
    "legacy": "Bir cümlelik miras.",
    "essay": ["Uzun paragraf."],
    "sources": [{"title": "TDV, TÜRK", "url": "https://islamansiklopedisi.org.tr/turk"}],
    "rulers": [
      {
        "id": "ornek-devlet-kagan",
        "name": "Örnek Kağan",
        "title": "kağan",
        "birth": null,
        "birthNote": "kayıtlarda yok",
        "death": 630,
        "reign": [552, 630],
        "reignNote": "",
        "summary": "Kurucu.",
        "traits": ["askerî örgütlenme", "Çin ile denge siyaseti"],
        "contribution": "Devleti kurdu.",
        "harm": "",
        "wives": [{"name": "Örnek Hatun", "note": "Çin prensesi olabilir", "certainty": "tartismali"}],
        "children": [{"name": "Oğul Kağan", "mother": "Örnek Hatun", "note": "", "certainty": "kesin"}],
        "wars": [{"name": "Örnek Savaşı", "when": "600", "foe": "Komşu", "result": "zafer", "note": "Kaynak adı vermez."}],
        "legends": ["Sonradan yazılan anlatıya göre…"],
        "sources": [{"title": "TDV, TÜRK", "url": "https://islamansiklopedisi.org.tr/turk"}]
      }
    ]
  }
]
```

## Kontrol

Yazdıktan sonra mutlaka çalıştır:

```bash
npm run validate
```

Hata varsa düzelt, geçene kadar tekrarla.
