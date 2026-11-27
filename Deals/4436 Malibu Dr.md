---
type: deal
address: "4436 Malibu Dr, Decatur, GA 30035"
zip: "30035"
market: Atlanta
strategy: flip
status: analyzing
list_price: 183900
arv: 303241
rehab: 37950
rent: 2400
source: 
created: 2026-11-13
updated: 2026-11-17
tags: [deal]
---

# 4436 Malibu Dr, Decatur, GA 30035

Market: [[Atlanta]] · Zip: [[30035]] · Project: [[Deal Pipeline]]

Property: 5 bd, 2.5 ba, 2,322 sf, 1968

## Numbers (verified only — each with source)
| Item | Value | Source |
|---|---|---|
| List / ask price | $183,900 | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| Listing status in analysis | Active (FMLS 7783639 / GAMLS 10780291, Mainstay Brokerage). This cycle listed 2026-06-06 at $260,150, 8 cuts to $183,900 (11/3) = -29%. Prior cycle 2024-12-31 at $278,000 -> $258,000, removed 5/2026 -> true DOM ~682 (2 cycles) -> -15%. Sold 2020-02-18 for $119,000; listed for rent 2020 ($1,625) and 11/2022 ($1,750). | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| ARV | $303,241 | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| Rehab estimate | $37,950 | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| Rent (monthly) | $2,400 | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| Max flip offer | $178,900 | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| BRRRR cash flow (modeled) | $82 / mo | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| School average | 2.3 — below 4, red flag | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |
| Owner of record | company: Not verified (DeKalb assessor script errors). Mainstay Brokerage listing, rented 2020-2022 -> likely institutional SFR owner (company flag). | payload 2026-11-13 (`4436-malibu-dr-decatur-ga-30035.payload.json`) |

## Criteria check
- BRRRR target on standard terms: **no** (from analysis payload).
- Grade: B

## Verdict
**go-conditional**

Flip passes at negotiated $156,315 (-15%, true DOM ~682): profit $57,941, ROI 29.8% (conservative ARV $43,403); BRRRR target with partial refi at <= $159,200 (6 mo). Conditions: walk-through (boarded openings, virtual staging), legal bedroom count, HVAC/roof.

Go-conditional at <= $159,200 BRRRR (partial refi) / <= $178,900 flip; offer $156,315. Offer math: flip max $178,900 (6 mo) / $166,400 (12 mo) at median ARV $303,241; $167,500 / $154,700 at conservative ARV $287,438.

## Listing status (checked 2026-11-17, no RapidAPI)
- Status: **off-market (email)**
- Place on the site after PR 367: Relevant / Email
- The only off-market deal in the 2026-11-17 Relevant set. Ask $183.9k, rent $2,400, ARV $303k. Needs ~2% off; cash flow +$82 in that snapshot. Not part of the on-market status check.

## Open tasks
- [ ] 

## Links
- Project: [[Deal Pipeline]]
- Market: [[Atlanta]]
- Zip: [[30035]]

## Log
Analyses and source files (latest used for the numbers above):
- 2026-11-13 (analysis): `/home/box/shared/deal-outcomes/analyses/2026-11-13/zillow/4436-malibu-dr-decatur-ga-30035.md`
- 2026-11-13 (payload): `/home/box/shared/deal-outcomes/analyses/2026-11-13/zillow/4436-malibu-dr-decatur-ga-30035.payload.json`
- [verified] 2026-11-27 12:25 Israel (live Supabase, via Grok Bot chat): after PR #398 (15% rule) this deal is one of 7 **relevant** on the site: works at 8% off ($168.8K), very low ARV confidence. Analyzed before the 24 Nov engine change. Optional re-analysis offered to Eran, not requested (OI-REANALYZE-2711).
