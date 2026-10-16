<script lang="ts">
  const SITE = 'https://yucelgumus.dev/';
</script>

<footer class="site-footer">
  <p class="made">Tasarlayan ve geliştiren</p>
  <a class="author" href={SITE} target="_blank" rel="noopener author">
    <span class="mark" aria-hidden="true">YG</span>
    <span class="text">
      <strong>Yücel Gümüş</strong>
      <span>Full Stack Developer &amp; Yazılım Mühendisi</span>
    </span>
    <span class="link">yucelgumus.dev <span aria-hidden="true">→</span></span>
  </a>
</footer>

<style>
  /* Ağacın üstünde, ekranın altında ortalı yazar kartı; ağacı sürüklemeyi engellemez. */
  .site-footer {
    position: fixed;
    left: 50%;
    bottom: calc(14px + env(safe-area-inset-bottom));
    transform: translateX(-50%);
    display: grid;
    justify-items: center;
    gap: 6px;
    pointer-events: none;
    max-width: calc(100vw - 24px);
  }
  .made {
    margin: 0;
    padding: 2px 10px;
    border-radius: 999px;
    background: color-mix(in srgb, var(--paper) 85%, transparent);
    color: var(--ink-muted);
    font-size: 10.5px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
  }
  .author {
    pointer-events: auto;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 8px 8px 8px;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 999px;
    box-shadow: var(--shadow);
    color: var(--ink);
    text-decoration: none;
    transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
  }
  .author:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
  }
  .author:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
  }
  .mark {
    display: grid;
    place-items: center;
    width: 40px;
    height: 40px;
    flex: none;
    border-radius: 50%;
    background: var(--accent);
    color: var(--surface);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 0.04em;
  }
  .text {
    display: grid;
    line-height: 1.25;
    min-width: 0;
  }
  .text strong {
    font-family: var(--serif);
    font-size: 15.5px;
  }
  .text span {
    color: var(--ink-muted);
    font-size: 12px;
    white-space: nowrap;
  }
  .link {
    flex: none;
    margin-left: 4px;
    padding: 8px 14px;
    border-radius: 999px;
    background: var(--accent-soft);
    color: var(--accent);
    font-weight: 700;
    font-size: 13px;
    white-space: nowrap;
    transition: background 0.2s, color 0.2s;
  }
  .author:hover .link {
    background: var(--accent);
    color: var(--surface);
  }

  @media (max-width: 560px) {
    .made,
    .text span {
      display: none;
    }
    .author {
      gap: 10px;
      padding: 6px;
    }
    .mark {
      width: 34px;
      height: 34px;
      font-size: 12.5px;
    }
    .text strong {
      font-size: 14px;
      white-space: nowrap;
    }
    .link {
      padding: 7px 12px;
      font-size: 12.5px;
    }
  }
</style>
