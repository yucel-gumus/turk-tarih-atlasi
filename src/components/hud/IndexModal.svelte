<script lang="ts">
  import { ui } from '../../lib/stores/ui.svelte';
  import { camera } from '../../lib/stores/camera.svelte';
  import { REGIONS, canon, yearLabel, type PositionedState } from '../../lib/data/atlas';
  import { X, Search, Crown, User, ChevronRight } from '@lucide/svelte';

  let { states }: { states: PositionedState[] } = $props();

  let selectedRegion = $state<string>('all');
  let filterText = $state('');

  const filteredStates = $derived.by(() => {
    const q = canon(filterText.trim());
    return states.filter((ps) => {
      if (selectedRegion !== 'all' && ps.state.region !== selectedRegion) {
        return false;
      }
      if (!q) return true;
      const sKey = canon(`${ps.state.name} ${(ps.state.aliases || []).join(' ')} ${ps.state.capital || ''}`);
      const rKey = (ps.state.rulers || []).some((r) => canon(`${r.name} ${(r.aliases || []).join(' ')}`).includes(q));
      return sKey.includes(q) || rKey;
    });
  });

  function close() {
    ui.toggleIndex(false);
  }

  function jumpToState(ps: PositionedState) {
    camera.focusState(ps);
    close();
  }

  function jumpToRuler(ps: PositionedState, rulerId: string) {
    const ruler = ps.state.rulers?.find((r) => r.id === rulerId);
    camera.focusState(ps);
    if (ruler) {
      ui.openRulerDetail(ruler, ps.state);
    }
    close();
  }

  function onKeyDown(e: KeyboardEvent) {
    if (e.key === 'Escape') close();
  }
</script>

<svelte:window onkeydown={onKeyDown} />

