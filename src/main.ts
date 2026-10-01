import { mount } from 'svelte';
import './app.css';
import App from './App.svelte';
import { preloadAtlas } from './lib/data/atlas';

const target = document.getElementById('app');
if (!target) {
  throw new Error('Atlas kök elemanı (#app) dokümanda bulunamadı.');
}

/**
 * Veri, arayüz bağlanmadan önce yüklenir. `data/raw/*.json` dosyaları ayrı
 * parçalar hâlinde paralel indiği için bu bekleme kısadır; sonrasında bütün
 * sayfalar senkron çalışır (`atlasIndex()` önbellekten okur).
 */
async function bootstrap(): Promise<void> {
  await preloadAtlas();
  mount(App, { target: target as HTMLElement });
}

void bootstrap();
