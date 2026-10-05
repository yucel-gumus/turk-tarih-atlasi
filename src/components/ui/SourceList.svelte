<script lang="ts">
  import type { Source } from '../../schemas/atlas.schema';
  import ExternalLink from '@lucide/svelte/icons/external-link';

  let { sources }: { sources: Source[] } = $props();
</script>

<div class="sources-list">
  {#each sources as source, i (source.url + i)}
    <a href={source.url} target="_blank" rel="noopener noreferrer" class="source-link">
      <span>{source.title}</span>
      <ExternalLink size={12} aria-hidden="true" />
    </a>
  {/each}
</div>

<style>
  .sources-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .source-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    padding: 9px 13px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 9px;
    font-size: 12.5px;
    font-weight: 500;
    color: var(--accent-strong);
    transition: background 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
  }

  .source-link:hover {
    background: var(--accent-soft);
    border-color: var(--accent-line);
    box-shadow: var(--shadow-sm);
  }
</style>
