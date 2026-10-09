<script lang="ts">
  import type { Person } from '../schemas/atlas.schema';
  import { atlasIndex, reignLabel, resolveWife, RESULT_ORDER, warRecord } from '../lib/data/lookup';
  import { RESULT_MAP, yearLabel } from '../lib/data/atlas';
  import { hrefHome, hrefPerson, hrefRuler, hrefState, hrefWar } from '../lib/router/route';
  import { router } from '../lib/router/router.svelte';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import MetaCard from '../components/ui/MetaCard.svelte';
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';
  import PersonPill from '../components/ui/PersonPill.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import SourceList from '../components/ui/SourceList.svelte';
  import WarRow from '../components/ui/WarRow.svelte';
  import ChevronLeft from '@lucide/svelte/icons/chevron-left';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import Swords from '@lucide/svelte/icons/swords';
  import Users from '@lucide/svelte/icons/users';

  let { stateId, rulerId }: { stateId: string; rulerId: string } = $props();

  const index = atlasIndex();
  const ruler = $derived(index.rulersById.get(rulerId) ?? null);
  /** Hükümdarın gerçek devleti; adresteki devlet parçası yanlış olabilir. */
  const state = $derived(index.rulerStateById.get(rulerId) ?? null);

  const reign = $derived(ruler ? reignLabel(ruler) : '');
  const wars = $derived(ruler?.wars ?? []);
  const warTotals = $derived(warRecord(wars));
  const siblings = $derived(state?.rulers ?? []);
  const at = $derived(siblings.findIndex((r) => r.id === rulerId));
  const previousRuler = $derived(at > 0 ? siblings[at - 1] : null);
  const nextRuler = $derived(at >= 0 && at < siblings.length - 1 ? siblings[at + 1] : null);

  /** Ölçülmüş annesi çözülemeyen çocuk sayısı; sabit yazılmaz. */
  const motherStats = $derived.by(() => {
    const current = ruler;
    if (!current) return { filled: 0, resolved: 0 };
    const filled = current.children.filter((child) => child.mother);
    return {
      filled: filled.length,
      resolved: filled.filter((child) => resolveWife(current, child.mother) !== null).length,
    };
  });

  /** Çocuğun annesi eş listesinde bulunuyorsa o eşin sayfasına bağlanır. */
  function motherHref(child: Person): string | null {
    if (!ruler || !state) return null;
    const wife = resolveWife(ruler, child.mother);
    if (!wife) return null;
    const wifeIndex = ruler.wives.indexOf(wife);
    return wifeIndex < 0 ? null : hrefPerson(state.id, ruler.id, 'es', wifeIndex + 1, wife.name);
  }

  // Adres hükümdarın devletini yanlış taşıyorsa (paylaşılmış bağlantıda yol
  // parçası bozulmuşsa) kanonik adrese düzeltilir; kayıt yine doğru gösterilir.
  $effect(() => {
    if (ruler && state && state.id !== stateId) router.replace(hrefRuler(state.id, ruler.id));
  });
</script>

