---
type: reference
status: active
owner: H.S HOLDINGS
market: indianapolis
created: 2026-11-18
updated: 2026-11-18
tags: [project, deals, pipeline, reference]
---
# Deal Pipeline - How It Works

A reference for the site funnel and the Deal Analysis bot, so nobody has to re-read the code. It was read from `hs-hold/hsdeals-claude-code` main and checked against prod Supabase `ywvdyogbdptfyclgjbpf` on 2026-11-18. Parent note: [[Deal Pipeline]]. Site: [[Deals Site]].

## 1. Flow at a glance
```
daily routine (08:00 IL) ──POST x-funnel-cron──▶ funnel-run-next-zip
   └─ pickNextZip (oldest due enabled zip) ─▶ funnel-screen {pull:true,pullOnly:true,bounded:true}
         ├─ zillow-search (for-sale)          ┐
         ├─ RapidAPI sold-homes (6 mo)        │ RapidAPI host us-real-estate-listings
         ├─ RapidAPI for-rent                 │ (owner pays per call, plan 6,000/mo)
         └─ v2/property detail (survivors, detail_daily_cap = 10/day) ┘
   └─ screen in batches of 25 (self-chained screenBatch calls) ─▶ funnel_properties.screen
   └─ finishScreen ─▶ queueZip ─▶ deal_queue (max 5 per zip, smallest discount first)
daily routine ─▶ GET deal-analysis-ingest?limit=5 (marks rows "sent") ─▶ Deal Analysis bot
Deal Analysis ─▶ POST deal-analysis-ingest ─▶ deals (Grok Deals tab)
```
The routine runs the pull twice now (2 zips a day). Health mode is `{"health":true}`: it returns the next zip and the last run, and uses no RapidAPI.

## 2. Zip rotation (`zipRun.ts`, `funnel_zips`, `funnel_settings`)
- Only `enabled=true` zips are used. As of 2026-11-18 that is 34 Indy zips; Atlanta is disabled, not deleted.
- A zip is due when it was never pulled, or when `now - last_pulled_at >= pull_interval_days`. `funnel_settings.pull_interval_days` is 1, so every zip is always due and the order is never-pulled first, then the oldest pull.
- `last_pulled_at` is stamped only by a successful pull. A failed pull is retried next time.
- One call pulls one zip. At 2 a day, the 34 zips take a 17-day cycle.

## 3. Pull (`funnel-screen`, pull mode)
- For-sale listings come through the `zillow-search` function, which is RapidAPI. They are stored in `market_listings` and `funnel_properties` (dedup by identity; a price-only change re-prices without re-scoring).
- Sold comps: `sold-homes`, `sold_in_last=6` months, 1 page when `bounded`. They are merged into `funnel_zips.sold_cache`.
- Rent comps: `for-rent`, stored in `funnel_zips.rent_cache`.
- Detail enrichment (`v2/property`) runs for survivors, capped at `detail_daily_cap` (10) a day.
- Measured cost (rapidapi_usage, Nov 13–18): about 3–5 calls per zip pull. On 2026-11-18 the quota had about 4,070 calls left.

## 4. Screen (stage 1, no AI, no tokens) (`src/utils/funnel/screen.ts`)
Inputs per listing: list price, sqft (TOTAL sqft from the feed, which can include basements), beds, year, description.

**Subject exclusions** (`subjectScreen.ts`): rental status, price under $5,000 (a rent), mobile/manufactured, land or lot. `is_pending` and `is_contingent` are NOT checked.

**ARV**, in this order:
1. Verified engine (`arvEngine.computeVerifiedArv`): renovated sold comps from the zip sold cache, weighted median of adjusted prices. Settings: `arv_comp_min` 3, `comp_radius_miles` 1.5, `comp_sqft_band` 0.25, `arv_sold_days` 365. It outputs `arv`, plus `screeningArv` (the lower figure the screen prices with), `confidence` and `arvCompCount`.
2. If the engine fails, a screening estimate (`screeningEstimate.ts`): the P25 of renovated $/sf within 1 mile (else across the zip, min 5 sales, 183 days) × subject sqft, adjusted by `screeningSubject.ts` (an already-renovated subject uses the lowest $/sf). Labeled "Not an ARV". **Bug:** sqft includes basements, so on 2026-11-18 in 46112 it produced $657–845k against a $419k real ARV.

