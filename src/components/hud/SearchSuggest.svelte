<script lang="ts">
  import type { SearchItem, State, PositionedState } from '../../lib/data/atlas';
  import { canon } from '../../lib/data/atlas';
  import { camera } from '../../lib/stores/camera.svelte';
  import { ui } from '../../lib/stores/ui.svelte';
  import { Search, MapPin, Swords, User, Crown } from '@lucide/svelte';

  let { items, states }: { items: SearchItem[]; states: PositionedState[] } = $props();

  let query = $state('');
  let isOpen = $state(false);
  let activeIndex = $state(0);
  let inputEl: HTMLInputElement | null = null;

  const filtered = $derived.by(() => {
    const q = canon(query.trim());
    if (q.length < 2) return [];
    return items.filter((it) => it.key.includes(q)).slice(0, 7);
  });

  function selectItem(item: SearchItem) {
    query = '';
    isOpen = false;

    const pState = states.find((s) => s.state.id === item.stateId);
    if (!pState) return;

    if (item.rulerId) {
      const ruler = pState.state.rulers?.find((r) => r.id === item.rulerId);
      if (ruler) {
        camera.focusState(pState);
        ui.openRulerDetail(ruler, pState.state);
        return;
      }
    }

    camera.focusState(pState);
    ui.openStateDetail(pState.state);
  }

  function onKeyDown(e: KeyboardEvent) {
    if (!isOpen || !filtered.length) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeIndex = (activeIndex + 1) % filtered.length;
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeIndex = (activeIndex - 1 + filtered.length) % filtered.length;
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (filtered[activeIndex]) {
        selectItem(filtered[activeIndex]);
      }
    } else if (e.key === 'Escape') {
      isOpen = false;
    }
  }
</script>

<div class="search-container">
  <div class="input-wrapper">
    <Search size={15} class="search-icon" />
    <input
      id="globalSearch"
      name="globalSearch"
      bind:this={inputEl}
      type="search"
      placeholder="Devlet, hükümdar, savaş veya eş ara..."
      bind:value={query}
      onfocus={() => (isOpen = true)}
      oninput={() => (isOpen = true, activeIndex = 0)}
      onkeydown={onKeyDown}
      aria-label="Tarih atlasında ara"
      aria-autocomplete="list"
      aria-controls="search-suggestions"
    />
  </div>

  {#if isOpen && filtered.length > 0}
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <div id="search-suggestions" role="listbox" class="suggest-dropdown glass-panel">
      {#each filtered as item, i (item.id)}
        <button
          type="button"
          role="option"
          aria-selected={i === activeIndex}
          class="suggest-item"
          class:active={i === activeIndex}
          onclick={() => selectItem(item)}
        >
          <div class="kind-icon">
            {#if item.kind === 'Devlet'}
              <Crown size={14} class="text-amber-400" />
            {:else if item.kind === 'Hükümdar'}
              <User size={14} class="text-emerald-400" />
            {:else if item.kind === 'Savaş'}
              <Swords size={14} class="text-rose-400" />
            {:else}
              <MapPin size={14} class="text-sky-400" />
            {/if}
          </div>

          <div class="item-texts">
            <span class="item-title">{item.title}</span>
            <span class="item-sub">{item.sub}</span>
          </div>

          <span class="kind-badge">{item.kind}</span>
        </button>
      {/each}
    </div>
  {/if}
</div>

<style>
  .search-container {
    position: relative;
    width: 290px;
  }

  .input-wrapper {
    position: relative;
    display: flex;
    align-items: center;
  }

  :global(.search-icon) {
    position: absolute;
    left: 12px;
    color: var(--text-dim);
    pointer-events: none;
  }

  input {
    width: 100%;
    height: 38px;
    background: rgba(14, 18, 23, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid var(--border-glass);
    border-radius: 9999px;
    padding: 0 14px 0 36px;
    font-size: 12px;
    color: var(--text-main);
    transition: all 0.2s ease;
  }

  input::placeholder {
    color: var(--text-dim);
  }

  input:hover {
    border-color: var(--border-glass-bright);
    background: rgba(22, 28, 36, 0.85);
  }

  input:focus {
    border-color: var(--gold-primary);
    box-shadow: 0 0 16px var(--gold-glow);
    background: var(--bg-surface);
  }

  .suggest-dropdown {
    position: absolute;
    top: calc(100% + 8px);
    left: 0;
    right: 0;
    border-radius: 12px;
    overflow: hidden;
    padding: 6px;
    z-index: 100;
  }

  .suggest-item {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 10px;
    border-radius: 8px;
    text-align: left;
    transition: background 0.15s ease;
  }

  .suggest-item:hover, .suggest-item.active {
    background: rgba(255, 255, 255, 0.08);
  }

  .kind-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: rgba(255, 255, 255, 0.04);
  }

  .item-texts {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    flex-grow: 1;
  }

  .item-title {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-main);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .item-sub {
    font-size: 11px;
    color: var(--text-muted);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .kind-badge {
    font-size: 10px;
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.1);
    padding: 2px 6px;
    border-radius: 4px;
  }
</style>
