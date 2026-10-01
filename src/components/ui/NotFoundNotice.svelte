<script lang="ts">
  import { hrefHome } from '../../lib/router/route';

  /** Adres sözdizimi hatalı ya da kayıt bulunamadı — ikisi de aynı bildirimi görür. */
  let { raw }: { raw?: string } = $props();
</script>

<div class="notice glass-panel">
  <h2 class="notice-title">Bu adres bir kayda karşılık gelmiyor</h2>
  <p class="body-text">
    Bağlantı eksik ya da bozuk olabilir. Adres sessizce başka bir sayfaya yönlendirilmez,
    çünkü o zaman kırık bağlantı fark edilmezdi.
  </p>
  {#if raw}
    <code class="attempted">{raw}</code>
  {/if}
  <a class="home-link" href={hrefHome()}>Açılış sayfasına dön</a>
</div>

<style>
  .notice {
    border-radius: 14px;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-start;
  }

  .notice-title {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 21px;
    color: var(--ink);
  }

  .attempted {
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 12px;
    color: var(--ink-soft);
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 6px 10px;
    word-break: break-all;
  }

  .home-link {
    display: inline-flex;
    align-items: center;
    padding: 8px 15px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
    color: var(--accent-strong);
    background: var(--accent-soft);
    border: 1px solid var(--accent-line);
    transition: background 0.18s ease;
  }

  .home-link:hover {
    background: rgba(150, 96, 26, 0.18);
  }
</style>
