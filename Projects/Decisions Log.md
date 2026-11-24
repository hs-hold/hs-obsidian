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
- 2026-11-23 16:26 [decision] (Eran, Grok Bot voice call): The BiggerPockets reminder is a quiet standing reminder. Keep it stored, but never surface it proactively, repeatedly, or in open-item lists, digests or notifications; mention it only if the owner brings it up. Applies to all bots, including מזכירה.
- 2026-11-23 16:27 [decision] (Eran, Grok Bot voice call): approved one-batch merge+deploy of PRs 370, 376, 377 plus live re-pull of 46143/46168/46236. [verified] Done 17:05: squash commits 34798ec, 76fa46b, 73003e5; migration 20261117120000_motivated_seller applied; funnel-screen v20, funnel-run-next-zip v9, gmail-sync v52, deal-analysis-ingest v12, zillow-search v38 deployed; re-pull used 5 RapidAPI calls (1262 to 1267). 46168 queued 2 (605 S East St, 4099 N Cheltonham Ct, still pending, not sent to Deal Analysis). 46236: 5 rows unscreened due to HTTP 546. Timeout fix returned the new retry_later contract live.
- 2026-11-23 16:25 [decision] (Eran, Grok Bot chat): for every email Grok Bot sends from deals@, report back in the Grok Bot chat when a reply arrives.
- 2026-11-23 19:19 [decision] (Eran, Grok Bot chat): replies to deals@ emails that introduced Tal (Indy brokers, Nolan Lamkin, Steele Kruzel) are reported to the owner in the Grok Bot chat; all other deals@ replies are forwarded to the relevant bot (usually Deal Inbox), not the owner.
- 2026-11-23 20:03 [decision] (Eran, Grok Bot voice call): decide whether Atlanta moves to the Indy ARV method only after the filter-audit conclusions; no change until then.
- 2026-11-23 20:46 [decision] (Eran, Grok Bot chat): any property that passes Deal Analysis is uploaded to the deals site, including audit/test properties.
- 2026-11-23 20:50 [decision] (Eran, Grok Bot chat): "תמיד תעלה כאלה שעובדים עם הנחה של עד 15%" — properties that pass at ask or at up to 15% off ask are always uploaded. 20:51: approved writing the rule into Deal Analysis's git rules file (done 20:56, reported).
- 2026-11-23 21:05 [decision] (Eran, Grok Bot chat): Indy Tuesday meeting replies (Steele, Zac, Nolan) — "דואגים להכל, אל תענה לאף אחד כרגע": no replies or drafts for now.

- 2026-11-24 11:40 [decision] Indianapolis full cosmetic rehab range for screening = $25–35/sqft (Eran chose $35 cap instead of the $45 found in research); replaces the $55/sqft default (rehab.ts:105-114) when the rehab-estimate PR is built. Not live yet.
- 2026-11-24 11:41 [decision] Indy cosmetic sub-tiers (calibration direction): light refresh/paint only <$25/sf; $25/sf = popcorn ceiling, maybe doors, sometimes kitchen; $30/sf with credit = includes kitchen. Overall range stays $25-35. Eran: the filter must separate tiers precisely. Log only.
- 2026-11-24 11:42 [decision] Rehab calibration guidance: Eran's tier figures are a starting point only, not fixed rules; research online instead of guessing when info is missing; decompose each rehab tier into cost-driving components for precise later calibration. No production changes.
- 2026-11-24 11:43 [decision] Principle: the analysis bot and the whole filter/analysis pipeline see all available data and use wide discretion; agreed rules (rehab ranges, filter criteria, ARV approach) are guidelines, not rigid laws; when something is open the bot closes on the correct numbers itself and records them with reasoning. Auto-upload safety blocks stay hard unless Eran decides otherwise (flagged to him). Log only.
- 2026-11-24 11:44 [decision] Definition: "super comp" = a property sold in the last 3 months. Its role in the ARV pipeline (incl. relation to the single-comp auto-upload block) is still to be defined by Eran. Log only.
