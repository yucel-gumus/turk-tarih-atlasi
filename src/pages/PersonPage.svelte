<script lang="ts">
  import { atlasIndex, personRulerLink, resolvePerson, resolveWife } from '../lib/data/lookup';
  import { CERTAINTY_MAP } from '../lib/data/atlas';
  import {
    hrefHome,
    hrefPerson,
    hrefRuler,
    hrefState,
    PERSON_ROLE_LABEL,
    type PersonRole,
  } from '../lib/router/route';
  import { router } from '../lib/router/router.svelte';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import MetaCard from '../components/ui/MetaCard.svelte';
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';
  import PersonPill from '../components/ui/PersonPill.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import SourceList from '../components/ui/SourceList.svelte';

  let {
    stateId,
    rulerId,
    role,
    index: position,
    slug,
  }: { stateId: string; rulerId: string; role: PersonRole; index: number; slug: string } = $props();

  const index = atlasIndex();
  const ruler = $derived(index.rulersById.get(rulerId) ?? null);
  const state = $derived(index.rulerStateById.get(rulerId) ?? null);
  const people = $derived(ruler ? (role === 'es' ? ruler.wives : ruler.children) : []);
  const resolved = $derived(ruler ? resolvePerson(ruler, role, position, slug) : null);
  const person = $derived(resolved?.person ?? null);
  const roleLabel = $derived(PERSON_ROLE_LABEL[role]);

  /** Çocuk kaydındaki anne adı eş listesinde bulunuyorsa o eş. */
  const motherWife = $derived(
    role === 'cocuk' && person && ruler ? resolveWife(ruler, person.mother) : null
  );

  /** Annesi bu eş olarak çözülen çocuklar. */
  const ownChildren = $derived.by(() => {
    if (role !== 'es' || !person || !ruler) return [];
    return ruler.children.filter((child) => resolveWife(ruler, child.mother) === person);
  });

  const rulerLink = $derived(person ? personRulerLink(index, person.name) : { kind: 'none' as const });

  // Slug kimlik, sıra yalnız okunabilirlik: adres kanonikten sapıyorsa düzeltilir,
  // kayıt doğru gösterilir; eşleşme yoksa "bulunamadı" denir.
  $effect(() => {
    if (!ruler || !state || !person || !resolved) return;
    if (state.id !== stateId || resolved.index !== position) {
      router.replace(hrefPerson(state.id, ruler.id, role, resolved.index, person.name));
    }
  });
</script>

