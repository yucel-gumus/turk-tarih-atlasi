/** Historical dates retain their precision; unknown years are never invented. */
export interface HistoricalDate {
  start: number | null;
  end: number | null;
  exact: boolean;
}
const unknown = (): HistoricalDate => ({ start: null, end: null, exact: false });
export function parseHistoricalDate(value: string): HistoricalDate {
  const text = value.trim();
  const bce = /^MÖ\s*/i.test(text);
  const clean = text.replace(/^(?:MÖ|MS)\s*/i, '');
  const signed = (n: number) => bce ? -n : n;
  // ISO dates must be checked before year ranges (1302-07-27).
  const iso = /^(\d{3,4})-(\d{2})(?:-(\d{2}))?$/.exec(clean);
  if (iso && Number(iso[2]) >= 1 && Number(iso[2]) <= 12 && (!iso[3] || (Number(iso[3]) >= 1 && Number(iso[3]) <= 31))) {
    return { start: signed(Number(iso[1])), end: signed(Number(iso[1])), exact: true };
  }
  const range = /^(\d{1,4})\s*[-–]\s*(\d{1,4})(?:\s+arası)?$/.exec(clean);
  if (range) {
    const start = Number(range[1]);
    let end = Number(range[2]);
    if (!bce && range[2].length < range[1].length) {
      const magnitude = 10 ** range[2].length;
      end += Math.floor(start / magnitude) * magnitude;
      if (end < start) end += magnitude;
    }
    const a = signed(start), b = signed(end);
    return { start: Math.min(a, b), end: Math.max(a, b), exact: a === b };
  }
  const single = /^(\d{1,4})$/.exec(clean);
  if (single) return { start: signed(Number(single[1])), end: signed(Number(single[1])), exact: true };
  const dated = /^\d{1,2}\s+(?:Ocak|Şubat|Mart|Nisan|Mayıs|Haziran|Temmuz|Ağustos|Eylül|Ekim|Kasım|Aralık)\s+(\d{3,4})$/i.exec(clean);
  if (dated) return { start: signed(Number(dated[1])), end: signed(Number(dated[1])), exact: true };
  // Approximate and narrative expressions only supply a sorting hint.
  const hint = /^(\d{2,4})(?:\s|[-–?'’])/.exec(clean);
  return hint ? { start: signed(Number(hint[1])), end: null, exact: false } : unknown();
}
export function battleOccursInYear(date: HistoricalDate, year: number): boolean {
  return date.start !== null && date.end !== null && date.start <= year && year <= date.end;
}
export function compareBattleYears(a: number | null, b: number | null, descending = false): number {
  if (a === null) return b === null ? 0 : 1;
  if (b === null) return -1;
  return descending ? b - a : a - b;
}
export const MIN_YEAR = -220;
export const MAX_YEAR = 1925;
export function validAtlasYear(year: number): boolean {
  return Number.isSafeInteger(year) && year !== 0 && year >= MIN_YEAR && year <= MAX_YEAR;
}
export function clampAtlasYear(year: number): number {
  const value = Math.max(MIN_YEAR, Math.min(MAX_YEAR, Math.round(year)));
  return value === 0 ? 1 : value;
}
