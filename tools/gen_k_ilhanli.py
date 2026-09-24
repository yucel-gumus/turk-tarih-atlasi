#!/usr/bin/env python3
"""Build k-ilhanli-memluk.json combining ilhanli, memluk, zengi, eftalit, celayirli."""
import json
from pathlib import Path

ROOT = Path("/Users/hayabusa/turk-tarih-atlasi")
ilhanli_raw = json.loads((ROOT / "data" / "states" / "ilhanli.json").read_text(encoding="utf-8"))
memluk_raw = json.loads((ROOT / "data" / "states" / "memluk.json").read_text(encoding="utf-8"))

zengi_state = {
  "id": "zengi",
  "name": "Zengîler",
  "short": "Zengîler (Musul ve Halep Atabeyliği)",
  "aliases": ["Musul Atabegleri", "Halep Atabegleri", "Âl-i Zengî"],
  "region": "anadolu",
  "start": 1127,
  "end": 1250,
  "startNote": "İmâdeddin Zengî'nin 1127'de Musul ve Halep valisi ve Selçuklu atabegi olmasıyla kuruldu.",
  "endNote": "1250 civarında Eyyûbîlerin Halep kolunu, ardından Hülagû'nun Musul'u zaptetmesiyle sona erdi.",
  "capital": "Musul ve Halep",
  "religion": "İslamiyet (Sünnî-Hanefî)",
  "confidence": "kayit",
  "confidenceNote": "İbnü'l-Esîr (et-Târîhu'l-Bâhir fi'd-Devleti'l-Atâbekiyye), İbnü'l-Adîm (Zübdetü'l-Haleb) ile eksiksiz sabittir.",
  "summary": "Selçuklu emiri Aksungur el-Hâcib'in oğlu İmâdeddin Zengî tarafından kurulan, Haçlı Seferleri'ne karşı İslam dünyasının ilk büyük karşı taarruzunu başlatan şanlı Türk devleti. 1144'te Urfa Haçlı Kontluğu'nu fethederek tarihte ilk kez bir Haçlı devletini ortadan kaldırdılar ve II. Haçlı Seferi'ni tetiklediler. Oğlu Nûreddin Mahmud Zengî, Şam ve Mısır'ı birleştirerek Selâhaddîn-i Eyyûbî'yi yetiştirdi; Kudüs'ün fethinin manevi mimarı oldu.",
  "legacy": "Haçlıların yenilmezlik efsanesini yıktı; Selâhaddîn-i Eyyûbî'yi yetiştirip Kudüs fethinin askeri ve manevi zeminini hazırladı. Nûreddin Zengî'nin yaptırdığı Mescid-i Aksâ ahşap kündekârî minberi İslam sanatının şaheseridir.",
  "essay": [
    "Zengîler, Sultan Melikşah'ın has emiri Halep Valisi Aksungur'un oğlu İmâdeddin Zengî tarafından 1127'de Musul merkezli kuruldu. İmâdeddin, Suriye ve el-Cezire'deki dağınık Türk emirlerini tek çatı altında topladı.",
    "24 Aralık 1144'te Urfa'yı fethederek Haçlıların kurduğu ilk devlet olan Urfa Kontluğu'nu tarihten sildi. Bu tarihi zafer Avrupa'yı dehşete düşürdü ve Alman İmparatoru ile Fransız Kralı'nın katıldığı II. Haçlı Seferi'ne yol açtı; Zengîler bu seferi Anadolu ve Şam önlerinde püskürttü.",
    "İmâdeddin'in şehadetinden sonra Halep kolunun başına geçen oğlu el-Melikü'l-Âdil Nûreddin Mahmud Zengî (1146-1174), adaleti ve dindarlığıyla 'Hulefâ-yi Râşidîn' dönemini andıran bir sultan oldu. Şam'ı fethetti, Haçlı ordularını Harim ve İnab'da hezimete uğrattı. Kumandanı Şîrkûh ve yeğeni Selâhaddîn-i Eyyûbî'yi Mısır'a göndererek Fâtımî hilafetine son verdi. Kudüs'ün fethi için Mescid-i Aksâ'ya konulmak üzere muazzam bir ahşap minber yaptırdı. 1174'teki vefatıyla yerini Selâhaddîn-i Eyyûbî aldı."
  ],
  "sources": [
    {"title": "TDV İslâm Ansiklopedisi, ZENGÎLER", "url": "https://islamansiklopedisi.org.tr/zengiler"},
    {"title": "TDV İslâm Ansiklopedisi, NÛREDDİN ZENGÎ", "url": "https://islamansiklopedisi.org.tr/nureddin-zengi"}
  ],
  "rulers": [
    {
      "id": "zengi-imadeddin",
      "name": "İmâdeddin Zengî",
      "aliases": ["İmâdüddin Zengî b. Aksungur"],
      "title": "Atabeg / Melik",
      "birth": 1085,
      "birthNote": "1085 doğumlu",
      "death": 1146,
      "deathNote": "Câber Kalesi kuşatmasında uykudayken kölesi Yârektaş tarafından şehit edildi",
      "reign": [1127, 1146],
      "reignNote": "19 yıllık cihat ve fütuhat saltanatı.",
      "summary": "Zengîler Devleti'nin kurucusu. Haçlılara karşı İslam cihadını örgütleyen ilk büyük lider. 1144'te Urfa Haçlı Kontluğu'nu yıkarak İslam alemine en büyük zaferlerinden birini kazandırdı.",
      "traits": ["Büyük mücahid", "Korkusuz komutan", "Demir disiplinli"],
      "contribution": "Urfa'yı fethedip Haçlı Kontluğu'nu yıktı; Haçlı yayılmasına karşı İslam mukavemet cephesini kurdu.",
      "harm": "Aşırı sert disiplini kölesi tarafından uğradığı suikasta zemin hazırladı.",
      "wives": [
        {"name": "Zümrüd Hatun", "note": "Dımaşk hakimi Börü'nün annesi", "certainty": "kesin"}
      ],
      "children": [
        {"name": "Nûreddin Mahmud", "mother": "", "note": "Halep meliki, büyük adalet timsali", "certainty": "kesin"},
        {"name": "I. Seyfeddin Gazi", "mother": "", "note": "Musul meliki", "certainty": "kesin"},
        {"name": "Kutbeddin Mevdud", "mother": "", "note": "Musul meliki", "certainty": "kesin"}
      ],
      "wars": [
        {"name": "Urfa'nın Fethi", "when": "1144", "foe": "Urfa Haçlı Kontluğu (II. Joscelin)", "result": "zafer", "note": "Urfa Kalesi fethedildi, Urfa Haçlı Kontluğu ortadan kaldırıldı."},
        {"name": "Bârin Muharebesi", "when": "1137", "foe": "Kudüs Haçlı Krallığı (Kral Fulk)", "result": "zafer", "note": "Haçlı ordusu dağıtıldı, Kral Fulk Bârin kalesinde kuşatılıp teslim alındı."}
      ],
      "legends": ["Tarihçi İbnü'l-Esîr babasının ve kendisinin atabeglik sarayında yetiştiği için onun adalet ve heybetini destansı bir dille anlatır."],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, ZENGÎ, İmâdüddin", "url": "https://islamansiklopedisi.org.tr/zengi-imaduddin"}
      ]
    },
    {
      "id": "zengi-nureddin-mahmud",
      "name": "Nûreddin Mahmud Zengî",
      "aliases": ["Nûreddin Zengî", "el-Melikü'l-Âdil"],
      "title": "Melik / Sultan / el-Âdil",
      "birth": 1118,
      "birthNote": "1118'de Halep'te doğdu",
      "death": 1174,
      "deathNote": "Dımaşk'ta boğaz iltihabından vefat etti, Dârü'l-Hadîs medresesindeki türbesindedir",
      "reign": [1146, 1174],
      "reignNote": "28 yıllık adalet, cihat ve medeniyet devri.",
      "summary": "İmâdeddin Zengî'nin oğlu. İslam tarihinin Hulefâ-yi Râşidîn ve Ömer b. Abdülazîz'den sonraki en adil ve takva sahibi hükümdarı sayılır. Şam'ı fethetti, II. Haçlı Seferi'ni püskürttü, Mısır'ı kontrolüne alıp Fâtımîleri bitirdi. Selâhaddîn-i Eyyûbî'nin hamisi ve Kudüs fethinin manevi mimarıdır.",
      "traits": ["Adalet ve zühd timsali", "Büyük mücahid", "İlim ve hadis aşığı"],
      "contribution": "Suriye ve Mısır'ı birleştirerek Kudüs'ün fethini hazırladı; tarihteki ilk Dârü'l-Hadîs ihtisas medresesini ve adalet saraylarını (Dârü'l-Adl) kurdu.",
      "harm": "Kayıtlarda belirgin bir zararı geçmez.",
      "wives": [
        {"name": "İsmetüddin Hatun", "note": "Dımaşk Atabeyi Üner'in kızı; Nûreddin'den sonra Selâhaddîn ile evlendi", "certainty": "kesin"}
      ],
      "children": [
        {"name": "el-Melikü's-Sâlih İsmâil", "mother": "İsmetüddin Hatun", "note": "Çocuk yaşta halef oldu", "certainty": "kesin"}
      ],
      "wars": [
        {"name": "İnâb Muharebesi", "when": "1149", "foe": "Antakya Haçlı Prensliği (Raymond de Poitiers)", "result": "zafer", "note": "Haçlı ordusu imha edildi, Antakya Prensi Raymond öldürüldü."},
        {"name": "Harim Muharebesi", "when": "1164", "foe": "Birleşik Haçlı ve Bizans ordusu", "result": "zafer", "note": "Antakya Prensi III. Bohemund ve Trablus Kontu Raymond esir alındı."}
      ],
      "legends": ["Kudüs'ün fethine o kadar inanmıştı ki fetihten 20 yıl önce Halep'te kündekârî sanatıyla tek bir çivi çakılmadan muazzam bir ahşap minber yaptırmıştı. Selâhaddîn 1187'de Kudüs'ü alınca bu minberi Mescid-i Aksâ'ya yerleştirdi."],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, NÛREDDİN ZENGÎ", "url": "https://islamansiklopedisi.org.tr/nureddin-zengi"}
      ]
    }
  ]
}

