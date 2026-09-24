#!/usr/bin/env python3
"""Build l-anadolu-selcuklu.json."""
import json
from pathlib import Path

data = [
  {
    "id": "anadolu-selcuklu",
    "name": "Anadolu Selçuklu Devleti",
    "short": "Türkiye Selçukluları",
    "aliases": ["Türkiye Selçuklu Devleti", "Rum Selçukluları", "Sultanate of Rum"],
    "region": "anadolu",
    "start": 1077,
    "end": 1308,
    "startNote": "Kutalmışoğlu Süleyman Şah'ın İznik'i fethederek başkent yapmasıyla kuruldu.",
    "endNote": "1308 yılında Sultan II. Mesud'un vefatıyla hanedan sona erdi; Anadolu beylikler dönemine girdi.",
    "capital": "İznik (1077-1097), ardından Konya (1097-1308)",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "İbn Bîbî (el-Evâmirü'l-Alâiyye), Kerîmüddin Aksarâyî (Müsâmeretü'l-Ahbâr) ve Bizans kronikleriyle sabittir.",
    "summary": "1071 Malazgirt Zaferi'nin ardından Kutalmışoğlu Süleyman Şah tarafından İznik merkezli kurulan, I. Haçlı Seferi'nden sonra başkenti Konya'ya taşıyan büyük Türk devleti. II. Kılıç Arslan devrinde 1176 Miryokefalon Zaferi ile Anadolu'nun tapusu kesin olarak alındı ve Avrupalılar Anadolu'ya 'Turchia' (Türkiye) demeye başladı. I. Alâeddin Keykubad zamanında kervansaraylar, tersaneler ve kalelerle Akdeniz ve Karadeniz ticaretine hükmeden bir refah imparatorluğu oldu. 1243 Kösedağ hezimetinin ardından İlhanlı Moğol vesayetine girdi ve 1308'de dağıldı.",
    "legacy": "Anadolu'yu geri dönülemez biçimde kalıcı bir Türk ve İslam yurdu kıldı. İpek Yolu üzerinde inşa ettiği yüzlerce kervansaray, medrese, darüşşifa ve kümbetlerle eşsiz Selçuklu mimarisini miras bıraktı. Mevlânâ Celâleddîn-i Rûmî, Yûnus Emre ve Hacı Bektâş-ı Velî gibi manevi kurucuların ocağı oldu.",
    "essay": [
      "Anadolu Selçuklu Devleti, Büyük Selçuklu hanedan ailesinden Arslan Yabgu'nun torunu Kutalmışoğlu Süleyman Şah'ın Türkmen boylarıyla Anadolu içlerine akmasıyla doğdu. 1075-1077 yıllarında Bizans'ın elindeki İznik'i fetheden Süleyman Şah, başkentini İstanbul Boğazı'nın yanı başında kurdu. 1086'da Antakya yakınlarında Suriye Meliki Tutuş ile yaptığı savaşta şehit düştü.",
      "Oğlu I. Kılıç Arslan (1092-1107), 1096-1097'de yüz binlerce kişilik I. Haçlı Seferi ordularına karşı İznik'i kahramanca savundu; şehri Bizans'a bırakmak zorunda kalınca devlet merkezini Konya'ya nakletti. Haçlı ordularını Eskişehir ve Toroslar'da gerilla taktikleriyle yıprattı. II. Kılıç Arslan (1155-1192) devrinde Bizans İmparatoru Manuel Komnenos büyük bir orduyla Anadolu'yu geri almak için harekete geçtiyse de 17 Eylül 1176'da Eğirdir gölü yakınlarındaki Miryokefalon Geçidi'nde Türk ordusunca pusuya düşürülüp tamamen imha edildi. Bu zaferle Bizans'ın Türkleri Anadolu'dan atma ümidi ebediyen söndü.",
      "Devlet en parlak devrini I. Alâeddin Keykubad (1220-1237) zamanında yaşadı. Akdeniz'de Alâiye (Alanya) fethedilerek tersane kuruldu; Karadeniz'de Kırım'daki Suğdak limanına ilk denizaşırı deniz seferi düzenlendi. Anadolu baştan başa kervansaraylarla örüldü, dünyada ilk devlet sigortacılığı sistemi uygulandı. Ancak Keykubad'ın zehirlenerek ölümü ve ehliyetsiz vezir Sadettin Köpek'in entrikaları devleti zaafa uğrattı. 1240 Babâî İsyanı ile sarsılan ordu, 1243 Kösedağ Muharebesi'nde Moğol kumandanı Baycu Noyan'a mağlup oldu. Devlet Moğol haraçgüzarı haline geldi ve 1308'de son sultan II. Mesud'un ölümüyle tarih sahnesinden çekildi."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, ANADOLU SELÇUKLULARI", "url": "https://islamansiklopedisi.org.tr/anadolu-selcuklulari"},
      {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN KEYKUBAD I", "url": "https://islamansiklopedisi.org.tr/alaeddin-keykubad-i"},
      {"title": "TDV İslâm Ansiklopedisi, KILIÇARSLAN II", "url": "https://islamansiklopedisi.org.tr/kilicarslan-ii"}
    ],
    "rulers": [
      {
        "id": "anadolu-selcuklu-suleyman-sah",
        "name": "Kutalmışoğlu Süleyman Şah",
        "aliases": ["I. Süleyman Şah", "Süleyman bin Kutalmış"],
        "title": "Sultan / Fatih",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1086,
        "deathNote": "Ayn Seylem Muharebesi'nde Tutuş'a yenilince kendi hançeriyle intihar etti veya öldürüldü",
        "reign": [1077, 1086],
        "reignNote": "9 yıllık kurucu hükümdarlık.",
        "summary": "Anadolu Selçuklu Devleti'nin kurucusu. İznik'i fethederek başkent yaptı; Marmara ve Boğaziçi kıyılarına kadar uzanıp Bizans iç siyasetinde imparator belirleyecek güce ulaştı. 1084'te Antakya'yı fethetti; Suriye Meliki Tutuş ile savaşında vefat etti.",
        "traits": ["Büyük fatih", "Cesur komutan", "Teşkilatçı"],
        "contribution": "Anadolu'da bağımsız Türk devletini kurdu; İznik ve Antakya'yı fethetti.",
        "harm": "Büyük Selçuklu hanedan mensuplarıyla girdiği çatışma erken ölümüne ve devletin 6 yıl başsız kalmasına yol açtı.",
        "wives": [],
        "children": [
          {"name": "I. Kılıç Arslan", "mother": "", "note": "İkinci sultan, Haçlı savaşçısı", "certainty": "kesin"},
          {"name": "Kulan Arslan (Davud)", "mother": "", "note": "Şehzade", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "İznik'in Fethi", "when": "1075", "foe": "Bizans İmparatorluğu", "result": "zafer", "note": "İznik fethedilip başkent yapıldı."},
          {"name": "Antakya Fethi", "when": "1084", "foe": "Bizans valisi Philaretos", "result": "zafer", "note": "Müstahkem Antakya kalesi gece baskınıyla fethedildi."},
          {"name": "Ayn Seylem Muharebesi", "when": "1086", "foe": "Suriye Selçuklu Meliki Tutuş", "result": "yenilgi", "note": "Süleyman Şah savaşta vefat etti, oğulları İsfahan'a rehin götürüldü."}
        ],
        "legends": ["Mezarı Caber Kalesi eteklerinde 'Türk Mezarı' olarak asırlarca Türk bayrağı altında saygıyla korundu."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, SÜLEYMAN ŞAH I", "url": "https://islamansiklopedisi.org.tr/suleyman-sah-i"}
        ]
      },
      {
        "id": "anadolu-selcuklu-kilic-arslan-1",
        "name": "I. Kılıç Arslan",
        "aliases": ["Ebû'l-Kāsım Kılıç Arslan"],
        "title": "Sultan",
        "birth": 1079,
        "birthNote": "1079 doğumlu",
        "death": 1107,
        "deathNote": "Habur çayında zırhının ağırlığıyla atıyla birlikte boğularak şehit oldu",
        "reign": [1092, 1107],
        "reignNote": "15 yıllık Haçlı seferleriyle dolu kahramanlık devri.",
        "summary": "Süleyman Şah'ın oğlu. Melikşah'ın ölümü üzerine esaretten dönüp İznik'te tahta çıktı. 1096'da Keşiş Pierre l'Ermite'in ilk Haçlı sürüsünü Yalova'da tamamen imha etti. I. Haçlı Seferi'nin devasa şövalye ordularına karşı başkenti Konya'ya taşıyıp gerilla savaşıyla Haçlılara ağır kayıplar verdirdi. Musul'u fethettikten sonra Habur nehrinde şehit düştü.",
        "traits": ["Haçlı fatihi", "Yılmayan savaşçı", "Millet muhafızı"],
        "contribution": "Haçlı ordularının Anadolu'da tutunmasını engelleyerek Türk varlığını korudu; Konya'yı ebedi başkent yaptı.",
        "harm": "Kayınpederi Çaka Bey'i Bizans entrikasıyla öldürtmesi Ege'deki deniz gücünü yok etti.",
        "wives": [
          {"name": "Ayşe Hatun", "note": "Çaka Bey'in kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "I. Mesud", "mother": "", "note": "Uzun süre hüküm süren kudretli sultan", "certainty": "kesin"},
          {"name": "Melikşah (Şahinşah)", "mother": "", "note": "Taht mücadelesine girdi", "certainty": "kesin"},
          {"name": "Tuğrul Arslan", "mother": "", "note": "Malatya meliki", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Halk Haçlı Seferi İmhası (Kibotos)", "when": "1096", "foe": "Pierre l'Ermite ve Walter Sans-Avoir komutasındaki Haçlılar", "result": "zafer", "note": "20 binden fazla Haçlı Yalova'da kılıçtan geçirildi."},
          {"name": "Dorylaion (Eskişehir) Muharebesi", "when": "1097", "foe": "I. Haçlı Seferi büyük ordusu (Bohemund, Godfrey)", "result": "yenilgi", "note": "Sayıca üstün Haçlılara karşı gerilla taktiğine dönüldü, başkent Konya'ya taşındı."},
          {"name": "1101 Haçlı Seferlerinin İmhası", "when": "1101", "foe": "Fransız, Alman ve Lombard Haçlı orduları", "result": "zafer", "note": "Danişmend Gazi ile birleşerek Merzifon, Konya ve Ereğli'de üç ayrı Haçlı ordusunu yok etti."}
        ],
        "legends": ["Silvan'daki kayıp mezarı (Kümbet-i Sultan) 2021 yılında Türk tarihçileri ve arkeologlarınca keşfedilmiştir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, KILIÇARSLAN I", "url": "https://islamansiklopedisi.org.tr/kilicarslan-i"}
        ]
      },
      {
        "id": "anadolu-selcuklu-kilic-arslan-2",
        "name": "II. Kılıç Arslan",
        "aliases": ["İzzeddin Kılıç Arslan"],
        "title": "Sultan / Gazi",
        "birth": 1113,
        "birthNote": "Yaklaşık 1113 doğumlu",
        "death": 1192,
        "deathNote": "Konya'da 79 yaşında vefat etti",
        "reign": [1155, 1192],
        "reignNote": "37 yıllık muhteşem saltanat.",
        "summary": "I. Mesud'un oğlu. 1176 Miryokefalon Zaferi ile Bizans ordusunu perişan ederek Anadolu'nun ebediyen Türk yurdu olduğunu tescil ettirdi. Danişmendli beyliğine son vererek Anadolu Türk birliğini ilk kez geniş ölçüde kurdu. Aksaray şehrini kurdu, ilk Selçuklu gümüş ve altın parasını bastırdı.",
        "traits": ["Büyük stratejist", "İmar hamisi", "Metanetli"],
        "contribution": "Miryokefalon Zaferi ile Anadolu'nun Türklüğünü kesinleştirdi; kervansaray mimarisini başlattı (Alay Han).",
        "harm": "Yaşlılığında ülkeyi 11 oğlu arasında paylaştırması ölümünden önce ve sonra kanlı iç savaşlara yol açtı.",
        "wives": [],
        "children": [
          {"name": "Kutbeddin Melikşah", "mother": "", "note": "Sivas meliki, babasına isyan etti", "certainty": "kesin"},
          {"name": "I. Gıyâseddin Keyhüsrev", "mother": "", "note": "Tahtı devralan sultan", "certainty": "kesin"},
          {"name": "Rükneddin Süleyman Şah", "mother": "", "note": "Kardeşlerini tasfiye edip tek başına sultan oldu", "certainty": "kesin"},
          {"name": "Muhyiddin Mesud Şah", "mother": "", "note": "Ankara meliki", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Miryokefalon Meydan Muharebesi", "when": "1176", "foe": "Bizans İmparatorluğu (Manuel I Komnenos)", "result": "zafer", "note": "Bizans ordusu dar dağ geçidinde pusuya düşürülüp imha edildi, Bizans ağır tazminat ödedi."}
        ],
        "legends": ["Miryokefalon zaferinden sonra Batılı kroniklerin Anadolu'ya 'Turchia' (Türklerin Yurdu) adını vermeye başlaması bu zaferin meyvesidir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, KILIÇARSLAN II", "url": "https://islamansiklopedisi.org.tr/kilicarslan-ii"}
        ]
      },
      {
        "id": "anadolu-selcuklu-alaeddin-keykubad",
        "name": "I. Alâeddin Keykubad",
        "aliases": ["Alâeddin Keykubad", "Uluğ Sultan"],
        "title": "Sultan / Sultanü'l-Gālib",
        "birth": 1190,
        "birthNote": "1190 doğumlu",
        "death": 1237,
        "deathNote": "Kayseri Meşhedliğindeki ziyafette av etinden zehirlenerek şehit edildi",
        "reign": [1220, 1237],
        "reignNote": "17 yıllık altın çağ.",
        "summary": "Anadolu Selçuklularının en kudretli ve en büyük sultanı. Akdeniz'de Kalonoros kalesini fethedip Alâiye (Alanya) adıyla donanma üssü ve kışlık başkent yaptı. Karadeniz'de Kırım'a donanma gönderip Suğdak'ı fethetti. Konya, Sivas ve Kayseri surlarını tahkim etti, kervansaraylarla ülkeyi donattı. Yassıçemen'de Harzemşah Celâleddin'i mağlup etti. Moğol tehlikesine karşı tedbirler alırken zehirlendi.",
        "traits": ["Cihan devleti hükümdarı", "Mimar ve şehir kurucusu", "Yüksek adalet ve basiret"],
        "contribution": "Türkiye'yi denizci bir ticaret imparatorluğuna yükseltti; kervansaray ağı ve tüccar sigortasıyla iktisadi altın çağı inşa etti.",
        "harm": "Ani zehirlenmesi devletin liyakatsiz vezir Sadettin Köpek'in eline düşmesine yol açtı.",
        "wives": [
          {"name": "Mahperi Hunat Hatun", "note": "Alanya tekfurunun kızı, Kayseri'deki Hunat Hatun Külliyesi'ni yaptıran dindar valide sultan", "certainty": "kesin"},
          {"name": "Melike Âdile Hatun", "note": "Eyyûbî Sultanı el-Âdil'in kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "II. Gıyâseddin Keyhüsrev", "mother": "Mahperi Hunat Hatun", "note": "Kösedağ'da mağlup olan sultan", "certainty": "kesin"},
          {"name": "İzzettin Kılıç Arslan", "mother": "Melike Âdile Hatun", "note": "Keykubad'ın veliahtıydı, katledildi", "certainty": "kesin"},
          {"name": "Rükneddin", "mother": "Melike Âdile Hatun", "note": "Şehzade, katledildi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kalonoros (Alanya) Kuşatması", "when": "1221", "foe": "Ermeni Kir Fard tekfurluğu", "result": "zafer", "note": "Alanya fethedildi, tersane ve Kızıl Kule inşa edildi."},
          {"name": "Suğdak Kırım Deniz Seferi", "when": "1224", "foe": "Kıpçaklar ve Rus dükleri", "result": "zafer", "note": "Emir Hüsameddin Çoban donanmayla Kırım'a çıktı, Suğdak alındı."},
          {"name": "Yassıçemen Muharebesi", "when": "1230", "foe": "Harzemşahlar (Celâleddin)", "result": "zafer", "note": "Erzincan yakınlarında Celâleddin mağlup edildi, doğu sınırları emniyete alındı."}
        ],
        "legends": ["Konya ve Sivas surlarının taşlarına şairlerin beyitlerini ve kentin koruyucu çift başlı kartal tılsımlarını bizzat elleriyle koydurduğu anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ALÂEDDİN KEYKUBAD I", "url": "https://islamansiklopedisi.org.tr/alaeddin-keykubad-i"}
        ]
      }
    ]
  },
  {
    "id": "danismendli",
    "name": "Dânişmendliler",
    "short": "Dânişmendliler",
    "aliases": ["Dânişmend Beyliği", "Âl-i Dânişmend"],
    "region": "anadolu",
    "start": 1080,
    "end": 1178,
    "startNote": "Malazgirt fatihlerinden Dânişmend Gazi tarafından Sivas merkezli kuruldu.",
    "endNote": "1178'de II. Kılıç Arslan'ın Malatya koluna son vermesiyle Anadolu Selçuklu Devleti'ne bağlandı.",
    "capital": "Sivas, Niksar ve Malatya",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "Dânişmendnâme destanı, İbnü'l-Esîr, Süryani Mihail ve Bizans kronikleriyle sabittir.",
    "summary": "Malazgirt Zaferi'nden sonra Orta ve Kuzey Anadolu'da (Sivas, Tokat, Niksar, Amasya, Kayseri, Malatya) kurulan en güçlü Türk beyliği. Haçlı Seferleri'ne karşı kahramanca savaştılar; Antakya Haçlı Prensi Bohemund'u esir alıp Niksar kalesine hapsettiler. Anadolu'da ilk tıp medresesi olan Tokat ve Niksar Yağıbasan Medresesi'ni (kapalı kubbeli) inşa ettiler. Dânişmend Gazi'nin kahramanlıkları Dânişmendnâme adıyla halk destanına dönüştü.",
    "legacy": "Anadolu'da ilk kubbeli Türk medresesini (Niksar ve Tokat Yağıbasan Medreseleri) inşa etti; Dânişmendnâme Türk halk edebiyatının kurucu şaheseri oldu.",
    "essay": [
      "Dânişmendliler, Sultan Alparslan'ın Anadolu fethiyle görevlendirdiği ve ilmi kişiliği dolayısıyla 'Dânişmend' (bilgin/hoca) lakabıyla anılan Ahmed Gazi tarafından 1080 civarında Sivas merkezli kuruldu.",
      "Melik Gazi devrinde I. Kılıç Arslan ile birleşerek 1101 yılı Haçlı dalgalarını Merzifon ve Ereğli'de imha ettiler. Antakya Prensi Bohemund'u esir alarak İslam dünyasında büyük şöhret kazandılar. Melik Muhammed ve Nizamettin Yağıbasan dönemlerinde Kayseri ve Tokat muhteşem imar hareketleriyle donatıldı.",
      "Hanedanın Sivas, Kayseri ve Malatya kollarına ayrılması gücünü zayıflattı. 1178 yılında Anadolu Selçuklu Sultanı II. Kılıç Arslan bütün Dânişmendli topraklarını ilhak ederek Anadolu Türk birliğini kurdu."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, DÂNİŞMENDLİLER", "url": "https://islamansiklopedisi.org.tr/danismendliler"},
      {"title": "TDV İslâm Ansiklopedisi, DÂNİŞMEND GAZİ", "url": "https://islamansiklopedisi.org.tr/danismend-gazi"}
    ],
    "rulers": [
      {
        "id": "danismendli-ahmed-gazi",
        "name": "Dânişmend Gazi",
        "aliases": ["Dânişmend Ahmed Gazi", "Gümüştekin Ahmed Gazi"],
        "title": "Melik / Gazi",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1104,
        "deathNote": "Niksar'da vefat etti, türbesi oradadır",
        "reign": [1080, 1104],
        "reignNote": "24 yıllık gazalarla dolu beylik.",
        "summary": "Beyliğin kurucusu ve Dânişmendnâme kahramanı. Sivas, Niksar, Çorum ve Tokat'ı fethederek Türk yurdu yaptı. 1100 yılında Antakya Prinkepsi Bohemund'u Malatya önlerinde esir alarak İslam dünyasına bayram yaşattı.",
        "traits": ["Âlim savaşçı", "Destan kahramanı", "Adil"],
        "contribution": "Orta Karadeniz ve Sivas havzasının fethini ve Türkleşmesini sağladı.",
        "harm": "Malatya kuşatması yüzünden Selçuklu Sultanı Kılıç Arslan ile çekişti.",
        "wives": [],
        "children": [
          {"name": "Emir Gazi (Gümüştekin)", "mother": "", "note": "Babasından sonra tahta oturdu, Abbasi halifesi meliklik menşuru verdi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Malatya Muharebesi (Bohemund'un Esareti)", "when": "1100", "foe": "Antakya Haçlı Prensliği (I. Bohemund)", "result": "zafer", "note": "Bohemund esir edildi, Niksar kalesine hapsedildi, 100 bin altın fidye alındı."}
        ],
        "legends": ["Dânişmendnâme'de Battal Gazi'nin soyundan geldiği ve rüyasında Peygamber Efendimiz tarafından Anadolu fethine memur edildiği anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, DÂNİŞMEND GAZİ", "url": "https://islamansiklopedisi.org.tr/danismend-gazi"}
        ]
      }
    ]
  },
  {
    "id": "saltuklu",
    "name": "Saltuklular",
    "short": "Saltuklular",
    "aliases": ["Saltuklu Beyliği", "Âl-i Saltuk"],
    "region": "anadolu",
    "start": 1072,
    "end": 1202,
    "startNote": "Malazgirt Zaferi'nin ardından Ebü'l-Kāsım Saltuk'un Erzurum ve Kars havalisini fethetmesiyle kuruldu.",
    "endNote": "1202 yılında Rükneddin Süleyman Şah'ın Gürcü seferi sırasında Erzurum'u ilhak etmesiyle sona erdi.",
    "capital": "Erzurum",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "İbnü'l-Esîr, Ahbârü'd-Devleti's-Selcûkıyye ve Erzurum kitabeleriyle sabittir.",
    "summary": "Malazgirt Zaferi sonrası Doğu Anadolu'da kurulan ilk Türk beyliği. Erzurum merkezli olarak Bayburt, Kars, Oltu ve İspir bölgelerine hakim oldular. Gürcü Krallığı'nın akınlarına karşı İslam sınır boylarını korudular. Erzurum Kale Mescidi, Tepsi Minare, Ulu Cami ve Tercan'daki ünlü Mama Hatun Kümbeti ve Kervansarayı bu beyliğin şaheserleridir.",
    "legacy": "Doğu Anadolu'nun kapısı Erzurum'u Türk-İslam mimarisinin abidevi eserleriyle donattı; Türk kadınının devlet yöneticiliğindeki dirayetini simgeleyen Mama Hatun Külliyesi'ni armağan etti.",
    "essay": [
      "Saltuklular, Sultan Alparslan'ın Malazgirt Zaferi'nden sonra fethettiği Erzurum ve civarını dirlik olarak verdiği kumandanı Ebü'l-Kāsım Saltuk Bey tarafından 1072'de kuruldu.",
      "Beylik en parlak devrini II. İzzeddin Saltuk (1132-1168) ve kızı Mama Hatun zamanında yaşadı. Mama Hatun, Tercan'da kendi adına yaptırdığı dairevi planlı eşsiz kümbet, kervansaray ve hamamıyla Türk kadın hükümdarlarının zarafet ve kudret timsali oldu. 1202 yılında Anadolu Selçuklu Sultanı Rükneddin Süleyman Şah, Gürcü seferi sırasında itaatsizlik gösteren son Saltuklu beyi Alâeddin Muhammed'i tutuklayarak beyliği Anadolu Selçuklu Devleti'ne bağladı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, SALTUKLULAR", "url": "https://islamansiklopedisi.org.tr/saltuklular"}
    ],
    "rulers": [
      {
        "id": "saltuklu-ebul-kasim",
        "name": "Ebü'l-Kāsım Saltuk Bey",
        "aliases": ["Saltuk Gazi", "Emir Saltuk"],
        "title": "Emir / Bey",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1102,
        "deathNote": "Erzurum'da vefat etti",
        "reign": [1072, 1102],
        "reignNote": "30 yıllık kurucu beylik.",
        "summary": "Malazgirt komutanlarından, Erzurum'un fatihi ve beyliğin kurucusu. Gürcü ve Bizans saldırılarına karşı sınır boyunu müdafaa etti; Erzurum Kalesi'ni tahkim ettirdi.",
        "traits": ["Gazi komutan", "Serhat muhafızı"],
        "contribution": "Doğu Anadolu'da ilk Türk yerleşimini ve idaresini kurdu.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "Ali b. Saltuk", "mother": "", "note": "İkinci bey", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Erzurum Fethi", "when": "1072", "foe": "Bizans ve Gürcü garnizonları", "result": "zafer", "note": "Erzurum fethedilip başkent yapıldı."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, SALTUKLULAR", "url": "https://islamansiklopedisi.org.tr/saltuklular"}
        ]
      },
      {
        "id": "saltuklu-mama-hatun",
        "name": "Melike Mama Hatun",
        "aliases": ["Mama Hatun"],
        "title": "Melike / Kadın Hükümdar",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1201,
        "deathNote": "Tercan veya Erzurum'da vefat etti",
        "reign": [1191, 1200],
        "reignNote": "Saltuklu tahtını tek başına dirayetle yöneten kadın hükümdar.",
        "summary": "II. Saltuk'un kızı. 10 yıl boyunca Saltuklu tahtında oturarak beyliği yönetti. Eyyûbîlerle diplomatik ilişkiler kurdu. Tercan'da inşa ettirdiği, Türk mimarisinin dünya çapındaki şaheseri sayılan dilimli kubbeli Mama Hatun Kümbeti ve Kervansarayı ile ölümsüzleşti.",
        "traits": ["Dirayetli kadın lider", "Sanat ve mimari hamisi", "Adil"],
        "contribution": "Anadolu'da eşsiz bir mimari külliye inşa ettirdi; kadın hükümdarlık geleneğinin seçkin bir temsilcisi oldu.",
        "harm": "Evlilik meselesinde beylerle anlaşmazlığa düşüp tahttan indirildi.",
        "wives": [],
        "children": [],
        "wars": [],
        "legends": ["Ahlatlı Mimar Ebü'n-Nemâ b. Mufaddal'a yaptırdığı dairevi planlı türbe mimarlık tarihinde dünyada tektir."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, MAMA HATUN", "url": "https://islamansiklopedisi.org.tr/mama-hatun"},
          {"title": "TDV İslâm Ansiklopedisi, SALTUKLULAR", "url": "https://islamansiklopedisi.org.tr/saltuklular"}
        ]
      }
    ]
  },
  {
    "id": "mengucek",
    "name": "Mengücekliler",
    "short": "Mengücekliler",
    "aliases": ["Mengücek Beyliği", "Âl-i Mengücek"],
    "region": "anadolu",
    "start": 1071,
    "end": 1277,
    "startNote": "Malazgirt Zaferi'nin ardından Mengücek Gazi'nin Erzincan, Kemah ve Divriği'yi fethetmesiyle kuruldu.",
    "endNote": "1277 yılında Anadolu Selçukluları ve Moğol idaresi altında tamamen lağvedildi.",
    "capital": "Kemah, Erzincan ve Divriği",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "UNESCO Dünya Mirası Divriği Ulu Camii kitabeleri, İbn Bîbî ve Süryani kronikleriyle sabittir.",
    "summary": "Malazgirt kahramanlarından Mengücek Gazi tarafından Erzincan, Kemah, Divriği ve Şebinkarahisar yöresinde kurulan beylik. Bilime, tıbba ve sanata büyük kıymet verdiler; meşhur tabip Abdüllatîf el-Bağdâdî'yi Erzincan sarayında ağırladılar. Hükümdar Ahmed Şah ve eşi Turan Melek tarafından 1228'de yaptırılan UNESCO Dünya Mirası Divriği Ulu Camii ve Darüşşifası, taş işçiliğinin dünyadaki en muazzam başyapıtı kabul edilir.",
    "legacy": "İslam taş işçiliğinin 'Görmeden ölmeyin' denilen başyapıtı Divriği Ulu Camii ve Darüşşifası'nı (UNESCO Dünya Mirası) dünya kültür hazinesine kazandırdı.",
    "essay": [
      "Mengücekliler, Malazgirt Zaferi'nin ardından Fırat'ın yukarı havzasını fetheden Mengücek Gazi tarafından kuruldu. Başlangıçta Kemah kalesi merkez yapıldı, ardından Erzincan ve Divriği gelişti.",
      "Fahreddin Behramşah (1162-1225) dönemi beyliğin altın çağı oldu. Şair Nizâmî-i Gencevî, meşhur 'Mahzenü'l-Esrâr' (Sırlar Hazinesi) mesnevisini Behramşah'a ithaf etti. Behramşah'ın torunu Ahmed Şah ve eşi Turan Melek Hatun, 1228'de Divriği Ulu Camii ve Darüşşifası'nı inşa ettirdi. Cami kapısındaki taş oyma süslemelerin güneş ışığıyla ikindi vaktinde namaz kılan bir insan silueti oluşturması matematik ve mimari dehanın zirvesidir. 1228'de I. Alâeddin Keykubad Erzincan kolunu ilhak etti, Divriği kolu ise 1277'ye kadar Selçuklu vassalı olarak sürdü."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, MENGÜCEKLİLER", "url": "https://islamansiklopedisi.org.tr/mengucekliler"},
      {"title": "TDV İslâm Ansiklopedisi, DİVRİĞİ ULU CAMİİ VE DÂRÜŞŞİFASI", "url": "https://islamansiklopedisi.org.tr/divrigi-ulu-camii-ve-darussifasi"}
    ],
    "rulers": [
      {
        "id": "mengucek-mengucek-gazi",
        "name": "Mengücek Gazi",
        "aliases": ["Emir Mengücek", "Mengücük Gazi"],
        "title": "Gazi / Emir",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1118,
        "deathNote": "Kemah'ta şehit düştü, türbesi Kemah Kalesi eteklerindedir",
        "reign": [1071, 1118],
        "reignNote": "47 yıllık kurucu beylik ve fetih dönemi.",
        "summary": "Malazgirt fatihlerinden, beyliğin kurucusu. Kemah, Erzincan ve Divriği'yi Rumlardan fethedip İslamlaştırdı. Türbesi Kemah Fırat kıyısında asırlardır ziyaretgahtır.",
        "traits": ["Alp-gazi", "Korkusuz serhat kumandanı"],
        "contribution": "Fırat vadisini Türk yurdu haline getirdi.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "İshak Bey", "mother": "", "note": "Babasından sonra beyliği devraldı", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Kemah ve Erzincan Fethi", "when": "1071-1075", "foe": "Bizans sınır garnizonu", "result": "zafer", "note": "Sarp Kemah kalesi fethedildi."}
        ],
        "legends": ["Kemah'taki türbesinde cesedinin çürümeden mumyalanmış halde günümüze ulaştığına inanılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, MENGÜCEKLİLER", "url": "https://islamansiklopedisi.org.tr/mengucekliler"}
        ]
      },
      {
        "id": "mengucek-fahreddin-behramsah",
        "name": "Fahreddin Behramşah",
        "aliases": ["Melik Behramşah"],
        "title": "Melik / Gazi",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1225,
        "deathNote": "Erzincan'da vefat etti",
        "reign": [1162, 1225],
        "reignNote": "63 yıllık adalet ve ilim çağı.",
        "summary": "Mengüceklilerin en büyük meliki. Selçuklu II. Kılıç Arslan'ın damadı oldu. Bilim adamlarına, hekimlere ve şairlere sınırsız imkanlar sundu. Nizâmî-i Gencevî 'Mahzenü'l-Esrâr' eserini ona ithaf edince şaire binlerce altın, köle ve hediye katarları gönderdi.",
        "traits": ["İlim ve şiir aşığı", "Cömertlik abidesi", "Adil melik"],
        "contribution": "Erzincan'ı doğunun en saygın ilim ve tıp merkezlerinden biri yaptı.",
        "harm": "Ölümüyle oğulları Selçuklulara karşı direnemedi.",
        "wives": [
          {"name": "Selçuklu Prensesi", "note": "II. Kılıç Arslan'ın kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Dâvud Şah", "mother": "", "note": "Erzincan meliki", "certainty": "kesin"},
          {"name": "Hüsamettin Ahmed Şah", "mother": "", "note": "Divriği Ulu Camii'ni yaptıran melik", "certainty": "kesin"}
        ],
        "wars": [],
        "legends": ["Gence'den gelen elçinin getirdiği şiire karşılık şair Nizâmî'ye deve yükleriyle kumaş ve altın gönderdiği Cüveynî'de anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, MENGÜCEKLİLER", "url": "https://islamansiklopedisi.org.tr/mengucekliler"}
        ]
      }
    ]
  },
  {
    "id": "artuklu",
    "name": "Artuklular",
    "short": "Artuklular",
    "aliases": ["Artuklu Beyliği", "Âl-i Artuk"],
    "region": "anadolu",
    "start": 1102,
    "end": 1409,
    "startNote": "Artuk Bey'in oğulları Sökmen ve İlgazi tarafından Hasankeyf ve Mardin merkezli kuruldu.",
    "endNote": "1409 yılında Karakoyunlu Kara Yusuf'un Mardin'i almasıyla sona erdi.",
    "capital": "Hısnkeyfâ (Hasankeyf), Mardin ve Harput",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "İbnü'l-Ezrak (Târîhu Meyyâfârikīn), İbn Şeddâd, İbnü'l-Esîr kronikleri ve El-Cezerî'nin mekanik kitabı ile sabittir.",
    "summary": "Oğuzların Döğer boyundan Eksük oğlu Artuk Bey'in evlatları tarafından Güneydoğu Anadolu'da (Mardin, Hasankeyf, Harput, Meyyâfârikīn) kurulan köklü Türk devleti. Necmeddin İlgazi devrinde 1119 Tell-Akrîbâ (Kanlı Meydan) Zaferi ile Antakya Haçlı ordusunu yok ettiler. Dünyanın ilk robot ve sibernetik bilgini İsmâil el-Cezerî, Artuklu sarayında 25 yıl başmühendislik yaparak su saatleri ve otomatik makineler icat etti. Malabadi Köprüsü ve Mardin taş medreseleri bu beyliğin şaheseridir.",
    "legacy": "Sibernetik ve robotik ilminin kurucusu El-Cezerî'yi yetiştirdi; dünyanın en geniş açıklıklı taş kemerli köprüsü olan Malabadi Köprüsü'nü ve Mardin medreselerini miras bıraktı.",
    "essay": [
      "Artuklular, Selçuklu ordusunda Kudüs valiliği yapmış olan Döğer boyu beyi Artuk Bey'in vefatından sonra oğulları Sökmen ve İlgazi tarafından kuruldu. Sökmen 1102'de Hasankeyf (Hısnkeyfâ), İlgazi ise 1107 civarında Mardin merkezli kollarını kurdu; daha sonra Harput kolu teşekkül etti.",
      "İlgazi Bey, Haçlı Seferleri'ne karşı İslam dünyasının en büyük kahramanlarından biri oldu. 28 Haziran 1119'da Tell-Akrîbâ (Ager Sanguinis / Kanlı Meydan) Muharebesi'nde Antakya Prinkepsi Roger komutasındaki Haçlı ordusunu neredeyse tek bir kişi sağ kalmayacak şekilde imha etti.",
      "Hasankeyf hükümdarı Nâsırüddin Mahmud devrinde (1200-1222), Cizreli büyük Türk-İslam bilgini İsmâil el-Cezerî sarayda başmühendis olarak çalıştı. 1206 yılında tamamladığı 'Kitâb fî Ma'rifeti'l-Hiyeli'l-Hendesiye' adlı eserinde 50'den fazla robot, mekanik su saati, krank mili ve şifreli kilitlerin çizim ve çalışma prensiplerini insanlığa kazandırdı. Beylik Moğol, Eyyûbî ve Akkoyunlu baskılarına rağmen 1409'a kadar Mardin kalesinde 3 asırdan fazla varlığını korudu."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, ARTUKLULAR", "url": "https://islamansiklopedisi.org.tr/artuklular"},
      {"title": "TDV İslâm Ansiklopedisi, CEZERÎ, İsmâil b. Rezzâz", "url": "https://islamansiklopedisi.org.tr/cezeri-ismail-b-rezzaz"},
      {"title": "TDV İslâm Ansiklopedisi, İLGAZİ, Necmeddin", "url": "https://islamansiklopedisi.org.tr/ilgazi-necmeddin"}
    ],
    "rulers": [
      {
        "id": "artuklu-ilgazi",
        "name": "Necmeddin İlgazi",
        "aliases": ["İlgazi b. Artuk", "Necmeddin İlgazi"],
        "title": "Emir / Kutbüddin",
        "birth": 1062,
        "birthNote": "Yaklaşık 1062 doğumlu",
        "death": 1122,
        "deathNote": "Meyyâfârikīn (Silvan) yolunda hastalanarak vefat etti",
        "reign": [1107, 1122],
        "reignNote": "15 yıllık Haçlı gazalarıyla dolu şanlı hükümdarlık.",
        "summary": "Mardin Artuklularının kurucusu ve Haçlıların korkulu rüyası. Bağdat şahneliği yaptı. 1119 Kanlı Meydan Muharebesi'nde Antakya Haçlı Prensliği ordusunu bütünüyle imha ederek Haçlıların Doğu Akdeniz'deki yayılmasını durdurdu; Halep'i korudu.",
        "traits": ["Yenilmez gazâ önderi", "Meydan muharebesi ustası", "Cesur"],
        "contribution": "Güneydoğu Anadolu ve Suriye'yi Haçlı istilasından kurtardı; Mardin'i Türk başkenti yaptı.",
        "harm": "Sert tabiatı ve zaman zaman içki nöbetleri kriz anlarında karar almasını zorlaştırdı.",
        "wives": [
          {"name": "Firk Hatun", "note": "Dımaşk Atabeyi Tuğtekin'in kızı", "certainty": "kesin"}
        ],
        "children": [
          {"name": "Hüsameddin Timurtaş", "mother": "", "note": "Mardin beyi, Malabadi Köprüsü'nü tamamlayan melik", "certainty": "kesin"},
          {"name": "Süleyman", "mother": "", "note": "Halep valisi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Ager Sanguinis (Kanlı Meydan Muharebesi)", "when": "1119", "foe": "Antakya Haçlı Prensliği (Prinkeps Roger)", "result": "zafer", "note": "Haçlı ordusu imha edildi, Roger savaş meydanında öldürüldü, yüzlerce şövalye esir alındı."}
        ],
        "legends": ["Haçlı kronikçileri Walter the Chancellor ve William of Tyre onun adını dehşet ve hayranlıkla anar."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, İLGAZİ, Necmeddin", "url": "https://islamansiklopedisi.org.tr/ilgazi-necmeddin"}
        ]
      },
      {
        "id": "artuklu-sokmen",
        "name": "Muînüddin Sökmen",
        "aliases": ["Sökmen b. Artuk"],
        "title": "Emir / Muînüddin",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1104,
        "deathNote": "Haçlı seferi yolunda Karyeteyn'de vefat etti",
        "reign": [1102, 1104],
        "reignNote": "Hasankeyf kolunun kurucusu.",
        "summary": "Artuk Bey'in oğlu. Kudüs valiliği yaptıktan sonra Hasankeyf'te beyliğini kurdu. 1104 Harran Muharebesi'nde Çökürmüş ile birleşerek Urfa Haçlı Kontu II. Baudouin'i esir aldı ve Haçlıların Fırat doğusuna geçişini ebediyen kesti.",
        "traits": ["Gazi", "Stratejist"],
        "contribution": "Harran Zaferi ile Haçlıların Musul ve Bağdat'a yürümesini önledi.",
        "harm": "Erken ölümü beyliğin toparlanma sürecini yavaşlattı.",
        "wives": [],
        "children": [
          {"name": "İbrâhim", "mother": "", "note": "Hasankeyf meliki", "certainty": "kesin"},
          {"name": "Dâvud", "mother": "", "note": "Hasankeyf meliki", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Harran (Belih Çayı) Muharebesi", "when": "1104", "foe": "Haçlı Kontlukları (Urfa Kontu Baudouin ve Antakya Kontu Bohemund)", "result": "zafer", "note": "Haçlı ordusu dağıtıldı, Baudouin esir edildi, Urfa Haçlı Kontluğu ölümcül darbe aldı."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ARTUKLULAR", "url": "https://islamansiklopedisi.org.tr/artuklular"}
        ]
      }
    ]
  },
  {
    "id": "ahlatsah",
    "name": "Ahlatşahlar",
    "short": "Ahlatşahlar (Sökmenliler)",
    "aliases": ["Ermenşahlar", "Sökmeniyye Devleti"],
    "region": "anadolu",
    "start": 1100,
    "end": 1207,
    "startNote": "Sökmen el-Kutbî'nin Ahlat ve Van Gölü çevresinde beyliğini kurmasıyla temellendi.",
    "endNote": "1207 yılında Eyyûbîlerin Ahlat'ı zaptetmesiyle tarih sahnesinden çekildi.",
    "capital": "Ahlat",
    "religion": "İslamiyet (Sünnî-Hanefî)",
    "confidence": "kayit",
    "confidenceNote": "İbnü'l-Esîr, Râvendî ve Ahlat Selçuklu Meydan Mezarlığı taş kitabeleriyle sabittir.",
    "summary": "Van Gölü havzasında (Ahlat, Erciş, Adilcevaz, Van, Bitlis, Malazgirt) hüküm süren Türk devleti. Selçuklu emiri Sökmen el-Kutbî tarafından kuruldu. Başkent Ahlat 'Kubbetü'l-İslam' (İslam'ın Kubbesi) unvanını aldı; yüz binlerce nüfusu, zengin tüccarları ve devasa mezar taşlarıyla dünyanın en büyük Türk nekropolünü meydana getirdi. Gürcülere karşı Doğu Anadolu'yu savundular.",
    "legacy": "Dünyanın en büyük tarihi İslam mezarlığı olan Ahlat Selçuklu Meydan Mezarlığı'ndaki abidevi şahideleri, kümbetleri ve zengin taş işçiliği ekolünü miras bıraktı.",
    "essay": [
      "Ahlatşahlar, Büyük Selçuklu veliahtı Kutbeddin İsmail'in kölesi (gulâmı) olan Sökmen el-Kutbî tarafından 1100 yılında Van Gölü kıyısındaki Ahlat merkez yapılarak kuruldu.",
      "II. Sökmen (1128-1185) dönemi Ahlat'ın en mamur ve zengin çağı oldu. Şehir sanatkârlar, hattatlar ve taş yontucularıyla doldu; 'Kubbetü'l-İslam' sıfatını Belh ve Buhara ile paylaştı. Ahlat mezar taşları birer heykel zarafetinde işlendi. II. Sökmen'in çocuksuz vefatı üzerine idare memlük kumandanların eline geçti; iç çekişmeleri fırsat bilen Eyyûbîler 1207'de şehri işgal etti."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, AHLATŞAHLAR", "url": "https://islamansiklopedisi.org.tr/ahlat-sahlar"}
    ],
    "rulers": [
      {
        "id": "ahlatsah-sokmen",
        "name": "Sökmen el-Kutbî",
        "aliases": ["I. Sökmen", "Ahlatşah Sökmen"],
        "title": "Şah / Emir",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1111,
        "deathNote": "Haçlı seferinden dönerken hastalanarak vefat etti",
        "reign": [1100, 1111],
        "reignNote": "11 yıl hüküm sürdü.",
        "summary": "Ahlatşahlar Devleti'nin kurucusu. Van Gölü havzasını tek bayrak altında topladı. Haçlılara karşı Suriye'deki cihat ordularına katılarak büyük kahramanlıklar gösterdi.",
        "traits": ["Gazi", "Şehir kurucu", "Cesur"],
        "contribution": "Van Gölü havzasında zengin bir Türk medeniyet odağı kurdu.",
        "harm": "Kayıtlarda belirgin bir zararı geçmez.",
        "wives": [],
        "children": [
          {"name": "Zahîreddîn İbrâhim", "mother": "", "note": "İkinci hükümdar", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Tel Bâşir Kuşatması", "when": "1108", "foe": "Haçlılar (Joscelin)", "result": "zafer", "note": "Haçlı garnizonu mağlup edildi."}
        ],
        "legends": [],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, AHLATŞAHLAR", "url": "https://islamansiklopedisi.org.tr/ahlat-sahlar"}
        ]
      }
    ]
  },
  {
    "id": "caka-beyligi",
    "name": "Çaka Beyliği",
    "short": "Çaka Beyliği",
    "aliases": ["İzmir Türk Beyliği"],
    "region": "anadolu",
    "start": 1081,
    "end": 1093,
    "startNote": "Çaka Bey'in Bizans esaretinden kurtulup 1081'de İzmir'i fethederek ilk Türk donanmasını kurmasıyla başladı.",
    "endNote": "1093 yılında damadı Anadolu Selçuklu Sultanı I. Kılıç Arslan tarafından bir ziyafette öldürülmesiyle yıkıldı.",
    "capital": "İzmir (Smyrna)",
    "religion": "İslamiyet (Sünnî)",
    "confidence": "kayit",
    "confidenceNote": "Anna Komnena'nın Alexiad eseriyle en ince ayrıntısına kadar belgelidir.",
    "summary": "Tarihteki ilk Türk denizcisi ve amirali kabul edilen Çaka Bey tarafından İzmir merkezli kurulan beylik. 40 parçalık ilk Türk donanmasını inşa ederek Urla, Foça, Midilli, Sakız, Sisam ve Rodos adalarını fethetti. 1090 yılında Koyun Adaları Deniz Muharebesi'nde Bizans donanmasını hezimete uğratarak tarihteki ilk Türk deniz zaferini kazandı. İstanbul'u Peçenekler ile ortaklaşa fethetmeyi planlarken Bizans İmparatoru Aleksios Komnenos'un entrikası sonucu damadı I. Kılıç Arslan tarafından öldürüldü.",
    "legacy": "Türk Deniz Kuvvetleri'nin kuruluş tarihi kabul edilen 1081 yılını ve ilk Türk amiralliği mirasını tarihe hediye etti.",
    "essay": [
      "Çaka Bey, Malazgirt Zaferi sonrası Batı Anadolu akınlarına katılan bir Türkmen beyi iken 1078 civarında Bizans kumandanı Kabalika Aleksandros'a esir düşerek İstanbul'a saraya götürüldü. Burada Yunancayı ve Bizans saray entrikalarını, denizcilik ve gemi yapım tekniklerini öğrendi. İmparator Botaneiates ona 'protonobilissimos' unvanı verdi.",
      "1081'de I. Aleksios Komnenos tahta çıkınca rütbeleri elinden alınan Çaka Bey İstanbul'dan kaçarak İzmir'e geldi. İzmir'i fethedip burada bir tersane kurdu ve 40 parçalık kürekli ve yelkenli ilk Türk donanmasını inşa etti. Bu tarih (1081), modern Türk Deniz Kuvvetleri'nin de resmi kuruluş yılıdır.",
      "Çaka Bey Ege Denizi'ne açılarak Klazomenai (Urla), Phokaia (Foça) limanlarını ve Sakız, Midilli, Sisam adalarını fethetti. 19 Mayıs 1090'da Sakız açıklarında Koyun Adaları Deniz Muharebesi'nde Bizans Amiralı Niketas Kastamonites komutasındaki donanmayı ağır bir yenilgiye uğrattı. Kendisine 'İmparator' (Basileus) unvanı veren Çaka Bey, Trakya'daki Peçenek Türkleriyle anlaşarak İstanbul'u denizden ve karadan kuşatma planı yaptı. Ancak Bizans İmparatoru Aleksios, Anadolu Selçuklu Sultanı I. Kılıç Arslan'a mektup yazarak Çaka Bey'in onu tahtından edeceğini fısıldadı; 1093'te Abydos kuşatması sırasında Kılıç Arslan kayınpederi Çaka Bey'i bir ziyafette kılıçla öldürttü ve beylik dağıldı."
    ],
    "sources": [
      {"title": "TDV İslâm Ansiklopedisi, ÇAKA BEY", "url": "https://islamansiklopedisi.org.tr/caka-bey"},
      {"title": "Britannica, Tzachas", "url": "https://www.britannica.com/biography/Tzachas"}
    ],
    "rulers": [
      {
        "id": "caka-bey",
        "name": "Çaka Bey",
        "aliases": ["Tzachas", "Çaka Gazi"],
        "title": "Emir / İlk Türk Amirali",
        "birth": None,
        "birthNote": "Kayıtlarda yok",
        "death": 1093,
        "deathNote": "Abydos'ta I. Kılıç Arslan tarafından bir ziyafette katledildi",
        "reign": [1081, 1093],
        "reignNote": "12 yıl boyunca Ege'ye hükmetti.",
        "summary": "İlk Türk denizcisi ve amirali. İzmir'de ilk Türk donanmasını inşa etti. Ege adalarını fethetti, 1090 Koyun Adaları zaferiyle Bizans donanmasını yendi. İstanbul'u fethetmeyi tasarlarken Bizans entrikasıyla katledildi.",
        "traits": ["Öncü denizci", "Dahi amiral", "Stratejist"],
        "contribution": "Türklere denizcilik ufkunu kazandırdı; ilk Türk tersanesini ve donanmasını kurdu.",
        "harm": "Hedeflerini çok erken aşamada açık etmesi Bizans ve Selçukluları kendisine karşı birleştirdi.",
        "wives": [],
        "children": [
          {"name": "Ayşe Hatun", "mother": "", "note": "I. Kılıç Arslan ile evlendi", "certainty": "kesin"}
        ],
        "wars": [
          {"name": "Koyun Adaları Deniz Muharebesi", "when": "1090", "foe": "Bizans İmparatorluk Donanması (Kastamonites)", "result": "zafer", "note": "Tarihteki ilk Türk deniz zaferi kazanıldı, Bizans donanması yok edildi."},
          {"name": "Midilli ve Sakız Seferleri", "when": "1089", "foe": "Bizans Ege garnizonları", "result": "zafer", "note": "Ege adaları Türk hakimiyetine girdi."}
        ],
        "legends": ["Bizans prensesi Anna Komnena'nın Alexiad adlı eserinde Çaka Bey'in denizdeki cüreti ve savaş zekası korkuyla karışık bir hayranlıkla anlatılır."],
        "sources": [
          {"title": "TDV İslâm Ansiklopedisi, ÇAKA BEY", "url": "https://islamansiklopedisi.org.tr/caka-bey"}
        ]
      }
    ]
  }
]

out = Path("/Users/hayabusa/turk-tarih-atlasi/data/raw/l-anadolu-selcuklu.json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(data)} states to {out}")
