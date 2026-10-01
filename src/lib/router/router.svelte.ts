import { parseHash, type Route } from './route';

/**
 * Hash tabanlı yönlendirici. Tek dinleyici `hashchange`'tir: Chrome geri ve
 * ileri tuşlarında hem `popstate` hem `hashchange` tetiklenir, ikisini birden
 * dinlemek durumu iki kez günceller. Gezinmenin kendisi bağlantı üzerinden
 * yürür (`<a href="#/devlet/osmanli">`); bu sınıf adresi okur ve yalnız
 * programatik geçiş için `go`/`replace` sunar.
 */
class Router {
  route = $state<Route>(parseHash(window.location.hash));

  constructor() {
    // Tarayıcının kendi kaydırma onarımı kapatılır: geri/ileri tuşunda önceki
    // sayfanın kaydırma konumunu geri getirir ve aşağıdaki `scrollTo(0, 0)` ile
    // çakışıp sayfayı rastgele bir yere bırakırdı. Tek kaynak burasıdır.
    history.scrollRestoration = 'manual';

    if (!window.location.hash) {
      // Açılış adresi kanonik olsun: kopyalanan bağlantı '#' değil '#/' taşısın.
      history.replaceState(null, '', '#/');
    }

    window.addEventListener('hashchange', () => {
      this.route = parseHash(window.location.hash);
      // Her rota ayrı bir sayfadır; önceki sayfanın kaydırma konumu taşınmaz.
      window.scrollTo(0, 0);
    });
  }

  /**
   * Yeni geçmiş kaydı açar; geri tuşuyla dönülebilir. Adres zaten bu değerdeyse
   * tarayıcı `hashchange` üretmez ve hiçbir şey olmaz — bağlantının kendi
   * davranışı da budur (aynı sayfaya tıklamak yeni kayıt açmaz).
   */
  go(hash: string) {
    window.location.hash = hash.replace(/^#/, '');
  }

  /**
   * Geçmişe kayıt eklemeden adresi düzeltir. `replaceState` `hashchange`
   * tetiklemediği için rota burada elle güncellenir.
   */
  replace(hash: string) {
    history.replaceState(null, '', hash);
    this.route = parseHash(hash);
  }
}

export const router = new Router();