eftalit_state = {
  "id": "eftalit",
  "name": "Eftalitler (Ak Hunlar)",
  "short": "Ak Hunlar",
  "aliases": ["Eftalit Devleti", "Hephthalites", "Hayâtıla", "Sveta Huna"],
  "region": "diger",
  "start": 420,
  "end": 567,
  "startNote": "5. yüzyıl başlarında Ceyhun nehri havzasında bağımsız krallık olarak tarih sahnesine çıktılar.",
  "endNote": "557-567 yıllarında Göktürk (İstemi Yabgu) ve Sâsânî (Enûşirvân) ortak harekatıyla yıkıldılar.",
  "capital": "Balkh (Belh), Kunduz ve Bâmiyân",
  "religion": "Gök Tanrı inancı, Budizm, Zerdüştlük ve Şamanizm unsurları",
  "confidence": "tartismali",
  "confidenceNote": "Etnik kökenleri Türk, Doğu İrani (Hoten-Saka) veya karma bozkır federasyonu olarak akademik dünyada tartışmalıdır.",
  "summary": "Orta Asya, Afganistan, Horasan ve Kuzeybatı Hindistan'da hüküm süren kudretli bozkır imparatorluğu. Sâsânî İmparatorluğu'nu ağır vergilere bağladılar; 484 Herat Muharebesi'nde Sâsânî Şahı Firuz'u ordusuyla birlikte imha ettiler. Toramana ve oğlu Mihirakula devrinde Hindistan'a inerek Gupta İmparatorluğu'nu çökerttiler. 557-567 yıllarında Göktürk Kağanlığı (İstemi Yabgu) ve Sâsânîlerin ortak askeri kıskacıyla ortadan kaldırıldılar.",
  "legacy": "Sâsânî İmparatorluğu'nun askeri ve mali sistemini derinden etkiledi; Kuzey Hindistan'daki Gupta hakimiyetini yıkarak bölgenin siyasi ve etnik haritasını dönüştürdü.",
  "essay": [
    "Eftalitler (Ak Hunlar), Çin kaynaklarında Yeda, Arap-Fars kaynaklarında Hayâtıla, Bizans kaynaklarında Ephtalitai ve Hint kaynaklarında Huna adıyla geçer. Hun konfederasyonunun güney kolunu teşkil ettikleri kabul edilir.",
    "Hükümdarları Akşunvar (Khanghil) devrinde Sâsânî İmparatorluğu'na karşı büyük üstünlük sağladılar. 484 Herat Muharebesi'nde kazdıkları gizli hendek taktiğiyle Sâsânî Şahı Firuz'u ve tüm ordusunu yok ettiler; Sâsânîleri yıllık ağır haraçlara bağladılar.",
    "Toramana ve oğlu Mihirakula devrinde Pencap ve Ganj havzasına inen Ak Hunlar, Hindistan'ın altın çağını yaşayan Gupta İmparatorluğu'nu yıktılar. Ancak 6. yüzyıl ortasında doğudan gelen Göktürk Kağanlığı'nın kurucuları Bumın ve İstemi Yabgu, Sâsânî Şahı Enûşirvân ile anlaşarak Ak Hunları iki taraftan kuşattı ve 567'de devleti tamamen yıktı."
  ],
  "sources": [
    {"title": "TDV İslâm Ansiklopedisi, AK HUNLAR", "url": "https://islamansiklopedisi.org.tr/ak-hunlar"},
    {"title": "Britannica, Hephthalite", "url": "https://www.britannica.com/topic/Hephthalite"}
  ],
  "rulers": [
    {
      "id": "eftalit-aksunvar",
      "name": "Akşunvar",
      "aliases": ["Aksuvar", "Khanghil", "Khushnavaz"],
      "title": "Tegin / Hükümdar",
      "birth": None,
      "birthNote": "Kayıtlarda yok",
      "death": 490,
      "deathNote": "Belh civarında vefat etti",
      "reign": [459, 490],
      "reignNote": "31 yıl boyunca Sâsânîlere kök söktürdü.",
      "summary": "Ak Hunların en meşhur hükümdarı. Sâsânî Şahı Firuz'u iki kez esir alıp fidye karşılığı bıraktı; üçüncü seferde 484 Herat Muharebesi'nde Firuz'u öldürüp Sâsânîleri haraca bağladı.",
      "traits": ["Savaş hilesi ustası", "Stratejist"],
      "contribution": "Ak Hun devletini Horasan ve Orta Asya'nın tartışmasız tek hakimi yaptı.",
      "harm": "Kayıtlarda belirgin bir zararı geçmez.",
      "wives": [],
      "children": [],
      "wars": [
        {"name": "Herat Meydan Muharebesi", "when": "484", "foe": "Sâsânî İmparatorluğu (Şah Firuz)", "result": "zafer", "note": "Kazılan gizli hendeklere düşen Sâsânî ordusu ve Şah Firuz imha edildi."}
      ],
      "legends": ["Firuz'un cesedinin bulunamadığı ve parmağındaki efsanevi incinin Akşunvar'ın tacına takıldığı anlatılır."],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, AK HUNLAR", "url": "https://islamansiklopedisi.org.tr/ak-hunlar"}
      ]
    },
    {
      "id": "eftalit-toramana",
      "name": "Toramana",
      "aliases": ["Toramana Huna"],
      "title": "Maha-Raca / Hükümdar",
      "birth": None,
      "birthNote": "Kayıtlarda yok",
      "death": 515,
      "deathNote": "Kuzey Hindistan seferinde vefat etti",
      "reign": [495, 515],
      "reignNote": "20 yıl boyunca Hindistan içlerine hükmetti.",
      "summary": "Ak Hunların Hindistan fatihi. Pencap, Racastan, Keşmir ve Gucerat'ı fethederek Gupta İmparatorluğu'nu yıktı; kendi adına madeni paralar bastırdı.",
      "traits": ["Fatih", "Sert komutan"],
      "contribution": "Ak Hun sınırlarını Ganj havzasına kadar ulaştırdı.",
      "harm": "Hint tapınaklarına yönelik sert tutumu yerel direnişi körükledi.",
      "wives": [],
      "children": [
        {"name": "Mihirakula", "mother": "", "note": "Halefi, Budist kaynaklarınca 'Hindistan'ın Attila'sı' sayılır", "certainty": "kesin"}
      ],
      "wars": [
        {"name": "Kuzey Hindistan Seferleri", "when": "500-510", "foe": "Gupta İmparatorluğu", "result": "zafer", "note": "Gupta orduları dağıtıldı, orta Hindistan vergiye bağlandı."}
      ],
      "legends": [],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, AK HUNLAR", "url": "https://islamansiklopedisi.org.tr/ak-hunlar"}
      ]
    }
  ]
}

