---
name: vault-setup-interview
description: One-time (re-runnable) interview that fills or updates the shared Obsidian vault's 00 Profile.md and Projects/ notes - company, partners, markets, deal criteria, rules for bots, bots list and active projects. Use when the owner says "setup the vault", "הקם כספת", "ראיון הקמה", "update my profile", "add a project", or when session-open reports PROFILE MISSING.
---

# vault-setup-interview

Adapted from trestle `/onboard` (MIT), cut down for a real-estate team. Bots on this box share one vault: `/home/box/shared/obsidian-vault`.

## Step 0 - Load what exists (one call)
```bash
V=/home/box/shared/obsidian-vault; git -C $V pull --rebase --autostash -q; cat "$V/00 Profile.md" 2>/dev/null; ls "$V/Projects"
```
If the profile exists, this is an **update**: only ask about what is missing or changed.

## Step 1 - Interview (Hebrew, one question at a time, max 8; skip any already answered)
1. Company name and partners (who decides what).
2. Business model and markets (cities / zips).
3. Deal criteria per strategy (flip, BRRRR, other) - exact numbers.
4. How bots should talk to you (language, length) and standing rules (what bots must never do).
5. Which bots exist and what each is responsible for.
6. Active projects: name, owner, goal, deadline.
7. For each project: known verified facts and open tasks.
8. One recurring task you do every week that a bot could own (optional; log it in the project as a task, do not build anything now).

Record **only** what the owner said. Unknown = leave the field empty. No guesses.

## Step 2 - Write (one call)
- Profile: fill `/home/box/shared/obsidian-vault/_system/grok-trestle/templates/profile.md` → `/home/box/shared/obsidian-vault/00 Profile.md` (on update, edit only changed lines; keep `updated:` = today).
- Each project: fill `templates/project.md` → `Projects/<Project Name>.md`; link it under "Active projects" in the profile as `[[<Project Name>]]`.
- Then:
```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/vault-health.py; bash $S/safe-push.sh "AGENT" "setup interview: profile + projects"
```

## Step 3 - Prove it works
Tell the owner (Hebrew): what was written, and that any bot can now load it with "open session <project>" (`session-open`).
