# Veri Köken ve Yaşam Döngüsü Haritası (Data Provenance)

Bu doküman, `data/raw/*.json` dosyalarının kökenini ve harici kaynakları (`data/sources/`) belgeler.

---

## 1. Ham Veri Dosyaları ve Kapsam

| Ham Dosya (`data/raw/`) | Devlet Sayısı | Hükümdar | Durum & Notlar |
|---|---|---|---|
| `a-giris.json` | — | 0 | Giriş / Okuma yönergesi kaydı (`id: okuma`). Türk devleti değildir; zaman şeridine ve sayımlara girmez. |
| `a-bati.json` | 9 | 36 | Avrupa Hun, Avar, Hazar, Bulgar, Peçenek, Kıpçak. |
| `b-bozkir-hun.json` | 3 | 50 | Asya Hun, Kuzey Hun, Güney Hun (`asya-hun-teoman` vb.). |
| `c-gokturk.json` | 6 | 19 | Göktürk kağanlıkları, Türgiş, Karluk. |
| `d-uygur-kirgiz.json` | 4 | 28 | Uygur, Yenisey Kırgız, Kimek, İdikut (Koço). |
| `e-turkistan-islam.json`| 3 | 37 | Karahanlı, Gazneli, Harzemşah. Metin kaynakları `data/sources/e-turkistan-islam/` içinde. |
| `f-altin-orda.json` | 4 | 25 | Altın Orda, Kazak, Nogay, Ak Orda. |
| `g-kuzey-hanliklari.json`| 6 | 22 | Kırım, Kazan, Astrahan, Sibir, Kasım, Delhi. |
| `h-timur-ortaasya.json` | 7 | 79 | Timur, Bâbür, Özbek, Buhara, Hive, Hokand, Çağatay. |
| `i-iran-selcuklu.json` | 7 | 35 | Büyük Selçuklu, Kirman Selçuklu, Suriye Selçuklu, İldeniz, Salgur, Tolun, İhşid. Kaynaklar `data/sources/i-iran-selcuklu/`. |
| `j-iran-gec.json` | 5 | 8 | Akkoyunlu, Karakoyunlu, Safevî, Avşar, Kaçar. |
| `k-ilhanli-memluk.json` | 5 | 23 | İlhanlı, Memlük, Zengî, Eftalit, Celâyirli. |
| `l-anadolu-selcuklu.json`| 7 | 56 | Anadolu Selçuklu, Dânişmendli, Saltuklu, Mengücek, Artuklu, Ahlatşah, Çaka. |
| `m-beylikler-bati.json` | 8 | 46 | Batı Anadolu Beylikleri (Karesi, Saruhan, Aydın, Menteşe, Germiyan, Hamid, Eşref, Teke). |
| `n-beylikler-dogu.json` | 5 | 21 | Karaman, Dulkadir, Ramazan, Candar, Eretna. |
| `o-osmanli.json` | 1 | 40 | Osmanlı Devleti (36 padişah + 4 taht iddiacısı). |
| **TOPLAM** | **80 devlet + 1 rehber** | **525** | **504 savaş, 148 eş, 556 çocuk** |

---

## 2. Kanonik Veri Deposu

Tüm tarihsel veriler `data/raw/*.json` altında kanonik olarak saklanmaktadır. Uygulama (`src/lib/data/atlas.ts`), bu dosyaları doğrudan Vite `import.meta.glob` ile yükler ve Zod şemasıyla (`src/schemas/atlas.schema.ts`) doğrular.

---

## 3. Kaynak ve Atıf Durumu (`data/sources/`)

- `data/raw` içindeki 834 kaynak referansının dağılımı (yinelenen URL'ler ayrı referanstır):
  - **TDV İslâm Ansiklopedisi:** 697
  - **Vikipedi:** 67
  - **Encyclopaedia Britannica:** 62
  - **Akademik yayın, birincil metin ve üniversite ders notu:** 8
- Vikipedi ağırlığı Xiongnu/Hun bölümünde toplanır (`asya-hun`, `güney-hun`, `kuzey-hun`): TDV bireysel şanyüler için ayrı madde vermez, ctext.org ise bot erişimini yasaklar. Bu kayıtlarda Vikipedi, doğrulanabilir tek kaynak olduğu için korunmuştur; yerine geçecek doğrulanmış bir kaynak uydurulmamıştır. Uygur, Kırgız, Kimek, Avar ve Hazar kayıtlarındaki geniş Vikipedi sayfaları ise ilgili TDV kavim maddesiyle (UYGURLAR, KIRGIZLAR, KİMEK, AVARLAR, HAZARLAR) değiştirilmiştir.
- Yerel metin arşivleri:
  - `data/sources/e-turkistan-islam/` (29 kaynak metni / HTML dökümü + `SOURCES.md`)
  - `data/sources/i-iran-selcuklu/` (19 kaynak metni / ham JSON + `SOURCES.md`)
- Kalan 14 blokta metinler `data/raw/*.json` içindeki `sources` dizisinde doğrudan URL ve başlık olarak tutulmaktadır.

---

## 4. Kalite Kapısı ve Derleme Zinciri

```
data/raw/*.json ──► npm run validate (Zod StateSchema tip doğrulaması)
                         │
                         ▼ (Exit code 0 ise)
                    npm run check (Svelte 5 tip denetimi)
                         │
                         ▼
                    npm run build (Vite üretim derlemesi)
```

1. **Veri Doğrulama:** `npm run validate` (80 devlet + 1 rehber, 525 hükümdar şema kontrolü).
2. **Tip Kontrolü:** `npm run check` (Svelte ve TypeScript denetimi).
3. **Uygulama Derleme:** `npm run build` (Vite prodüksiyon derlemesi).
