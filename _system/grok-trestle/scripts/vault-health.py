#!/usr/bin/env python3
"""Vault health check (adapted from trestle kb-check.mjs, MIT). python3 stdlib only.

Usage: vault-health.py [--stale-days N] [--inbox-days N] [--json]
Checks:
  FRONTMATTER  every note (outside _system/) has a --- YAML block with a `type:` key
  LINKS        [[wikilinks]] and relative markdown links resolve to a real file
  STALE        Projects with status active/planning not updated in N days (default 14);
               00 Inbox notes older than M days (default 7)
  TASKS        count of open "- [ ]" tasks (info)
  SECRETS      credential-shaped values anywhere in the vault (FAIL => do not commit)
  SYNC         uncommitted / unpushed / behind origin
Exit: 0 = no WARN/FAIL, 1 = WARN only, 2 = FAIL (secrets).
"""
import os, re, sys, json, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import VAULT, md_files, read, frontmatter, strip_code, git, today, parse_date

def arg(name, default):
    if name in sys.argv:
        return int(sys.argv[sys.argv.index(name) + 1])
    return default

STALE_DAYS, INBOX_DAYS = arg("--stale-days", 14), arg("--inbox-days", 7)
LINK_EXEMPT = ("_system/grok-trestle/templates/",)

def run():
    res = {}  # check -> (level, summary, details[])
    files = list(md_files(include_system=False))
    all_md = list(md_files(include_system=True))
    rels = [os.path.relpath(p, VAULT) for p in files]

    # index for wikilinks: by basename (no .md) and by relative path (no .md)
    names = set()
    for p in all_md:
        r = os.path.relpath(p, VAULT)[:-3]
        names.add(r.lower()); names.add(os.path.basename(r).lower())
    all_files = set()
    for d, dirs, fs in os.walk(VAULT):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in fs:
            r = os.path.relpath(os.path.join(d, f), VAULT)
            all_files.add(r.lower()); all_files.add(os.path.basename(r).lower())

    fm_bad, broken, stale, tasks = [], [], [], 0
    for p, r in zip(files, rels):
        text = read(p)
        base = os.path.basename(r)
        fm = frontmatter(text)
        if base != "README.md":
            if fm is None:
                fm_bad.append(f"{r}: no frontmatter block")
            elif not fm.get("type"):
                fm_bad.append(f"{r}: frontmatter has no `type:`")
        body = strip_code(text)
        tasks += len(re.findall(r"^\s*[-*] \[ \]\s*\S", body, re.M))
        for m in re.finditer(r"!?\[\[([^\]|#^]+)(?:[#^][^\]|]*)?(?:\|[^\]]*)?\]\]", body):
            t = m.group(1).strip().lower()
            if t.endswith(".md"): t = t[:-3]
            if t not in names and t not in all_files:
                broken.append(f"{r}: [[{m.group(1)}]]")
        for m in re.finditer(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", body):
            t = m.group(1)
            if re.match(r"^[a-z][a-z0-9+.-]*:", t, re.I) or t.startswith("#"):
                continue
            t = t.split("#")[0].replace("%20", " ")
            target = os.path.normpath(os.path.join(os.path.dirname(p), t))
            if not os.path.exists(target):
                broken.append(f"{r}: ({m.group(1)})")
        # staleness
        if fm and r.startswith("Projects" + os.sep) and fm.get("status", "").lower() in ("active", "planning"):
            d = parse_date(fm.get("updated") or fm.get("date"))
            if d and (today() - d).days > STALE_DAYS:
                stale.append(f"{r}: status {fm.get('status')}, last updated {d} ({(today()-d).days}d)")
            elif not d:
                stale.append(f"{r}: active project without `updated:` date")
        if r.startswith("00 Inbox" + os.sep):
            d = parse_date((fm or {}).get("date"))
            if d and (today() - d).days > INBOX_DAYS:
                stale.append(f"{r}: in Inbox {(today()-d).days}d - file it")

    res["FRONTMATTER"] = ("WARN" if fm_bad else "OK", f"{len(fm_bad)} note(s) need frontmatter fixes" if fm_bad else f"{len(files)} notes OK", fm_bad)
    res["LINKS"] = ("WARN" if broken else "OK", f"{len(broken)} broken link(s)" if broken else "all links resolve", broken)
    res["STALE"] = ("WARN" if stale else "OK", f"{len(stale)} stale item(s)" if stale else "nothing stale", stale)
    res["TASKS"] = ("INFO", f"{tasks} open task(s) '- [ ]'", [])

    sc = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "secrets-scan.py")],
                        capture_output=True, text=True)
    lines = sc.stdout.strip().splitlines()
    res["SECRETS"] = ("FAIL" if sc.returncode == 2 else "OK", lines[0].replace("SECRETS: ", "") if lines else "?", [l.strip() for l in lines[1:]])

    dirty = [l for l in git("status", "--porcelain").splitlines() if l.strip()]
    ab = git("rev-list", "--left-right", "--count", "@{u}...HEAD").split()
    behind, ahead = (int(ab[0]), int(ab[1])) if len(ab) == 2 else (0, 0)
    sync_bits = []
    if dirty: sync_bits.append(f"{len(dirty)} uncommitted change(s)")
    if ahead: sync_bits.append(f"{ahead} unpushed commit(s)")
    if behind: sync_bits.append(f"{behind} commit(s) behind origin (run git pull --rebase)")
    res["SYNC"] = ("WARN" if sync_bits else "OK", "; ".join(sync_bits) or "clean and in sync with origin (as of last fetch)", dirty[:20])
    return res

if __name__ == "__main__":
    res = run()
    if "--json" in sys.argv:
        print(json.dumps({k: {"level": v[0], "summary": v[1], "details": v[2]} for k, v in res.items()}, ensure_ascii=False, indent=1))
    else:
        print(f"VAULT HEALTH  {VAULT}  {today()}")
        for k, (lvl, s, det) in res.items():
            print(f"{lvl:5} {k:12} {s}")
            for d in det[:15]:
                print(f"        - {d}")
            if len(det) > 15:
                print(f"        ... +{len(det)-15} more")
    lv = [v[0] for v in res.values()]
    sys.exit(2 if "FAIL" in lv else 1 if "WARN" in lv else 0)
