<script lang="ts">
  import {
    Minus,
    Plus,
    Maximize2,
    ChevronLeft,
    ChevronRight,
    MoveHorizontal,
    Compass,
  } from '@lucide/svelte';

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

  let activeEraId = $state<string>('all');

  function handleEraClick(era: EraPreset) {
    activeEraId = era.id;
    onJumpToEra(era);
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

        <span class="zoom-value" title="Mevcut yakınlaştırma katsayısı">
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
          onclick={() => {
            activeEraId = 'all';
            onSetScale(0);
          }}
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
        onclick={() =>
          document.getElementById('devlet-listesi')?.scrollIntoView({ behavior: 'smooth' })}
      >
        Devlet listesi
      </button>
    </div>
  </div>

  <!-- Dönem Kısayolları (Era Quick Jump Bar) -->
  <div class="era-strip" role="toolbar" aria-label="Tarihsel dönemlere hızlı atla">
    <span class="era-title">
      <Compass size={11} aria-hidden="true" />
      Dönemler:
    </span>
    <div class="era-pills">
      {#each ERA_PRESETS as era (era.id)}
        <button
          type="button"
          class="era-pill"
          class:active={activeEraId === era.id}
          onclick={() => handleEraClick(era)}
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
    gap: 8px;
    user-select: none;
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
    gap: 10px;
    flex-wrap: wrap;
  }

  .toolbar-hint {
    font-size: 11px;
    color: var(--text-muted);
  }

  .toolbar-hint strong {
    color: var(--gold-primary);
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
    color: var(--ink-dim);
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 9999px;
    padding: 2px 9px;
  }

  .toolbar-right {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .button-group {
    display: inline-flex;
    align-items: center;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 9px;
    padding: 2px;
    gap: 2px;
  }

  .control-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 26px;
    height: 26px;
    border-radius: 7px;
    color: var(--ink-muted);
    transition: all 0.16s ease;
  }

  .control-btn:hover:not(:disabled) {
    color: var(--accent-strong);
    background: var(--accent-soft);
  }

  .control-btn:disabled {
    opacity: 0.32;
    cursor: default;
  }

  .fit-btn {
    border-left: 1px solid var(--border);
    margin-left: 2px;
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
    font-size: 11px;
    font-weight: 600;
    color: var(--accent-strong);
    text-decoration: underline;
    text-underline-offset: 3px;
    text-decoration-color: var(--accent-line);
    padding: 4px 6px;
    transition: opacity 0.15s ease;
  }

  .list-jump-btn:hover {
    opacity: 0.85;
    text-decoration-color: currentColor;
  }

  /* Dönem çipleri */
  .era-strip {
    display: flex;
    align-items: center;
    gap: 8px;
    overflow-x: auto;
    padding-bottom: 2px;
    font-size: 10px;
  }

  .era-title {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-weight: 600;
    white-space: nowrap;
  }

  .era-pills {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: nowrap;
  }

  .era-pill {
    padding: 4px 10px;
    border-radius: 7px;
    border: 1px solid var(--border);
    background: var(--surface-1);
    color: var(--ink-muted);
    font-size: 10px;
    font-weight: 500;
    white-space: nowrap;
    transition: all 0.15s ease;
  }

  .era-pill:hover {
    color: var(--ink);
    border-color: var(--border-strong);
    background: var(--surface-2);
  }

  .era-pill.active {
    color: var(--accent-strong);
    background: var(--accent-soft);
    border-color: var(--accent-line);
    font-weight: 600;
  }

  @media (max-width: 768px) {
    .interaction-help {
      display: none;
    }
    .era-strip {
      display: none;
    }
  }
</style>
