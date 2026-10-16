<script lang="ts">
  import {
    getState,
    getRuler,
    isOngoing,
    reignLabel,
    yearLabel,
    warStats,
    childAsRuler,
    RESULT_LABEL,
    CERTAINTY_LABEL,
    CURRENT_YEAR,
  } from '../../lib/data/atlas';
  import { modals } from '../../lib/modals.svelte';
  import type { BattleResult } from '../../schemas/atlas.schema';

  const { stateId, rulerId }: { stateId: string; rulerId: string } = $props();
  const state = $derived(getState(stateId)!);
  const ruler = $derived(getRuler(stateId, rulerId)!);
  const ongoing = $derived(isOngoing(state));
  const pos = $derived(state.rulers.findIndex((r) => r.id === rulerId));
  const prev = $derived(state.rulers[pos - 1]);
  const next = $derived(state.rulers[pos + 1]);
  const stats = $derived(warStats(ruler.wars));
  const RESULTS: BattleResult[] = ['zafer', 'yenilgi', 'sonucsuz', 'antlasma', 'belirsiz'];

  const [rs, re] = $derived(ruler.reign);
  const reignEnd = $derived(re ?? (ongoing ? CURRENT_YEAR : null));
  const reignYears = $derived(rs !== null && reignEnd !== null ? reignEnd - rs : null);

  function lifeLabel(year: number | null | undefined, fallback: string) {
    return year == null ? fallback : yearLabel(year);
  }
</script>

