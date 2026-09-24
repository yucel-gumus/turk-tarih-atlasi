#!/usr/bin/env python3
"""Atlas ham veri doğrulayıcı.

Kullanım:  python3 tools/validate.py data/raw/a-bati.json [...]
Kod 0 = geçti, 1 = hata. Tüm dosyalar için:  python3 tools/validate.py data/raw/*.json
"""
import json
import sys
from pathlib import Path

REGIONS = {"giris", "bozkir", "turkistan", "bati", "kuzey", "iran", "anadolu", "diger"}
CONF = {"kayit", "tartismali", "rivayet"}
RESULTS = {"zafer", "yenilgi", "sonucsuz", "belirsiz", "antlasma"}
CERT = {"kesin", "olasi", "muhtemel", "tartismali", "rivayet"}
ROOT = Path(__file__).resolve().parent.parent


def is_url(u):
    return isinstance(u, str) and u.startswith(("http://", "https://")) and " " not in u


def check_person(p, where, errs):
    if not isinstance(p, dict):
        errs.append(f"{where}: kişi nesne değil")
        return
    if not isinstance(p.get("name"), str) or not p["name"].strip():
        errs.append(f"{where}: kişi adı yok")
    if p.get("certainty") and p["certainty"] not in CERT:
        errs.append(f"{where}: certainty geçersiz ({p['certainty']})")


def check_sources(src, where, errs, required=True):
    if not isinstance(src, list):
        errs.append(f"{where}: sources dizi değil")
        return
    if required and not src:
        errs.append(f"{where}: kaynak yok")
    for s in src:
        if not isinstance(s, dict) or not isinstance(s.get("title"), str) or not s["title"].strip():
            errs.append(f"{where}: kaynak başlığı eksik")
            continue
        if not is_url(s.get("url", "")):
            errs.append(f"{where}: kaynak url geçersiz ({s.get('url')!r})")


def check_year(v, where, errs, field):
    if v is not None and not isinstance(v, int):
        errs.append(f"{where}: {field} sayı değil ({v!r})")


