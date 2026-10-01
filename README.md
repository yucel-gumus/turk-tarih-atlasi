# Türk Devletleri Atlası

Türkçe, kaynak bağlantılı bir tarih atlası. Devletler başlangıç ve bitiş yıllarına göre kronolojik şeritte gösterilir. Bölge süzgeçleri, devlet listesi ve tüm kayıtları kapsayan arama ile bir devletin, hükümdarın, savaşın veya kişi kaydının sayfasına gidilebilir.

Atlasın kapsamı bugün **80 devlet, 525 hükümdar, 504 savaş, 148 eş kaydı ve 556 çocuk kaydıdır**. Ayrıca bir okuma rehberi vardır; devlet sayısına ve şeride girmez. Eş ve çocuk kartları yalnız tekil kişi kayıtlarıdır; kimliği belirlenemeyen topluluklar hükümdar sayfasındaki aile notlarında açıklanır ve bu sayılara katılmaz. Tekil bir kişinin adı bilinmiyorsa kayıtta bu belirsizlik gösterilir. Atlas, eksiksiz soy ağacı iddiasında bulunmaz.

## Çalıştırma

Node.js ve npm gereklidir.

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

Uygulama Vite ile üretilen statik dosyalardan oluşur. Sayfa adresleri `#/...` biçiminde olduğundan statik bir sunucuda sunulabilir; `dist/` klasörü yayın çıktısıdır.

Yayın: site GitHub Pages üzerinde yayınlanır — **https://yucel-gumus.github.io/turk-tarih-atlasi/**. Üretim derlemesi `gh-pages` dalına gönderilir; Vite `base` değeri bu proje alt yoluna göre ayarlıdır (`vite.config.ts`).

## Veri ve kaynaklar

- Kanonik kayıtlar: `data/raw/*.json`
- Alanların açıklaması: `data/SCHEMA.md`
- Veri kökeni ve kapsam: `data/PROVENANCE.md`
- Veri kontrolü: `scripts/validate.ts`

Her devlet ve hükümdar kaydında en az bir kaynak bağlantısı bulunur. Savaş, eş ve çocuk kayıtlarının ayrı kaynak alanı yoktur; sayfaları bağlı hükümdarın kaynaklarını **ilgili kaynaklar** olarak gösterir. Bu bağlantıların her alt iddiayı tek tek kanıtladığı varsayılmamalıdır.

Yeni kayıt eklerken mevcut JSON düzenini izleyin ve `npm run validate` çalıştırın. Doğrulama şemayı, tekil kimlikleri, URL adreslerini, tarih sırasını ve savaş/kişi bağlantılarının çakışmasını denetler. Tarihî doğruluk ise kaynak okuması gerektirir; otomatik denetim bunun yerine geçmez.

Toplu ve adsız aile kayıtlarına ilişkin kararlar [denetim dosyasında](data/FAMILY_AUDIT.md) kaynaklarıyla listelenir.

## Uygulama yapısı

- `src/pages/`: şerit, arama, rehber ve ayrıntı sayfaları
- `src/lib/data/`: veri yükleme, sayımlar, arama ve kayıt çözümleme
- `src/lib/router/`: paylaşılabilir hash adresleri
- `src/schemas/`: çalışma zamanı veri şeması

Adres örnekleri: `#/`, `#/?bolge=anadolu`, `#/arama?q=sel%C3%A7uklu`, `#/devlet/osmanli`.

## Lisans

- Kaynak kodu: [MIT](LICENSE)
- Tarihsel içerik ve veri (`data/`, uygulamada gösterilen metinler): [CC BY 4.0](LICENSE-CONTENT.md)
