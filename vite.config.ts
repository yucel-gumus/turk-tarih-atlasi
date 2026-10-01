import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
  // Üretimde ve önizlemede site GitHub Pages alt yolu (/turk-tarih-atlasi/)
  // üzerinden çalışır; hem dev hem build hem preview aynı base'i kullanır.
  base: '/turk-tarih-atlasi/',
  plugins: [svelte()],
  server: {
    port: 5173,
    host: true,
  },
  preview: {
    port: 4173,
    strictPort: true,
  },
  build: {
    target: 'esnext',
    assetsInlineLimit: 4096,
  },
});
