<script lang="ts">
  import {
    getState,
    buildTree,
    stateWars,
    warStats,
    isOngoing,
    reignLabel,
    spanLabel,
    yearLabel,
    REGION_COLORS,
    RESULT_LABEL,
    CONFIDENCE_LABEL,
    EDGE_LABEL,
    CURRENT_YEAR,
    type TreeNode,
  } from '../../lib/data/atlas';
  import { modals } from '../../lib/modals.svelte';
  import type { BattleResult } from '../../schemas/atlas.schema';

  const { id }: { id: string } = $props();
  const state = $derived(getState(id)!);
  const node = $derived(buildTree().byId.get(id)!);
  const ongoing = $derived(isOngoing(state));
  const wars = $derived(stateWars(id));
  const stats = $derived(warStats(wars.map((w) => w.war)));
  const years = $derived((ongoing ? CURRENT_YEAR : state.end) - state.start);
  const RESULTS: BattleResult[] = ['zafer', 'yenilgi', 'sonucsuz', 'antlasma', 'belirsiz'];

  function openNode(n: TreeNode) {
    modals.open(n.kind === 'state' ? { kind: 'state', id: n.id } : { kind: 'context', id: n.id });
  }

  function nodeColor(n: TreeNode) {
    return n.region ? REGION_COLORS[n.region] : 'var(--ink-muted)';
  }
</script>

<dl class="facts">
  <div><dt>Dönem</dt><dd>{spanLabel(state.start, state.end, ongoing)}</dd></div>
  <div><dt>Süre</dt><dd>{years} yıl{ongoing ? ' (sürüyor)' : ''}</dd></div>
  {#if state.capital}<div><dt>Başkent</dt><dd>{state.capital}</dd></div>{/if}
  <div><dt>{ongoing ? 'Devlet başkanı' : 'Hükümdar'}</dt><dd>{state.rulers.length} kişi</dd></div>
  <div><dt>Savaş kaydı</dt><dd>{wars.length}</dd></div>
</dl>

<p class="lead">{state.summary}</p>
{#if state.religion}<p class="muted"><b>İnanç:</b> {state.religion}</p>{/if}

<section class="sec">
  <h3>Soy ağacındaki yeri</h3>
  <div class="relation">
    {#if node.parent}
      <div class="item">
        <button type="button" class="chip" style:--c={nodeColor(node.parent)} onclick={() => openNode(node.parent!)}>
          <span>Nereden geldi · {EDGE_LABEL[node.edgeKind!]}</span>
          <b>{node.parent.name}</b>
        </button>
        <p>{node.edgeNote}</p>
      </div>
    {:else}
      <p class="muted">Soy ağacının kökü: bilinen ilk büyük Türk devleti olarak kabul edilir.</p>
    {/if}
    {#each node.children as c (c.id)}
      <div class="item">
        <button type="button" class="chip" style:--c={nodeColor(c)} onclick={() => openNode(c)}>
          <span>Ondan doğan · {EDGE_LABEL[c.edgeKind!]}</span>
          <b>{c.name}</b>
        </button>
        <p>{c.edgeNote}</p>
      </div>
    {/each}
  </div>
</section>

{#if state.rulers.length}
  <section class="sec">
    <h3>{ongoing ? 'Devlet başkanları' : 'Hükümdarlar'} <small>{state.rulers.length} kişi · tıklayın</small></h3>
    <ul class="rows">
      {#each state.rulers as r, i (r.id)}
        <li>
          <button type="button" class="row" onclick={() => modals.open({ kind: 'ruler', stateId: id, rulerId: r.id })}>
            <span class="num">{i + 1}</span>
            <span class="main">
              <span class="t">{r.name} {#if r.claim}<span class="tag">taht iddiacısı</span>{/if}</span>
              <span class="s">{r.title || (ongoing ? 'Devlet başkanı' : 'Hükümdar')}</span>
            </span>
            <span class="side">
              {reignLabel(r, ongoing)}
              {#if r.wars.length}<span class="tag">{r.wars.length} savaş</span>{/if}
            </span>
          </button>
        </li>
      {/each}
    </ul>
  </section>
{/if}

{#if wars.length}
  <section class="sec">
    <h3>Savaşlar <small>{wars.length} kayıt</small></h3>
    <div class="stats">
      {#each RESULTS as k}
        {#if stats[k]}<span class="result {k}">{stats[k]} {RESULT_LABEL[k].toLocaleLowerCase('tr')}</span>{/if}
      {/each}
    </div>
    <ul class="rows">
      {#each wars as w (w.rulerId + w.index)}
        <li>
          <button
            type="button"
            class="row"
            onclick={() => modals.open({ kind: 'war', stateId: id, rulerId: w.rulerId, index: w.index })}
          >
            <span class="main">
              <span class="t">{w.war.name}</span>
              <span class="s">{w.war.foe ? `karşısında: ${w.war.foe}` : 'karşı taraf kayıtlarda yok'} · {w.ruler.name}</span>
            </span>
            <span class="side">
              {w.war.when}
              <span class="result {w.war.result}">{RESULT_LABEL[w.war.result]}</span>
            </span>
          </button>
        </li>
      {/each}
    </ul>
  </section>
{/if}

{#if state.essay.length}
  <details class="more">
    <summary>Ayrıntılı tarih anlatısı</summary>
    {#each state.essay as p}<p>{p}</p>{/each}
  </details>
{/if}

{#if state.legacy || state.startNote || state.endNote || state.confidenceNote}
  <details class="more">
    <summary>Miras ve tarih notları</summary>
    <dl>
      {#if state.legacy}<dt>Tarihe bıraktığı iz</dt><dd>{state.legacy}</dd>{/if}
      {#if state.startNote}<dt>Kuruluş ({yearLabel(state.start)})</dt><dd>{state.startNote}</dd>{/if}
      {#if state.endNote}<dt>{ongoing ? 'Bugün' : `Yıkılış (${yearLabel(state.end)})`}</dt><dd>{state.endNote}</dd>{/if}
      {#if state.confidenceNote}
        <dt>Kayıtların güvenilirliği: {CONFIDENCE_LABEL[state.confidence]}</dt><dd>{state.confidenceNote}</dd>
      {/if}
    </dl>
  </details>
{/if}

<section class="sec">
  <h3>Kaynaklar</h3>
  <ul class="sources">
    {#each state.sources as s}
      <li><a href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a></li>
    {/each}
  </ul>
</section>
