<script lang="ts">
  import { getAllBattles, getBattleStats, type BattleItem, type FoeCategory } from '../lib/data/battles';
  import { RESULT_MAP } from '../lib/data/atlas';
  import { hrefHome } from '../lib/router/route';
  import type { BattleResult } from '../schemas/atlas.schema';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import Swords from '@lucide/svelte/icons/swords';
  import Search from '@lucide/svelte/icons/search';
  import Trophy from '@lucide/svelte/icons/trophy';
  import ShieldAlert from '@lucide/svelte/icons/shield-alert';
  import Scroll from '@lucide/svelte/icons/scroll';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import { canon } from '../lib/text';

  const allBattles = getAllBattles();
  const stats = getBattleStats();

  let searchQuery = $state('');
  let selectedResult = $state<BattleResult | 'all'>('all');
  let selectedFoe = $state<FoeCategory | 'all'>('all');
  let sortOrder = $state<'asc' | 'desc' | 'name'>('asc');
  let displayLimit = $state(40);

  const foeOptions: FoeCategory[] = [
    'Bizans',
    'Haçlılar',
    'Moğollar',
    'Çin',
    'Rus',
    'Safevî / İran',
    'Avrupa / Balkan',
    'Türk / İç Mücadele',
    'Diğer',
  ];

  const filteredBattles = $derived.by(() => {
    const q = canon(searchQuery.trim());

    return allBattles
      .filter((b) => {
        if (selectedResult !== 'all' && b.result !== selectedResult) return false;
        if (selectedFoe !== 'all' && b.foeCategory !== selectedFoe) return false;
        if (q.length > 0) {
          const text = canon(`${b.name} ${b.foe} ${b.when} ${b.stateName} ${b.rulerName} ${b.note}`);
          if (!text.includes(q)) return false;
        }
        return true;
      })
      .sort((a, b) => {
        if (sortOrder === 'asc') return a.year - b.year || a.name.localeCompare(b.name, 'tr');
        if (sortOrder === 'desc') return b.year - a.year || a.name.localeCompare(b.name, 'tr');
        return a.name.localeCompare(b.name, 'tr');
      });
  });

  const visibleBattles = $derived(filteredBattles.slice(0, displayLimit));

  function loadMore() {
    displayLimit += 40;
  }

  function resetFilters() {
    searchQuery = '';
    selectedResult = 'all';
    selectedFoe = 'all';
    sortOrder = 'asc';
    displayLimit = 40;
  }
</script>

<Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: 'Savaşlar Gezgini' }]} />

<PageHeader
  eyebrow="Tarihsel Çatışmalar ve Seferler"
  title="Büyük Savaşlar ve Meydan Muharebeleri"
  subtitle="80 Türk devletinin katıldığı 791 savaşın hasımları, sonuçları ve tarihsel kayıtları"
