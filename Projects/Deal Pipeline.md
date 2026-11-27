---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-16
updated: 2026-11-20
tags: [project, deals]
---
# Deal Pipeline

## Goal
Find, screen and analyze flip and BRRRR deals in [[Atlanta]] and [[Indianapolis]]. One note per deal in `Deals/` (template: `_system/grok-trestle/templates/deal.md`). Site: [[Deals Site]].

## Criteria (a deal must pass all of its strategy's lines)
| Strategy | Rule |
|---|---|
| Flip | profit ≥ $30k |
| Flip | ROI ≥ 15% |
| Flip | price ≥ 15% below ARV including selling costs |
| BRRRR | equity ≥ 15% |
| BRRRR | equity ≥ $30k |
| BRRRR | cash left in deal ≤ $60k |
| BRRRR | cash flow ≥ $250/mo |

Primary strategy is BRRRR; flip is secondary (owner, 2026-11-12). Full rules: [[00 Profile]].

## Key facts (verified only — add source)
- Pipeline: site code pulls one zip at a time via RapidAPI → pre-filter in code → Deal Analysis (max ~5 per run) → write-back to Grok Deals. Daily search at 08:00 Asia/Jerusalem.
- Off-market intake: Deal Inbox reads `deals@hs-hold.com`. Zillow *email* intake was stopped on 2026-11-15; the site funnel still pulls on-market listings through site code.
- Screen's max offer was found (2026-11-13) to be looser than Deal Analysis's flip formula (no hard money, 4-month hold), which fills the queue with deals that later fail.
- Pattern (Nov 2026 analyses): many Atlanta deals in the $170–300k ARV+ band do not hit $250/mo BRRRR at 65% / 7.5%; they enter "Relevant" on flip numbers or as "works with a discount". On 2026-11-17, none of the 24 "Relevant" site deals passed the $250/mo BRRRR target at asking; 4799 Oak Ct reached +$281 only with about a 5% discount.
- Do not buy in East Point (owner, 2026-11-13).
- Past outcome files (for calibration, not a journal run): `/home/box/shared/deal-outcomes/` including [[1514 Peachcrest Rd]], [[3169 Canary Ct]], [[2195 Trailwood Dr SE]].

## Decisions
- See [[00 Profile]] for the dated owner rules (pre-filter, highway comps, time-to-sell, levers, auto-adjust cash-in, site tabs, ranking, unanalyzed deals must not appear, deal journal only after a stated purchase).
- 2026-11-15: owner rated [[1733 Olive St]] 8/10 as the top BRRRR-oriented example (ask $85k, rent $1,710 unverified, ARV ~$250k); works at ~$84.4k with partial refi or at ask with interest-only; rent and insurance unverified.
- 2026-11-17: listing-status check (no RapidAPI) of on-market "Relevant" deals; under-contract deals moved to the Unavailable tab (PR 367). Auction listings stay in Relevant with an Auction badge.

## Open tasks
Canonical live list: [[Open Items]]. Items below are kept as history and should be reconciled there, not duplicated as a second source of truth.

- [ ] Fix funnel-run-next-zip: on a RapidAPI timeout (retry_later) keep the same zip instead of advancing nextZip; re-pull 46143 and 46168 (skipped Nov 21). Land in the next single merge batch.
- [ ] After Indy ARV fixes (PR 329 landed): audit the share of deals with no auto ARV / needs_comps, and deals dropped for missing API data (owner asked 2026-11-10; do not start before the fix, then do it)
- [ ] Daily routine that calls `funnel-run-next-zip` once and hands `deal_queue` (max 5) to Deal Analysis — was pending owner approval
- [ ] Optional: investigate why the 2026-11-17 daily pull of zip 30273 returned 55 properties and none passed screening (possible screen skip after a timeout retry)
- [x] Grok Analyses market filter live (PR 368/369)
- [ ] Trial criteria Nov 18–24; compare on Nov 25 10:00
- [ ] Indy-only check-in Nov 24 10:00
- [ ] Engine tax-change proposal still awaiting a yes from the owner
- [ ] Older open item: contractor size research, paused
- [ ] Deep recheck of old contacts (see [[Indy Trip Nov 2026]])
- [ ] Next single batch: PR 370 + PR 376, plus (proposed 2026-11-20) a read-only `deal_queue` peek so GET does not mark unpulled items 'sent', a screened-listing count in the funnel health response, and "ready for full renovation"/"blank canvas" listing text → heavy rehab tier
- [ ] Owner: analyse the two sent-but-unanalysed Avon items (7228 Lockford Walk N, 1881 Wynnewood Ln)? Recommendation: no
- [ ] Off-market lead source (2026-11-20): owner to decide scope / runner / budget of [[off-market-lead-generation]]; recommended start = free Indy lists + direct mail with QR consent; reminder delivered Sun Nov 22 10:00, awaiting owner
- [ ] Investigate RapidAPI spike 2026-11-22 (155 calls/24h, mostly zillow-search for-sale) and stop unscheduled pulls
- [ ] Pre-screen passed 0 for several daily runs in a row (e.g. 46214/46220 on Nov 22) — check if stricter than trial criteria

