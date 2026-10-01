<script lang="ts">
  import { atlasIndex } from '../../lib/data/lookup';
  import { hrefHome } from '../../lib/router/route';
  import SearchSuggest from './SearchSuggest.svelte';
  import { BookOpen } from '@lucide/svelte';

  /** Sayılar kayıtlardan sayılır; rehber kartı devlet sayılmaz. */
  const toplam = atlasIndex().toplam;
</script>

<header class="hud-root no-print">
  <div class="brand-group">
    <div class="logo-mark">
      <div class="inner-circle"></div>
    </div>
    <div>
      <a class="brand-title" href={hrefHome()}>TÜRK DEVLETLERİ ATLASI</a>
      <p class="brand-subtitle">
        {toplam.devlet} devlet · {toplam.hukumdar} hükümdar · {toplam.savas} savaş
      </p>
    </div>
  </div>

  <SearchSuggest />

  <div class="controls-group">
    <a class="btn-home glass-pill" href={hrefHome()}>
      <BookOpen size={14} aria-hidden="true" />
      <span>Şerit</span>
    </a>
  </div>
</header>

<style>
  /* Sabit krom yüzeyi: metin seçimi kapalıdır, sayfa gövdesinde açıktır. */
  .hud-root {
    position: fixed;
    top: 14px;
    left: 20px;
    right: 20px;
    height: 58px;
    background: rgba(14, 18, 23, 0.72);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--border-glass);
    border-radius: 16px;
    padding: 0 18px;
    display: flex;
    align-items: center;
    gap: 16px;
    z-index: 50;
    box-shadow: 0 16px 36px -6px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    user-select: none;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .logo-mark {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: linear-gradient(135deg, #e5c378 0%, #b88628 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 14px var(--gold-glow);
    flex-shrink: 0;
  }

  .inner-circle {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    border: 2px solid #080a0d;
  }

  .brand-title {
    display: block;
    font-family: var(--font-display);
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.06em;
    background: linear-gradient(180deg, #ffffff 20%, #e5c378 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.15;
  }

  .brand-subtitle {
    margin: 2px 0 0;
    font-size: 10px;
    color: var(--text-dim);
    letter-spacing: 0.01em;
  }

  .controls-group {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .btn-home {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    font-size: 12px;
    font-weight: 600;
    color: var(--text-main);
  }

  @media (max-width: 700px) {
    .hud-root {
      top: 8px;
      left: 8px;
      right: 8px;
      height: auto;
      min-height: 92px;
      flex-wrap: wrap;
      gap: 8px;
      padding: 9px 12px;
    }

    .brand-group {
      min-width: 0;
      gap: 8px;
    }

    .brand-title { font-size: 11px; }
    .brand-subtitle { font-size: 9px; }
    .logo-mark { width: 28px; height: 28px; }
    .controls-group { gap: 0; }
    .btn-home { padding: 6px 8px; }
  }
</style>
