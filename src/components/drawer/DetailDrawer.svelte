<script lang="ts">
  import { ui } from '../../lib/stores/ui.svelte';
  import { yearLabel, RESULT_MAP, CERTAINTY_MAP } from '../../lib/data/atlas';
  import { X, ExternalLink, Swords, Users, Landmark, Compass, Award, Scroll, BookMarked } from '@lucide/svelte';

  const ruler = $derived(ui.selectedRuler);
  const rulerState = $derived(ui.selectedRulerState);
  const state = $derived(ui.selectedState);

  function close() {
    ui.closeDetail();
  }

  function onKeyDown(e: KeyboardEvent) {
    if (e.key === 'Escape') close();
  }
</script>

<svelte:window onkeydown={onKeyDown} />

{#if ui.isDetailDrawerOpen}
  <!-- Backdrop -->
  <!-- svelte-ignore a11y_click_events_have_key_events -->
  <div class="drawer-backdrop" onclick={close} role="presentation"></div>

  <!-- Slide-over Drawer Panel -->
  <div
    class="drawer-panel glass-panel"
    role="dialog"
    aria-modal="true"
    aria-label={ruler ? `${ruler.name} ayrıntılı bilgisi` : state ? `${state.name} devlet bilgisi` : 'Detay paneli'}
  >
    <div class="drawer-header">
      <div class="header-titles">
        {#if ruler}
          <span class="eyebrow">{rulerState?.name || 'Hükümdar'}</span>
          <h2 class="drawer-title">{ruler.name}</h2>
          {#if ruler.title}
            <p class="drawer-subtitle">{ruler.title}</p>
          {/if}
        {:else if state}
          <span class="eyebrow">Türk Devleti</span>
          <h2 class="drawer-title">{state.name}</h2>
          {#if state.short && state.short !== state.name}
            <p class="drawer-subtitle">{state.short}</p>
          {/if}
        {/if}
      </div>

      <button type="button" class="close-btn" onclick={close} aria-label="Paneli kapat">
        <X size={18} />
      </button>
    </div>

    <div class="drawer-content">
      {#if ruler}
        <!-- RULER VIEW -->
        <!-- Reign & Life -->
        <div class="meta-section">
          <div class="meta-card">
            <span class="meta-label">Saltanat</span>
            <span class="meta-val">
              {#if ruler.reign}
                {ruler.reign[0] != null ? yearLabel(ruler.reign[0]) : '?'} – {ruler.reign[1] != null ? yearLabel(ruler.reign[1]) : '?'}
              {:else}
                Bilinmiyor
              {/if}
            </span>
            {#if ruler.reignNote}
              <span class="meta-sub">{ruler.reignNote}</span>
            {/if}
          </div>

          <div class="meta-card">
            <span class="meta-label">Yaşam Süresi</span>
            <span class="meta-val">
              {ruler.birth != null ? yearLabel(ruler.birth) : '?'} – {ruler.death != null ? yearLabel(ruler.death) : '?'}
            </span>
            {#if ruler.deathNote}
              <span class="meta-sub">{ruler.deathNote}</span>
            {/if}
          </div>
        </div>

        <!-- Summary -->
        {#if ruler.summary}
          <section class="section-box">
            <h3 class="section-heading"><BookMarked size={15} /> Genel Bakış</h3>
            <p class="body-text">{ruler.summary}</p>
          </section>
        {/if}

        <!-- Contribution & Harm -->
        {#if ruler.contribution || ruler.harm}
          <div class="contrast-grid">
            {#if ruler.contribution}
              <div class="contrast-card positive">
                <span class="contrast-label">Tarihe Katkısı & Başarı</span>
                <p>{ruler.contribution}</p>
              </div>
            {/if}
            {#if ruler.harm}
              <div class="contrast-card negative">
                <span class="contrast-label">Hata & Olumsuz Miras</span>
                <p>{ruler.harm}</p>
              </div>
            {/if}
          </div>
        {/if}

        <!-- Battles -->
        {#if ruler.wars && ruler.wars.length > 0}
          <section class="section-box">
            <h3 class="section-heading"><Swords size={15} /> Savaşlar & Seferler ({ruler.wars.length})</h3>
            <div class="wars-list">
              {#each ruler.wars as war}
                {@const resInfo = RESULT_MAP[war.result || 'belirsiz']}
                <div class="war-item">
                  <div class="war-info">
                    <div class="war-header-row">
                      <span class="war-name">{war.name}</span>
                      {#if war.when}
                        <span class="war-year">({war.when})</span>
                      {/if}
                    </div>
                    {#if war.foe}
                      <div class="war-foe">Karşı Taraf: <b>{war.foe}</b></div>
                    {/if}
                    {#if war.note}
                      <p class="war-note">{war.note}</p>
                    {/if}
                  </div>
                  <span class="result-badge {war.result || 'belirsiz'}">
                    {resInfo?.label || war.result}
                  </span>
                </div>
              {/each}
            </div>
          </section>
        {/if}

        <!-- Genealogy: Wives and Children -->
        {#if (ruler.wives && ruler.wives.length > 0) || (ruler.children && ruler.children.length > 0)}
          <section class="section-box">
            <h3 class="section-heading"><Users size={15} /> Hanedan & Aile Şeceresi</h3>
            {#if ruler.wives && ruler.wives.length > 0}
              <div class="family-subgroup">
                <h4 class="sub-title">Eşleri / Hatunları</h4>
                <div class="people-pills">
                  {#each ruler.wives as wife}
                    <div class="person-pill">
                      <span class="person-name">{wife.name}</span>
                      {#if wife.certainty && wife.certainty !== 'kesin'}
                        <span class="cert-tag {wife.certainty}">{CERTAINTY_MAP[wife.certainty]}</span>
                      {/if}
                      {#if wife.note}
                        <span class="person-note">{wife.note}</span>
                      {/if}
                    </div>
                  {/each}
                </div>
              </div>
            {/if}

            {#if ruler.children && ruler.children.length > 0}
              <div class="family-subgroup">
                <h4 class="sub-title">Çocukları / Şehzadeleri</h4>
                <div class="people-pills">
                  {#each ruler.children as child}
                    <div class="person-pill">
                      <span class="person-name">{child.name}</span>
                      {#if child.mother}
                        <span class="mother-tag">Valide: {child.mother}</span>
                      {/if}
                      {#if child.certainty && child.certainty !== 'kesin'}
                        <span class="cert-tag {child.certainty}">{CERTAINTY_MAP[child.certainty]}</span>
                      {/if}
                      {#if child.note}
                        <span class="person-note">{child.note}</span>
                      {/if}
                    </div>
                  {/each}
                </div>
              </div>
            {/if}
          </section>
        {/if}

        <!-- Traits & Legends -->
        {#if (ruler.traits && ruler.traits.length > 0) || (ruler.legends && ruler.legends.length > 0)}
          <section class="section-box">
            {#if ruler.traits && ruler.traits.length > 0}
              <h3 class="section-heading"><Award size={15} /> Nitelikler & Şahsiyet</h3>
              <div class="tags-cluster">
                {#each ruler.traits as t}
                  <span class="trait-badge">{t}</span>
                {/each}
              </div>
            {/if}

            {#if ruler.legends && ruler.legends.length > 0}
              <div class="legends-box">
                <h4 class="sub-title">Rivayet ve Menkıbeler</h4>
                {#each ruler.legends as leg}
                  <blockquote class="legend-quote">"{leg}"</blockquote>
                {/each}
              </div>
            {/if}
          </section>
        {/if}

        <!-- Sources -->
        {#if ruler.sources && ruler.sources.length > 0}
          <section class="section-box">
            <h3 class="section-heading"><Scroll size={15} /> Doğrulanmış Kaynaklar</h3>
            <div class="sources-list">
              {#each ruler.sources as src}
                <a href={src.url} target="_blank" rel="noopener noreferrer" class="source-link">
                  <span>{src.title}</span>
                  <ExternalLink size={12} />
                </a>
              {/each}
            </div>
          </section>
        {/if}

      {:else if state}
        <!-- STATE VIEW -->
        <div class="meta-section">
          <div class="meta-card">
            <span class="meta-label">Tarih Aralığı</span>
            <span class="meta-val">{yearLabel(state.start)} – {yearLabel(state.end)}</span>
            {#if state.startNote || state.endNote}
              <span class="meta-sub">{state.startNote} {state.endNote}</span>
            {/if}
          </div>

          {#if state.capital}
            <div class="meta-card">
              <span class="meta-label">Başkent</span>
              <span class="meta-val">{state.capital}</span>
            </div>
          {/if}

          {#if state.religion}
            <div class="meta-card">
              <span class="meta-label">İnanç & Din</span>
              <span class="meta-val">{state.religion}</span>
            </div>
          {/if}
        </div>

        {#if state.summary}
          <section class="section-box">
            <h3 class="section-heading"><BookMarked size={15} /> Özet</h3>
            <p class="body-text">{state.summary}</p>
          </section>
        {/if}

        {#if state.essay && state.essay.length > 0}
          <section class="section-box">
            <h3 class="section-heading"><Scroll size={15} /> Tarihi İnceleme & Gelişim</h3>
            {#each state.essay as p}
              <p class="body-text essay-paragraph">{p}</p>
            {/each}
          </section>
        {/if}

        {#if state.legacy}
          <section class="section-box">
            <h3 class="section-heading"><Award size={15} /> Tarihi Miras & Etki</h3>
            <p class="body-text">{state.legacy}</p>
          </section>
        {/if}

        {#if state.sources && state.sources.length > 0}
          <section class="section-box">
            <h3 class="section-heading"><Scroll size={15} /> Kaynaklar</h3>
            <div class="sources-list">
              {#each state.sources as src}
                <a href={src.url} target="_blank" rel="noopener noreferrer" class="source-link">
                  <span>{src.title}</span>
                  <ExternalLink size={12} />
                </a>
              {/each}
            </div>
          </section>
        {/if}
      {/if}
    </div>
  </div>
{/if}

<style>
  .drawer-backdrop {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(4px);
    z-index: 90;
    animation: fadeIn 0.2s ease;
  }

  .drawer-panel {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    width: min(520px, 100vw);
    background: rgba(14, 18, 23, 0.94);
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    border-left: 1px solid var(--border-glass-bright);
    z-index: 100;
    display: flex;
    flex-direction: column;
    box-shadow: -16px 0 48px rgba(0, 0, 0, 0.7);
    animation: slideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  }

  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes slideIn {
    from { transform: translateX(100%); }
    to { transform: translateX(0); }
  }

  .drawer-header {
    padding: 20px 24px;
    border-bottom: 1px solid var(--border-glass);
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 16px;
  }

  .eyebrow {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--gold-primary);
  }

  .drawer-title {
    margin: 4px 0 0;
    font-family: var(--font-serif);
    font-size: 26px;
    font-weight: 700;
    color: var(--text-main);
    line-height: 1.2;
  }

  .drawer-subtitle {
    margin: 4px 0 0;
    font-size: 13px;
    color: var(--text-muted);
  }

  .close-btn {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-muted);
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border-glass);
    transition: all 0.2s ease;
  }

  .close-btn:hover {
    color: var(--text-main);
    background: rgba(255, 255, 255, 0.1);
  }

  .drawer-content {
    padding: 24px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 20px;
    flex-grow: 1;
  }

  .meta-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 10px;
  }

  .meta-card {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border-glass);
    padding: 10px 14px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .meta-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: var(--text-dim);
  }

  .meta-val {
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 600;
    color: var(--gold-primary);
  }

  .meta-sub {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .section-box {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 16px;
  }

  .section-heading {
    margin: 0 0 12px;
    font-size: 13px;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--gold-primary);
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }

  .body-text {
    margin: 0;
    font-size: 13px;
    line-height: 1.65;
    color: #cbd5e1;
  }

  .essay-paragraph {
    margin-bottom: 12px;
  }

  .contrast-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .contrast-card {
    border-radius: 10px;
    padding: 12px 14px;
    font-size: 12px;
    line-height: 1.5;
  }

  .contrast-card.positive {
    background: rgba(74, 222, 128, 0.06);
    border: 1px solid rgba(74, 222, 128, 0.2);
    color: #86efac;
  }

  .contrast-card.negative {
    background: rgba(248, 113, 113, 0.06);
    border: 1px solid rgba(248, 113, 113, 0.2);
    color: #fca5a5;
  }

  .contrast-label {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    display: block;
    margin-bottom: 4px;
  }

  .wars-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .war-item {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    padding: 10px 12px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
  }

  .war-header-row {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .war-name {
    font-size: 13px;
    font-weight: 600;
    color: var(--text-main);
  }

  .war-year {
    font-size: 11px;
    color: var(--text-dim);
  }

  .war-foe {
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 2px;
  }

  .war-note {
    font-size: 11px;
    color: var(--text-dim);
    margin: 4px 0 0;
  }

  .result-badge {
    font-size: 11px;
    font-weight: 600;
    padding: 3px 8px;
    border-radius: 6px;
    white-space: nowrap;
  }
  .result-badge.zafer { background: rgba(74, 222, 128, 0.15); color: #86efac; border: 1px solid rgba(74, 222, 128, 0.3); }
  .result-badge.yenilgi { background: rgba(248, 113, 113, 0.15); color: #fca5a5; border: 1px solid rgba(248, 113, 113, 0.3); }
  .result-badge.sonucsuz { background: rgba(251, 191, 36, 0.15); color: #fde047; border: 1px solid rgba(251, 191, 36, 0.3); }
  .result-badge.antlasma { background: rgba(56, 189, 248, 0.15); color: #7dd3fc; border: 1px solid rgba(56, 189, 248, 0.3); }
  .result-badge.belirsiz { background: rgba(148, 163, 184, 0.15); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.3); }

  .family-subgroup {
    margin-top: 10px;
  }

  .sub-title {
    margin: 0 0 8px;
    font-size: 11px;
    text-transform: uppercase;
    color: var(--text-muted);
  }

  .people-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .person-pill {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    padding: 4px 10px;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
  }

  .cert-tag {
    font-size: 9px;
    padding: 1px 4px;
    border-radius: 4px;
  }
  .cert-tag.tartismali { background: rgba(251, 191, 36, 0.2); color: #fde047; }
  .cert-tag.rivayet { background: rgba(168, 85, 247, 0.2); color: #d8b4fe; }

  .mother-tag {
    font-size: 10px;
    color: var(--text-dim);
  }

  .person-note {
    font-size: 10px;
    color: var(--text-dim);
  }

  .tags-cluster {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .trait-badge {
    background: rgba(229, 195, 120, 0.08);
    border: 1px solid rgba(229, 195, 120, 0.2);
    color: var(--gold-primary);
    padding: 4px 10px;
    border-radius: 9999px;
    font-size: 11px;
  }

  .legends-box {
    margin-top: 14px;
  }

  .legend-quote {
    margin: 6px 0 0;
    padding: 8px 12px;
    border-left: 2px solid var(--gold-primary);
    background: rgba(229, 195, 120, 0.04);
    font-style: italic;
    font-size: 12px;
    color: #cbd5e1;
    border-radius: 0 6px 6px 0;
  }

  .sources-list {
    display: flex;
    flex-direction: column;
    gap: 6px;
  }

  .source-link {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 12px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 8px;
    font-size: 12px;
    color: var(--gold-primary);
    text-decoration: none;
    transition: background 0.2s ease;
  }

  .source-link:hover {
    background: rgba(229, 195, 120, 0.08);
    border-color: var(--border-glass-bright);
  }
</style>
