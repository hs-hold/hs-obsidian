---
name: session-open
description: Open a work session against the shared Obsidian vault (hs-obsidian) - pull the latest notes and load this bot's context (profile, project note, recent agent log, open tasks, health). Use when the owner says "open session", "open session <project>", "פתח סשן", "תפתח סשן על <פרויקט>", "load context", or at the start of any substantial task about a deal, market, contact or project.
---

# session-open

Grok Trestle opening ritual (adapted from trestle `/cq`, MIT). Goal: start every piece of work with the vault's current context, in **one shell call**.

Vault: `/home/box/shared/obsidian-vault` (git repo `hs-hold/hs-obsidian`, auth via the configured credential helper; never print or echo the token).

## Steps

1. Work out two values:
   - `AGENT` = your own bot name exactly as listed in `00 Profile.md` (e.g. `Grok Bot`, `Deal Analysis`, `Indianapolis Market Research`, `מזכירה`).
   - `PROJECT` = the project the owner named (a file in `Projects/`, partial name is fine, e.g. `Indy`, `Deal Pipeline`). If none was named, omit `--project`.
2. Run exactly one command:

```bash
python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/session-open.py --agent "AGENT" --project "PROJECT"
```

   Without a project: `python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/session-open.py --agent "AGENT"`

3. Read the output (already in context - do not re-open the same files):
   - `PULL: FAIL` → tell the owner the vault could not sync and continue read-only.
   - `PROJECT ... NOT FOUND` → offer to create it: `cp /home/box/shared/obsidian-vault/_system/grok-trestle/templates/project.md "/home/box/shared/obsidian-vault/Projects/<Name>.md"` then fill the `{{...}}` fields with facts the owner gave (no guesses).
   - `PROFILE ... MISSING` → suggest the `vault-setup-interview` skill.
   - Any `FAIL SECRETS` → stop and tell the owner; do not commit anything until fixed.
4. Reply to the owner in Hebrew, short: project status in 1-2 lines, the open tasks relevant to them, and any WARN worth knowing. Then continue with the task.

## Rules
- Facts in the vault are the team's memory: prefer them over your own memory, but if a fact conflicts with a fresh verified source, say so and fix it at session-close.
- Do not write during open; writing happens in `session-close`.
