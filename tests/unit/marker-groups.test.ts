import { describe, it, expect } from 'vitest';
import { groupScreenMarkers } from '../../src/lib/data/marker-groups';

describe('overlapping map targets', () => {
  it('keeps every co-located state and isolated state exactly once', () => {
    const points = [{ id: 'a', x: 0, y: 0 }, { id: 'b', x: 0, y: 0 }, { id: 'c', x: 100, y: 0 }];
    const groups = groupScreenMarkers(points, p => p);
    expect(groups.map(group => group.map(p => p.id))).toEqual([['a', 'b'], ['c']]);
    expect(groups.flat()).toHaveLength(points.length);
  });
  it('resolves overlap chains even when input order separates neighbors', () => {
    const points = [{ x: 0, y: 0 }, { x: 80, y: 0 }, { x: 40, y: 0 }];
    expect(groupScreenMarkers(points, p => p)).toEqual([points]);
  });
  it('separates records as projected distance increases on zoom', () => {
    const points = [{ x: 0, y: 0 }, { x: 30, y: 0 }];
    expect(groupScreenMarkers(points, p => p)).toHaveLength(1);
    expect(groupScreenMarkers(points, p => ({ x: p.x * 2, y: p.y * 2 }))).toHaveLength(2);
    expect(groupScreenMarkers([], () => ({ x: 0, y: 0 }))).toEqual([]);
  });
});
