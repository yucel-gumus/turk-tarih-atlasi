# Görev blokları

Her blok ayrı bir ajan tarafından yazılır. Dosya yolu ve devlet listesi kesindir:
`id`, `name`, `region`, `start`, `end` alanlarını aşağıdaki gibi kullan (tarih
tartışmalıysa `startNote`/`endNote` ile gerekçelendir).

## Blok B — `data/raw/b-bozkir-hun.json` (region: bozkir)
- `asya-hun` | Asya Hun Devleti (Büyük Hun) | -220..216 — **mevcut kartı oku ve genişlet:**
  `/Users/hayabusa/turk-tarih-atlasi/data/base/asya-hun.json`. Teoman ve Mete için
  oradaki ayrıntıyı koru, Mete'den sonraki şanyüleri (Laoshang, Gunchen, Huhanye,
  Zhizhi, Huduershi ve bilinen diğerleri) ekle. MÖ 209, MÖ 200 Baideng,
  MÖ 36 Zhizhi, MS 48 bölünme bu kartın omurgasıdır.
- `guney-hun` | Güney Hun Devleti | 48..216 | Han vasallığı dönemi, Bi ve sonrası.
- `kuzey-hun` | Kuzey Hun Devleti | 48..155 | Batıya kayış, 91/93 yenilgisi, dağılma.

## Blok C — `data/raw/c-gokturk.json` (region: bozkir)
- `gokturk` | Birinci Göktürk Kağanlığı | 552..630 | Bumin, İstemi (batı ortak),
  Mukan, Taspar, Nivar, İşbara, Tulan, Kimin… Yazıtlar ve Çin kaynakları.
- `dogu-gokturk` | Doğu Göktürk Kağanlığı | 581..630
- `bati-gokturk` | Batı Göktürk Kağanlığı | 581..659 | Tardu, Şikoey, Tong Yabgu…
- `ikinci-gokturk` | İkinci (Kutluk) Göktürk Kağanlığı | 682..745 | Kutluk, Kapgan,
  Bilge, Kül Tigin, Tengri, Ozmış… Orhun Yazıtları.
- `turges` | Türgiş Kağanlığı | 717..766 | Sulu Kağan, 751 Talas.
- `karluk` | Karluk Yabguluğu | 766..940 | Talas sonrası Batı Türkistan, Oğuzlarla ilişki.

## Blok D — `data/raw/d-uygur-kirgiz.json` (region: bozkir)
- `uygur-kaganligi` | Uygur Kağanlığı | 744..840 | Kutluk Bilge Kül, Moyunçur,
  Bögü, Almış… Mani dini, Karabalgasun, 840 Kırgız yenilgisi.
- `yenisey-kirgiz` | Yenisey Kırgız Kağanlığı | 840..1207 | Uygur yıkımı, aarlar/açalar notu.
- `kimek` | Kimek-Kıpçak konfederasyonu | 880..1030 | İrtiş yöresi, Kıpçaklara devir.

## Blok E — `data/raw/e-turkistan-islam.json` (region: turkistan)
- `karahanli` | Karahanlı Devleti | 840..1212 | Bilge Kül Kadir, Satuk Buğra,
  Musa, Ahmed, Yusuf Kadir, Ali Tegin, Tamgaç Buğra Han… Doğu-Batı bölünmesi ayrıntılı.
- `gazneli` | Gazneliler | 963..1187 | Alp Tigin, Sebüktegin, Mahmud, Mesud,
  Mevdud, İbrahim, Behramşah, Hüsrev Melik… Hindistan seferleri.
- `harzemsah` | Harzemşahlar | 1097..1231 | Atsız, İl Arslan, Tekiş, Alâeddin Muhammed,
  Celâleddin; 1220 Moğol yıkımı.

## Blok F — `data/raw/f-altin-orda.json` (region: kuzey; ak-orda: turkistan)
- `altin-orda` | Altın Orda | 1240..1502 | Batu, Berke, Mengü Timur, Tokta,
  Özbek Han, Canıbek, Toktamış, Uluğ Muhammed; 1380 Kulikovo, 1395 Terek.
- `ak-orda` | Ak Orda (Kök Orda) | 1361..1428 | Orda-Ecen soyu, Ebu'l-Hayr öncesi.
- `nogay-ordasi` | Nogay Ordası | 1440..1634 | Edigu soyu, Mangıt beyleri.