def validate_file(path):
    errs, stats = [], {"states": 0, "rulers": 0, "wars": 0, "wives": 0, "children": 0}
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: JSON okunamadı: {exc}"], stats
    if isinstance(raw, dict) and "id" in raw:
        raw = [raw]
    if not isinstance(raw, list):
        return [f"{path}: kök dizi olmalı"], stats
    ids = set()
    for i, s in enumerate(raw):
        where = f"{path}[{i}]"
        if not isinstance(s, dict):
            errs.append(f"{where}: devlet nesne değil")
            continue
        sid = s.get("id", "")
        where = f"{path}[{sid or i}]"
        if not isinstance(sid, str) or not sid.strip() or sid != sid.lower() or " " in sid:
            errs.append(f"{where}: id geçersiz ({sid!r})")
        if sid in ids:
            errs.append(f"{where}: id tekrar")
        ids.add(sid)
        for f in ("name", "short", "summary"):
            if not isinstance(s.get(f), str) or not s[f].strip():
                errs.append(f"{where}: {f} boş")
        if s.get("region") not in REGIONS:
            errs.append(f"{where}: region geçersiz ({s.get('region')!r})")
        if s.get("confidence", "kayit") not in CONF:
            errs.append(f"{where}: confidence geçersiz ({s.get('confidence')!r})")
        for f in ("start", "end"):
            if not isinstance(s.get(f), int):
                errs.append(f"{where}: {f} sayı değil")
        if isinstance(s.get("start"), int) and isinstance(s.get("end"), int) and s["end"] < s["start"]:
            errs.append(f"{where}: end < start")
        if not isinstance(s.get("essay", []), list) or any(not isinstance(p, str) for p in s.get("essay", [])):
            errs.append(f"{where}: essay string dizisi değil")
        check_sources(s.get("sources"), where, errs)
        rulers = s.get("rulers", [])
        if not isinstance(rulers, list):
            errs.append(f"{where}: rulers dizi değil")
            rulers = []
        rids = set()
        for r in rulers:
            if not isinstance(r, dict):
                errs.append(f"{where}: hükümdar nesne değil")
                continue
            rw = f"{where}/{r.get('id', '?')}"
            rid = r.get("id", "")
            if not isinstance(rid, str) or not rid.strip() or " " in rid:
                errs.append(f"{rw}: id geçersiz")
            if rid in rids:
                errs.append(f"{rw}: hükümdar id tekrar")
            rids.add(rid)
            if not isinstance(r.get("name"), str) or not r["name"].strip():
                errs.append(f"{rw}: ad yok")
            if not isinstance(r.get("summary"), str) or not r["summary"].strip():
                errs.append(f"{rw}: summary boş")
            reign = r.get("reign")
            if not isinstance(reign, list) or len(reign) != 2:
                errs.append(f"{rw}: reign [a,b] olmalı")
            else:
                a, b = reign
                if a is not None and not isinstance(a, int):
                    errs.append(f"{rw}: reign başlangıcı sayı ya da null olmalı")
                if b is not None and not isinstance(b, int):
                    errs.append(f"{rw}: reign bitişi sayı ya da null olmalı")
                elif isinstance(a, int) and isinstance(b, int) and b < a:
                    errs.append(f"{rw}: reign bitişi başlangıçtan önce")
            check_year(r.get("birth"), rw, errs, "birth")
            check_year(r.get("death"), rw, errs, "death")
            for f in ("traits", "legends", "aliases"):
                v = r.get(f, [])
                if not isinstance(v, list) or any(not isinstance(x, str) for x in v):
                    errs.append(f"{rw}: {f} string dizisi değil")
            for f in ("wives", "children"):
                v = r.get(f)
                if not isinstance(v, list):
                    errs.append(f"{rw}: {f} dizi değil")
                    continue
                for p in v:
                    check_person(p, rw, errs)
                    if f == "children" and isinstance(p, dict) and p.get("mother") is not None and not isinstance(p["mother"], str):
                        errs.append(f"{rw}: çocuk anne alanı string değil")
            wars = r.get("wars")
            if not isinstance(wars, list):
                errs.append(f"{rw}: wars dizi değil")
            else:
                for w in wars:
                    if not isinstance(w, dict) or not isinstance(w.get("name"), str) or not w["name"].strip():
                        errs.append(f"{rw}: savaş adı yok")
                        continue
                    if w.get("result") not in RESULTS:
                        errs.append(f"{rw}: savaş sonucu geçersiz ({w.get('result')!r})")
            check_sources(r.get("sources"), rw, errs)
            stats["rulers"] += 1
            stats["wars"] += len(wars) if isinstance(wars, list) else 0
            stats["wives"] += len(r.get("wives", [])) if isinstance(r.get("wives"), list) else 0
            stats["children"] += len(r.get("children", [])) if isinstance(r.get("children"), list) else 0
        stats["states"] += 1
    return errs, stats


def main(argv):
    files = argv[1:]
    if not files:
        print(__doc__)
        return 1
    total, all_errs = {"states": 0, "rulers": 0, "wars": 0, "wives": 0, "children": 0}, []
    seen = {}
    for f in files:
        errs, stats = validate_file(f)
        all_errs.extend(errs)
        for k in total:
            total[k] += stats[k]
        print(f"{Path(f).name}: {stats['states']} devlet, {stats['rulers']} hükümdar, "
              f"{stats['wars']} savaş, {stats['wives']} eş, {stats['children']} çocuk, "
              f"{len(errs)} hata")
        try:
            _d = json.loads(Path(f).read_text(encoding="utf-8"))
            for s in ([_d] if isinstance(_d, dict) else _d):
                if s.get("id") in seen:
                    all_errs.append(f"{Path(f).name}: '{s['id']}' id'si {seen[s['id']]} dosyasında da var")
                seen[s.get("id")] = Path(f).name
        except Exception:  # noqa: BLE001
            pass
    print(f"TOPLAM: {total}")
    if all_errs:
        print(f"\n{len(all_errs)} HATA:")
        for e in all_errs[:80]:
            print("  -", e)
        return 1
    print("Tamam, hata yok.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
