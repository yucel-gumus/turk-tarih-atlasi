<script lang="ts">
  import type { Snippet } from 'svelte';

  /** İçerik bölümü: başlık, isteğe bağlı ikon ve snippet içerik. */
  let {
    id,
    title,
    icon,
    children,
  }: {
    id?: string;
    title?: string;
    icon?: Snippet;
    children: Snippet;
  } = $props();
</script>

<!-- svelte-ignore a11y_no_noninteractive_tabindex -->
<section {id} class="section-box" tabindex={id ? -1 : undefined}>
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
    scroll-margin-top: 110px;
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
