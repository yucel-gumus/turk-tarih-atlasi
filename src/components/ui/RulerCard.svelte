<script lang="ts">
  import type { Ruler, State } from '../../schemas/atlas.schema';
  import { yearLabel } from '../../lib/data/atlas';
  import { reignLabel } from '../../lib/data/lookup';
  import { hrefRuler } from '../../lib/router/route';
  import { ChevronRight, Swords, Users } from '@lucide/svelte';

  let { ruler, state }: { ruler: Ruler; state: State } = $props();

  const reign = $derived(reignLabel(ruler));
  const wars = $derived(ruler.wars ?? []);
  const victories = $derived(wars.filter((war) => war.result === 'zafer').length);
  const family = $derived((ruler.wives?.length ?? 0) + (ruler.children?.length ?? 0));
</script>

<a class="ruler-card" href={hrefRuler(state.id, ruler.id)} aria-label="{ruler.name} hükümdar sayfası">
  <div class="card-header">
    <div class="name-block">
      <h3 class="ruler-name">{ruler.name}</h3>
      {#if ruler.title}
        <div class="ruler-title">{ruler.title}</div>
      {/if}
    </div>
    {#if ruler.claim}
      <span class="claim-tag">Taht iddiası</span>
    {/if}
  </div>

  <div class="meta-pills">
    {#if reign}
      <span class="meta-pill">{reign}</span>
    {/if}
    {#if ruler.birth != null || ruler.death != null}
      <span class="meta-pill">
        {ruler.birth != null ? yearLabel(ruler.birth) : '?'} – {ruler.death != null ? yearLabel(ruler.death) : '?'}
      </span>
    {/if}
    {#if wars.length > 0}
      <span class="meta-pill">
        <Swords size={12} class="icon-war" aria-hidden="true" />
        {victories}/{wars.length} zafer
      </span>
    {/if}
    {#if family > 0}
      <span class="meta-pill">
        <Users size={12} class="icon-person" aria-hidden="true" />
        {family} hanedan kaydı
      </span>
    {/if}
  </div>

  {#if ruler.summary}
    <p class="summary-text">{ruler.summary}</p>
  {/if}

  {#if ruler.traits && ruler.traits.length > 0}
    <div class="traits">
      {#each ruler.traits.slice(0, 3) as trait (trait)}
        <span class="trait-tag">{trait}</span>
      {/each}
    </div>
  {/if}

  <span class="detail-hint">
    Sayfayı aç
    <ChevronRight size={13} aria-hidden="true" />
  </span>
</a>

<style>
  .ruler-card {
    background: var(--bg-card);
    border: 1px solid var(--border-glass);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .ruler-card:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-glass-bright);
    transform: translateY(-2px);
    box-shadow: 0 10px 24px -4px rgba(0, 0, 0, 0.6), 0 0 16px var(--gold-glow);
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
  }

  .name-block {
    min-width: 0;
  }

  .ruler-name {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 17px;
    font-weight: 600;
    color: var(--gold-primary);
    line-height: 1.25;
  }

  .ruler-title {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .summary-text {
    margin: 0;
    font-size: 12px;
    line-height: 1.5;
    color: var(--text-muted);
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .traits {
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
  }

  .trait-tag {
    font-size: 10px;
    color: var(--gold-primary);
    background: rgba(229, 195, 120, 0.08);
    border: 1px solid rgba(229, 195, 120, 0.16);
    padding: 2px 6px;
    border-radius: 6px;
  }

  .detail-hint {
    margin-top: auto;
    display: flex;
    align-items: center;
    gap: 2px;
    font-size: 11px;
    color: var(--text-dim);
    transition: color 0.2s ease;
  }

  .ruler-card:hover .detail-hint {
    color: var(--gold-primary);
  }
</style>
