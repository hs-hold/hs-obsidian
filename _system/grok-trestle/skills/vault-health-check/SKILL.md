---
name: vault-health-check
description: Run the health check on the shared Obsidian vault (hs-obsidian) - broken links, missing frontmatter, stale projects/inbox, open-task count, secrets scan and git sync state - and fix what it finds. Use when the owner asks "is the vault OK", "בדיקת בריאות לכספת", "check Obsidian", before any big write, or when session-close shows WARN/FAIL.
---

# vault-health-check

Adapted from trestle `kb-check` (MIT). Checks fail loudly so problems get fixed instead of remembered.

## Run (one call)
```bash
python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/vault-health.py
```
Options: `--stale-days 14` (active projects not updated in N days), `--inbox-days 7`, `--json`.
Exit code: 0 all OK, 1 WARN, 2 FAIL (secrets).

Secrets only: `python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/secrets-scan.py` (whole vault) or `... secrets-scan.py "Deals/123 Main St.md"` (one file).

## Fix each finding
- `FRONTMATTER` → add a `---` block with `type:` (profile | project | deal | contact | meeting | agent-log | note | market) at the top. Copy the matching block from `_system/grok-trestle/templates/`.
- `LINKS` → `[[Name]]` must match an existing file name (without `.md`); markdown links are relative to the note's folder. Fix the name or create the missing note from a template.
- `STALE` project → ask the owner: next step, or set `status: on-hold` / `done`. Inbox note → move it to the right folder (`git mv`).
- `SECRETS FAIL` → **never commit**. Delete the value, replace with a pointer ("stored in owner's password manager"). If `git log -S` shows it was already pushed, tell the owner to rotate the key.
- `SYNC` → run session-close / `safe-push.sh`.

Commit fixes with:
```bash
bash /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/safe-push.sh "AGENT" "health fixes"
```
Reply in Hebrew: one line per check (OK/WARN/FAIL) + what you fixed.
