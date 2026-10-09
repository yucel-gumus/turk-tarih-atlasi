<script lang="ts">
  import type { Snippet } from 'svelte';
  import HUD from '../hud/HUD.svelte';

  let { children }: { children: Snippet } = $props();
</script>

<a class="skip-link" href="#main-content" onclick={(event) => { event.preventDefault(); document.getElementById('main-content')?.focus(); }}>İçeriğe geç</a>
<HUD />

<main id="main-content" tabindex="-1" class="page-main">
  {@render children()}
</main>

<style>
  .page-main:focus { outline: none; }

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

  @media (max-width: 1000px) {
    .page-main {
      padding: 120px 12px calc(100px + env(safe-area-inset-bottom));
      gap: 14px;
    }
  }
</style>
