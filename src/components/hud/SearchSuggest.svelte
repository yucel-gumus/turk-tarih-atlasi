<script lang="ts">
  import { atlasIndex, searchItems, type SearchItem } from '../../lib/data/lookup';
  import { router } from '../../lib/router/router.svelte';
  import { hrefSearch } from '../../lib/router/route';
  import BookOpen from '@lucide/svelte/icons/book-open';
  import Crown from '@lucide/svelte/icons/crown';
  import Heart from '@lucide/svelte/icons/heart';
  import Search from '@lucide/svelte/icons/search';
  import Swords from '@lucide/svelte/icons/swords';
  import User from '@lucide/svelte/icons/user';
  import Users from '@lucide/svelte/icons/users';

  const items = atlasIndex().arama;

  let query = $state('');
  let isOpen = $state(false);
  let activeIndex = $state(0);
  let inputEl: HTMLInputElement | null = null;

  /** Açılır liste ekrana sığsın diye sınırlıdır; kırpma gizlenmez, yazılır. */
  const MAX_SUGGESTIONS = 8;

  const matched = $derived.by(() => {
    return searchItems(items, query);
  });
  const filtered = $derived(matched.slice(0, MAX_SUGGESTIONS));
  const hiddenCount = $derived(Math.max(0, matched.length - filtered.length));

  function selectItem(item: SearchItem) {
    query = '';
    isOpen = false;
    // Öneri doğrudan ilgili sayfaya iner: savaş önerisi savaş sayfasını,
    // kişi önerisi kişi sayfasını açar.
    router.go(item.href);
  }

  function onKeyDown(e: KeyboardEvent) {
    if (e.key === 'Escape') {
      isOpen = false;
      inputEl?.blur();
      return;
    }

    if (!isOpen || !filtered.length) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeIndex = (activeIndex + 1) % filtered.length;
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeIndex = (activeIndex - 1 + filtered.length) % filtered.length;
    } else if (e.key === 'Enter') {
      e.preventDefault();
      const item = filtered[activeIndex];
      if (item) selectItem(item);
    }
  }

  function handleBlur() {
    // Öneri düğmesine tıklamanın kaydolması için kapanma kısa süre geciktirilir.
    setTimeout(() => {
      isOpen = false;
    }, 150);
  }
</script>

<div class="search-container">
  <div class="input-wrapper">
    <Search size={15} class="search-icon" aria-hidden="true" />
    <input
      id="globalSearch"
      name="globalSearch"
      bind:this={inputEl}
      type="search"
      role="combobox"
      placeholder="Devlet, hükümdar, savaş veya kişi ara..."
      bind:value={query}
      onfocus={() => (isOpen = true)}
      oninput={() => {
        isOpen = true;
        activeIndex = 0;
      }}
      onblur={handleBlur}
      onkeydown={onKeyDown}
      aria-label="Atlasta ara"
      aria-autocomplete="list"
      aria-haspopup="listbox"
      aria-controls="search-suggestions"
      aria-expanded={isOpen && filtered.length > 0}
      aria-activedescendant={isOpen && filtered.length > 0 ? `search-option-${activeIndex}` : undefined}
    />
  </div>

  {#if isOpen && query.trim().length >= 2}
    <!-- svelte-ignore a11y_no_noninteractive_element_interactions -->
    <div class="suggest-dropdown glass-panel">
      {#if filtered.length > 0}
        <div id="search-suggestions" role="listbox">
          {#each filtered as item, i (item.id)}
        <button
          id={`search-option-${i}`}
          type="button"
          role="option"
          aria-selected={i === activeIndex}
          class="suggest-item"
          class:active={i === activeIndex}
          onclick={() => selectItem(item)}
        >
          <div class="kind-icon">
            {#if item.kind === 'Devlet'}
              <Crown size={14} class="icon-state" aria-hidden="true" />
            {:else if item.kind === 'Rehber'}
              <BookOpen size={14} class="icon-state" aria-hidden="true" />
            {:else if item.kind === 'Hükümdar'}
              <User size={14} class="icon-ruler" aria-hidden="true" />
            {:else if item.kind === 'Savaş'}
              <Swords size={14} class="icon-war" aria-hidden="true" />
            {:else if item.kind === 'Eş'}
              <Heart size={14} class="icon-person" aria-hidden="true" />
            {:else}
              <Users size={14} class="icon-person" aria-hidden="true" />
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
        {#if hiddenCount > 0}
          <a class="suggest-more" href={hrefSearch(query)} onclick={() => (isOpen = false)}>
            {matched.length} sonucun tamamını göster →
          </a>
        {/if}
      {:else}
        <p class="suggest-empty" role="status">Eşleşen kayıt yok.</p>
      {/if}
    </div>
  {/if}
</div>

<style>
  .search-container {
    position: relative;
    width: 320px;
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
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 9999px;
    padding: 0 14px 0 36px;
    font-size: 12px;
    color: var(--ink);
    transition: border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  }

  input::placeholder {
    color: var(--ink-dim);
  }

  input:hover {
    border-color: var(--border-strong);
    background: var(--surface-1);
  }

  input:focus {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-soft);
    background: var(--surface-1);
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
    background: var(--surface-1);
    box-shadow: var(--shadow-lg);
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

  .suggest-item:hover,
  .suggest-item.active {
    background: var(--surface-2);
  }

  .kind-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: var(--surface-2);
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
    font-weight: 600;
    color: var(--accent-strong);
    background: var(--accent-soft);
    padding: 2px 6px;
    border-radius: 5px;
  }

  .suggest-more {
    display: block;
    margin: 6px 4px 2px;
    padding: 8px;
    font-size: 10px;
    color: var(--gold-primary);
  }

  .suggest-empty {
    margin: 0;
    padding: 10px;
    color: var(--text-muted);
    font-size: 12px;
  }

  @media (max-width: 700px) {
    .search-container {
      order: 3;
      width: 100%;
    }
  }
</style>
