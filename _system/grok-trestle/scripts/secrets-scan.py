#!/usr/bin/env python3
"""Scan vault files for credential-shaped values. Never prints the full value.

Usage:
  secrets-scan.py              # scan every text file in the vault (except .git, _private/)
  secrets-scan.py FILE...      # scan only these files (paths relative to vault or absolute)
  secrets-scan.py --staged     # scan the content staged for commit (used by safe-push.sh)
Exit code: 0 = clean, 2 = secrets found.
"""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import VAULT, SECRET_RE, SKIP_DIRS, mask, read

TEXT_EXT = {".md", ".txt", ".csv", ".json", ".yml", ".yaml", ".html", ".htm", ".py", ".sh", ".js", ".mjs", ".env", ".ini", ".toml", ""}
SELF = {"_system/grok-trestle/scripts/_common.py"}  # holds the regex itself

def scan_text(name, text, hits):
    for i, line in enumerate(text.splitlines(), 1):
        for m in SECRET_RE.finditer(line):
            hits.append((name, i, mask(m.group(0))))

def is_private(rel):
    return rel.split("/")[0] == "_private" or "/_private/" in rel

def main(argv):
    hits = []
    if argv[:1] == ["--staged"]:
        names = subprocess.run(["git", "-C", VAULT, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
                               capture_output=True, text=True).stdout.split("\0")
        for rel in filter(None, names):
            if rel in SELF or is_private(rel):
                continue
            blob = subprocess.run(["git", "-C", VAULT, "show", f":{rel}"], capture_output=True)
            if b"\0" in blob.stdout[:4096]:
                continue
            scan_text(rel, blob.stdout.decode("utf-8", "replace"), hits)
    else:
        files = []
        if argv:
            files = [a if os.path.isabs(a) else os.path.join(VAULT, a) for a in argv]
        else:
            for d, dirs, fs in os.walk(VAULT):
                dirs[:] = [x for x in dirs if x not in SKIP_DIRS and x != "_private"]
                files += [os.path.join(d, f) for f in fs if os.path.splitext(f)[1].lower() in TEXT_EXT]
        for p in files:
            rel = os.path.relpath(p, VAULT)
            if rel in SELF or is_private(rel) or not os.path.isfile(p):
                continue
            scan_text(rel, read(p), hits)
    if hits:
        print(f"SECRETS: FOUND {len(hits)} credential-shaped value(s) - DO NOT COMMIT")
        for f, ln, m in hits:
            print(f"  {f}:{ln}  {m}")
        return 2
    print("SECRETS: OK (none found)")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
