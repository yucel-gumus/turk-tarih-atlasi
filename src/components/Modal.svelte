<script lang="ts">
  import { onMount, type Snippet } from 'svelte';
  import { modals } from '../lib/modals.svelte';

  interface Props {
    depth: number;
    crumbs: string[];
    kicker: string;
    title: string;
    subtitle?: string;
    accent?: string;
    children: Snippet;
  }
  const { depth, crumbs, kicker, title, subtitle = '', accent = 'var(--accent)', children }: Props = $props();

  let dialog: HTMLDialogElement;
  const top = $derived(depth === modals.items.length);

  onMount(() => {
    dialog.showModal();
    return () => dialog.close();
  });

  function onCancel(e: Event) {
    e.preventDefault();
    if (top) modals.back();
  }

  function onBackdrop(e: MouseEvent) {
    if (e.target === dialog) modals.back();
  }
</script>

<!-- svelte-ignore a11y_click_events_have_key_events, a11y_no_noninteractive_element_interactions -->
<dialog
  bind:this={dialog}
  class="modal"
  style:--accent-c={accent}
  style:--lvl={Math.min(depth - 1, 6)}
  aria-labelledby="modal-title-{depth}"
  oncancel={onCancel}
  onclick={onBackdrop}
>
  <div class="sheet">
    <header>
      <div class="bar">
        {#if depth > 1}
          <button type="button" class="back" onclick={() => modals.back()} aria-label="Önceki pencereye dön">
            ← Geri
          </button>
        {/if}
        <nav class="crumbs" aria-label="Açık pencereler">
          {#each crumbs as c, i}
            {#if i < crumbs.length - 1}
              <button type="button" onclick={() => modals.closeTo(i)}>{c}</button>
              <span aria-hidden="true">›</span>
            {:else}
              <span class="here" aria-current="page">{c}</span>
            {/if}
          {/each}
        </nav>
        <button type="button" class="close" onclick={() => modals.closeAll()} aria-label="Tümünü kapat, soy ağacına dön">✕</button>
      </div>
      <p class="kicker">{kicker}</p>
      <h2 id="modal-title-{depth}">{title}</h2>
      {#if subtitle}<p class="subtitle">{subtitle}</p>{/if}
    </header>
    <div class="body">
      {@render children()}
    </div>
  </div>
</dialog>

<style>
  .modal {
    padding: 0;
    border: 0;
    background: transparent;
    max-width: none;
    max-height: none;
    width: 100%;
    height: 100%;
    margin: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }
  .modal::backdrop {
    background: var(--backdrop);
  }
  .sheet {
    --off: calc(var(--lvl) * 14px);
    position: relative;
    width: min(760px, calc(100vw - 48px));
    max-height: calc(100dvh - 64px);
    margin-top: var(--off);
    display: flex;
    flex-direction: column;
    background: var(--surface);
    color: var(--ink);
    border-radius: 18px;
    border-top: 5px solid var(--accent-c);
    box-shadow: var(--shadow-lg);
    overflow: hidden;
    animation: rise 0.2s ease-out;
  }
  @keyframes rise {
    from {
      opacity: 0;
      transform: translateY(14px) scale(0.985);
    }
  }
  header {
    padding: 14px 24px 16px;
    border-bottom: 1px solid var(--line);
  }
  .bar {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }
  .crumbs {
    flex: 1;
    min-width: 0;
    display: flex;
    align-items: center;
    gap: 4px;
    overflow-x: auto;
    scrollbar-width: none;
    font-size: 12.5px;
    color: var(--ink-muted);
    white-space: nowrap;
  }
  .crumbs button {
    border: 0;
    background: none;
    padding: 2px 4px;
    border-radius: 6px;
    color: var(--ink-muted);
    cursor: pointer;
    text-decoration: underline;
    text-decoration-color: var(--line-strong);
    text-underline-offset: 3px;
  }
  .crumbs button:hover {
    color: var(--ink);
  }
  .crumbs .here {
    padding: 2px 4px;
    color: var(--ink);
    font-weight: 600;
  }
  .back,
  .close {
    flex: none;
    border: 1px solid var(--line);
    background: var(--surface-2);
    border-radius: 999px;
    cursor: pointer;
    color: var(--ink-soft);
  }
  .back {
    padding: 4px 12px;
    font-size: 13px;
    font-weight: 600;
  }
  .close {
    width: 32px;
    height: 32px;
    font-size: 14px;
  }
  .back:hover,
  .close:hover {
    background: var(--line);
  }
  .kicker {
    margin: 0;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--accent-c);
  }
  h2 {
    margin: 2px 0 0;
    font-family: var(--serif);
    font-size: 28px;
    line-height: 1.15;
  }
  .subtitle {
    margin: 4px 0 0;
    color: var(--ink-muted);
    font-size: 14px;
  }
  .body {
    padding: 18px 24px 28px;
    overflow-y: auto;
    overscroll-behavior: contain;
  }

  @media (max-width: 640px) {
    .modal {
      align-items: flex-end;
    }
    .sheet {
      width: 100%;
      max-height: calc(100dvh - 24px - var(--off));
      border-radius: 18px 18px 0 0;
      margin-top: 0;
    }
    header {
      padding: 12px 16px 14px;
    }
    .body {
      padding: 16px 16px calc(28px + env(safe-area-inset-bottom));
    }
    h2 {
      font-size: 24px;
    }
  }
</style>
