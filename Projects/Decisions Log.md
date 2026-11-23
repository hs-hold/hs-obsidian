---
type: project
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [project, decisions]
---
# Decisions Log

Append-only. Do not edit or delete older entries. If a decision changes, add a new dated line that points at the previous id.

## 2026-11-23
- D-2026-11-23-01 [decision] Owner approved the full agent-system upgrade plan, with five clarifications: (1) M-10 — do not change the original sync-time decision; keep the running routine at 23:00 and record 23:00 vs 23:30 as an open item; (2) C-1–C-4 — the central watch must be verified on all relevant deals@ outreach threads, including new replies, not only Nolan and Steele, before any other bot stops reporting; do not retire an existing mechanism first; (3) P0 — backups must be secure, restorable, and free of exposed secrets; a real restore test is a precondition; (4) R-3 — a PR and mock tests are allowed with zero RapidAPI calls; do not call the timeout bug fixed in production until merge, deploy, and a live test (separate approval); (5) K-1–K-5 — no business criteria changes before the 25 Nov decision; internal docs may be updated after that decision; code, merge, and deploy still need separate approval. Source: owner message 14:00 Asia/Jerusalem, 23 Nov 2026.
- D-2026-11-23-02 [decision] US send hours (already in [[00 Profile]]): always track Atlanta and Indianapolis local time (US Eastern). Emails to US contacts only at reasonable local business hours (about 09:00–18:00 Eastern weekdays = 16:00–01:00 Israel). State the local time when proposing a send; if off-hours, schedule for 09:00 their time. Source: owner, 23 Nov 2026, already synced at 13:16–13:20.
- D-2026-11-17-01 [decision] [reported from existing profile] Owner asked for a twice-daily harvest at 13:00 and 23:30 Asia/Jerusalem, plus an immediate write when something is decided. The running routines and script comments use 13:00 and 23:00. Contradiction left open as OI-M10; no time change made on 23 Nov 2026.

- 2026-11-23 14:39 [decision] (Eran, Grok Bot chat): RapidAPI volume is not a problem in itself (113 calls on 23.11 partly from owner-requested searches). Never limit owner-requested searches or reduce deal quantity/quality to save calls; only watch for loops, unnecessary duplicate calls and faults causing abnormal waste.
