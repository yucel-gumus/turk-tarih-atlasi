<script lang="ts">
  import type { State, Ruler } from '../../schemas/atlas.schema';
  import { hrefPerson, hrefRuler } from '../../lib/router/route';
  import { reignLabel } from '../../lib/data/lookup';
  import { canon } from '../../lib/text';
  import Crown from '@lucide/svelte/icons/crown';
  import Heart from '@lucide/svelte/icons/heart';
  import Users from '@lucide/svelte/icons/users';
  import User from '@lucide/svelte/icons/user';
  import ChevronRight from '@lucide/svelte/icons/chevron-right';
  import Search from '@lucide/svelte/icons/search';

  let { state: targetState }: { state: State } = $props();

  let filterText = $state('');

  // Soyağacı istatistikleri
  const totalWives = $derived(
    targetState.rulers.reduce((acc, r) => acc + (r.wives?.length ?? 0), 0)
  );
  const totalChildren = $derived(
    targetState.rulers.reduce((acc, r) => acc + (r.children?.length ?? 0), 0)
  );

  // Bu devletteki hükümdarların isim kümesi (çocuklardan hangisi tahta çıktı tespit etmek için)
  const rulerNameSet = $derived.by(() => {
    const set = new Set<string>();
    for (const r of targetState.rulers) {
      set.add(canon(r.name));
      for (const a of r.aliases ?? []) {
        set.add(canon(a));
      }
    }
    return set;
  });

  function isChildEnthroned(childName: string): boolean {
    const c = canon(childName);
    for (const rName of rulerNameSet) {
      if (rName.includes(c) || c.includes(rName)) return true;
    }
    return false;
  }

  const filteredRulers = $derived.by(() => {
    const q = canon(filterText.trim());
    if (!q) return targetState.rulers;

    return targetState.rulers.filter((r) => {
      if (canon(r.name).includes(q)) return true;
      if ((r.aliases ?? []).some((a) => canon(a).includes(q))) return true;
      if ((r.wives ?? []).some((w) => canon(w.name).includes(q))) return true;
      if ((r.children ?? []).some((c) => canon(c.name).includes(q))) return true;
      return false;
    });
  });
</script>

