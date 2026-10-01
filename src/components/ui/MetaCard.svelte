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
    background: var(--surface-1);
    border: 1px solid var(--border);
    padding: 11px 14px;
    border-radius: 12px;
    display: flex;
    flex-direction: column;
    gap: 3px;
    box-shadow: var(--shadow-sm);
  }

  .meta-label {
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: var(--ink-dim);
  }

  .meta-val {
    font-family: var(--font-serif);
    font-size: 15px;
    font-weight: 600;
    color: var(--ink);
  }

  .meta-sub {
    font-size: 11px;
    color: var(--ink-muted);
    margin-top: 2px;
    line-height: 1.5;
  }
</style>
