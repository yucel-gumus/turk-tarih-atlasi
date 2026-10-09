<script lang="ts">
  import { router } from './lib/router/router.svelte';
  import PageShell from './components/layout/PageShell.svelte';
  import HomePage from './pages/HomePage.svelte';
  import GuidePage from './pages/GuidePage.svelte';
  import SearchPage from './pages/SearchPage.svelte';
  import BattlesPage from './pages/BattlesPage.svelte';
  import TimeMachinePage from './pages/TimeMachinePage.svelte';
  const mapPage = () => import('./pages/MapPage.svelte');
  import StatePage from './pages/StatePage.svelte';
  import RulerPage from './pages/RulerPage.svelte';
  import WarPage from './pages/WarPage.svelte';
  import PersonPage from './pages/PersonPage.svelte';
  import NotFoundNotice from './components/ui/NotFoundNotice.svelte';

  /**
   * Uygulama ince bir dağıtıcıdır: hangi sayfanın çizileceğini adres belirler.
   * Global klavye kısayolu yoktur; gezinme bağlantılar ve geri tuşu ile yürür.
   * Tek klavye etkileşimi arama kutusunun kendi ok/Enter/Escape tuşlarıdır.
   */
  const route = $derived(router.route);
</script>

<PageShell>
  {#if route.name === 'home'}
    <HomePage region={route.region} />
  {:else if route.name === 'guide'}
    <GuidePage />
  {:else if route.name === 'battles'}
    <BattlesPage />
  {:else if route.name === 'timeMachine'}
    <TimeMachinePage year={route.year} />
  {:else if route.name === 'map'}
    {#await mapPage()}
      <p role="status">Harita yükleniyor…</p>
    {:then module}
      <module.default />
    {:catch}
      <p role="alert">Harita yüklenemedi. Bağlantınızı kontrol edip sayfayı yenileyin.</p>
    {/await}
  {:else if route.name === 'search'}
    <SearchPage query={route.query} />
  {:else if route.name === 'state'}
    <StatePage stateId={route.stateId} />
  {:else if route.name === 'ruler'}
    <RulerPage stateId={route.stateId} rulerId={route.rulerId} />
  {:else if route.name === 'war'}
    <WarPage stateId={route.stateId} rulerId={route.rulerId} index={route.index} slug={route.slug} />
  {:else if route.name === 'person'}
    <PersonPage
      stateId={route.stateId}
      rulerId={route.rulerId}
      role={route.role}
      index={route.index}
      slug={route.slug}
    />
  {:else}
    <NotFoundNotice raw={route.raw} />
  {/if}
</PageShell>
