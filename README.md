# Türk Devletleri Atlası

Türkçe, kaynak bağlantılı bir tarih atlası. Devletler başlangıç ve bitiş yıllarına göre kronolojik şeritte gösterilir. Bölge süzgeçleri, devlet listesi ve tüm kayıtları kapsayan arama ile bir devletin, hükümdarın, savaşın veya kişi kaydının sayfasına gidilebilir.

Atlasın kapsamı bugün **80 devlet, 713 hükümdar, 791 savaş, 190 eş kaydı ve 763 çocuk kaydıdır**. Ayrıca bir okuma rehberi vardır; devlet sayısına ve şeride girmez. Eş ve çocuk kartları yalnız tekil kişi kayıtlarıdır; kimliği belirlenemeyen topluluklar hükümdar sayfasındaki aile notlarında açıklanır ve bu sayılara katılmaz. Tekil bir kişinin adı bilinmiyorsa kayıtta bu belirsizlik gösterilir. Atlas, eksiksiz soy ağacı iddiasında bulunmaz.

## Çalıştırma

Node.js 22.12 veya üzeri ve npm gereklidir.

```bash
npm ci
npm run dev
```

Üretim çıktısı ve yerel önizleme:

```bash
npm run validate
npm run check
npm run build
npm run preview
```

Tam kalite kapısı: `npm run verify` (veri, Svelte/TypeScript, birim testleri, üretim derlemesi ve masaüstü/mobil tarayıcı testleri). İlk kullanımda `npx playwright install chromium` çalıştırın; macOS üzerinde kurulu Google Chrome varsa testler onu kullanır. `npm audit --audit-level=high` bağımlılık güvenlik kontrolüdür. GitHub Actions aynı kalite kapısını `main` push ve pull request üzerinde çalıştırır.

Kod inceleme bulguları ve doğrulama kapsamı: [verification/review.json](verification/review.json).

Uygulama Vite ile üretilen statik dosyalardan oluşur. Sayfa adresleri `#/...` biçiminde olduğundan statik bir sunucuda sunulabilir; `dist/` klasörü yayın çıktısıdır.

Yayın: site GitHub Pages üzerinde yayınlanır — **https://yucel-gumus.github.io/turk-tarih-atlasi/**. Üretim derlemesi `gh-pages` dalına gönderilir; Vite `base` değeri bu proje alt yoluna göre ayarlıdır (`vite.config.ts`).

## Yayına alma

Önce değişiklikleri commit edin ve `main` dalını push edin; ardından `npm run deploy` çalıştırın. Yayın komutu kalite kapısını çalıştırır, temiz bir kaynak ağacı ister, `gh-pages` geçmişini koruyarak normal Git push yapar. Her yayında `release.json` kaynak commit kimliğini taşır. GitHub Pages derlemesi tamamlandıktan sonra canlı dosyadaki `revision` ile `git rev-parse HEAD` karşılaştırılmalı ve canlı tarayıcı testleri çalıştırılmalıdır:

```bash
ATLAS_BASE_URL=https://yucel-gumus.github.io/turk-tarih-atlasi/ npm run test:e2e
```

## Veri ve kaynaklar

- Kanonik kayıtlar: `data/raw/*.json`
- Alanların açıklaması: `data/SCHEMA.md`
- Veri kökeni ve kapsam: `data/PROVENANCE.md`
- Veri kontrolü: `scripts/validate.ts`

Her devlet ve hükümdar kaydında en az bir kaynak bağlantısı bulunur. Savaş, eş ve çocuk kayıtlarının ayrı kaynak alanı yoktur; sayfaları bağlı hükümdarın kaynaklarını **ilgili kaynaklar** olarak gösterir. Bu bağlantıların her alt iddiayı tek tek kanıtladığı varsayılmamalıdır.

Yeni kayıt eklerken mevcut JSON düzenini izleyin ve `npm run validate` çalıştırın. Doğrulama şemayı, tekil kimlikleri, URL adreslerini, tarih sırasını ve savaş/kişi bağlantılarının çakışmasını denetler. Tarihî doğruluk ise kaynak okuması gerektirir; otomatik denetim bunun yerine geçmez.

Toplu ve adsız aile kayıtlarına ilişkin kararlar [denetim dosyasında](data/FAMILY_AUDIT.md) kaynaklarıyla listelenir.

## Tarih, harita ve aile kayıtlarının yorumu

Zaman makinesi açık yılları ve açık yıl aralıklarını kullanır. Yaklaşık tarih bir kesin yıla çevrilmez; iki saltanat sınırı da kayıtlı hükümdarlar listelenir. Yıl sıfır yoktur. Harita zemini proje içinde yayımlanan Natural Earth vektör verisinden çizilir; API anahtarı veya dış karo servisi gerekmez. Veri kökeni ve lisansı `data/MAP_PROVENANCE.json` içindedir. Harita her devlet için bir yaklaşık başkent veya odak konumu gösterir; başkent değişimlerini ve tarihî sınırları modellemez. Aile görünümündeki “Aynı adlı hükümdar” etiketi ad eşleşmesidir; bağımsız bir kimlik veya tahta çıkış kanıtı değildir. Savaş sayıları hükümdar kayıtları toplamıdır; aynı olay farklı hükümdarlarda geçebilir.

## Uygulama yapısı

- `src/pages/`: şerit, arama, rehber ve ayrıntı sayfaları
- `src/lib/data/`: veri yükleme, sayımlar, arama ve kayıt çözümleme
- `src/lib/router/`: paylaşılabilir hash adresleri
- `src/schemas/`: çalışma zamanı veri şeması

Adres örnekleri: `#/`, `#/?bolge=anadolu`, `#/arama?q=sel%C3%A7uklu`, `#/devlet/osmanli`.

## Lisans

- Kaynak kodu: [MIT](LICENSE)
- Tarihsel içerik ve veri (`data/`, uygulamada gösterilen metinler): [CC BY 4.0](LICENSE-CONTENT.md)
