import type { State, Ruler, Region } from '../../schemas/atlas.schema';

export class UIStore {
  selectedState = $state<State | null>(null);
  selectedRuler = $state<Ruler | null>(null);
  selectedRulerState = $state<State | null>(null);

  isIndexOpen = $state(false);
  isDetailDrawerOpen = $state(false);

  searchQuery = $state('');
  filterRegion = $state<Region | 'all'>('all');

  openRulerDetail(ruler: Ruler, state: State) {
    this.selectedRuler = ruler;
    this.selectedRulerState = state;
    this.isDetailDrawerOpen = true;
  }

  openStateDetail(state: State) {
    this.selectedState = state;
    this.selectedRuler = null;
    this.selectedRulerState = null;
    this.isDetailDrawerOpen = true;
  }

  closeDetail() {
    this.isDetailDrawerOpen = false;
  }

  toggleIndex(open?: boolean) {
    this.isIndexOpen = typeof open === 'boolean' ? open : !this.isIndexOpen;
  }
}

export const ui = new UIStore();
