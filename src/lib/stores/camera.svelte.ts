import { clamp, xOf, type PositionedState } from '../data/atlas';

export class CameraStore {
  x = $state(0);
  y = $state(0);
  scale = $state(1);

  viewportW = $state(1200);
  viewportH = $state(800);
  worldW = $state(20000);
  worldH = $state(4000);

  minScale = $state(0.04);
  maxScale = $state(2.8);

  isPanning = $state(false);
  isFlying = $state(false);

  // Derived detail visibility
  detail = $derived(clamp((this.scale - 0.5) / 0.5, 0, 1));
  detailActive = $derived(this.scale >= 0.52);
  milestoneActive = $derived(this.scale >= 0.15);

  // Visible years range
  visibleRange = $derived.by(() => {
    const minPx = -this.x;
    const maxPx = minPx + this.viewportW;
    const y1 = Math.round(-280 + (minPx / this.scale - 48) / 8);
    const y2 = Math.round(-280 + (maxPx / this.scale - 48) / 8);
    return {
      startYear: clamp(y1, -280, 1930),
      endYear: clamp(y2, -280, 1930),
    };
  });

  // Zoom level badge text
  zoomLabel = $derived.by(() => {
    if (this.scale < 0.08) return 'en uzak (tüm atlas)';
    if (this.scale < 0.18) return 'çağ / asır görünümü';
    if (this.scale < 0.52) return 'devletler genel bakış';
    if (this.scale < 1.2) return 'hükümdarlar & savaşlar';
    return 'derin detay & hanedan';
  });

  updateDimensions(vw: number, vh: number, ww?: number, wh?: number) {
    this.viewportW = vw;
    this.viewportH = vh;
    if (ww) this.worldW = ww;
    if (wh) this.worldH = wh;
    this.minScale = Math.max(0.03, Math.min(vw / this.worldW, vh / this.worldH) * 0.95);
  }

  zoomAt(cx: number, cy: number, nextScale: number) {
    const s = clamp(nextScale, this.minScale, this.maxScale);
    const ratio = s / this.scale;
    this.x = cx - (cx - this.x) * ratio;
    this.y = cy - (cy - this.y) * ratio;
    this.scale = s;
    this.clampCamera();
  }

  panBy(dx: number, dy: number) {
    this.x += dx;
    this.y += dy;
    this.clampCamera();
  }

  private clampCamera() {
    const margin = 140;
    const minX = this.viewportW - this.worldW * this.scale - margin;
    const maxX = margin;
    const minY = this.viewportH - this.worldH * this.scale - margin;
    const maxY = margin;

    if (this.worldW * this.scale <= this.viewportW) {
      this.x = (this.viewportW - this.worldW * this.scale) / 2;
    } else {
      this.x = clamp(this.x, minX, maxX);
    }

    if (this.worldH * this.scale <= this.viewportH) {
      this.y = (this.viewportH - this.worldH * this.scale) / 2;
    } else {
      this.y = clamp(this.y, minY, maxY);
    }
  }

  flyTo(tx: number, ty: number, targetScale: number, durationMs = 500) {
    const startX = this.x;
    const startY = this.y;
    const startScale = this.scale;
    const startTime = performance.now();
    this.isFlying = true;

    const easeOutCubic = (t: number) => 1 - Math.pow(1 - t, 3);

    const step = (now: number) => {
      const elapsed = now - startTime;
      const progress = clamp(elapsed / durationMs, 0, 1);
      const eased = easeOutCubic(progress);

      this.x = startX + (tx - startX) * eased;
      this.y = startY + (ty - startY) * eased;
      this.scale = startScale + (targetScale - startScale) * eased;
      this.clampCamera();

      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        this.isFlying = false;
      }
    };

    requestAnimationFrame(step);
  }

  fit(animate = true) {
    const margin = 32;
    const s = Math.min(
      (this.viewportW - margin * 2) / this.worldW,
      (this.viewportH - margin * 2) / this.worldH
    );
    const targetScale = clamp(s, this.minScale, this.maxScale);
    const targetX = (this.viewportW - this.worldW * targetScale) / 2;
    const targetY = (this.viewportH - this.worldH * targetScale) / 2;

    if (animate) {
      this.flyTo(targetX, targetY, targetScale, 600);
    } else {
      this.x = targetX;
      this.y = targetY;
      this.scale = targetScale;
      this.clampCamera();
    }
  }

  focusYear(year: number) {
    const wx = xOf(year);
    const targetScale = Math.max(0.7, this.scale);
    const targetX = this.viewportW / 2 - wx * targetScale;
    this.flyTo(targetX, this.y, targetScale, 450);
  }

  focusState(s: PositionedState) {
    const targetScale = Math.max(0.65, this.scale);
    const targetX = this.viewportW / 2 - (s.x + s.w / 2) * targetScale;
    const targetY = this.viewportH / 2 - (s.y + s.h / 2) * targetScale;
    this.flyTo(targetX, targetY, targetScale, 500);
  }
}

export const camera = new CameraStore();