<dl class="facts">
  <div><dt>{ongoing ? 'Görev süresi' : 'Hükümdarlık'}</dt><dd>{reignLabel(ruler, ongoing)}</dd></div>
  {#if reignYears !== null}<div><dt>Süre</dt><dd>{reignYears < 1 ? '1 yıldan az' : `${reignYears} yıl`}</dd></div>{/if}
  <div><dt>Doğum</dt><dd>{lifeLabel(ruler.birth, 'Kayıtlarda yok')}</dd></div>
  <div><dt>Ölüm</dt><dd>{lifeLabel(ruler.death, ongoing || ruler.reign[1] === null ? '—' : 'Kayıtlarda yok')}</dd></div>
  <div><dt>Sıra</dt><dd>{pos + 1}. / {state.rulers.length}</dd></div>
</dl>

{#if ruler.claim}<p class="muted"><span class="tag">Taht iddiacısı</span> Klasik hükümdar sıralamasına girmeyen, tahtı talep etmiş kişi.</p>{/if}
<p class="lead">{ruler.summary}</p>

{#if ruler.traits.length}
  <ul class="plain">
    {#each ruler.traits as t}<li>{t}</li>{/each}
  </ul>
{/if}

{#if ruler.contribution || ruler.harm}
  <section class="sec">
    <h3>Ülkesine etkisi</h3>
    <div class="pair">
      {#if ruler.contribution}<div class="plus"><h4>Katkısı</h4><p>{ruler.contribution}</p></div>{/if}
      {#if ruler.harm}<div class="minus"><h4>Bedeli</h4><p>{ruler.harm}</p></div>{/if}
    </div>
  </section>
{/if}

<section class="sec">
  <h3>Savaşları <small>{ruler.wars.length ? `${ruler.wars.length} kayıt · tıklayın` : ''}</small></h3>
  {#if ruler.wars.length}
    <div class="stats">
      {#each RESULTS as k}
        {#if stats[k]}<span class="result {k}">{stats[k]} {RESULT_LABEL[k].toLocaleLowerCase('tr')}</span>{/if}
      {/each}
    </div>
    <ul class="rows">
      {#each ruler.wars as w, i}
        <li>
          <button type="button" class="row" onclick={() => modals.open({ kind: 'war', stateId, rulerId, index: i })}>
            <span class="main">
              <span class="t">{w.name}</span>
              <span class="s">{w.foe ? `karşısında: ${w.foe}` : 'karşı taraf kayıtlarda yok'}</span>
            </span>
            <span class="side">
              {w.when}
              <span class="result {w.result}">{RESULT_LABEL[w.result]}</span>
            </span>
          </button>
        </li>
      {/each}
    </ul>
  {:else}
    <p class="muted">Bu kişiye bağlı bir savaş kaydı yok.</p>
  {/if}
</section>

{#if ruler.wives.length || ruler.children.length || ruler.familyNotes.length}
  <section class="sec">
    <h3>Ailesi</h3>
    {#if ruler.wives.length}
      <p class="muted"><b>Eşleri</b></p>
      <ul class="rows">
        {#each ruler.wives as p}
          <li class="row">
            <span class="main">
              <span class="t">{p.name} {#if p.certainty !== 'kesin'}<span class="tag">{CERTAINTY_LABEL[p.certainty]}</span>{/if}</span>
              {#if p.note}<span class="s">{p.note}</span>{/if}
            </span>
          </li>
        {/each}
      </ul>
    {/if}
    {#if ruler.children.length}
      <p class="muted" style="margin-top:14px"><b>Çocukları</b></p>
      <ul class="rows">
        {#each ruler.children as p}
          {@const asRuler = childAsRuler(state, ruler, p.name)}
          <li>
            {#if asRuler}
              <button type="button" class="row" onclick={() => modals.open({ kind: 'ruler', stateId, rulerId: asRuler.id })}>
                <span class="main">
                  <span class="t">{p.name} <span class="tag">hükümdar oldu: {asRuler.name}</span></span>
                  {#if p.note || p.mother}<span class="s">{[p.mother && `Annesi: ${p.mother}`, p.note].filter(Boolean).join(' · ')}</span>{/if}
                </span>
                <span class="side"></span>
              </button>
            {:else}
              <div class="row">
                <span class="main">
                  <span class="t">{p.name} {#if p.certainty !== 'kesin'}<span class="tag">{CERTAINTY_LABEL[p.certainty]}</span>{/if}</span>
                  {#if p.note || p.mother}<span class="s">{[p.mother && `Annesi: ${p.mother}`, p.note].filter(Boolean).join(' · ')}</span>{/if}
                </span>
              </div>
            {/if}
          </li>
        {/each}
      </ul>
    {/if}
    {#if ruler.familyNotes.length}
      <ul class="plain muted" style="margin-top:10px">
        {#each ruler.familyNotes as n}<li>{n}</li>{/each}
      </ul>
    {/if}
  </section>
{/if}

{#if prev || next}
  <section class="sec">
    <h3>Tahtta önce ve sonra</h3>
    <div class="chips">
      {#if prev}
        <button type="button" class="chip" onclick={() => modals.open({ kind: 'ruler', stateId, rulerId: prev.id })}>
          <span>← Önceki · {reignLabel(prev, ongoing)}</span><b>{prev.name}</b>
        </button>
      {/if}
      {#if next}
        <button type="button" class="chip" onclick={() => modals.open({ kind: 'ruler', stateId, rulerId: next.id })}>
          <span>Sonraki → · {reignLabel(next, ongoing)}</span><b>{next.name}</b>
        </button>
      {/if}
      <button type="button" class="chip" onclick={() => modals.open({ kind: 'state', id: stateId })}>
        <span>Devlet</span><b>{state.name}</b>
      </button>
    </div>
  </section>
{/if}

{#if ruler.legends.length || ruler.birthNote || ruler.deathNote || ruler.reignNote}
  <details class="more">
    <summary>Ayrıntılı notlar ve rivayetler</summary>
    <dl>
      {#if ruler.birthNote}<dt>Doğum</dt><dd>{ruler.birthNote}</dd>{/if}
      {#if ruler.reignNote}<dt>Hükümdarlık</dt><dd>{ruler.reignNote}</dd>{/if}
      {#if ruler.deathNote}<dt>Ölüm</dt><dd>{ruler.deathNote}</dd>{/if}
      {#each ruler.legends as l}<dt>Rivayet</dt><dd>{l}</dd>{/each}
    </dl>
  </details>
{/if}

<section class="sec">
  <h3>Kaynaklar</h3>
  <ul class="sources">
    {#each ruler.sources as s}
      <li><a href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a></li>
    {/each}
  </ul>
</section>
