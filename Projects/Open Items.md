---
type: project
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [project, tracker]
---
# Open Items

Single tracker for open decisions and tasks. Fields: id, topic, owner agent, status, updated, next action, needs-owner-approval, source. History is kept at the bottom. Do not close an item without verification. Populated by the existing 13:00 / 23:00 sync — no new routine.

Status values: open, waiting-owner, waiting-verification, prepared, blocked, closed.

## Open

### OI-M10 — Sync time 23:00 vs 23:30
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner decides whether documentation and/or the evening routine should be 23:00 or 23:30
- Needs owner approval: yes
- Source: [[00 Profile]] (writes 13:00 and 23:30, original request 17 Nov); running brain-sync routine and `_system/scripts/README.md` use 13:00 and 23:00; last successful midday sync 2026-11-23 13:20 IST
- Notes: [verified] The 23 Nov upgrade must not change this decision. The running 23:00 routine was left untouched, and docs were not aligned to 23:00.

### OI-C-WATCH — Widen and verify the Indy broker reply watch
- Owner agent: Grok Bot
- Status: waiting-verification
- Updated: 2026-11-23 14:20
- Next action: coordinator already applied the widened watch prompt (old prompt + schedule snapshotted under `/home/box/shared/backups/2026-11-23/routine-snapshots/`; schedule unchanged 09/15/21). Eight "send now" specialist messages were sent (priority false); Deal Inbox and Indy Research were told to keep reporting until verification. A read-only dry run of checklist items 1–9 on 23 Nov 14:15 Israel **passed** (report: `artifacts/e-watch-verification-dry-run-2026-11-23.md`). No A/B/C subject gap. C-4 stop-reporting messages are still **not** sent — coordinator sends them after accepting this dry run, then watches one cycle for duplicate reports. Do not disturb the Steele 16:00 send or the Nolan 18:00 call.
- Needs owner approval: no
- Source: `/home/box/shared/indy-trip/broker-replies-log.md`; artifacts in `/home/box/shared/backups/2026-11-23/artifacts/`

### OI-STEEL-EMAIL — Steele call-request email
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23
- Next action: one-off routine should send today at 16:00 Israel (09:00 Indy). Report the result. Then set a call; he offered Tue 1 Dec 10:00–12:00 Indy.
- Needs owner approval: no for the already-approved send; yes for any new commitment
- Source: [[Steele Kruzel]], thread 1a1ff4e4244967dd

### OI-NOLAN-CALL — Tal / Nolan call
- Owner agent: Grok Bot (coordinate only; Tal calls)
- Status: open
- Updated: 2026-11-23
- Next action: call today 18:00–18:30 Israel / 11:00 ET at (317) 696-9545. Do not send a reminder email (owner did not approve one).
- Needs owner approval: no
- Source: [[Nolan Lamkin]], thread 1a1ff1abd91802e5, event on deals@ calendar

### OI-BOUNCE — Bounced intro recipients
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner chooses — Tal calls KK Buys Indy Homes (Kent) and Stacy Patlan, or new emails are found and a resend is approved. Also note a delivery *delay* (not a confirmed bounce) to salesteam@indytradingpost.com, thread 1a1ff11944150d2d.
- Needs owner approval: yes
- Source: broker-replies-log.md; [[Indy Trip Nov 2026]]

### OI-CRITERIA — Trial criteria review 25 Nov
- Owner agent: Grok Bot / Deal Analysis
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: review 25 Nov 2026 10:00 Israel. Mapping of current contradictions is in [[Criteria Map]]. No business criteria will be changed before this decision. After the decision, internal docs may be updated to the approved version; code, merge, and deploy still need a separate batch approval.
- Needs owner approval: yes
- Source: [[00 Profile]] trial block 18–24 Nov; [[Criteria Map]]

### OI-PRESREEN — Pre-screen vs trial criteria
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23
- Next action: wait for OI-CRITERIA. Site code (read-only, `src/utils/funnel/screen.ts` on `hs-hold/hsdeals-claude-code`) uses flip profit $30,000 and 15% ROI, or rent at 1% (near pass 0.9%), with up to 25% off list. Several recent daily zips passed 0 listings. Do not change code until the owner decides and a later PR is approved.
- Needs owner approval: yes (business rule and later merge)
- Source: [[Criteria Map]], [[Deal Pipeline]]

### OI-TIMEOUT — Timeout advances the next zip
- Owner agent: Grok Bot (cloud agent may open a PR)
- Status: prepared
- Updated: 2026-11-23
- Next action: coordinator launched a cloud agent to open the timeout PR (no merge). The production bug is **not** fixed: the 23 Nov extra search recorded `retry_later` / "Signal timed out." on 46236 at 07:13 UTC, then pulled 46239 (which also timed out once, then succeeded). Re-pull 46143, 46168, and 46236 only after a later approved deploy and live test.
- Needs owner approval: yes for merge/deploy/live test; PR preparation is in the approved plan
- Source: `supabase/functions/funnel-run-next-zip/index.ts` (retry_later sets pull_retry_after and returns nextZip); [[Deal Pipeline]]

### OI-RAPIDAPI — RapidAPI pace above the ~25/day target
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23
- Next action: live `rapidapi_usage` for the Nov 22 155-call window is still not queryable from this helper (no Supabase connector; secrets were not used). A pre-existing dump `/workspace/deal-search-2026-11-23-extra/rapidapi_today.json` (no new RapidAPI calls) covers 23 Nov 01:24–07:25 UTC only: 113 calls, 86 of them Atlanta zips under trigger `zillow_search` (burst 06:50–07:03 UTC / 08:50–09:03 Israel), and 27 Indy under trigger `funnel`. That Atlanta burst is the likely driver of the 09:03 alert (96 calls / 24h, 90 zillow-search for-sale). Do not start further unscheduled pulls. See the RapidAPI note in progress.md.
- Needs owner approval: no for further read-only investigation; yes to change schedules or deploy
- Source: RapidAPI watch 22–23 Nov; that report

