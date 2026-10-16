export type ModalEntry =
  | { kind: 'state'; id: string }
  | { kind: 'context'; id: string }
  | { kind: 'ruler'; stateId: string; rulerId: string }
  | { kind: 'war'; stateId: string; rulerId: string; index: number };

/**
 * Üst üste açılan modallar. Her açılış tarayıcı geçmişine bir adım ekler;
 * böylece telefonda "geri" hareketi ya da tarayıcının geri tuşu yalnızca en
 * üstteki modalı kapatır, sayfadan çıkmaz.
 */
class ModalStack {
  items = $state<ModalEntry[]>([]);

  constructor() {
    if (typeof window === 'undefined') return;
    history.replaceState({ ...(history.state ?? {}), depth: 0 }, '');
    window.addEventListener('popstate', (e) => {
      const depth = typeof e.state?.depth === 'number' ? e.state.depth : 0;
      if (depth < this.items.length) this.items = this.items.slice(0, depth);
      else if (depth > this.items.length) history.go(this.items.length - depth);
    });
  }

  open(entry: ModalEntry) {
    this.items = [...this.items, entry];
    history.pushState({ depth: this.items.length }, '');
  }

  /** En üstteki modalı kapatır. */
  back() {
    if (this.items.length) history.back();
  }

  /** Belirtilen düzeye kadar (o düzey açık kalarak) kapatır. */
  closeTo(depth: number) {
    const steps = this.items.length - depth;
    if (steps > 0) history.go(-steps);
  }

  closeAll() {
    this.closeTo(0);
  }
}

export const modals = new ModalStack();
