# Tamamlama planı

## Ürün amacı

Atlas, Türk tarihiyle ilişkili siyasi yapıları zaman ve bölge üzerinden keşfetmeyi; her devletin hükümdar, savaş ve aile kayıtlarına inip kaynak bağlantılarını görmeyi sağlar. Tarihî sınır haritası veya bütün tarihsel kişilerin eksiksiz envanteri olduğunu iddia etmez.

## Tamamlanan temel işler

- [x] Mevcut veri kapsamını ve kullanıcı akışını inceledim; rehber kaydını devlet sayımından ayrı tuttum.
- [x] Şeritte etiketi görünmeyen devletler için süzülen devlet listesi ekledim.
- [x] Arama önerilerinden tam sonuç sayfasına erişimi ve sonuç türü süzgeçlerini ekledim.
- [x] Arama sıralamasında başlık eşleşmelerini öne aldım.
- [x] Şema dışındaki veri bütünlüğü kontrollerini ekledim.
- [x] Yanlış kategoriye yerleşmiş iki Osmanlı aile kaydını kaldırdım.
- [x] Toplu ve adsız aile satırlarını kaynaklarıyla tek tek denetledim; doğrulanan kişileri ayırdım, toplu sayıları aile notuna taşıdım.
- [x] Denetim kararlarını `data/FAMILY_AUDIT.md` içinde belgeledim ve toplu kişi adları için veri kontrolü ekledim.
- [x] Savaş ve kişi sayfalarında bağlı hükümdarın kaynaklarını gösterdim.
- [x] Küçük ekran üst çubuğunu ve metin kontrastını iyileştirdim.

## Yayın öncesi kabul ölçütleri

- [x] `npm run validate`, `npm run check`, `npm run build` hatasız çalışır.
- [x] Şerit, bölge süzgeci, devlet listesi, arama ve dört ayrıntı sayfası tarayıcıda açılır.
- [x] Klavye ile arama önerisi seçilir; sonuç türü süzgeci ve geri bağlantıları çalışır.
- [x] 390 piksel ekran genişliğinde üst çubuk ve içerik birbirini örtmez, belge yatay taşmaz.

## İçerik için ayrı karar

Eş/çocuk aile denetiminin kapsamı ve açık sınırları `data/FAMILY_AUDIT.md` içinde. Yayın hedefi GitHub Pages olarak belirlenmiştir. 2026-10-09 kod incelemesi, test kapsamı ve içerik sınırlamaları `verification/review.json` içinde; yayın komutu ve canlı sürüm doğrulaması README içinde belgelenmiştir.
