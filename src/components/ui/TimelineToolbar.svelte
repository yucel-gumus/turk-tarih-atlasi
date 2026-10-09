<script lang="ts">
  import Minus from '@lucide/svelte/icons/minus';
  import Plus from '@lucide/svelte/icons/plus';
  import Maximize2 from '@lucide/svelte/icons/maximize-2';
  import ChevronLeft from '@lucide/svelte/icons/chevron-left';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import LayoutList from '@lucide/svelte/icons/layout-list';

  export interface EraPreset {
    id: string;
    label: string;
    year: number;
    scaleIndex: number;
  }

  export const ERA_PRESETS: EraPreset[] = [
    { id: 'all', label: 'Tüm tarih', year: -209, scaleIndex: 0 },
    { id: 'bozkir', label: 'Hun & Bozkır', year: -209, scaleIndex: 3 },
    { id: 'gokturk', label: 'Göktürk & Uygur', year: 552, scaleIndex: 4 },
    { id: 'islam', label: 'Karahanlı & Gazneli', year: 840, scaleIndex: 4 },
    { id: 'selcuklu', label: 'Büyük Selçuklu', year: 1040, scaleIndex: 5 },
    { id: 'beylikler', label: 'Anadolu Beylikleri', year: 1299, scaleIndex: 5 },
    { id: 'osmanli', label: 'Osmanlı Dönemi', year: 1453, scaleIndex: 4 },
    { id: 'cumhuriyet', label: 'Cumhuriyet', year: 1923, scaleIndex: 5 },
  ];

  let {
    filteredCount,
    minYearLabel,
    maxYearLabel,
    scales,
    scaleIndex,
    activeEraId = 'all',
    onSetScale,
    onPanBy,
    onJumpToEra,
  }: {
    filteredCount: number;
    minYearLabel: string;
    maxYearLabel: string;
    scales: number[];
    scaleIndex: number;
    activeEraId?: string;
    onSetScale: (index: number) => void;
    onPanBy: (pixels: number) => void;
    onJumpToEra: (era: EraPreset) => void;
  } = $props();

  /** Listeye kaydır ve klavye odağını da oraya taşı. */
  function jumpToList() {
    const target = document.getElementById('devlet-listesi');
    if (!target) return;
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
    target.focus({ preventScroll: true });
  }
</script>

<div class="timeline-toolbar-wrapper no-print">
  <div class="period-row">
    <label>Dönem seçerek incele
      <select aria-label="İncelenecek dönem" value={activeEraId} onchange={(event) => { const era = ERA_PRESETS.find(item => item.id === event.currentTarget.value); if (era) onJumpToEra(era); }}>
        {#each ERA_PRESETS as era (era.id)}<option value={era.id}>{era.label}</option>{/each}
      </select>
    </label>
    <span class="scope-pill">{filteredCount} devlet · {minYearLabel} – {maxYearLabel}</span>
    <button class="list-jump-btn" type="button" onclick={jumpToList}><LayoutList size={15} aria-hidden="true" /> Devlet listesi</button>
  </div>
  <details class="tool-disclosure">
    <summary>Yakınlaştırma ve şerit araçları</summary>
    <div class="toolbar-right">
      <div class="button-group" role="group" aria-label="Zaman şeridini kaydır">
        <button type="button" aria-label="Geçmişe kaydır" onclick={() => onPanBy(-300)}><ChevronLeft size={18} aria-hidden="true" /></button>
        <button type="button" aria-label="Geleceğe kaydır" onclick={() => onPanBy(300)}><ChevronRight size={18} aria-hidden="true" /></button>
      </div>
      <div class="button-group" role="group" aria-label="Yakınlaştırma seviyesi">
        <button type="button" aria-label="Uzaklaştır" disabled={scaleIndex === 0} onclick={() => onSetScale(scaleIndex - 1)}><Minus size={18} aria-hidden="true" /></button>
        <span aria-live="polite">{scales[scaleIndex]}×</span>
        <button type="button" aria-label="Yakınlaştır" disabled={scaleIndex === scales.length - 1} onclick={() => onSetScale(scaleIndex + 1)}><Plus size={18} aria-hidden="true" /></button>
        <button type="button" aria-label="Tüm aralığı ekrana sığdır" disabled={scaleIndex === 0} onclick={() => onSetScale(0)}><Maximize2 size={18} aria-hidden="true" /></button>
      </div>
      <p>Şeridi sürükleyin; yakınlaştırmak için + / − veya Ctrl + fare tekerleğini kullanın.</p>
    </div>
  </details>
</div>
<style>
  .timeline-toolbar-wrapper { display: grid; gap: 8px; }
  .period-row { display: flex; align-items: center; flex-wrap: wrap; gap: 10px; }
  label { display: grid; gap: 4px; font-size: 12px; font-weight: 600; color: var(--ink); }
  select { min-height: 44px; max-width: 100%; border: 1px solid var(--border-strong); border-radius: 8px; padding: 8px 10px; background: var(--surface-1); color: var(--ink); font-size: 14px; }
  .scope-pill { font-size: 12px; color: var(--ink-muted); }
  .list-jump-btn { display: inline-flex; align-items: center; gap: 6px; min-height: 44px; margin-left: auto; border: 1px solid var(--border); border-radius: 8px; padding: 8px 12px; color: var(--ink); }
  summary { cursor: pointer; color: var(--ink-muted); font-size: 12px; padding: 8px 0; }
  .toolbar-right { display: flex; flex-wrap: wrap; align-items: center; gap: 10px; padding: 8px 0; }
  .button-group { display: inline-flex; align-items: center; gap: 4px; border: 1px solid var(--border); border-radius: 8px; }
  .button-group button { display: grid; place-items: center; width: 44px; height: 44px; color: var(--ink); }
  .button-group button:disabled { opacity: .4; }
  .button-group span { font-size: 13px; min-width: 30px; text-align: center; }
  p { font-size: 12px; color: var(--ink-muted); margin: 0; }
  @media (max-width: 700px) { .scope-pill { display: none; } label { flex: 1; min-width: 0; } .list-jump-btn { font-size: 12px; padding: 8px; } }
</style>