**Rent**: verified rent comps (3 or more, `rent_comp_min`) from the rent cache. Otherwise 85% of HUD FY2027 SAFMR (`safmrFy2027.ts`). That table covers only 16 of the 34 Indy zips. Missing: 46107, 46112, 46113, 46123, 46140, 46142, 46143, 46168, 46214, 46220, 46227, 46228, 46229, 46235, 46236, 46239, 46254, 46268.

**Rehab** (`rehab.ts`): sqft × tier rate. Indy: light $35, medium $55, heavy $85 per sf. Text picks the tier (gut → heavy, distressed → medium, renovated → light, default medium). Pre-1960 adds 10%. A Deal Analysis rehab, when one exists, replaces it.

**Offer formulas** (`DEFAULT_ASSUMPTIONS`, same values in `funnel_settings`):
- Flip max offer = min(byProfit, byRoi, byArvCap), where net = ARV × 0.92:
  - byProfit = (net − rehab − 3,300 hold − 30,000) / 1.02
  - byRoi = (net − 3,300 − rehab × 1.15) / 1.17
  - byArvCap = net × 0.85
  - There is no financing cost. Hold is $550 × 6.
- Rental max offer = rent / 1% − rehab. The near-rental offer = rent / 0.9% − rehab.
- **Pass** = (flip max or near-rental max) ≥ 75% of list (`maxDiscount` 0.25). `requiredDiscountPct` = % off list of the better of flip and 1%-rental max.

**Decisions**:
| decision | when | goes to queue? |
|---|---|---|
| passed | pass at list or ≤25% off | yes (if not excluded or handled) |
| rejected | both rules computable and both fail at 25% off | no |
| needs_comps | no verified ARV and no pass on the screening estimate | **no** (re-screened only when the zip is pulled again, with the same missing data) |
| held | flip fails and rent is missing; or sqft, rehab or price missing | **no** (same: stays stuck until the data changes) |

## 5. Queue (`funnel-run-next-zip.queueZip`, `zipRun.ts`)
- Only rows from the zip just pulled, with `screen.pass = true`, no exclusion, not already sent, analyzed or rejected.
- Pending rows older than 36h are expired first (`QUEUE_FRESH_MS`).
- Sorted by smallest required discount, max 5 per zip.
- The handoff is `GET deal-analysis-ingest?limit=5`, which marks rows `sent`. There is no read-only peek, so pending or already-analyzed listings still reach the bot, and the bot must skip them by hand.

## 6. Deal Analysis bot (stage 2, tokens)
Rules: `/home/box/shared/agent-rules/deal-analysis.md`, `comp-adjustments.md`, `rehab-big5.md`, `levers.md`. Outputs go to `/home/box/shared/deal-outcomes/analyses/<date>/`.
- ARV: closed renovated comps, 3 months / closest first, expand to 6 months / 0.5 mile, weighted median of adjusted prices, above-grade GLA (basement valued separately).
- Rent: verified rent comps only. Repairs: from photos, line items, Big 5 + 1.
- Trial criteria (Nov 18–24): refi at 65% LTV, ≤ $60k of our cash left in, CF ≥ $250/mo self-managed with 12% reserves, cash-flip profit ≥ $20–25k, ARV $200–300k preferred. MAO in every analysis.
- Flip math (`model15.py`): profit = ARV × 0.92 − P × 1.02 − rehab − financing (2% + 1%/mo of P+R) − $600/mo hold. Pass needs ≥ $30k and ≥ 15% ROI.
- Write-back: `POST deal-analysis-ingest`, which creates or updates a `deals` row (`analysis_source = deal analysis bot`).
- Cost (measured by the parent bot): about 0.2% of weekly usage per full analysis, and about 0.4% per daily 2-zip run.

## 7. Known gaps (2026-11-18)
1. needs_comps and held are dead ends in practice: 85% of screened Indy listings (879 of 1,040) never get a decision.
2. The screening ARV uses total sqft including basements, so ARV is inflated in basement zips.
3. The SAFMR table is missing 18 of the 34 Indy zips, so those listings land in "held".
4. The screen flip has no financing cost and a 25% band, so its MAO is about $12–20k above Deal Analysis on a $150–250k basis.
5. The queue does not exclude `is_pending` or `is_contingent`, and junk got through (sqft 2, sqft 25,850, a $1,275 "price").
6. There is no read-only queue peek, and 28 of 52 queue rows expired without analysis.

## Log
- 2026-11-18: Note created from a code read plus a prod data audit (Grok Bot, owner voice request).
