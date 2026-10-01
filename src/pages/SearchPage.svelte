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
    padding: 7px 12px;
    border: 1px solid var(--border);
    background: var(--surface-1);
    border-radius: 999px;
    color: var(--ink-muted);
    font-size: 11px;
    font-weight: 500;
    transition: color 0.16s ease, border-color 0.16s ease, background 0.16s ease;
  }

  .kind-filters button.active,
  .kind-filters button:hover {
    color: var(--accent-strong);
    border-color: var(--accent-line);
    background: var(--accent-soft);
  }

  .result-list {
    display: grid;
    gap: 8px;
  }

  .result-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 13px 15px;
    border: 1px solid var(--border);
    border-radius: 12px;
    background: var(--surface-1);
    box-shadow: var(--shadow-sm);
    transition: border-color 0.18s ease, background 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
  }

  .result-item:hover {
    border-color: var(--accent-line);
    background: var(--bg-card-hover);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
  }

  .result-kind {
    width: 72px;
    flex-shrink: 0;
    font-size: 10px;
    font-weight: 700;
    color: var(--accent-strong);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .result-body {
    display: flex;
    flex-direction: column;
    min-width: 0;
    gap: 3px;
  }

  .result-body strong {
    color: var(--ink);
    font-size: 13px;
  }

  .result-body small {
    color: var(--ink-muted);
    line-height: 1.4;
  }

  .result-arrow {
    margin-left: auto;
    color: var(--accent);
  }
</style>
