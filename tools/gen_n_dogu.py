#!/usr/bin/env python3
"""Build n-beylikler-dogu.json."""
import json
from pathlib import Path

data = [
  {
    "id": "karamanoglu",
    "name": "Karamanoğulları Beyliği",
    "short": "Karamanoğulları",
    "aliases": ["Karaman Beyliği", "Karamanoğulları Devleti"],
    "region": "anadolu",
    "start": 1256,
    "end": 1487,
    "startNote": "Nûre Sûfî ve oğlu Kerîmüddin Karaman Bey'in Ermenek ve Toroslar'da beylik kurmasıyla başladı.",
    "endNote": "1487 yılında II. Bayezid devrinde son Karaman kalıntıları temizlenerek Osmanlı'ya bağlandı.",
    "capital": "Ermenek, Lârende (Karaman) ve Konya",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Şikârî'nin Karamannâme'si, İbn Bîbî, Âşıkpaşazâde ve Neşrî kronikleriyle sabittir.",
    "summary": "Oğuzların Avşar boyuna mensup Nûre Sûfî ve Kerîmüddin Karaman Bey tarafından Toroslar'da kurulan, Anadolu Selçuklu Devleti'nin gerçek varisi olma iddiasıyla Osmanlı Devleti'ne karşı en uzun ve çetin direnişi gösteren güçlü beylik. 13 Mayıs 1277'de Karamanoğlu Mehmed Bey, Selçuklu başkenti Konya'yı fethederek ünlü 'Bugünden sonra divanda, dergâhta, bargâhta, mecliste ve meydanda Türkçeden başka dil kullanılmaya' fermanını yayınladı. Fatih Sultan Mehmed ve II. Bayezid dönemlerinde Osmanlı'ya katıldı.",
    "legacy": "Türkçenin resmi devlet dili olarak ilan edilmesinin bayraktarı oldu. Her yıl 13 Mayıs'ta Türk Dil Bayramı olarak kutlanan tarihi mirasın mimarıdır.",
    "essay": [
      "Karamanoğulları, Moğol istilası önünden Anadolu'ya göç eden Avşar Türkmenlerinin başında bulunan Nûre Sûfî ve oğlu Kerîmüddin Karaman Bey önderliğinde Ermenek çevresinde kuruldu. Selçuklu Devleti'nin Moğol vesayetine girmesine karşı en sert Türkmen direnişini temsil ettiler.",
      "1277 yılında Kerîmüddin Karaman'ın oğlu Mehmed Bey, Selçuklu şehzadesi Cimri (Siyavuş) ile birlikte Konya'ya girdi ve Selçuklu vezirlerini saf dışı bıraktı. 13 Mayıs 1277'de Türkçe fermanını yayınlayarak Farsçanın devlet ve bürokrasi dili hakimiyetine son verdi. Ancak Selçuklu-Moğol karşı ordusuyla yapılan savaşta şehit düştü.",
      "14. ve 15. yüzyıllarda Konya, Karaman, Niğde, Aksaray ve Antalya'ya hakim olan beylik, Alâeddin Ali Bey ve II. İbrâhim Bey devirlerinde Osmanlı Devleti ile amansız bir Anadolu hakimiyeti mücadelesine girdi. Zaman zaman Memlükler, Akkoyunlular ve Macarlar ile Osmanlı aleyhine ittifaklar kurdular. Fatih Sultan Mehmed'in 1468 Konya ve Karaman seferleri ve ardından Gedik Ahmed Paşa'nın harekatıyla 1487'de tamamen Osmanlı topraklarına katıldı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, KARAMANOĞULLARI", "url": "https://islamansiklopedisi.org.tr/karamanogullari"},
      {"title": "TDV İslâm Ansiklopedisi, MEHMED BEY, Karamanoğlu", "url": "https://islamansiklopedisi.org.tr/mehmed-bey-karamanoglu"}
    ],
    "rulers": [
      {
        "id": "karamanoglu-mehmed-bey",
        "name": "Karamanoğlu Mehmed Bey",
        "aliases": ["Şemseddin Mehmed Bey"],
        "title": "Bey / Vezir",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1277,
        "deathNote": "Moğol-Selçuklu müfrezesiyle çarpışırken okla şehit edildi",
        "reign": [1261, 1277],
        "reignNote": "16 yıl beylik yaptı.",
        "summary": "Kerîmüddin Karaman Bey'in oğlu. 1277'de Konya'yı fethedip vezir oldu ve Türkçeyi resmi devlet dili ilan eden tarihi fermanı yayınladı. Moğollara karşı Göksu boylarında şehit düştü.",
        "traits": ["Türkçe aşığı", "Milli şuur önderi", "Gözü pek gazi"],
        "contribution": "Türk dilini devlet ve edebiyat dili mertebesine yükseltti; Moğol tahakkümüne karşı Türkmen direnişinin bayrağı oldu.",
        "harm": "Selçuklu şehzadesi Siyavuş (Cimri) macerasına girişerek siyasi meşruiyet krizine yol açtı.",
        "wives": [],
        "children": [],
        "wars": [
          {"name": "Konya'nın Fethi", "when": "1277", "foe": "Moğol kuklası Selçuklu naibleri", "result": "zafer", "note": "Konya fethedildi, Türkçe fermanı ilan edildi."},
          {"name": "Göksu Muharebesi", "when": "1277", "foe": "Moğol ve Selçuklu ortak ordusu", "result": "yenilgi", "note": "Pusuda iki kardeşiyle birlikte şehit düştü."}
        ],
        "legends": ["'Bugünden sonra divanda, dergâhta, bargâhta, mecliste ve meydanda Türkçeden başka dil kullanılmaya' fermanı Karaman meydanında tunç yazıtlara kazınmıştır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, MEHMED BEY, Karamanoğlu", "url": "https://islamansiklopedisi.org.tr/mehmed-bey-karamanoglu"}
        ]
      },
      {
        "id": "karamanoglu-ibrahim-2",
        "name": "Tâceddin II. İbrâhim Bey",
        "aliases": ["İbrâhim Bey II"],
        "title": "Bey",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1464,
        "deathNote": "Gevele kalesinde kederinden vefat etti",
        "reign": [1424, 1464],
        "reignNote": "40 yıllık uzun hükümdarlık.",
        "summary": "Mehmed Bey'in oğlu. Osmanlı Sultanı II. Murad'ın kız kardeşi İsfendiyar Sultan (İlaldı Hatun) ile evlendi. Osmanlıların Rumeli'de Haçlılarla savaştığı anlarda defalarca Anadolu'da Osmanlı şehirlerine saldırdı; Varna öncesi anlaşmak zorunda kaldı. Karaman'daki İbrâhim Bey İmareti ve Külliyesi'ni inşa ettirdi.",
        "traits": ["İnatçı siyasetçi", "İmar hamisi", "Fırsatçı"],
        "contribution": "Karaman ve Konya'da çok sayıda medrese, köprü ve imaret yaptırdı.",
        "harm": "Osmanlı'nın Haçlılarla yaptığı ölüm kalım savaşlarında arkadan saldırması Türk-İslam dünyasında büyük tepki çekti.",
        "wives": [
          {"name": "İsfendiyar Sultan (İlaldı Hatun)", "note": "Osmanlı Sultanı II. Murad'ın kız kardeşi", "certainty": "kesin"}
        ],
        "children": [
          {"name": "İshak Bey", "mother": "", "note": "Akkoyunlu destekli veliaht", "certainty": "kesin"},
          {"name": "Pîr Ahmed Bey", "mother": "İsfendiyar Sultan", "note": "Osmanlı destekli oğlu", "certainty": "kesin"},
          {"name": "Kasım Bey", "mother": "İsfendiyar Sultan", "note": "Son direnişçi bey", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Akşehir ve Beyşehir Kuşatmaları", "when": "1443", "foe": "Osmanlı Devleti (II. Murad)", "result": "yenilgi", "note": "Osmanlı ordusu gelince Toros dağlarına kaçtı, 'Sevgendnâme' ile barış istedi."}
        ],
        "legends": ["Yaptırdığı İbrâhim Bey İmareti'nin çinili mihrabı günümüzde İstanbul Çinili Köşk Müzesi'nin başyapıtıdır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, KARAMANOĞULLARI", "url": "https://islamansiklopedisi.org.tr/karamanogullari"}
        ]
      }
    ]
  },
  {
    "id": "dulkadir",
    "name": "Dulkadiroğulları Beyliği",
    "short": "Dulkadiroğulları",
    "aliases": ["Dulkadır Beyliği", "Zülkadir Devleti"],
    "region": "anadolu",
    "start": 1337,
    "end": 1522,
    "startNote": "Zeyneddin Karaca Bey'in Memlük Sultanı Nâsır Muhammed tarafından Elbistan Türkmen emiri tanınmasıyla kuruldu.",
    "endNote": "1515 Turnadağ Zaferi ve 1522'de Şehsuvaroğlu Ali Bey'in katliyle Osmanlı'ya bağlandı.",
    "capital": "Elbistan ve Maraş",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Memlük kronikleri (Makrîzî, İbn Hacer) ve Osmanlı kaynaklarıyla sabittir.",
    "summary": "Oğuzların Bozok koluna mensup Türkmenler tarafından Elbistan, Maraş, Malatya, Harput ve Antep sahasında kurulan stratejik beylik. Osmanlı ile Memlük süper güçleri arasında tampon devlet rolü oynadılar. Osmanlı hanedanına çok sayıda gelin verdiler (Emine Hatun, Sitti Mükrime Hatun, Gülbahar Hatun). 1515'te Yavuz Sultan Selim'in Turnadağ Muharebesi'nde Alâüddevle Bozkurt Bey'i yenmesiyle Osmanlı hakimiyetine girdi.",
    "legacy": "Osmanlı padişahlarına valide sultanlar veren köklü hanedan bağı kurdu; Çukurova ve Güneydoğu Anadolu yaylalarında zengin konargöçer Türkmen kültürünü yaşattı.",
    "essay": [
      "Dulkadiroğulları, İlhanlıların Anadolu'daki hakimiyetinin çökmesi üzerine Maraş-Elbistan sahasındaki Bozok Türkmenlerini birleştiren Zeyneddin Karaca Bey tarafından 1337'de kuruldu. Memlük Devleti başlangıçta beyliği sınır muhafızı olarak tanıdı.",
      "Halil Bey ve Sevli Bey devirlerinde Memlüklerle çetin savaşlar yaşandı. Nasreddin Mehmed Bey döneminde Osmanlılarla akrabalık kurularak kızı Emine Hatun Çelebi Mehmed ile evlendirildi (II. Murad'ın annesi). Fatih Sultan Mehmed de Dulkadirli Süleyman Bey'in kızı Sitti Mükrime Hatun ile evlendi; Yavuz Sultan Selim'in annesi Ayşe Gülbahar Hatun da Alâüddevle'nin kızıdır.",
      "Son kudretli hükümdar Alâüddevle Bozkurt Bey (1480-1515), Yavuz Sultan Selim'in Çaldıran Seferi sırasında Osmanlı ikmal kollarını vurdu ve sefere katılmayı reddetti. Yavuz, Çaldıran dönüşünde 12 Haziran 1515'te Turnadağ Muharebesi'nde Alâüddevle'yi mağlup ederek öldürttü; beylik 1522'de resmen Osmanlı beylerbeyliği oldu."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, DULKADIROĞULLARI", "url": "https://islamansiklopedisi.org.tr/dulkadirogullari"}
    ],
    "rulers": [
      {
        "id": "dulkadir-karaca-bey",
        "name": "Zeyneddin Karaca Bey",
        "aliases": ["Karaca Bey"],
        "title": "Bey / Emir",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1353,
        "deathNote": "Kahire'de Memlük Sultanı tarafından idam edildi",
        "reign": [1337, 1353],
        "reignNote": "16 yıl hüküm sürdü.",
        "summary": "Dulkadiroğulları'nın kurucusu. Elbistan ve Maraş'ta Türkmen birliğini kurdu. Memlük ordularına karşı Düldül Dağı eteklerinde büyük zaferler kazandı; Kayseri'de Eretnaoğullarına sığındıysa da Memlüklere teslim edilip Kahire'de katledildi.",
        "traits": ["Cesur kurucu", "Bozok reisi"],
        "contribution": "İki asır yaşayacak Dulkadir beyliğinin temellerini attı.",
        "harm": "Memlük iç çekişmelerine aşırı müdahil olması idamına yol açtı.",
        "wives": [],
        "children": [
          {"name": "Halil Bey", "mother": "", "note": "İkinci bey", "certainty": "kesin"},
          {"name": "Sevli Bey", "mother": "", "note": "Üçüncü bey", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Düldül Dağı Muharebesi", "when": "1343", "foe": "Memlük Halep Valisi Yelboğa", "result": "zafer", "note": "Memlük ordusu hezimete uğratıldı."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, DULKADIROĞULLARI", "url": "https://islamansiklopedisi.org.tr/dulkadirogullari"}
        ]
      },
      {
        "id": "dulkadir-alauddevle",
        "name": "Alâüddevle Bozkurt Bey",
        "aliases": ["Alâüddevle Bey", "Bozkurt Bey"],
        "title": "Bey",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1515,
        "deathNote": "Turnadağ Meydan Muharebesi'nde savaşarak şehit düştü",
        "reign": [1480, 1515],
        "reignNote": "35 yıllık kudretli saltanat.",
        "summary": "Dulkadiroğullarının en meşhur hükümdarı. Kızı Ayşe Hatun'u II. Bayezid'e verdi (Yavuz Sultan Selim'in dedesidir). Safevi Şahı İsmail'in Diyarbekir ve Maraş akınlarına karşı savaştı. Çaldıran'da Yavuz'a yardım etmeyip lojistiği tazyik edince 1515 Turnadağ Muharebesi'nde dört oğluyla birlikte şehit düştü.",
        "traits": ["Kudretli hükümdar", "İnatçı diplomat", "Yaşlı kurt"],
        "contribution": "Maraş Ulu Camii ve külliyelerini inşa ettirdi; beyliğe en geniş sınırlarını yaşattı.",
        "harm": "Osmanlı ile Safevi arasındaki dünya savaşında tarafsız kalarak beyliğinin sonunu hazırladı.",
        "wives": [],
        "children": [
          {"name": "Ayşe Gülbahar Hatun", "mother": "", "note": "II. Bayezid'in eşi, Yavuz Sultan Selim'in annesi", "certainty": "kesin"},
          {"name": "Şahruh", "mother": "", "note": "Şehzade, gözlerine mil çekildi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Turnadağ Meydan Muharebesi", "when": "1515", "foe": "Osmanlı Ordusu (Hadım Sinan Paşa)", "result": "yenilgi", "note": "Alâüddevle ve dört oğlu öldürüldü, beylik fiilen sona erdi."}
        ],
        "legends": ["90 yaşına yakın olmasına rağmen Turnadağ'da zırhını kuşanıp bizzat kılıç sallayarak çarpıştığı tarihe geçmiştir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, DULKADIROĞULLARI", "url": "https://islamansiklopedisi.org.tr/dulkadirogullari"}
        ]
      }
    ]
  },
  {
    "id": "ramazanoglu",
    "name": "Ramazanoğulları Beyliği",
    "short": "Ramazanoğulları",
    "aliases": ["Ramazan Beyliği", "Âl-i Ramazan"],
    "region": "anadolu",
    "start": 1352,
    "end": 1608,
    "startNote": "Ramazan Bey'in Memlükler tarafından Çukurova Türkmenleri emirliğine atanmasıyla kuruldu.",
    "endNote": "1608 yılında son bey Pîrîzâde Ahmed Bey'in vefatıyla beylik doğrudan Osmanlı Adana eyaleti oldu.",
    "capital": "Adana",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Evliya Çelebi Seyahatnâmesi, Osmanlı Mühimme Defterleri ve Adana Ulu Cami kitabeleriyle sabittir.",
    "summary": "Oğuzların Üçok koluna mensup Yüreğir Türkmenleri tarafından Adana, Misis, Tarsus ve Ayas çevresinde kurulan beylik. 250 yılı aşkın süre Çukurova'ya hükmettiler. Osmanlı hakimiyetini Yavuz Sultan Selim devrinde gönüllü kabul ederek yurtluk-ocaklık statüsüyle iç işlerinde serbest kaldılar. Pîrî Mehmed Paşa devrinde Adana Ulu Camii ve Külliyesi gibi abidevi eserler inşa edildi.",
    "legacy": "Çukurova'nın tamamen Türkleşmesini sağladı; Adana Ulu Camii ve zengin Selçuklu-Memlük-Osmanlı sentezi mimari mirası bıraktı.",
    "essay": [
      "Ramazanoğulları, 14. yüzyıl ortalarında Kilikya Ermeni Krallığı'nı yıkan Yüreğir boyu reisi Ramazan Bey tarafından Adana merkezli kuruldu.",
      "Uzun süre Memlük himayesinde yaşayan beylik, Halil Bey ve İbrahim Bey dönemlerinde Adana'yı imar etti. 1516 yılında Yavuz Sultan Selim Mısır Seferi'ne giderken Ramazanoğlu Mahmud Bey Osmanlı'ya tam bağlılık bildirdi.",
      "En parlak devrini yaşayan Pîrî Mehmed Paşa (1520-1568), Kanuni Sultan Süleyman'ın yakın dostu oldu ve Adana'yı saraylar, medreseler ve camilerle donattı. 1608'de son bey Ahmed Bey'in ölümüyle beylik doğrudan Adana Beylerbeyliği'ne dönüştürüldü."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, RAMAZANOĞULLARI", "url": "https://islamansiklopedisi.org.tr/ramazanogullari"}
    ],
    "rulers": [
      {
        "id": "ramazanoglu-ramazan-bey",
        "name": "Ramazan Bey",
        "aliases": ["Emir Ramazan"],
        "title": "Emir / Bey",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1378,
        "deathNote": "Adana'da vefat etti",
        "reign": [1352, 1378],
        "reignNote": "26 yıllık kurucu beylik.",
        "summary": "Yüreğir boyu reisi ve beyliğin kurucusu. Çukurova'daki Ermeni krallığına ölümcül darbeler vurarak Adana'yı Türk yurdu yaptı.",
        "traits": ["Gazi", "Yüreğir reisi"],
        "contribution": "Çukurova'da 250 yıl sürecek Türk hakimiyetini kurdu.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "İbrâhim Bey", "mother": "", "note": "İkinci bey", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Çukurova Fethi", "when": "1352-1360", "foe": "Kilikya Ermeni Krallığı", "result": "zafer", "note": "Adana ve Tarsus fethedildi."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, RAMAZANOĞULLARI", "url": "https://islamansiklopedisi.org.tr/ramazanogullari"}
        ]
      },
      {
        "id": "ramazanoglu-piri-mehmed",
        "name": "Pîrî Mehmed Paşa",
        "aliases": ["Ramazanoğlu Pîrî Bey"],
        "title": "Bey / Paşa",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1568,
        "deathNote": "Adana'da vefat etti, türbesi Adana Ulu Camii haziresindedir",
        "reign": [1520, 1568],
        "reignNote": "48 yıllık adalet ve imar çağı.",
        "summary": "Ramazanoğullarının en büyük hükümdarı. Kanuni Sultan Süleyman'ın takdirini kazanarak vezirlik rütbesi aldı. Adana Ulu Camii, Yağ Camii, medreseler ve imaretler yaptırarak Adana'yı bir medeniyet merkezine çevirdi.",
        "traits": ["Büyük imar hamisi", "Âlim devlet adamı", "Adil"],
        "contribution": "Adana Ulu Camii ve Külliyesi'ni inşa ettirdi; 48 yıl boyunca Çukurova'da asayiş ve refahı sağladı.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "İbrahim Bey", "mother": "", "note": "Babasından sonra bey oldu", "certainty": "kesin"}
        ],
        "wars": [],
        "legends": ["Kanuni Sultan Süleyman'ın Irak ve İran seferlerinde ordunun Çukurova'dan geçişinde sunduğu muhteşem ziyafetler seyahatnamelerde anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, RAMAZANOĞULLARI", "url": "https://islamansiklopedisi.org.tr/ramazanogullari"}
        ]
      }
    ]
  },
  {
    "id": "candaroglu",
    "name": "Candaroğulları Beyliği",
    "short": "Candaroğulları",
    "aliases": ["İsfendiyaroğulları", "Kastamonu Beyliği"],
    "region": "anadolu",
    "start": 1291,
    "end": 1461,
    "startNote": "Şemseddin Yaman Candar'ın Selçuklu Sultanı Mesud tarafından Kastamonu emirliğine atanmasıyla kuruldu.",
    "endNote": "1461 yılında Fatih Sultan Mehmed'in Trabzon Seferi sırasında Sinop ve Kastamonu'yu ilhakıyla sona erdi.",
    "capital": "Kastamonu ve Sinop",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "İbn Battûta Seyahatnâmesi, Osmanlı vekayinameleri ve Sinop kitabeleriyle sabittir.",
    "summary": "Oğuzların Kayı koluyla akraba Türkmenler tarafından Kuzey Anadolu'da (Kastamonu, Sinop, Çankırı, Safranbolu) kurulan beylik. Sinop tersanesi sayesinde güçlü bir Karadeniz donanması kurdular; Cenevizlilerle deniz ticareti yaptılar. İsfendiyar Bey devrinde Osmanlı ile denge siyaseti güttüler. İlim ve tababete büyük önem verdiler; ilk Türkçe tıp kitapları bu sarayda yazıldı. 1461'de Fatih Sultan Mehmed tarafından Osmanlı'ya katıldı.",
    "legacy": "Sinop tersanesi ve Karadeniz Türk denizciliğini geliştirdi; Türkçe telif ve tercüme tıp eserlerinin (Müntahab-ı Şifâ) yazılmasını teşvik etti.",
    "essay": [
      "Candaroğulları, Selçuklu Sultanı II. Mesud'u düşmanlarının elinden kurtaran Şemseddin Yaman Candar'a Kastamonu'nun dirlik verilmesiyle 1291'de kuruldu.",
      "Süleyman Paşa 1322'de Sinop'u fethederek beyliğe güçlü bir deniz üssü kazandırdı. İbn Battûta 1332'de Kastamonu'ya uğradığında burayı ucuz ve mamur bir şehir, hükümdarı Süleyman Bey'i de dindar ve adil bir sultan olarak tasvir eder.",
      "Kötürüm Bâyezid ve İsfendiyar Bey dönemlerinde Timur istilasında beylik genişledi. Fatih Sultan Mehmed, Trabzon Rum İmparatorluğu'na sefere çıktığı 1461 yılında Sinop'u karadan ve denizden kuşattı; son hükümdar İsmail Bey kan dökülmesini istemeyerek şehri teslim etti ve kendisine Bursa ve Yenişehir tımar olarak verildi."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, CANDAROĞULLARI", "url": "https://islamansiklopedisi.org.tr/candarogullari"}
    ],
    "rulers": [
      {
        "id": "candaroglu-yaman-candar",
        "name": "Şemseddin Yaman Candar",
        "aliases": ["Yaman Candar"],
        "title": "Emir / Candar",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1301,
        "deathNote": "Kastamonu'da vefat etti",
        "reign": [1291, 1301],
        "reignNote": "10 yıllık kurucu beylik.",
        "summary": "Beyliğin kurucusu. Selçuklu saray muhafız birliği (candar) komutanıydı. Sultan II. Mesud'u kurtardığı için kendisine Kastamonu dirlik verildi.",
        "traits": ["Sadık muhafız", "Cesur komutan"],
        "contribution": "Batı Karadeniz'de köklü bir Türk beyliğinin temelini attı.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "I. Süleyman Paşa", "mother": "", "note": "Sinop'u fetheden hükümdar", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kastamonu Muharebesi", "when": "1291", "foe": "Çobanoğulları muhalifleri", "result": "zafer", "note": "Kastamonu zaptedildi."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, CANDAROĞULLARI", "url": "https://islamansiklopedisi.org.tr/candarogullari"}
        ]
      },
      {
        "id": "candaroglu-ismail-bey",
        "name": "Kemâleddin İsmail Bey",
        "aliases": ["İsmail Bey"],
        "title": "Bey / Kemâleddin",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1479,
        "deathNote": "Filibe'de vefat etti, türbesi oradadır",
        "reign": [1443, 1461],
        "reignNote": "18 yıl hüküm sürdü.",
        "summary": "Candaroğullarının son hükümdarı. Büyük bir âlim ve tıp aşığıydı. Kendisi 'Hulviyyât-ı Şâhî' adlı fıkıh kitabını yazdı; Kastamonu'da İsmail Bey Külliyesi'ni yaptırdı. 1461'de Fatih'in ordusu gelince Müslüman kanı dökülmesin diye Sinop'u teslim etti.",
        "traits": ["Âlim hükümdar", "Merhametli ve cömert", "Yazar"],
        "contribution": "Kastamonu'da muhteşem İsmail Bey Külliyesi'ni kurdu; Türkçe ilmi eserler telif ettirdi.",
        "harm": "Devletini Osmanlı'ya karşı askeri olarak savunamadı.",
        "wives": [],
        "children": [
          {"name": "Hasan Bey", "mother": "", "note": "Oğlu", "certainty": "kesin"}
        ],
        "wars": [],
        "legends": ["Fatih Sultan Mehmed onun teslimiyetindeki asalete hürmet ederek kendisine hürmetle muamele etmiş ve Filibe zeametini vermiştir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, CANDAROĞULLARI", "url": "https://islamansiklopedisi.org.tr/candarogullari"}
        ]
      }
    ]
  },
  {
    "id": "eretna",
    "name": "Eretna Devleti",
    "short": "Eretna Devleti",
    "aliases": ["Âl-i Eretna", "Kadı Burhaneddin Devleti"],
    "region": "anadolu",
    "start": 1335,
    "end": 1398,
    "startNote": "Uygur asıllı İlhanlı emiri Alâeddin Eretna'nın Sivas ve Kayseri'de sultanlığını ilan etmesiyle kuruldu.",
    "endNote": "1398 yılında Kadı Burhaneddin'in Akkoyunlu Kara Yülük Osman Bey tarafından öldürülmesi ve Sivas'ın Osmanlı'ya teslimiyle bitti.",
    "capital": "Sivas ve Kayseri",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Azîz b. Erdeşîr-i Esterâbâdî'nin Bezm ü Rezm eseri ve İbn Battûta seyahatnamesiyle sabittir.",
    "summary": "İlhanlıların Anadolu genel valisi Uygur Türkü Alâeddin Eretna tarafından Orta ve Doğu Anadolu'da (Sivas, Kayseri, Amasya, Tokat, Niğde, Erzincan) kurulan sultanlık. Eretna Bey adil yönetimi dolayısıyla halk arasında 'Köse Peygamber' lakabıyla anıldı. Devletin zayıflaması üzerine veziri ve kadısı olan büyük şair Kadı Burhaneddin Ahmed 1381'de iktidarı ele geçirerek kendi devletini kurdu ve Azerbaycan Türkçesiyle yazdığı divanıyla edebiyata damga vurdu.",
    "legacy": "Kadı Burhaneddin Divanı ile klasik Türk edebiyatının kurucu şaheserini armağan etti; Sivas ve Kayseri'de köşkler ve medreseler bıraktı.",
    "essay": [
      "Eretna Devleti, İlhanlı hükümdarı Ebû Said Bahadır Han'ın 1335'te vefatı üzerine Anadolu genel valisi Çobanlı Emîr Hasan-ı Küçük'ün naibi olan Uygur asıllı Alâeddin Eretna tarafından kuruldu. Eretna, 1343'te Karanbük Muharebesi'nde Moğol Çobanlı ordusunu hezimete uğratarak tam bağımsızlığını ilan etti.",
      "Eretna Bey'in 1352'de ölümüyle oğulları Mehmed ve Ali beyler devrinde devlet karışıklıklara sürüklendi. Bu sırada beyliğin kadısı ve veziri olan Kadı Burhaneddin Ahmed, devlet otoritesini eline alarak 1381'de Sivas'ta sultanlığını ilan etti.",
      "Kadı Burhaneddin, 17 yıl boyunca hem Osmanlılara (Yıldırım Bayezid), hem Karamanoğullarına hem de Akkoyunlulara karşı fırtınalı bir askeri ve siyasi mücadele yürüttü. Aynı zamanda Türk edebiyatının tuyuğ nazım şeklini zirveye taşıyan büyük bir divan şairiydi. 1398'de Akkoyunlu Kara Yülük Osman Bey tarafından pusuya düşürülüp öldürülünce Sivas halkı şehri Yıldırım Bayezid'e teslim etti."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, ERETNAOĞULLARI", "url": "https://islamansiklopedisi.org.tr/eretnaogullari"},
      {"title": "TDV İslâm Ansiklopedisi, KADI BURHÂNEDDİN", "url": "https://islamansiklopedisi.org.tr/kadi-burhaneddin"}
    ],
    "rulers": [
      {
        "id": "eretna-alaeddin",
        "name": "Alâeddin Eretna",
        "aliases": ["Eretna Bey", "Köse Peygamber"],
        "title": "Sultan / Alâeddin",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1352,
        "deathNote": "Kayseri'de vefat etti, Köşk Medrese'deki türbesindedir",
        "reign": [1335, 1352],
        "reignNote": "17 yıl adaletle hüküm sürdü.",
        "summary": "Uygur kökenli kurucu sultan. Moğol istilasından sonra Orta Anadolu'da can ve mal emniyetini yeniden sağladı. Aşırı adil ve müşfik tabiatı sebebiyle tebaası ona 'Köse Peygamber' lakabını taktı. Kayseri'de Köşk Medrese'yi inşa ettirdi.",
        "traits": ["Uygur asıllı dirayetli devlet adamı", "Adalet timsali", "Halk dostu"],
        "contribution": "Orta Anadolu'da Moğol anarşisini bitirip barış ve zenginlik ortamı kurdu.",
        "harm": "Ölümünden sonra yerine yetersiz şehzadelerin kalması devleti vezirlerin eline düşürdü.",
        "wives": [
          {"name": "Tuğa Hatun", "note": "Eşi", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Gıyâseddin Mehmed", "mother": "", "note": "İkinci sultan", "certainty": "kesin"},
          {"name": "Cafer", "mother": "", "note": "Şehzade", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Karanbük Muharebesi", "when": "1343", "foe": "Çobanlı Moğol Ordusu (Şeyh Hasan)", "result": "zafer", "note": "Moğol ordusu imha edildi, Eretna tam bağımsız sultanlığını ilan etti."}
        ],
        "legends": ["İbn Battûta seyahatnamesinde onun alicenaplığını, misafirperverliğini ve halkına olan şefkatini övgüyle anlatır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ERETNAOĞULLARI", "url": "https://islamansiklopedisi.org.tr/eretnaogullari"}
        ]
      },
      {
        "id": "eretna-kadi-burhaneddin",
        "name": "Kadı Burhaneddin",
        "aliases": ["Kadı Burhâneddin Ahmed"],
        "title": "Sultan / Kadı / Şair",
        "birth": 1345,
        "birthNote": "1345'te Kayseri'de doğdu",
        "death": 1398,
        "deathNote": "Akkoyunlu Kara Yülük Osman Bey tarafından pusuya düşürülüp şehit edildi",
        "reign": [1381, 1398],
        "reignNote": "17 yıllık kılıç ve divan saltanatı.",
        "summary": "Kayseri kadısı iken Eretna tahtını devralıp Sivas merkezli devlet kuran büyük şair-hükümdar. Gündüz at sırtında kılıç sallayıp gece çadırında aşk ve tasavvuf şiirleri yazdı; Türk edebiyatında tuyuğ nazım şeklinin kurucusu oldu. Yıldırım Bayezid ve Timur'a boyun eğmedi.",
        "traits": ["Cengaver şair", "Âlim kadı", "Yılmaz savaşçı"],
        "contribution": "Türk divan edebiyatına muazzam bir Divan hediye etti; Anadolu'da bağımsızlık timsali oldu.",
        "harm": "Sürekli savaş hali devletini ekonomik olarak yıprattı.",
        "wives": [],
        "children": [
          {"name": "Zeynelâbidîn", "mother": "", "note": "Kısa süre sultan ilan edildi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kırkdilim Muharebesi", "when": "1392", "foe": "Osmanlı Ordusu (Şehzade Ertuğrul)", "result": "zafer", "note": "Çorum yakınlarında Osmanlı ordusu mağlup edildi, Şehzade Ertuğrul şehit düştü."}
        ],
        "legends": ["'Hak yoluna can vermeyen er sayılmaz' mısrasıyla hem kılıcın hem kalemin sultanı olduğunu ispatlamıştır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, KADI BURHÂNEDDİN", "url": "https://islamansiklopedisi.org.tr/kadi-burhaneddin"}
        ]
      }
    ]
  }
]

out = Path(__file__).resolve().parent.parent / "data" / "raw" / "n-beylikler-dogu.json"
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data)} states to {out}")
