#!/usr/bin/env python3
"""data/raw/*.json -> data/atlas.js derleyici."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "atlas.js"

MILESTONES = [
    {"year": -209, "label": "Mete"},
    {"year": 552, "label": "Göktürk"},
    {"year": 630, "label": "Batı Göktürk"},
    {"year": 744, "label": "Uygur"},
    {"year": 840, "label": "Karahanlı"},
    {"year": 963, "label": "Gazneli"},
    {"year": 1040, "label": "Selçuklu"},
    {"year": 1071, "label": "Malazgirt"},
    {"year": 1096, "label": "Haçlı"},
    {"year": 1206, "label": "Moğol"},
    {"year": 1243, "label": "Kösedağ"},
    {"year": 1299, "label": "Osmanlı"},
    {"year": 1402, "label": "Ankara"},
    {"year": 1453, "label": "İstanbul"},
    {"year": 1514, "label": "Çaldıran"},
    {"year": 1517, "label": "Mısır"},
    {"year": 1526, "label": "Babür"},
    {"year": 1571, "label": "İnebahtı"},
    {"year": 1683, "label": "Viyana"},
    {"year": 1699, "label": "Karlofça"},
    {"year": 1774, "label": "Küçük Kaynarca"},
    {"year": 1839, "label": "Tanzimat"},
    {"year": 1911, "label": "Trablusgarp"},
    {"year": 1922, "label": "Saltanat"},
]

# Derleme sırasında devletleri bu bölge sırasına göre dizer.
REGION_ORDER = ["giris", "bozkir", "turkistan", "bati", "kuzey", "iran", "anadolu", "diger"]


def main():
    states, by_id, warnings = [], {}, []
    sources = sorted(RAW.glob("*.json")) + sorted((ROOT / "data" / "states").glob("*.json"))
    for path in sources:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"{path.name}: okunamadı ({exc})")
            continue
        if isinstance(data, dict) and "id" in data:
            data = [data]
        if not isinstance(data, list):
            warnings.append(f"{path.name}: kök dizi değil, atlandı")
            continue
        for s in data:
            sid = s.get("id")
            if sid in by_id:
                warnings.append(f"{sid}: {path.name} ile {by_id[sid]} çakışıyor, son gelen tutuldu")
                states[[x.get("id") for x in states].index(sid)] = s
                continue
            by_id[sid] = path.name
            states.append(s)

    def key(s):
        r = REGION_ORDER.index(s["region"]) if s.get("region") in REGION_ORDER else len(REGION_ORDER)
        return (r, s.get("start", 0), s.get("id", ""))

    states.sort(key=key)
    total_rulers = sum(len(s.get("rulers", [])) for s in states)
    out = OUT
    out.write_text(
        "/* data/raw/*.json dosyalarından tools/build.py ile üretildi. Elle düzenlemeyin. */\n"
        "window.ATLAS = " + json.dumps({"milestones": MILESTONES, "states": states}, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print(f"{len(states)} devlet, {total_rulers} hükümdar -> {out} ({out.stat().st_size/1024:.0f} KB)")
    for w in warnings:
        print("UYARI:", w)


if __name__ == "__main__":
    main()
