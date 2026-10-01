<script lang="ts">
  import { ChevronRight } from '@lucide/svelte';

  /** Kırıntı yolu: son öğe bağlantısızdır ve geçerli sayfayı işaretler. */
  let { items }: { items: { label: string; href?: string }[] } = $props();
</script>

<nav class="breadcrumb" aria-label="Sayfa yolu">
  <ol>
    {#each items as item, i (item.label + i)}
      <li>
        {#if item.href}
          <a href={item.href}>{item.label}</a>
        {:else}
          <span aria-current="page">{item.label}</span>
        {/if}
        {#if i < items.length - 1}
          <ChevronRight size={12} aria-hidden="true" />
        {/if}
      </li>
    {/each}
  </ol>
</nav>

<style>
  .breadcrumb ol {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }

  .breadcrumb li {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    color: var(--text-dim);
  }

  .breadcrumb a {
    color: var(--text-muted);
    transition: color 0.15s ease;
  }

  .breadcrumb a:hover {
    color: var(--gold-primary);
  }

  .breadcrumb [aria-current='page'] {
    color: var(--text-main);
  }
</style>
