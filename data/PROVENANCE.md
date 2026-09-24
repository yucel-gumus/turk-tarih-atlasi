# Veri Köken ve Yaşam Döngüsü Haritası (Data Provenance)

Bu doküman, `data/raw/*.json` dosyalarının kökenini, üretim betiklerini (`tools/gen_*.py`), çekirdek taslakları (`data/base/`) ve harici kaynakları (`data/sources/`) belgeler.

---

## 1. Ham Veri Dosyaları ve Üretim Durumu

| Ham Dosya (`data/raw/`) | Devlet Sayısı | Hükümdar | Üretici Betik (`tools/`) | Durum & Notlar |
|---|---|---|---|---|
| `a-giris.json` | 1 | 0 | *Yok (El ile yazıldı)* | Giriş / Okuma yönergesi kartı (`id: okuma`). |
| `a-bati.json` | 9 | 36 | *Yok (El ile yazıldı)* | Avrupa Hun, Avar, Hazar, Bulgar, Peçenek, Kıpçak. |
| `b-bozkir-hun.json` | 3 | 50 | *Yok (data/base türevi)* | `data/base/asya-hun.json` genişletilerek üretildi. ID şeması farklılaştırıldı (`asya-hun-teoman`). |
| `c-gokturk.json` | 6 | 19 | `gen_c_gokturk.py` | Göktürk kağanlıkları, Türgiş, Karluk. Python literalinden üretildi. |
| `d-uygur-kirgiz.json` | 3 | 21 | *Yok (El ile yazıldı)* | Uygur, Yenisey Kırgız, Kimek konfederasyonu. |
| `e-turkistan-islam.json`| 3 | 9 | `gen_e_turkistan.py` | Karahanlı, Gazneli, Harzemşah. Metin kaynakları `data/sources/e-turkistan-islam/` içinde. |
| `f-altin-orda.json` | 4 | 11 | `gen_fg_kuzey.py` | Altın Orda, Kazak, Nogay, Ak Orda. |
| `g-kuzey-hanliklari.json`| 6 | 12 | `gen_fg_kuzey.py` | Kırım, Kazan, Astrahan, Sibir, Kasım, Delhi. |
| `h-timur-ortaasya.json` | 6 | 8 | `gen_h_timur.py` | Timur, Bâbür, Özbek, Buhara, Hive, Hokand. |
| `i-iran-selcuklu.json` | 5 | 14 | `gen_i_selcuklu.py` | Büyük Selçuklu, İldeniz, Salgur, Tolun, İhşid. Kaynaklar `data/sources/i-iran-selcuklu/`. |
| `j-iran-gec.json` | 5 | 8 | `gen_j_iran.py` | Akkoyunlu, Karakoyunlu, Safevî, Avşar, Kaçar. |
| `k-ilhanli-memluk.json` | 5 | 23 | `gen_k_ilhanli.py` *(kırık)* | İlhanlı, Memlük, Zengî, Eftalit, Celâyirli. Mevcut dosya nihai kaynaktır; betik `data/states/` aradığı için kırıktı. |
| `l-anadolu-selcuklu.json`| 7 | 13 | `gen_l_anadolu.py` | Anadolu Selçuklu, Dânişmendli, Saltuklu, Mengücek, Artuklu, Ahlatşah, Çaka. |
| `m-beylikler-bati.json` | 8 | 46 | *Yok (El ile yazıldı)* | Batı Anadolu Beylikleri (Karesi, Saruhan, Aydın, Menteşe, Germiyan, Hamid, Eşref, Teke). |
| `n-beylikler-dogu.json` | 5 | 10 | `gen_n_dogu.py` | Karaman, Dulkadir, Ramazan, Candar, Eretna. |
| `o-osmanli.json` | 1 | 40 | *Yok (data/base türevi)* | `data/base/osmanli.json` çekirdeği 36 padişah + 4 taht iddiacısına genişletildi. |
| **TOPLAM** | **77** | **320** | **9 betik / 7 el/çekirdek** | **473 savaş, 149 eş, 474 çocuk** |

---

## 2. Çekirdek Taslaklar (`data/base/`) — Neden Saklanmalı?

- `data/base/asya-hun.json` ve `data/base/osmanli.json`, projenin ilk aşamasında oluşturulmuş prototip şemadır.
- **Kimlik Farkı (ID Schema):** `data/base` dosyalarında ID'ler yalındır (`teoman`, `mete`, `osman-gazi`, `orhan-gazi`). `data/raw/` dosyalarında ise blok ve hanedan ön ekli veya sıra numaralıdır (`asya-hun-teoman`, `osman-1`).
- Bu dosyalar raw'ın bir alt kümesi değil, projenin kurucu metin varyantlarıdır; silinmemeli ve arşiv olarak korunmalıdır.

---

## 3. Kaynak ve Atıf Durumu (`data/sources/`)

- Projedeki 608 toplam kaynak referansının dağılımı:
  - **TDV İslâm Ansiklopedisi:** 450 kaynak (~%74)
  - **Vikipedi (CC BY-SA 4.0):** 96 kaynak (~%16)
  - **Encyclopaedia Britannica:** 62 kaynak (~%10)
- Yerel metin arşivleri:
  - `data/sources/e-turkistan-islam/` (29 kaynak metni / HTML dökümü + `SOURCES.md`)
  - `data/sources/i-iran-selcuklu/` (19 kaynak metni / ham JSON + `SOURCES.md`)
- Kalan 14 blokta metinler `data/raw/*.json` içindeki `sources` dizisinde doğrudan URL ve başlık olarak tutulmaktadır.

---

## 4. Kalite Kapısı ve Derleme Zinciri

```
data/raw/*.json ──► tools/validate.py (Şema, tipler, URL, kesinlik kontrolü)
                         │
                         ▼ (Exit code 0 ise)
                    tools/build.py (Sıralama, sha256 özeti, tarih damgası)
                         │
                         ▼
                    data/atlas.js (window.ATLAS globali)
```

1. **Doğrulama:** `python3 tools/validate.py data/raw/*.json` (0 hata zorunludur).
2. **Derleme:** `python3 tools/build.py` (atlas.js başlığına SHA256 ve kaynak verilerin son güncelleme zaman damgasını işler; uyarı durumunda çıkış kodu 1 verir).