>
  {#snippet badges()}
    <span class="meta-pill"><Swords size={13} aria-hidden="true" /> {stats.total} Savaş</span>
    <span class="result-badge zafer">Zafer · {stats.byResult.zafer}</span>
    <span class="result-badge yenilgi">Yenilgi · {stats.byResult.yenilgi}</span>
    <span class="result-badge antlasma">Antlaşma · {stats.byResult.antlasma}</span>
  {/snippet}
</PageHeader>

<!-- İstatistik Panosu -->
<div class="stats-grid">
  <div class="stat-card">
    <div class="stat-icon-wrapper victory">
      <Trophy size={18} aria-hidden="true" />
    </div>
    <div class="stat-details">
      <span class="stat-value">{stats.byResult.zafer}</span>
      <span class="stat-label">Zafer (%{Math.round((stats.byResult.zafer / stats.total) * 100)})</span>
    </div>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrapper defeat">
      <ShieldAlert size={18} aria-hidden="true" />
    </div>
    <div class="stat-details">
      <span class="stat-value">{stats.byResult.yenilgi}</span>
      <span class="stat-label">Yenilgi (%{Math.round((stats.byResult.yenilgi / stats.total) * 100)})</span>
    </div>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrapper treaty">
      <Scroll size={18} aria-hidden="true" />
    </div>
    <div class="stat-details">
      <span class="stat-value">{stats.byResult.antlasma}</span>
      <span class="stat-label">Antlaşma / Diplomatik</span>
    </div>
  </div>

  <div class="stat-card">
    <div class="stat-icon-wrapper conflict">
      <Swords size={18} aria-hidden="true" />
    </div>
    <div class="stat-details">
      <span class="stat-value">{stats.byFoe['Türk / İç Mücadele']}</span>
      <span class="stat-label">İç Mücadele & Taht Savaşı</span>
    </div>
  </div>
</div>

<!-- Filtre ve Arama Alanı -->
<SectionBox title="Savaş Süzgeci">
  <div class="filter-controls">
    <div class="search-input-group">
      <Search size={16} class="search-icon" aria-hidden="true" />
      <input
        type="search"
        class="search-field"
        placeholder="Savaş adı, hasım birlik, hükümdar veya şehir ara..."
        bind:value={searchQuery}
      />
      {#if searchQuery}
        <button class="clear-btn" type="button" onclick={() => (searchQuery = '')}>Temizle</button>
      {/if}
    </div>

    <!-- Sonuç Filtresi -->
    <div class="pill-group-wrapper">
      <span class="pill-group-title">Sonuç:</span>
      <div class="pill-group">
        <button
          type="button"
          class="filter-pill"
          class:active={selectedResult === 'all'}
          onclick={() => (selectedResult = 'all')}
        >
          Tümü ({stats.total})
        </button>
        <button
          type="button"
          class="filter-pill zafer-pill"
          class:active={selectedResult === 'zafer'}
          onclick={() => (selectedResult = 'zafer')}
        >
          Zafer ({stats.byResult.zafer})
        </button>
        <button
          type="button"
          class="filter-pill yenilgi-pill"
          class:active={selectedResult === 'yenilgi'}
          onclick={() => (selectedResult = 'yenilgi')}
        >
          Yenilgi ({stats.byResult.yenilgi})
        </button>
        <button
          type="button"
          class="filter-pill antlasma-pill"
          class:active={selectedResult === 'antlasma'}
          onclick={() => (selectedResult = 'antlasma')}
        >
          Antlaşma ({stats.byResult.antlasma})
        </button>
        <button
          type="button"
          class="filter-pill"
          class:active={selectedResult === 'belirsiz'}
          onclick={() => (selectedResult = 'belirsiz')}
        >
          Belirsiz ({stats.byResult.belirsiz + stats.byResult.sonucsuz})
        </button>
      </div>
    </div>

    <!-- Hasım Odak Filtresi -->
    <div class="pill-group-wrapper">
      <span class="pill-group-title">Hasım Taraf:</span>
      <div class="pill-group wrap">
        <button
          type="button"
          class="filter-pill"
          class:active={selectedFoe === 'all'}
          onclick={() => (selectedFoe = 'all')}
        >
          Tüm Hasımlar
        </button>
        {#each foeOptions as foe (foe)}
          <button
            type="button"
            class="filter-pill"
            class:active={selectedFoe === foe}
            onclick={() => (selectedFoe = foe)}
          >
            {foe} ({stats.byFoe[foe]})
          </button>
        {/each}
      </div>
    </div>

    <!-- Sıralama ve Sonuç Sayısı -->
    <div class="sort-and-count">
      <div class="result-count">
        <b>{filteredBattles.length}</b> savaş listeleniyor
        {#if filteredBattles.length !== stats.total}
          <button type="button" class="reset-link" onclick={resetFilters}>Filtreleri sıfırla</button>
        {/if}
      </div>

      <div class="sort-control">
        <label for="sort-select" class="sort-label">Sırala:</label>
        <select id="sort-select" class="sort-select" bind:value={sortOrder}>
          <option value="asc">Kronolojik (Eskiden Yeniye)</option>
          <option value="desc">Kronolojik (Yeniden Eskiye)</option>
          <option value="name">Savaş Adına Göre (A-Z)</option>
        </select>
      </div>
    </div>
  </div>
</SectionBox>

<!-- Savaş Listesi -->
<div class="battles-container">
  {#if visibleBattles.length === 0}
    <div class="empty-state">
      <p>Arama kriterlerine uygun savaş kaydı bulunamadı.</p>
      <button type="button" class="reset-btn" onclick={resetFilters}>Süzgeci Temizle</button>
    </div>
  {:else}
    <div class="battles-grid">
      {#each visibleBattles as b (b.id)}
        <a class="battle-card" href={b.href}>
          <div class="card-top">
            <div class="title-and-date">
              <h3 class="battle-title">{b.name}</h3>
              <span class="battle-when">{b.when}</span>
            </div>
            <span class="result-badge {b.result}">{RESULT_MAP[b.result]}</span>
          </div>

          <div class="parties-row">
            <div class="party-tag owner-tag">
              <span class="tag-label">Devlet & Hükümdar:</span>
              <span class="tag-name">{b.stateName} · <b>{b.rulerName}</b></span>
            </div>
            <div class="party-tag foe-tag">
              <span class="tag-label">Hasım Taraf:</span>
              <span class="tag-name"><b>{b.foe}</b></span>
            </div>
          </div>

          {#if b.note}
            <p class="battle-note">{b.note}</p>
          {/if}

          <div class="card-footer">
            <span class="category-pill">{b.foeCategory}</span>
            <span class="view-detail">
              İncele <ChevronRight size={13} aria-hidden="true" />
            </span>
          </div>
        </a>
      {/each}
    </div>

    {#if displayLimit < filteredBattles.length}
      <div class="load-more-row">
        <button type="button" class="load-more-btn" onclick={loadMore}>
          Daha Fazla Göster ({filteredBattles.length - displayLimit} savaş kaldı)
        </button>
      </div>
    {/if}
  {/if}
</div>

<style>
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 12px;
  }

  .stat-card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: var(--shadow-sm);
  }

  .stat-icon-wrapper {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  .stat-icon-wrapper.victory {
    background: var(--victory-bg);
    color: var(--victory-ink);
  }

  .stat-icon-wrapper.defeat {
    background: var(--defeat-bg);
    color: var(--defeat-ink);
  }

  .stat-icon-wrapper.treaty {
    background: var(--treaty-bg);
    color: var(--treaty-ink);
  }

  .stat-icon-wrapper.conflict {
    background: var(--warn-bg);
    color: var(--warn-ink);
  }

  .stat-details {
    display: flex;
    flex-direction: column;
  }

  .stat-value {
    font-family: var(--font-serif);
    font-size: 22px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.1;
  }

  .stat-label {
    font-size: 11px;
    color: var(--ink-dim);
    margin-top: 2px;
  }

  .filter-controls {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .search-input-group {
    position: relative;
    display: flex;
    align-items: center;
  }

  .search-input-group :global(.search-icon) {
    position: absolute;
    left: 14px;
    color: var(--ink-dim);
    pointer-events: none;
  }

  .search-field {
    width: 100%;
    padding: 10px 80px 10px 38px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 14px;
    color: var(--ink);
    outline: none;
    transition: border-color 0.18s ease, background 0.18s ease;
  }

  .search-field:focus {
    background: var(--surface-1);
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-soft);
  }

  .clear-btn {
    position: absolute;
    right: 12px;
    padding: 4px 8px;
    font-size: 11px;
    background: var(--surface-3);
    border: none;
    border-radius: 6px;
    color: var(--ink-dim);
    cursor: pointer;
  }

  .pill-group-wrapper {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .pill-group-title {
    font-size: 11px;
    font-weight: 600;
    color: var(--ink-dim);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .pill-group {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 2px;
  }

  .pill-group.wrap {
    flex-wrap: wrap;
  }

  .filter-pill {
    padding: 5px 11px;
    font-size: 12px;
    font-weight: 500;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--surface-1);
    color: var(--ink-soft);
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.18s ease;
  }

  .filter-pill:hover {
    background: var(--surface-2);
    border-color: var(--border-strong);
  }

  .filter-pill.active {
    background: var(--accent);
    border-color: var(--accent);
    color: #ffffff;
  }

  .filter-pill.zafer-pill.active {
    background: var(--accent-victory);
    border-color: var(--accent-victory);
  }

  .filter-pill.yenilgi-pill.active {
    background: var(--accent-defeat);
    border-color: var(--accent-defeat);
  }

  .filter-pill.antlasma-pill.active {
    background: var(--accent-treaty);
    border-color: var(--accent-treaty);
  }

  .sort-and-count {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 6px;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
    gap: 8px;
  }

  .result-count {
    font-size: 13px;
    color: var(--ink-dim);
  }

  .reset-link {
    background: none;
    border: none;
    color: var(--accent);
    font-size: 12px;
    cursor: pointer;
    text-decoration: underline;
    margin-left: 8px;
    padding: 0;
  }

  .sort-control {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .sort-label {
    font-size: 12px;
    color: var(--ink-dim);
  }

  .sort-select {
    padding: 4px 10px;
    font-size: 12px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--ink);
    outline: none;
  }

  .battles-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 12px;
  }

  .battle-card {
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    text-decoration: none;
    color: inherit;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .battle-card:hover {
    transform: translateY(-2px);
    border-color: var(--accent-line);
    box-shadow: var(--shadow-md);
  }

  .card-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
  }

  .battle-title {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.25;
  }

  .battle-when {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    margin-top: 2px;
  }

  .parties-row {
    display: flex;
    flex-direction: column;
    gap: 4px;
    padding: 8px 10px;
    background: var(--surface-2);
    border-radius: 8px;
    font-size: 12px;
  }

  .party-tag {
    display: flex;
    gap: 6px;
    align-items: baseline;
  }

  .tag-label {
    font-size: 10px;
    text-transform: uppercase;
    color: var(--ink-dim);
    flex-shrink: 0;
    width: 95px;
  }

  .tag-name {
    color: var(--ink);
    word-break: break-word;
  }

  .battle-note {
    margin: 0;
    font-size: 12.5px;
    line-height: 1.45;
    color: var(--ink-soft);
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .card-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    padding-top: 8px;
    border-top: 1px solid var(--border);
  }

  .category-pill {
    font-size: 10px;
    padding: 2px 7px;
    border-radius: 4px;
    background: var(--surface-3);
    color: var(--ink-dim);
    font-weight: 500;
  }

  .view-detail {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 3px;
  }

  .load-more-row {
    display: flex;
    justify-content: center;
    margin-top: 20px;
  }

  .load-more-btn {
    padding: 10px 24px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 10px;
    font-size: 13px;
    font-weight: 600;
    color: var(--accent);
    cursor: pointer;
    box-shadow: var(--shadow-sm);
    transition: background 0.18s ease, border-color 0.18s ease;
  }

  .load-more-btn:hover {
    background: var(--surface-2);
    border-color: var(--accent-line);
  }

  .empty-state {
    text-align: center;
    padding: 48px 16px;
    background: var(--surface-1);
    border: 1px dashed var(--border);
    border-radius: 12px;
    color: var(--ink-dim);
  }

  .reset-btn {
    margin-top: 10px;
    padding: 8px 16px;
    background: var(--accent);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
  }
</style>
