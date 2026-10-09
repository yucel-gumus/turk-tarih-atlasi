import { describe, it, expect, beforeAll } from 'vitest';
import { parseHistoricalDate, battleOccursInYear, compareBattleYears, validAtlasYear } from '../../src/lib/data/dates';
import { preloadAtlas } from '../../src/lib/data/atlas';
import { atlasIndex, resolveWar, resolvePerson } from '../../src/lib/data/lookup';
import { parseHash } from '../../src/lib/router/route';
import { getAllBattles, getBattleStats, categorizeFoe } from '../../src/lib/data/battles';

describe('historical date precision', () => {
  it.each([
    ['73', 73, 73, true], ['MÖ 200', -200, -200, true],
    ['MS 10-13', 10, 13, false], ['MÖ 209-177 arası', -209, -177, false],
    ['1231-32', 1231, 1232, false], ['1302-07-27', 1302, 1302, true],
    ['1329-06', 1329, 1329, true], ['3 Eylül 1260', 1260, 1260, true],
    ['MÖ 3. yüzyıl sonu', null, null, false], ['IX-X. yüzyıl', null, null, false],
    ['MÖ 209 civarı', -209, null, false], ['1231?', 1231, null, false],
    ['1403 veya 1404', 1403, null, false], ['', null, null, false],
  ])('%s retains precision', (text, start, end, exact) => {
    expect(parseHistoricalDate(text)).toEqual({ start, end, exact });
  });
  it('does not assign uncertain dates to exact-year views', () => {
    expect(battleOccursInYear(parseHistoricalDate('1453 civarı'), 1453)).toBe(false);
    expect(battleOccursInYear(parseHistoricalDate('1919-1922'), 1921)).toBe(true);
    expect(battleOccursInYear(parseHistoricalDate('1919-1922'), 1923)).toBe(false);
  });
  it('sorts unknown dates last in either direction', () => {
    expect(compareBattleYears(null, 1453)).toBeGreaterThan(0);
    expect(compareBattleYears(null, 1453, true)).toBeGreaterThan(0);
  });
  it('excludes year zero, fractions and out-of-range years', () => {
    for (const year of [0, 1.5, Infinity, -221, 1926]) expect(validAtlasYear(year)).toBe(false);
  });
});

describe('atlas integrity and route round trips', () => {
  beforeAll(async () => { await preloadAtlas(); });
  it('resolves every indexed destination to the same record', () => {
    const index = atlasIndex();
    for (const item of index.arama) {
      const route = parseHash(item.href);
      expect(route.name, item.href).not.toBe('notFound');
      if (route.name === 'war') expect(resolveWar(index.rulersById.get(route.rulerId)!, route.index, route.slug)?.war.name).toBe(item.title);
      if (route.name === 'person') expect(resolvePerson(index.rulersById.get(route.rulerId)!, route.role, route.index, route.slug)?.person.name).toBe(item.title);
    }
  });
  it('keeps guide separate and battle counts aligned', () => {
    const index = atlasIndex();
    expect(index.devletler.every(s => s.region !== 'giris')).toBe(true);
    expect(getAllBattles()).toHaveLength(index.toplam.savas);
    expect(Object.values(getBattleStats().byResult).reduce((a,b) => a+b, 0)).toBe(index.toplam.savas);
  });
  it.each(['#/zaman-makinesi/0', '#/zaman-makinesi/1453/extra', '#/zaman-makinesi/1.2', '#/zaman-makinesi/9999', '#/devlet/osmanli/hukumdar/foo/savas/99999999999999999999-test'])('rejects malformed route %s', (hash) => {
    expect(parseHash(hash).name).toBe('notFound');
  });
  it('accepts early and BCE year routes', () => {
    expect(parseHash('#/zaman-makinesi/-209')).toEqual({ name: 'timeMachine', year: -209 });
    expect(parseHash('#/zaman-makinesi/73')).toEqual({ name: 'timeMachine', year: 73 });
  });
  it('does not classify every khan as China', () => {
    expect(categorizeFoe('Timur Han kuvvetleri', 'Osmanlı')).toBe('Türk / İç Mücadele');
  });
});

describe('geographic coverage and safe metadata', () => {
  it('covers every real state with valid world coordinates', async () => {
    const { getAllStateGeoMarkers } = await import('../../src/lib/data/geo');
    const markers = getAllStateGeoMarkers();
    expect(markers).toHaveLength(atlasIndex().toplam.devlet);
    for (const marker of markers) {
      expect(marker.geo.stateId).toBe(marker.state.id);
      expect(marker.geo.lat).toBeGreaterThanOrEqual(-90);
      expect(marker.geo.lat).toBeLessThanOrEqual(90);
      expect(marker.geo.lon).toBeGreaterThanOrEqual(-180);
      expect(marker.geo.lon).toBeLessThanOrEqual(180);
    }
  });
  it('does not resolve an ambiguous mother name to the first match', async () => {
    const { resolveWife } = await import('../../src/lib/data/lookup');
    const r = { wives: [{ name: 'Ayşe (birinci)' }, { name: 'Ayşe (ikinci)' }] };
    expect(resolveWife(r as any, 'Ayşe?')).toBeNull();
  });
  it('rejects executable source URLs and unsafe record IDs', async () => {
    const { SourceSchema, StateSchema } = await import('../../src/schemas/atlas.schema');
    expect(SourceSchema.safeParse({ title: 'test', url: 'javascript:alert(1)' }).success).toBe(false);
    expect(StateSchema.safeParse({ ...atlasIndex().devletler[0], id: '../evil' }).success).toBe(false);
  });
});
