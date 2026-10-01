<script lang="ts">
  import { atlasIndex, searchItems, type SearchItem } from '../lib/data/lookup';
  import { canon } from '../lib/text';
  import { hrefHome } from '../lib/router/route';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';

  let { query }: { query: string } = $props();
  const items = atlasIndex().arama;
  const kinds: SearchItem['kind'][] = ['Devlet', 'Hükümdar', 'Savaş', 'Eş', 'Çocuk', 'Rehber'];
  let kind = $state<SearchItem['kind'] | 'Tümü'>('Tümü');
  const normalized = $derived(canon(query.trim()));
  const matches = $derived(searchItems(items, query));
  const results = $derived(kind === 'Tümü' ? matches : matches.filter((item) => item.kind === kind));
</script>

<Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: 'Arama' }]} />
<PageHeader
  eyebrow="Atlas araması"
  title="Arama sonuçları"
  subtitle={query.trim() ? `“${query.trim()}” için ${matches.length} kayıt` : 'Üstteki arama alanına en az iki karakter yazın.'}
/>

{#if normalized.length < 2}
  <p class="honesty-note">Aramak için en az iki karakter yazın.</p>
{:else if results.length === 0}
  <p class="honesty-note">Bu aramayla eşleşen kayıt bulunamadı. Başka bir ad veya yazım deneyin.</p>
{:else}
  <div class="kind-filters" aria-label="Sonuç türü">
    <button type="button" class:active={kind === 'Tümü'} onclick={() => (kind = 'Tümü')}>
      Tümü · {matches.length}
    </button>
    {#each kinds as option (option)}
      {@const count = matches.filter((item) => item.kind === option).length}
      {#if count > 0}
        <button type="button" class:active={kind === option} onclick={() => (kind = option)}>
          {option} · {count}
        </button>
      {/if}
    {/each}
  </div>
  {#if results.length === 0}
    <p class="honesty-note">Bu türde sonuç bulunamadı.</p>
  {/if}
  <div class="result-list" aria-label="Arama sonuçları">
    {#each results as item (item.id)}
      <a class="result-item" href={item.href}>
        <span class="result-kind">{item.kind}</span>
        <span class="result-body">
          <strong>{item.title}</strong>
          <small>{item.sub}</small>
        </span>
        <span class="result-arrow" aria-hidden="true">→</span>
      </a>
    {/each}
  </div>
{/if}

<style>
  .kind-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .kind-filters button {
    padding: 6px 10px;
    border: 1px solid var(--border-glass);
    border-radius: 999px;
    color: var(--text-muted);
    font-size: 11px;
  }

  .kind-filters button.active,
  .kind-filters button:hover {
    color: var(--gold-primary);
    border-color: var(--border-glass-bright);
    background: rgba(229, 195, 120, 0.08);
  }

  .result-list {
    display: grid;
    gap: 8px;
  }

  .result-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    border: 1px solid var(--border-glass);
    border-radius: 10px;
    background: var(--bg-card);
  }

  .result-item:hover {
    border-color: var(--border-glass-bright);
    background: var(--bg-card-hover);
  }

  .result-kind {
    width: 72px;
    flex-shrink: 0;
    font-size: 10px;
    color: var(--gold-primary);
    text-transform: uppercase;
  }

  .result-body {
    display: flex;
    flex-direction: column;
    min-width: 0;
    gap: 3px;
  }

  .result-body strong {
    color: var(--text-main);
    font-size: 13px;
  }

  .result-body small {
    color: var(--text-muted);
    line-height: 1.4;
  }

  .result-arrow {
    margin-left: auto;
    color: var(--gold-primary);
  }
</style>