{#if !ruler || !state || !person}
  <NotFoundNotice raw={`#/devlet/${stateId}/hukumdar/${rulerId}/kisi/${role}/${position}-${slug}`} />
{:else}
  <Breadcrumb
    items={[
      { label: 'Atlas', href: hrefHome() },
      { label: state.name, href: hrefState(state.id) },
      { label: ruler.name, href: hrefRuler(state.id, ruler.id) },
      { label: person.name },
    ]}
  />

  <PageHeader eyebrow={`${ruler.name} · ${roleLabel}`} title={person.name}>
    {#snippet badges()}
      <span class="meta-pill">{roleLabel}</span>
      {#if person.certainty !== 'kesin'}
        <span class="cert-tag {person.certainty}">{CERTAINTY_MAP[person.certainty]}</span>
      {/if}
    {/snippet}
  </PageHeader>

  <div class="meta-section">
    <MetaCard label="Kayıt Türü" value={roleLabel} />
    <MetaCard label="Kesinlik" value={CERTAINTY_MAP[person.certainty]} />
    <MetaCard label="Bağlı Olduğu Hükümdar" value={ruler.name} />
    {#if role === 'cocuk'}
      <MetaCard
        label="Anne"
        value={person.mother || 'Kayıtta yok'}
        note={person.mother ? undefined : 'Bu kayıtta anne adı yazılmamış.'}
      />
    {/if}
  </div>

  <SectionBox title="Not">
    {#if person.note}
      <p class="body-text">{person.note}</p>
    {:else}
      <p class="honesty-note">Bu kayıtta not alanı boş.</p>
    {/if}
  </SectionBox>

  {#if role === 'cocuk'}
    <SectionBox title="Anne Bağlantısı">
      {#if !person.mother}
        <p class="honesty-note">Bu çocuk kaydında anne adı yazılmamış.</p>
      {:else if motherWife}
        <PersonPill
          person={motherWife}
          href={hrefPerson(state.id, ruler.id, 'es', ruler.wives.indexOf(motherWife) + 1, motherWife.name)}
        />
      {:else}
        <p class="body-text">Kayıttaki anne adı: <b>{person.mother}</b></p>
        <p class="honesty-note">
          Bu ad eş listesindeki adlarla birebir eşleşmiyor, bu yüzden bağlantı kurulmadı.
          Kayıtta yazıldığı gibi gösterilir; hangi eş olduğu tahmin edilmez.
        </p>
      {/if}
    </SectionBox>
  {/if}

  {#if role === 'es'}
    <SectionBox title={`Bu eşin çocukları · ${ownChildren.length}`}>
      {#if ownChildren.length === 0}
        <p class="honesty-note">
          Çocuk kayıtlarının hiçbirinde anne adı bu eşle eşleşmiyor. Bu, çocuğu olmadığı
          anlamına gelmez; annesi yazılmamış ya da başka bir adla yazılmış olabilir.
        </p>
      {:else}
        <div class="people-pills">
          {#each ruler.children as child, i (i)}
            {#if resolveWife(ruler, child.mother) === person}
              <PersonPill person={child} href={hrefPerson(state.id, ruler.id, 'cocuk', i + 1, child.name)} />
            {/if}
          {/each}
        </div>
      {/if}
    </SectionBox>
  {/if}

  <SectionBox title={role === 'es' ? 'Aynı hükümdarın diğer eşleri' : 'Kardeşler'}>
    {#if people.length <= 1}
      <p class="honesty-note">Bu hükümdarın kaydında başka {roleLabel} kaydı yok.</p>
    {:else}
      <div class="people-pills">
        {#each people as entry, i (i)}
          {#if entry !== person}
            <PersonPill person={entry} href={hrefPerson(state.id, ruler.id, role, i + 1, entry.name)} />
          {/if}
        {/each}
      </div>
    {/if}
  </SectionBox>

  {#if rulerLink.kind === 'single' || rulerLink.kind === 'ambiguous'}
    <SectionBox title="Aynı adı taşıyan hükümdar kaydı">
    {#if rulerLink.kind === 'single'}
      <a class="ruler-link" href={hrefRuler(rulerLink.state.id, rulerLink.ruler.id)}>
        {rulerLink.ruler.name} · {rulerLink.state.name}
      </a>
    {:else if rulerLink.kind === 'ambiguous'}
      <p class="honesty-note">
        Bu adı taşıyan birden çok hükümdar kaydı var; hangisinin kastedildiği kayıtta
        belirtilmemiş. Seçim yapılmaz, adaylar listelenir.
      </p>
      <div class="people-pills">
        {#each rulerLink.candidates as candidate (candidate.ruler.id)}
          <a class="ruler-link" href={hrefRuler(candidate.state.id, candidate.ruler.id)}>
            {candidate.ruler.name} · {candidate.state.name}
          </a>
        {/each}
      </div>
    {/if}
    </SectionBox>
  {/if}

  <SectionBox title="İlgili kaynaklar">
    <p class="honesty-note">Bu bağlantılar hükümdar kaydının kaynaklarıdır; kişi için ayrı kaynak alanı bulunmuyor.</p>
    <SourceList sources={ruler.sources} />
  </SectionBox>
{/if}

<style>
  .people-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .ruler-link {
    font-size: 12px;
    font-weight: 600;
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.08);
    border: 1px solid rgba(229, 195, 120, 0.2);
    padding: 5px 10px;
    border-radius: 6px;
  }

  .ruler-link:hover {
    background: rgba(229, 195, 120, 0.16);
  }
</style>
