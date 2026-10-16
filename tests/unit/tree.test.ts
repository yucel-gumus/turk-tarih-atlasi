import { describe, it, expect, beforeAll } from 'vitest';
import {
  preloadAtlas,
  allStates,
  buildTree,
  getState,
  getRuler,
  getWar,
  counterpartWars,
  foeMatches,
  childAsRuler,
  durationLabel,
} from '../../src/lib/data/atlas';
import { layoutTree, NODE_W, NODE_H } from '../../src/lib/tree/layout';

beforeAll(async () => {
  await preloadAtlas();
});

describe('soy ağacı', () => {
  it('Asya Hun kökünden başlar ve her devleti bir kez içerir', () => {
    const { root, byId } = buildTree();
    expect(root.id).toBe('asya-hun');
    for (const s of allStates()) expect(byId.has(s.id), s.id).toBe(true);
  });

  it('Osmanlı üzerinden Türkiye Cumhuriyeti köke bağlanır', () => {
    const { byId } = buildTree();
    const chain: string[] = [];
    for (let n = byId.get('turkiye') ?? null; n; n = n.parent) chain.unshift(n.id);
    expect(chain).toEqual([
      'asya-hun',
      'gokturk',
      'dogu-gokturk',
      'ikinci-gokturk',
      'oguz-yabgu',
      'buyuk-selcuklu',
      'anadolu-selcuklu',
      'osmanli',
      'turkiye',
    ]);
  });

  it('günümüz Türk devletlerinin hepsi ağaçta', () => {
    const { byId } = buildTree();
    for (const id of ['turkiye', 'kktc', 'azerbaycan', 'kazakistan', 'ozbekistan', 'turkmenistan', 'kirgizistan']) {
      expect(byId.get(id)?.ongoing, id).toBe(true);
    }
  });

  it('yerleşimde düğümler üst üste binmez ve çocuk üst düğümün altındadır', () => {
    const { root } = buildTree();
    const layout = layoutTree(root);
    const seen = new Set<string>();
    for (const p of layout.placed) {
      for (const q of layout.placed) {
        if (p === q) continue;
        const key = [p.node.id, q.node.id].sort().join('|');
        if (seen.has(key)) continue;
        seen.add(key);
        const overlap = p.x < q.x + NODE_W && q.x < p.x + NODE_W && p.y < q.y + NODE_H && q.y < p.y + NODE_H;
        expect(overlap, key).toBe(false);
      }
      if (p.node.parent) expect(p.y).toBeGreaterThan(layout.byId.get(p.node.parent.id)!.y + NODE_H);
    }
  });
});

describe('ardıllık ve dal ayrımı', () => {
  it('Osmanlı → Türkiye düz aşağı iner, Türkiye → KKTC yana açılır', () => {
    const { root } = buildTree();
    const { byId } = layoutTree(root);
    const x = (id: string) => byId.get(id)!.x;
    expect(x('turkiye')).toBe(x('osmanli'));
    expect(x('kktc')).not.toBe(x('turkiye'));
    expect(x('teke')).not.toBe(x('hamid'));
  });
});

describe('modal içerikleri', () => {
  it("Fâtih'in savaşları ve karşı taraf kaydı bulunur", () => {
    const fatih = getRuler('osmanli', 'mehmed-ii')!;
    const index = fatih.wars.findIndex((w) => w.name === 'Otlukbeli');
    const entry = getWar({ stateId: 'osmanli', rulerId: 'mehmed-ii', index })!;
    expect(entry.war.result).toBe('zafer');
    expect(counterpartWars(entry).map((w) => w.stateId)).toContain('akkoyunlu');
    const foe = foeMatches(entry).find((f) => f.state.id === 'akkoyunlu');
    expect(foe?.ruler?.name).toMatch(/Uzun Hasan/);
  });

  it('hükümdar olan çocuk kendi kaydına bağlanır', () => {
    const osmanli = getState('osmanli')!;
    const fatih = getRuler('osmanli', 'mehmed-ii')!;
    expect(childAsRuler(osmanli, fatih, 'Bayezid')?.name).toBe('II. Bayezid');
    expect(childAsRuler(osmanli, fatih, 'Mustafa')).toBeNull();
  });

  it('savaş süresi yalnız kayıttaki tarihten hesaplanır', () => {
    expect(durationLabel(1480, 1481)).toContain('yaklaşık 1 yıl');
    expect(durationLabel(1453, 1453)).toBe('1453 yılı içinde');
    expect(durationLabel(null, null)).toBe('Kayıtta kesin tarih yok');
  });
});
