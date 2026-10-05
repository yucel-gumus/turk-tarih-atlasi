import { mount } from 'svelte';
import './app.css';
import App from './App.svelte';
import { preloadAtlas } from './lib/data/atlas';

const target = document.getElementById('app');
if (!target) {
  throw new Error('Atlas kök elemanı (#app) dokümanda bulunamadı.');
}
const appRoot: HTMLElement = target;

/**
 * Veri, arayüz bağlanmadan önce yüklenir. `data/raw/*.json` dosyaları ayrı
 * parçalar hâlinde paralel indiği için bu bekleme kısadır; sonrasında bütün
 * sayfalar senkron çalışır (`atlasIndex()` önbellekten okur).
 */
async function bootstrap(): Promise<void> {
  try {
    await preloadAtlas();
    mount(App, { target: appRoot });
  } catch (err) {
    console.error('[AtlasBootstrap] Atlas verisi yüklenirken hata oluştu:', err);
    appRoot.innerHTML = `
      <div style="font-family: serif; max-width: 520px; margin: 80px auto; padding: 24px; text-align: center; border: 1px solid #d3ccbb; border-radius: 12px; background: #fffdf8; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
        <h2 style="color: #7a4d0f; margin: 0 0 10px; font-size: 20px;">Atlas Yüklenemedi</h2>
        <p style="color: #554f43; font-size: 13.5px; line-height: 1.6; margin: 0 0 18px;">Tarih kayıtları indirilirken bir ağ veya ayrıştırma hatası oluştu.</p>
        <button onclick="location.reload()" style="padding: 8px 20px; border-radius: 9999px; background: #96601a; color: #ffffff; border: none; cursor: pointer; font-size: 13px; font-weight: 600;">Yeniden Dene</button>
      </div>
    `;
  }
}

void bootstrap();
