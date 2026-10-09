import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs';
import { slug } from '../../src/lib/text';
const raw = JSON.parse(fs.readFileSync('data/raw/o-osmanli.json', 'utf8'));
const ottoman = (Array.isArray(raw) ? raw : [raw])[0];
const ruler = ottoman.rulers.find((r: any) => r.wars?.length && r.wives?.length);
const baseRuler = `#/devlet/osmanli/hukumdar/${ruler.id}`;
const routes = ['#/', '#/rehber', '#/savaslar', '#/zaman-makinesi/1453', '#/harita', '#/arama?q=osmanli', '#/devlet/osmanli', baseRuler, `${baseRuler}/savas/1-${slug(ruler.wars[0].name)}`, `${baseRuler}/kisi/es/1-${slug(ruler.wives[0].name)}`, '#/missing'];

for (const hash of routes) {
  test(`page, layout and accessibility ${hash}`, async ({ page }) => {
    const errors: string[] = [];
    page.on('pageerror', e => errors.push(e.message));
    await page.goto(hash);
    await expect(page.locator('main')).toBeVisible();
    await expect(page.locator('h1')).toBeVisible();
    if (hash === '#/harita') {
      await expect(page.locator('.leaflet-container')).toBeVisible();
      await expect(page.locator('.atlas-base-land')).toHaveCount(177);
    }
    const layout = await page.evaluate(() => {
      const main = document.querySelector('main')!.firstElementChild!.getBoundingClientRect();
      const header = document.querySelector('header')!.getBoundingClientRect();
      const clipped = [...document.querySelectorAll('main input, main .battle-card, main .current-year-badge')].filter(el => {
        const r = el.getBoundingClientRect(); return r.width && (r.left < -1 || r.right > innerWidth + 1);
      }).map(el => el.className);
      return { mainTop: main.top, headerBottom: header.bottom, clipped };
    });
    expect(layout.mainTop).toBeGreaterThanOrEqual(layout.headerBottom);
    expect(layout.clipped).toEqual([]);
    const audit = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
    expect(audit.violations.map(v => ({ id: v.id, nodes: v.nodes.map(n => n.target) }))).toEqual([]);
    expect(errors).toEqual([]);
  });
}

test('search filters remain usable after query changes', async ({ page }) => {
  await page.goto('#/arama?q=osmanli');
  await page.getByRole('button', { name: /^Çocuk ·/ }).click();
  await page.evaluate(() => { location.hash = '#/arama?q=malazgirt'; });
  await expect(page.getByRole('button', { name: /^Tümü ·/ })).toHaveAttribute('aria-pressed', 'true');
  await expect(page.locator('.result-item').first()).toBeVisible();
});

test('year address, refresh and BCE transition', async ({ page }) => {
  await page.goto('#/zaman-makinesi/1453');
  await page.getByRole('button', { name: '1 Yıl İleri', exact: true }).click();
  await expect(page).toHaveURL(/zaman-makinesi\/1454$/);
  await page.reload();
  await expect(page.locator('.year-huge')).toHaveText('1454');
  await page.goto('#/zaman-makinesi/-1');
  await page.getByRole('button', { name: '1 Yıl İleri', exact: true }).click();
  await expect(page.locator('.year-huge')).toHaveText('1');
});

test('uncertain result filter includes both result types', async ({ page }) => {
  await page.goto('#/savaslar');
  const filter = page.getByRole('button', { name: /^Belirsiz \(/ });
  const count = Number((await filter.innerText()).match(/\d+/)![0]);
  await filter.click();
  await expect(page.locator('.result-count b')).toHaveText(String(count));
});

test('map list resolves overlapping markers and clears stale selection', async ({ page }) => {
  await page.goto('#/harita');
  const list = page.locator('.map-state-list');
  await expect(list.locator('button')).toHaveCount(80);
  await list.getByRole('button', { name: /^Osmanlı/ }).click();
  await expect(page.locator('.drawer-title')).toContainText('Osmanlı');
  await page.getByRole('button', { name: /Bozkır ve İç Asya/ }).click();
  await expect(page.locator('.active-state-drawer')).toHaveCount(0);
  await page.getByRole('link', { name: 'Şerit', exact: true }).click();
  await expect(page.locator('h1')).toHaveText('Türk Devletleri Atlası');
});

test('keyboard search and skip navigation', async ({ page }) => {
  await page.goto('#/');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link', { name: 'İçeriğe geç' })).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.locator('main')).toBeFocused();
  const search = page.getByRole('combobox', { name: 'Atlasta ara' });
  await search.fill('osmanli');
  await expect(page.getByRole('listbox')).toBeVisible();
  await search.press('Escape');
  await expect(search).toBeFocused();
  await expect(page.getByRole('listbox')).toHaveCount(0);
  await search.fill('osmanli');
  await search.press('Enter');
  await expect(page).toHaveURL(/devlet\/osmanli$/);
});

test('data chunk failure displays a recovery action', async ({ page }) => {
  await page.route('**/assets/o-osmanli-*.js', route => route.abort());
  await page.goto('#/');
  await expect(page.getByRole('heading', { name: 'Atlas Yüklenemedi' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Yeniden Dene' })).toBeVisible();
});

test('local basemap failure leaves list and navigation operational', async ({ page }) => {
  await page.route('**/assets/world.geo-*.json', route => route.abort());
  await page.goto('#/harita');
  await expect(page.getByRole('status')).toContainText('Harita zemini');
  await page.locator('.map-state-list').getByRole('button', { name: /^Osmanlı/ }).click();
  await expect(page.locator('.drawer-link-btn')).toBeVisible();
  await page.getByRole('link', { name: 'Savaşlar', exact: true }).click();
  await expect(page.locator('h1')).toContainText('Büyük Savaşlar');
});

test('family search avoids claiming enthronement from partial names', async ({ page }) => {
  await page.goto('#/devlet/osmanli');
  await page.getByRole('button', { name: 'Hanedan Soyağacı' }).click();
  const input = page.getByRole('searchbox', { name: 'Hanedan aile kayıtlarında ara' });
  await input.fill('mehmed');
  await expect(page.locator('.tree-node').first()).toBeVisible();
  await expect(page.getByText('Tahta Çıktı', { exact: true })).toHaveCount(0);
  const audit = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa']).analyze();
  expect(audit.violations.map(v => v.id)).toEqual([]);
});

test('small mobile controls fit at 320 pixels', async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 740 });
  await page.goto('#/zaman-makinesi/-209');
  const box = await page.locator('.year-display-row').boundingBox();
  const children = await page.locator('.year-display-row').evaluate(el => [...el.children].map(child => {
    const r = child.getBoundingClientRect(); return { left: r.left, right: r.right };
  }));
  expect(box).not.toBeNull();
  expect(children.every(r => r.left >= 0 && r.right <= 320)).toBe(true);
});

test('timeline shortcuts leave other keyboard controls alone', async ({ page }) => {
  await page.goto('#/');
  const search = page.getByRole('combobox', { name: 'Atlasta ara' });
  await search.focus();
  await search.press('0');
  await expect(search).toHaveValue('0');
  await page.locator('.timeline-scroll').focus();
  await page.locator('.timeline-scroll').press('+');
  await expect(page.locator('.timeline-surface')).toHaveCSS('width', /px/);
});