## Links
- Profile: [[00 Profile]]
- Site: [[Deals Site]]
- Markets: [[Atlanta]], [[Indianapolis]]

## Log
- 2026-11-09–12: first analysis waves (Indy + Atlanta), including [[1733 Olive St]] and [[1613 Draper St]] (later re-analyzed under the 11-11 rules).
- 2026-11-13: 30032/30058 added to the buy box; East Point excluded; 5BR allowed; Malibu and Primrose among the better flip-conditional names; screen-vs-analysis gap noted.
- 2026-11-15: three wholesaler deals ([[5301 Essex Farms Pl]], [[5811 Shadow Rock Dr]], [[4799 Oak Ct]]) all rejected at ask; Essex already pending on MLS at $290k.
- 2026-11-17: daily funnel zip 30273 — 0 passed screening. Listing-status pass on the 24 Relevant deals; PR 367 shipped Unavailable + status badges. [[4213 River Rd]] (Anthony / Mr ATL Wholesaler, $249k) rejected; records are 4/3 and 2,911 sf plus unfinished basement, not 5BR / 4,000+ sf.
- 2026-11-17 evening: trial criteria for Nov 18–24 set (see [[00 Profile]]); MAO required in every analysis; Indianapolis-only focus, funnel expanded with the 33 trip zips, two zips per day with motivated-seller priority. [[1733 Olive St]] rejected after the micro-location check.
- 2026-11-19: daily zips 46113/46123, 0 sent. Owner approved pending + new-construction pre-queue skips, the Indy 50% finished-basement rule, 8 prescreen fixes (outliers flagged, not removed) and one-batch landing. PRs 375/374/372/373/371 merged; 4 migrations and 9 functions deployed; cache-only re-screen of 732 rows queued 0 (197 held for `basement_unknown`). [[2026-11-19 Indy ARV diagnostic (4 listings)]] and [[2026-11-19 Atlanta held deals (4)]]: all reject. Next proposed step: Marion County Assessor above-grade/basement data. See [[2026-11-19]].
- 2026-11-19 (evening): owner approved the Marion County backfill; PR 376 filled 133/197 holds from the live county property card and re-screened them: 0 queued (main blockers: too few comps, high asks). 64 still held (49 in 46112, outside Marion). PR 370 motivated-seller tag kept loose by the owner. PRs 370 + 376 wait for the next single batch.
- 2026-11-20: daily zips 46140/46142 → 1 queued → [[1019 N Broadway St]] REJECT (rehab tier was the screen's big miss: $75.8k vs $39.1k). Deal Analysis found the ingest GET marks unpulled items 'sent'. Next due zip 46143. Wholesale lead [[4244 Canby Ln]] also REJECT. See [[2026-11-20]].
- 2026-11-20 evening: WhatsApp wholesale lead from [[Adam (Atlanta wholesaler)]] → [[714 Cather Ct]] (30088, $143k, hoarder) REJECT, trial MAO $86.1k; posted to the site on owner instruction (deal b74f7b63).
- 2026-11-21: daily search failed — RapidAPI timeouts on 46143 (07:54) and 46168 (08:06), 0 properties, nothing analyzed; found the timeout zip-skip bug. RapidAPI 1,953/6,000 used. See [[2026-11-21]].
- 2026-11-21: Owner wants Claude to review the hsdeals-claude-code repo and suggest optimizations. Grok Bot wrote an English handoff brief (flow, key files, what lives outside code, known bugs; no secrets): /home/box/shared/claude-handoff/claude-handoff-brief-2026-11-21.md, Drive דוחות ומחקר. Claude may propose PRs only — no merge/deploy; changes go into the single merge batch.
- 2026-11-22: daily zips 46214/46220 OK, 190 checked, 0 passed pre-screen; 46143/46168 still not re-pulled. RapidAPI 2,117/6,000 used, 155 calls in 24h (alert). See [[2026-11-22]].
- 2026-11-25: quick-screen quality check (20:02, read only): 239 scanned in 46268/46205, 9 passed, 5 queued, all rejected by Deal Analysis. Findings: 5-per-run queue cap silently drops passes (4515 Primrose, 4532 Indianola, 4846 Crittenden, 5153 Kingsley — all 13–16% off); `low_comps` hold may block 3369 Broadway St ($135k, screen ARV $353k); screen misses already-renovated homes; possible 30-s health polling loop on 46201/46205. Report in Drive דוחות ומחקר. See OI-SCREEN-QUALITY-2511 and [[2026-11-25]].
- 2026-11-26: Atlanta 2170 Lilac Ln / 7080 Stone St (owner-OK'd) both rejected; funnel 46201+46203 4/4 rejected, goodPotential on 2856 S State Ave and 321 S Hamilton Ave. ~$60k number sent on 303 N Franklin Rd. See [[2026-11-26]].
- 2026-11-27 evening: final screening-quality report + queue-gap investigation (Grok Bot 20:05/20:36): 8 screen passes never queued (7 cut by 5-per-run cap in 46208, 3423 N Sherman Dr blocked by dedupe against an un-analysed intake row); 4 of them pass at ask by screen MAO. PR #399 (low_comps exception, owner-approved Option 1) open. See [[2026-11-27]] and OI-SCREEN-QUALITY-2511.
