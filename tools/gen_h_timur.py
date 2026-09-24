#!/usr/bin/env python3
"""Build h-timur-ortaasya.json."""
import json
from pathlib import Path

data = [
  {
    "id": "timur-imparatorlugu",
    "name": "Timur İmparatorluğu",
    "short": "Timurlular",
    "aliases": ["Tîmûriyye", "Gürgâniyye", "Timurid Empire"],
    "region": "turkistan",
    "start": 1370,
    "end": 1507,
    "startNote": "Emir Timur'un 1370'te Belh kurultayında 'Büyük Emir' seçilerek Semerkant tahtına oturmasıyla kuruldu.",
    "endNote": "1507 yılında Özbek Hanı Muhammed Şeybânî'nin Herat'ı zaptetmesiyle sona erdi.",
    "capital": "Semerkant ve Herat",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Yezdî (Zafernâme), Nizâmeddin Şâmî (Zafernâme), İbn Arabşah ve Clavijo sefaretnâmesiyle sabittir.",
    "summary": "Barlas boyuna mensup Emir Timur (Aksak Timur / Timurlenk) tarafından Semerkant merkezli kurulan, Volga'dan Ganj'a, İzmir'den Çin sınırına kadar uzanan cihan imparatorluğu. Timur girdiği hiçbir meydan muharebesinde yenilmedi; 1402'de Ankara Savaşı'nda Yıldırım Bayezid'i mağlup etti. Semerkant'ı dünyanın en göz kamaştırıcı başkentine dönüştürdü. Oğlu Şahruh ve torunu Uluğ Bey devirlerinde astronomi, matematik, mimari ve Çağatay Türk edebiyatı (Ali Şîr Nevâî) Rönesans seviyesine ulaştı. 1507'de Şeybânîler tarafından yıkıldı.",
    "legacy": "Timurlu Rönesansı'nı başlattı; Uluğ Bey Rasathanesi ve Zîc-i Uluğ Bey ile modern gökbiliminin temellerini attı. Ali Şîr Nevâî ve Hüseyin Baykara meclisleriyle Çağatay Türkçesini yüksek bir medeniyet ve edebiyat dili haline getirdi.",
    "essay": [
      "Timur İmparatorluğu, Çağatay Hanlığı'nın kargaşa günlerinde Türkleşmiş Barlas boyu reisi Emîr Taragay'ın oğlu Timur tarafından 1370'te kuruldu. Cengiz soyundan olmadığı için 'Han' unvanını almayıp 'Emîr' unvanıyla yetindi; Cengiz hanedanından bir prensesle evlenerek 'Gürgân' (Han Damadı) lakabını kullandı.",
      "Timur, 35 yıllık hükümdarlığında üç yıllık, beş yıllık ve yedi yıllık seferlerle Altın Orda'yı (Toktamış), Memlükleri (Halep ve Şam), Delhi Sultanlığı'nı ve 1402 Ankara Meydan Muharebesi'nde Osmanlı Devleti'ni (Yıldırım Bayezid) mağlup etti. İzmir'i Rodos Şövalyeleri'nden fethederek Hristiyan dünyasını sarstı. Semerkant'ta Bîbî Hanım Camii ve Gûr-ı Emîr türbesini inşa ettirdi; fethettiği yerlerdeki en mahir sanatkârları ve âlimleri Semerkant'a topladı. 1405'te Çin Seferi'ne giderken Otrar'da vefat etti.",
      "Timur'un oğlu Şahruh (1409-1447) ve eşi Gevher Şad devleti Herat merkezli barış ve sanat çağına taşıdı. Semerkant'ta hüküm süren torunu Uluğ Bey, dünyanın en gelişmiş rasathanesini kurarak yıldız cetvellerini hazırladı. Son büyük dönem Hüseyin Baykara ve çocukluk dostu vezir Ali Şîr Nevâî'nin Herat meclisleriyle geçti. 1507'de Özbeklerin Herat'ı almasıyla imparatorluk çöktü, hanedanın mirası Bâbür Şah ile Hindistan'a taşındı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, TİMURLULAR", "url": "https://islamansiklopedisi.org.tr/timurlular"},
      {"title": "TDV İslâm Ansiklopedisi, TİMUR", "url": "https://islamansiklopedisi.org.tr/timur"},
      {"title": "TDV İslâm Ansiklopedisi, ULUĞ BEY", "url": "https://islamansiklopedisi.org.tr/ulug-bey"}
    ],
    "rulers": [
      {
        "id": "timur-imparatorlugu-timur",
        "name": "Emir Timur",
        "aliases": ["Timur Gürgân", "Timurlenk", "Aksak Timur", "Tamerlane"],
        "title": "Büyük Emir / Gürgân / Sahipkıran",
        "birth": 1336,
        "birthNote": "Keş (Şehr-i Sebz) yakınlarında 1336'da doğdu",
        "death": 1405,
        "deathNote": "Çin Seferi sırasında Otrar'da hastalanarak vefat etti, Gûr-ı Emîr'dedir",
        "reign": [1370, 1405],
        "reignNote": "35 yıl boyunca yenilgi yüzü görmeyen cihan fatihi.",
        "summary": "Tarihin en büyük askeri dahilerinden biri. Asya'nın bir ucundan diğer ucuna ordular yürüttü; girdiği hiçbir savaşı kaybetmedi. Altın Orda, Delhi Sultanlığı, Memlükler ve Osmanlıları mağlup etti. Semerkant'ı eşsiz anıtlarla donattı.",
        "traits": ["Yenilmez mareşal", "Satranç ve tarih üstadı", "İmar hamisi fakat acımasız"],
        "contribution": "Semerkant'ı bir dünya kültür ve mimarlık cennetine çevirdi; Türk-İslam medeniyetinde Timurlu Rönesansı'nı başlattı.",
        "harm": "Altın Orda'yı yıkması Rus knezliklerinin önünü açtı; Osmanlı'yı yenmesi İstanbul'un fethini yarım asır geciktirdi; fethettiği şehirlerdeki kafa kuleleri dehşet saçtı.",
        "wives": [
          {"name": "Saray Mülk Hatun (Büyük Hanım)", "note": "Kazan Han'ın kızı; Timur'a Gürgân unvanını kazandıran baş hatun", "certainty": "kesin"},
          {"name": "Ulcay Türkan Ağa", "note": "Emir Kazgan'ın torunu", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Cihangir Mirza", "mother": "", "note": "Çok sevdiği büyük oğlu, erken vefat etti", "certainty": "kesin"},
          {"name": "Ömer Şeyh Mirza", "mother": "", "note": "Fars valisi", "certainty": "kesin"},
          {"name": "Miranşah", "mother": "", "note": "Azerbaycan valisi, Bâbür'ün dedesi", "certainty": "kesin"},
          {"name": "Şahruh", "mother": "", "note": "Babasından sonra imparatorluğu toparlayan sultan", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kunduzca Muharebesi", "when": "1391", "foe": "Altın Orda Hanlığı (Toktamış)", "result": "zafer", "note": "Volga boylarında Toktamış Han'ın ordusu bozguna uğratıldı."},
          {"name": "Terek Irmağı Muharebesi", "when": "1395", "foe": "Altın Orda Hanlığı (Toktamış)", "result": "zafer", "note": "Altın Orda ordusu tamamen imha edildi, Saray şehri yıkıldı."},
          {"name": "Delhi Muharebesi", "when": "1398", "foe": "Delhi Türk Sultanlığı (Sultan Mahmud)", "result": "zafer", "note": "120 zırhlı savaş filine karşı develere saman bağlayıp yakarak filleri püskürttü, Delhi alındı."},
          {"name": "Ankara Meydan Muharebesi", "when": "1402", "foe": "Osmanlı Devleti (Yıldırım Bayezid)", "result": "zafer", "note": "Çubuk Ovası'nda Yıldırım esir alındı, Anadolu beylikleri yeniden canlandırıldı."},
          {"name": "İzmir Kuşatması", "when": "1402", "foe": "Rodos Şövalyeleri (Hospitalier)", "result": "zafer", "note": "Hristiyan şövalyelerin deniz kalesi 15 günde yerle bir edildi."}
        ],
        "legends": ["Semerkant'taki mezar taşına 'Kim ki benim mezarımı açarsa benden daha korkunç bir istilacıyla karşılaşır' yazıldığı ve Sovyet arkeolog Gerasimov'un mezarı açtığı 22 Haziran 1941 günü Hitler'in SSCB'ye saldırdığı tarihi bir rastlantı olarak anılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, TİMUR", "url": "https://islamansiklopedisi.org.tr/timur"}
        ]
      },
      {
        "id": "timur-imparatorlugu-ulug-bey",
        "name": "Uluğ Bey",
        "aliases": ["Muhammed Taragay Uluğ Bey"],
        "title": "Sultan / Müneccimbaşı / Âlim",
        "birth": 1394,
        "birthNote": "Sultaniye'de 1394'te doğdu",
        "death": 1449,
        "deathNote": "Oğlu Abdüllatif'in azmettirdiği suikastçılar tarafından Semerkant yakınlarında şehit edildi",
        "reign": [1447, 1449],
        "reignNote": "1409'dan itibaren 38 yıl Semerkant valisi ve hükümdarı, 1447-1449 arasında büyük sultan.",
        "summary": "Timur'un torunu, Şahruh'un oğlu. Dünya gökbilim ve matematik tarihinin en büyük dehalarından biri. Semerkant Rasathanesi'ni kurdu, Kadızâde-i Rûmî ve Ali Kuşçu ile birlikte 1018 yıldızın konumunu hatasız hesaplayan 'Zîc-i Uluğ Bey'i hazırladı. Kendi nankör oğlu tarafından şehit edildi.",
        "traits": ["Gökbilimci dahi", "Matematikçi", "Müşfik hükümdar", "İlim aşığı"],
        "contribution": "Semerkant Rasathanesi ve Uluğ Bey Medresesi'ni kurdu; hazırladığı yıldız cetvelleri asırlarca Doğu ve Batı dünyasında temel kaynak oldu; Ali Kuşçu'yu yetiştirdi.",
        "harm": "Devlet idaresinde askeri disiplini bilimsel çalışmalarının gerisinde tuttu; oğlu Abdüllatif'in isyanını bastıramadı.",
        "wives": [],
        "children": [
          {"name": "Abdüllatif", "mother": "", "note": "Babasını katlettiren isyancı oğul", "certainty": "kesin"},
          {"name": "Abdülaziz", "mother": "", "note": "Şehzade", "certainty": "kesin"}
        ],
        "wars": [],
        "legends": ["Ay üzerindeki kraterlerden birine ve bir asteroide uluslararası astronomi birliği tarafından 'Ulugh Beg' adı verilmiştir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ULUĞ BEY", "url": "https://islamansiklopedisi.org.tr/ulug-bey"}
        ]
      }
    ]
  },
  {
    "id": "babur-imparatorlugu",
    "name": "Bâbür İmparatorluğu",
    "short": "Bâbürlüler (Hint Türk Devleti)",
    "aliases": ["Gürgâniyye", "Mughal Empire", "Bâbür Devleti"],
    "region": "turkistan",
    "start": 1526,
    "end": 1857,
    "startNote": "Bâbür Şah'ın 1526 Panipat Meydan Muharebesi'nde İbrâhim Lûdî'yi yenerek Delhi tahtına oturmasıyla kuruldu.",
    "endNote": "1857 Sipahi İsyanı sonrası İngilizlerin son imparator II. Bahadır Şah'ı Rangun'a sürmesiyle sona erdi.",
    "capital": "Agra, Delhi ve Lahor",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Bâbürnâme, Ebü'l-Fazl el-Allâmî (Âyin-i Ekberî / Ekbernâme) ve resmi vakayinâmelerle sabittir.",
    "summary": "Timur'un torunlarından Zahîrüddin Muhammed Bâbür tarafından Hindistan'da kurulan, 330 yılı aşkın süre Hint alt kıtasını yöneten muazzam cihan devleti. Bâbür Şah dünya otobiyografi şaheseri Bâbürnâme'yi Türkçe kaleme aldı. Ekber Şah imparatorluğu kıtasal güce ulaştırdı; Şah Cihan eşi Mümtaz Mahal için mimarlık tarihinin zirvesi Tac Mahal'i inşa ettirdi; Evrengzib devrinde Hindistan'ın tamamına hükmedildi. 1857'de İngiliz sömürgeciliği tarafından yıkıldı.",
    "legacy": "Dünyanın 7 harikasından biri kabul edilen Tac Mahal'i, Delhi Kızıl Kale'yi, Lahor Şâlimâr Bahçeleri'ni ve Bâbürnâme'yi insanlığa armağan etti.",
    "essay": [
      "Bâbür İmparatorluğu, Fergana vadisinde tahtını kaybeden Timur soyundan Zahîrüddin Muhammed Bâbür'ün yılmayan iradesiyle doğdu. Önce Kabil'i fetheden Bâbür, 21 Nisan 1526'da Panipat Meydan Muharebesi'nde yüz bin kişilik ve savaş filleriyle donatılmış Delhi Sultanı İbrâhim Lûdî'nin ordusunu Osmanlı tarzı top ve tüfek taktiğiyle imha ederek Delhi ve Agra'ya hakim oldu.",
      "Bâbür'ün torunu Ekber Şah (1556-1605), Racput prensleriyle akrabalıklar kurarak imparatorluğu merkezileştirdi. Cihangir ve ardından Şah Cihan (1628-1658) devirleri Türk-İslam mimarisinin Hindistan'daki zirvesi oldu. Şah Cihan, 14. çocuğunu doğururken vefat eden eşi Ercümend Bânû Begüm (Mümtaz Mahal) için Agra'da beyaz mermerden bir aşk ve zarafet abidesi olan Tac Mahal'i inşa ettirdi.",
      "Evrengzib (1658-1707) devrinde imparatorluk tüm Hindistan ve Afganistan'ı kapsayarak 150 milyonu aşan nüfusuyla dünyanın en kalabalık ve zengin devleti oldu; Fetâvâ-yı Hindiyye derlendi. Ancak Evrengzib sonrası taht kavgaları ve İngiliz Doğu Hindistan Şirketi'nin sömürgeci yayılması devleti tüketti. 1857 Bağımsızlık İsyanı'nın ardından İngilizler son hükümdar şair II. Bahadır Şah'ı Burma'ya sürgüne göndererek hanedana son verdi."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, BÂBÜRLÜLER", "url": "https://islamansiklopedisi.org.tr/baburluler"},
      {"title": "TDV İslâm Ansiklopedisi, BÂBÜR", "url": "https://islamansiklopedisi.org.tr/babur"},
      {"title": "TDV İslâm Ansiklopedisi, TAC MAHAL", "url": "https://islamansiklopedisi.org.tr/tac-mahal"}
    ],
    "rulers": [
      {
        "id": "babur-imparatorlugu-babur",
        "name": "Bâbür Şah",
        "aliases": ["Zahîrüddin Muhammed Bâbür"],
        "title": "Padişah / Şehinşah",
        "birth": 1483,
        "birthNote": "1483'te Fergana'da Andican'da doğdu",
        "death": 1530,
        "deathNote": "Agra'da vefat etti, vasiyeti üzerine Kabil'deki Bâbür Bahçesi'ne defnedildi",
        "reign": [1526, 1530],
        "reignNote": "1526'da Panipat ile Hindistan tahtını kurdu.",
        "summary": "İmparatorluğun kurucusu, büyük fatih ve edebiyatçı. Fergana'dan sürülmesine rağmen Kabil'i ve ardından Hindistan'ı fethetti. Doğu Türkçesiyle yazdığı hatıratı Bâbürnâme, samimiyeti, coğrafi gözlemleri ve edebi zarafetiyle dünya edebiyatının şaheseridir.",
        "traits": ["Eşsiz edebiyatçı", "Askerî teşkilatçı", "Tabiat aşığı ve samimi"],
        "contribution": "Hindistan'da 330 yıl sürecek muazzam bir Türk imparatorluğu kurdu; Bâbürnâme'yi Türk kültürüne kazandırdı.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [
          {"name": "Mâhım Begüm", "note": "Hümâyun'un annesi, baş hatun", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Hümâyun", "mother": "Mâhım Begüm", "note": "İkinci imparator", "certainty": "kesin"},
          {"name": "Kâmrân Mirza", "mother": "", "note": "Kabil valisi", "certainty": "kesin"},
          {"name": "Gülbeden Begüm", "mother": "", "note": "Hümâyunnâme yazarı ünlü prenses", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Panipat Meydan Muharebesi", "when": "1526", "foe": "Delhi Lûdî Sultanlığı (İbrâhim Lûdî)", "result": "zafer", "note": "Sayıca kat kat üstün Hint ordusu topçu ateşiyle bozguna uğratıldı, Delhi fethedildi."},
          {"name": "Kanhua (Khanwa) Muharebesi", "when": "1527", "foe": "Racput Konfederasyonu (Rana Sanga)", "result": "zafer", "note": "Racput süvarileri imha edildi, Kuzey Hindistan hakimiyeti kesinleşti."}
        ],
        "legends": ["Oğlu Hümâyun ölümcül bir hastalığa yakalandığında yatağının etrafında üç kez dönüp 'Onun canını bana ver, ona şifa ihsan eyle' diye dua ettiği ve oğlunun iyileşip kendisinin hastalanarak vefat ettiği tarihi bir fedakarlık destanıdır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, BÂBÜR", "url": "https://islamansiklopedisi.org.tr/babur"}
        ]
      },
      {
        "id": "babur-imparatorlugu-sah-cihan",
        "name": "Şah Cihan",
        "aliases": ["Şihâbüddin Muhammed Şah Cihan", "Hurrem"],
        "title": "Padişah / Sahipkıran",
        "birth": 1592,
        "birthNote": "1592'de Lahor'da doğdu",
        "death": 1666,
        "deathNote": "Agra Kalesi'nde mahpusken Tac Mahal'e bakarak vefat etti, Tac Mahal'dedir",
        "reign": [1628, 1658],
        "reignNote": "30 yıllık mimarlık ve refah mucizesi.",
        "summary": "Cihangir'in oğlu. İmparatorluğu iktisadi ve mimari zirvesine taşıdı. Erken yaşta kaybettiği eşi Mümtaz Mahal için 22 yılda 20 bin işçi ve mimarla Tac Mahal'i yaptırdı; Delhi'de Cuma Camii ve Şahcihanabad'ı kurdu. Oğlu Evrengzib tarafından tahttan indirilip Agra kalesine hapsedildi.",
        "traits": ["Büyük mimar hükümdar", "Aşk ve sanat timsali", "Estetik deha"],
        "contribution": "Tac Mahal, Agra Kalesi, Delhi Moti Mescid gibi dünya harikalarını inşa ettirdi.",
        "harm": "Devasa inşaat projeleri devlet hazinesini tüketti; oğulları arasında kanlı taht kavgasını engelleyemedi.",
        "wives": [
          {"name": "Ercümend Bânû Begüm (Mümtaz Mahal)", "note": "Adına Tac Mahal yaptırılan efsanevi eşi", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Dârâ Şükûh", "mother": "Mümtaz Mahal", "note": "Âlim veliaht, Evrengzib tarafından katledildi", "certainty": "kesin"},
          {"name": "Evrengzib (Alemgîr)", "mother": "Mümtaz Mahal", "note": "İmparatorluğu devralan oğul", "certainty": "kesin"},
          {"name": "Cihanâra Begüm", "mother": "Mümtaz Mahal", "note": "Babasını hapiste yalnız bırakmayan vefakar kızı", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Dekken Seferleri", "when": "1630-1636", "foe": "Güney Hindistan Sultanlıkları (Ahmednagar, Bicapur)", "result": "zafer", "note": "Dekken bölgesi haraca bağlandı."}
        ],
        "legends": ["Ömrünün son sekiz yılını Agra Kalesi'nin zindanında pencereden Yamuna nehri kıyısındaki Tac Mahal'i seyrederek geçirdiği anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ŞAH CİHAN", "url": "https://islamansiklopedisi.org.tr/sah-cihan"},
          {"title": "TDV İslâm Ansiklopedisi, TAC MAHAL", "url": "https://islamansiklopedisi.org.tr/tac-mahal"}
        ]
      }
    ]
  },
  {
    "id": "ozbek-hanligi",
    "name": "Özbek Hanlığı",
    "short": "Özbek Hanlığı (Ebu'l-Hayr)",
    "aliases": ["Ebu'l-Hayr Hanlığı", "Göçebe Özbek Devleti"],
    "region": "turkistan",
    "start": 1428,
    "end": 1500,
    "startNote": "Cuci'nin oğlu Şiban soyundan Ebu'l-Hayr Han'ın Sibir ve Deşt-i Kıpçak boylarını birleştirmesiyle kuruldu.",
    "endNote": "1500 yılında Muhammed Şeybânî Han'ın Maveraünnehir'e inip Buhara merkezli Şeybânî Devleti'ni kurmasıyla dönüştü.",
    "capital": "Çimki-Tura (Tümen), Sıgnak",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Târîh-i Ebü'l-Hayr Hânî ve Habîbü's-Siyer kronikleriyle sabittir.",
    "summary": "Deşt-i Kıpçak bozkırlarında Cengiz Han'ın torunu Şiban soyundan Ebu'l-Hayr Han tarafından kurulan ilk müstakil Özbek devleti. Adını Altın Orda Hanı Özbek Han'dan alan bu konfederasyon, bozkır Türk ve Moğol boylarını birleştirdi. Sıgnak şehrini başkent yaparak şehirleşmeye yöneldiler. Hanlıktan ayrılan Canibek ve Kerey hanlar Kazak Hanlığı'nı kurarken, Ebu'l-Hayr'ın torunu Şeybânî Han Maveraünnehir'e inerek Timurluları yıktı.",
    "legacy": "Özbek ve Kazak milli kimliklerinin doğduğu tarihi beşik oldu.",
    "essay": [
      "Özbek Hanlığı, 1428 yılında henüz 16 yaşındaki Ebu'l-Hayr Han'ın Sibirya ve İdil boylarındaki Şibanî boylarını birleştirmesiyle doğdu.",
      "Ebu'l-Hayr Han, Siriderya boyundaki Sıgnak, Suzak ve Arkuk şehirlerini fethederek göçebe boyları ticaret merkezlerine bağladı. Timurlu taht kavgalarına müdahil olarak Ebu Said Mirza'ya destek verdi. Ancak 1450'lerin sonunda aşırı merkeziyetçi baskılar sebebiyle Canibek ve Kerey hanlar boylarıyla birlikte ayrılarak Kazak Hanlığı'nın temelini attılar.",
      "Ebu'l-Hayr'ın 1468'de Kalmuklar ve Kazaklarla mücadelesinde ölümünden sonra hanlık dağıldı. Torunu Muhammed Şeybânî Han boyları yeniden toplayarak 1500'de Semerkant ve Buhara'yı fethedip Şeybânîler Hanedanı'nı başlattı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, ÖZBEKLER", "url": "https://islamansiklopedisi.org.tr/ozbekler"},
      {"title": "TDV İslâm Ansiklopedisi, EBÜ'l-HAYR HAN", "url": "https://islamansiklopedisi.org.tr/ebul-hayr-han"}
    ],
    "rulers": [
      {
        "id": "ozbek-hanligi-ebul-hayr",
        "name": "Ebu'l-Hayr Han",
        "aliases": ["Ebü'l-Hayr Han"],
        "title": "Han",
        "birth": 1412,
        "birthNote": "1412'de doğdu",
        "death": 1468,
        "deathNote": "Kazak bozkırında Ak-Kışlak civarında vefat etti",
        "reign": [1428, 1468],
        "reignNote": "40 yıllık kurucu hükümdarlık.",
        "summary": "Özbek Hanlığı'nın kurucusu. 40 yıl boyunca Deşt-i Kıpçak'ta hüküm sürdü. Seyhun havzasını zaptedip Sıgnak'ı başkent yaptı. Torunu Şeybânî Han yoluyla modern Özbekistan'ın temelini attı.",
        "traits": ["Bozkır fatihi", "Teşkilatçı"],
        "contribution": "Özbek siyasi varlığını teşkilatlandırdı, bozkır göçebelerini yerleşik medeniyetle buluşturdu.",
        "harm": "Aşırı sertliği Kazak boylarının kopmasına engel olamadı.",
        "wives": [
          {"name": "Rabia Sultan Begüm", "note": "Uluğ Bey'in kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Şah Budak", "mother": "", "note": "Muhammed Şeybânî Han'ın babası", "certainty": "kesin"},
          {"name": "Haydar Sultan", "mother": "", "note": "Şehzade", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Sıgnak Fethi", "when": "1446", "foe": "Timurlu sınır valileri", "result": "zafer", "note": "Sıgnak ve Siriderya boyları zaptedildi."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, EBÜ'l-HAYR HAN", "url": "https://islamansiklopedisi.org.tr/ebul-hayr-han"}
        ]
      }
    ]
  },
  {
    "id": "buhara-hanligi",
    "name": "Buhara Hanlığı",
    "short": "Buhara Hanlığı (Emirliği)",
    "aliases": ["Buhara Emirliği", "Şeybânîler Hanlığı", "Canidler", "Mangıtlar"],
    "region": "turkistan",
    "start": 1500,
    "end": 1920,
    "startNote": "Muhammed Şeybânî Han'ın Semerkant ve Buhara'yı fethedip Timurlu hakimiyetine son vermesiyle kuruldu.",
    "endNote": "1920 yılında Kızıl Ordu'nun Buhara'yı bombalayıp son emir Alim Han'ı devirmesiyle sona erdi.",
    "capital": "Buhara ve Semerkant",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Buhara vakfiyeleri, Mahmûd b. Velî (Bahrü'l-Esrâr) ve Rus arşivleriyle sabittir.",
    "summary": "Maveraünnehir'de Şeybânîler, Aşterhanîler (Canidler) ve Mangıt hanedanları tarafından 420 yıl yönetilen ulu Türk devleti. Şeybânî Han ve II. Abdullah Han devirlerinde Safevîlere ve Babürlülere karşı zaferler kazanarak Orta Asya'da Sünnî İslam'ın kalesi oldular. Buhara ve Semerkant'ı yüzlerce medrese ve camiyle donatarak 'Kubbetü'l-İslam' unvanını korudular. 1920'de Bolşevik Kızıl Ordu tarafından yıkıldı.",
    "legacy": "Buhara Kelyan Minaresi ve Medresesi, Mir Arab Medresesi ve Semerkant Registan Meydanı'ndaki Şir-Dor ve Tilla-Kari medreselerini insanlığa kazandırdı.",
    "essay": [
      "Buhara Hanlığı, Ebu'l-Hayr Han'ın torunu Muhammed Şeybânî Han'ın 1500 yılında Timurlu şehzadelerini kovarak Semerkant ve Buhara'yı almasıyla kuruldu.",
      "Şeybânîler (1500-1599) devrinde Ubeydullah Han ve II. Abdullah Han İran Safevîlerine karşı amansız bir mücadele vererek Horasan'ı ve Herat'ı fethetti. Ardından gelen Astrahan soyundan Canidler (Aşterhanîler, 1599-1785) döneminde Semerkant Registan Meydanı bugünkü muazzam çinili silüetine kavuştu.",
      "Mangıt Hanedanı (1785-1920) devrinde devlet 'Buhara Emirliği' adını aldı. 1868'de Çarlık Rusyası'nın himayesine giren emirlik, iç işlerinde serbest kaldı. 2 Eylül 1920'de General Frunze komutasındaki Kızıl Ordu Buhara'yı uçaklarla bombalayarak son emir Seyyid Âlim Han'ı Afganistan'a kaçırdı ve devlete son verdi."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, BUHARA HANLIĞI", "url": "https://islamansiklopedisi.org.tr/buhara-hanligi"},
      {"title": "TDV İslâm Ansiklopedisi, ŞEYBÂNÎ HAN", "url": "https://islamansiklopedisi.org.tr/seybani-han"}
    ],
    "rulers": [
      {
        "id": "buhara-hanligi-seybani-han",
        "name": "Muhammed Şeybânî Han",
        "aliases": ["Şibani Han", "Şâhibek Han"],
        "title": "Han / Şâhibek",
        "birth": 1451,
        "birthNote": "1451 doğumlu",
        "death": 1510,
        "deathNote": "Merv Meydan Muharebesi'nde Şah İsmail'e karşı şehit düştü",
        "reign": [1500, 1510],
        "reignNote": "10 yıllık büyük fütuhat saltanatı.",
        "summary": "Hanlığın kurucusu. Timurluları Maveraünnehir'den sürdü, Bâbür'ü Semerkant'ta mağlup etti; Hârizm ve Horasan'ı fethetti. Türkçe divanı olan şair ve fakih bir hükümdardı. 1510 Merv savaşında Şah İsmail tarafından öldürüldü.",
        "traits": ["Fatih", "Âlim hükümdar", "Şair"],
        "contribution": "Maveraünnehir'de 4 asır sürecek Özbek hanlıkları düzenini kurdu.",
        "harm": "Şah İsmail'e karşı tedbirsizce kuşatmadan çıkıp pusuya düşmesi canına ve Horasan'ın kaybına mal oldu.",
        "wives": [],
        "children": [
          {"name": "Muhammed Temür Sultan", "mother": "", "note": "Şehzade", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Sar-ı Pul Muharebesi", "when": "1501", "foe": "Bâbür Şah", "result": "zafer", "note": "Bâbür mağlup edildi, Semerkant kesin olarak zaptedildi."},
          {"name": "Merv Meydan Muharebesi", "when": "1510", "foe": "Safevî Devleti (Şah İsmail)", "result": "yenilgi", "note": "Kızılbaş ordusunun sahte ricat tuzağına düştü, bataklıkta öldürüldü."}
        ],
        "legends": ["Şah İsmail'in onun kafatasını altınla kaplatıp kadeh olarak kullandığı tarihi kaynaklarda zikredilir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ŞEYBÂNÎ HAN", "url": "https://islamansiklopedisi.org.tr/seybani-han"}
        ]
      }
    ]
  },
  {
    "id": "hive-hanligi",
    "name": "Hive Hanlığı",
    "short": "Hive Hanlığı",
    "aliases": ["Hârizm Hanlığı", "Yadigâr Şibanîleri"],
    "region": "turkistan",
    "start": 1511,
    "end": 1920,
    "startNote": "İlbars Han'ın Safevî garnizonunu kovarak Hive merkezli bağımsız hanlık kurmasıyla başladı.",
    "endNote": "1920'de Bolşevik Kızıl Ordu tarafından son han İsfendiyar'ın devrilmesiyle Harezm Sovyet Cumhuriyeti'ne çevrildi.",
    "capital": "Vezir, Ürgenç ve Hive",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Ebulgazi Bahadır Han (Şecere-i Terâkime / Şecere-i Türkî) ve Münis ile Âgehî kronikleriyle sabittir.",
    "summary": "Aral gölü güneyindeki tarihi Hârizm havzasında Cengiz soyundan İlbars Han tarafından kurulan Türkmen ve Özbek devleti. Safevî yayılmasına karşı vatanlarını korudular. Ebulgazi Bahadır Han devrinde Türk boylarının şecerelerini ve Oğuznâme rivayetlerini toplayan 'Şecere-i Terâkime' ve 'Şecere-i Türkî' gibi ölümsüz tarih eserleri yazıldı. İçan Kale mimari kompleksi bugün UNESCO Dünya Mirası olarak ayaktadır. 1920'de Kızıl Ordu tarafından yıkıldı.",
    "legacy": "Hive İçan Kale açık hava müze kentini günümüze ulaştırdı; Ebulgazi Bahadır Han'ın eserleriyle Türk boylarının tarihini ve soy kütüğünü aydınlattı.",
    "essay": [
      "Hive Hanlığı, 1511 yılında Şiban soyundan İlbars Han'ın Hârizm halkının davetiyle Safevî valilerini kılıçtan geçirerek Vezir ve Ürgenç şehirlerini almasıyla kuruldu.",
      "Hanlığın en bilgin hükümdarı Ebulgazi Bahadır Han (1643-1663) oldu. Rus ve Kalmuk baskılarına karşı savaştı; Türk diline aşık bir bilgin olarak Türk boylarının şecerelerini halk Türkçesiyle kaleme aldı. Eserleri Türk tarih yazıcılığının temel taşlarındandır.",
      "1873 yılında General Kaufmann komutasındaki Çarlık Rusyası ordularınca işgal edilerek Rus vassalı yapıldı. 1920'de Sovyet Kızıl Ordusu hanlığı tamamen ortadan kaldırdı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, HİVE HANLIĞI", "url": "https://islamansiklopedisi.org.tr/hive-hanligi"},
      {"title": "TDV İslâm Ansiklopedisi, EBULGAZİ BAHADIR HAN", "url": "https://islamansiklopedisi.org.tr/ebulgazi-bahadir-han"}
    ],
    "rulers": [
      {
        "id": "hive-hanligi-ebulgazi",
        "name": "Ebulgazi Bahadır Han",
        "aliases": ["Ebülfeyz Bahadır Han", "Ebülgazi Han"],
        "title": "Han / Müverrih",
        "birth": 1603,
        "birthNote": "1603'te Ürgenç'te doğdu",
        "death": 1663,
        "deathNote": "Hive'de vefat etti",
        "reign": [1643, 1663],
        "reignNote": "20 yıllık ilim ve gazâ saltanatı.",
        "summary": "Hive Hanı ve büyük Türk tarihçisi. Kalmuklar ve Ruslarla savaştı. Türkmen boylarının tarihini 'Şecere-i Terâkime', Türk hanedanlarını 'Şecere-i Türkî' adlı eserlerinde sade ve akıcı bir Türkçeyle yazarak dünya Türkolojisine en kıymetli hazineleri bıraktı.",
        "traits": ["Müverrih han", "Türkçe aşığı", "Cengaver"],
        "contribution": "Türk boylarının tarih ve şecere hafızasını kayıt altına aldı; Hive'yi imar etti.",
        "harm": "Türkmen boylarına karşı zaman zaman sert tenkil hareketlerine girişti.",
        "wives": [],
        "children": [
          {"name": "Enûşe Han", "mother": "", "note": "Babasının eserini tamamlayan halef", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kalmuk Seferleri", "when": "1646-1655", "foe": "Kalmuk (Oyrat) istilacıları", "result": "zafer", "note": "Bozkırdan gelen Kalmuk yağmaları püskürtüldü."}
        ],
        "legends": ["Kitabının önsözünde 'Bu kitabı Türk, Tacik herkes anlasın diye açık ve arı bir Türk diliyle yazdım, tek bir Farsça veya Arapça lügate ihtiyaç duyulmasın istedim' demesi milli dil bilincinin zirvesidir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, EBULGAZİ BAHADIR HAN", "url": "https://islamansiklopedisi.org.tr/ebulgazi-bahadir-han"}
        ]
      }
    ]
  },
  {
    "id": "hokand-hanligi",
    "name": "Hokand Hanlığı",
    "short": "Hokand Hanlığı",
    "aliases": ["Kokand Hanlığı", "Fergana Hanlığı", "Ming Hanedanı"],
    "region": "turkistan",
    "start": 1709,
    "end": 1876,
    "startNote": "Özbek Ming boyundan Şahruh Bey'in Fergana vadisinde bağımsızlık ilan etmesiyle kuruldu.",
    "endNote": "1876'da Rus Çarlığı generali Skobelev tarafından tamamen ilhak edilerek Fergana vilayeti yapıldı.",
    "capital": "Hokand",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Târîh-i Şahruhî, Molla Âlim Mahdum (Târîh-i Türkistan) ve Rus askeri raporlarıyla sabittir.",
    "summary": "Bereketli Fergana vadisinde (Özbekistan, Kırgızistan, Tacikistan kavşağında) Ming boyu tarafından kurulan zengin hanlık. Âlim Han ve Ömer Han devirlerinde Taşkent, Çimkent ve Türkistan şehirlerini alarak Doğu Türkistan'a (Kaşgar) kadar nüfuz ettiler. Ömer Han ve eşi Nâdire Begüm saraylarında zengin bir edebiyat meclisi kurdular. 1876'da Rus Çarlığı tarafından kanlı bir savaşla ilhak edildi.",
    "legacy": "Hokand Hüdâyâr Han Sarayı'nı ve Fergana ipekçilik/dokuma zanaatını miras bıraktı; Nâdire Begüm divanıyla kadın Türk edebiyatını taçlandırdı.",
    "essay": [
      "Hokand Hanlığı, 1709 yılında Buhara hakimiyetinden ayrılan Özbek Ming boyu beyi Şahruh Bey tarafından zengin Fergana vadisinde kuruldu.",
      "Âlim Han (1798-1810) 'Han' unvanını alarak Taşkent'i fethetti. Halefi Ömer Han (1810-1822) ve eşi büyük şaire Nâdire Begüm dönemi hanlığın kültürel altın çağı oldu. Medreseler açıldı, kanallar kazıldı.",
      "19. yüzyıl ortalarında Çarlık Rusyası'nın güneye inmesiyle General Çernyayev ve Skobelev komutasındaki Rus orduları Taşkent'i (1865) ve ardından Hokand'ı kuşattı. Polat Han'ın halk direnişine rağmen 1876'da hanlık resmen lağvedildi ve toprakları Rus Fergana Valiliği yapıldı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, HOKAND HANLIĞI", "url": "https://islamansiklopedisi.org.tr/hokand-hanligi"}
    ],
    "rulers": [
      {
        "id": "hokand-hanligi-omer-han",
        "name": "Muhammed Ömer Han",
        "aliases": ["Ömer Han", "Emîrü'l-Müslimîn"],
        "title": "Han / Emîrü'l-Müslimîn",
        "birth": 1787,
        "birthNote": "1787'de doğdu",
        "death": 1822,
        "deathNote": "Hokand'da vefat etti",
        "reign": [1810, 1822],
        "reignNote": "12 yıllık altın dönem.",
        "summary": "Hokand Hanlığı'nın en sevilen hükümdarı. Sınırları Seyhun boylarına genişletti. Kendisi 'Emîrî' mahlasıyla Türkçe ve Farsça divanlar yazdı; eşi Nâdire Begüm ile birlikte Hokand'ı bir şiir ve sanat başkenti yaptı.",
        "traits": ["Şair hükümdar", "Halk dostu", "İmar hamisi"],
        "contribution": "Hokand'da büyük medreseler ve kanallar açtırdı; Fergana edebiyat meclislerini kurdu.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [
          {"name": "Mâhlar Âyim (Nâdire Begüm)", "note": "Ünlü Türk şairesi ve naibe hatun", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Muhammed Ali Han (Madali)", "mother": "Nâdire Begüm", "note": "Babasından sonra han oldu", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Türkistan Şehri Fethi", "when": "1814", "foe": "Kazak cüzleri", "result": "zafer", "note": "Hoca Ahmed Yesevî türbesinin bulunduğu Türkistan şehri hanlığa bağlandı."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, HOKAND HANLIĞI", "url": "https://islamansiklopedisi.org.tr/hokand-hanligi"}
        ]
      }
    ]
  }
]

out = Path("/Users/hayabusa/turk-tarih-atlasi/data/raw/h-timur-ortaasya.json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data)} states to {out}")
