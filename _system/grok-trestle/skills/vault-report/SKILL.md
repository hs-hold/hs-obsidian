---
name: vault-report
description: Generate a self-contained Hebrew HTML status report of the shared Obsidian vault (health, notes per folder, projects, open tasks, bot activity, recent changes) and save it into the vault. Use when the owner asks for "vault report", "דוח כספת", "status of Obsidian", "מה המצב בכספת", or a weekly overview.
---

# vault-report

Adapted from trestle `/visualize` (MIT): one self-contained HTML file, opens offline, on phone, and inside Obsidian.

## Run (one call)
```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/vault-report.py && bash $S/safe-push.sh "AGENT" "vault report $(date +%F)"
```
Output: `/home/box/shared/obsidian-vault/_system/reports/vault-report.html` (overwritten each run; history stays in git).
For a copy outside the vault: `python3 $S/vault-report.py --out /workspace/vault-report.html`.

## Reply
Hebrew, short: counts (notes, projects, open tasks, WARNs) and attach the HTML file. Do not paste the whole report into chat.
