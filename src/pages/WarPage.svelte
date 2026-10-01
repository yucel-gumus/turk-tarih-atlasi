<script lang="ts">
  import { atlasIndex, reignLabel, resolveWar, RESULT_ORDER, stateWarRecord } from '../lib/data/lookup';
  import { RESULT_MAP } from '../lib/data/atlas';
  import { hrefHome, hrefRuler, hrefState, hrefWar } from '../lib/router/route';
  import { router } from '../lib/router/router.svelte';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import MetaCard from '../components/ui/MetaCard.svelte';
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import SourceList from '../components/ui/SourceList.svelte';
  import WarRow from '../components/ui/WarRow.svelte';
  import { Swords } from '@lucide/svelte';

  let {
    stateId,
    rulerId,
    index: position,
    slug,
  }: { stateId: string; rulerId: string; index: number; slug: string } = $props();

  const index = atlasIndex();
  const ruler = $derived(index.rulersById.get(rulerId) ?? null);
  const state = $derived(index.rulerStateById.get(rulerId) ?? null);
  const resolved = $derived(ruler ? resolveWar(ruler, position, slug) : null);
  const war = $derived(resolved?.war ?? null);
  const otherWars = $derived(ruler?.wars ?? []);
  const stateRecord = $derived(state ? stateWarRecord(state) : null);

  // Sıra ve slug birlikte doğrulanır: slug kaydın kimliğidir, sıra yalnız
  // okunabilirlik içindir. Adres kanonikten sapıyorsa düzeltilir, kayıt yine
  // doğru gösterilir; eşleşme yoksa "bulunamadı" denir — asla başka bir savaş.
  $effect(() => {
    if (!ruler || !state || !war || !resolved) return;
    if (state.id !== stateId || resolved.index !== position) {
      router.replace(hrefWar(state.id, ruler.id, resolved.index, war.name));
    }
  });
</script>

{#if !ruler || !state || !war}
  <NotFoundNotice raw={`#/devlet/${stateId}/hukumdar/${rulerId}/savas/${position}-${slug}`} />
{:else}
  <Breadcrumb
    items={[
      { label: 'Atlas', href: hrefHome() },
      { label: state.name, href: hrefState(state.id) },
      { label: ruler.name, href: hrefRuler(state.id, ruler.id) },
      { label: war.name },
    ]}
  />

  <PageHeader eyebrow={`${ruler.name} · Savaş`} title={war.name}>
    {#snippet badges()}
      <span class="result-badge {war.result}">{RESULT_MAP[war.result]}</span>
      {#if reignLabel(ruler)}
        <span class="dates-tag">{reignLabel(ruler)}</span>
      {/if}
    {/snippet}
  </PageHeader>

  <div class="meta-section">
    <MetaCard
      label="Tarih İfadesi"
      value={war.when || 'Kayıtta yok'}
      note={war.when ? 'Kayıttaki metin olduğu gibi yazılır; yıla çevrilmez.' : 'Bu kayıtta tarih ifadesi boş.'}
    />
    <MetaCard
      label="Karşı Taraf"
      value={war.foe || 'Kayıtta yok'}
      note={war.foe ? undefined : 'Bu kayıtta karşı taraf yazılmamış.'}
    />
    <MetaCard label="Sonuç" value={RESULT_MAP[war.result]} />
    <MetaCard label="Hükümdar" value={ruler.name} />
  </div>

  <SectionBox title="Not">
    {#if war.note}
      <p class="body-text">{war.note}</p>
    {:else}
      <p class="honesty-note">Bu savaş kaydında not alanı boş.</p>
    {/if}
    <p class="honesty-note">
      Bu kayıtta savaşın ayrıntılı anlatımı bulunmuyor.
    </p>
  </SectionBox>

  <SectionBox title={`${ruler.name} hükümdarlığındaki diğer savaşlar · ${otherWars.length - 1}`}>
    {#snippet icon()}
      <Swords size={14} class="icon-war" aria-hidden="true" />
    {/snippet}
    {#if otherWars.length <= 1}
      <p class="honesty-note">Bu hükümdarın kaydında başka savaş yok.</p>
    {:else}
      <div class="war-list">
        {#each otherWars as entry, i (i)}
          {#if entry !== war}
            <WarRow war={entry} href={hrefWar(state.id, ruler.id, i + 1, entry.name)} />
          {/if}
        {/each}
      </div>
    {/if}
  </SectionBox>

  {#if stateRecord && stateRecord.total > 0}
    <SectionBox title={`${state.name} savaş kaydı · ${stateRecord.total}`}>
      <div class="meta-pills">
        {#each RESULT_ORDER as result (result)}
          {#if stateRecord.byResult[result] > 0}
            <span class="result-badge {result}">{RESULT_MAP[result]} · {stateRecord.byResult[result]}</span>
          {/if}
        {/each}
      </div>
      <a class="inline-link" href={hrefState(state.id)}>{state.name} sayfasında tamamını gör</a>
    </SectionBox>
  {/if}

  <SectionBox title="İlgili kaynaklar">
    <p class="honesty-note">Bu bağlantılar hükümdar kaydının kaynaklarıdır; savaş için ayrı kaynak alanı bulunmuyor.</p>
    <SourceList sources={ruler.sources} />
  </SectionBox>
{/if}

<style>
  .war-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

</style>
