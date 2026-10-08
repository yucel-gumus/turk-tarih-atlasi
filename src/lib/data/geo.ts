import type { State } from '../../schemas/atlas.schema';
import { atlasIndex } from './lookup';

export interface StateGeoPoint {
  stateId: string;
  capitalName: string;
  lat: number;
  lon: number;
  modernCountry: string;
  note?: string;
}

// Bütün 80 Türk devletinin başkent ve odak coğrafi koordinatları
export const STATE_GEO_POINTS: Record<string, StateGeoPoint> = {
  // a-bati
  'avrupa-hun': { stateId: 'avrupa-hun', capitalName: 'Tisa / Pannonia (Macaristan ovası)', lat: 46.8, lon: 19.8, modernCountry: 'Macaristan' },
  'avar-kaganligi': { stateId: 'avar-kaganligi', capitalName: 'Avar Ringi (Pannonia)', lat: 47.1, lon: 19.2, modernCountry: 'Macaristan' },
  'hazar-kaganligi': { stateId: 'hazar-kaganligi', capitalName: 'İtil / Sarkel', lat: 46.3, lon: 47.9, modernCountry: 'Rusya (Hazar kıyısı)' },
  'buyuk-bulgarya': { stateId: 'buyuk-bulgarya', capitalName: 'Fanagurya (Taman)', lat: 45.2, lon: 36.9, modernCountry: 'Rusya / Kırım kıyısı' },
  'tuna-bulgar': { stateId: 'tuna-bulgar', capitalName: 'Pliska / Preslav', lat: 43.36, lon: 27.13, modernCountry: 'Bulgaristan' },
  'itil-bulgar': { stateId: 'itil-bulgar', capitalName: 'Bulgar / Bilyar', lat: 54.98, lon: 49.05, modernCountry: 'Rusya (Tataristan)' },
  'oguz-yabgu': { stateId: 'oguz-yabgu', capitalName: 'Yenikent (Cend/Seyhun)', lat: 45.5, lon: 62.1, modernCountry: 'Kazakistan' },
  'pecenek': { stateId: 'pecenek', capitalName: 'Dinyeper-Don Yaylakları', lat: 48.2, lon: 35.5, modernCountry: 'Ukrayna' },
  'kipcak-kuman': { stateId: 'kipcak-kuman', capitalName: 'Deşt-i Kıpçak Ordugâhı', lat: 47.8, lon: 38.0, modernCountry: 'Ukrayna / Rusya Bozkırı' },

  // b-bozkir-hun
  'asya-hun': { stateId: 'asya-hun', capitalName: 'Ötüken / Orhun', lat: 47.5, lon: 102.8, modernCountry: 'Moğolistan' },
  'guney-hun': { stateId: 'guney-hun', capitalName: 'Meji (Ordos)', lat: 39.1, lon: 109.8, modernCountry: 'Çin (İç Moğolistan)' },
  'kuzey-hun': { stateId: 'kuzey-hun', capitalName: 'Orhun / Altay boyu', lat: 48.0, lon: 90.5, modernCountry: 'Moğolistan / Kazakistan' },

  // c-gokturk
  'gokturk': { stateId: 'gokturk', capitalName: 'Ötüken', lat: 47.5, lon: 102.8, modernCountry: 'Moğolistan' },
  'dogu-gokturk': { stateId: 'dogu-gokturk', capitalName: 'Ötüken', lat: 47.5, lon: 102.8, modernCountry: 'Moğolistan' },
  'bati-gokturk': { stateId: 'bati-gokturk', capitalName: 'Suyab / Çu Vadisi', lat: 42.8, lon: 75.2, modernCountry: 'Kırgızistan' },
  'ikinci-gokturk': { stateId: 'ikinci-gokturk', capitalName: 'Ötüken', lat: 47.5, lon: 102.8, modernCountry: 'Moğolistan' },
  'turges': { stateId: 'turges', capitalName: 'Suyab / Balasagun', lat: 42.75, lon: 75.25, modernCountry: 'Kırgızistan' },
  'karluk': { stateId: 'karluk', capitalName: 'Suyab / Taraz', lat: 42.9, lon: 71.37, modernCountry: 'Kazakistan' },

  // d-uygur-kirgiz
  'uygur-kaganligi': { stateId: 'uygur-kaganligi', capitalName: 'Karabalgasun', lat: 47.43, lon: 102.65, modernCountry: 'Moğolistan' },
  'yenisey-kirgiz': { stateId: 'yenisey-kirgiz', capitalName: 'Yenisey Boyu (Hakasya)', lat: 53.7, lon: 91.4, modernCountry: 'Rusya (Sibirya)' },
  'kimek': { stateId: 'kimek', capitalName: 'İmiş / İrtiş Boyu', lat: 52.3, lon: 76.9, modernCountry: 'Kazakistan' },
  'idikut-uygur': { stateId: 'idikut-uygur', capitalName: 'Koço / Turfan', lat: 42.95, lon: 89.18, modernCountry: 'Doğu Türkistan' },

  // e-turkistan-islam
  'karahanli': { stateId: 'karahanli', capitalName: 'Balasagun / Kaşgar', lat: 39.47, lon: 75.99, modernCountry: 'Kırgızistan / Doğu Türkistan' },
  'gazneli': { stateId: 'gazneli', capitalName: 'Gazne / Lahor', lat: 33.55, lon: 68.42, modernCountry: 'Afganistan' },
  'harzemsah': { stateId: 'harzemsah', capitalName: 'Gürgenç (Köhne Ürgenç)', lat: 42.3, lon: 59.15, modernCountry: 'Türkmenistan' },

  // f-altin-orda
  'altin-orda': { stateId: 'altin-orda', capitalName: 'Saray Batu / Saray Berke', lat: 47.15, lon: 48.05, modernCountry: 'Rusya (Aşağı İdil)' },
  'kazak-hanligi': { stateId: 'kazak-hanligi', capitalName: 'Sığnak / Türkistan', lat: 43.3, lon: 68.27, modernCountry: 'Kazakistan' },
  'nogay-ordasi': { stateId: 'nogay-ordasi', capitalName: 'Saraycık (Yayık boyu)', lat: 47.05, lon: 51.65, modernCountry: 'Kazakistan' },
  'ak-orda': { stateId: 'ak-orda', capitalName: 'Sığnak', lat: 43.3, lon: 68.27, modernCountry: 'Kazakistan' },

  // g-kuzey-hanliklari
  'kirim-hanligi': { stateId: 'kirim-hanligi', capitalName: 'Bahçesaray', lat: 44.75, lon: 33.86, modernCountry: 'Kırım' },
  'kazan-hanligi': { stateId: 'kazan-hanligi', capitalName: 'Kazan', lat: 55.79, lon: 49.12, modernCountry: 'Rusya (Tataristan)' },
  'astrahan-hanligi': { stateId: 'astrahan-hanligi', capitalName: 'Hacıtarhan (Astrahan)', lat: 46.35, lon: 48.04, modernCountry: 'Rusya' },
  'sibir-hanligi': { stateId: 'sibir-hanligi', capitalName: 'Kaşlık / Sibir', lat: 58.2, lon: 68.25, modernCountry: 'Rusya (Batı Sibirya)' },
  'kasim-hanligi': { stateId: 'kasim-hanligi', capitalName: 'Kasimov (Oka boyu)', lat: 54.94, lon: 41.4, modernCountry: 'Rusya' },
  'delhi-turk-sultanligi': { stateId: 'delhi-turk-sultanligi', capitalName: 'Delhi', lat: 28.61, lon: 77.21, modernCountry: 'Hindistan' },

  // h-timur-ortaasya
  'timur-imparatorlugu': { stateId: 'timur-imparatorlugu', capitalName: 'Semerkant / Herat', lat: 39.65, lon: 66.97, modernCountry: 'Özbekistan' },
  'babur-imparatorlugu': { stateId: 'babur-imparatorlugu', capitalName: 'Agra / Delhi / Lahor', lat: 27.18, lon: 78.01, modernCountry: 'Hindistan' },
  'ozbek-hanligi': { stateId: 'ozbek-hanligi', capitalName: 'Semerkant / Buhara', lat: 39.65, lon: 66.97, modernCountry: 'Özbekistan' },
  'buhara-hanligi': { stateId: 'buhara-hanligi', capitalName: 'Buhara', lat: 39.77, lon: 64.42, modernCountry: 'Özbekistan' },
  'hive-hanligi': { stateId: 'hive-hanligi', capitalName: 'Hive', lat: 41.38, lon: 60.36, modernCountry: 'Özbekistan' },
  'hokand-hanligi': { stateId: 'hokand-hanligi', capitalName: 'Hokand', lat: 40.53, lon: 70.94, modernCountry: 'Özbekistan (Fergana)' },
  'cagatay-hanligi': { stateId: 'cagatay-hanligi', capitalName: 'Almalık (İli Vadisi)', lat: 44.15, lon: 80.7, modernCountry: 'Doğu Türkistan / Kazakistan sınırı' },

  // i-iran-selcuklu
  'buyuk-selcuklu': { stateId: 'buyuk-selcuklu', capitalName: 'Nişabur / Rey / İsfahan', lat: 32.65, lon: 51.67, modernCountry: 'İran' },
  'ildenizli': { stateId: 'ildenizli', capitalName: 'Tebriz / Nahçıvan / Hemedan', lat: 38.08, lon: 46.29, modernCountry: 'İran (Azerbaycan)' },
  'salgurlu': { stateId: 'salgurlu', capitalName: 'Şiraz (Fars)', lat: 29.59, lon: 52.58, modernCountry: 'İran' },
  'tulun': { stateId: 'tulun', capitalName: 'Katai (Kahire)', lat: 30.03, lon: 31.25, modernCountry: 'Mısır' },
  'ihsid': { stateId: 'ihsid', capitalName: 'Fustat (Kahire)', lat: 30.01, lon: 31.23, modernCountry: 'Mısır' },
  'kirman-selcuklu': { stateId: 'kirman-selcuklu', capitalName: 'Berdesîr (Kirman)', lat: 30.28, lon: 57.08, modernCountry: 'İran' },
  'suriye-selcuklu': { stateId: 'suriye-selcuklu', capitalName: 'Dımaşk (Şam) / Halep', lat: 33.51, lon: 36.29, modernCountry: 'Suriye' },

  // j-iran-gec
  'akkoyunlu': { stateId: 'akkoyunlu', capitalName: 'Diyarbekir / Tebriz', lat: 38.08, lon: 46.29, modernCountry: 'İran / Türkiye' },
  'karakoyunlu': { stateId: 'karakoyunlu', capitalName: 'Erciş / Tebriz', lat: 38.08, lon: 46.29, modernCountry: 'İran / Türkiye' },
  'safevi': { stateId: 'safevi', capitalName: 'Tebriz / Kazvin / İsfahan', lat: 32.65, lon: 51.67, modernCountry: 'İran' },
  'avsar': { stateId: 'avsar', capitalName: 'Meşhed', lat: 36.3, lon: 59.6, modernCountry: 'İran' },
  'kacar': { stateId: 'kacar', capitalName: 'Tahran', lat: 35.69, lon: 51.39, modernCountry: 'İran' },

  // k-ilhanli-memluk
  'ilhanli': { stateId: 'ilhanli', capitalName: 'Meraga / Tebriz / Sultaniye', lat: 36.43, lon: 48.8, modernCountry: 'İran' },
  'memluk': { stateId: 'memluk', capitalName: 'Kahire', lat: 30.04, lon: 31.23, modernCountry: 'Mısır' },
  'zengi': { stateId: 'zengi', capitalName: 'Musul / Halep', lat: 36.34, lon: 43.13, modernCountry: 'Irak / Suriye' },
  'eftalit': { stateId: 'eftalit', capitalName: 'Balkh (Belh) / Badahşan', lat: 36.75, lon: 66.9, modernCountry: 'Afganistan' },
  'celayirli': { stateId: 'celayirli', capitalName: 'Bağdat / Tebriz', lat: 33.31, lon: 44.36, modernCountry: 'Irak / İran' },

  // l-anadolu-selcuklu
  'anadolu-selcuklu': { stateId: 'anadolu-selcuklu', capitalName: 'İznik / Konya', lat: 37.87, lon: 32.48, modernCountry: 'Türkiye' },
  'danismendli': { stateId: 'danismendli', capitalName: 'Sivas / Niksar', lat: 40.59, lon: 36.95, modernCountry: 'Türkiye' },
  'saltuklu': { stateId: 'saltuklu', capitalName: 'Erzurum', lat: 39.9, lon: 41.27, modernCountry: 'Türkiye' },
  'mengucek': { stateId: 'mengucek', capitalName: 'Erzincan / Divriği', lat: 39.75, lon: 39.49, modernCountry: 'Türkiye' },
  'artuklu': { stateId: 'artuklu', capitalName: 'Hasankeyf / Mardin / Harput', lat: 37.31, lon: 40.74, modernCountry: 'Türkiye' },
  'ahlatsah': { stateId: 'ahlatsah', capitalName: 'Ahlat (Van Gölü kıyısı)', lat: 38.75, lon: 42.48, modernCountry: 'Türkiye' },
  'caka-beyligi': { stateId: 'caka-beyligi', capitalName: 'Smyrna (İzmir)', lat: 38.42, lon: 27.14, modernCountry: 'Türkiye' },

  // m-beylikler-bati
  'karesi': { stateId: 'karesi', capitalName: 'Balıkesir / Bergama', lat: 39.65, lon: 27.88, modernCountry: 'Türkiye' },
  'saruhan': { stateId: 'saruhan', capitalName: 'Manisa', lat: 38.61, lon: 27.43, modernCountry: 'Türkiye' },
  'aydin': { stateId: 'aydin', capitalName: 'Birgi / Ayasuluk (Selçuk)', lat: 38.25, lon: 28.06, modernCountry: 'Türkiye' },
  'mentese': { stateId: 'mentese', capitalName: 'Milas / Peçin / Muğla', lat: 37.31, lon: 27.78, modernCountry: 'Türkiye' },
  'germiyan': { stateId: 'germiyan', capitalName: 'Kütahya', lat: 39.42, lon: 29.98, modernCountry: 'Türkiye' },
  'hamid': { stateId: 'hamid', capitalName: 'Eğirdir / Isparta / Antalya', lat: 37.87, lon: 30.85, modernCountry: 'Türkiye' },
  'esref': { stateId: 'esref', capitalName: 'Beyşehir', lat: 37.68, lon: 31.72, modernCountry: 'Türkiye' },
  'teke': { stateId: 'teke', capitalName: 'Antalya / Korkuteli', lat: 36.89, lon: 30.7, modernCountry: 'Türkiye' },

  // n-beylikler-dogu
  'karamanoglu': { stateId: 'karamanoglu', capitalName: 'Ermenek / Lârende (Karaman) / Konya', lat: 37.18, lon: 33.22, modernCountry: 'Türkiye' },
  'dulkadir': { stateId: 'dulkadir', capitalName: 'Elbistan / Maraş', lat: 38.2, lon: 37.19, modernCountry: 'Türkiye' },
  'ramazanoglu': { stateId: 'ramazanoglu', capitalName: 'Adana', lat: 37.0, lon: 35.32, modernCountry: 'Türkiye' },
  'candaroglu': { stateId: 'candaroglu', capitalName: 'Eflani / Kastamonu / Sinop', lat: 41.38, lon: 33.78, modernCountry: 'Türkiye' },
  'eretna': { stateId: 'eretna', capitalName: 'Sivas / Kayseri', lat: 39.75, lon: 37.01, modernCountry: 'Türkiye' },

  // o-osmanli
  'osmanli': { stateId: 'osmanli', capitalName: 'Söğüt / Bursa / Edirne / İstanbul', lat: 41.01, lon: 28.98, modernCountry: 'Türkiye' },
};

