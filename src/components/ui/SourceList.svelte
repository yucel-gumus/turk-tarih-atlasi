<script lang="ts">
  import type { Source } from '../../schemas/atlas.schema';
  import { ExternalLink } from '@lucide/svelte';

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
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    font-size: 12px;
    color: var(--gold-primary);
    transition: background 0.2s ease;
  }

  .source-link:hover {
    background: rgba(229, 195, 120, 0.08);
    border-color: var(--border-glass-bright);
  }
</style>