celayirli_state = {
  "id": "celayirli",
  "name": "Celâyirîler",
  "short": "Celâyirîler",
  "aliases": ["Celâyir Devleti", "Âl-i Celâyir", "Jalayirids"],
  "region": "diger",
  "start": 1335,
  "end": 1432,
  "startNote": "İlhanlıların çöküşüyle Moğol Celâyir boyundan Şeyh Hasan Büzürg'ün Bağdat ve Irak'ta hakimiyet kurmasıyla başladı.",
  "endNote": "1432 yılında Karakoyunluların son Celâyir sığınağı Hille'yi almasıyla sona erdi.",
  "capital": "Bağdat ve Tebriz",
  "religion": "İslamiyet (Sünnî ve Şiî unsurlar)",
  "confidence": "kayit",
  "confidenceNote": "Aynî, İbn Hacer, Hâfız-ı Ebrû ve Târîh-i Güzîde ile sabittir.",
  "summary": "İlhanlılar döneminde Türkleşen Moğol Celâyir boyuna mensup Şeyh Hasan Büzürg tarafından Irak ve Azerbaycan'da kurulan devlet. Sultan Üveys devrinde Tebriz'i başkent yaparak Azerbaycan ve Fars'a hükmettiler; Tebriz'de devasa Devlet-hâne sarayını yaptırdılar. Sultan Ahmed Celâyir devrinde Timur'un amansız seferlerine karşı Yıldırım Bayezid ve Memlüklere sığındılar. 1432'de Karakoyunlular tarafından yıkıldılar.",
  "legacy": "Bağdat ve Tebriz'de minyatür, tezhip ve şiir sanatını zirveye taşıdı; Sultan Ahmed Celâyir'in Türkçe divanı erken dönem Azerbaycan Türk edebiyatının seçkin anıtı oldu.",
  "essay": [
    "Celâyirîler, Moğol istilasıyla batıya gelen ve hızla Türk-İslam kültürünü benimseyen Celâyir boyunun reisi Emîr Hüseyin'in oğlu Şeyh Hasan Büzürg (Büyük Hasan) tarafından 1335'te Bağdat'ta kuruldu.",
    "Sultan Üveys (1356-1374) devrinde devlet altın çağını yaşadı. Tebriz'i zaptedip başkent yaptı; Şirvan, Diyarbekir ve Musul'u kendine bağladı. Edebiyat, musiki ve mimaride parlak eserler verildi.",
    "Sultan Ahmed Celâyir dönemi Timur kasırgasının gölgesinde geçti. Bağdat'ı üç kez Timur'a kaptıran Sultan Ahmed, Karakoyunlu Kara Yusuf ile birlikte Osmanlı Sultanı Yıldırım Bayezid'e sığındı (Ankara Savaşı'nın gerekçelerinden biri oldu). 1410'da Tebriz yakınlarında eski dostu Kara Yusuf ile yaptığı Esed Muharebesi'nde yenilip idam edildi; hanedanın kalıntıları 1432'de Karakoyunlularca tamamen tasfiye edildi."
  ],
  "sources": [
    {"title": "TDV İslâm Ansiklopedisi, CELÂYİRLİLER", "url": "https://islamansiklopedisi.org.tr/celayirliler"},
    {"title": "Britannica, Jalayirid dynasty", "url": "https://www.britannica.com/topic/Jalayirid"}
  ],
  "rulers": [
    {
      "id": "celayirli-hasan-buzurg",
      "name": "Şeyh Hasan Büzürg",
      "aliases": ["Büyük Hasan", "Tâceddin Hasan"],
      "title": "Ulus Emiri / Han",
      "birth": None,
      "birthNote": "Kayıtlarda yok",
      "death": 1356,
      "deathNote": "Bağdat'ta vefat etti",
      "reign": [1335, 1356],
      "reignNote": "21 yıllık kurucu hükümdarlık.",
      "summary": "Celâyirîler Devleti'nin kurucusu. İlhanlıların dağılması üzerine Bağdat'ı başkent yaparak Irak'ta müstakil bir idare kurdu; Çobanlı Hasan-ı Küçük ile kanlı mücadeleler verdi.",
      "traits": ["Devlet kurucu emir", "Sabırlı stratejist"],
      "contribution": "Irak ve Mezopotamya'da Moğol anarşisini durdurup istikrarlı bir devlet kurdu.",
      "harm": "Çobanlılarla sürekli iç savaş Tebriz'i harabeye çevirdi.",
      "wives": [
        {"name": "Dilşad Hatun", "note": "Son İlhanlı Ebu Said'in eşi, Dımaşk Hoca'nın kızı", "certainty": "kesin"}
      ],
      "children": [
        {"name": "Sultan Üveys", "mother": "Dilşad Hatun", "note": "Büyük hükümdar", "certainty": "kesin"}
      ],
      "wars": [
        {"name": "Bağdat ve Irak Hakimiyeti", "when": "1340", "foe": "Çobanlılar (Hasan-ı Küçük)", "result": "zafer", "note": "Bağdat fethedilip Celâyirî başkenti yapıldı."}
      ],
      "legends": [],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, CELÂYİRLİLER", "url": "https://islamansiklopedisi.org.tr/celayirliler"}
      ]
    },
    {
      "id": "celayirli-sultan-ahmed",
      "name": "Sultan Ahmed Celâyir",
      "aliases": ["Gıyâseddin Ahmed"],
      "title": "Sultan / Şair",
      "birth": None,
      "birthNote": "Kayıtlarda yok",
      "death": 1410,
      "deathNote": "Tebriz yakınlarında Kara Yusuf tarafından esir alınıp idam edildi",
      "reign": [1382, 1410],
      "reignNote": "28 yıllık sürgünler ve taht kavgalarıyla dolu saltanat.",
      "summary": "Sultan Üveys'in oğlu. Timur'un amansız istilalarına karşı Bağdat'ı kahramanca savundu, defalarca şehri terk edip geri aldı. Türkçe divan yazan ilk hükümdar şairlerdendir. Yıldırım Bayezid'e sığınması Ankara Savaşı'nı tetikledi. Eski dostu Karakoyunlu Kara Yusuf ile taht savaşında öldü.",
      "traits": ["Musikişinas ve şair", "Yenilmeyen irade", "Gözü pek"],
      "contribution": "Türkçe ve Farsça Divanıyla erken dönem Türk şiirine şaheserler kazandırdı.",
      "harm": "Karakoyunlular ile uzlaşmak yerine Tebriz tahtı için savaşa tutuşması devletinin sonunu getirdi.",
      "wives": [],
      "children": [],
      "wars": [
        {"name": "Bağdat Savunması", "when": "1393 ve 1401", "foe": "Timurlu Ordusu (Timur bizzat)", "result": "yenilgi", "note": "Bağdat düştü, kafa kuleleri dikildi, sultan Memlüklere ve Osmanlı'ya kaçtı."},
        {"name": "Esed Muharebesi", "when": "1410", "foe": "Karakoyunlular (Kara Yusuf)", "result": "yenilgi", "note": "Sultan esir alındı ve idam edildi."}
      ],
      "legends": ["Yıldırım Bayezid'in onu Bursa'da krallar gibi ağırladığı ve Timur'un 'Ahmed ile Yusuf'u bana teslim et' tehditlerine karşı 'Sığınan misafiri teslim etmek töremizde yoktur' diyerek savaşı göze aldığı meşhurdur."],
      "sources": [
        {"title": "TDV İslâm Ansiklopedisi, CELÂYİRLİLER", "url": "https://islamansiklopedisi.org.tr/celayirliler"}
      ]
    }
  ]
}

def to_list(x):
    return x if isinstance(x, list) else [x]

data = to_list(ilhanli_raw) + to_list(memluk_raw) + [zengi_state, eftalit_state, celayirli_state]

out = ROOT / "data" / "raw" / "k-ilhanli-memluk.json"
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data)} states to {out}")