{#if !ruler || !state}
  <NotFoundNotice raw={`#/devlet/${stateId}/hukumdar/${rulerId}`} />
{:else}
  <Breadcrumb
    items={[
      { label: 'Atlas', href: hrefHome() },
      { label: state.name, href: hrefState(state.id) },
      { label: ruler.name },
    ]}
  />

  <PageHeader eyebrow={state.name} title={ruler.name} subtitle={ruler.title}>
    {#snippet badges()}
      {#if reign}
        <span class="dates-tag">{reign}</span>
      {/if}
      {#if ruler.claim}
        <span class="claim-tag">Taht iddiası</span>
      {/if}
      {#if warTotals.total > 0}
        <span class="meta-pill">
          <Swords size={12} class="icon-war" aria-hidden="true" />
          {warTotals.total} savaş kaydı
        </span>
      {/if}
      {#if ruler.wives.length + ruler.children.length > 0}
        <span class="meta-pill">
          <Users size={12} class="icon-person" aria-hidden="true" />
          {ruler.wives.length} eş · {ruler.children.length} çocuk
        </span>
      {/if}
    {/snippet}
  </PageHeader>

  <div class="meta-section">
    <MetaCard label="Saltanat" value={reign || 'Kayıtta yok'} />
    <MetaCard
      label="Yaşam Süresi"
      value="{ruler.birth != null ? yearLabel(ruler.birth) : '?'} – {ruler.death != null ? yearLabel(ruler.death) : '?'}"
    />
    <MetaCard label="Devlet" value={state.name} />
  </div>

  {#if ruler.aliases.length > 0}
    <SectionBox title="Diğer adları">
      <div class="alias-pills">
        {#each ruler.aliases as alias (alias)}
          <span class="alias-pill">{alias}</span>
        {/each}
      </div>
    </SectionBox>
  {/if}

  {#if ruler.summary}
    <SectionBox title="Özet">
      <p class="body-text">{ruler.summary}</p>
    </SectionBox>
  {/if}

  {#if ruler.reignNote || ruler.birthNote || ruler.deathNote}
    <SectionBox title="Kayıt Notları">
      {#if ruler.reignNote}
        <h3 class="sub-title">Saltanat</h3>
        <p class="body-text">{ruler.reignNote}</p>
      {/if}
      {#if ruler.birthNote}
        <h3 class="sub-title">Doğum</h3>
        <p class="body-text">{ruler.birthNote}</p>
      {/if}
      {#if ruler.deathNote}
        <h3 class="sub-title">Ölüm</h3>
        <p class="body-text">{ruler.deathNote}</p>
      {/if}
    </SectionBox>
  {/if}

  {#if ruler.contribution || ruler.harm}
    <div class="contrast-grid">
      {#if ruler.contribution}
        <div class="contrast-card positive">
          <h3 class="sub-title">Katkı</h3>
          <p class="body-text">{ruler.contribution}</p>
        </div>
      {/if}
      {#if ruler.harm}
        <div class="contrast-card negative">
          <h3 class="sub-title">Zarar</h3>
          <p class="body-text">{ruler.harm}</p>
        </div>
      {/if}
    </div>
  {/if}

  {#if ruler.traits.length > 0}
    <SectionBox title="Nitelikler">
      <div class="tags-cluster">
        {#each ruler.traits as trait (trait)}
          <span class="trait-badge">{trait}</span>
        {/each}
      </div>
    </SectionBox>
  {/if}

  {#if ruler.legends.length > 0}
    <SectionBox title="Efsaneler">
      {#each ruler.legends as legend, i (i)}
        <blockquote class="legend-quote">{legend}</blockquote>
      {/each}
    </SectionBox>
  {/if}

  <SectionBox title={`Savaşlar · ${wars.length}`}>
    {#snippet icon()}
      <Swords size={14} class="icon-war" aria-hidden="true" />
    {/snippet}
    {#if wars.length === 0}
      <p class="honesty-note">
        Bu hükümdarın kaydında savaş bulunmuyor. Bu, savaşmadığı anlamına gelmez.
      </p>
    {:else}
      <div class="meta-pills">
        {#each RESULT_ORDER as result (result)}
          {#if warTotals.byResult[result] > 0}
            <span class="result-badge {result}">{RESULT_MAP[result]} · {warTotals.byResult[result]}</span>
          {/if}
        {/each}
      </div>
      <div class="war-list">
        {#each wars as war, i (i)}
          <WarRow {war} href={hrefWar(state.id, ruler.id, i + 1, war.name)} />
        {/each}
      </div>
    {/if}
  </SectionBox>

  {#if ruler.wives.length > 0}
    <SectionBox title={`Eş / Hatun · ${ruler.wives.length}`}>
      {#snippet icon()}
        <Users size={14} class="icon-person" aria-hidden="true" />
      {/snippet}
      <div class="people-pills">
        {#each ruler.wives as wife, i (i)}
          <PersonPill person={wife} href={hrefPerson(state.id, ruler.id, 'es', i + 1, wife.name)} />
        {/each}
      </div>
    </SectionBox>
  {/if}

  {#if ruler.children.length > 0}
    <SectionBox title={`Çocuk / Şehzade · ${ruler.children.length}`}>
      <div class="people-pills">
        {#each ruler.children as child, i (i)}
          <PersonPill
            person={child}
            href={hrefPerson(state.id, ruler.id, 'cocuk', i + 1, child.name)}
            motherHref={motherHref(child)}
          />
        {/each}
      </div>
      {#if motherStats.filled > 0}
        <p class="honesty-note">
          Anne adı yazılı çocuk kaydı: {motherStats.filled}. Bunlardan eş listesindeki bir
          adla eşleşen {motherStats.resolved}, eşleşmeyen
          {motherStats.filled - motherStats.resolved}. Eşleşmeyen ad ham metin olarak
          gösterilir, uydurma bağlantı kurulmaz.
        </p>
      {/if}
    </SectionBox>
  {/if}

  {#if ruler.familyNotes.length > 0}
    <SectionBox title="Aileye ilişkin kayıtlar">
      {#each ruler.familyNotes as note, i (i)}
        <p class="body-text">{note}</p>
      {/each}
    </SectionBox>
  {/if}

  <SectionBox title="Kaynaklar">
    <SourceList sources={ruler.sources} />
  </SectionBox>

  {#if previousRuler || nextRuler}
    <nav class="sibling-nav" aria-label="Devlet içindeki hükümdarlar">
      {#if previousRuler}
        <a class="sibling-link" href={hrefRuler(state.id, previousRuler.id)}>
          <ChevronLeft size={14} aria-hidden="true" />
          <span>{previousRuler.name}</span>
        </a>
      {:else}
        <span></span>
      {/if}
      {#if nextRuler}
        <a class="sibling-link" href={hrefRuler(state.id, nextRuler.id)}>
          <span>{nextRuler.name}</span>
          <ChevronRight size={14} aria-hidden="true" />
        </a>
      {/if}
    </nav>
  {/if}
{/if}

<style>
  .alias-pills,
  .tags-cluster,
  .people-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .alias-pill,
  .trait-badge {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent-strong);
    background: var(--accent-soft);
    border: 1px solid var(--accent-line);
    padding: 3px 9px;
    border-radius: 7px;
  }

  .contrast-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 10px;
  }

  .contrast-card {
    border-radius: 14px;
    padding: 15px 17px;
    border: 1px solid var(--border);
    background: var(--surface-1);
    box-shadow: var(--shadow-sm);
  }

  .contrast-card.positive {
    border-left: 3px solid var(--accent-victory);
  }

  .contrast-card.negative {
    border-left: 3px solid var(--accent-defeat);
  }

  .legend-quote {
    margin: 0;
    font-family: var(--font-serif);
    font-style: italic;
    font-size: 13.5px;
    line-height: 1.65;
    color: var(--ink-muted);
    border-left: 2px solid var(--accent-line);
    padding-left: 13px;
  }

  .war-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .sibling-nav {
    display: flex;
    justify-content: space-between;
    gap: 10px;
  }

  .sibling-link {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 12px;
    font-weight: 500;
    color: var(--ink-muted);
    padding: 9px 13px;
    border-radius: 9px;
    border: 1px solid var(--border);
    background: var(--surface-1);
    transition: color 0.18s ease, border-color 0.18s ease, background 0.18s ease;
  }

  .sibling-link:hover {
    color: var(--accent-strong);
    border-color: var(--accent-line);
    background: var(--accent-soft);
  }
</style>
