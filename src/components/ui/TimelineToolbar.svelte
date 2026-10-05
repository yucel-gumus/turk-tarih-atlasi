<script lang="ts">
  import Minus from '@lucide/svelte/icons/minus';
  import Plus from '@lucide/svelte/icons/plus';
  import Maximize2 from '@lucide/svelte/icons/maximize-2';
  import ChevronLeft from '@lucide/svelte/icons/chevron-left';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import MoveHorizontal from '@lucide/svelte/icons/move-horizontal';
  import Compass from '@lucide/svelte/icons/compass';

  export interface EraPreset {
    id: string;
    label: string;
    year: number;
    scaleIndex: number;
  }

  export const ERA_PRESETS: EraPreset[] = [
    { id: 'all', label: 'Tümü', year: -209, scaleIndex: 0 },
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
    onSetScale,
    onPanBy,
    onJumpToEra,
  }: {
    filteredCount: number;
    minYearLabel: string;
    maxYearLabel: string;
    scales: number[];
    scaleIndex: number;
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
  <!-- Ana Kontrol Çubuğu -->
  <div class="timeline-toolbar">
    <div class="toolbar-left">
      <span class="toolbar-hint">
        Şerit <strong>{filteredCount}</strong> devlet gösteriyor · {minYearLabel} – {maxYearLabel}
      </span>
      <div class="interaction-help">
        <span class="help-badge" title="Etkileşim ipuçları">
          <MoveHorizontal size={12} aria-hidden="true" />
          <span>Fareyle sürükle & tekerlekle yakınlaştır</span>
        </span>
      </div>
    </div>

    <div class="toolbar-right">
      <!-- Pan / Kaydırma Butonları -->
      <div class="button-group pan-group" role="group" aria-label="Zaman şeridini kaydır">
        <button
          type="button"
          class="control-btn"
          onclick={() => onPanBy(-300)}
          aria-label="Geçmişe kaydır"
          title="Geçmişe kaydır (Sol ok tuşu)"
        >
          <ChevronLeft size={15} aria-hidden="true" />
        </button>
        <button
          type="button"
          class="control-btn"
          onclick={() => onPanBy(300)}
          aria-label="Geleceğe kaydır"
          title="Geleceğe kaydır (Sağ ok tuşu)"
        >
          <ChevronRight size={15} aria-hidden="true" />
        </button>
      </div>

      <!-- Yakınlaştırma Kontrolleri -->
      <div class="button-group zoom-group" role="group" aria-label="Yakınlaştırma seviyesi">
        <button
          class="control-btn"
          type="button"
          onclick={() => onSetScale(scaleIndex - 1)}
          disabled={scaleIndex === 0}
          aria-label="Uzaklaştır"
          title="Uzaklaştır (Fare tekerleği aşağı veya - tuşu)"
        >
          <Minus size={14} aria-hidden="true" />
        </button>

        <span class="zoom-value" title="Mevcut yakınlaştırma katsayısı" aria-live="polite">
          {scales[scaleIndex]}×
        </span>

        <button
          class="control-btn"
          type="button"
          onclick={() => onSetScale(scaleIndex + 1)}
          disabled={scaleIndex === scales.length - 1}
          aria-label="Yakınlaştır"
          title="Yakınlaştır (Fare tekerleği yukarı veya + tuşu)"
        >
          <Plus size={14} aria-hidden="true" />
        </button>

        <button
          class="control-btn fit-btn"
          type="button"
          onclick={() => onSetScale(0)}
          disabled={scaleIndex === 0}
          aria-label="Tüm aralığı ekrana sığdır"
          title="Tüm aralığı sığdır (1×)"
        >
          <Maximize2 size={13} aria-hidden="true" />
        </button>
      </div>

      <button
        class="list-jump-btn"
        type="button"
        onclick={jumpToList}
      >
        Devlet listesi
      </button>
    </div>
  </div>

  <!-- Dönem Kısayolları (Era Quick Jump Bar) -->
  <div class="era-strip" role="group" aria-label="Tarihsel dönemlere hızlı atla">
    <span class="era-title">
      <Compass size={11} aria-hidden="true" />
      Dönemler:
    </span>
    <div class="era-pills">
      {#each ERA_PRESETS as era (era.id)}
        <button
          type="button"
          class="era-pill"
          onclick={() => onJumpToEra(era)}
        >
          {era.label}
        </button>
      {/each}
    </div>
  </div>
</div>

<style>
  .timeline-toolbar-wrapper {
    display: flex;
    flex-direction: column;
    gap: 12px;
    user-select: none;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
  }

  .timeline-toolbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    flex-wrap: wrap;
  }

  .toolbar-left {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }

  .toolbar-hint {
    font-size: 11.5px;
    color: var(--ink-muted);
  }

  .toolbar-hint strong {
    color: var(--ink);
    font-weight: 600;
  }

  .interaction-help {
    display: inline-flex;
    align-items: center;
  }

  .help-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 10px;
    font-weight: 500;
    color: var(--ink-dim);
    background: var(--surface-2);
    border-radius: 9999px;
    padding: 3px 10px;
  }

  .toolbar-right {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .button-group {
    display: inline-flex;
    align-items: center;
    background: var(--surface-2);
    border-radius: 99px;
    padding: 3px;
    gap: 1px;
  }

  .control-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 26px;
    height: 26px;
    border-radius: 99px;
    color: var(--ink-muted);
    transition: all 0.16s ease;
  }

  .control-btn:hover:not(:disabled) {
    color: var(--accent-strong);
    background: var(--surface-1);
    box-shadow: var(--shadow-sm);
  }

  .control-btn:disabled {
    opacity: 0.32;
    cursor: default;
  }

  .fit-btn {
    position: relative;
    margin-left: 4px;
  }
  .fit-btn::before {
    content: '';
    position: absolute;
    left: -2px;
    top: 4px;
    bottom: 4px;
    width: 1px;
    background: var(--border-strong);
    opacity: 0.5;
  }

  .zoom-value {
    font-size: 11px;
    font-weight: 600;
    color: var(--ink);
    min-width: 32px;
    text-align: center;
    font-variant-numeric: tabular-nums;
  }

  .list-jump-btn {
    font-size: 11.5px;
    font-weight: 600;
    color: var(--accent-strong);
    padding: 4px 8px;
    transition: opacity 0.15s ease;
  }

  .list-jump-btn:hover {
    opacity: 0.85;
  }

  /* Dönem çipleri */
  .era-strip {
    display: flex;
    align-items: center;
    gap: 10px;
    overflow-x: auto;
    font-size: 10.5px;
  }

  .era-title {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    color: var(--ink-dim);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 700;
    white-space: nowrap;
  }

  .era-pills {
    display: flex;
    align-items: center;
    gap: 4px;
    flex-wrap: nowrap;
  }

  .era-pill {
    padding: 4px 12px;
    border-radius: 99px;
    border: 1px solid transparent;
    background: transparent;
    color: var(--ink-muted);
    font-size: 11px;
    font-weight: 500;
    white-space: nowrap;
    transition: all 0.15s ease;
  }

  .era-pill:hover {
    color: var(--ink);
    background: var(--surface-2);
  }

  @media (max-width: 768px) {
    .interaction-help {
      display: none;
    }
    .era-title {
      display: none;
    }
  }
</style>
