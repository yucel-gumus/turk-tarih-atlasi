<script lang="ts">
  import type { Snippet } from 'svelte';

  /** İçerik bölümü: başlık, isteğe bağlı ikon ve snippet içerik. */
  let { title, icon, children }: { title?: string; icon?: Snippet; children: Snippet } = $props();
</script>

<section class="section-box">
  {#if title}
    <h2 class="section-heading">
      {#if icon}
        {@render icon()}
      {/if}
      <span>{title}</span>
    </h2>
  {/if}
  {@render children()}
</section>

<style>
  .section-box {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 18px;
    display: flex;
    flex-direction: column;
    gap: 11px;
    box-shadow: var(--shadow-sm);
  }

  .section-heading {
    margin: 0;
    font-size: 12px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--ink);
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }
</style>
