<script lang="ts">
  import type { War } from '../../schemas/atlas.schema';
  import { RESULT_MAP } from '../../lib/data/atlas';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';

  let { war, href, owner }: { war: War; href: string; owner?: string } = $props();
</script>

{#snippet content()}
  <div class="war-info">
    <div class="war-header-row">
      <span class="war-name">{war.name}</span>
      {#if war.when}
        <!-- `when` serbest metin bir tarih ifadesidir; ayrıştırılmaz, olduğu gibi gösterilir. -->
        <span class="war-year">{war.when}</span>
      {/if}
      {#if owner}
        <span class="war-owner">{owner}</span>
      {/if}
    </div>
    {#if war.foe}
      <div class="war-foe">Karşı Taraf: <b>{war.foe}</b></div>
    {/if}
    {#if war.note}
      <p class="war-note">{war.note}</p>
    {/if}
  </div>

  <span class="result-badge {war.result}">{RESULT_MAP[war.result]}</span>

  <ChevronRight size={14} class="war-arrow" aria-hidden="true" />
{/snippet}

<a class="war-item" {href}>{@render content()}</a>

<style>
  .war-item {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 11px 13px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    transition: background 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
  }

  a.war-item:hover {
    background: var(--bg-card-hover);
    border-color: var(--accent-line);
    box-shadow: var(--shadow-sm);
  }

  .war-info {
    flex-grow: 1;
    min-width: 0;
  }

  .war-header-row {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }

  .war-name {
    font-size: 13px;
    font-weight: 600;
    color: var(--ink);
  }

  .war-year {
    font-size: 11px;
    color: var(--ink-dim);
  }

  .war-owner {
    font-size: 10px;
    font-weight: 600;
    color: var(--accent-strong);
    background: var(--accent-soft);
    padding: 1px 6px;
    border-radius: 5px;
  }

  .war-foe {
    font-size: 11px;
    color: var(--ink-muted);
    margin-top: 2px;
  }

  .war-note {
    font-size: 11px;
    color: var(--ink-dim);
    margin: 4px 0 0;
    line-height: 1.5;
  }

  .war-arrow {
    color: var(--ink-dim);
    flex-shrink: 0;
    margin-top: 2px;
  }
</style>
