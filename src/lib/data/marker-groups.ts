/** Group overlapping screen targets without dropping any historical record.
 * Connected components also resolve chains of overlapping hit areas. */
export function groupScreenMarkers<T>(items: T[], project: (item: T) => { x: number; y: number }, distance = 48): T[][] {
  const points = items.map(project);
  const parents = items.map((_, i) => i);
  function root(i: number): number {
    while (parents[i] !== i) { parents[i] = parents[parents[i]]; i = parents[i]; }
    return i;
  }
  for (let i = 0; i < items.length; i++) {
    for (let j = i + 1; j < items.length; j++) {
      if (Math.hypot(points[i].x - points[j].x, points[i].y - points[j].y) < distance) parents[root(j)] = root(i);
    }
  }
  const groups = new Map<number, T[]>();
  items.forEach((item, i) => { const key = root(i); const group = groups.get(key) ?? []; group.push(item); groups.set(key, group); });
  return [...groups.values()];
}