### OI-OFFERS — Offers submitted this week
- Owner agent: Grok Bot / מזכירה
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner to state how many offers were submitted (asked in weekly metrics)
- Needs owner approval: yes (the number comes from the owner)
- Source: [[Metrics]]

### OI-SKILLS — Seven skill proposals
- Owner agent: Grok Bot / Content Insights
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner approves, drops, or revises each proposal. Summary: `_system/reports/2026-11-23-skill-proposals-summary.md`. Do not implement any skill without approval. Proposal 3 (call scripts) was already dropped for Tal's trip.
- Needs owner approval: yes
- Source: `/home/box/shared/skills-proposed/`

### OI-MERGE-BATCH — Next merge/deploy batch
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: after open questions are answered, one batch: PRs 370 and 376, plus queued fixes (screened count in health, queue peek / non-consuming GET, full-renovation text → heavy rehab, timeout retry same zip, re-pull 46143 and 46168). Do not merge now.
- Needs owner approval: yes
- Source: [[Deal Pipeline]], [[Deals Site]]

### OI-SITE-UPLOAD — Five 23 Nov analyses not on the site
- Owner agent: Deal Analysis
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner approval in the Deal Analysis chat before any site write. Files are in `/home/box/shared/deal-outcomes/analyses/2026-11-23/`. All five were REJECT at ask.
- Needs owner approval: yes
- Source: [[2026-11-23 Indy extra search near-misses (5)]]

### OI-AVON — Two sent-but-unanalysed Avon items
- Owner agent: Deal Analysis
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner yes/no on analysing 7228 Lockford Walk N and 1881 Wynnewood Ln. Recommendation on file: no
- Needs owner approval: yes
- Source: [[Deal Pipeline]]

### OI-OFFMARKET — Off-market lead scope
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner decides scope, runner, and budget of the off-market-lead-generation proposal. Reminder already delivered 22 Nov.
- Needs owner approval: yes
- Source: [[off-market-lead-generation]], [[Indy Trip Nov 2026]]

### OI-TAX-ENGINE — Engine tax-change proposal
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner yes/no
- Needs owner approval: yes
- Source: [[Deal Pipeline]]

### OI-DROPPED-AUDIT — Audit deals dropped for missing ARV/API data
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23
- Next action: start only after the relevant Indy ARV fixes are confirmed landed
- Needs owner approval: no to start after the precondition; report results
- Source: [[Deal Pipeline]]

### OI-DAILY-FUNNEL-ROUTINE — Daily funnel-run-next-zip routine
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: create only after approval (was pending)
- Needs owner approval: yes
- Source: [[Deal Pipeline]]

### OI-TRIP-FLIGHTS — Tal's exact flight dates
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-23
- Next action: owner confirms flight dates
- Needs owner approval: yes
- Source: [[Indy Trip Nov 2026]]

### OI-SQ-MEETUP — Simple Quarters meetup 25 Nov
- Owner agent: Indianapolis Market Research
- Status: open
- Updated: 2026-11-23
- Next action: confirm whether the meetup runs on Thanksgiving eve
- Needs owner approval: no for the check; yes before any contact
- Source: [[Indy Trip Nov 2026]]

### OI-BIGGERPOCKETS — Secretary holds BiggerPockets reminder
- Owner agent: מזכירה
- Status: quiet standing reminder (owner decision 2026-11-23 16:26)
- Updated: 2026-11-23
- Next action: keep stored silently; do NOT surface proactively, in open-item lists, digests or notifications; mention only if the owner raises it
- Needs owner approval: no
- Source: [[2026-11-23]]

### OI-ZIPINTEL-GAPS — Zip intel files still missing
- Owner agent: Zip Intel
- Status: open
- Updated: 2026-11-23
- Next action: notes still missing for 46107, 46113, 46142, 46143, 46168, 46214, 46229, 46236, 46239 (checked on disk 2026-11-23). 46112, 46123, and 46140 exist.
- Needs owner approval: no
- Source: `/home/box/shared/zip-intel/`

### OI-PROPERTYCOUNT — Health propertyCount always 0
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23
- Next action: treat as a stale/unused field unless a later PR is approved to fix the health payload
- Needs owner approval: yes to change/deploy
- Source: [[2026-11-23]] daily search note

### OI-LOG-SYNTAX — 22 Nov "log write syntax error"
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-23 14:20
- Next action: [verified] not found in vault, shared files, the audit text, Deal Inbox transcript, or this helper's session. The main Grok Bot transcript is still not searchable from the executor. Coordinator can close this if a search of the main chat also finds nothing; otherwise leave open only if the main chat has a hit.
- Needs owner approval: no
- Source: agent audit 23 Nov; rechecked 23 Nov 14:15

## History (closed, keep)

### OI-46140 — Zip intel note for 46140 claimed missing
- Owner agent: Zip Intel
- Status: closed
- Updated: 2026-11-23
- Next action: none
- Needs owner approval: no
- Source: [[2026-11-20]] open checkbox; file `/home/box/shared/zip-intel/46140.md`
- Evidence: [verified] 2026-11-23, the file exists, 29,297 bytes, mtime 2026-11-21 21:40 IST, and is a full Greenfield / Hancock County note (mentions 1019 N Broadway St). The 20 Nov daily checkbox was marked done and [stale], not deleted.
