import { defineConfig, devices } from '@playwright/test';
import fs from 'node:fs';
const chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  workers: 2,
  retries: 0,
  reporter: [['list'], ['html', { open: 'never' }]],
  use: {
    baseURL: process.env.ATLAS_BASE_URL ?? 'http://127.0.0.1:4173/turk-tarih-atlasi/',
    trace: 'retain-on-failure',
    launchOptions: fs.existsSync(chrome) ? { executablePath: chrome } : {},
  },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile', use: { ...devices['Pixel 7'], viewport: { width: 390, height: 844 } } },
  ],
  webServer: process.env.ATLAS_BASE_URL ? undefined : {
    command: 'npm run preview -- --host 127.0.0.1',
    url: 'http://127.0.0.1:4173/turk-tarih-atlasi/',
    reuseExistingServer: !process.env.CI,
  },
});
