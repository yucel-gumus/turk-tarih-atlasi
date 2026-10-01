<script lang="ts">
  import NotFoundNotice from '../components/ui/NotFoundNotice.svelte';

  /** Hem bozuk sözdizimi hem çözülemeyen kimlik buraya düşer; bildirim tek kaynaktır. */
  let { raw }: { raw: string } = $props();
</script>

<NotFoundNotice {raw} />
