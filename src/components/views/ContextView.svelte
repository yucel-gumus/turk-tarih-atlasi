<script lang="ts">
  import { getContext, buildTree, REGION_COLORS, EDGE_LABEL } from '../../lib/data/atlas';
  import { modals } from '../../lib/modals.svelte';

  const { id }: { id: string } = $props();
  const ctx = $derived(getContext(id)!);
  const node = $derived(buildTree().byId.get(id)!);
</script>

<p class="lead">{ctx.summary}</p>

<section class="sec">
  <h3>Soy ağacındaki yeri</h3>
  <div class="relation">
    {#if node.parent}
      <div class="item">
        <button type="button" class="chip" onclick={() => modals.open({ kind: 'state', id: node.parent!.id })}>
          <span>Nereden geldi · {EDGE_LABEL[node.edgeKind!]}</span>
          <b>{node.parent.name}</b>
        </button>
        <p>{node.edgeNote}</p>
      </div>
    {/if}
    {#each node.children as c (c.id)}
      <div class="item">
        <button
          type="button"
          class="chip"
          style:--c={c.region ? REGION_COLORS[c.region] : undefined}
          onclick={() => modals.open({ kind: 'state', id: c.id })}
        >
          <span>Buradan doğan · {EDGE_LABEL[c.edgeKind!]}</span>
          <b>{c.name}</b>
        </button>
        <p>{c.edgeNote}</p>
      </div>
    {/each}
  </div>
</section>

<section class="sec">
  <h3>Kaynaklar</h3>
  <ul class="sources">
    {#each ctx.sources as s}
      <li><a href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a></li>
    {/each}
  </ul>
</section>
