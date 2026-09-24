#!/usr/bin/env python3
"""Ham veriyi şemaya çeker: certainty sözlüğü, kaynak başlıkları, tip sapmaları."""
import json, re, sys
from pathlib import Path
from urllib.parse import urlparse

CERT = {
    "kesin": "kesin", "yuksek": "kesin", "yüksek": "kesin", "high": "kesin",
    "orta": "olasi", "olasi": "olasi", "olası": "olasi", "medium": "olasi",
    "muhtemel": "muhtemel",
    "dusuk": "tartismali", "düşük": "tartismali", "low": "tartismali",
    "tartismali": "tartismali", "tartışmalı": "tartismali", "belirsiz": "tartismali",
    "rivayet": "rivayet", "efsane": "rivayet",
}
HOST = {
    "islamansiklopedisi.org.tr": "TDV İslâm Ansiklopedisi",
    "britannica.com": "Britannica",
    "www.britannica.com": "Britannica",
    "tr.wikipedia.org": "Vikipedi (TR)",
    "en.wikipedia.org": "Vikipedi (EN)",
    "wikipedia.org": "Vikipedi",
}


def fix_sources(src):
    out = []
    for s in src or []:
        if not isinstance(s, dict):
            continue
        url = s.get("url", "")
        title = (s.get("title") or "").strip()
        if not title:
            host = urlparse(url).netloc.lower()
            title = HOST.get(host) or host or "Kaynak"
            if host == "islamansiklopedisi.org.tr":
                slug = urlparse(url).path.strip("/").replace("-", " ").title()
                title = f"TDV İslâm Ansiklopedisi, {slug}"
        out.append({"title": title, "url": url})
    seen, uniq = set(), []
    for s in out:
        if s["url"] in seen:
            continue
        seen.add(s["url"])
        uniq.append(s)
    return uniq


def fix_people(rows):
    out = []
    for p in rows or []:
        if not isinstance(p, dict):
            continue
        c = str(p.get("certainty", "") or "").strip().lower()
        if c:
            p["certainty"] = CERT.get(c, c)
        p.setdefault("note", "")
        out.append(p)
    return out


def fix(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    was_dict = False
    if isinstance(data, dict) and "id" in data:
        data = [data]
        was_dict = True
    changes = 0
    for s in data:
        s["sources"] = fix_sources(s.get("sources"))
        s.setdefault("aliases", [])
        for key in ("startNote", "endNote", "capital", "religion", "confidenceNote", "legacy"):
            s.setdefault(key, "")
        if s.get("confidence") not in ("kayit", "tartismali", "rivayet"):
            s["confidence"] = "kayit"
        for r in s.get("rulers", []):
            r.setdefault("aliases", [])
            r.setdefault("title", "")
            r.setdefault("reignNote", "")
            r.setdefault("contribution", "")
            r.setdefault("harm", "")
            for f in ("traits", "legends"):
                v = r.get(f)
                if isinstance(v, str):
                    r[f] = [v] if v.strip() else []
                elif not isinstance(v, list):
                    r[f] = []
                else:
                    r[f] = [str(x) for x in v if str(x).strip()]
            r["wives"] = fix_people(r.get("wives"))
            r["children"] = fix_people(r.get("children"))
            if not isinstance(r.get("reign"), list) or len(r["reign"]) != 2:
                r["reign"] = [None, None]
            for p in r["children"]:
                p.setdefault("mother", "")
            r["sources"] = fix_sources(r.get("sources"))
            for w in r.get("wars", []):
                w.setdefault("note", "")
                w.setdefault("when", "")
                w.setdefault("foe", "")
            changes += 1
    out_data = data[0] if was_dict else data
    Path(path).write_text(json.dumps(out_data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{Path(path).name}: {len(data)} devlet, {changes} hükümdar düzeltildi")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        fix(p)
