---
name: session-close
description: Close a work session and write what was learned back to the shared Obsidian vault (hs-obsidian) - dated learnings, decisions and open tasks to the project note and Agents/<bot>.md, then health check and safe git commit + push. Use when the owner says "close session", "סגור סשן", "wrap up", "save to Obsidian", "תשמור באובסידיאן", at the end of a substantial task, or after any decision, verified finding or new task worth remembering.
---

# session-close

Grok Trestle sign-off ritual (adapted from trestle `/73`, MIT). The session only "grows" the vault if something writes it back - this is that something. **Target: 2 shell calls.**

Scripts dir: `/home/box/shared/obsidian-vault/_system/grok-trestle/scripts`

## Step 1 - Decide what to write (no tool call)
From the conversation you already have, pick only durable, verified items:
- **learned**: verified facts with source (numbers, zips, contacts, market facts).
- **decision**: what the owner decided (and why, if said).
- **task**: open follow-ups, phrased as an action ("Get rehab quote for 123 Main St").
- **done**: open tasks in the project note that were completed (exact task text).
- Bigger artifacts get their own note from a template (deal → `Deals/<address>.md`, contact → `Contacts/<name>.md`, meeting → `Meetings/YYYY-MM-DD <title>.md`, market research → `Markets/<city>/...`). Templates: `/home/box/shared/obsidian-vault/_system/grok-trestle/templates/`.
Never write passwords, tokens, API keys, card numbers or login details. Point to where they live instead ("login: in the owner's password manager").

## Step 2 - Write + check + push (one shell call)

```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/session-close.py --agent "AGENT" --project "PROJECT" \
  --summary "one-line summary of the session" \
  --learned "fact (source: URL)" --decision "decision" --task "next action" --done "exact text of finished task" ; \
python3 $S/vault-health.py ; \
bash $S/safe-push.sh "AGENT" "session close: PROJECT - short summary"
```
- Repeat `--learned/--decision/--task/--done` as many times as needed; drop any that are empty. Omit `--project` if there is none (then tasks go to the agent log as checkboxes).
- If you also created notes from templates, create them in the same call (heredoc `cat > ... <<'EOF'`) **before** `safe-push.sh`.

## Step 3 - Handle results
- `PUSH: OK <sha>` → done.
- `PUSH: BLOCKED secrets found` → nothing was committed. Remove the value from the file named, then rerun `safe-push.sh`. If a secret was ever pushed before, tell the owner plainly: **it is in git history - rotate it.**
- `PUSH: FAIL ... conflict` → run `git -C /home/box/shared/obsidian-vault status`, resolve by keeping both sides' lines (append-only notes), `git add -A && git rebase --continue`, then rerun `safe-push.sh`.
- Health `WARN LINKS/FRONTMATTER` caused by this session → fix in a follow-up call and push again. Other WARNs → mention as action items.

## Step 4 - Reply
Hebrew, short: what was saved (counts + note names), open tasks, and "saved and synced" / "not synced: reason".
