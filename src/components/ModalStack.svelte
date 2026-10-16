<script lang="ts">
  import Modal from './Modal.svelte';
  import StateView from './views/StateView.svelte';
  import ContextView from './views/ContextView.svelte';
  import RulerView from './views/RulerView.svelte';
  import WarView from './views/WarView.svelte';
  import { modals, type ModalEntry } from '../lib/modals.svelte';
  import {
    getState,
    getContext,
    getRuler,
    getWar,
    isOngoing,
    reignLabel,
    spanLabel,
    REGION_COLORS,
    REGION_NAMES,
  } from '../lib/data/atlas';

  interface Head {
    crumb: string;
    kicker: string;
    title: string;
    subtitle: string;
    accent: string;
  }

  function head(e: ModalEntry): Head {
    if (e.kind === 'state') {
      const s = getState(e.id)!;
      return {
        crumb: s.short || s.name,
        kicker: `Devlet · ${REGION_NAMES[s.region]}`,
        title: s.name,
        subtitle: spanLabel(s.start, s.end, isOngoing(s)),
        accent: REGION_COLORS[s.region],
      };
    }
    if (e.kind === 'context') {
      const c = getContext(e.id)!;
      return { crumb: c.short, kicker: 'Bağlam', title: c.name, subtitle: spanLabel(c.start, c.end), accent: 'var(--ink-muted)' };
    }
    const s = getState(e.stateId)!;
    const r = getRuler(e.stateId, e.rulerId)!;
    if (e.kind === 'ruler') {
      return {
        crumb: r.name,
        kicker: `${r.title || 'Hükümdar'} · ${s.short || s.name}`,
        title: r.name,
        subtitle: reignLabel(r, isOngoing(s)),
        accent: REGION_COLORS[s.region],
      };
    }
    const w = getWar(e)!;
    return {
      crumb: w.war.name,
      kicker: `Savaş · ${s.short || s.name}`,
      title: w.war.name,
      subtitle: w.war.when,
      accent: REGION_COLORS[s.region],
    };
  }

  const heads = $derived(modals.items.map(head));
</script>

{#each modals.items as entry, i (i + ':' + JSON.stringify(entry))}
  {@const h = heads[i]}
  <Modal
    depth={i + 1}
    crumbs={['Soy ağacı', ...heads.slice(0, i + 1).map((x) => x.crumb)]}
    kicker={h.kicker}
    title={h.title}
    subtitle={h.subtitle}
    accent={h.accent}
  >
    {#if entry.kind === 'state'}
      <StateView id={entry.id} />
    {:else if entry.kind === 'context'}
      <ContextView id={entry.id} />
    {:else if entry.kind === 'ruler'}
      <RulerView stateId={entry.stateId} rulerId={entry.rulerId} />
    {:else}
      <WarView stateId={entry.stateId} rulerId={entry.rulerId} index={entry.index} />
    {/if}
  </Modal>
{/each}