## Blok G — `data/raw/g-kuzey-hanliklari.json` (region: kuzey)
- `kirim-hanligi` | Kırım Hanlığı | 1449..1783 | Hacı Giray, Mengli Giray,
  Sahib Giray, I. Devlet Giray, II. Devlet, Selim Giray… 1774/1783 Rus ilhakı.
- `kazan-hanligi` | Kazan Hanlığı | 1438..1552 | Uluğ Muhammed, Mahmud, Safa Giray…
- `astrahan-hanligi` | Astrahan Hanlığı | 1466..1556
- `sibir-hanligi` | Sibir Hanlığı | 1428..1598 | Taibuga/Mar soyu, Küçüm, Yermak.
- `kasim-hanligi` | Kasım Hanlığı | 1452..1681 | Moskova himayesindeki hanlık.

## Blok H — `data/raw/h-timur-ortaasya.json` (region: turkistan)
- `timur-imparatorlugu` | Timur İmparatorluğu | 1370..1507 | Timur, Şahruh,
  Uluğ Bey, Ebu Said, Hüseyin Baykara; 1402 Ankara, 1507 Şeybani sonu.
- `ozbek-hanligi` | Özbek (Şeybani öncesi) Hanlığı | 1428..1500 | Ebu'l-Hayr Han.
- `buhara-hanligi` | Buhara Hanlığı | 1500..1785 | Şeybani, Ubeydullah, Abdullah Han…
- `hive-hanligi` | Hive Hanlığı | 1511..1920 | İlbars, Ebulgazi Bahadır Han…
- `hokand-hanligi` | Hokand Hanlığı | 1709..1876 | Şahruh, Alim, Ömer, Muhammed Ali…
- `babur-imparatorlugu` | Bâbür İmparatorluğu | 1526..1857 | Bâbür, Hümâyun, Ekber,
  Cihangir, Şah Cihan, Evrengzib, Bahadır Şah… 1857 son.

## Blok I — `data/raw/i-iran-selcuklu.json` (region: iran; tulun/ihsid: anadolu)
- `buyuk-selcuklu` | Büyük Selçuklu İmparatorluğu | 1040..1194 | Tuğrul, Alparslan,
  Melikşah, Berkyaruk, Muhammed Tapar, Sencer; 1048 Pasinler, 1071 Malazgirt,
  1141 Katvan.
- `ildenizli` | İldenizliler (Azerbaycan Atabeyliği) | 1136..1225 | Şemseddin İldeniz…
- `salgurlu` | Salgurlular (Fars Atabeyliği) | 1148..1284
- `tulun` | Tolunoğulları | 868..905 | Ahmed b. Tolun, Humâreveyh…
- `ihsid` | İhşîdîler | 935..969 | Muhammed b. Togaç, Kâfûr; 969 Fâtımî sonu.

## Blok J — `data/raw/j-iran-gec.json` (region: iran)
- `akkoyunlu` | Akkoyunlu Devleti | 1378..1508 | Kara Yülük Osman, Uzun Hasan,
  Yakub; 1473 Otlukbeli, 1501 Şurur.
- `karakoyunlu` | Karakoyunlu Devleti | 1380..1469 | Kara Yusuf, Cihan Şah.
- `safevi` | Safevî Devleti | 1501..1736 | Şah İsmail, Tahmasb, I. Abbas,
  Safi, II. Abbas, Hüseyin; 1514 Çaldıran, 1598/1603 savaşları, 1722 İsfahan.
- `avsar` | Avşar Hanedanı (Nâdir Şah) | 1736..1796 | Nâdir Şah, Adil Şah, Şahruh.
- `kacar` | Kaçar Hanedanı | 1796..1925 | Ağa Muhammed, Feth Ali, Nasreddin,
  Muzafferüddin, Ahmed Şah; 1813/1828 Rus savaşları, 1906 Meşrutiyet.

## Blok K — `data/raw/k-ilhanli-memluk.json` (region: diger; memluk: anadolu)
- `ilhanli` | İlhanlılar | 1256..1335 | Hülagû, Abaka, Gazan, Olcaytu, Ebu Said;
  Moğol hanedanı, son dönem Türkleşme ve İslamlaşma notu.
- `celayirli` | Celâyirîler | 1335..1432 | Şeyh Hasan Büzürg, Sultan Ahmed.
- `eftalit` | Eftalitler (Ak Hunlar) | 420..567 | tartışmalı: Türk mü, İranî mi?
- `zengi` | Zengîler | 1127..1250 | İmadeddin Zengi, Nureddin Mahmud; 1144 Urfa.
- `memluk` | Memlük Devleti | 1250..1517 | Kutuz, Baybars, Kalavun, Barsbay,
  Kayıtbay, Kansu Gavri, Tomanbay; 1260 Ayn Calut, 1516 Mercidabık, 1517 Ridaniye.
  Bahri=Kıpçak, Burci=Çerkes ayrımını yaz.

