<script lang="ts">
  import { atlasIndex } from '../../lib/data/lookup';
  import { hrefBattles, hrefHome, hrefMap, hrefTimeMachine } from '../../lib/router/route';
  import { router } from '../../lib/router/router.svelte';
  import SearchSuggest from './SearchSuggest.svelte';
  import BookOpen from '@lucide/svelte/icons/book-open';
  import Compass from '@lucide/svelte/icons/compass';
  import Clock from '@lucide/svelte/icons/clock';
  import Swords from '@lucide/svelte/icons/swords';

  /** Sayılar kayıtlardan sayılır; rehber kartı devlet sayılmaz. */
  const toplam = atlasIndex().toplam;
  const currentRoute = $derived(router.route.name);
</script>

<header class="hud-root no-print">
  <div class="brand-group">
    <div class="logo-mark">
      <div class="inner-circle"></div>
    </div>
    <div>
      <a class="brand-title" href={hrefHome()}>TÜRK DEVLETLERİ ATLASI</a>
      <p class="brand-subtitle">
        {toplam.devlet} devlet · {toplam.hukumdar} hükümdar · {toplam.savas} savaş kaydı
      </p>
    </div>
  </div>

  <SearchSuggest />

  <nav class="controls-group" aria-label="Ana Gezinme">
    <a
      class="nav-pill glass-pill"
      class:active={currentRoute === 'home'}
      aria-current={currentRoute === 'home' ? 'page' : undefined}
      href={hrefHome()}
      title="Kronolojik Zaman Şeridi"
    >
      <BookOpen size={13} aria-hidden="true" />
      <span>Zaman Şeridi</span>
    </a>
    <a
      class="nav-pill glass-pill"
      class:active={currentRoute === 'map'}
      aria-current={currentRoute === 'map' ? 'page' : undefined}
      href={hrefMap()}
      title="Avrasya Coğrafi Haritası"
    >
      <Compass size={13} aria-hidden="true" />
      <span>Harita</span>
    </a>
    <a
      class="nav-pill glass-pill"
      class:active={currentRoute === 'timeMachine'}
      aria-current={currentRoute === 'timeMachine' ? 'page' : undefined}
      href={hrefTimeMachine()}
      title="Tarihsel Zaman Makinesi"
    >
      <Clock size={13} aria-hidden="true" />
      <span>Zaman Makinesi</span>
    </a>
    <a
      class="nav-pill glass-pill"
      class:active={currentRoute === 'battles'}
      aria-current={currentRoute === 'battles' ? 'page' : undefined}
      href={hrefBattles()}
      title="Büyük Savaşlar Gezgini"
    >
      <Swords size={13} aria-hidden="true" />
      <span>Savaşlar</span>
    </a>
  </nav>
</header>

<style>
  /* Sabit krom yüzeyi: metin seçimi kapalıdır, sayfa gövdesinde açıktır. */
  .hud-root {
    position: fixed;
    top: 14px;
    left: 20px;
    right: 20px;
    height: 60px;
    background: var(--surface-translucent);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 0 18px;
    display: flex;
    align-items: center;
    gap: 16px;
    z-index: 50;
    box-shadow: var(--shadow-md);
    user-select: none;
  }

  .brand-group {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .logo-mark {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    background: linear-gradient(135deg, var(--gold-fill) 0%, var(--accent) 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px -2px rgba(122, 77, 15, 0.5);
    flex-shrink: 0;
  }

  .inner-circle {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    border: 2px solid rgba(255, 255, 255, 0.92);
  }

  .brand-title {
    display: block;
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.03em;
    color: var(--ink);
    line-height: 1.15;
  }

  .brand-title:hover {
    color: var(--accent-strong);
  }

  .brand-subtitle {
    margin: 2px 0 0;
    font-size: 10px;
    color: var(--ink-dim);
    letter-spacing: 0.01em;
  }

  .controls-group {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .nav-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 6px 11px;
    font-size: 12px;
    font-weight: 600;
    color: var(--ink-soft);
    border-radius: 999px;
    text-decoration: none;
    transition: all 0.18s ease;
    white-space: nowrap;
    border: 1px solid transparent;
  }

  .nav-pill:hover {
    color: var(--accent-strong);
    background: var(--surface-2);
  }

  .nav-pill.active {
    background: var(--accent);
    color: #ffffff;
    border-color: var(--accent-strong);
    box-shadow: 0 1px 4px rgba(150, 96, 26, 0.3);
  }

  @media (max-width: 950px) {
    .nav-pill span {
      display: none;
    }
    .nav-pill {
      padding: 6px 8px;
    }
  }

  @media (max-width: 1000px) {
    .hud-root {
      top: 8px;
      left: 8px;
      right: 8px;
      height: auto;
      min-height: 92px;
      backdrop-filter: none;
      -webkit-backdrop-filter: none;
      background: var(--surface-1);
      flex-wrap: wrap;
      gap: 8px;
      padding: 9px 12px;
    }

    .brand-group {
      min-width: 0;
      gap: 8px;
    }

    .brand-title { font-size: 11.5px; }
    .brand-subtitle { font-size: 9px; }
    .logo-mark { width: 28px; height: 28px; }
    .controls-group {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: var(--surface-1);
      box-shadow: 0 -4px 18px rgba(40, 33, 20, .08);
      padding: 6px 6px calc(6px + env(safe-area-inset-bottom));
      min-height: 64px;
      gap: 4px;
      width: 100%;
      justify-content: space-around;
      order: 3;
      border-top: 1px solid var(--border);
    }
    .nav-pill span {
      display: inline;
      font-size: 10px;
    }
    .nav-pill {
      padding: 6px 4px;
      min-width: 44px;
      min-height: 48px;
      flex: 1;
      flex-direction: column;
      gap: 4px;
      border-radius: 10px;
    }
  }
</style>
