<script lang="ts">
  import { MIN_YEAR, MAX_YEAR } from '../../lib/data/dates';
  let { year, onSelect, label = 'Yıl girin' }: { year: number; onSelect: (year: number) => void; label?: string } = $props();
  let draft = $state('');
  let error = $state('');
  $effect(() => { draft = String(year); error = ''; });
  function submit(event: SubmitEvent) {
    event.preventDefault();
    const value = Number(draft);
    if (!draft.trim() || !Number.isInteger(value) || value === 0 || value < MIN_YEAR || value > MAX_YEAR) {
      error = 'MÖ 220 ile 1925 arasında bir tam yıl girin. Yıl sıfır yoktur.';
      return;
    }
    error = '';
    onSelect(value);
  }
</script>

<form class="year-entry" onsubmit={submit} novalidate>
  <label>{label}<input type="number" min={MIN_YEAR} max={MAX_YEAR} step="1" value={draft} oninput={(event) => draft = event.currentTarget.value} aria-label={label} aria-invalid={error ? 'true' : undefined} /></label>
  <button type="submit">Göster</button>
  <small>MÖ için eksi yazın: −209</small>
  {#if error}<p role="alert">{error}</p>{/if}
</form>

<style>
  .year-entry { display: flex; align-items: end; flex-wrap: wrap; gap: 8px; }
  label { display: grid; gap: 4px; font-size: 12px; font-weight: 600; color: var(--ink); }
  input { width: 120px; min-height: 44px; border: 1px solid var(--border-strong); border-radius: 8px; background: var(--surface-1); color: var(--ink); padding: 8px 10px; font-size: 16px; }
  button { min-height: 44px; padding: 8px 18px; border-radius: 8px; background: var(--accent); color: white; font-weight: 600; }
  small { align-self: center; color: var(--ink-muted); font-size: 12px; }
  p { flex-basis: 100%; color: var(--ink); margin: 0; font-size: 13px; }
</style>
