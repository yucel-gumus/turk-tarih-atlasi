<script lang="ts">
  let { label, value, note }: { label: string; value: string; note?: string } = $props();
</script>

<div class="meta-card">
  <span class="meta-label">{label}</span>
  <span class="meta-val">{value}</span>
  {#if note}
    <span class="meta-sub">{note}</span>
  {/if}
</div>

<style>
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
    line-height: 1.5;
  }
</style>
