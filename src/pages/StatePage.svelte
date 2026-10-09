<script lang="ts">
  import { atlasIndex, RESULT_ORDER, stateWarRecord, stateWars } from '../lib/data/lookup';
  import { CONFIDENCE_MAP, REGION_MAP, RESULT_MAP, yearLabel } from '../lib/data/atlas';
  import { hrefGuide, hrefHome, hrefWar, SEG } from '../lib/router/route';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import MetaCard from '../components/ui/MetaCard.svelte';
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';
  import RulerCard from '../components/ui/RulerCard.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import SourceList from '../components/ui/SourceList.svelte';
  import WarRow from '../components/ui/WarRow.svelte';
  import DynastyTree from '../components/ui/DynastyTree.svelte';
  import { tick } from 'svelte';
  import Crown from '@lucide/svelte/icons/crown';
  import Swords from '@lucide/svelte/icons/swords';

  let { stateId }: { stateId: string } = $props();

  let rulerViewMode = $state<'cards' | 'tree'>('cards');
  async function jumpToSection(id: string, tree = false) {
    if (tree) rulerViewMode = 'tree';
    await tick();
    const target = document.getElementById(id);
    target?.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    target?.focus({ preventScroll: true });
  }
  function shortSummary(text: string) {
    return text.split(/(?<=[.!?])\s+(?=[A-ZÇĞİÖŞÜ])/u).slice(0, 2).join(' ');
  }


  const index = atlasIndex();
  /**
   * Sayfa üç durumdan birindedir: devlet kaydı, rehber kaydı ya da hiç kayıt.
   * Tek bir birleşimde toplanır ki şablonda her alan daraltılmış (narrowed) olsun;
   * rehber kaydı devlet sayfası olarak çizilmez, uydurma tarihleri gösterilmez.
   */
  const page = $derived.by(() => {
    const found = index.statesById.get(stateId) ?? null;
    if (!found) return null;
    if (found.region === 'giris') {
      return { kind: 'guide' as const, record: found };
    }
    // `regionId` ayrı bir sabite alınır: böylece tip 'giris' dışına daralır ve
    // bölge süzgeci bağlantısı doğru tipte üretilir.
    const regionId = found.region;
    const state = found;
    return {
      kind: 'state' as const,
      state,
      regionId,
      region: REGION_MAP[regionId],
      wars: stateWars(state),
      warSummary: stateWarRecord(state),
    };
  });
</script>