<div class="dynasty-root">
  <!-- Soyağacı İstatistik ve Açıklama Bandı -->
  <div class="dynasty-banner">
    <div class="stats-pills">
      <span class="meta-pill"><Crown size={12} aria-hidden="true" /> {targetState.rulers.length} Hükümdar</span>
      {#if totalWives > 0}
        <span class="meta-pill"><Heart size={12} aria-hidden="true" /> {totalWives} Kayıtlı Eş / Hatun</span>
      {/if}
      {#if totalChildren > 0}
        <span class="meta-pill"><Users size={12} class="icon-user" aria-hidden="true" /> {totalChildren} Şehzade & Çocuk</span>
      {/if}
    </div>

    <div class="tree-search">
      <Search size={14} class="search-icon" aria-hidden="true" />
      <input
        type="search"
        class="tree-search-input"
        placeholder="Hükümdar, valide veya şehzade ara..."
        bind:value={filterText}
      />
    </div>
  </div>

  {#if filteredRulers.length === 0}
    <div class="empty-tree">Arama kriterinize uygun hanedan üyesi bulunamadı.</div>
  {:else}
    <div class="tree-timeline">
      {#each filteredRulers as ruler, i (ruler.id)}
        <div class="tree-node">
          <!-- Sol Akış Çizgisi ve Nesil Numarası -->
          <div class="node-spine">
            <div class="node-badge" title="{i + 1}. Hükümdar">{i + 1}</div>
            {#if i < filteredRulers.length - 1}
              <div class="node-line"></div>
            {/if}
          </div>

          <!-- Sağ İçerik: Hükümdar ve Aile Kartı -->
          <div class="node-card">
            <!-- Hükümdar Başlığı -->
            <a class="ruler-banner" href={hrefRuler(targetState.id, ruler.id)}>
              <div class="ruler-meta-left">
                <Crown size={16} aria-hidden="true" />
                <div>
                  <h4 class="ruler-name">{ruler.name}</h4>
                  {#if ruler.title}
                    <span class="ruler-title">{ruler.title}</span>
                  {/if}
                </div>
              </div>
              <div class="ruler-meta-right">
                <span class="reign-badge">{reignLabel(ruler) || 'Dönem belirsiz'}</span>
                <ChevronRight size={14} aria-hidden="true" />
              </div>
            </a>

            <!-- Aile İçi Not / Veraset Notu -->
            {#if ruler.familyNotes && ruler.familyNotes.length > 0}
              <div class="family-note-box">
                <b>Veraset & Aile:</b> {ruler.familyNotes.join(' ')}
              </div>
            {/if}

            <!-- Eşler ve Çocuklar -->
            {#if (ruler.wives && ruler.wives.length > 0) || (ruler.children && ruler.children.length > 0)}
              <div class="family-branches">
                <!-- Eşler / Hatunlar -->
                {#if ruler.wives && ruler.wives.length > 0}
                  <div class="branch-group">
                    <span class="branch-title">
                      <Heart size={11} aria-hidden="true" /> Eşler ({ruler.wives.length})
                    </span>
                    <div class="members-list">
                      {#each ruler.wives as wife, wIdx (wife.name + wIdx)}
                        <a
                          class="member-pill wife-pill"
                          href={hrefPerson(targetState.id, ruler.id, 'es', wIdx + 1, wife.name)}
                        >
                          <span class="member-name">{wife.name}</span>
                          {#if wife.note}
                            <span class="member-sub">{wife.note}</span>
                          {/if}
                        </a>
                      {/each}
                    </div>
                  </div>
                {/if}

                <!-- Çocuklar / Şehzadeler -->
                {#if ruler.children && ruler.children.length > 0}
                  <div class="branch-group">
                    <span class="branch-title">
                      <User size={11} aria-hidden="true" /> Çocuklar & Şehzadeler ({ruler.children.length})
                    </span>
                    <div class="members-list">
                      {#each ruler.children as child, cIdx (child.name + cIdx)}
                        {@const enthroned = isChildEnthroned(child.name)}
                        <a
                          class="member-pill child-pill"
                          class:enthroned
                          href={hrefPerson(targetState.id, ruler.id, 'cocuk', cIdx + 1, child.name)}
                        >
                          <span class="member-name">
                            {#if enthroned}
                              <Crown size={10} aria-hidden="true" />
                            {/if}
                            {child.name}
                          </span>
                          {#if enthroned}
                            <span class="enthroned-tag">Tahta Çıktı</span>
                          {:else if child.note}
                            <span class="member-sub">{child.note}</span>
                          {/if}
                        </a>
                      {/each}
                    </div>
                  </div>
                {/if}
              </div>
            {/if}
          </div>
        </div>
      {/each}
    </div>
  {/if}
</div>

<style>
  .dynasty-root {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .dynasty-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }

  .stats-pills {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }

  .meta-pill {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-size: 11.5px;
    padding: 4px 10px;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 999px;
    color: var(--ink-soft);
  }

  .tree-search {
    position: relative;
    display: flex;
    align-items: center;
    min-width: 240px;
  }

  .tree-search :global(.search-icon) {
    position: absolute;
    left: 10px;
    color: var(--ink-dim);
    pointer-events: none;
  }

  .tree-search-input {
    width: 100%;
    padding: 6px 12px 6px 30px;
    font-size: 12px;
    background: var(--surface-2);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--ink);
    outline: none;
  }

  .tree-search-input:focus {
    border-color: var(--accent);
    background: var(--surface-1);
  }

  .tree-timeline {
    display: flex;
    flex-direction: column;
    gap: 16px;
    position: relative;
  }

  .tree-node {
    display: flex;
    gap: 16px;
    position: relative;
  }

  .node-spine {
    display: flex;
    flex-direction: column;
    align-items: center;
    flex-shrink: 0;
    width: 32px;
  }

  .node-badge {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: var(--surface-3);
    border: 2px solid var(--surface-1);
    color: var(--ink-soft);
    font-size: 11px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 1px var(--border);
    z-index: 2;
  }

  .node-line {
    flex-grow: 1;
    width: 2px;
    background: var(--border-strong);
    margin: 4px 0 -12px;
  }

  .node-card {
    flex-grow: 1;
    background: var(--surface-1);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    box-shadow: var(--shadow-sm);
  }

  .ruler-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    text-decoration: none;
    color: inherit;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
    transition: color 0.18s ease;
  }

  .ruler-banner:hover .ruler-name {
    color: var(--accent);
  }

  .ruler-meta-left {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .ruler-name {
    margin: 0;
    font-family: var(--font-serif);
    font-size: 16px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.2;
  }

  .ruler-title {
    font-size: 11.5px;
    color: var(--ink-dim);
  }

  .ruler-meta-right {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .reign-badge {
    font-size: 12px;
    font-weight: 600;
    color: var(--accent);
    background: var(--surface-2);
    padding: 3px 8px;
    border-radius: 6px;
  }

  .family-note-box {
    font-size: 12px;
    line-height: 1.4;
    background: var(--warn-bg);
    color: var(--warn-ink);
    padding: 6px 10px;
    border-radius: 6px;
    border-left: 3px solid var(--accent);
  }

  .family-branches {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .branch-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .branch-title {
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--ink-dim);
    display: flex;
    align-items: center;
    gap: 5px;
  }

  .members-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .member-pill {
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11.5px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    transition: all 0.18s ease;
    border: 1px solid var(--border);
  }

  .wife-pill {
    background: #fdf6f7;
    color: #8c2841;
    border-color: #f3d4dc;
  }

  .wife-pill:hover {
    background: #fae8ec;
    border-color: #e5a4b5;
  }

  .child-pill {
    background: #f4f8f9;
    color: #1b5b6d;
    border-color: #d1e5ea;
  }

  .child-pill:hover {
    background: #e6f1f4;
    border-color: #a4cbd5;
  }

  .child-pill.enthroned {
    background: #fdf8ed;
    color: #8f580f;
    border-color: #edd59b;
    font-weight: 600;
  }

  .enthroned-tag {
    font-size: 9.5px;
    background: var(--accent);
    color: #ffffff;
    padding: 1px 5px;
    border-radius: 4px;
    font-weight: 600;
  }

  .member-sub {
    font-size: 10px;
    color: var(--ink-dim);
    max-width: 140px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .empty-tree {
    text-align: center;
    padding: 32px 16px;
    color: var(--ink-dim);
    background: var(--surface-1);
    border: 1px dashed var(--border);
    border-radius: 12px;
  }
</style>
