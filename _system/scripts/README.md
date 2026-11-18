# _system/scripts

## build_memory_file.py → `00 Memory.md`
Builds ONE compressed, always-fresh memory file at the vault root (`00 Memory.md`) so a main agent can answer "how does bot X work / what is decided / what is open" without reading the whole vault.

- Run: `python3 _system/scripts/build_memory_file.py` (options: `--days 7`, `--out "00 Memory.md"`). Python 3 stdlib only, no network/LLM, <1 s, deterministic. Overwrites the file every run — never edit it by hand.
- Sections: header (generated time Asia/Jerusalem + source commit) · Bots (one block per bot: role/job, rules files, rules naming the bot, schedules, latest log entry, open to-dos, recent daily-note mentions, last activity) · Owner rules & active criteria · Open decisions/items · Key recent outcomes (last 7 days) · folder map · gaps.
- Sources: `Agents/*.md`, `00 Profile.md` (rule sections + Bots list), `Projects/*.md` (Decisions, Open tasks, Known gaps), `Notes/Daily/*.md` (sections whose headings contain Decisions / Conclusions / Info from the owner / Agent work / What happened / Open; `- [ ]` anywhere; `- [x]` skipped). Bot roles also come from `/home/box/agent-data/agents/*/profile.json` when readable (skipped silently otherwise).
- Safety: output passes through a secret-pattern redaction; secrets never belong in the vault anyway.
- Trigger: run at the end of the twice-daily vault sync (13:00 / 23:00 Asia/Jerusalem), then commit with `_system/grok-trestle/scripts/safe-push.sh`.
- Agents: read `00 Memory.md` first; if a topic is missing, search the vault for it before answering.
