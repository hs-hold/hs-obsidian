---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-16
updated: 2026-11-17
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
- [ ] After Indy ARV fixes (PR 329 landed): audit the share of deals with no auto ARV / needs_comps, and deals dropped for missing API data (owner asked 2026-11-10; do not start before the fix, then do it)
- [ ] Daily routine that calls `funnel-run-next-zip` once and hands `deal_queue` (max 5) to Deal Analysis — was pending owner approval
- [ ] Optional: investigate why the 2026-11-17 daily pull of zip 30273 returned 55 properties and none passed screening (possible screen skip after a timeout retry)
- [ ] Grok Analyses market filter (Indianapolis vs Georgia) — requested 2026-11-17; cloud agent started, confirm it is live
- [ ] Engine tax-change proposal still awaiting a yes from the owner
- [ ] Older open item: contractor size research, paused
- [ ] Deep recheck of old contacts (see [[Indy Trip Nov 2026]])

## Links
- Profile: [[00 Profile]]
- Site: [[Deals Site]]
- Markets: [[Atlanta]], [[Indianapolis]]

## Log
- 2026-11-09–12: first analysis waves (Indy + Atlanta), including [[1733 Olive St]] and [[1613 Draper St]] (later re-analyzed under the 11-11 rules).
- 2026-11-13: 30032/30058 added to the buy box; East Point excluded; 5BR allowed; Malibu and Primrose among the better flip-conditional names; screen-vs-analysis gap noted.
- 2026-11-15: three wholesaler deals ([[5301 Essex Farms Pl]], [[5811 Shadow Rock Dr]], [[4799 Oak Ct]]) all rejected at ask; Essex already pending on MLS at $290k.
- 2026-11-17: daily funnel zip 30273 — 0 passed screening. Listing-status pass on the 24 Relevant deals; PR 367 shipped Unavailable + status badges. [[4213 River Rd]] (Anthony / Mr ATL Wholesaler, $249k) rejected; records are 4/3 and 2,911 sf plus unfinished basement, not 5BR / 4,000+ sf.
