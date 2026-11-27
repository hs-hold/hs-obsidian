---
type: project
status: active
created: 2026-11-23
updated: 2026-11-27
tags: [project, memory]
---
# Canonical Sources

Map of where authoritative information lives. [verified] 2026-11-23. If two places disagree, use the source in this table and update or stale-mark the other.

## Map
- Owner standing rules and business criteria (until the 25 Nov review): [[00 Profile]]
- Compressed always-fresh summary (generated, do not edit by hand): [[00 Memory]]
- Open tasks and decisions waiting for the owner: [[Open Items]]
- Append-only owner and team decisions: [[Decisions Log]]
- Memory tags, stale-marking, sync merge rules: [[conventions]]
- Bot roles and recent logs: `Agents/<bot>.md`
- Deal pipeline narrative and older open-task lists (history): [[Deal Pipeline]], [[Deal Pipeline - How It Works]]
- Indianapolis trip: [[Indy Trip Nov 2026]]
- Outreach and broker replies (every thread id): `/home/box/shared/indy-trip/broker-replies-log.md`
- Broker search prompt: `/home/box/shared/indy-trip/broker-search-prompt.md` (also [[broker-search-prompt]])
- Specialist standing rules: `/home/box/shared/agent-rules/` (git on this box, no GitHub remote)
- Zip intel notes: `/home/box/shared/zip-intel/<zip>.md`
- Full deal analyses: `/home/box/shared/deal-outcomes/analyses/`
- Site and funnel code: GitHub `hs-hold/hsdeals-claude-code` (changes only via PR; merge/deploy need a separate owner batch)
- Who changes the site [verified process, 2026-11-27 11:10, Grok Bot chat]: only Grok Bot, through a new Cursor cloud agent per change that opens a PR in hs-hold/hsdeals-claude-code. Nothing merges without Eran's approval. The site auto-deploys after a merge. Deal Analysis never touches code and only uploads deals as data.
- Criteria differences across files (mapping only, no new business rule): [[Criteria Map]]
- Drive library: only inside the Content Insights folder, see [[Drive Library]]
- Secrets: never in the vault or Drive. Live on the box under `/home/box/shared/secrets/` or the owner's password manager.

## How bots should use this
Read [[00 Memory]] first. If a topic is missing, use this map, then open the canonical file. Do not invent a second copy of the same list.
