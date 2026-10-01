<script lang="ts">
  import type { Person } from '../../schemas/atlas.schema';
  import { CERTAINTY_MAP } from '../../lib/data/atlas';

  let {
    person,
    href,
    motherHref = null,
  }: { person: Person; href: string; motherHref?: string | null } = $props();
</script>

<!-- Pill'in tamamı bağlantı değildir: içinde anne bağlantısı da bulunur ve
     bağlantı içinde bağlantı geçersiz HTML olurdu. Ad, kişi sayfasına gider. -->
<div class="person-pill">
  <a class="person-name" {href}>{person.name}</a>

  {#if person.mother}
    {#if motherHref}
      <a class="mother-tag mother-link" href={motherHref}>Valide: {person.mother}</a>
    {:else}
      <span class="mother-tag">Valide: {person.mother}</span>
    {/if}
  {/if}

  {#if person.certainty !== 'kesin'}
    <span class="cert-tag {person.certainty}">{CERTAINTY_MAP[person.certainty]}</span>
  {/if}

  {#if person.note}
    <span class="person-note">{person.note}</span>
  {/if}
</div>

<style>
  .person-pill {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    padding: 4px 10px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    flex-wrap: wrap;
    transition: border-color 0.18s ease, background 0.18s ease;
  }

  .person-pill:hover {
    border-color: var(--border-glass-bright);
    background: rgba(255, 255, 255, 0.06);
  }

  .person-name {
    font-weight: 600;
    color: var(--text-main);
  }

  .person-name:hover {
    color: var(--gold-primary);
  }

  .mother-link {
    text-decoration: underline;
    text-decoration-style: dotted;
    text-underline-offset: 2px;
  }

  .mother-link:hover {
    color: var(--gold-primary);
  }

  .person-note {
    font-size: 10px;
    color: var(--text-dim);
  }
</style>
