#!/usr/bin/env python3
"""Open a session: pull the vault and print the context a bot needs, compactly.

Usage: session-open.py --agent "<bot name>" [--project "<project note name>"] [--log-lines 40] [--no-pull]
Prints: profile, project note (if given), last entries of Agents/<bot>.md, open tasks, inbox, health one-liners.
Project lookup: exact file Projects/<name>.md, else first Projects/*.md whose name contains <name> (case-insensitive).
"""
import os, re, sys, subprocess, argparse, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import VAULT, read, md_files, strip_code

ap = argparse.ArgumentParser()
ap.add_argument("--agent", required=True); ap.add_argument("--project")
ap.add_argument("--log-lines", type=int, default=40); ap.add_argument("--no-pull", action="store_true")
a = ap.parse_args()

def sec(t): print(f"\n===== {t} =====")

if not a.no_pull:
    r = subprocess.run(["flock", "-w", "60", "/tmp/hs-obsidian-vault.lock", "git", "-C", VAULT, "pull", "--rebase", "--autostash", "-q"],
                       capture_output=True, text=True)
    print("PULL:", "OK" if r.returncode == 0 else "FAIL - " + re.sub(r"https://[^@\s]+@", "https://***@", r.stderr.strip())[-300:])

sec("PROFILE (00 Profile.md)")
pp = os.path.join(VAULT, "00 Profile.md")
print(read(pp).strip() if os.path.exists(pp) else "MISSING - run the vault-setup-interview skill")

proj_rel = None
if a.project:
    exact = os.path.join(VAULT, "Projects", a.project if a.project.endswith(".md") else a.project + ".md")
    cands = [exact] if os.path.exists(exact) else [p for p in sorted(glob.glob(os.path.join(VAULT, "Projects", "*.md")))
                                                     if a.project.lower() in os.path.basename(p).lower()]
    sec(f"PROJECT ({a.project})")
    if cands:
        proj_rel = os.path.relpath(cands[0], VAULT); print(f"[{proj_rel}]"); print(read(cands[0]).strip())
    else:
        print("NOT FOUND. Existing projects:", ", ".join(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(VAULT, "Projects", "*.md"))) or "none")

sec(f"AGENT LOG (Agents/{a.agent}.md, last {a.log_lines} lines)")
ap_ = os.path.join(VAULT, "Agents", a.agent + ".md")
if os.path.exists(ap_):
    lines = read(ap_).rstrip().splitlines(); print("\n".join(lines[-a.log_lines:]))
else:
    print("No log yet - session-close.py will create it.")

sec("OPEN TASKS (- [ ])")
n = 0
for p in md_files():
    rel = os.path.relpath(p, VAULT)
    for line in strip_code(read(p)).splitlines():
        if re.match(r"^\s*[-*] \[ \]\s*\S", line):
            n += 1
            if n <= 30: print(f"{rel}: {line.strip()[6:]}")
print(f"total open: {n}" + (" (showing 30)" if n > 30 else ""))

inbox = [f for f in os.listdir(os.path.join(VAULT, "00 Inbox")) if f.endswith(".md")] if os.path.isdir(os.path.join(VAULT, "00 Inbox")) else []
sec("INBOX"); print(f"{len(inbox)} unfiled note(s)" + (": " + ", ".join(inbox[:10]) if inbox else ""))

sec("HEALTH")
h = subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault-health.py")], capture_output=True, text=True)
print("\n".join(l for l in h.stdout.splitlines()[1:] if not l.startswith("        ")))