/**
 * Avrasya odaklı SVG projeksiyonu.
 * Enlem (Lat): 15°N ile 65°N
 * Boylam (Lon): 12°E ile 118°E
 * Genişlik: 1000px, Yükseklik: 550px
 */
export function projectGeoToSvg(
  lat: number,
  lon: number,
  width: number = 1000,
  height: number = 550
): { x: number; y: number } {
  const minLon = 12;
  const maxLon = 118;
  const minLat = 18;
  const maxLat = 62;

  // Sınır koruması
  const clampedLon = Math.max(minLon, Math.min(maxLon, lon));
  const clampedLat = Math.max(minLat, Math.min(maxLat, lat));

  const x = ((clampedLon - minLon) / (maxLon - minLon)) * width;
  const y = ((maxLat - clampedLat) / (maxLat - minLat)) * height;

  return {
    x: Math.round(x * 10) / 10,
    y: Math.round(y * 10) / 10,
  };
}

export interface GeoStateMarker {
  state: State;
  geo: StateGeoPoint;
  svgPos: { x: number; y: number };
}

export function getAllStateGeoMarkers(): GeoStateMarker[] {
  const index = atlasIndex();
  const markers: GeoStateMarker[] = [];

  for (const state of index.devletler) {
    const geo = STATE_GEO_POINTS[state.id];
    if (geo) {
      markers.push({
        state,
        geo,
        svgPos: projectGeoToSvg(geo.lat, geo.lon),
      });
    }
  }

  return markers;
}
