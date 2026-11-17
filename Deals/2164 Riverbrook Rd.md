---
type: deal
address: "2164 Riverbrook Rd, Decatur, GA 30035"
zip: "30035"
market: Atlanta
strategy: flip
status: analyzing
list_price: 250000
arv: 316188
rehab: 22550
rent: 1900
source: "https://www.realtor.com/realestateandhomes-detail/2164-Riverbrook-Rd_Decatur_GA_30035_M64087-16985"
created: 2026-11-12
updated: 2026-11-17
tags: [deal]
---

# 2164 Riverbrook Rd, Decatur, GA 30035

Market: [[Atlanta]] · Zip: [[30035]] · Project: [[Deal Pipeline]]

Property: 3 bd, 2.5 ba, 1,782 sf, 1972

## Numbers (verified only — each with source)
| Item | Value | Source |
|---|---|---|
| List / ask price | $250,000 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| Listing status in analysis | for_sale (MLS Active, new 11/4/2026) | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| ARV | $316,188 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| Rehab estimate | $22,550 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| Rent (monthly) | $1,900 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| Max flip offer | $207,600 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| BRRRR cash flow (modeled) | $-472 / mo | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| School average | 2.7 — below 4, red flag | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |
| Owner of record | company: FIDELIS EQUITY AND REAL ESTATE (company) - DeKalb assessor 2026-11-12 | payload 2026-11-12 (`2164-riverbrook-rd-decatur-ga-30035.payload.json`) |

## Criteria check
- BRRRR target on standard terms: **no** (from analysis payload).
- Grade: D

## Verdict
**rejected**

Already-renovated flip product. Fails flip ROI at -15% (profit $29,189, ROI 12.4%); max flip offer $207,600. Not a BRRRR target at any price (cash flow ~$-472/mo). Low-confidence ARV, schools 2.7.

REJECTED. Active (new listing 11/4/2026 at $250,000). Already renovated by the current owner (bought 10/2024 for $160,000; listed 5/2026 $339k -> $315k -> $299,950, delisted 10/1; listed for rent $1,900 7/23-10/19 without leasing; relisted for sale at $250k). True DOM 184 days, 3 cycles. ARV $316,188 (weighted median of 2468 Leslie Brook 0.34 mi w1 (short sale), 4469 Wellington Ter 0.52 mi w2, 2417 Winshire 0.30 mi w1 (4BR wider-range); spread 17.4% -> LOW confidence). Rehab $22,550: light make-ready $5,500 + 10% + Big5 HVAC full $11,000 + roof half $5,500 (no system ages stated). Flip at negotiated $212,500 (-15%): profit $29,189 / ROI 12.4% - fails ROI. Max flip offer $207,600 (17% below asking). BRRRR (7.5% placeholder, conditional): cash left $63,556, cash flow $-472/mo (range -636 to -390) - not a target at any price; rent needed ~$2,780. Its own $1,900 rent ad did not lease in 3 months. Owner FIDELIS EQUITY AND REAL ESTATE (company/flipper). HOA: MLS says Association Yes, fee unknown. Tax $4,815 (MLS tax year 2025; MLS fields swapped). Schools 5/2/1 avg 2.7 RED FLAG.

## Listing status (checked 2026-11-17, no RapidAPI)
- Status: **for sale**
- Place on the site after PR 367: Relevant / Market
- Ask $250k. Still for sale.

## Open tasks
- [ ] 

## Links
- Project: [[Deal Pipeline]]
- Market: [[Atlanta]]
- Zip: [[30035]]
- Listing: https://www.realtor.com/realestateandhomes-detail/2164-Riverbrook-Rd_Decatur_GA_30035_M64087-16985

## Log
Analyses and source files (latest used for the numbers above):
- 2026-11-12 (analysis): `/home/box/shared/deal-outcomes/analyses/2026-11-12/2164-riverbrook-rd-decatur-ga-30035.md`
- 2026-11-12 (payload): `/home/box/shared/deal-outcomes/analyses/2026-11-12/2164-riverbrook-rd-decatur-ga-30035.payload.json`
