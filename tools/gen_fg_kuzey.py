#!/usr/bin/env python3
"""Generate data/raw/f-altin-orda.json and data/raw/g-kuzey-hanliklari.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"

# ==========================================
# BLOCK F: ALTIN ORDA VE STEP HANLIKLARI
# ==========================================
data_f = [
    {
        "id": "altin-orda",
        "name": "Altın Orda Hanlığı",
        "short": "Altın Orda (Cuci Ulusu)",
        "aliases": ["Altın Ordu", "Deşt-i Kıpçak Hanlığı", "Cuci Ulusu", "Kıpçak Hanlığı", "Golden Horde"],
        "region": "kuzey",
        "start": 1227,
        "end": 1502,
        "startNote": "Cengiz Han'ın büyük oğlu Cuci'nin vefatı ve Batu Han'ın Deşt-i Kıpçak seferleriyle 1227-1242'de kuruldu.",
        "endNote": "1502 yılında Kırım Hanı I. Mengli Giray'ın Saray şehrini zaptetmesi ve son han Şeyh Ahmed'in yenilgisiyle yıkıldı.",
        "capital": "Saray (Sarây-ı Bâtû ve Sarây-ı Berke)",
        "religion": "İslamiyet (Özbek Han devrinden itibaren resmi din; önceleri Şamanizm / Gök Tanrı)",
        "confidence": "kayit",
        "confidenceNote": "Cüveynî, Reşîdüddin (Câmiu't-Tevârîh), İbn Battûta seyahatnamesi ve Rus vakayinâmeleriyle sabittir.",
        "summary": "Cuci'nin oğlu Batu Han tarafından Deşt-i Kıpçak, Harezm, İdil boyu ve Doğu Avrupa'da kurulan, yaklaşık üç asır boyunca Rus knezliklerini haraca bağlayan ve Avrasya bozkırlarını birleştiren ulu Türk-Tatar devleti. Berke Han devrinde İslamiyet kabul edildi; Memlüklerle ittifak kurularak İlhanlılar durduruldu. Özbek Han devrinde İslam resmi din ilan edildi ve imparatorluk en parlak devrini yaşadı. Timur istilaları ve taht kavgaları sonucu dağılarak Kazan, Kırım, Astrahan ve Sibir hanlıklarına bölündü.",
        "legacy": "Rus knezliklerini 250 yıl boyunca 'Tatar Boyunduruğu' (Yoke) altında tutarak Rusların birliğini geciktirdi; İpek Yolu ve Kürk Yolu ticaretini güvene aldı; Saray şehrini doğunun en büyük kültür ve ticaret merkezlerinden biri yaptı.",
        "essay": [
            "Altın Orda Hanlığı, Moğol istilası sonrası Deşt-i Kıpçak sahasına yerleşen yönetici tabakanın kısa sürede bölgedeki yoğun Kıpçak Türk nüfusuyla kaynaşıp Türkleşmesi ve İslamlaşması sonucu tam anlamıyla bir Türk-Tatar imparatorluğuna dönüştü.",
            "Batu Han, 1236-1242 Batı Seferi ile Moskova, Vladimir, Kiev, Polonya ve Macaristan'ı ezerek Adriyatik Denizi'ne kadar ilerledi. Başkent Saray'ı İdil (Volga) kıyısında kurdu. Kardeşi Berke Han İslamiyeti kabul etti; 1258 Bağdat fâciası sonrası İlhanlı Hülâgû'ya savaş açarak Memlük Sultanı Baybars ile tarihi bir ittifak kurdu.",
            "Gıyâseddin Muhammed Özbek Han (1313-1341) İslamiyeti devlet dini yaptı. İbn Battûta, Saray şehrinin camilerini, hanlarını, saraylarını ve zenginliğini hayranlıkla kaydeder. Canıbek Han'ın ardından başlayan iç karışıklıklar ('Büyük Kargaşa'), Toktamış Han tarafından geçici olarak toparlandıysa da Timur'un 1391 ve 1395 seferleri Saray şehrini yerle bir etti ve devletin belini kırdı. 1502'de Kırım Hanlığı tarafından son verildi."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, ALTIN ORDA", "url": "https://islamansiklopedisi.org.tr/altin-orda"},
            {"title": "TDV İslâm Ansiklopedisi, BATU HAN", "url": "https://islamansiklopedisi.org.tr/batu-han"},
            {"title": "TDV İslâm Ansiklopedisi, BERKE HAN", "url": "https://islamansiklopedisi.org.tr/berke-han"},
            {"title": "TDV İslâm Ansiklopedisi, ÖZBEK HAN", "url": "https://islamansiklopedisi.org.tr/ozbek-han"}
        ],
        "rulers": [
            {
                "id": "altin-orda-batu",
                "name": "Batu Han",
                "aliases": ["Sain Han", "Batu Khan"],
                "title": "Uluğ Han / Fatih",
                "birth": 1205,
                "birthNote": "Cuci'nin ikinci oğlu olarak Moğol bozkırında doğdu",
                "death": 1255,
                "deathNote": "Saray şehrinde vefat etti",
                "reign": [1227, 1255],
                "reignNote": "1227'de babasının ulusunu devraldı; 1236-1242 seferleriyle Altın Orda'yı fiilen kurdu.",
                "summary": "Altın Orda Devleti'nin kurucusu ve tarihin en kudretli fatihlerinden biri. Rus knezliklerini, Polonya ve Macar krallıklarını bozguna uğrattı. İdil boyunda Saray şehrini kurdu. 'Sain Han' (Adil/İyi Han) unvanıyla anıldı.",
                "traits": ["Büyük stratejist", "Teşkilatçı", "Adil hükümdar", "Askeri deha"],
                "contribution": "Avrasya bozkırlarını tek idarede birleştirdi; Deşt-i Kıpçak'ta asırlarca sürecek Türk-Tatar devlet geleneğini kurdu.",
                "harm": "Doğu Avrupa ve Rus şehirlerinde ağır tahribat ve can kaybına yol açtı.",
                "wives": [
                    {"name": "Borakçin Hatun", "note": "Büyük baş hatun", "certainty": "kesin"}
                ],
                "children": [
                    {"name": "Sartak Han", "mother": "", "note": "Hristiyanlığı kabul eden veliaht, kısa süre han oldu", "certainty": "kesin"},
                    {"name": "Tokokan", "mother": "", "note": "Mengü Timur'un babası", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Rus Seferi (Vladimir ve Moskova)", "when": "1237-1238", "foe": "Rus Knezlikleri (Yuri II)", "result": "zafer", "note": "Ryazan, Kolomna, Moskova ve Vladimir zaptedildi."},
                    {"name": "Sit Nehri Muharebesi", "when": "1238", "foe": "Vladimir Büyük Dükalığı", "result": "zafer", "note": "Büyük Knez Yuri öldürüldü, Rusya tamamen itaat altına alındı."},
                    {"name": "Mohi Muharebesi", "when": "1241", "foe": "Macaristan Krallığı (IV. Bela)", "result": "zafer", "note": "Sajo nehri kıyısında Macar ve Templar şövalye ordusu imha edildi."},
                    {"name": "Legnica (Liegnitz) Muharebesi", "when": "1241", "foe": "Polonya ve Alman Şövalyeleri (II. Henryk)", "result": "zafer", "note": "Polonya dükü ve şövalye orduları imha edildi."}
                ],
                "legends": ["Moğol kurultayına gitmeyip 'hastayım' diyerek kendi hanlığında kalması ve imparatorluk kaderini Saray'dan belirlemesi efsaneleşmiştir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, BATU HAN", "url": "https://islamansiklopedisi.org.tr/batu-han"}
                ]
            },
            {
                "id": "altin-orda-berke",
                "name": "Berke Han",
                "aliases": ["Birkai Khan"],
                "title": "Han / Mücahid",
                "birth": 1208,
                "birthNote": "Cuci'nin üçüncü oğlu olarak doğdu",
                "death": 1266,
                "deathNote": "Kafkasya seferi sırasında Tiflis yakınlarında Kura Irmağı boyunda vefat etti",
                "reign": [1257, 1266],
                "reignNote": "İslamiyeti kabul eden ilk Altın Orda hükümdarı.",
                "summary": "Batu Han'ın kardeşi. Buhara'da Şeyh Seyfeddin Bâharzî vasıtasıyla Müslüman oldu. Hülâgû'nun 1258'de Bağdat'ı tahrip edip Abbâsî halifesini katletmesine öfkelenerek İlhanlılar'a savaş açtı. Mısır Memlük Sultanı I. Baybars ile ilk Türk-İslam ittifakını kurdu. Sarây-ı Berke şehrini imar etti.",
                "traits": ["Mütedeyyin Müslüman", "Cesur başbuğ", "Diplomat", "Adil"],
                "contribution": "Altın Orda'nın İslamlaşmasını başlattı; Memlüklerle kurduğu ittifakla İslam dünyasının İlhanlılar tarafından tamamen yutulmasını önledi.",
                "harm": "İlhanlılar ile Altın Orda arasında uzun sürecek kardeş kavgalarını ve Kafkasya kanlı çatışmalarını başlattı.",
                "wives": [
                    {"name": "Cicek Hatun", "note": "Müslüman eşi", "certainty": "olasi"}
                ],
                "children": [],
                "wars": [
                    {"name": "Terek Irmağı Muharebesi", "when": "1262", "foe": "İlhanlı Devleti (Hülâgû Han)", "result": "zafer", "note": "Hülâgû'nun ordusu buz tutmuş Terek üzerinde kırılan buzlar ve süvari hücumuyla bozguna uğratıldı."}
                ],
                "legends": ["Hülâgû'nun Bağdat katliamını duyduğunda 'O masum Müslümanların kanını döktü, Allah şahidim olsun ki bunun hesabını soracağım' diye ant içtiği rivayet edilir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, BERKE HAN", "url": "https://islamansiklopedisi.org.tr/berke-han"}
                ]
            },
            {
                "id": "altin-orda-ozbek",
                "name": "Gıyâseddin Muhammed Özbek Han",
                "aliases": ["Özbek Han", "Sultan Muhammed Özbek"],
                "title": "Uluğ Han / Padişah",
                "birth": 1282,
                "birthNote": "Tuğrulça'nın oğlu olarak Saray'da doğdu",
                "death": 1341,
                "deathNote": "Başkent Saray'da vefat etti",
                "reign": [1313, 1341],
                "reignNote": "28 yıllık saltanatıyla Altın Orda'nın altın çağını yaşattı.",
                "summary": "Altın Orda'nın en parlak hükümdarı. İslamiyeti devletin resmi dini ilan etti. Bozkır halklarının İslamlaşmasını tamamladı. Başkent Saray'ı camiler, medreseler ve saraylarla bezedi; İbn Battûta onun meclislerini hayranlıkla tasvir etti. Adı, bugünkü 'Özbek' Türk boyunun etnonimine dönüştü.",
                "traits": ["Karizmatik lider", "Reformcu", "İlim ve sanat hamisi", "Ticaret koruyucusu"],
                "contribution": "İslamiyet'i devletin resmi dini yaptı; Altın Orda'yı dünyanın en zengin ticaret kavşaklarından biri haline getirdi; Rus knezliklerini mutlak vergiye bağladı.",
                "harm": "Moskova Knezliği'nin güçlenmesine göz yumarak Kalita İvan'a büyük knezlik yetkisi verdi, bu da gelecekte Rus birliğinin önünü açtı.",
                "wives": [
                    {"name": "Taydula Hatun", "note": "Devlet işlerinde çok etkili baş hatun", "certainty": "kesin"},
                    {"name": "Bayalun Hatun", "note": "Bizans İmparatoru IX. Andronikos'un kızı", "certainty": "kesin"}
                ],
                "children": [
                    {"name": "Tini Bek", "mother": "Taydula Hatun", "note": "Kısa süre tahta oturdu", "certainty": "kesin"},
                    {"name": "Canıbek Han", "mother": "Taydula Hatun", "note": "Babasından sonra tahta geçen büyük sultan", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Kafkasya İlhanlı Seferi", "when": "1319", "foe": "İlhanlı Devleti (Ebu Said Bahadır Han)", "result": "sonucsuz", "note": "Kür Irmağı boyunda çarpışmalar yapıldı."},
                    {"name": "Tver İsyanı Bastırması", "when": "1327", "foe": "Tver Rus Knezliği", "result": "zafer", "note": "İsyan eden Rus kenti yerle bir edildi, Moskova knezi vergi tahsildarı tayin edildi."}
                ],
                "legends": ["Seyyah İbn Battûta, Özbek Han'ın cuma namazına giderken halkın önünde tevazuyla yürüdüğünü ve sarayında âlimlerle dini münazaralar yaptığını hayranlıkla nakleder."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ÖZBEK HAN", "url": "https://islamansiklopedisi.org.tr/ozbek-han"}
                ]
            },
            {
                "id": "altin-orda-canibek",
                "name": "Celâleddin Mahmud Canıbek Han",
                "aliases": ["Canıbek Han", "Djani Beg"],
                "title": "Sultan / Han",
                "birth": 1315,
                "birthNote": "Saray şehrinde doğdu",
                "death": 1357,
                "deathNote": "Tebriz dönüşü hastalanarak oğlu Berdibek tarafından zehirlenerek şehit edildi",
                "reign": [1342, 1357],
                "reignNote": "Altın Orda'nın kudretli son büyük padişahı.",
                "summary": "Özbek Han'ın oğlu. Tebriz'i fethederek İlhanlı mirasçısı Çobanoğulları'na son verdi ve Azerbaycan'ı Altın Orda'ya kattı. Kefe'deki Ceneviz kolonisini kuşatması sırasında vebalı cesetleri mancınıkla surların içine fırlatması, tarihte ilk biyolojik savaş taktiği ve Kara Ölüm'ün Avrupa'ya yayılma noktası olarak anılır.",
                "traits": ["Cengaver fatih", "Mütefekkir", "Adaletli", "Şair ruhlu"],
                "contribution": "Azerbaycan ve Kafkasya'yı tamamen bağladı; Altın Orda sınırlarını en geniş haline getirdi.",
                "harm": "Ölümüyle birlikte hanlık 20 yıl sürecek kanlı taht kavgalarına ('Büyük Kargaşa') sürüklendi.",
                "wives": [],
                "children": [
                    {"name": "Berdibek Han", "mother": "", "note": "Babasını öldürerek tahtı ele geçiren zalim han", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Kefe Kuşatması", "when": "1346", "foe": "Ceneviz Cumhuriyeti (Kefe Kolonisi)", "result": "sonucsuz", "note": "Veba salgını sebebiyle kuşatma kaldırıldı; Ceneviz gemileri vebayı İtalya'ya taşıdı."},
                    {"name": "Tebriz Seferi", "when": "1356-1357", "foe": "Çobanoğulları Devleti (Melik Eşref)", "result": "zafer", "note": "Tebriz fethedildi, Melik Eşref asıldı, Azerbaycan bağlandı."}
                ],
                "legends": ["Kefe kuşatmasında mancınıkla surların içine atılan vebalı cesetlerin Avrupa'daki Kara Veba salgınını tetiklediği dünya tıp ve tarih literatüründe en çok tartışılan vakalardandır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, CANIBEK HAN", "url": "https://islamansiklopedisi.org.tr/canibek-han"}
                ]
            },
            {
                "id": "altin-orda-toktamis",
                "name": "Nâsırüddin Toktamış Han",
                "aliases": ["Toktamış", "Tokhtamysh"],
                "title": "Han",
                "birth": 1350,
                "birthNote": "Ak Orda bozkırında doğdu",
                "death": 1406,
                "deathNote": "Sibirya'da Tümen yakınlarında Şadibek ve İdigü taraftarlarınca öldürüldü",
                "reign": [1380, 1396],
                "reignNote": "Altın Orda'yı son kez tek bayrak altında birleştiren hükümdar.",
                "summary": "Emir Timur'un yardımıyla Ak Orda ve Altın Orda tahtını ele geçirdi. 1380 Kulikovo yenilgisinin ardından dağılan devleti topladı; 1382'de Moskova'yı kuşatarak yaktı ve Rusları tekrar haraca bağladı. Ancak nankörlük ederek Timur'un topraklarına (Harezm ve Azerbaycan) saldırdı; Timur'a karşı 1391 Kunduzca ve 1395 Terek muharebelerinde ağır hezimete uğrayarak Altın Orda'nın yıkımını getirdi.",
                "traits": ["Hırslı kumandan", "Fırsatçı", "İnatçı savaşçı", "Talihsiz siyasetçi"],
                "contribution": "Kulikovo sonrası Rus knezliklerinin bağımsızlık hevesini 1382 Moskova Seferi ile kırarak hanlığı birleştirdi.",
                "harm": "Hamisi Timur'a ihanet edip savaş açarak Saray ve Deşt-i Kıpçak şehirlerinin yerle bir olmasına, Altın Orda'nın parçalanmasına sebep oldu.",
                "wives": [
                    {"name": "Togaybike Hatun", "note": "Baş hatun", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "Celâleddin Han", "mother": "", "note": "1410 Grunwald Muharebesi'nde Polonya-Litvanya safında Töton Şövalyeleri'ni ezen Tatar komutan", "certainty": "kesin"},
                    {"name": "Kerim Berdi", "mother": "", "note": "Kısa süre hanlık yaptı", "certainty": "kesin"},
                    {"name": "Kebek Han", "mother": "", "note": "Han", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Moskova Kuşatması ve Yakılması", "when": "1382", "foe": "Moskova Knezliği (Dmitriy Donskoy)", "result": "zafer", "note": "Moskova tamamen yakıldı, 24.000 Rus öldürüldü, Rus knezleri tekrar vergiye bağlandı."},
                    {"name": "Kunduzca Irmağı Muharebesi", "when": "1391", "foe": "Timur İmparatorluğu (Emir Timur)", "result": "yenilgi", "note": "Volga boyunda Timur'un ordusu karşısında ordusu dağıldı."},
                    {"name": "Terek Irmağı Muharebesi", "when": "1395", "foe": "Timur İmparatorluğu (Emir Timur)", "result": "yenilgi", "note": "Altın Orda ordusu tamamen imha edildi; Timur başkent Saray'ı yerle bir etti."}
                ],
                "legends": ["Oğlu Celâleddin Han'ın komutasındaki Tatar süvarilerinin 1410 Tannenberg/Grunwald Muharebesi'nde sahte ricat taktiğiyle Töton Şövalyeleri'ni pusuya düşürüp Avrupa tarihini değiştirdiği meşhurdur."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, TOKTAMIŞ HAN", "url": "https://islamansiklopedisi.org.tr/toktamis-han"}
                ]
            }
        ]
    },
    {
        "id": "kazak-hanligi",
        "name": "Kazak Hanlığı",
        "short": "Kazak Hanlığı (Qazaq Eli)",
        "aliases": ["Kazakh Khanate", "Qazaq Khandygy", "Kazak Eli"],
        "region": "kuzey",
        "start": 1465,
        "end": 1847,
        "startNote": "1465'te Kerey Han ve Canıbek Han'ın Ebulhayr Han'dan ayrılarak Yedisu bölgesinde bağımsızlık ilan etmesiyle kuruldu.",
        "endNote": "1847 yılında son bağımsız han Kenesarı Han'ın şehit düşmesi ve Rus Çarlığı'nın bozkırı ilhakıyla sona erdi.",
        "capital": "Türkistan (Yesi), Sıgnak, Sozak",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Mirza Muhammed Haydar Duğlat (Târîh-i Reşîdî), Kadir Ali Bey (Câmiu't-Tevârîh) ve Rus arşivleriyle sabittir.",
        "summary": "15. yüzyıl ortalarında Özbek Ebulhayr Han'a isyan eden Kerey ve Canıbek Hanlar öncülüğünde Yedisu ve Çu vadilerinde kurulan bağımsız Türk devleti. 'Kazak' (hür, başına buyruk, yiğit) adını alan halk, bozkır Türk kültürünü ve Yesevî İslam geleneğini yaşattı. Kasım Han devrinde sınırları Hazar'dan Balkaş'a genişledi ve nüfusu 1 milyonu aştı. Üç Cüz (Ulu, Orta, Küçük Cüz) idari yapısıyla yönetildi. 18. yüzyılda Abılay Han Cungar istilasını kırarak ülkeyi birleştirdi. 1847'de Rus Çarlığı işgaliyle son buldu.",
        "legacy": "Modern Kazakistan devletinin doğrudan tarihi ve kültürel atasıdır; zengin bozkır epik geleneği (akınlar, cıravlar) ve töresi günümüze taşınmıştır.",
        "essay": [
            "Kazak Hanlığı'nın doğuşu, bozkır Türk halklarının hürriyet arayışının timsalidir. 1465-1466 civarında Şeybânî Ebulhayr Han'ın baskıcı yönetimine karşı çıkan Cuci soyundan Kerey ve Canıbek Hanlar, kendilerine bağlı boylarla Moğolistan Hanı Esen Buğa'nın topraklarına göç ederek Çu vadisinde bağımsız sancak açtılar.",
            "Kasım Han (1511-1521) döneminde Kazak Hanlığı Avrasya sahnesine büyük güç olarak çıktı. 'Kasım Han'ın Kaşka Yolu' (Qasym Khannyn Qasqa Zholy) adı verilen ilk Kazak töre kanunnamesi yürürlüğe girdi. 17. yüzyıl sonlarında Cungar (Kalmuk) istilası 'Aktaban Şubırındı' (Büyük Felaket) adıyla Kazak bozkırını sarstıysa da Abılay Han önderliğinde Anırakay Zaferi ile Cungarlar püskürtüldü.",
            "19. yüzyılda Rus Çarlığı bozkırı kalelerle kuşatarak cüzleri yutmaya başladı. Son Han Kenesarı Kasımoğlu (1841-1847), 10 yıl boyunca Rus sömürgeciliğine karşı gerilla ve meydan savaşı yürüterek destan yazdı; 1847'de şehit edilmesiyle hanlık devri kapandı."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, KAZAKLAR", "url": "https://islamansiklopedisi.org.tr/kazaklar"},
            {"title": "TDV İslâm Ansiklopedisi, ABILAY HAN", "url": "https://islamansiklopedisi.org.tr/abilay-han"},
            {"title": "TDV İslâm Ansiklopedisi, KASIM HAN", "url": "https://islamansiklopedisi.org.tr/kasim-han--kazak"}
        ],
        "rulers": [
            {
                "id": "kazak-kerey-canibek",
                "name": "Kerey Han ve Canıbek Han",
                "aliases": ["Girey Han ve Canıbek Han"],
                "title": "Müşterek Hanlar / Kurucular",
                "birth": 1420,
                "birthNote": "Deşt-i Kıpçak bozkırında doğdular",
                "death": 1480,
                "deathNote": "Yedisu bölgesinde vefat ettiler",
                "reign": [1465, 1480],
                "reignNote": "Kazak Hanlığı'nın ortaklaşa kurucusu iki büyük han.",
                "summary": "Cuci Han'ın torunları. Şeybânî Ebulhayr Han'ın despotluğuna başkaldırarak 200 bin göçebeyle birlikte Çu ve Kozybasi vadilerine göçtüler. 'Kazak' (hür ve serbest) kimliğini devletleştirdiler.",
                "traits": ["Özgürlük öncüsü", "Bozkır töresi koruyucusu", "Cesur diplomat"],
                "contribution": "Kazak milletinin ve devletinin temellerini attılar; bozkır boylarını hürriyet sancağı altında topladılar.",
                "harm": "Bozkır boylarının bölünmesine ve Şeybânî Özbekleri ile uzun kanlı mücadelelere yol açtı.",
                "wives": [],
                "children": [
                    {"name": "Burunduk Han", "mother": "", "note": "Kerey Han'ın oğlu, sonraki han", "certainty": "kesin"},
                    {"name": "Kasım Han", "mother": "", "note": "Canıbek Han'ın oğlu, devleti imparatorluk yapan hükümdar", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Çu Vadisi Bağımsızlık Savaşı", "when": "1465-1468", "foe": "Özbek Hanlığı (Ebulhayr Han)", "result": "zafer", "note": "Ebulhayr Han'ın seferi başarısız oldu, Kazak Hanlığı bağımsızlığını pekiştirdi."}
                ],
                "legends": ["Tarihçi Mirza Haydar Duğlat'ın Târîh-i Reşîdî adlı eserinde 'Kazak sultanlarının hükümranlığı 870 (1465-66) yılında başladı' kaydı bağımsızlığın tescili sayılır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KAZAKLAR", "url": "https://islamansiklopedisi.org.tr/kazaklar"}
                ]
            },
            {
                "id": "kazak-kasim",
                "name": "Kasım Han",
                "aliases": ["Qasym Khan"],
                "title": "Han / Kanun Koyucu",
                "birth": 1445,
                "birthNote": "Sıgnak bozkırında doğdu",
                "death": 1521,
                "deathNote": "Başkent Saraycık'ta vefat etti ve orada defnedildi",
                "reign": [1511, 1521],
                "reignNote": "Kazak Hanlığı'nı Avrasya'nın en güçlü bozkır devletine dönüştürdü.",
                "summary": "Canıbek Han'ın oğlu. Hanlığın sınırlarını Hazar Denizi'nden Balkaş Gölü'ne, İdil nehrinden Seyhun'a kadar genişletti. Ordusunu 300 bin ata çıkardı, nüfus 1 milyonu aştı. 'Kasım Han'ın Kaşka Yolu' kanunnamesini hazırladı.",
                "traits": ["Büyük kanun koyucu", "Usta kumandan", "Merhametli ve kudretli"],
                "contribution": "İlk yazılı Kazak kanunnamesini (Töre) yürürlüğe koydu; devleti uluslararası alanda Moskova ve Safevîler nezdinde tanıttı.",
                "harm": "Ölümünün ardından oğulları ve boy beyleri arasında geçici otorite boşluğu yaşandı.",
                "wives": [],
                "children": [
                    {"name": "Mamak Han", "mother": "", "note": "Kısa süre hanlık yaptı", "certainty": "kesin"},
                    {"name": "Haknazar Han", "mother": "", "note": "Devleti tekrar toparlayan büyük han", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Sayram ve Taşkent Seferleri", "when": "1512-1513", "foe": "Şeybânîler Devleti (Muhammed Şeybânî mirasçıları)", "result": "zafer", "note": "Seyhun boyundaki stratejik kaleler ve ticaret şehirleri Kazak hakimiyetine girdi."}
                ],
                "legends": ["Bâbür Şah'ın hatıratında 'Kasım Han gibi kudretli bir hükümdar Cuci ulusunda Batu Han'dan sonra görülmedi' diye övdüğü nakledilir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KASIM HAN", "url": "https://islamansiklopedisi.org.tr/kasim-han--kazak"}
                ]
            },
            {
                "id": "kazak-abilay",
                "name": "Abılay Han",
                "aliases": ["Abilmansur", "Ablai Khan"],
                "title": "Büyük Han / Bozkır Kaplanı",
                "birth": 1711,
                "birthNote": "Türkistan bozkırında doğdu",
                "death": 1781,
                "deathNote": "Arıs Irmağı boyunda Taşkent yakınlarında vefat etti; Yesi'de Hoca Ahmed Yesevî Türbesi'ne defnedildi",
                "reign": [1771, 1781],
                "reignNote": "Üç Kazak Cüzü'nün müşterek ulu hanı.",
                "summary": "18. yüzyılda Üç Cüz'ü birleştiren dahi lider. Gençliğinde 'Sabaalak' adıyla çobanlık yaptı, Cungar istilasına karşı teke tek dövüşte Cungar noyonu Şarış'ı öldürerek kahramanlaştı. Kalmukları mağlup ederek toprakları geri aldı. Rus Çarlığı ve Çin Mançu İmparatorluğu arasında usta bir denge politikası güttü.",
                "traits": ["Manevi önder", "Askeri deha", "Denge ustası diplomat", "Halk aşığı"],
                "contribution": "Cungar soykırım ve istila tehdidini bertaraf etti; Kazak toprak bütünlüğünü sağladı; Ahmed Yesevî türbesini ihya etti.",
                "harm": "Rusya ile yapılan taktiksel anlaşmalar ileride Çarlık ordularının bozkırda kale hatları kurmasını engelleyemedi.",
                "wives": [
                    {"name": "Babak Hanım", "note": "Baş eşi", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "Vali Han", "mother": "", "note": "Orta Cüz Hanı", "certainty": "kesin"},
                    {"name": "Kasım Sultan", "mother": "", "note": "Kenesarı Han'ın babası", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Anırakay Muharebesi", "when": "1729-1730", "foe": "Cungar Hanlığı (Kalmuklar)", "result": "zafer", "note": "Balkaş Gölü güneyinde Cungar ordusu ezildi, 'Aktaban Şubırındı' felaketi son buldu."}
                ],
                "legends": ["Yesi'deki Hoca Ahmed Yesevî türbesinde Üç Cüz'ün aksakalları ve biy'leri tarafından beyaz keçe üzerine oturtulup göğe kaldırılarak 'Ulu Han' ilan edilmiştir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ABILAY HAN", "url": "https://islamansiklopedisi.org.tr/abilay-han"}
                ]
            },
            {
                "id": "kazak-kenesari",
                "name": "Kenesarı Han",
                "aliases": ["Kenesary Kasymov", "Son Han"],
                "title": "Son Bağımsız Kazak Hanı / Şehid",
                "birth": 1802,
                "birthNote": "Kokşetav bozkırında doğdu",
                "death": 1847,
                "deathNote": "Kırgız dağlarında Maitobe mevkiinde pusuya düşürülerek şehit edildi",
                "reign": [1841, 1847],
                "reignNote": "1841'de tüm cüzlerin temsilcileri tarafından han seçildi; 10 yıl Rus işgaline direndi.",
                "summary": "Abılay Han'ın torunu. Rus Çarlığı'nın Kazak bozkırındaki hanlık sistemini kaldırıp sömürge kaleleri kurmasına karşı 1837-1847 yılları arasında 10 yıl süren destansı bir bağımsızlık savaşı yürüttü. Rus tahkimatlarını bastı, Hokand Hanlığı ile savaştı. 1847'de Rus kışkırtmasıyla Kırgız manapları tarafından tuzağa düşürülüp şehit edildi.",
                "traits": ["Yılmayan bağımsızlık savaşçısı", "Sert disiplinli başbuğ", "Halk kahramanı"],
                "contribution": "Kazakların milli bağımsızlık bilincini ebedileştirdi; Rus istilasına karşı tek vücut direniş sembolü oldu.",
                "harm": "Kırgız kabileleriyle diplomatik uzlaşma sağlayamayarak kardeş kavgasına girdi ve ordusunu kaybetti.",
                "wives": [
                    {"name": "Kunimcan Hatun", "note": "Sadık eşi ve mücadele yoldaşı", "certainty": "kesin"}
                ],
                "children": [
                    {"name": "Sıdık Sultan (Sadyk)", "mother": "Kunimcan Hatun", "note": "Babasının intikamı için Ruslara ve Hokand'a karşı savaşan kahraman", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Akmeşit ve Sozak Kuşatması", "when": "1841", "foe": "Hokand Hanlığı ve Rus İleri Karakolları", "result": "zafer", "note": "Kaleler zaptedildi, güney Kazak boyları kurtarıldı."},
                    {"name": "Maitobe Muharebesi", "when": "1847", "foe": "Çarlık Destekli Kırgız Manap Birlikleri", "result": "yenilgi", "note": "Kenesarı Han kuşatıldı ve 32 yiğidiyle birlikte son nefesine kadar savaşarak şehit düştü."}
                ],
                "legends": ["Kenesarı Han'ın kesik başının Rusya'ya götürülerek Petersburg'da Çara sunulduğu ve Hermitage Müzesi depolarında saklandığı iddiaları Kazakistan'da halen canlı bir milli meseledir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KAZAKLAR", "url": "https://islamansiklopedisi.org.tr/kazaklar"}
                ]
            }
        ]
    },
    {
        "id": "nogay-ordasi",
        "name": "Nogay Ordası",
        "short": "Nogay Ordası (Mangıt Yurdu)",
        "aliases": ["Nogai Horde", "Mangıt Yurdu", "Nogay Hanlığı"],
        "region": "kuzey",
        "start": 1391,
        "end": 1634,
        "startNote": "Emir Edigü Bey'in Altın Orda'dan ayrılarak İdil-Yayık (Volga-Ural) bozkırlarında Mangıt boylarını birleştirmesiyle kuruldu.",
        "endNote": "1634 yılında Doğu'dan gelen Kalmuk Budist istilası ve Rus Çarlığı baskısı sonucu dağıldı.",
        "capital": "Saraycık (Yayık Irmağı üzerinde)",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Edige Destanı, Şecere-i Terâkime ve Rus sefaretnâmeleriyle sabittir.",
        "summary": "Altın Orda'nın parçalanma sürecinde İdil ile Yayık (Ural) ırmakları arasındaki uçsuz bucaksız bozkırlarda Mangıt boy beyleri tarafından kurulan güçlü göçebe Türk devleti. Kurucusu Emir Edigü Bey, Altın Orda tahtına hanlar oturtup indiren efsanevi bir başbuğdur. 1399 Vorskla zaferiyle Doğu Avrupa'nın kaderini değiştirdi. Nogay atlıları Kırım ve Osmanlı seferlerinin en çevik süvari gücünü oluşturdu.",
        "legacy": "Nogay Türkçesi ve zengin Edige Destanı kültürünü Avrasya edebiyatına kazandırdı; hafif süvari savaş taktiğinin zirvesini temsil etti.",
        "essay": [
            "Nogay Ordası, adını Altın Orda'nın kudretli kumandanı Nogay Han'dan alsa da asıl siyasi varlığını Mangıt kabilesi reisi Emir Edigü Bey'in önderliğinde kazandı. Başkent Saraycık, İpek Yolu'nun Hazar kuzeyi güzergâhında gelişmiş bir ticaret merkeziydi.",
            "Edigü Bey, 1399'da Vorskla Irmağı Savaşı'nda Litvanya Büyük Dükü Vytautas ve müttefiki Toktamış'ı hezimete uğratarak Doğu Avrupa'da Haçlı-Litvanya yayılmasını durdurdu; 1408'de Moskova'yı kuşatarak haraca bağladı.",
            "16. yüzyılda Büyük Nogay ve Küçük Nogay olarak ikiye bölündü. Doğudan gelen Kalmuk Moğollarının kanlı saldırıları, kuraklık ve Rus Çarlığı'nın baskıları sonucu 1634'te siyasi birliğini kaybetti; Nogay boylarının bir kısmı Kırım, Kafkasya ve Dobruca'ya göç etti."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, NOGAYLAR", "url": "https://islamansiklopedisi.org.tr/nogaylar"},
            {"title": "TDV İslâm Ansiklopedisi, EDİGÜ", "url": "https://islamansiklopedisi.org.tr/edigu"}
        ],
        "rulers": [
            {
                "id": "nogay-edigu-bey",
                "name": "Emir Edigü Bey",
                "aliases": ["Edige Bey", "İdigü", "Edigu Mangıt"],
                "title": "Uluğ Bey / Başbuğ / Bîklerbîkî",
                "birth": 1352,
                "birthNote": "Deşt-i Kıpçak sahasında Mangıt boy beyi Baltyçak'ın oğlu olarak doğdu",
                "death": 1419,
                "deathNote": "Saraycık yakınlarında Seyhun boyunda Toktamış'ın oğullarıyla girdiği muharebede şehit düştü",
                "reign": [1396, 1419],
                "reignNote": "23 yıl boyunca fiili Altın Orda ve Nogay hükümdarı.",
                "summary": "Nogay Ordası'nın kurucusu ve Avrasya bozkırının efsanevi kahramanı (Edige Destanı). Timur'un desteğiyle yükseldi; Altın Orda'da veziriazam (Bîklerbîkî) sıfatıyla kukla hanlar idare etti. 1399 Vorskla Meydan Muharebesi'nde Litvanya-Polonya ve müttefik ordularını imha etti. Moskova'yı kuşatarak Rusları dize getirdi.",
                "traits": ["Dahi mareşal", "Siyasi satranç ustası", "Bozkır destan kahramanı"],
                "contribution": "Nogay birliğini kurdu; Doğu Avrupa'da Litvanya ve Töton yayılmasını kırarak İslam-Türk varlığını korudu.",
                "harm": "Cengiz soyundan olmadığı için tahta meşru hanlar yerine kuklalar oturtarak hanlık otoritesinin büsbütün aşınmasına yol açtı.",
                "wives": [],
                "children": [
                    {"name": "Nureddin Bey", "mother": "", "note": "Babasından sonra Nogay Ordası'nı yöneten kudretli bey", "certainty": "kesin"},
                    {"name": "Mansur Bey", "mother": "", "note": "Kırım ve bozkır siyasetinde etkili bey", "certainty": "kesin"},
                    {"name": "Gazi Bey", "mother": "", "note": "Nogay mirzası", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Vorskla Irmağı Meydan Muharebesi", "when": "1399", "foe": "Litvanya Büyük Dükalığı ve Polonya (Vytautas & Toktamış)", "result": "zafer", "note": "Doğu Avrupa tarihinin en büyük meydan savaşlarından biri; Haçlı-Litvanya ordusu tamamen imha edildi."},
                    {"name": "Moskova Seferi ve Kuşatması", "when": "1408", "foe": "Moskova Knezliği (I. Vasili)", "result": "zafer", "note": "Moskova surları altına gelindi, 3000 ruble haraç alınarak Rus knezliği itaate bağlandı."}
                ],
                "legends": ["Bütün Türk boylarında (Kazak, Kırgız, Karakalpak, Tatar, Nogay, Başkurt) müştereken anlatılan 'Edige Destanı' onun kahramanlıkları üzerine inşa edilmiştir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, EDİGÜ", "url": "https://islamansiklopedisi.org.tr/edigu"}
                ]
            }
        ]
    },
    {
        "id": "ak-orda",
        "name": "Ak Orda Hanlığı",
        "short": "Ak Orda (Sol Kol)",
        "aliases": ["White Horde", "Gök Orda", "Sol Kol Ulusu", "Sıgnak Hanlığı"],
        "region": "kuzey",
        "start": 1227,
        "end": 1428,
        "startNote": "Cuci'nin büyük oğlu Orda Ecen'e İrtiş, Seyhun ve Balkaş boylarının verilmesiyle Altın Orda'nın doğu kanadı olarak kuruldu.",
        "endNote": "1428'de Şeybânî Ebulhayr Han'ın Özbek Ulusu'nu kurmasıyla tarihe karıştı.",
        "capital": "Sıgnak",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Câmiu't-Tevârîh ve Şibanîler dönemi vakayinâmeleriyle sabittir.",
        "summary": "Cuci'nin en büyük oğlu Orda Ecen sülalesi tarafından İrtiş'ten Seyhun kıyılarına kadar uzanan sahada kurulan hanlık. Altın Orda'nın 'Sol Kolu'nu teşkil etti. Başkenti Sıgnak şehri ilim ve ticaret merkezi oldu. 14. yüzyılda Urus Han devrinde büyük bir askeri güç haline geldi; Kazak ve Özbek hanedanlarının doğrudan kök hücresini oluşturdu.",
        "legacy": "Kazak Hanlığı'nın han sülalesinin doğrudan atasıdır; Sıgnak ve Yesi havzasını Türk-İslam medeniyetiyle yoğurmuştur.",
        "essay": [
            "Ak Orda, Cuci'nin büyük oğlu Orda Ecen'e tahsis edilen doğu bozkırlarında özerk bir ulus olarak gelişti. Batıdaki Batu Han (Altın Orda) ulusuna tabiyet bağı zamanla gevşedi ve Sıgnak merkezli tam bağımsız bir hanlığa dönüştü.",
            "Urus Han (1368-1377), Ak Orda'yı bozkırın en çekinilen devleti yaptı. Saray tahtını ele geçirmeye çalıştı; Toktamış ve hamisi Emir Timur ile amansız savaşlara girdi. Urus Han'ın oğulları ve torunları daha sonra Kazak Hanlığı'nı kuracak olan çekirdek kadroyu oluşturdu."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, ALTIN ORDA", "url": "https://islamansiklopedisi.org.tr/altin-orda"},
            {"title": "TDV İslâm Ansiklopedisi, KAZAKLAR", "url": "https://islamansiklopedisi.org.tr/kazaklar"}
        ],
        "rulers": [
            {
                "id": "ak-orda-urus-han",
                "name": "Urus Han",
                "aliases": ["Oruz Han", "Muhammed Urus"],
                "title": "Han",
                "birth": 1330,
                "birthNote": "Sıgnak yöresinde doğdu",
                "death": 1377,
                "deathNote": "Seyhun boyunda vefat etti",
                "reign": [1368, 1377],
                "reignNote": "Ak Orda'nın en güçlü hükümdarı; Kazak hanlarının doğrudan atası.",
                "summary": "Ak Orda tahtında merkezi otoriteyi kuran, Sıgnak'ta kendi adına para bastıran ve Altın Orda başkenti Saray'ı da ele geçiren kudretli han. Toktamış'ın babasını isyan ettiği için idam ettirdi; Timur'un Toktamış'ı iade etme talebini reddederek Timur ordularına karşı direndi.",
                "traits": ["Tavizsiz hükümdar", "Cengaver", "Otoriter lider"],
                "contribution": "Ak Orda'yı müstakil bir güç yaptı; torunları Kerey ve Canıbek Hanlar Kazak Hanlığı'nı kurdu.",
                "harm": "Timur ile giriştiği savaşlar Ak Orda şehirlerinin tahrip olmasına yol açtı.",
                "wives": [],
                "children": [
                    {"name": "Kutluk Buka", "mother": "", "note": "Timur ile savaşırken şehit oldu", "certainty": "kesin"},
                    {"name": "Toktakıya", "mother": "", "note": "Kısa süre tahta geçti", "certainty": "kesin"},
                    {"name": "Koyurçuk", "mother": "", "note": "Kazak hanlarının dedesi", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Sıgnak Savunması", "when": "1376", "foe": "Timur İmparatorluğu Ordusu", "result": "zafer", "note": "Timur'un gönderdiği ilk ordu püskürtüldü."}
                ],
                "legends": ["Kazak şecerelerinde Kazak hanlarının 'Urus Han nesli' olarak anılması onun bozkırdaki derin meşruiyetinin simgesidir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ALTIN ORDA", "url": "https://islamansiklopedisi.org.tr/altin-orda"}
                ]
            }
        ]
    }
]

# ==========================================
# BLOCK G: KUZEY HANLIKLARI VE DELHİ SULTANLIĞI
# ==========================================
data_g = [
    {
        "id": "kirim-hanligi",
        "name": "Kırım Hanlığı",
        "short": "Kırım Hanlığı (Qırım Yurtı)",
        "aliases": ["Crimean Khanate", "Kırım Yurdu", "Qırım Hanlığı", "Giray Hanedanı"],
        "region": "kuzey",
        "start": 1441,
        "end": 1783,
        "startNote": "1441'de Hacı Giray Han'ın Altın Orda'dan ayrılarak Bahçesaray merkezli bağımsız hanlığını kurmasıyla başladı.",
        "endNote": "1783 yılında Rus Çariçesi II. Katerina tarafından Kırım'ın resmen ilhak edilmesiyle sona erdi.",
        "capital": "Bahçesaray (Çufutkale ve Hansaray)",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Kırım Hanlığı mahkeme sicilleri (şer'iyye sicilleri), Osmanlı mühimme defterleri ve sefaretnâmelerle sabittir.",
        "summary": "Hacı Giray Han tarafından kurulan, yaklaşık 350 yıl boyunca Karadeniz'in kuzeyine, Kırım yarımadasına ve Ukrayna bozkırlarına hükmeden ulu hanlık. 1475'te Fatih Sultan Mehmed devrinde Osmanlı himayesine girdi; Osmanlı ordusunun en seçkin ve korkusuz süvari kanadını teşkil etti. 1502'de Altın Orda'yı yıktı; 1571'de I. Devlet Giray Moskova'yı ateşe verdi. Bahçesaray Hansarayı ve zengin medreseleriyle İslami kültürün kuzeydeki kalesi oldu. 1774 Küçük Kaynarca Antlaşması sonrası 1783'te Çarlık Rusyası tarafından ilhak edildi.",
        "legacy": "Bahçesaray Hansaray'ı, Gözleve Cuma Cami, Zincirli Medrese ve Tarak Tamga sembolüyle Kırım Tatar milli kimliğinin ebedi timsalidir.",
        "essay": [
            "Kırım Hanlığı, Altın Orda'nın çöküş devrinde Cuci soyundan gelen Hacı Giray Han'ın Bahçesaray'da bağımsızlığını ilan etmesiyle tarih sahnesine çıktı. Hacı Giray, sülalenin arması olarak 'Tarak Tamga'yı seçti.",
            "1475 yılında Fatih Sultan Mehmed'in veziri Gedik Ahmed Paşa Kefe'deki Ceneviz kolonilerini fethettiğinde, I. Mengli Giray Osmanlı Devleti'nin yüksek himayesini kabul etti. Bu ittifak Kırım Hanlarına özel bir statü kazandırdı; Giraylar protokolde sadrazam ile denk tutuldu, Osmanlı hanedanının tükenmesi halinde tahta geçecek yegâne soy kabul edildi. 1502'de Mengli Giray Saray şehrini zaptederek Altın Orda Devleti'ne nihai darbeyi indirdi.",
            "1571'de I. Devlet Giray, Korkunç İvan'ın yayılmacılığına son vermek üzere 120 bin süvariyle Moskova'yı kuşatarak yaktı ve 'Taht Algan' (Taht Alan) unvanını kazandı. Ancak 18. yüzyılda Rus Çarlığı'nın Karadeniz'e inme siyaseti neticesinde 1774 Küçük Kaynarca Antlaşması ile hanlık Osmanlı'dan koparıldı; son han Şahin Giray'ın basiretsizliği sonucu 1783'te Rusya tarafından ilhak edildi."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, KIRIM HANLIĞI", "url": "https://islamansiklopedisi.org.tr/kirim-hanligi"},
            {"title": "TDV İslâm Ansiklopedisi, HACI GİRAY I", "url": "https://islamansiklopedisi.org.tr/haci-giray-i"},
            {"title": "TDV İslâm Ansiklopedisi, DEVLET GİRAY I", "url": "https://islamansiklopedisi.org.tr/devlet-giray-i"},
            {"title": "TDV İslâm Ansiklopedisi, MENGLİ GİRAY I", "url": "https://islamansiklopedisi.org.tr/mengli-giray-i"}
        ],
        "rulers": [
            {
                "id": "kirim-haci-giray",
                "name": "I. Hacı Giray Han",
                "aliases": ["Melek Hacı Giray", "Haji Giray"],
                "title": "Han / Kurucu",
                "birth": 1397,
                "birthNote": "Litvanya'da sürgünde (Troki) doğdu",
                "death": 1466,
                "deathNote": "Bahçesaray yakınlarında Çufutkale'de vefat etti",
                "reign": [1441, 1466],
                "reignNote": "Kırım Hanlığı ve Giray Hanedanı'nın kurucusu.",
                "summary": "Kırım Tatarlarının ve Giray Hanedanı'nın atası. Kırım beylerinin ve Şirin kabilesinin davetiyle Kırım'a gelerek Altın Orda valilerini kovdu ve bağımsızlığını ilan etti. Litvanya Büyük Dükalığı ile ittifak kurdu. Bahçesaray ve Salaçık'ta Zincirli Medrese ve türbesini inşa ettirdi.",
                "traits": ["Kurucu lider", "Mutedil ve adil", "Halk tarafından sevilen ('Melek')"],
                "contribution": "350 yıl sürecek bağımsız Kırım Hanlığı'nı kurdu; Tarak Tamga'yı hanedan arması yaptı.",
                "harm": "Vefatından sonra oğulları arasında 10 yıl süren taht kavgası baş gösterdi.",
                "wives": [
                    {"name": "Asiye Hatun", "note": "Baş hatun", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "Nur Devlet", "mother": "", "note": "Kısa süre hanlık yaptı", "certainty": "kesin"},
                    {"name": "Haydar Han", "mother": "", "note": "Han", "certainty": "kesin"},
                    {"name": "I. Mengli Giray", "mother": "", "note": "Devleti kurumsallaştıran kudretli hükümdar", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Altın Orda Kuşatması Püskürtmesi", "when": "1455", "foe": "Altın Orda Hanlığı (Seyyid Ahmed Han)", "result": "zafer", "note": "Kırım'ı istilaya gelen Seyyid Ahmed Han mağlup edilerek esir alındı."}
                ],
                "legends": ["Adaleti ve dindarlığı sebebiyle Kırım halkı tarafından kendisine 'Melek' lakabının verildiği kaydedilir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, HACI GİRAY I", "url": "https://islamansiklopedisi.org.tr/haci-giray-i"}
                ]
            },
            {
                "id": "kirim-mengli-giray",
                "name": "I. Mengli Giray Han",
                "aliases": ["Mengli I Giray"],
                "title": "Uluğ Han / Padişah",
                "birth": 1445,
                "birthNote": "Kırım'da doğdu",
                "death": 1515,
                "deathNote": "Bahçesaray'da vefat etti, Salaçık Türbesi'ndedir",
                "reign": [1467, 1515],
                "reignNote": "Fatih Sultan Mehmed ile ittifak kuran ve Altın Orda'yı yıkan büyük hükümdar.",
                "summary": "Hacı Giray'ın oğlu. 1475'te Gedik Ahmed Paşa'nın Kefe fethinden sonra Fatih Sultan Mehmed ile ebedi ittifak kurarak Osmanlı himayesini kabul etti. 1502'de Saray şehrini yerle bir ederek 300 yıllık Altın Orda Hanlığı'na son verdi. Kızı Ayşe Hafsa Sultan'ı Şehzade Selim (Yavuz Sultan Selim) ile evlendirdi; Kanunî Sultan Süleyman'ın dedesidir.",
                "traits": ["Büyük siyasetçi", "Stratejist", "İmar hamisi", "Sadık müttefik"],
                "contribution": "Kırım Hanlığı'nı kurumsallaştırdı; Zincirli Medrese'yi tamamladı; Altın Orda'ya son vererek Kırım'ı kuzeyin tek meşru gücü yaptı.",
                "harm": "Altın Orda'nın yıkılması ilerleyen asırlarda Rus knezliklerinin doğuya doğru yayılmasının önündeki en büyük engeli kaldırmış oldu.",
                "wives": [
                    {"name": "Nursultan Hatun", "note": "Kazan Hanı Halil ve İbrâhim'in eski eşi, diplomatik evlilik", "certainty": "kesin"}
                ],
                "children": [
                    {"name": "I. Mehmed Giray", "mother": "", "note": "Babasından sonra tahta geçen fatih han", "certainty": "kesin"},
                    {"name": "I. Saadet Giray", "mother": "", "note": "Han", "certainty": "kesin"},
                    {"name": "I. Sahib Giray", "mother": "", "note": "Kazan ve Kırım Hanı", "certainty": "kesin"},
                    {"name": "Ayşe Hafsa Sultan", "mother": "", "note": "Yavuz Sultan Selim'in eşi, Kanunî Sultan Süleyman'ın annesi (Valide Sultan)", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Saray Kuşatması ve Fethi", "when": "1502", "foe": "Altın Orda Devleti (Şeyh Ahmed Han)", "result": "zafer", "note": "Başkent Saray yerle bir edildi, Altın Orda Devleti tarihe karıştı."}
                ],
                "legends": ["Kızı Ayşe Hafsa Sultan'ın Manisa'da şifa kaynağı Mesir Macunu geleneğini başlatan muhterem valide sultan olması aile bağlarının canlı timsalidir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, MENGLİ GİRAY I", "url": "https://islamansiklopedisi.org.tr/mengli-giray-i"}
                ]
            },
            {
                "id": "kirim-devlet-giray",
                "name": "I. Devlet Giray Han",
                "aliases": ["Taht Algan Devlet Giray", "Devlet I Giray"],
                "title": "Han / Gazi / Taht Algan",
                "birth": 1512,
                "birthNote": "Bahçesaray'da doğdu",
                "death": 1577,
                "deathNote": "Bahçesaray'da veba sebebiyle vefat etti",
                "reign": [1551, 1577],
                "reignNote": "26 yıl saltanat sürdü; Moskova'yı yakan ünlü gazi han.",
                "summary": "Kırım Hanlığı'nın en muzaffer hükümdarı. Kanunî Sultan Süleyman devrinde Kırım tahtına oturdu. Çar Korkunç İvan'ın Kazan ve Astrahan'ı işgal etmesine karşı 1571'de 120 bin süvariyle Moskova Seferi'ne çıktı; şehri ve Kremlin varoşlarını ateşe vererek Çarı kaçmaya mecbur etti. 'Taht Algan' (Moskova Tahtını Alan) unvanını aldı.",
                "traits": ["Yenilmez akıncı", "Sert mareşal", "Gözü pek gazî", "Osmanlı'nın en sadık müttefiki"],
                "contribution": "Korkunç İvan'ın güneye ve Kırım'a sarkmasını 20 yıl geciktirdi; Kırım süvarisinin yenilmezliğini dünyaya kanıtladı.",
                "harm": "1572 Molodi Muharebesi'nde aşırı özgüven sonucu pusuya düşerek ağır süvari zayiatı verdi.",
                "wives": [
                    {"name": "Ayşe Fâtıma Hatun", "note": "Baş hatun", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "II. Mehmed Giray (Semiz)", "mother": "", "note": "Han", "certainty": "kesin"},
                    {"name": "II. İslâm Giray", "mother": "", "note": "Han", "certainty": "kesin"},
                    {"name": "II. Gazi Giray (Bora)", "mother": "", "note": "Meşhur şair ve bestekâr kahraman han", "certainty": "kesin"},
                    {"name": "I. Fetih Giray", "mother": "", "note": "Haçova fatihi han", "certainty": "kesin"},
                    {"name": "I. Selâmet Giray", "mother": "", "note": "Han", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Moskova Seferi ve Yangını", "when": "1571", "foe": "Rus Çarlığı (Korkunç İvan)", "result": "zafer", "note": "Moskova surlarına girildi, şehir tamamen yakıldı; Çar İvan şehirden kaçtı."},
                    {"name": "Molodi Muharebesi", "when": "1572", "foe": "Rus Çarlığı (Prens Mihail Vorotınski)", "result": "yenilgi", "note": "Gulyay-gorod tahkimatına çarpan Kırım ordusu geri çekildi."}
                ],
                "legends": ["Korkunç İvan'a gönderdiği mektupta 'Moskova'yı yaktım, tacını ve tahtını çiğnedim; gururundan vazgeçip Kazan ve Astrahan'ı geri ver' diye meydan okuduğu meşhurdur."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, DEVLET GİRAY I", "url": "https://islamansiklopedisi.org.tr/devlet-giray-i"}
                ]
            },
            {
                "id": "kirim-sahin-giray",
                "name": "Şahin Giray Han",
                "aliases": ["Shahin Giray", "Son Kırım Hanı"],
                "title": "Son Han",
                "birth": 1745,
                "birthNote": "Edirne'de sürgünde doğdu",
                "death": 1787,
                "deathNote": "Osmanlı'ya sığındıktan sonra Rodos'ta idam edildi",
                "reign": [1777, 1783],
                "reignNote": "Kırım Hanlığı'nın son hükümdarı.",
                "summary": "Kırım'ın son hanı. Petersburg ve Avrupa'da eğitim gördü. Rus Çariçesi II. Katerina'nın desteğiyle tahta çıktı. Kırım'da orduyu ve idareyi Batı tarzında modernize etmeye çalıştı; ancak halk bu reformları ve Rus kuklalığını reddederek isyan etti. 1783'te Katerina'nın Kırım'ı ilhak fermanına boyun eğdi. Pişman olarak Osmanlı'ya sığındıysa da vatanı Ruslara teslim ettiği gerekçesiyle Rodos'ta idam edildi.",
                "traits": ["Batı hayranı", "Halkından kopuk", "Trajik reformcu", "Basiretsiz siyasetçi"],
                "contribution": "Bahçesaray'da modern matbaa ve darphane kurmaya çalıştı.",
                "harm": "Rus politikalarına alet olarak 350 yıllık bağımsız Kırım Hanlığı'nın haritadan silinmesine ve Kırım Tatarlarının yüzyıllar sürecek sürgün ve trajedilerine sebep oldu.",
                "wives": [],
                "children": [],
                "wars": [
                    {"name": "Kırım Halk İsyanı Bastırması", "when": "1781-1782", "foe": "Kırım Tatar Halkı ve Ulema", "result": "yenilgi", "note": "Halk isyan etti, Şahin Giray Rus süngüleriyle tahtta kalabildi."}
                ],
                "legends": ["Tahttan feragat ettikten sonra Rusya'da ev hapsine alındığında Çariçe Katerina'nın kendisine verdiği sözleri tutmadığını anlayıp Osmanlı'ya kaçtığı bilinir."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ŞÂHİN GİRAY", "url": "https://islamansiklopedisi.org.tr/sahin-giray"}
                ]
            }
        ]
    },
    {
        "id": "kazan-hanligi",
        "name": "Kazan Hanlığı",
        "short": "Kazan Hanlığı (Qazan Yurtı)",
        "aliases": ["Kazan Khanate", "Qazan Hanlığı", "Kazan Krallığı"],
        "region": "kuzey",
        "start": 1438,
        "end": 1552,
        "startNote": "Altın Orda hanlarından Uluğ Muhammed Han'ın İdil (Volga) kıyısında Kazan merkezli kurmasıyla başladı.",
        "endNote": "1552 yılında Korkunç İvan komutasındaki 150 bin kişilik Rus ordusunun Kazan Kalesi'ni zaptetmesiyle yıkıldı.",
        "capital": "Kazan",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Kazan Kroniği (Kazanskaya Istoriya), Rus vakayinâmeleri ve kitabelerle sabittir.",
        "summary": "İdil Bulgar mirası üzerine Altın Orda hanı Uluğ Muhammed Han tarafından kurulan zengin ve medeni Türk-Tatar devleti. Volga nehir ticaretini elinde tuttu. 1445 Suzdal zaferiyle Moskova Büyük Knezini esir aldı. Sarayları, camileri (Kul Şerif Camii) ve zengin kütüphaneleriyle tanındı. 1552'de Korkunç İvan'ın aylar süren kanlı kuşatması sonrası düşerek Rus Çarlığı tarafından ilhak edildi.",
        "legacy": "Kazan Tatarlarının yüksek şehir kültürünü, Kul Şerif destanını ve Süyümbike Minaresi efsanesini tarihe emanet etti.",
        "essay": [
            "Kazan Hanlığı, eski İdil Bulgar Devleti'nin verimli topraklarında ve Altın Orda'nın çöküş boşluğunda Uluğ Muhammed Han tarafından 1438'de kuruldu.",
            "Uluğ Muhammed Han, 1445'te Suzdal Meydan Muharebesi'nde Moskova Büyük Knezi II. Vasili'yi ordusuyla birlikte esir alarak Rusları ağır haraca bağladı ve Kasım Hanlığı'nın kurulmasına zemin hazırladı.",
            "Hanlık içindeki Rus yanlısı ve Kırım-Osmanlı yanlısı hizipler devleti zayıflattı. Safa Giray Han devrinde bağımsızlık korunduysa da onun ölümünden sonra tahta çıkan küçük yaştaki oğlu adına devleti yöneten kahraman naibe Süyümbike Hatun, Moskova entrikalarına direndi. 1552 sonbaharında Korkunç İvan 150 bin asker ve yüzlerce topla Kazan'ı kuşattı; Seyyid Kul Şerif ve talebeleri cami önünde son nefeslerine kadar dövüşerek şehit düştü ve hanlık yıkıldı."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, KAZAN HANLIĞI", "url": "https://islamansiklopedisi.org.tr/kazan-hanligi"},
            {"title": "TDV İslâm Ansiklopedisi, ULUĞ MUHAMMED HAN", "url": "https://islamansiklopedisi.org.tr/ulug-muhammed-han"},
            {"title": "TDV İslâm Ansiklopedisi, SÜYÜMBİKE", "url": "https://islamansiklopedisi.org.tr/suyumbike"}
        ],
        "rulers": [
            {
                "id": "kazan-ulug-muhammed",
                "name": "Uluğ Muhammed Han",
                "aliases": ["Oluğ Muhammed", "Ulan Han"],
                "title": "Han / Kurucu",
                "birth": 1405,
                "birthNote": "Deşt-i Kıpçak sahasında doğdu",
                "death": 1445,
                "deathNote": "Kazan'da vefat etti",
                "reign": [1438, 1445],
                "reignNote": "Kazan Hanlığı ve Kasım Hanlığı'nın kurucu atası.",
                "summary": "Altın Orda tahtından ayrıldıktan sonra İdil boyuna gelerek Kazan Hanlığı'nı kuran tecrübeli hükümdar. 1445 Suzdal Muharebesi'nde Moskova ordusunu bozguna uğratıp Rus Büyük Knezi II. Vasili'yi esir aldı; Rusları ağır tazminata bağladı.",
                "traits": ["Dirayetli lider", "Usta komutan", "Teşkilatçı"],
                "contribution": "Kazan Hanlığı'nı kurdu; Rus knezliklerine karşı Tatar askeri üstünlüğünü sürdürdü.",
                "harm": "Vefatından sonra oğlu Mahmud ile kardeşi Kasım arasında başlayan çekişme hanlığın bölünmesine yol açtı.",
                "wives": [],
                "children": [
                    {"name": "Mahmud Han", "mother": "", "note": "Kazan tahtına geçen oğlu", "certainty": "kesin"},
                    {"name": "Kasım Han", "mother": "", "note": "Kasım Hanlığı'nı kuran oğlu", "certainty": "kesin"},
                    {"name": "Yakup Bey", "mother": "", "note": "Kazan prensi", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Belyov Muharebesi", "when": "1437", "foe": "Moskova Knezliği (II. Vasili)", "result": "zafer", "note": "40 bin kişilik Rus ordusu 3 bin kişilik Tatar süvarisi tarafından darmadağın edildi."},
                    {"name": "Suzdal Meydan Muharebesi", "when": "1445", "foe": "Moskova Büyük Knezliği (II. Vasili)", "result": "zafer", "note": "Büyük Knez esir alındı, ağır fidye ve vergi anlaşması imzalandı."}
                ],
                "legends": ["Rus Büyük Knezini bizzat çadırında esir tutup ayağına diz çöktürmesi Rus vakayinâmelerinde asırlarca utançla anılmıştır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ULUĞ MUHAMMED HAN", "url": "https://islamansiklopedisi.org.tr/ulug-muhammed-han"}
                ]
            },
            {
                "id": "kazan-suyumbike",
                "name": "Süyümbike Hatun",
                "aliases": ["Soyembika", "Melike Süyümbike"],
                "title": "Naibe Hanım / Han Bike",
                "birth": 1516,
                "birthNote": "Nogay Ordası'nda başkent Saraycık'ta doğdu",
                "death": 1554,
                "deathNote": "Kasimov'da sürgünde vefat etti",
                "reign": [1549, 1551],
                "reignNote": "Kazan Hanlığı'nın efsanevi kadın naibesi ve hükümdarı.",
                "summary": "Nogay Beyi Yusuf'un kızı, Kazan Hanı Safa Giray'ın eşi. Eşinin vefatından sonra 2 yaşındaki oğlu Ötemiş Giray adına taht naibesi olarak devleti yönetti. Moskova'nın tehditlerine karşı Kazan Kalesi'ni savundu. Rus işbirlikçisi hain beyler tarafından hileyle esir alınıp Ruslara teslim edildi. Moskova'da vaftiz edilmeye zorlandı, zorla Şah Ali ile evlendirildi. Tatar bağımsızlık mücadelesinin en kutsal sembolüdür.",
                "traits": ["Milli kahraman", "Fedakar anne", "Bağımsızlık sembolü", "Asil melike"],
                "contribution": "Kazan halkının bağımsızlık ruhunu diri tuttu; adaletli ve dirayetli bir naibelik yürüttü.",
                "harm": "İçteki Rus taraftarı aristokratların entrikalarını ve hanlığın teslim edilmesini engelleyemedi.",
                "wives": [],
                "children": [
                    {"name": "Ötemiş Giray", "mother": "", "note": "Kazan'ın küçük hanı, annesiyle birlikte Moskova'ya esir götürüldü", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Kazan Kalesi Savunması", "when": "1550", "foe": "Moskova Çarlığı (Korkunç İvan)", "result": "zafer", "note": "Korkunç İvan'ın şehri kuşatan ordusu ağır kış şartları ve Tatar taarruzuyla püskürtüldü."}
                ],
                "legends": ["Kazan Kremlin'indeki meşhur 'Süyümbike Minaresi' efsanesine göre, Korkunç İvan onunla evlenmek istemiş, o da 7 günde 7 katlı minare yapılması şartını koşmuş, minare bitince kendisini minarenin tepesinden atarak can vermiştir (tarihte ise esir edilip sürülmüştür)."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, SÜYÜMBİKE", "url": "https://islamansiklopedisi.org.tr/suyumbike"}
                ]
            }
        ]
    },
    {
        "id": "astrahan-hanligi",
        "name": "Astrahan Hanlığı",
        "short": "Astrahan (Hacı Tarhan)",
        "aliases": ["Astrakhan Khanate", "Hacı Tarhan Hanlığı", "Ejderhan Hanlığı"],
        "region": "kuzey",
        "start": 1465,
        "end": 1556,
        "startNote": "Altın Orda'nın dağılmasıyla Mahmud Han tarafından İdil deltasındaki Hacı Tarhan merkezli kuruldu.",
        "endNote": "1556 yılında Korkunç İvan komutasındaki Rus donanması ve ordusu tarafından zaptedilerek ilhak edildi.",
        "capital": "Hacı Tarhan (Astrahan)",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Osmanlı Don-Volga kanalı layiha vesikaları ve Rus arşivleriyle sabittir.",
        "summary": "İdil Irmağı'nın Hazar Denizi'ne döküldüğü stratejik delta üzerinde kurulan ticaret hanlığı. Hazar deniz ticareti, ipek, tuz ve kürk yollarını denetledi. 1556'da Korkunç İvan tarafından ilhak edilerek Rusların Hazar Denizi'ne inmesine yol açtı. 1569'da Osmanlı Sadrazamı Sokullu Mehmed Paşa burayı geri almak ve Rus yayılmasını kesmek için Don-Volga Kanalı Seferi'ni başlattı.",
        "legacy": "Don-Volga Kanal projesine ilham kaynağı oldu; Hazar-İdil ticaret havzasını asırlarca canlandırdı.",
        "essay": [
            "Astrahan Hanlığı, Altın Orda Hanı Küçük Muhammed'in oğlu Mahmud Han tarafından İdil deltasındaki Hacı Tarhan şehrinde kuruldu. Coğrafi konumu sebebiyle Asya, Rusya, Kafkasya ve İran ticaretinin kilit düğüm noktasıydı.",
            "Hanlık, Kırım Hanlığı ve Nogay Ordası'nın sürekli siyasi çekişmelerine sahne oldu. 1556'da Korkunç İvan'ın nehir donanması şehri işgal etti. Osmanlı Devleti 1569'da Kırım Hanı Devlet Giray ve Kasım Paşa komutasında Don-Volga Kanalı Projesi ile Astrahan'ı geri almayı hedeflediyse de kış şartları ve Kırım Hanı'nın isteksizliği sebebiyle sefer tamamlanamadı."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, ASTRAHAN HANLIĞI", "url": "https://islamansiklopedisi.org.tr/astrahan-hanligi"}
        ],
        "rulers": [
            {
                "id": "astrahan-mahmud-han",
                "name": "Mahmud Han",
                "aliases": ["Mahmud bin Küçük"],
                "title": "Han / Kurucu",
                "birth": 1430,
                "birthNote": "Saray şehrinde doğdu",
                "death": 1476,
                "deathNote": "Hacı Tarhan'da vefat etti",
                "reign": [1465, 1476],
                "reignNote": "Astrahan Hanlığı'nın kurucusu.",
                "summary": "Altın Orda Hanı Küçük Muhammed'in oğlu. Kardeşi Ahmed Han ile anlaşamayarak Hacı Tarhan'a çekildi ve bağımsız Astrahan Hanlığı'nı kurdu. Hazar ticaretini organize etti.",
                "traits": ["Ticaret ehli", "Diplomat", "Mutedil lider"],
                "contribution": "Hacı Tarhan'ı Doğu ile Batı arasında uluslararası ticaret limanına dönüştürdü.",
                "harm": "Askeri kuvvetini zayıf tutarak hanlığı komşu güçlerin nüfuz mücadelesine açık bıraktı.",
                "wives": [],
                "children": [
                    {"name": "Kasım Han", "mother": "", "note": "Babasından sonra tahta geçen han", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Hacı Tarhan Savunması", "when": "1468", "foe": "Altın Orda Ordusu (Ahmed Han)", "result": "zafer", "note": "Kardeşinin şehri alma girişimi püskürtüldü."}
                ],
                "legends": ["Hacı Tarhan şehrinin adının buraya yerleşip vergiden muaf tutulan kutlu bir derviş olan 'Hacı Tarhan'dan geldiği anlatılır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ASTRAHAN HANLIĞI", "url": "https://islamansiklopedisi.org.tr/astrahan-hanligi"}
                ]
            }
        ]
    },
    {
        "id": "sibir-hanligi",
        "name": "Sibir Hanlığı",
        "short": "Sibir Hanlığı (Tümen Yurdu)",
        "aliases": ["Sibir Khanate", "Tümen Hanlığı", "İsker Hanlığı", "Sibir Yurtı"],
        "region": "kuzey",
        "start": 1468,
        "end": 1598,
        "startNote": "Batı Sibirya'da İrtiş ve Tobol nehirleri havzasında İbak Han ve Taibuga sülalesi tarafından kuruldu.",
        "endNote": "1598 Irmak Muharebesi sonrası son han Küçüm Han'ın çekilmesi ve Rus Çarlığı ilhakıyla sona erdi.",
        "capital": "Çingi-Tura (Tümen) ve İsker (Kaşlık)",
        "religion": "İslamiyet (Sünnî-Hanefî) ve Şamanizm",
        "confidence": "kayit",
        "confidenceNote": "Stroganov ve Remezov Sibirya kronikleri ve Buhara elçilik kayıtlarıyla sabittir.",
        "summary": "Tarihte 'Sibirya' coğrafyasına adını veren tek Müslüman-Türk devleti. Batı Sibirya düzlüklerinde, İrtiş ve Tobol ırmakları boyunda hüküm sürdü. Küçüm Han devrinde Buhara'dan din âlimleri ve şeyhler getirtilerek bölge halkları (Tatarlar, Hantılar, Mansiler) arasında İslamiyet hızla yayıldı. 1581'de Rus Kazak atamanı Yermak'ın istilasına karşı Küçüm Han 17 yıl boyunca amansız bir gerilla ve meydan savaşı verdi; Yermak'ı İrtiş Nehri'nde boğdurarak intikam aldı. 1598'de yıkıldı.",
        "legacy": "Uçsuz bucaksız Sibirya kıtasına adını mühürledi; kutup dairesine yakın topraklarda İslam medeniyetinin meşalesini yaktı.",
        "essay": [
            "Sibir Hanlığı, Altın Orda'nın dağılmasıyla Batı Sibirya'nın orman ve tayga kuşağında kuruldu. Hanlık başkenti önce Çingi-Tura (bugünkü Tümen), ardından İrtiş kıyısındaki korunaklı İsker (Kaşlık / Sibir) şehri oldu.",
            "Hanlığın en büyük hükümdarı Şeybânî soyundan gelen Küçüm Han (1563-1598) oldu. Küçüm Han, tebaası arasında İslamiyeti samimiyetle yaydı. Ancak Çar Korkunç İvan'ın fermanı ve zengin Stroganov tüccarlarının finansmanıyla donatılan Kazak Atamanı Yermak Timofeyeviç, 1581'de ateşli silahlarla Sibirya'yı istila etti.",
            "Küçüm Han, başkenti İsker'i kaybetmesine rağmen teslim olmadı; taygalarda 17 yıl süren destansı bir direniş örgütledi. 1585'te gece baskınıyla Yermak'ın birliğini kılıçtan geçirdi; zırhıyla İrtiş'e atlayan Yermak boğuldu. Ancak Rus takviye orduları karşısında 1598'de son savaşını kaybeden ihtiyar Küçüm Han bozkıra çekildi ve hanlık çöktü."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, SİBİR HANLIĞI", "url": "https://islamansiklopedisi.org.tr/sibir-hanligi"},
            {"title": "TDV İslâm Ansiklopedisi, KÜÇÜM HAN", "url": "https://islamansiklopedisi.org.tr/kucum-han"}
        ],
        "rulers": [
            {
                "id": "sibir-kucum-han",
                "name": "Küçüm Han",
                "aliases": ["Kuchum Khan", "Kocum Han"],
                "title": "Han / Gazi / Sibirya Mücahidi",
                "birth": 1515,
                "birthNote": "Aral bozkırında doğdu",
                "death": 1605,
                "deathNote": "Buhara bozkırında Nogaylar arasında vefat etti",
                "reign": [1563, 1598],
                "reignNote": "35 yıl saltanat sürdü; Yermak'a karşı Sibirya'yı savunan efsanevi han.",
                "summary": "Sibir Hanlığı'nın en şanlı hükümdarı. Buhara Emiri Abdullah Han'ın desteğiyle tahta çıktı; Sibirya'da camiler ve medreseler açtı. Rus Çarlığı'nın paralı atamanı Yermak'ın ateşli silahlı Kazak ordusuna karşı 17 yıl savaştı. 1585'te Vagay Nehri baskınında Yermak'ı nehirde boğdurdu. Gözleri kör olana ve son askeri şehit düşene kadar Çarlığa boyun eğmedi.",
                "traits": ["Yılmayan mücahid", "Dindar hami", "Cesur başbuğ", "Vatanperver"],
                "contribution": "Sibirya'da İslamiyet'in kök salmasını sağladı; Rus istilasına karşı eşsiz bir direniş destanı bıraktı.",
                "harm": "Ateşli silahlara karşı ordusunun geleneksel ok ve kılıç taktiğinde geç kalması mağlubiyeti kaçınılmaz kıldı.",
                "wives": [
                    {"name": "Süzenge Hatun", "note": "İsker savunmasında kahramanca direnen ve esir düşmemek için canına kıyan baş hatun", "certainty": "kesin"}
                ],
                "children": [
                    {"name": "Ali Han", "mother": "", "note": "Babasından sonra direnişi sürdüren oğlu", "certainty": "kesin"},
                    {"name": "Kanay Han", "mother": "", "note": "Sibirya şehzadesi", "certainty": "kesin"},
                    {"name": "İşim Sultan", "mother": "", "note": "Şehzade", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Çuvaş Burnu Muharebesi", "when": "1582", "foe": "Rus Çarlığı Kazakları (Ataman Yermak)", "result": "yenilgi", "note": "Ateşli tüfeklerin gürültüsü ve etkisi karşısında İsker tahliye edildi."},
                    {"name": "Vagay Irmağı Gece Baskını", "when": "1585", "foe": "Rus Çarlığı Kazak Birliği (Ataman Yermak)", "result": "zafer", "note": "Yermak'ın kampı gece basıldı; Çarın hediye ettiği çifte ağır zırhı taşıyan Yermak nehre atlayıp boğuldu."},
                    {"name": "Irmak Muharebesi", "when": "1598", "foe": "Rus Çarlığı Ordusu (Voyvoda Voyeykov)", "result": "yenilgi", "note": "Küçüm Han'ın son ordusu dağıldı, ailesi esir alındı, kendisi bozkıra çekildi."}
                ],
                "legends": ["Çar Boris Godunov'un kendisine teslim olması halinde sarayında hürmet göreceği teklifini 'Ben hür doğdum, bir kula kul olarak ölemem; gözlerim görmez oldu ama kalbim hürdür' diyerek reddetmesi destanlaşmıştır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KÜÇÜM HAN", "url": "https://islamansiklopedisi.org.tr/kucum-han"}
                ]
            }
        ]
    },
    {
        "id": "kasim-hanligi",
        "name": "Kasım Hanlığı",
        "short": "Kasım Hanlığı (Mişer Yurdu)",
        "aliases": ["Kasimov Khanate", "Mişer Yurdu", "Gorodets Hanlığı"],
        "region": "kuzey",
        "start": 1452,
        "end": 1681,
        "startNote": "Kazan Hanı Uluğ Muhammed'in oğlu Kasım Han'a Oka Nehri boyundaki Gorodets kentinin yurtluk verilmesiyle kuruldu.",
        "endNote": "1681 yılında son naibe Fâtıma Sultan Bikem'in vefatıyla özerklik tamamen kaldırılarak Rusya'ya bağlandı.",
        "capital": "Kasimov (Gorodets Meşçerskiy)",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Velyaminov-Zernov'un dört ciltlik Kasimov Hanlığı tetkikatı ve Rus elçilik defterleriyle sabittir.",
        "summary": "Moskova Knezliği sınırları içinde, Oka Irmağı üzerinde 230 yıl boyunca varlığını sürdüren özerk Müslüman-Türk hanlığı. Kurucusu Kasım Han'ın adıyla anılan başkent Kasimov'da camiler ve han türbeleri inşa edildi. Rusya'nın Kazan, Astrahan, Kırım ve Livonya ile diplomatik ve askeri ilişkilerinde kilit köprü rolü oynadı. 1681'de Rusya tarafından ilhak edildi.",
        "legacy": "Moskova'nın göbeğinde iki asır boyunca İslam sancağını dalgalandırdı; Kasimov Han Camii minaresi günümüze kadar ayakta kaldı.",
        "essay": [
            "Kasım Hanlığı, 1445 Suzdal zaferinden sonra Uluğ Muhammed Han'ın oğlu Kasım Han'ın Moskova Büyük Knezi II. Vasili ile yaptığı anlaşma neticesinde Oka boyunda bir tampon Türk beyliği olarak 1452'de kuruldu.",
            "Hanlığın ahalisini Mişer Tatarları oluşturuyordu. Kasım Hanları Rusya'nın dış ilişkilerinde ordu komutanı, elçi ve arabulucu olarak en yüksek mertebede görev yaptılar. Şah Ali Han ve Seyyid Burhan gibi hanlar döneminde hanlık Rusya içi siyasetin odak noktası oldu. 1681'de son naibe Fâtıma Sultan Bikem'in vefatıyla lağvedildi."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, KASIM HANLIĞI", "url": "https://islamansiklopedisi.org.tr/kasim-hanligi"}
        ],
        "rulers": [
            {
                "id": "kasim-kasim-han",
                "name": "Kasım Han",
                "aliases": ["Qasim Khan"],
                "title": "Han / Kurucu",
                "birth": 1425,
                "birthNote": "Altın Orda bozkırında doğdu",
                "death": 1469,
                "deathNote": "Kasimov'da vefat etti",
                "reign": [1452, 1469],
                "reignNote": "Kasım Hanlığı'nın kurucusu ve isim babası.",
                "summary": "Uluğ Muhammed Han'ın oğlu. 1445'te Suzdal zaferinden sonra Moskova knezine yardım etti; Oka Irmağı boyundaki Gorodets şehri kendisine bağışlandı. Burada bağımsız bir Müslüman idare kurdu; şehir 'Kasimov' adını aldı.",
                "traits": ["Diplomat", "Usta kumandan", "Mutedil siyasetçi"],
                "contribution": "Rus topraklarında 230 yıl sürecek Müslüman Türk yurdunu ve hanlığını kurdu.",
                "harm": "Moskova ile kurduğu bağımlılık ilişkisi hanlığın tam bağımsız bir devlet olmasını engelledi.",
                "wives": [],
                "children": [
                    {"name": "Danyal Han", "mother": "", "note": "Babasından sonra han olan oğlu", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Moskova Taht Kavgası Müdahalesi", "when": "1449-1450", "foe": "Dmitriy Şemyaka Birlikleri", "result": "zafer", "note": "II. Vasili'nin tahtını kurtararak Oka boyunu yurtluk olarak kazandı."}
                ],
                "legends": ["Kasimov kentinde 1467 yılında inşa ettirdiği taş minarenin bugün dahi Rusya Federasyonu'nda ayakta duran en eski İslam anıtlarından biri olması onun mirasıdır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KASIM HANLIĞI", "url": "https://islamansiklopedisi.org.tr/kasim-hanligi"}
                ]
            }
        ]
    },
    {
        "id": "delhi-turk-sultanligi",
        "name": "Delhi Türk Sultanlığı",
        "short": "Delhi Sultanlığı (Memlûk-Halacî)",
        "aliases": ["Delhi Sultanate", "Saltanat-ı Dehlî", "Hindistan Türk Devleti"],
        "region": "turkistan",
        "start": 1206,
        "end": 1526,
        "startNote": "1206'da Kutbüddin Aybeg'in bağımsızlığını ilan etmesiyle kurulan; Memlûk, Halacî ve Tuğluk Türk hanedanlarının yönettiği büyük imparatorluk.",
        "endNote": "1526 Panipat Meydan Muharebesi'nde Bâbür Şah'ın İbrâhim Lûdî'yi yenmesiyle yerini Bâbür İmparatorluğu'na bıraktı.",
        "capital": "Delhi (Lâl Kot, Tughlakabad)",
        "religion": "İslamiyet (Sünnî-Hanefî)",
        "confidence": "kayit",
        "confidenceNote": "Minhâc-ı Sirâc (Tabakât-ı Nâsırî), Ziyâeddin Berenî (Târîh-i Fîrûzşâhî) ve İbn Battûta seyahatnamesiyle sabittir.",
        "summary": "Hindistan alt kıtasında İslam hakimiyetini kalıcı kılan, 320 yıl boyunca Delhi merkezli hüküm süren kudretli Türk imparatorluğu. Kutbüddin Aybeg, Şemseddin İltutmuş, Türk ve İslam tarihinin ilk kadın hükümdarı Raziyye Sultan, Alâeddin Halacî ve Muhammed bin Tuğluk gibi büyük hükümdarlar yönetti. Kutub Minar gibi abidevi eserler inşa edildi. Moğol istilalarını defalarca püskürterek Hindistan'ı tahripten kurtardı. 1526'da Bâbür İmparatorluğu'na devroldu.",
        "legacy": "Dünyanın en yüksek tuğla minaresi olan Kutub Minar'ı insanlığa kazandırdı; Hint alt kıtasını Türk-İslam mimarisi ve sanatıyla yoğurdu.",
        "essay": [
            "Delhi Türk Sultanlığı, Gurlu kumandanı Kıpçak asıllı Kutbüddin Aybeg'in 1206'da bağımsızlığını ilan etmesiyle kuruldu. Aybeg'in başlattığı Kutub Minar, Türk-İslam mimarisinin Hindistan'daki zafer anıtı oldu.",
            "Şemseddin İltutmuş devleti teşkilatlandırdı; vefatında yerine kızı Raziyye Sultan'ı veliaht bıraktı. Raziyye Sultan (1236-1240), erkek kıyafetleriyle ordusunun başında bizzat sefere çıkan, feraseti ve adaletli yönetimiyle Türk tarihine geçen ilk kadın sultan oldu.",
            "Alâeddin Halacî (1296-1316), Moğol ordularını beş kez üst üste hezimete uğratarak Hindistan'ı Moğol felaketinden kurtardı ve Güney Hindistan'ı fethetti. Muhammed bin Tuğluk devrinde imparatorluk tüm Hint kıtasına yayıldı. 1526'da taht Timur soyundan gelen Bâbür Şah'a geçti."
        ],
        "sources": [
            {"title": "TDV İslâm Ansiklopedisi, DELHİ SULTANLIĞI", "url": "https://islamansiklopedisi.org.tr/delhi-sultanligi"},
            {"title": "TDV İslâm Ansiklopedisi, KUTBÜDDİN AYBEG", "url": "https://islamansiklopedisi.org.tr/kutbuddin-aybeg"},
            {"title": "TDV İslâm Ansiklopedisi, RAZİYYE BEGÜM", "url": "https://islamansiklopedisi.org.tr/raziyye-begum"},
            {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN HALACÎ", "url": "https://islamansiklopedisi.org.tr/alaeddin-halaci"}
        ],
        "rulers": [
            {
                "id": "delhi-kutbuddin-aybeg",
                "name": "Kutbüddin Aybeg",
                "aliases": ["Aybeg", "Lâh-bahş (Milyonlar Bağışlayan)"],
                "title": "Sultan / Memlûk / Kurucu",
                "birth": 1150,
                "birthNote": "Türkistan bozkırında doğdu, Nişabur'da köle pazarından alındı",
                "death": 1210,
                "deathNote": "Lahor'da polo (çevgân) oynarken atından düşerek vefat etti",
                "reign": [1206, 1210],
                "reignNote": "Delhi Sultanlığı ve Muizzî (Memlûk) Hanedanı'nın kurucusu.",
                "summary": "Türkistan'dan köle olarak getirilip liyakatiyle Hindistan fatihi ve hükümdarı olan büyük sultan. Delhi'yi fethederek başkent yaptı. Hindistan'ın en görkemli taş minaresi olan Kutub Minar'ın ve Kuvvetü'l-İslam Camii'nin inşasını başlattı. Cömertliği sebebiyle 'Lâh-bahş' lakabını aldı.",
                "traits": ["Fevkalade cömert", "Yenilmez fatih", "Mütevazı teşkilatçı"],
                "contribution": "Hindistan'da 300 yıl sürecek Türk hakimiyetini kurdu; Kutub Minar'ın temelini attı.",
                "harm": "Erken vefatı sebebiyle sultanlığın idari teşkilatını tam olarak tamamlayamadı.",
                "wives": [
                    {"name": "Tâceddin Yıldız'ın Kızı", "note": "Siyasi izdivaç", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "Ârâm Şah", "mother": "", "note": "Kısa süre tahta oturdu", "certainty": "tartismali"},
                    {"name": "Kutbiyye Hatun", "mother": "", "note": "Şemseddin İltutmuş ile evlenen kızı", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Tarain Muharebesi", "when": "1192", "foe": "Çauhan Racput Krallığı (Prithviraj)", "result": "zafer", "note": "Kuzey Hindistan kapıları Türk ordularına açıldı."},
                    {"name": "Delhi Kuşatması ve Fethi", "when": "1193", "foe": "Tomara Hanedanı", "result": "zafer", "note": "Delhi zaptedilerek Türk hakimiyetinin merkezi yapıldı."}
                ],
                "legends": ["Kutub Minar'ın dibinde bulunan paslanmaz demir sütunun (Iron Pillar of Delhi) yanına inşa ettiği cami günümüzde UNESCO Dünya Mirasıdır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, KUTBÜDDİN AYBEG", "url": "https://islamansiklopedisi.org.tr/kutbuddin-aybeg"}
                ]
            },
            {
                "id": "delhi-raziyye-sultan",
                "name": "Raziyye Sultan",
                "aliases": ["Celâletüddin Raziyye Begüm", "Razia Sultana"],
                "title": "Sultan / Padişah-ı Âlem",
                "birth": 1205,
                "birthNote": "Delhi'de sarayda doğdu",
                "death": 1240,
                "deathNote": "Kaithal yakınlarında esir alınıp şehit edildi",
                "reign": [1236, 1240],
                "reignNote": "Türk-İslam tarihinin tahta geçen İLK kadın hükümdarı.",
                "summary": "Şemseddin İltutmuş'un kızı. Babasının vasiyeti ve halkın desteğiyle tahta çıktı. Sarayda ve orduda erkek kıyafetleriyle göründü; ata bindi, ordusunun başında bizzat savaştı. 'Umdetü'n-Nisvân' unvanıyla sikke bastırdı. Kırklar Meclisi'nin (Çihilgân) Türk emirlerinin entrikalarına karşı cesurca savaştı. Altuniye ile evlenerek tahtını geri almaya çalışırken pusuya düşürülüp şehit edildi.",
                "traits": ["Cesur kadın hükümdar", "Adalet timsali", "Fevkalade zeki", "Halkın sevgilisi"],
                "contribution": "Türk kadınının devlet idaresindeki kudretini ve cesaretini tüm dünyaya kanıtladı; medreseler ve kütüphaneler kurdu.",
                "harm": "Gelenekçi Türk emirleri ('Kırklar') ile girdiği iktidar mücadelesi saray krizlerini tetikledi.",
                "wives": [],
                "children": [],
                "wars": [
                    {"name": "Delhi Taht İsyanı Bastırması", "when": "1236", "foe": "Vezir Cüneydî ve İsyancı Türk Emirleri", "result": "zafer", "note": "Kırmızı elbise giyip halkın önüne çıkarak adaleti sağladı ve tahtını güvenceye aldı."},
                    {"name": "Kaithal Muharebesi", "when": "1240", "foe": "Behram Şah Destekçisi Emirler", "result": "yenilgi", "note": "Ordusu dağıldı, esir alınarak şehit edildi."}
                ],
                "legends": ["Tarihçi Minhâc-ı Sirâc onun için: 'Büyük bir hükümdarda bulunması gereken bütün vasıflara fazlasıyla sahipti; tek eksiği kaderin onu kadın yaratmış olmasıydı' diye yazmıştır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, RAZİYYE BEGÜM", "url": "https://islamansiklopedisi.org.tr/raziyye-begum"}
                ]
            },
            {
                "id": "delhi-alaeddin-halaci",
                "name": "Alâeddin Halacî",
                "aliases": ["Sikander-i Sâni (İkinci İskender)"],
                "title": "Sultan / İkinci İskender",
                "birth": 1266,
                "birthNote": "Delhi civarında doğdu",
                "death": 1316,
                "deathNote": "Delhi'de vefat etti",
                "reign": [1296, 1316],
                "reignNote": "20 yıllık hükümdarlığıyla Hindistan'ın en kudretli fatihi.",
                "summary": "Halacî Türk hanedanının en büyük sultanı. Çağatay Moğollarının 5 büyük istila ordusunu Kili, Delhi ve Amroha muharebelerinde imha ederek Hindistan'ı Moğol istilasından kurtardı. Güney Hindistan'ı (Dekkan, Madurai) fethetti. Tarihin ilk sıkı fiyat denetimi ve narh sistemini (pazar ekonomisi kontrolü) başarıyla uyguladı. Kendisine 'İkinci İskender' lakabını verdi.",
                "traits": ["Yenilmez mareşal", "Ekonomi dehası", "Kati disiplinli lider", "Moğol fatihi"],
                "contribution": "Hindistan'ı Moğol soykırımından kurtardı; pazar ve narh reformlarıyla halkın alım gücünü ve ordu donanımını zirveye çıkardı.",
                "harm": "Vergileri çok yüksek tuttu; şüphelendiği muhaliflere karşı acımasız cezalar uyguladı.",
                "wives": [
                    {"name": "Kemlâ Devî", "note": "Gucerât racasının eski eşi", "certainty": "kesin"},
                    {"name": "Mehru'n-Nisâ", "note": "Alp Han'ın kız kardeşi", "certainty": "olasi"}
                ],
                "children": [
                    {"name": "Hızır Han", "mother": "", "note": "Veliaht şehzade", "certainty": "kesin"},
                    {"name": "Kutbüddin Mübârek Şah", "mother": "", "note": "Sonraki sultan", "certainty": "kesin"}
                ],
                "wars": [
                    {"name": "Kili Muharebesi (Moğol İstilası)", "when": "1299", "foe": "Çağatay Hanlığı Moğol Ordusu (Kutluk Hoca)", "result": "zafer", "note": "200 bin kişilik Moğol ordusu Delhi önlerinde bozguna uğratıldı."},
                    {"name": "Çitor Kuşatması ve Fethi", "when": "1303", "foe": "Mewar Racput Krallığı (Ratan Singh)", "result": "zafer", "note": "Aşılamaz Çitor dağ kalesi fethedildi."},
                    {"name": "Amroha Muharebesi", "when": "1305", "foe": "Moğol Ordusu (Ali Beg ve Tarğı)", "result": "zafer", "note": "Moğol komutanları esir alındı, Moğol tehdidi kalıcı olarak kırıldı."}
                ],
                "legends": ["Bastırdığı sikkelerin üzerine 'İskender-i Sâni' (İkinci İskender) unvanını kazıtması ve dünyayı fethetme ideali tarih boyunca anlatılmıştır."],
                "sources": [
                    {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN HALACÎ", "url": "https://islamansiklopedisi.org.tr/alaeddin-halaci"}
                ]
            }
        ]
    }
]

def main():
    p_f = RAW / "f-altin-orda.json"
    p_f.write_text(json.dumps(data_f, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(data_f)} states to {p_f}")

    p_g = RAW / "g-kuzey-hanliklari.json"
    p_g.write_text(json.dumps(data_g, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(data_g)} states to {p_g}")

if __name__ == "__main__":
    main()
