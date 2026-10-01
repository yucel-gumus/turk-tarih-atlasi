<script lang="ts">
  import type { Snippet } from 'svelte';
  import HUD from '../hud/HUD.svelte';

  let { children }: { children: Snippet } = $props();
</script>

<HUD />

<main class="page-main">
  {@render children()}
</main>

<style>
  .page-main {
    position: relative;
    z-index: 1;
    width: 100%;
    min-width: 0;
    max-width: 1180px;
    margin: 0 auto;
    padding: 96px 20px 96px;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }

  .page-main :global(> *) {
    min-width: 0;
    max-width: 100%;
  }

  @media (max-width: 700px) {
    .page-main {
      padding: 126px 12px 64px;
      gap: 14px;
    }
  }
</style>
