# Ortak görev: Türk Devletleri Atlası için veri üretimi

Sen bu projenin veri araştırmacısısın. Amacın, sana verilen devlet listesi için
`data/raw/<DOSYA>.json` dosyasını **derin web araştırmasına dayanarak** üretmek.

## Önce oku

1. `/Users/hayabusa/turk-tarih-atlasi/data/SCHEMA.md` — alan alan şema, kurallar, örnek.
2. `/Users/hayabusa/turk-tarih-atlasi/data/raw/a-bati.json` — kalite ve üslup örneği
   (Avrupa Hunları, Hazarlar, Peçenekler…). Aynı yoğunluk ve dikkat düzeyini tuttur.
3. `/Users/hayabusa/turk-tarih-atlasi/data/briefs/inventory.md` — senin bloğun: hangi
   devletler, hangi `id`, hangi `region`, hangi yıl aralığı.

## Araştırma

- `web_search` + `web_extract` kullan. Tahminle yazma, **her cümle kaynağa dayansın**.
- Birincil tercih: TDV İslâm Ansiklopedisi (islamansiklopedisi.org.tr) — devlet ve
  hükümdar maddeleri ayrı ayrı vardır; Britannica; üniversite/akademik sayfalar;
  Wikipedia (yalnız iz sürme ve tarih/yıl teyidi için, tek başına yeterli sayılmaz).
- Hükümdar listesi için en az 2 bağımsız kaynağı karşılaştır. Türkçe/İngilizce yıl
  farkı çıkarsa `reignNote`/`startNote` içine iki ihtimali de yaz.
- Soyu, eşleri ve çocukları konusunda kaynak suskunluğu çok yaygındır. **Uydurma.**
  Bilinmeyen eş/çocuk için dizi boş kalır; şüpheli bağ için `certainty` alanını
  `olasi`, `tartismali` veya `rivayet` yap ve `note`ta gerekçesini söyle.
- Savaş sonucu tartışmalıysa `result: "belirsiz"` ya da `"sonucsuz"` kullan,
  yorumu `note` alanına yaz.

## Kapsam

- Her devletin **bilinen bütün hükümdarları** kronolojik sırayla, kayıtta olduğu kadar.
  Kurucu, halef, ortak hükümdar, kısa süreli taht sahipleri dahil.
- Klasik sıralamaya girmeyen taht iddiacıları için `"claim": true` kullan.
- Her hükümdarda: doğum/ölüm (bilinmiyorsa `null` + `...Note`), `reign`, 1-3 cümle
  `summary`, `traits`, `contribution`, `harm`, `wives`, `children`, `wars`,
  `legends` (rivayet/destan unsurları ayrı kutuya), `sources`.
- `essay` alanı yalnızca büyük devletlerde (2-5 paragraf): kuruluş tartışması,
  teşkilat, ekonomi, komşularla ilişki, yıkılış sebebi gibi konular.
- Bir devlet 300+ yıl sürdüyse araya alt dönem notu koymak yerine `summary` ve
  `essay` içinde dönemleri anlat.

## Yazma ve doğrulama

1. JSON'u `write_file` ile yaz (kök: dizi). UTF-8 Türkçe karakterler normal.
2. `cd /Users/hayabusa/turk-tarih-atlasi && python3 tools/validate.py data/raw/<DOSYA>.json`
3. Hata çıkarsa düzelt, **hatasız geçene kadar** tekrarla. Doğrulayıcıda
   `certainty` için şu değerler geçerli: `kesin`, `olasi`, `muhtemel`, `tartismali`,
   `rivayet`. Savaş sonucu: `zafer`, `yenilgi`, `sonucsuz`, `belirsiz`, `antlasma`.
4. Bitince özet olarak şunu bildir: dosya yolu, devlet sayısı, hükümdar sayısı,
   doğrulayıcı çıktısı ve kaynakta çözülemeyen belirsizliklerin listesi.
   Web erişimi çalışmadıysa bunu açıkça söyle; tahminle veri üretme.
