# Grok Trestle

A session-ritual toolkit for the H.S HOLDINGS Grok Bot agents, living inside the shared Obsidian vault (`hs-hold/hs-obsidian`).

Adapted from **[trestle](https://github.com/liormesh/trestle)** by Lior Meshullam (MIT) — the Claude Code workspace setup tool. Trestle's ideas (profile interview, open/close session rituals, health checks that fail loudly, secrets guard, self-contained HTML reports) are re-implemented here for Grok Bot agents that share one Linux box and have no Claude Code hooks.

| Folder | What |
|---|---|
| `skills/` | 5 Grok Bot skills: `vault-setup-interview`, `session-open`, `session-close`, `vault-health-check`, `vault-report` |
| `scripts/` | python3/bash, stdlib only: `session-open.py`, `session-close.py`, `vault-health.py`, `secrets-scan.py`, `vault-report.py`, `safe-push.sh` |
| `templates/` | profile, project, deal, contact, meeting, agent-log (YAML frontmatter) |
| `GUIDE-he.md/.html`, `GUIDE-en.md/.html` | Full guide (Hebrew / English) |

Quick use (on the box):
```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/session-open.py --agent "Grok Bot" --project "Indy"
python3 $S/session-close.py --agent "Grok Bot" --project "Indy" --learned "..." --task "..."
python3 $S/vault-health.py && bash $S/safe-push.sh "Grok Bot" "session close"
python3 $S/vault-report.py
```

## License
Original trestle: MIT © 2026 Lior Meshullam — full text in [LICENSE-trestle-MIT.txt](LICENSE-trestle-MIT.txt). The secret-pattern list in `scripts/_common.py` and the skill structure are derived from it. This adaptation is distributed under the same MIT terms.
