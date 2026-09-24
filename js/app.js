(() => {
  const PX = 8;
  const MIN_YEAR = -280;
  const MAX_YEAR = 1930;
  const ORIGIN_X = 48;
  const TOP = 36;
  const REGIONS = [
    { id: "giris", name: "Nasıl okunur", color: "#e0c48a" },
    { id: "bozkir", name: "Bozkır ve İç Asya", color: "#d08a45" },
    { id: "turkistan", name: "Türkistan", color: "#3c9a8c" },
    { id: "bati", name: "Hazar, Karadeniz, Avrupa", color: "#6a8cbf" },
    { id: "kuzey", name: "İdil, Kırım, kuzey hanlıkları", color: "#7da36a" },
    { id: "iran", name: "İran, Horasan, Hindistan", color: "#c46b86" },
    { id: "anadolu", name: "Anadolu, Ortadoğu, Mısır", color: "#d4b06a" },
    { id: "diger", name: "Sınırda ve ilişkili yapılar", color: "#9a8f82" }
  ];
  const RESULT = {
    zafer: "Zafer",
    yenilgi: "Yenilgi",
    sonucsuz: "Sonuçsuz",
    belirsiz: "Belirsiz",
    antlasma: "Antlaşma"
  };
  const CERTAINTY = {
    kesin: "Kesin",
    olasi: "Olası",
    muhtemel: "Muhtemel",
    tartismali: "Tartışmalı",
    rivayet: "Rivayet"
  };

  const viewport = document.getElementById("viewport");
  const world = document.getElementById("world");
  const bandsEl = document.getElementById("bands");
  const gridEl = document.getElementById("grid");
  const statesEl = document.getElementById("states");
  const flagsEl = document.getElementById("flags");
  const timebar = document.getElementById("timebar");
  const labelsEl = document.getElementById("labels");
  const suggest = document.getElementById("suggest");
  const q = document.getElementById("q");
  const slider = document.getElementById("zoomSlider");
  const zlabel = document.getElementById("zlabel");
  const yearRead = document.getElementById("yearRead");
  const hint = document.getElementById("hint");
  const boot = document.getElementById("boot");
  const minimap = document.getElementById("minimap");
  const ctx = minimap.getContext("2d");
  const rail = document.getElementById("rail");

  const atlas = window.ATLAS;
  if (!atlas || !Array.isArray(atlas.states)) {
    boot.textContent = "Atlas verisi yüklenemedi.";
    return;
  }

  let scale = 1;
  let x = 0;
  let y = 0;
  let minScale = 0.05;
  let maxScale = 2.6;
  let WORLD_W = 1000;
  let WORLD_H = 1000;
  let anim = 0;
  let labelTimer = 0;
  let lastDetail = -1;
  let minimapBgCanvas = null;
  let sugIndex = 0;
  let sugItems = [];
  const backStack = [];
  const index = [];
  const regionGeom = [];

  const yearLabel = (n) => (n < 0 ? `MÖ ${-n}` : String(n));
  const xOf = (year) => ORIGIN_X + (year - MIN_YEAR) * PX;
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
  }[c]));
  const fold = (s) => s.toLocaleLowerCase("tr")
    .replaceAll("ı", "i").replaceAll("ş", "s").replaceAll("ğ", "g")
    .replaceAll("ü", "u").replaceAll("ö", "o").replaceAll("ç", "c")
    .replaceAll("â", "a").replaceAll("î", "i").replaceAll("û", "u");
  const canon = (s) => fold(s)
    .replaceAll("kokturk", "gokturk")
    .replaceAll("vahdettin", "vahdeddin")
    .replaceAll("vahideddin", "vahdeddin")
    .replaceAll("mehmet", "mehmed")
    .replaceAll("beyazit", "bayezid");
  const safeUrl = (u) => {
    try {
      const url = new URL(u);
      if (url.protocol === "https:" || url.protocol === "http:") return url.href;
    } catch { /* ignore */ }
    return "";
  };

  function colsFor(width, n) {
    if (n <= 1) return 1;
    const inner = Math.max(280, width - 28);
    const cols = Math.floor((inner + 12) / 312);
    return clamp(cols, 1, n);
  }

  function stateWidth(s) {
    const span = Math.max(1, (s.end ?? s.start) - s.start);
    let w = Math.max(88, span * PX);
    const n = (s.rulers || []).length;
    if ((s.essay || []).length) w = Math.max(w, 760);
    if (n) w = Math.max(w, 332);
    return w;
  }

  function renderSources(list) {
    const items = (list || []).map((src) => {
      const href = safeUrl(src.url);
      return href ? `<a href="${esc(href)}" target="_blank" rel="noopener">${esc(src.title || href)}</a>` : "";
    }).filter(Boolean);
    if (!items.length) return "";
    return `<div class="sec srcs"><h4>Kaynak</h4><p>${items.join(" · ")}</p></div>`;
  }

  function peopleList(title, rows, line) {
    if (!rows || !rows.length) {
      return `<div class="sec"><h4>${title}</h4><p>Adı güvenilir kayda geçmiş kişi yok. Bu, hiç kimse olmadığı anlamına gelmez.</p></div>`;
    }
    return `<div class="sec"><h4>${title}</h4><ul>${rows.map(line).join("")}</ul></div>`;
  }

  function renderRuler(r, stateName) {
    const reign = r.reign || [null, null];
    const a = reign[0] == null ? "?" : yearLabel(reign[0]);
    const b = reign[1] == null ? "?" : yearLabel(reign[1]);
    const birth = r.birth == null ? (r.birthNote || "doğum yılı kayda geçmemiş") : `${yearLabel(r.birth)}${r.birthNote ? ` (${r.birthNote})` : ""}`;
    const death = r.death == null ? (r.deathNote || "ölüm yılı belirsiz") : `${yearLabel(r.death)}${r.deathNote ? ` (${r.deathNote})` : ""}`;
    const wars = (r.wars || []).map((w) => {
      const res = RESULT[w.result] ? w.result : "belirsiz";
      return `<div class="war"><div><b>${esc(w.name)}</b> <span>${esc(w.when || "")}</span><br><span>${esc(w.foe || "")}</span>${w.note ? `<br><span>${esc(w.note)}</span>` : ""}</div><div class="res ${res}">${RESULT[res]}</div></div>`;
    }).join("");
    const traits = (r.traits || []).length
      ? `<div class="sec"><h4>Bilinen özellikleri</h4><div class="chips">${r.traits.map((t) => `<span>${esc(t)}</span>`).join("")}</div></div>`
      : "";
    const legends = (r.legends || []).length
      ? `<div class="sec legend-box"><h4>Rivayet</h4><ul>${r.legends.map((t) => `<li>${esc(t)}</li>`).join("")}</ul></div>`
      : "";
    const extra = [
      r.contribution ? `<div class="sec"><h4>Ülkesine katkısı</h4><p>${esc(r.contribution)}</p></div>` : "",
      r.harm ? `<div class="sec"><h4>Bedel ve zarar</h4><p>${esc(r.harm)}</p></div>` : "",
      !r.contribution && !r.harm ? `<div class="sec"><h4>Katkı ve bedel</h4><p>Kaynaklar bu başlığı ayrıca ayırmıyor.</p></div>` : ""
    ].join("");
    const claim = r.claim ? " · talip, klasik padişah sayımına girmez" : "";
    return `<article class="ruler" data-id="${esc(r.id)}">
      <div class="ghost">${esc(reign[0] == null ? "" : yearLabel(reign[0]))}</div>
      <div class="kicker">${esc(stateName)}${claim}</div>
      <h3>${esc(r.name)}</h3>
      <p class="dates">${esc(r.title || "")} · ${a} – ${b}</p>
      ${r.reignNote ? `<p class="life">${esc(r.reignNote)}</p>` : ""}
      <p class="life">Doğum: ${esc(birth)} · Ölüm: ${esc(death)}</p>
      <p class="sum">${esc(r.summary || "")}</p>
      ${peopleList("Eşler", r.wives, (p) => `<li>${esc(p.name)}${p.note ? ` — ${esc(p.note)}` : ""}${p.certainty && p.certainty !== "kesin" ? `<span class="cert">${esc(CERTAINTY[p.certainty] || p.certainty)}</span>` : ""}</li>`)}
      ${peopleList("Çocuklar", r.children, (p) => `<li>${esc(p.name)}${p.mother ? ` · anne: ${esc(p.mother)}` : ""}${p.note ? ` — ${esc(p.note)}` : ""}${p.certainty && p.certainty !== "kesin" ? `<span class="cert">${esc(CERTAINTY[p.certainty] || p.certainty)}</span>` : ""}</li>`)}
      <div class="sec"><h4>Savaşlar</h4>${wars || "<p>Adı konmuş büyük bir sefer bu kartta yok.</p>"}</div>
      ${extra}${traits}${legends}${renderSources(r.sources)}
    </article>`;
  }

  function renderState(s) {
    const accent = (REGIONS.find((r) => r.id === s.region) || {}).color || "#e0c48a";
    const w = stateWidth(s);
    const cols = colsFor(w, (s.rulers || []).length || 1);
    const when = `${yearLabel(s.start)} – ${yearLabel(s.end)}`;
    const flag = s.confidence === "tartismali"
      ? `<div class="flag">Tartışmalı${s.confidenceNote ? `: ${esc(s.confidenceNote)}` : ""}</div>`
      : (s.confidence === "rivayet" ? `<div class="flag">Rivayet ağırlıklı</div>` : "");
    const essay = (s.essay || []).map((p) => `<p class="state-sum">${esc(p)}</p>`).join("");
    const rulers = (s.rulers || []).map((r) => renderRuler(r, s.short || s.name)).join("");
    const el = document.createElement("section");
    el.className = `state${s.confidence === "tartismali" ? " tartismali" : ""}`;
    el.id = `state-${s.id}`;
    el.dataset.id = s.id;
    el.style.width = `${w}px`;
    el.style.setProperty("--accent", accent);
    el.innerHTML = `<header class="state-head">
        <div class="state-kicker">${esc((REGIONS.find((r) => r.id === s.region) || {}).name || "")}</div>
        <h2>${esc(s.name)}</h2>
        <p class="state-when">${when}</p>
        <p class="state-meta">${[s.capital ? `Merkez: ${s.capital}` : "", s.religion ? `İnanç: ${s.religion}` : ""].filter(Boolean).join(" · ")}</p>
        ${s.startNote || s.endNote ? `<p class="life">${esc([s.startNote, s.endNote].filter(Boolean).join(" "))}</p>` : ""}
        <p class="state-sum">${esc(s.summary || "")}</p>
        ${s.legacy ? `<p class="state-sum">${esc(s.legacy)}</p>` : ""}
        ${flag}
        ${renderSources(s.sources)}
      </header>
      ${essay ? `<div class="essay">${essay}</div>` : ""}
      ${rulers ? `<div class="rulers" style="grid-template-columns:repeat(${cols}, minmax(0,1fr));max-width:${cols * 372}px">${rulers}</div>` : ""}`;
    statesEl.appendChild(el);
    s._el = el;
    s._w = w;
    (s.rulers || []).forEach((r) => {
      index.push({
        kind: r.claim ? "Talip" : "Hükümdar",
        title: r.name,
        sub: s.name,
        key: canon(`${r.name} ${(r.aliases || []).join(" ")} ${s.name} ${(r.wives || []).map((w) => w.name).join(" ")} ${(r.children || []).map((c) => c.name).join(" ")} ${(r.wars || []).map((w) => w.name).join(" ")}`),
        state: s,
        rulerId: r.id
      });
    });
    index.push({
      kind: "Devlet",
      title: s.name,
      sub: when,
      key: canon(`${s.name} ${s.short || ""} ${(s.aliases || []).join(" ")} ${s.summary || ""}`),
      state: s
    });
  }

  function pack(keepView) {
    const cx = keepView ? (viewport.clientWidth / 2 - x) / scale : null;
    const cy = keepView ? (viewport.clientHeight / 2 - y) / scale : null;
    let cursorY = TOP;
    regionGeom.length = 0;
    bandsEl.innerHTML = "";
    for (const region of REGIONS) {
      const list = atlas.states.filter((s) => s.region === region.id);
      if (!list.length) continue;
      const items = list.map((s) => ({
        s,
        x: xOf(s.start),
        w: s._w,
        h: Math.max(140, s._el.offsetHeight)
      })).sort((a, b) => a.x - b.x || a.w - b.w);
      const laneEnds = [];
      for (const it of items) {
        let lane = laneEnds.findIndex((end) => end + 18 <= it.x);
        if (lane < 0) {
          lane = laneEnds.length;
          laneEnds.push(it.x + it.w);
        } else laneEnds[lane] = it.x + it.w;
        it.lane = lane;
      }
      const laneH = [];
      for (const it of items) laneH[it.lane] = Math.max(laneH[it.lane] || 0, it.h);
      const laneY = [];
      let acc = 28;
      for (let i = 0; i < laneH.length; i++) {
        laneY[i] = acc;
        acc += laneH[i] + 16;
      }
      const regionH = acc + 12;
      for (const it of items) {
        const top = cursorY + laneY[it.lane];
        it.s._el.style.left = `${it.x}px`;
        it.s._el.style.top = `${top}px`;
        it.s._x = it.x;
        it.s._y = top;
        it.s._h = it.h;
      }
      const band = document.createElement("div");
      band.className = "band";
      band.style.left = "24px";
      band.style.top = `${cursorY}px`;
      band.style.width = `${xOf(MAX_YEAR) - 24}px`;
      band.style.height = `${regionH}px`;
      band.style.outline = `1px solid ${region.color}22`;
      band.innerHTML = `<div class="band-name">${esc(region.name)}</div>`;
      bandsEl.appendChild(band);
      regionGeom.push({ id: region.id, name: region.name, color: region.color, y: cursorY, h: regionH });
      cursorY += regionH + 20;
    }
    let maxX = xOf(MAX_YEAR);
    for (const s of atlas.states) maxX = Math.max(maxX, s._x + s._w);
    WORLD_W = maxX + 80;
    WORLD_H = cursorY + 40;
    world.style.width = `${WORLD_W}px`;
    world.style.height = `${WORLD_H}px`;
    for (const band of bandsEl.children) band.style.width = `${WORLD_W - 48}px`;
    drawGrid();
    placeFlags();
    buildRail();
    resizeLimits();
    renderMinimapBg();
    if (cx == null) fit(false, false);
    else {
      x = viewport.clientWidth / 2 - cx * scale;
      y = viewport.clientHeight / 2 - cy * scale;
      apply();
    }
  }

  function drawGrid() {
    gridEl.innerHTML = "";
    const startYear = Math.ceil(MIN_YEAR / 100) * 100;
    const endYear = Math.floor(MAX_YEAR / 100) * 100;
    for (let year = startYear; year <= endYear; year += 100) {
      const line = document.createElement("div");
      line.className = "gridline";
      line.style.left = `${xOf(year)}px`;
      line.style.height = `${WORLD_H}px`;
      gridEl.appendChild(line);
    }
  }

  function placeFlags() {
    flagsEl.innerHTML = "";
    for (const m of atlas.milestones || []) {
      const b = document.createElement("button");
      b.className = "milestone";
      b.style.left = `${xOf(m.year)}px`;
      b.style.top = "6px";
      b.innerHTML = `<i></i>${esc(m.label)}`;
      b.addEventListener("click", (e) => {
        e.stopPropagation();
        focusYear(m.year);
      });
      flagsEl.appendChild(b);
    }
  }

  function buildRail() {
    rail.innerHTML = "";
    for (const g of regionGeom) {
      const b = document.createElement("button");
      b.type = "button";
      b.textContent = g.name;
      b.style.borderLeft = `3px solid ${g.color}`;
      b.dataset.region = g.id;
      b.addEventListener("click", () => {
        pushBack();
        const ns = clamp(viewport.clientWidth / (900 * 1.1), minScale, maxScale);
        animateTo(40 - ORIGIN_X * ns, viewport.clientHeight * 0.3 - (g.y + 40) * ns, ns);
      });
      rail.appendChild(b);
    }
  }

  const indexPanel = document.getElementById("indexPanel");
  const indexBtn = document.getElementById("indexBtn");
  const ixBody = document.getElementById("ixBody");

  function buildIndex() {
    const parts = [];
    for (const region of REGIONS) {
      const list = atlas.states.filter((s) => s.region === region.id);
      if (!list.length) continue;
      parts.push(`<h3><i style="background:${region.color}"></i>${esc(region.name)}</h3>`);
      for (const s of list) {
        const n = (s.rulers || []).length;
        parts.push(`<div class="ix-state"><button type="button" class="ix-s" data-state="${esc(s.id)}">${esc(s.name)}<span>${yearLabel(s.start)} – ${yearLabel(s.end)}${n ? ` · ${n} hükümdar` : ""}</span></button>`);
        if (n) {
          parts.push(`<div class="ix-rulers">${s.rulers.map((r) => `<button type="button" class="ix-r" data-state="${esc(s.id)}" data-ruler="${esc(r.id)}">${esc(r.name)}${r.claim ? " (talip)" : ""}</button>`).join("")}</div>`);
        }
        parts.push("</div>");
      }
    }
    ixBody.innerHTML = parts.join("");
  }

  function toggleIndex(open) {
    const next = typeof open === "boolean" ? open : indexPanel.hidden;
    if (next) {
      buildIndex();
      indexPanel.hidden = false;
      indexBtn.setAttribute("aria-expanded", "true");
      const closeBtn = document.getElementById("ixClose");
      if (closeBtn) closeBtn.focus();
    } else {
      indexPanel.hidden = true;
      indexBtn.setAttribute("aria-expanded", "false");
      indexBtn.focus();
    }
  }

  indexBtn.addEventListener("click", () => toggleIndex());
  document.getElementById("ixClose").addEventListener("click", () => toggleIndex(false));
  ixBody.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-state]");
    if (!btn) return;
    const st = atlas.states.find((s) => s.id === btn.dataset.state);
    if (!st) return;
    if (btn.dataset.ruler) flyToRuler(st, btn.dataset.ruler, true);
    else flyToState(st, true);
    toggleIndex(false);
  });

  function resizeLimits() {
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;
    minScale = Math.min(vw / WORLD_W, vh / WORLD_H) * 0.96;
    maxScale = 2.6;
    if (minScale > maxScale) minScale = maxScale;
  }

  function apply() {
    scale = clamp(scale, minScale, maxScale);
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;
    const ww = WORLD_W * scale;
    const wh = WORLD_H * scale;
    if (ww <= vw) x = (vw - ww) / 2;
    else x = clamp(x, vw - ww - 8, 8);
    if (wh <= vh) y = (vh - wh) / 2;
    else y = clamp(y, vh - wh - 8, 8);
    world.style.transform = `translate3d(${x}px, ${y}px, 0) scale(${scale})`;
    const detail = clamp((scale - 0.42) / 0.28, 0, 1);
    const detailRound = Math.round(detail * 50) / 50;
    if (Math.abs(detailRound - lastDetail) >= 0.02 || (detailRound === 0 && lastDetail !== 0) || (detailRound === 1 && lastDetail !== 1)) {
      lastDetail = detailRound;
      world.style.setProperty("--detail", detailRound.toFixed(2));
    }
    viewport.classList.toggle("detail-on", scale >= 0.62);
    const t = (Math.log(scale) - Math.log(minScale)) / (Math.log(maxScale) - Math.log(minScale) || 1);
    slider.value = String(Math.round(clamp(t, 0, 1) * 1000));
    const pct = Math.round(clamp(t, 0, 1) * 100);
    zlabel.textContent = pct <= 0 ? "en uzak" : pct >= 100 ? "en yakın" : `${pct}%`;
    const y1 = MIN_YEAR + ((-x) / scale - ORIGIN_X) / PX;
    const y2 = MIN_YEAR + ((-x + vw) / scale - ORIGIN_X) / PX;
    yearRead.textContent = `${yearLabel(Math.round(clamp(y1, MIN_YEAR, MAX_YEAR)))} – ${yearLabel(Math.round(clamp(y2, MIN_YEAR, MAX_YEAR)))}`;
    viewport.classList.toggle("far", scale < 0.22);
    viewport.classList.toggle("milestone-on", scale >= 0.4);
    drawTimebar();
    drawMinimap();
    clearTimeout(labelTimer);
    labelTimer = setTimeout(updateLabels, scale >= 0.7 ? 0 : 40);
  }

  function drawTimebar() {
    const frag = document.createDocumentFragment();
    const vw = viewport.clientWidth;
    let lastTick = -9999;
    const step = scale < 0.12 ? 200 : 100;
    const startYear = Math.ceil(MIN_YEAR / step) * step;
    const endYear = Math.floor(MAX_YEAR / step) * step;
    for (let year = startYear; year <= endYear; year += step) {
      const sx = x + xOf(year) * scale;
      if (sx < -20 || sx > vw + 20) continue;
      if (sx - lastTick < 64) continue;
      lastTick = sx;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "tick";
      b.dataset.year = String(year);
      b.style.left = `${sx}px`;
      b.textContent = yearLabel(year);
      frag.appendChild(b);
    }
    timebar.replaceChildren(frag);
  }

  function updateLabels() {
    if (scale >= 0.55) {
      labelsEl.innerHTML = "";
      return;
    }
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;
    const placed = [];
    const items = atlas.states.map((s) => {
      const sx = x + s._x * scale;
      const sy = y + s._y * scale;
      const sw = s._w * scale;
      const sh = s._h * scale;
      return { s, sx, sy, sw, sh, area: sw * sh };
    }).filter((it) => it.sw > 36 && it.sh > 14 && it.sx < vw && it.sy < vh && it.sx + it.sw > 0 && it.sy + it.sh > 0)
      .sort((a, b) => b.area - a.area);
    const nodes = [];
    for (const it of items) {
      const cx = clamp(it.sx + it.sw / 2, 80, vw - 80);
      const cy = clamp(it.sy + Math.min(it.sh / 2, 28), 8, vh - 8);
      const box = { l: cx - 70, t: cy - 10, r: cx + 70, b: cy + 10 };
      if (placed.some((p) => !(box.r < p.l || box.l > p.r || box.b < p.t || box.t > p.b))) continue;
      placed.push(box);
      nodes.push(`<div class="slabel" style="left:${cx}px;top:${cy}px">${esc(it.s.short || it.s.name)}</div>`);
      if (nodes.length > 28) break;
    }
    labelsEl.innerHTML = nodes.join("");
  }

  function renderMinimapBg() {
    if (!minimap.clientWidth || !minimap.clientHeight) return;
    const cw = minimap.clientWidth;
    const ch = minimap.clientHeight;
    minimap.width = cw * devicePixelRatio;
    minimap.height = ch * devicePixelRatio;
    minimapBgCanvas = document.createElement("canvas");
    minimapBgCanvas.width = minimap.width;
    minimapBgCanvas.height = minimap.height;
    const bctx = minimapBgCanvas.getContext("2d");
    bctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    bctx.clearRect(0, 0, cw, ch);
    for (const s of atlas.states) {
      const region = REGIONS.find((r) => r.id === s.region);
      bctx.fillStyle = region ? region.color : "#e0c48a";
      bctx.globalAlpha = 0.85;
      bctx.fillRect(s._x / WORLD_W * cw, s._y / WORLD_H * ch, Math.max(2, s._w / WORLD_W * cw), Math.max(2, s._h / WORLD_H * ch));
    }
  }

  function drawMinimap() {
    if (!minimap.clientWidth) return;
    if (!minimapBgCanvas) renderMinimapBg();
    if (!minimapBgCanvas) return;
    const cw = minimap.clientWidth;
    const ch = minimap.clientHeight;
    ctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
    ctx.clearRect(0, 0, cw, ch);
    ctx.drawImage(minimapBgCanvas, 0, 0, cw, ch);
    const vx = -x / scale / WORLD_W * cw;
    const vy = -y / scale / WORLD_H * ch;
    const vw = viewport.clientWidth / scale / WORLD_W * cw;
    const vh = viewport.clientHeight / scale / WORLD_H * ch;
    ctx.strokeStyle = "#f3eadc";
    ctx.lineWidth = 1;
    ctx.strokeRect(vx, vy, vw, vh);
  }

  function zoomAt(sx, sy, next) {
    next = clamp(next, minScale, maxScale);
    const wx = (sx - x) / scale;
    const wy = (sy - y) / scale;
    scale = next;
    x = sx - wx * scale;
    y = sy - wy * scale;
    apply();
  }

  function animateTo(nx, ny, ns) {
    const token = ++anim;
    const sx = x;
    const sy = y;
    const ss = scale;
    const t0 = performance.now();
    const dur = matchMedia("(prefers-reduced-motion: reduce)").matches ? 1 : 520;
    const frame = (t) => {
      if (token !== anim) return;
      const k = Math.min(1, (t - t0) / dur);
      const e = 1 - (1 - k) ** 3;
      x = sx + (nx - sx) * e;
      y = sy + (ny - sy) * e;
      scale = ss + (ns - ss) * e;
      apply();
      if (k < 1) requestAnimationFrame(frame);
    };
    requestAnimationFrame(frame);
    // Sekme arka plandayken çizim kareleri durur; hedefi yine de tuttur.
    setTimeout(() => {
      if (token !== anim) return;
      if (Math.abs(scale - ns) < 1e-6 && Math.abs(x - nx) < 0.6 && Math.abs(y - ny) < 0.6) return;
      x = nx;
      y = ny;
      scale = ns;
      apply();
    }, dur + 90);
  }

  function worldRect(el) {
    const r = el.getBoundingClientRect();
    const vr = viewport.getBoundingClientRect();
    return {
      wx: (r.left - vr.left - x) / scale,
      wy: (r.top - vr.top - y) / scale,
      ww: r.width / scale,
      wh: r.height / scale
    };
  }

  function flyToRect(rect, push = true, topAlign = false, minTargetScale = minScale) {
    if (!rect) return;
    if (push) pushBack();
    const vw = viewport.clientWidth;
    const vh = viewport.clientHeight;
    let ns = topAlign
      ? (vw * 0.78) / Math.max(280, rect.ww)
      : Math.min(vw / (rect.ww * 1.12), vh / (rect.wh * 1.12));
    ns = clamp(ns, Math.max(minScale, minTargetScale), maxScale);
    const nx = vw / 2 - (rect.wx + rect.ww / 2) * ns;
    const ny = topAlign ? (28 - rect.wy * ns) : (vh / 2 - (rect.wy + rect.wh / 2) * ns);
    animateTo(nx, ny, ns);
  }

  function flyToState(s, push = true) {
    flyToRect({ wx: s._x, wy: s._y, ww: s._w, wh: Math.min(s._h, 920) }, push);
    setHash(s.id, "");
  }

  function flyToRuler(state, rulerId, push = true) {
    const el = state._el.querySelector(`.ruler[data-id="${CSS.escape(rulerId)}"]`);
    if (!el) return flyToState(state, push);
    flyToRect(worldRect(el), push, true, 0.9);
    setHash(state.id, rulerId);
  }

  function setHash(sid, rid) {
    const next = rid ? `#${sid}/${rid}` : `#${sid}`;
    if (location.hash !== next) history.replaceState(null, "", next);
  }

  function focusYear(year) {
    pushBack();
    const vw = viewport.clientWidth;
    const ns = clamp(vw / (160 * PX), minScale, maxScale);
    const nx = vw / 2 - xOf(year) * ns;
    animateTo(nx, y, ns);
  }

  function fit(push = true, animate = true) {
    if (push) pushBack();
    resizeLimits();
    const nx = (viewport.clientWidth - WORLD_W * minScale) / 2;
    const ny = (viewport.clientHeight - WORLD_H * minScale) / 2;
    if (!animate) {
      x = nx;
      y = ny;
      scale = minScale;
      apply();
      return;
    }
    animateTo(nx, ny, minScale);
  }

  function pushBack() {
    backStack.push({ x, y, scale });
    if (backStack.length > 16) backStack.shift();
  }

  function popBack() {
    const prev = backStack.pop();
    if (!prev) return fit(false);
    animateTo(prev.x, prev.y, prev.scale);
  }

  function hideHint() {
    hint.style.display = "none";
    try { sessionStorage.setItem("atlas-hint", "1"); } catch { /* ignore */ }
  }

  let pointers = new Map();
  let drag = null;
  let pinch = null;
  let clickTimer = 0;

  viewport.addEventListener("pointerdown", (e) => {
    if (e.target.closest("a, button, input")) return;
    anim++;
    viewport.setPointerCapture(e.pointerId);
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size === 2) {
      const pts = [...pointers.values()];
      pinch = {
        d: Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y),
        scale
      };
      drag = null;
      return;
    }
    drag = { x: e.clientX, y: e.clientY, ox: x, oy: y, moved: false, target: e.target };
    viewport.classList.add("dragging");
  });

  viewport.addEventListener("pointermove", (e) => {
    if (!pointers.has(e.pointerId)) return;
    pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
    if (pointers.size >= 2 && pinch) {
      const pts = [...pointers.values()];
      const d = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
      const rect = viewport.getBoundingClientRect();
      const mx = (pts[0].x + pts[1].x) / 2 - rect.left;
      const my = (pts[0].y + pts[1].y) / 2 - rect.top;
      zoomAt(mx, my, pinch.scale * (d / pinch.d));
      hideHint();
      return;
    }
    if (!drag) return;
    const dx = e.clientX - drag.x;
    const dy = e.clientY - drag.y;
    if (Math.hypot(dx, dy) > 4) drag.moved = true;
    x = drag.ox + dx;
    y = drag.oy + dy;
    apply();
  });

  function endPointer(e) {
    const was = drag;
    pointers.delete(e.pointerId);
    if (pointers.size < 2) pinch = null;
    drag = null;
    viewport.classList.remove("dragging");
    if (!was || was.moved || e.type === "pointercancel") return;
    const ruler = was.target.closest?.(".ruler");
    const stateEl = was.target.closest?.(".state");
    clearTimeout(clickTimer);
    clickTimer = setTimeout(() => {
      if (scale >= 0.62 && ruler) {
        flyToRect(worldRect(ruler), true);
        const st = atlas.states.find((s) => s._el === stateEl);
        if (st) setHash(st.id, ruler.dataset.id);
      } else if (stateEl) {
        const st = atlas.states.find((s) => s._el === stateEl);
        if (st) flyToState(st, true);
      }
    }, 260);
  }

  viewport.addEventListener("pointerup", endPointer);
  viewport.addEventListener("pointercancel", endPointer);

  viewport.addEventListener("dblclick", (e) => {
    if (e.target.closest("a, button")) return;
    clearTimeout(clickTimer);
    anim++;
    zoomAt(e.clientX - viewport.getBoundingClientRect().left, e.clientY - viewport.getBoundingClientRect().top, scale * 1.7);
  });

  window.addEventListener("gesturestart", (e) => e.preventDefault(), { passive: false });
  window.addEventListener("gesturechange", (e) => e.preventDefault(), { passive: false });

  window.addEventListener("wheel", (e) => {
    e.preventDefault();
    if (e.target.closest("input, textarea, #suggest")) return;
    anim++;
    const dy = e.deltaMode === 1 ? e.deltaY * 16 : e.deltaMode === 2 ? e.deltaY * viewport.clientHeight : e.deltaY;
    const capped = clamp(dy, -90, 90);
    const strength = e.ctrlKey ? 0.01 : 0.0018;
    const rect = viewport.getBoundingClientRect();
    const sx = clamp(e.clientX - rect.left, 0, rect.width);
    const sy = clamp(e.clientY - rect.top, 0, rect.height);
    zoomAt(sx, sy, scale * Math.exp(-capped * strength));
    hideHint();
  }, { passive: false });

  window.addEventListener("keydown", (e) => {
    const typing = document.activeElement === q;
    if (e.key === "Escape") {
      if (!indexPanel.hidden) {
        toggleIndex(false);
        return;
      }
      if (suggest.classList.contains("open")) {
        suggest.classList.remove("open");
        q.removeAttribute("aria-activedescendant");
        return;
      }
      if (!typing) popBack();
      return;
    }
    if (typing) {
      if (e.key === "ArrowDown" || e.key === "ArrowUp") {
        e.preventDefault();
        if (!sugItems.length) return;
        sugIndex = (sugIndex + (e.key === "ArrowDown" ? 1 : -1) + sugItems.length) % sugItems.length;
        paintSuggest();
      } else if (e.key === "Enter") {
        e.preventDefault();
        const item = sugItems[sugIndex];
        if (item) openItem(item);
      }
      return;
    }
    const step = e.shiftKey ? 180 : 90;
    if (["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", " ", "+", "=", "-", "_", "0"].includes(e.key)) e.preventDefault();
    if (e.key === "ArrowLeft") { anim++; x += step; apply(); }
    if (e.key === "ArrowRight") { anim++; x -= step; apply(); }
    if (e.key === "ArrowUp") { anim++; y += step; apply(); }
    if (e.key === "ArrowDown") { anim++; y -= step; apply(); }
    if (e.key === "+" || e.key === "=") zoomAt(viewport.clientWidth / 2, viewport.clientHeight / 2, scale * 1.2);
    if (e.key === "-" || e.key === "_") zoomAt(viewport.clientWidth / 2, viewport.clientHeight / 2, scale / 1.2);
    if (e.key === "0") fit(true);
  });

  window.addEventListener("touchmove", (e) => {
    if (e.target.closest("#viewport, #timebar, #minimap, #hud")) e.preventDefault();
  }, { passive: false });

  slider.addEventListener("input", () => {
    anim++;
    const t = Number(slider.value) / 1000;
    const next = Math.exp(Math.log(minScale) + t * (Math.log(maxScale) - Math.log(minScale)));
    zoomAt(viewport.clientWidth / 2, viewport.clientHeight / 2, next);
  });

  document.getElementById("zoomIn").addEventListener("click", () => zoomAt(viewport.clientWidth / 2, viewport.clientHeight / 2, scale * 1.25));
  document.getElementById("zoomOut").addEventListener("click", () => zoomAt(viewport.clientWidth / 2, viewport.clientHeight / 2, scale / 1.25));
  document.getElementById("fit").addEventListener("click", () => fit(true));

  timebar.addEventListener("click", (e) => {
    const b = e.target.closest("button.tick");
    if (b && b.dataset.year) focusYear(Number(b.dataset.year));
  });

  function paintSuggest() {
    suggest.innerHTML = sugItems.map((item, i) => `<button type="button" role="option" id="sug-item-${i}" aria-selected="${i === sugIndex}" class="sug${i === sugIndex ? " on" : ""}" data-i="${i}"><span class="kind">${esc(item.kind)}</span><span><b>${esc(item.title)}</b><span>${esc(item.sub)}</span></span></button>`).join("");
    const open = sugItems.length > 0;
    suggest.classList.toggle("open", open);
    if (open && sugItems[sugIndex]) {
      q.setAttribute("aria-activedescendant", `sug-item-${sugIndex}`);
    } else {
      q.removeAttribute("aria-activedescendant");
    }
  }

  function search(text) {
    const f = canon(text.trim());
    if (f.length < 2) {
      sugItems = [];
      paintSuggest();
      return;
    }
    sugItems = index.filter((item) => item.key.includes(f)).slice(0, 6);
    sugIndex = 0;
    paintSuggest();
  }

  function openItem(item) {
    suggest.classList.remove("open");
    q.removeAttribute("aria-activedescendant");
    q.value = item.title;
    if (item.rulerId) flyToRuler(item.state, item.rulerId, true);
    else flyToState(item.state, true);
  }

  q.addEventListener("input", () => search(q.value));
  suggest.addEventListener("click", (e) => {
    const btn = e.target.closest(".sug");
    if (!btn) return;
    openItem(sugItems[Number(btn.dataset.i)]);
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest("#search")) {
      suggest.classList.remove("open");
      q.removeAttribute("aria-activedescendant");
    }
  });

  minimap.addEventListener("pointerdown", (e) => {
    const rect = minimap.getBoundingClientRect();
    const wx = (e.clientX - rect.left) / rect.width * WORLD_W;
    const wy = (e.clientY - rect.top) / rect.height * WORLD_H;
    anim++;
    x = viewport.clientWidth / 2 - wx * scale;
    y = viewport.clientHeight / 2 - wy * scale;
    apply();
  });

  let lastHudH = -1;
  function measureHud() {
    const hud = document.getElementById("hud");
    const h = hud.offsetHeight;
    if (h !== lastHudH) {
      lastHudH = h;
      document.documentElement.style.setProperty("--hud-h", `${h}px`);
    }
  }

  window.addEventListener("resize", () => {
    const wasFit = Math.abs(scale - minScale) < 0.004;
    const cx = (viewport.clientWidth / 2 - x) / scale;
    const cy = (viewport.clientHeight / 2 - y) / scale;
    measureHud();
    resizeLimits();
    renderMinimapBg();
    if (wasFit) fit(false, false);
    else {
      scale = clamp(scale, minScale, maxScale);
      x = viewport.clientWidth / 2 - cx * scale;
      y = viewport.clientHeight / 2 - cy * scale;
      apply();
    }
  });

  try { if (sessionStorage.getItem("atlas-hint")) hint.style.display = "none"; } catch { /* ignore */ }

  for (const s of atlas.states) {
    if (!REGIONS.some((r) => r.id === s.region)) s.region = "diger";
    if (typeof s.start !== "number") s.start = 0;
    if (typeof s.end !== "number" || s.end < s.start) s.end = s.start + 1;
    s.rulers = s.rulers || [];
    renderState(s);
  }
  measureHud();
  const start = () => {
    pack(false);
    boot.remove();
    const hash = decodeURIComponent(location.hash.replace(/^#/, ""));
    if (hash) {
      const [sid, rid] = hash.split("/");
      const st = atlas.states.find((s) => s.id === sid);
      if (st && rid) flyToRuler(st, rid, false);
      else if (st) flyToState(st, false);
    }
  };
  if (document.fonts && document.fonts.ready) {
    Promise.race([document.fonts.ready, new Promise((r) => setTimeout(r, 1600))]).then(start);
    document.fonts.ready.then(() => { if (!boot.isConnected) pack(true); });
  } else start();

  window.__atlas = {
    get scale() { return scale; },
    get min() { return minScale; },
    get max() { return maxScale; },
    get x() { return x; },
    get y() { return y; },
    ready: () => !document.getElementById("boot"),
    flyToId(id) {
      const item = index.find((it) => canon(it.title) === canon(id) || it.state.id === id || it.rulerId === id || it.key.includes(canon(id)));
      if (item) openItem(item);
    }
  };
})();
