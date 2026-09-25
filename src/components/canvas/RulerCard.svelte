<script lang="ts">
  import type { Ruler, State } from '../../schemas/atlas.schema';
  import { yearLabel, RESULT_MAP, CERTAINTY_MAP } from '../../lib/data/atlas';
  import { ui } from '../../lib/stores/ui.svelte';
  import { Shield, Sparkles, ChevronRight, Swords } from '@lucide/svelte';

  let { ruler, state }: { ruler: Ruler; state: State } = $props();

  const reignStr = $derived.by(() => {
    const [start, end] = ruler.reign || [null, null];
    if (start == null && end == null) return null;
    return `${start != null ? yearLabel(start) : '?'} – ${end != null ? yearLabel(end) : '?'}`;
  });

  const victoryCount = $derived(ruler.wars?.filter((w) => w.result === 'zafer').length || 0);
  const totalWars = $derived(ruler.wars?.length || 0);
  const familyCount = $derived((ruler.wives?.length || 0) + (ruler.children?.length || 0));

  function openDetail() {
    ui.openRulerDetail(ruler, state);
  }
</script>

<div
  role="button"
  tabindex="0"
  class="ruler-card group"
  onclick={openDetail}
  onkeydown={(e) => (e.key === 'Enter' || e.key === ' ') && openDetail()}
  aria-label="{ruler.name} kartı, detay için tıklayın"
>
  <!-- Background ghost monogram -->
  <div class="ghost-monogram" aria-hidden="true">
    {ruler.name.slice(0, 1)}
  </div>

  <div class="card-inner">
    <!-- Header -->
    <div class="card-header">
      <div>
        <h4 class="ruler-name">{ruler.name}</h4>
        {#if ruler.title}
          <div class="ruler-title">{ruler.title}</div>
        {/if}
      </div>

      {#if ruler.claim}
        <span class="badge-claim">Talip</span>
      {/if}
    </div>

    <!-- Reign & Life -->
    <div class="meta-row">
      {#if reignStr}
        <div class="reign-pill">
          <span class="dot"></span>
          <span>{reignStr}</span>
        </div>
      {/if}

      {#if ruler.birth != null || ruler.death != null}
        <div class="life-dates">
          ({ruler.birth != null ? yearLabel(ruler.birth) : '?'}&thinsp;–&thinsp;{ruler.death != null ? yearLabel(ruler.death) : '?'})
        </div>
      {/if}
    </div>

    <!-- Summary -->
    {#if ruler.summary}
      <p class="summary-text line-clamp-3">
        {ruler.summary}
      </p>
    {/if}

    <!-- Highlights Badges -->
    <div class="badges-footer">
      {#if totalWars > 0}
        <div class="stat-badge war-stat">
          <Swords size={12} class="text-amber-400" />
          <span>{victoryCount}/{totalWars} Zafer</span>
        </div>
      {/if}

      {#if familyCount > 0}
        <div class="stat-badge family-stat">
          <Shield size={12} class="text-sky-400" />
          <span>{familyCount} Hanedan</span>
        </div>
      {/if}

      {#if ruler.traits && ruler.traits.length > 0}
        <div class="trait-tag">
          {ruler.traits[0]}
        </div>
      {/if}

      <div class="detail-hint">
        <span>Detay</span>
        <ChevronRight size={13} />
      </div>
    </div>
  </div>
</div>

<style>
  .ruler-card {
    position: relative;
    background: var(--bg-card);
    backdrop-filter: blur(8px);
    border: 1px solid var(--border-glass);
    border-radius: 12px;
    padding: 14px 16px;
    overflow: hidden;
    cursor: pointer;
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    outline: none;
    text-align: left;
    display: flex;
    flex-direction: column;
    min-height: 190px;
  }

  .ruler-card:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-glass-bright);
    transform: translateY(-2px);
    box-shadow: 0 10px 24px -4px rgba(0, 0, 0, 0.6), 0 0 16px var(--gold-glow);
  }

  .ruler-card:focus-visible {
    border-color: var(--gold-primary);
    box-shadow: 0 0 0 2px var(--gold-primary);
  }

  .ghost-monogram {
    position: absolute;
    right: 6px;
    top: -12px;
    font-family: var(--font-serif);
    font-size: 88px;
    font-weight: 700;
    color: rgba(229, 195, 120, 0.04);
    line-height: 1;
    pointer-events: none;
    transition: transform 0.3s ease;
  }

  .ruler-card:hover .ghost-monogram {
    transform: scale(1.08) translateX(-4px);
    color: rgba(229, 195, 120, 0.08);
  }

  .card-inner {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 8px;
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

  .badge-claim {
    background: rgba(248, 113, 113, 0.15);
    border: 1px solid rgba(248, 113, 113, 0.3);
    color: #fca5a5;
    font-size: 10px;
    padding: 1px 6px;
    border-radius: 9999px;
  }

  .meta-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 8px;
    font-size: 11px;
    flex-wrap: wrap;
  }

  .reign-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: rgba(255, 255, 255, 0.05);
    padding: 2px 7px;
    border-radius: 6px;
    font-weight: 600;
    color: var(--text-main);
  }

  .reign-pill .dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: var(--gold-primary);
  }

  .life-dates {
    color: var(--text-dim);
  }

  .summary-text {
    margin: 8px 0 12px;
    font-size: 12px;
    line-height: 1.45;
    color: var(--text-muted);
    display: -webkit-box;
    -webkit-line-clamp: 3;
    line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    flex-grow: 1;
  }

  .badges-footer {
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: auto;
    font-size: 11px;
  }

  .stat-badge {
    display: flex;
    align-items: center;
    gap: 4px;
    background: rgba(255, 255, 255, 0.04);
    padding: 3px 6px;
    border-radius: 6px;
    color: var(--text-muted);
  }

  .trait-tag {
    background: rgba(229, 195, 120, 0.08);
    border: 1px solid rgba(229, 195, 120, 0.16);
    color: var(--gold-primary);
    padding: 2px 6px;
    border-radius: 6px;
    font-size: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 90px;
  }

  .detail-hint {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 2px;
    color: var(--text-dim);
    transition: color 0.2s ease;
  }

  .ruler-card:hover .detail-hint {
    color: var(--gold-primary);
  }
</style>
