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
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .section-heading {
    margin: 0;
    font-size: 13px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--gold-primary);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
</style>
