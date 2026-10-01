<script lang="ts">
  import { atlasIndex } from '../lib/data/lookup';
  import { hrefHome } from '../lib/router/route';
  import Breadcrumb from '../components/layout/Breadcrumb.svelte';
  import PageHeader from '../components/layout/PageHeader.svelte';
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';
  import SectionBox from '../components/ui/SectionBox.svelte';
  import SourceList from '../components/ui/SourceList.svelte';

  const guide = atlasIndex().rehber;
</script>

{#if !guide}
  <!-- Rehber kaydı veri kümesinden çıkarılırsa sayfa boş bir kabuk olarak
       kalmak yerine durumu açıkça bildirir. -->
  <NotFoundNotice />
{:else}
  <Breadcrumb items={[{ label: 'Atlas', href: hrefHome() }, { label: guide.name }]} />

  <PageHeader eyebrow="Rehber" title={guide.name} subtitle={guide.short} />

  <p class="honesty-note">
    Bu rehber atlasın kapsamını, kaynak kullanımını ve tarihsel belirsizliklerin nasıl
    gösterildiğini açıklar.
  </p>

  {#if guide.summary}
    <SectionBox title="Özet">
      <p class="body-text">{guide.summary}</p>
    </SectionBox>
  {/if}

  {#each guide.essay as paragraph, i (i)}
    <SectionBox title={i === 0 ? 'Yöntem' : `Yöntem · ${i + 1}`}>
      <p class="body-text essay-paragraph">{paragraph}</p>
    </SectionBox>
  {/each}

  <SectionBox title="Kaynaklar">
    <SourceList sources={guide.sources} />
  </SectionBox>
{/if}
