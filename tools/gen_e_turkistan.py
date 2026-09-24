#!/usr/bin/env python3
"""Build e-turkistan-islam.json."""
import json
from pathlib import Path

data = [
  {
    "id": "karahanli",
    "name": "Karahanlı Devleti",
    "short": "Karahanlılar",
    "aliases": ["Âl-i Afrâsiyâb", "Hakaniye", "İlek Hanlar", "Kara Hanlılar"],
    "region": "turkistan",
    "start": 840,
    "end": 1212,
    "startNote": "840 yılında Uygur Kağanlığı'nın çöküşü üzerine Bilge Kül Kadir Han'ın kağanlık ilan etmesiyle kuruldu.",
    "endNote": "1211'de Doğu Karahanlıların Karahıtaylar, 1212'de Batı Karahanlıların Harzemşah Alâeddin Muhammed tarafından ilhakıyla sona erdi.",
    "capital": "Balasagun, Kaşgar, Taraz ve Semerkant",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Arap-Fars vekayinameleri (İbnü'l-Esîr, Utbî), Divânu Lugâti't-Türk ve Kutadgu Bilig ile sabittir.",
    "summary": "Tarihte İslamiyet'i kabul eden ilk büyük Türk devleti. Karluk, Çiğil ve Yağma boylarının birleşmesiyle kurulan devlet, Satuk Buğra Han (Abdülkerim) devrinde İslamiyet'i resmi din olarak kabul etti. Maveraünnehir'e inerek Samanîler hanedanını yıktılar. Yusuf Has Hacib'in Kutadgu Bilig'i ve Kâşgarlı Mahmud'un Dîvânu Lugâti't-Türk'ü bu muazzam kültür devrinde yazıldı. 1042 civarında Doğu ve Batı olarak ikiye ayrıldılar.",
    "legacy": "Türk-İslam medeniyetinin kurucu omurgasını oluşturdu. Türk dilini ve edebiyatını İslam potasında abideleştiren Kutadgu Bilig ve Dîvânu Lugâti't-Türk'ü insanlığa armağan etti.",
    "essay": [
      "Karahanlılar, 840 yılında Yenisey Kırgızlarının Uygur başkenti Karabalgasun'u yerle bir etmesi üzerine Karluk yabgusu Bilge Kül Kadir Han'ın kendisini bozkırın meşru kağanı ilan etmesiyle doğdu. Devlet geleneksel ikili teşkilatla yönetilirdi: Büyük Kağan (Arslan Han) Balasagun'da, ortak kağan (Buğra Han) ise Taraz veya Kaşgar'da otururdu.",
      "Bilge Kül Kadir Han'ın torunu Satuk Buğra Han, Samani şehzadeleri ve seyyah Ebû Nasr el-Sâmânî'nin vesilesiyle genç yaşta gizlice İslamiyet'i kabul ederek 'Abdülkerim' adını aldı. 940 civarında amcası Oğulcak Kadir Han'a karşı darbe yaparak tahta geçti ve İslamiyet'i devletin resmi inancı yaptı. Oğlu Baytaş Musa Han zamanında (960 civarı) 200 bin çadırlık Türkmen kitlesinin Müslüman olduğu tarihi kaynaklarda zikredilir.",
      "10. yüzyıl sonunda Nasr b. Ali (İlig Han) komutasındaki Karahanlı orduları Buhara ve Semerkant'ı zaptederek Samani Devleti'ne son verdi ve Ceyhun nehrini Gazneliler ile sınır yaptı. 1042 yılında hanedan içi çekişmeler sebebiyle Semerkant merkezli Batı Karahanlılar ve Kaşgar merkezli Doğu Karahanlılar olmak üzere ikiye ayrıldılar. Doğu devleti 1211'de Karahıtaylar, Batı devleti ise 1212'de Semerkant'ta Harzemşah Alâeddin Muhammed tarafından ortadan kaldırıldı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, KARAHANLILAR", "url": "https://islamansiklopedisi.org.tr/karahanlilar"},
      {"title": "TDV İslâm Ansiklopedisi, SATUK BUĞRA HAN", "url": "https://islamansiklopedisi.org.tr/satuk-bugra-han"},
      {"title": "Britannica, Qarakhanid dynasty", "url": "https://www.britannica.com/topic/Qarakhanid-dynasty"}
    ],
    "rulers": [
      {
        "id": "karahanli-satuk-bugra",
        "name": "Satuk Buğra Han",
        "aliases": ["Abdülkerim Satuk Buğra Han", "Sultan Satuk Buğra"],
        "title": "Kağan / Abdülkerim",
        "birth": 895,
        "birthNote": "Yaklaşık 895 Kaşgar civarı",
        "death": 955,
        "deathNote": "Artuş'ta vefat etti, türbesi oradadır",
        "reign": [920, 955],
        "reignNote": "920'lerde İslamiyet'i ilan edip 955'e kadar hüküm sürdü.",
        "summary": "İslamiyet'i kabul eden ilk Türk kağanı. Samani mültecisi Ebû Nasr vesilesiyle gizlice Müslüman oldu, amcası Oğulcak'ı mağlup ederek Kaşgar tahtına oturdu ve İslam'ı devlet dini ilan etti. Gazaları Türk destanlarına konu oldu.",
        "traits": ["Gazi kağan", "Dindar inkılapçı", "Manevi önder"],
        "contribution": "Türk milletinin İslam medeniyetine girişine kapı açtı; ilk cami ve medreseleri kurdurdu.",
        "harm": "Eski inançlarını korumak isteyen akrabaları ve boylarla uzun iç savaşlara girdi.",
        "wives": [],
        "children": [
          {"name": "Baytaş Musa Buğra Han", "mother": "", "note": "İslamiyet'i halkına tam olarak kabul ettiren sultan", "certainty": "kesin"},
          {"name": "Süleyman Arslan Han", "mother": "", "note": "Büyük Kağan", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kaşgar Fethi ve İhtilal", "when": "920", "foe": "Oğulcak Kadir Han kuvvetleri", "result": "zafer", "note": "Kaşgar ele geçirilip İslam merkezi yapıldı."},
          {"name": "Hoten Seferleri", "when": "940-950", "foe": "Budist Hoten Krallığı", "result": "zafer", "note": "Doğu Tarım havzasına İslamiyet yayıldı."}
        ],
        "legends": ["Tezkire-i Satuk Buğra Han'da gece rüyasında gökten inen bir nur ile İslam'a davet edildiği ve kılıcının kırk arşın uzadığı rivayet edilir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, SATUK BUĞRA HAN", "url": "https://islamansiklopedisi.org.tr/satuk-bugra-han"}
        ]
      },
      {
        "id": "karahanli-musa-bugra",
        "name": "Musa Buğra Han",
        "aliases": ["Baytaş Musa Han", "Tonga İlig"],
        "title": "Büyük Kağan",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 971,
        "deathNote": "Kaşgar'da vefat etti",
        "reign": [955, 971],
        "reignNote": "16 yıl hüküm sürdü.",
        "summary": "Satuk Buğra Han'ın oğlu. 960 yılında 200 bin çadırlık Türkmen boyunun kitleler halinde Müslüman olmasını sağladı. İslam dünyasında Karahanlıların itibarını en üst seviyeye çıkardı.",
        "traits": ["Adil tebliğci", "Dirayetli hükümdar"],
        "contribution": "200 bin çadırlık Türk kitlesinin barışçıl biçimde Müslüman olmasını sağlayarak Türk tarihinin dönüm noktasını gerçekleştirdi.",
        "harm": "Budist Hoten Krallığı'nın ani karşı taarruzlarında kardeşi Arslan Han şehit düştü.",
        "wives": [],
        "children": [
          {"name": "Ali Arslan Han", "mother": "", "note": "Hoten savaşında şehit düştü", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Hoten Cihadı", "when": "965", "foe": "Budist Hoten Krallığı", "result": "zafer", "note": "Tarım havzasındaki direniş kırıldı."}
        ],
        "legends": ["960 yılındaki 200 bin çadırlık ihtida hadisesi İbnü'l-Esîr kroniğinde İslam tarihinin en büyük toplu hidayet olayı olarak anılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, KARAHANLILAR", "url": "https://islamansiklopedisi.org.tr/karahanlilar"}
        ]
      },
      {
        "id": "karahanli-tamgac-bugra",
        "name": "Tamgaç Buğra Han",
        "aliases": ["İbrâhim b. Nasr", "Ebû İshak İbrâhim Tamgaç Han"],
        "title": "Batı Kağanı / Tamgaç Han",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1068,
        "deathNote": "Semerkant'ta felç geçirerek vefat etti",
        "reign": [1052, 1068],
        "reignNote": "Batı Karahanlı Devleti'nin altın çağı.",
        "summary": "Batı Karahanlıların kurucusu ve İslam dünyasının en adil hükümdarlarından biri. Semerkant'ı ilim ve medeniyet yuvası yaptı; Semerkant Darüşşifası'nı kurdu. Yusuf Has Hacib ünlü Kutadgu Bilig eserini Doğu hükümdarı Tamgaç Uluğ Buğra Han'a ithaf ederken onun adalet anlayışından ilham aldı.",
        "traits": ["Hz. Ömer adaleti timsali", "Fakir babası", "Yolsuzluk düşmanı"],
        "contribution": "Semerkant'ta muazzam bir hastane, tıp medresesi ve kütüphane kurdu; piyasada fiyat narhını titizlikle korudu.",
        "harm": "Selçuklularla zaman zaman sürtüşmeye girdi.",
        "wives": [],
        "children": [
          {"name": "Şemsülmülk Nasr", "mother": "", "note": "Babasından sonra kağan oldu, Melikşah'ın bacanağı", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Semerkant Kuşatması ve İstiklâl", "when": "1052", "foe": "Doğu Karahanlı birlikleri", "result": "zafer", "note": "Semerkant'ı alarak Batı Karahanlı devletini tam bağımsız kıldı."}
        ],
        "legends": ["Geceleri kılık değiştirerek pazarları denetlediği, kasapların terazilerini bizzat kontrol ettiği ve çalınan tek bir elmanın hesabını sorduğu Avfî'nin Cevâmiu'l-Hikâyât eserinde anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, TAMGAÇ BUĞRA HAN", "url": "https://islamansiklopedisi.org.tr/tamgac-bugra-han"},
          {"title": "TDV İslâm Ansiklopedisi, KARAHANLILAR", "url": "https://islamansiklopedisi.org.tr/karahanlilar"}
        ]
      }
    ]
  },
  {
    "id": "gazneli",
    "name": "Gazneliler",
    "short": "Gazneliler",
    "aliases": ["Gazne Devleti", "Yemînîler", "Sebükteginîler"],
    "region": "turkistan",
    "start": 963,
    "end": 1187,
    "startNote": "Alp Tigin'in 963'te Gazne şehrini fethederek bağımsız beyliğini kurmasıyla temellendi.",
    "endNote": "1187 yılında Gurluların son merkez Lahor'u zaptedip Hüsrev Melik'i esir almasıyla yıkıldı.",
    "capital": "Gazne, ardından Lahor",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Utbî (Târîh-i Yemînî), Beyhakî (Târîh-i Beyhakī) ve Bîrûnî'nin eserleriyle eksiksiz sabittir.",
    "summary": "Samanîlerin Türk kumandanı Alp Tigin ve damadı Sebüktegin tarafından Afganistan'da kurulan, Sultan Mahmud devrinde Hindistan'a yapılan 17 büyük seferle İslamiyet'i Hint alt kıtasına taşıyan cihan devleti. 'Sultan' unvanını İslam tarihinde ilk kullanan hükümdar Sultan Mahmud oldu. Sarayında Bîrûnî ve Firdevsî gibi devasa dehaları ağırladılar. 1040 Dandanakan'da Selçuklulara yenilip batı topraklarını kaybettiler; 1187'de Gurlular tarafından yıkıldılar.",
    "legacy": "Hindistan'da İslamiyet'in kök salmasını sağladı; bugünkü Pakistan ve Bangladeş'in İslami kimliğinin temelini attı. Türk askerî dehâsını fil birlikleriyle harmanladı.",
    "essay": [
      "Gazneliler, Samani Devleti'nin ordu komutanı Alp Tigin'in 963'te Gazne kalesini fethetmesiyle kuruldu. Asıl hanedan kurucusu, Alp Tigin'in kölesi ve damadı olan, 'Pendnâme' adlı eseriyle bilinen bilge hükümdar Sebüktegin (977-997) oldu. Sebüktegin, Hint Racası Caypal'ı mağlup ederek Pencap kapılarını açtı.",
      "Sultan Mahmud (998-1030) devrinde Gazne İmparatorluğu gücünün zirvesine ulaştı. Abbasi Halifesi el-Kādir-Billâh tarafından 'Yemînüddövle' (Devletin Sağ Kolu) lakabı verilen Mahmud, Hindistan'a 17 büyük sefer düzenledi. 1026 yılında Gucerat'taki Somnath Tapınağı Seferi İslam dünyasında bir efsaneye dönüştü. Sarayında 400 şair ve yüzlerce âlim besleyen Mahmud, Bîrûnî için 'Sarayımın en değerli hazinesi' demiştir.",
      "Mahmud'un oğlu Sultan Mesud döneminde Selçuklularla yapılan 1040 Dandanakan Muharebesi'ndeki ağır yenilgi Horasan ve İran'ın tamamen elden çıkmasına yol açtı. Devlet merkezini Hindistan'daki Lahor'a kaydıran Gazneliler, 1187'de Afganistan'ın yerel kavmi Gurluların Lahor'u zaptetmesiyle tarihe karıştı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, GAZNELİLER", "url": "https://islamansiklopedisi.org.tr/gazneliler"},
      {"title": "TDV İslâm Ansiklopedisi, MAHMÛD-I GAZNEVÎ", "url": "https://islamansiklopedisi.org.tr/mahmud-i-gaznevi"},
      {"title": "TDV İslâm Ansiklopedisi, SEBÜK TEGİN", "url": "https://islamansiklopedisi.org.tr/sebuk-tegin"}
    ],
    "rulers": [
      {
        "id": "gazneli-sebuktegin",
        "name": "Sebüktegin",
        "aliases": ["Ebû Mansûr Sebüktegin", "Nâsırüddin Sebüktegin"],
        "title": "Emir / Nâsırüddin",
        "birth": 942,
        "birthNote": "Barsgan (Kırgızistan) civarında 942'de doğdu",
        "death": 997,
        "deathNote": "Belh seferi dönüşünde vefat etti",
        "reign": [977, 997],
        "reignNote": "20 yıl boyunca hanedanın gerçek temellerini attı.",
        "summary": "Gazneli hanedanının gerçek kurucusu. Alp Tigin'in kızıyla evlendi, beylerin ittifakıyla tahta çıktı. Hindistan Şahı Caypal'ı iki kez mağlup ederek Peşaver'i fethetti. Oğlu Mahmud için yazdığı devlet ahlakı kitabı Pendnâme ile meşhurdur.",
        "traits": ["Mütefekkir lider", "Gazi", "Adil"],
        "contribution": "Dağınık Gazne garnizonunu imparatorluğa dönüştürdü; Hindistan fetihlerinin yolunu açtı.",
        "harm": "Ölürken yerine küçük oğlu İsmail'i veliaht bırakması Mahmud ile taht kavgasına yol açtı.",
        "wives": [
          {"name": "Alp Tigin'in kızı", "note": "Hanedan meşruiyetini sağlayan eşi", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Sultan Mahmud", "mother": "", "note": "Büyük cihan sultanı", "certainty": "kesin"},
          {"name": "İsmail", "mother": "", "note": "Kısa süre tahta oturdu", "certainty": "kesin"},
          {"name": "Nasr", "mother": "", "note": "Sipehsalar", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Lâmğan Muharebesi", "when": "988", "foe": "Hindu Şahi Krallığı (Caypal)", "result": "zafer", "note": "Hint ordusu ve yüzlerce savaş fili bozguna uğratıldı, Peşaver alındı."}
        ],
        "legends": ["Avda yakaladığı bir ceylan yavrusunu annesinin acıklı bakışlarına kıyamayarak serbest bıraktığı ve rüyasında bu merhameti sebebiyle kendisine hükümdarlık müjdelendiği anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, SEBÜK TEGİN", "url": "https://islamansiklopedisi.org.tr/sebuk-tegin"}
        ]
      },
      {
        "id": "gazneli-mahmud",
        "name": "Sultan Mahmud",
        "aliases": ["Mahmûd-ı Gaznevî", "Yemînüddövle", "Seyfüddevle Mahmud"],
        "title": "Sultan / Yemînüddövle",
        "birth": 971,
        "birthNote": "971 yılında doğdu",
        "death": 1030,
        "deathNote": "Gazne'de veremden vefat etti",
        "reign": [998, 1030],
        "reignNote": "32 yıl boyunca dünyaya nam salan hükümdarlık.",
        "summary": "Tarihte ilk 'Sultan' unvanını alan hükümdar. Hindistan'a düzenlediği 17 seferle putperest tapınakları yıktı, Somnath Seferi'yle efsaneleşti ve İslam'ı Pencap ve Gucerat'a yaydı. Gazne'yi saraylar, kütüphaneler ve camilerle bir dünya başkenti yaptı.",
        "traits": ["Büyük cihangir", "Put kırıcı gazi", "Sanat ve ilim hamisi"],
        "contribution": "Hindistan'da İslam hakimiyetinin temellerini attı; Bîrûnî ve Firdevsî'yi himaye etti.",
        "harm": "Sürekli Hindistan seferleriyle ordusunu batıdaki Türkmen göçlerini (Selçukluları) denetlemekte yetersiz bıraktı.",
        "wives": [
          {"name": "Kavsariyye Hatun", "note": "Mesud ve Muhammed'in annesi", "certainty": "kesin"}
        ],
        "children": [
          {"name": "I. Mesud", "mother": "Kavsariyye Hatun", "note": "Dandanakan'da yenilen sultan", "certainty": "kesin"},
          {"name": "Muhammed", "mother": "Kavsariyye Hatun", "note": "Kısa süre tahta oturdu", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Somnath Seferi", "when": "1026", "foe": "Gucerat Racalıkları", "result": "zafer", "note": "Devasa Somnath tapınağı fethedildi, tapınak putları Gazne ve Mekke'ye gönderildi."},
          {"name": "Peşaver Muharebesi", "when": "1001", "foe": "Raca Caypal", "result": "zafer", "note": "Caypal esir edildi, intihar etti."}
        ],
        "legends": ["Somnath putunun rahipleri milyonlarca altın fidye teklif ettiğinde 'Ben put satan değil, put kıran Mahmud olarak anılmak isterim' diyerek gürzüyle putu parçaladığı meşhurdur."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, MAHMÛD-I GAZNEVÎ", "url": "https://islamansiklopedisi.org.tr/mahmud-i-gaznevi"}
        ]
      },
      {
        "id": "gazneli-mesud",
        "name": "Sultan I. Mesud",
        "aliases": ["Cemâlüddevle Mesud", "Gazi Mesud"],
        "title": "Sultan",
        "birth": 998,
        "birthNote": "998'de doğdu",
        "death": 1041,
        "deathNote": "Giri Kalesi'nde tahttan indirilip yeğeni tarafından öldürüldü",
        "reign": [1030, 1040],
        "reignNote": "1040 Dandanakan hezimetiyle son buldu.",
        "summary": "Sultan Mahmud'un oğlu. Bizzat savaş meydanlarında gürzü ve kılıcıyla cenk eden devasa cüsseli bir pehlivandı. Ancak Selçukluların Horasan'daki taktik yıpratma stratejisini küçümsedi; 1040 Dandanakan Muharebesi'nde ordusu dağılınca Horasan'ı Selçuklulara kaptırdı.",
        "traits": ["Pehlivan kuvvetli", "Kişisel cesareti yüksek", "Stratejide inatçı"],
        "contribution": "Hindistan'da Hansi kalesini fethederek gaza faaliyetlerini sürdürdü.",
        "harm": "Kibir ve inadı yüzünden Dandanakan'da imparatorluğun belkemiğini kırdı; Gaznelileri bölgesel bir Hindistan krallığına küçülttü.",
        "wives": [],
        "children": [
          {"name": "Mevdud b. Mesud", "mother": "", "note": "Babasından sonra Gazne tahtına geçti", "certainty": "kesin"},
          {"name": "İbrahim b. Mesud", "mother": "", "note": "Uzun süre hüküm süren istikrarlı sultan", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Dandanakan Muharebesi", "when": "1040", "foe": "Büyük Selçuklu Devleti (Tuğrul ve Çağrı)", "result": "yenilgi", "note": "Gazneli ordusu üç günlük kuşatmadan sonra çöktü, Mesud canını zor kurtardı."}
        ],
        "legends": ["Târîh-i Beyhakī'de savaş meydanında tek başına yüzlerce düşman arasına daldığı ve devasa çelik gürzünü savurduğu ayrıntılarıyla anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, GAZNELİLER", "url": "https://islamansiklopedisi.org.tr/gazneliler"}
        ]
      }
    ]
  },
  {
    "id": "harzemsah",
    "name": "Harzemşahlar",
    "short": "Harzemşahlar",
    "aliases": ["Hârizmşahlar", "Anuşteginliler"],
    "region": "turkistan",
    "start": 1097,
    "end": 1231,
    "startNote": "Selçuklu valisi Anuş Tegin'in oğlu Kutbeddin Muhammed'in Hârizmşah unvanıyla göreve gelmesiyle temellendi.",
    "endNote": "1231 yılında Celâleddin Mengüberti'nin Meyyâfârikīn dağlarında bir Kürt köylüsü tarafından öldürülmesiyle yıkıldı.",
    "capital": "Gürgenç (Köhne Ürgenç), ardından Tebriz",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Nesevî (Sîret-i Celâleddin), Cüveynî (Târîh-i Cihângüşâ) ve İbnü'l-Esîr ile sabittir.",
    "summary": "Aral gölü güneyindeki Hârizm havzasında Begdili Türkmen boyundan Anuş Tegin soyunca kurulan, 12. yüzyıl sonunda Büyük Selçuklu mirasını devralarak İran, Maveraünnehir ve Horasan'a hakim olan devasa imparatorluk. Alâeddin Tekiş ve oğlu Alâeddin Muhammed devrinde en geniş sınırlarına ulaştı. 1218 Otrar faciası sonrası başlayan Cengiz Han Moğol istilasıyla yıkıldı. Son hükümdar Celâleddin Mengüberti Moğollara karşı destansı bir direniş gösterdi.",
    "legacy": "Moğol kasırgasına karşı İslam dünyasının son büyük kalkanı oldu. Celâleddin Harzemşah'ın kahramanlığı Doğu ve Batı edebiyatında bağımsızlık ve cesaret sembolü olarak ölümsüzleşti.",
    "essay": [
      "Harzemşahlar Devleti, Selçuklu Sultanı Melikşah'ın taştdârı (ibrikçibaşı) olan Begdili boyu mensubu Anuş Tegin Garçai'nin soyundan gelir. 1097'de Hârizm valisi olan Kutbeddin Muhammed ve oğlu Atsız (1128-1156), Sultan Sencer'e karşı defalarca bağımsızlık mücadelesi vererek devleti güçlendirdi.",
      "İl Arslan'ın oğlu Alâeddin Tekiş (1172-1200), Karahıtay baskısını kırdı ve 1194'te son Irak Selçuklu Sultanı III. Tuğrul'u mağlup ederek bütün İran'ı egemenliği altına aldı. Halife Nâsır-Lidênillâh ile çatışmaya giren Tekiş, doğunun tartışmasız en büyük gücü oldu. Oğlu Alâeddin Muhammed (1200-1220) ise Gurluları ve Karahanlıları yıkarak sınırlarını Umman Denizi'nden Seyhun'a kadar genişletti.",
      "Ancak 1218 yılında Otrar valisi İnalcık'ın Moğol kervanındaki 450 Müslüman tüccarı casusluk iddiasıyla öldürtmesi (Otrar Faciası), Cengiz Han'ın devasa ordularıyla İslam dünyasına çullanmasına yol açtı. Alâeddin Muhammed Hazar Denizi'nde Abeskun adasında sefalet içinde öldü. Oğlu Celâleddin Mengüberti, 11 yıl boyunca Hindistan'dan Azerbaycan'a kadar Moğollarla tek başına savaştı; İndus nehrine atlayışı Cengiz Han'ı bile hayran bıraktı. 1230'da Yassıçemen'de Anadolu Selçuklularına yenildikten sonra 1231'de şehit edildi ve devlet son buldu."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, HÂRİZMŞAHLAR", "url": "https://islamansiklopedisi.org.tr/harizmsahlar"},
      {"title": "TDV İslâm Ansiklopedisi, CELÂLEDDİN HÂRİZMŞAH", "url": "https://islamansiklopedisi.org.tr/celaleddin-harizmsah"},
      {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN MUHAMMED", "url": "https://islamansiklopedisi.org.tr/alaeddin-muhammed"}
    ],
    "rulers": [
      {
        "id": "harzemsah-tekis",
        "name": "Alâeddin Tekiş",
        "aliases": ["Tekiş b. İl Arslan"],
        "title": "Hârizmşah / Sultan",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1200,
        "deathNote": "Hârizm yolunda Şehristan civarında vefat etti",
        "reign": [1172, 1200],
        "reignNote": "28 yıl hüküm sürdü.",
        "summary": "İl Arslan'ın oğlu. Harzemşahları bölgesel bir emirlikten cihanşümul imparatorluğa yükselten hükümdar. 1194'te Rey yakınlarında Irak Selçuklularına son verdi; Abbasi halifesini siyasi vesayetine aldı.",
        "traits": ["Kurt politikacı", "Büyük stratejist", "Yorulmaz fatih"],
        "contribution": "İran, Horasan ve Hârizm'i tek bayrak altında toplayarak Selçuklu mirasını devraldı.",
        "harm": "Abbasi halifesiyle girdiği sert çatışma İslam dünyasındaki mezhep ve meşruiyet dengelerini sarstı.",
        "wives": [
          {"name": "Terken Hatun", "note": "Kıpçak Kanglı boyundan, devlette muazzam nüfuz sahibi güçlü hatun", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Alâeddin Muhammed", "mother": "Terken Hatun", "note": "Babasından sonra tahta geçen imparator", "certainty": "kesin"},
          {"name": "Taceddin Ali Şah", "mother": "", "note": "İsfahan valisi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Rey Muharebesi", "when": "1194", "foe": "Irak Selçuklu Sultanı III. Tuğrul", "result": "zafer", "note": "Tuğrul öldürüldü, Irak Selçuklu devleti tamamen yıkıldı."},
          {"name": "Buhara Seferi", "when": "1182", "foe": "Karahıtay valileri", "result": "zafer", "note": "Buhara fethedildi."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, TEKİŞ", "url": "https://islamansiklopedisi.org.tr/tekis"}
        ]
      },
      {
        "id": "harzemsah-alaeddin-muhammed",
        "name": "Alâeddin Muhammed",
        "aliases": ["Kutbüddin Muhammed", "İkinci İskender", "Sencer-i Sânî"],
        "title": "Hârizmşah / Sultan",
        "birth": 1169,
        "birthNote": "1169 doğumlu",
        "death": 1220,
        "deathNote": "Hazar Denizi'ndeki Âbeskûn adasında zatürre ve kederden sefalet içinde öldü",
        "reign": [1200, 1220],
        "reignNote": "20 yıllık saltanatı ihtişamla başlayıp Moğol felaketiyle bitti.",
        "summary": "Tekiş'in oğlu. Kendisini 'İkinci İskender' ilan etti; Gurluları, Karahanlıları ve Karahıtayları yıkarak devasa bir imparatorluk kurdu. Ancak annesi Terken Hatun'un baskısı, Otrar Faciası ve Moğol ordusu karşısında ordusunu şehirlere dağıtıp kaçması İslam dünyasının tarihteki en büyük Moğol yıkımına uğramasına neden oldu.",
        "traits": ["Gururlu", "Hırslı fakat kriz anında panikleyen"],
        "contribution": "İmparatorluk sınırlarını Umman'dan Seyhun'a kadar genişletti.",
        "harm": "Otrar Faciası'na göz yumarak Cengiz Han istilasını tetikledi; ordusunu meydan savaşı yerine kalelere bölerek İslam şehirlerinin tek tek katledilmesine sebep oldu.",
        "wives": [],
        "children": [
          {"name": "Celâleddin Mengüberti", "mother": "", "note": "Efsanevi son hükümdar ve kahraman", "certainty": "kesin"},
          {"name": "Gıyâseddin Pîrşah", "mother": "", "note": "Irak meliki", "certainty": "kesin"},
          {"name": "Uzlagşah", "mother": "Terken Hatun soyundan", "note": "Terken Hatun'un veliaht yaptırdığı şehzade", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Otrar Faciası ve Moğol İstilası", "when": "1219-1220", "foe": "Moğol İmparatorluğu (Cengiz Han)", "result": "yenilgi", "note": "Buhara, Semerkant ve Gürgenç düştü, milyonlarca insan katledildi, sultan kaçtı."}
        ],
        "legends": ["Ölürken üzerinde kefen bezi bile bulunamadığı, sırtındaki yırtık gömlekle Hazar'daki ıssız adada toprağa verildiği anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN MUHAMMED", "url": "https://islamansiklopedisi.org.tr/alaeddin-muhammed"}
        ]
      },
      {
        "id": "harzemsah-celaleddin",
        "name": "Celâleddin Mengüberti",
        "aliases": ["Celâleddin Hârizmşah", "Mengüberti", "Mengü-Berti"],
        "title": "Hârizmşah / Sultan",
        "birth": 1199,
        "birthNote": "Yaklaşık 1199 doğumlu",
        "death": 1231,
        "deathNote": "Meyyâfârikīn dağlarında bir eşkıya tarafından şehit edildi",
        "reign": [1220, 1231],
        "reignNote": "11 yıllık efsanevi direniş destanı.",
        "summary": "Harzemşahların son hükümdarı ve Türk-İslam tarihinin en büyük kahramanlarından biri. Cengiz Han Moğollarına karşı Pervan'da İslam dünyasının ilk büyük zaferini kazandı. İndus nehrini atıyla geçerek Hindistan'a sığındı; geri dönüp Azerbaycan ve Gürcistan'ı fethederek Tebriz'de devletini yeniden kurdu. 11 yıl boyunca durmaksızın Moğollarla savaştı.",
        "traits": ["Yenilmez cengaver", "Döneminin Rüstem'i", "Korkusuz lider"],
        "contribution": "Moğolların yenilmezlik efsanesini Pervan'da yıktı; Kafkasya ve Doğu Anadolu'da direniş ruhunu canlı tuttu.",
        "harm": "Eyyûbîler ve Anadolu Selçukluları ile ittifak kurmak yerine Ahlat'ı kuşatıp Yassıçemen'de I. Alâeddin Keykubad ile savaşması İslam birliğini parçaladı.",
        "wives": [
          {"name": "Melike Hatun", "note": "İldenizli Atabeyi Özbek'in eşi, Selçuklu II. Tuğrul'un kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Menkeli", "mother": "", "note": "Oğlu", "certainty": "olasi"}
        ],
        "wars": [
          {"name": "Pervan Muharebesi", "when": "1221", "foe": "Moğol Ordusu (Şigi Kutuku)", "result": "zafer", "note": "Cengiz Han'ın seçkin ordusu imha edildi; Moğollara karşı ilk büyük İslam zaferi kazanıldı."},
          {"name": "İndus Nehri Yarma Harekâtı", "when": "1221", "foe": "Cengiz Han bizzat", "result": "yenilgi", "note": "Kuşatılınca atını uçurumdan coşkun İndus nehrine sürdü, Cengiz Han hayranlıkla izledi."},
          {"name": "Garni Muharebesi", "when": "1225", "foe": "Gürcistan Krallığı", "result": "zafer", "note": "Tiflis fethedildi, Gürcü ordusu dağıtıldı."},
          {"name": "Yassıçemen Muharebesi", "when": "1230", "foe": "Anadolu Selçukluları (I. Alâeddin Keykubad) ve Eyyûbîler", "result": "yenilgi", "note": "İslam dünyasının iki büyük Türk hükümdarı karşılaştı, Celâleddin yenildi."}
        ],
        "legends": ["İndus nehrine atlayıp karşı kıyıya geçtiğinde Cengiz Han oğullarına dönüp: 'Bir babanın böyle bir oğlu olmalı! İki elinde kılıçla azgın nehri yarıp geçti' demiştir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, CELÂLEDDİN HÂRİZMŞAH", "url": "https://islamansiklopedisi.org.tr/celaleddin-harizmsah"},
          {"title": "TDV İslâm Ansiklopedisi, HÂRİZMŞAHLAR", "url": "https://islamansiklopedisi.org.tr/harizmsahlar"}
        ]
      }
    ]
  }
]

out = Path("/Users/hayabusa/turk-tarih-atlasi/data/raw/e-turkistan-islam.json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data)} states to {out}")
