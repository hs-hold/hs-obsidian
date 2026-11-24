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
- 2026-11-24 11:44 [decision] SUPERSEDES previous super-comp line: super comp = near one-to-one comp: built within ±5 years, same or neighboring street <0.3 mi, same school district and similar amenities, nearly same size, same layout, sold in last 3 months; even if more renovated, renovating to its level means selling at its price. Open: can one super comp override the single-comp auto-upload block (Eran to decide). Log only.
- 2026-11-24 11:45 [decision] Super comp is slightly flexible: a near-miss is flagged as "potential super comp" and reported to Eran (which parameter is off and by how much); the bot does not decide silently. Log only.
- 2026-11-24 12:33 [decision] Build plan approved: 6 PRs (safety site+engine → screening+zillow-search → ARV engine with calibration before and after). Nothing implemented or deployed until ALL open decisions are collected.
- 2026-11-24 12:34 [decision] Auctions: not a focus now; filter auctions early at deal pulling so they never reach the Deal Analysis bot. Single-comp and missing-data blocks still open.
- 2026-11-24 12:35 [decision] Single-comp ARV block can be overridden when the comp is a super comp (per the definition approved today). Missing-data block still open.
- 2026-11-24 12:35 [decision] Single comp addition: a non-super single comp with high confidence is still a very good indication; when suitable comps are lacking, always pull 1-2 more comps even if they differ in size and lot area.
- 2026-11-24 12:37 [decision] Bathroom adjustments kept as in current engine code (Indy $9k/$12k for 1→2 by comp median <>$250k, 3rd+ $4k/$6k, half $4k/$6k or $3k/$4.5k; Atlanta 5% of comp price clamped $8k-$30k, half bath = half). Lot size remains filter-only, adjustment undecided (open).
- 2026-11-24 12:40 [decision] Missing-data block (closes decision 2): bot makes an effort to close a missing field; if it can't, it estimates and marks it uncertain, and the site shows a 'needs verification' marker wherever that field appears.
- 2026-11-24 12:42 [decision] Ingest plausibility (closes decision 4 of list): no fixed numeric ranges; bot judges reasonableness, researches real numbers if clearly off, and notifies Eran in chat if still unresolved.
- 2026-11-24 12:44 [decision] Calibration scope: separate per region (Indy and Atlanta), each its own 20 sales and own coefficients, not merged. Corrects an earlier same-minute 'combined' statement.
- 2026-11-24 12:45 [decision] Calibration addition: any verified data (own closed deals or authenticated market data) is fed into that region's calibration, in code without AI, recorded in code going forward.
- 2026-11-24 12:46 [decision] Atlanta rehab: research cosmetic costs, decompose into components like Indy, build Atlanta range + tiers similar to Indy.
- 2026-11-24 12:46 [decision] Correction: Atlanta rehab item is recorded as a decision only; nothing starts (no research, code or deploy) until all decisions are collected.
- 2026-11-24 12:47 [decision] BRRRR holding cost: actual tax + insurance replaces fixed $550/mo. New requirement: Deal Analysis bot must know every site data parameter and record all deal-analysis parameters for the site realistically and accurately.
- 2026-11-24 12:48 [decision] ARV > 2x ask: mark, don't stop; bot verifies with comps; more than one supporting comp means it may be real and the deal must not be missed.
- 2026-11-24 12:49 [decision] Low confidence: bot works to raise it; suspected-bad deals move on; likely-good but low-confidence deals get more data pulled; if still unconfirmed, tell Eran to verify (strong preference: bot gets the data itself). Closes the 3 site-gate fixes.
- 2026-11-24 12:50 [decision] Low-confidence addition: when unsure, bot pulls additional comps and makes additional comp adjustments to raise confidence.
- 2026-11-24 12:51 [decision] Bot override limit 70% vs its own engine number; under 70% stands with reason+evidence; over 70% high confidence = bot approves, low confidence = notify Eran.
- 2026-11-24 12:52 [decision] Deal engine moves to GitHub as source of truth for all work; local backup kept. Not moved yet.
- 2026-11-24 12:53 [decision] Lot size: calibration + bot judgment; extreme lot difference excludes the comp; similar house with lot 1.5-2x larger can still be suitable. ALL open decisions now collected; building still requires Eran's go-ahead.
- 2026-11-24 12:54 [decision] Super comp refinement: sold within 3 months, near-same build year and same building type; may override the single-comp block and serve as a single comp only if it truly meets the criteria. Near-miss does not override. No decisions remain open.

- 2026-11-24 13:03: D2 calibration list 20 Indy + 20 Atlanta, filled from each bot analysis rather than a separate search (owner, voice).
- 2026-11-24 13:04: photo-less comps: infer renovation from description and price position; repeated failures to find photos are escalated to Eran (owner, voice).
- 2026-11-24 13:05: school data from the existing API/site first, else ratings of the 3 nearby schools from Zillow/Realtor; compare subject vs comp (owner, voice).
- 2026-11-24 13:08: tests-first PR for screen/rehab/queueGate/ingest + CI on every PR approved (owner, voice).
- 2026-11-24 13:09: owner approved starting the full build once the Indy rehab research returns (owner, voice).
