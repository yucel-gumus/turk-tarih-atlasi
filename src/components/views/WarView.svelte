<script lang="ts">
  import {
    getWar,
    counterpartWars,
    foeMatches,
    durationLabel,
    reignLabel,
    isOngoing,
    REGION_COLORS,
    RESULT_LABEL,
  } from '../../lib/data/atlas';
  import { modals } from '../../lib/modals.svelte';

  const { stateId, rulerId, index }: { stateId: string; rulerId: string; index: number } = $props();
  const entry = $derived(getWar({ stateId, rulerId, index })!);
  const { war, state, ruler } = $derived(entry);
  const others = $derived(counterpartWars(entry));
  const foes = $derived(foeMatches(entry));
  const side = $derived(state.short || state.name);
  const foe = $derived(war.foe || 'Kayıtlarda yok');

  const verdict: Record<string, string> = $derived({
    zafer: `${side} kazandı`,
    yenilgi: `${side} yenildi${war.foe ? ` · ${war.foe} üstün geldi` : ''}`,
    sonucsuz: 'Kesin bir sonuç alınamadı',
    antlasma: 'Savaş antlaşmayla sonuçlandı',
    belirsiz: 'Sonucu kaynaklarda belirsiz',
  });
</script>

<div class="verdict result {war.result}">
  <span class="label">{RESULT_LABEL[war.result]}</span>
  <span>{verdict[war.result]}</span>
</div>

<section class="sides" aria-label="Taraflar">
  <div class="side-card" style:--c={REGION_COLORS[state.region]}>
    <span class="role">1. taraf</span>
    <button type="button" class="link big" onclick={() => modals.open({ kind: 'state', id: state.id })}>{state.name}</button>
    <span class="muted">Komutan / hükümdar:</span>
    <button type="button" class="link" onclick={() => modals.open({ kind: 'ruler', stateId, rulerId })}>
      {ruler.name} <small>({reignLabel(ruler, isOngoing(state))})</small>
    </button>
  </div>
  <div class="vs" aria-hidden="true">vs</div>
  <div class="side-card foe" style:--c={foes[0] ? REGION_COLORS[foes[0].state.region] : 'var(--line-strong)'}>
    <span class="role">2. taraf</span>
    <span class="big">{foe}</span>
    {#each foes as f (f.state.id)}
      <button type="button" class="link" onclick={() => modals.open({ kind: 'state', id: f.state.id })}>
        Devlet: {f.state.name} →
      </button>
      {#if f.ruler}
        <button type="button" class="link" onclick={() => modals.open({ kind: 'ruler', stateId: f.state.id, rulerId: f.ruler!.id })}>
          Hükümdar: {f.ruler.name} →
        </button>
      {/if}
    {/each}
  </div>
</section>

<dl class="facts">
  <div><dt>Tarih</dt><dd>{war.when || 'Kayıtlarda yok'}</dd></div>
  <div><dt>Ne kadar sürdü</dt><dd>{durationLabel(entry.start, entry.end)}</dd></div>
  <div><dt>Sonuç</dt><dd>{RESULT_LABEL[war.result]}</dd></div>
</dl>

{#if war.note}
  <section class="sec">
    <h3>Ne oldu?</h3>
    <p class="lead">{war.note}</p>
  </section>
{/if}

{#if others.length}
  <section class="sec">
    <h3>Karşı taraftaki kayıt <small>aynı savaş başka bir Türk devletinin kayıtlarında da var</small></h3>
    <ul class="rows">
      {#each others as o (o.stateId + o.rulerId + o.index)}
        <li>
          <button
            type="button"
            class="row"
            onclick={() => modals.open({ kind: 'war', stateId: o.stateId, rulerId: o.rulerId, index: o.index })}
          >
            <span class="main">
              <span class="t">{o.state.name} · {o.ruler.name}</span>
              <span class="s">{o.war.name}{o.war.note ? ` — ${o.war.note}` : ''}</span>
            </span>
            <span class="side"><span class="result {o.war.result}">{RESULT_LABEL[o.war.result]}</span></span>
          </button>
        </li>
      {/each}
    </ul>
  </section>
{/if}

<section class="sec">
  <h3>İlgili kaynaklar</h3>
  <p class="muted">Savaş kayıtlarının ayrı kaynağı yoktur; aşağıdakiler {ruler.name} kaydının kaynaklarıdır.</p>
  <ul class="sources">
    {#each ruler.sources as s}
      <li><a href={s.url} target="_blank" rel="noopener noreferrer">{s.title}</a></li>
    {/each}
  </ul>
</section>

<style>
  .verdict {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 600;
    white-space: normal;
    margin-bottom: 14px;
  }
  .verdict .label {
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 2px 9px;
    border-radius: 999px;
    border: 1.5px solid currentColor;
  }
  .sides {
    display: grid;
    grid-template-columns: 1fr auto 1fr;
    gap: 10px;
    align-items: stretch;
    margin-bottom: 14px;
  }
  .side-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
    padding: 12px 14px;
    border: 1px solid var(--line);
    border-top: 4px solid var(--c);
    border-radius: 12px;
    min-width: 0;
  }
  .role {
    font-size: 11.5px;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--ink-muted);
  }
  .big {
    font-family: var(--serif);
    font-size: 18px;
    font-weight: 700;
    line-height: 1.25;
    overflow-wrap: anywhere;
  }
  .vs {
    align-self: center;
    font-family: var(--serif);
    font-style: italic;
    color: var(--ink-muted);
  }
  .link {
    border: 0;
    background: none;
    padding: 0;
    color: var(--accent);
    text-align: left;
    cursor: pointer;
    text-decoration: underline;
    text-underline-offset: 3px;
    font-weight: 600;
  }
  .link.big {
    color: var(--ink);
  }
  .link small {
    color: var(--ink-muted);
    font-weight: 500;
  }
  @media (max-width: 640px) {
    .sides {
      grid-template-columns: 1fr;
    }
    .vs {
      justify-self: center;
    }
  }
</style>