## Blok L — `data/raw/l-anadolu-selcuklu.json` (region: anadolu)
- `anadolu-selcuklu` | Anadolu Selçuklu Devleti | 1077..1308 | Kutalmışoğlu
  Süleyman, I. Kılıç Arslan, Mesud, II. Kılıç Arslan, I. Gıyaseddin Keyhüsrev,
  I. Alâeddin Keykubad, II. Gıyaseddin… 1096 Haçlı, 1176 Miryokefalon, 1243 Kösedağ.
- `danismendli` | Dânişmendliler | 1080..1178 | Dânişmend Gazi, Melik Gazi, Yağıbasan.
- `saltuklu` | Saltuklular | 1072..1202
- `mengucek` | Mengücekliler | 1071..1277
- `artuklu` | Artuklular | 1102..1409 | Hısnkeyfa, Mardin, Harput kolları.
- `ahlatsah` | Ahlatşahlar (Sökmenliler) | 1100..1207
- `caka-beyligi` | Çaka Beyliği | 1081..1093 | İzmir; ilk Türk denizcisi tartışması.

## Blok M — `data/raw/m-beylikler-bati.json` (region: anadolu)
Karesi 1297..1361 · Saruhan 1300..1410 · Aydınoğulları 1308..1426 ·
Menteşeoğulları 1261..1424 · Germiyanoğulları 1300..1429 · Hamidoğulları 1300..1391 ·
Eşrefoğulları 1284..1326 · Tekeoğulları 1321..1424.
`id` olarak `karesi, saruhan, aydin, mentese, germiyan, hamid, esref, teke` kullan.
Her biri için kurucu ve bilinen beyleri, Osmanlı'ya katılma sürecini yaz.

## Blok N — `data/raw/n-beylikler-dogu.json` (region: anadolu)
- `karamangolu` | Karamanoğulları | 1256..1487 | Karamanoğlu Mehmed, Alâeddin Ali,
  II. İbrahim; Türkçe ferman 1277.
- `dulkadir` | Dulkadiroğulları | 1337..1522 | Zeyneddin Karaca, Şah Budak, Alâüddevle.
- `ramazanoglu` | Ramazanoğulları | 1352..1608
- `candaroglu` | Candaroğulları (İsfendiyaroğulları) | 1291..1461
- `eretna` | Eretna Devleti | 1335..1381 | Eretna, Mehmed Bey, Kadı Burhaneddin ayrı not.

## Blok O — `data/raw/o-osmanli.json` (region: anadolu)
- `osmanli` | Osmanlı Devleti | 1299..1922 — **mevcut kartı oku:**
  `/Users/hayabusa/turk-tarih-atlasi/data/base/osmanli.json`; I. Osman ve Orhan
  maddelerindeki ayrıntıyı koru ve bütün padişahları ekle. Klasik sayım 36 padişah:
  Osman I, Orhan, Murad I, Bayezid I, Mehmed I, Murad II, Mehmed II, Bayezid II,
  Selim I, Süleyman I, Selim II, Murad III, Mehmed III, Ahmed I, Mustafa I,
  Osman II, Murad IV, İbrahim, Mehmed IV, Süleyman II, Ahmed II, Mustafa II,
  Ahmed III, Mahmud I, Osman III, Mustafa III, Abdülhamid I, Selim III, Mustafa IV,
  Mahmud II, Abdülmecid, Abdülaziz, Murad V, Abdülhamid II, Mehmed V, Mehmed VI.
  Fetret Devri ve taht iddiacıları `claim: true` ile ayrıca girilsin:
  Süleyman Çelebi, Musa Çelebi, İsa Çelebi, Cem Sultan. Şehzade Mustafa gibi
  padişah olmayan kişiler hükümdar listesine girmez. 1402 Ankara, 1444 Varna,
  1453 İstanbul, 1514 Çaldıran, 1526 Mohaç, 1571 İnebahtı, 1683 Viyana,
  1699 Karlofça, 1774 Küçük Kaynarca, 1839 Tanzimat, 1877-78 Osmanlı-Rus,
  1912-13 Balkan, 1914-18 I. Dünya Savaşı, 1920 Sevr, 1922 saltanatın kaldırılması
  kartın omurgasıdır.
