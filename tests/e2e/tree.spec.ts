import { test, expect, type Page } from '@playwright/test';

const transform = (page: Page) =>
  page.locator('.layer').evaluate((el) => {
    const m = new DOMMatrix(getComputedStyle(el).transform);
    return { x: m.e, y: m.f, s: m.a };
  });

test('soy ağacından Osmanlı → Fâtih → savaş modallarına iner ve geri döner', async ({ page }) => {
  await page.goto('./');
  const node = page.locator('.node[data-id="osmanli"]');
  await expect(node).toBeAttached();
  await node.dispatchEvent('click');

  const top = () => page.locator('dialog[open]').last();
  await expect(top().getByRole('heading', { level: 2 })).toHaveText('Osmanlı Devleti');

  await top().getByRole('button', { name: /II\. Mehmed/ }).first().click();
  await expect(top().getByRole('heading', { level: 2 })).toHaveText('II. Mehmed');

  await top().getByRole('button', { name: /İstanbul/ }).first().click();
  await expect(top().getByRole('heading', { level: 2 })).toHaveText('İstanbul');
  await expect(top()).toContainText('Bizans');
  await expect(page.locator('dialog[open]')).toHaveCount(3);

  await page.keyboard.press('Escape');
  await expect(page.locator('dialog[open]')).toHaveCount(2);
  await page.goBack();
  await expect(page.locator('dialog[open]')).toHaveCount(1);
  await top().getByRole('button', { name: /Tümünü kapat/ }).click();
  await expect(page.locator('dialog[open]')).toHaveCount(0);
});

test('ekranda kontrol butonu yok, yazar kartı var, sayfa yatay taşmaz', async ({ page }) => {
  await page.goto('./');
  await expect(page.locator('.node').first()).toBeAttached();
  await expect(page.locator('.zoom')).toHaveCount(0);
  const author = page.getByRole('link', { name: /Yücel Gümüş/ });
  await expect(author).toBeVisible();
  await expect(author).toHaveAttribute('href', 'https://yucelgumus.dev/');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});

test('fare: sürükleme kaydırır, tekerlek imlece yakınlaşır, çift tık yakınlaşır', async ({ page, isMobile }) => {
  test.skip(isMobile, 'fare testi');
  await page.goto('./');
  await expect(page.locator('.node').first()).toBeAttached();
  const box = (await page.locator('.viewport').boundingBox())!;
  const cx = box.width / 2;
  const cy = box.height / 2 + 150;

  const a = await transform(page);
  await page.mouse.move(cx, cy);
  await page.mouse.down();
  await page.mouse.move(cx - 150, cy - 80, { steps: 6 });
  await page.mouse.up();
  const b = await transform(page);
  expect(Math.round(b.x - a.x)).toBe(-150);
  expect(Math.round(b.y - a.y)).toBe(-80);

  await page.mouse.move(cx, cy);
  await page.mouse.wheel(0, 400);
  const c = await transform(page);
  expect(c.s).toBeLessThan(b.s);
  // İmlecin altındaki ağaç noktası yerinde kalır.
  expect(Math.abs((cx - b.x) / b.s - (cx - c.x) / c.s)).toBeLessThan(1);
  expect(Math.abs((cy - b.y) / b.s - (cy - c.y) / c.s)).toBeLessThan(1);

  await page.mouse.dblclick(20, box.height - 20);
  expect((await transform(page)).s).toBeGreaterThan(c.s);
  await expect(page.locator('dialog[open]')).toHaveCount(0);
});

test('dokunma: çift dokunma yakınlaşır, kıstırma uzaklaşır', async ({ page, isMobile }) => {
  test.skip(!isMobile, 'dokunma testi');
  await page.goto('./');
  await expect(page.locator('.node').first()).toBeAttached();
  const s0 = (await transform(page)).s;
  const cdp = await page.context().newCDPSession(page);
  const touch = (type: string, pts: [number, number][]) =>
    cdp.send('Input.dispatchTouchEvent', { type, touchPoints: pts.map(([x, y], id) => ({ x, y, id })) });

  for (let i = 0; i < 2; i++) {
    await touch('touchStart', [[40, 780]]);
    await touch('touchEnd', []);
  }
  const s1 = (await transform(page)).s;
  expect(s1).toBeGreaterThan(s0 * 1.5);

  await touch('touchStart', [[150, 500], [230, 500]]);
  for (let i = 1; i <= 5; i++) await touch('touchMove', [[150 + i * 6, 500], [230 - i * 6, 500]]);
  await touch('touchEnd', []);
  expect((await transform(page)).s).toBeLessThan(s1);
});