{#if !page}
  <NotFoundNotice raw={`#/${SEG.state}/${stateId}`} />
{:else if page.kind === 'guide'}
  <Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: page.record.name }]} />
  <PageHeader eyebrow="Kayıt türü" title={page.record.name} subtitle={page.record.short} />
  <p class="honesty-note">
    Bu kayıt bir Türk devleti değil, atlasın nasıl okunacağını anlatan rehberdir; devlet
    sayfalarının alanlarını taşımaz. Kayıtta duran tarih değerleri şema gereği yazılmıştır,
    ölçülmüş bir aralık değildir ve bu yüzden hiçbir yerde gösterilmez.
  </p>
  <SectionBox title="Rehber">
    <a class="inline-link" href={hrefGuide()}>Rehber sayfasını aç</a>
  </SectionBox>
{:else}
  <Breadcrumb
    items={[
      { label: 'Atlas', href: hrefHome() },
      { label: page.region.name, href: hrefHome(page.regionId) },
      { label: page.state.name },
    ]}
  />

  <PageHeader
    eyebrow={page.region.name}
    title={page.state.name}
    subtitle={page.state.short !== page.state.name ? page.state.short : undefined}
  >
    {#snippet badges()}
      <span class="state-indicator" style="background: {page.region.color}"></span>
      <span class="dates-tag">{yearLabel(page.state.start)} – {yearLabel(page.state.end)}</span>
      {#if page.state.rulers.length > 0}
        <span class="meta-pill rulers-count">
          <Crown size={12} class="icon-ruler" aria-hidden="true" />
          {page.state.rulers.length} hükümdar
        </span>
      {/if}
      {#if page.warSummary.total > 0}
        <span class="meta-pill">
          <Swords size={12} class="icon-war" aria-hidden="true" />
          {page.warSummary.total} savaş kaydı
        </span>
      {/if}
      {#if page.state.confidence !== 'kayit'}
        <span class="confidence-tag {page.state.confidence}">
          {CONFIDENCE_MAP[page.state.confidence]}
        </span>
      {/if}
    {/snippet}
  </PageHeader>

  {#if page.state.confidence !== 'kayit' && page.state.confidenceNote}
    <p class="honesty-note">{page.state.confidenceNote}</p>
  {/if}

  {#if page.state.summary}
    <div class="state-intro">
      <p class="body-text">{shortSummary(page.state.summary)}</p>
      {#if shortSummary(page.state.summary) !== page.state.summary}
        <details><summary>Özetin tamamını oku</summary><p class="body-text">{page.state.summary}</p></details>
      {/if}
    </div>
  {/if}
  <nav class="section-nav" aria-label="Devlet sayfası bölümleri">
    <button type="button" onclick={() => jumpToSection('state-rulers')}>Hükümdarlar</button>
    <button type="button" onclick={() => jumpToSection('state-wars')}>Savaşlar</button>
    <button type="button" onclick={() => jumpToSection('state-rulers', true)}>Hanedan</button>
    <button type="button" onclick={() => jumpToSection('state-sources')}>Kaynaklar</button>
  </nav>
  <div class="meta-section">
    <MetaCard
      label="Tarih Aralığı"
      value="{yearLabel(page.state.start)} – {yearLabel(page.state.end)}"
    />
    <MetaCard
      label="Başkent"
      value={page.state.capital || 'Kayıtta yok'}
      note={page.state.capital ? undefined : 'Bu kayıtta başkent alanı boş; "bilinmiyor" demek değil.'}
    />
    <MetaCard label="İnanç" value={page.state.religion.split('(')[0].trim()} />
    <MetaCard label="Bölge" value={page.region.name} />
    <MetaCard label="Diğer adları" value={page.state.aliases.join(' · ')} />
  </div>

  {#if page.state.startNote || page.state.endNote || page.state.religion.includes('(')}
    <details class="reading-note">
      <summary>Tarih ve inanç bilgisine ilişkin kaynak notları</summary>
      {#if page.state.startNote}<p class="body-text">{page.state.startNote}</p>{/if}
      {#if page.state.endNote}<p class="body-text">{page.state.endNote}</p>{/if}
      {#if page.state.religion.includes('(')}<p class="body-text">İnanç: {page.state.religion}</p>{/if}
    </details>
  {/if}

  <SectionBox id="state-rulers" title={`Hükümdarlar · ${page.state.rulers.length}`}>
    {#snippet icon()}
      <Crown size={14} class="icon-ruler" aria-hidden="true" />
    {/snippet}
    {#if page.state.rulers.length === 0}
      <p class="honesty-note">
        Bu kayıtta hükümdar listesi yok. Liste boş bırakılmadı; kayıtta adı geçen hükümdar
        bilgisi bulunmuyor.
      </p>
    {:else}
      <div class="ruler-view-switcher">
        <button
          type="button"
          class="view-toggle-btn"
          class:active={rulerViewMode === 'cards'}
          aria-pressed={rulerViewMode === 'cards'}
          onclick={() => (rulerViewMode = 'cards')}
        >
          Kronolojik Kartlar ({page.state.rulers.length})
        </button>
        <button
          type="button"
          class="view-toggle-btn"
          class:active={rulerViewMode === 'tree'}
          aria-pressed={rulerViewMode === 'tree'}
          onclick={() => (rulerViewMode = 'tree')}
        >
          Hanedan Soyağacı
        </button>
      </div>

      {#if rulerViewMode === 'cards'}
        <div class="ruler-grid">
          {#each page.state.rulers as ruler (ruler.id)}
            <RulerCard {ruler} state={page.state} />
          {/each}
        </div>
      {:else}
        <DynastyTree state={page.state} />
      {/if}
    {/if}
  </SectionBox>

  {#if page.warSummary.total > 0}
    <SectionBox id="state-wars" title="Savaş Kaydı">
      {#snippet icon()}
        <Swords size={14} class="icon-war" aria-hidden="true" />
      {/snippet}
      <div class="meta-pills">
        {#each RESULT_ORDER as result (result)}
          {#if page.warSummary.byResult[result] > 0}
            <span class="result-badge {result}">
              {RESULT_MAP[result]} · {page.warSummary.byResult[result]}
            </span>
          {/if}
        {/each}
      </div>
      <!-- `when` serbest metin olduğu için (504 savaşın 172'si tek yıl değil) liste
           tarihe göre değil, hükümdar sırasına göre dizilir. -->
      <details class="war-details">
        <summary>{page.warSummary.total} savaş kaydının tamamını göster</summary>
        <div class="war-list-all">
          {#each page.wars as entry (entry.ruler.id + entry.index)}
            <WarRow
              war={entry.war}
              owner={entry.ruler.name}
              href={hrefWar(page.state.id, entry.ruler.id, entry.index, entry.war.name)}
            />
          {/each}
        </div>
      </details>
    </SectionBox>
  {:else}
    <SectionBox id="state-wars" title="Savaş Kaydı">
      {#snippet icon()}
        <Swords size={14} class="icon-war" aria-hidden="true" />
      {/snippet}
      <p class="honesty-note">
        Bu devletin hükümdar kayıtlarında savaş yok. Bölüm boş bırakılmadı, durum burada
        yazılı: "kayıtta yazılmamış" demektir, "savaşmamış" demek değildir.
      </p>
    </SectionBox>
  {/if}

  <SectionBox title="Tarihi İnceleme">
    {#if page.state.essay.length === 0}
      <p class="honesty-note">
        Bu devlet için uzun bir inceleme bulunmuyor. Özet, hükümdar kayıtları ve kaynak
        bağlantıları yukarıda yer alıyor.
      </p>
    {:else}
      {#each page.state.essay as paragraph, i (i)}
        <p class="body-text essay-paragraph">{paragraph}</p>
      {/each}
    {/if}
  </SectionBox>

  {#if page.state.legacy}
    <SectionBox title="Tarihi Miras">
      <p class="body-text">{page.state.legacy}</p>
    </SectionBox>
  {/if}

  <SectionBox id="state-sources" title="Kaynaklar">
    <SourceList sources={page.state.sources} />
  </SectionBox>
{/if}

<style>
  .state-intro p { margin: 0; max-width: 78ch; font-size: 16px; }
  .state-intro details { margin-top: 8px; }
  .state-intro summary { cursor: pointer; font-size: 13px; color: var(--accent-strong); }
  .state-intro details p { margin-top: 10px; }
  .reading-note p { max-width: 78ch; margin-top: 12px; }

  .ruler-view-switcher {
    display: flex;
    gap: 6px;
    margin-bottom: 12px;
    background: var(--surface-2);
    padding: 3px;
    border-radius: 8px;
    width: fit-content;
  }

  .view-toggle-btn {
    padding: 5px 12px;
    font-size: 12px;
    font-weight: 600;
    border: none;
    border-radius: 6px;
    background: transparent;
    color: var(--ink-dim);
    cursor: pointer;
    transition: all 0.18s ease;
  }

  .view-toggle-btn:hover {
    color: var(--ink);
  }

  .view-toggle-btn.active {
    background: var(--surface-1);
    color: var(--accent);
    box-shadow: var(--shadow-sm);
  }

  .ruler-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 10px;
  }

  .war-details summary {
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
    color: var(--accent-strong);
    padding: 6px 0;
  }

  .war-list-all {
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 6px;
  }
</style>
