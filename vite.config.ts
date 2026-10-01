import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig(({ command }) => ({
  // Üretimde site bir GitHub Pages proje alt yolunda yayınlanır
  // (https://yucel-gumus.github.io/turk-tarih-atlasi/); varlık yolları bu
  // öneke göre üretilmelidir. Geliştirme sunucusu kökte kalır.
  base: command === 'build' ? '/turk-tarih-atlasi/' : '/',
  plugins: [svelte()],
  server: {
    port: 5173,
    host: true,
  },
  build: {
    target: 'esnext',
    assetsInlineLimit: 4096,
  },
}));
