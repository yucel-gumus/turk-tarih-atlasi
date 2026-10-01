<script lang="ts">
  import type { Snippet } from 'svelte';

  let {
    eyebrow,
    title,
    subtitle,
    badges,
  }: { eyebrow?: string; title: string; subtitle?: string; badges?: Snippet } = $props();
</script>

<header class="page-header">
  {#if eyebrow}
    <span class="eyebrow">{eyebrow}</span>
  {/if}
  <h1 class="page-title">{title}</h1>
  {#if subtitle}
    <p class="page-subtitle">{subtitle}</p>
  {/if}
  {#if badges}
    <div class="badge-row">{@render badges()}</div>
  {/if}
</header>

<style>
  .badge-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 6px;
  }
</style>