{#if ui.isIndexOpen}
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <div class="modal-backdrop" onclick={close} role="presentation"></div>

  <div
    class="index-modal glass-panel"
    role="dialog"
    aria-modal="true"
    aria-label="Devlet ve Hükümdar Dizini"
  >
    <!-- Modal Head -->
    <div class="modal-head">
      <div>
        <h2 class="head-title">Devlet ve Hükümdar Dizini</h2>
        <p class="head-desc">77 Türk devleti ve 320 hükümdarın tam alfabetik ve coğrafi kronolojisi.</p>
      </div>

      <button type="button" class="close-btn" onclick={close} aria-label="Dizini kapat">
        <X size={18} />
      </button>
    </div>

    <!-- Filter Bar -->
    <div class="modal-filters">
      <div class="search-box">
        <Search size={14} class="search-icon" />
        <input
          id="indexFilterInput"
          name="indexFilterInput"
          type="search"
          placeholder="Dizin içinde ara..."
          bind:value={filterText}
          aria-label="Dizinde filtrele"
        />
      </div>

      <div class="region-tabs">
        <button
          type="button"
          class="tab-btn"
          class:active={selectedRegion === 'all'}
          onclick={() => (selectedRegion = 'all')}
        >
          Tümü ({states.length})
        </button>

        {#each REGIONS as r}
          {@const count = states.filter((s) => s.state.region === r.id).length}
          {#if count > 0}
            <button
              type="button"
              class="tab-btn"
              class:active={selectedRegion === r.id}
              onclick={() => (selectedRegion = r.id)}
              style="--r-color: {r.color};"
            >
              <span class="r-dot" style="background: {r.color};"></span>
              <span>{r.name.split(',')[0]} ({count})</span>
            </button>
          {/if}
        {/each}
      </div>
    </div>

    <!-- Index Body / State Cards -->
    <div class="index-scroll-body">
      {#each filteredStates as ps (ps.state.id)}
        <div class="state-index-card">
          <div class="state-row">
            <button type="button" class="state-jump-btn" onclick={() => jumpToState(ps)}>
              <Crown size={15} class="text-amber-400" />
              <span class="st-name">{ps.state.name}</span>
              <span class="st-dates">({yearLabel(ps.state.start)} – {yearLabel(ps.state.end)})</span>
              <ChevronRight size={14} class="jump-arrow" />
            </button>
          </div>

          <!-- Rulers Pills -->
          {#if ps.state.rulers && ps.state.rulers.length > 0}
            <div class="rulers-chip-list">
              {#each ps.state.rulers as ruler (ruler.id)}
                <button
                  type="button"
                  class="ruler-chip"
                  onclick={() => jumpToRuler(ps, ruler.id)}
                >
                  <User size={11} class="text-emerald-400" />
                  <span>{ruler.name}</span>
                  {#if ruler.claim}
                    <span class="claim-tag">talip</span>
                  {/if}
                </button>
              {/each}
            </div>
          {/if}
        </div>
      {/each}
    </div>
  </div>
{/if}

<style>
  .modal-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(8px);
    z-index: 110;
  }

  .index-modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(860px, 94vw);
    max-height: 86vh;
    background: rgba(14, 18, 23, 0.95);
    backdrop-filter: blur(28px);
    border: 1px solid var(--border-glass-bright);
    border-radius: 20px;
    z-index: 120;
    display: flex;
    flex-direction: column;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.8), 0 0 32px var(--gold-glow);
    overflow: hidden;
  }

  .modal-head {
    padding: 20px 24px;
    border-bottom: 1px solid var(--border-glass);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .head-title {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 22px;
    font-weight: 700;
    color: var(--gold-primary);
  }

  .head-desc {
    margin: 4px 0 0;
    font-size: 12px;
    color: var(--text-muted);
  }

  .close-btn {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-glass);
    transition: all 0.2s ease;
  }

  .close-btn:hover {
    color: var(--text-main);
    background: rgba(255, 255, 255, 0.1);
  }

  .modal-filters {
    padding: 14px 24px;
    border-bottom: 1px solid var(--border-glass);
    display: flex;
    flex-direction: column;
    gap: 12px;
    background: rgba(255, 255, 255, 0.015);
  }

  .search-box {
    position: relative;
    display: flex;
    align-items: center;
  }

  :global(.search-icon) {
    position: absolute;
    left: 12px;
    color: var(--text-dim);
  }

  .search-box input {
    width: 100%;
    height: 36px;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid var(--border-glass);
    border-radius: 8px;
    padding: 0 12px 0 34px;
    font-size: 13px;
    color: var(--text-main);
  }

  .region-tabs {
    display: flex;
    align-items: center;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 2px;
  }

  .tab-btn {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 4px 10px;
    border-radius: 9999px;
    white-space: nowrap;
    transition: all 0.2s ease;
  }

  .tab-btn:hover, .tab-btn.active {
    color: var(--text-main);
    background: rgba(255, 255, 255, 0.1);
    border-color: var(--gold-primary);
  }

  .r-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }

  .index-scroll-body {
    padding: 20px 24px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .state-index-card {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-glass);
    border-radius: 12px;
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .state-jump-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    text-align: left;
    outline: none;
    border-radius: 6px;
    padding: 2px 4px;
    transition: all 0.2s ease;
  }

  .state-jump-btn:hover {
    color: var(--gold-primary);
  }

  .st-name {
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 700;
  }

  .st-dates {
    font-size: 12px;
    color: var(--text-muted);
  }

  :global(.jump-arrow) {
    margin-left: auto;
    color: var(--text-dim);
  }

  .rulers-chip-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .ruler-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.06);
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 11px;
    color: var(--text-muted);
    transition: all 0.15s ease;
  }

  .ruler-chip:hover {
    background: rgba(229, 195, 120, 0.12);
    border-color: var(--border-glass-bright);
    color: var(--gold-primary);
  }

  .claim-tag {
    font-size: 9px;
    color: #fca5a5;
    background: rgba(248, 113, 113, 0.2);
    padding: 1px 4px;
    border-radius: 4px;
  }
</style>
