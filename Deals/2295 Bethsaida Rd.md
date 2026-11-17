---
type: deal
address: "2295 Bethsaida Rd, Riverdale, GA 30296"
zip: "30296"
market: Atlanta
strategy: flip
status: analyzing
list_price: 119950
arv: 213000
rehab: 58000
rent: 1650
source: "https://www.realtor.com/realestateandhomes-detail/2295-Bethsaida-Rd_Riverdale_GA_30296_M57982-28943"
created: 2026-11-09
updated: 2026-11-17
tags: [deal]
---

# 2295 Bethsaida Rd, Riverdale, GA 30296

Market: [[Atlanta]] · Zip: [[30296]] · Project: [[Deal Pipeline]]

Property: 3 bd, 1.5 ba, 1,333 sf, 1955

## Numbers (verified only — each with source)
| Item | Value | Source |
|---|---|---|
| List / ask price | $119,950 | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| Listing status in analysis | Active (FMLS 7790012), REO / foreclosure, not pending (funnel queue 2026-11-13) | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| ARV | $213,000 | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| Rehab estimate | $58,000 | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| Rent (monthly) | $1,650 | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| Max flip offer | $90,600 | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| BRRRR cash flow (modeled) | $42 / mo | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| School average | 3.33 — below 4, red flag | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |
| Owner of record | company: U S BANK TRUST NATIONAL ASSOCIATION (REO trustee) - Fulton GIS | payload 2026-11-09 (`2295-bethsaida-rd-riverdale-ga-30296.payload.json`) |

## Criteria check
- BRRRR target on standard terms: **no** (from analysis payload).
- Grade: D (confidence: low)

## Verdict
**rejected**

Not a BRRRR target on 65% terms at any price; flip needs <= $90,600 (24.5% off asking, below the $99,931 foreclosure basis). Low-confidence ARV.

REJECTED (LOW CONFIDENCE). REO (U S Bank Trust NA), listed 2026-06-17 at $174,950, 4 cuts to $119,950; true DOM ~149 -> negotiated -15% = $101,958. City of South Fulton (TaxDist 55, verified Fulton GIS). ARV $213,000 low confidence (5 COSF comps 0.39-0.96 mi, weighted median, -2% noise, -5% power lines). Rehab $58,000 (asbestos encapsulation, tar/gravel roof, windows, well/septic). Rent $1,650 (6 Redfin rental comps, Fulton side; size-matched median ~$1,790). Flip at negotiated: $17,566 / 11.0% (fails); max flip offer $90,600 (6 mo) / $79,800 (12 mo). BRRRR at 65%/7.5%/30y: cash flow $42/mo (investor tax $2,519/yr), not a target at any price. Levers: partial refi + IO -> <= $96,500 (6 mo). Schools 5/3/2 avg 3.33 RED FLAG. Zip 30296 (Fulton/COSF) score 2/5; vacant registry within 30 days; investor-hostile city.

## Listing status (checked 2026-11-17, no RapidAPI)
- Status: **for sale (back on market)**
- Place on the site after PR 367: Relevant / Market
- Ask $119.95k, BRRRR cash flow +$42 in an older model. Back on market; site had said pending.

## Open tasks
- [ ] 

## Links
- Project: [[Deal Pipeline]]
- Market: [[Atlanta]]
- Zip: [[30296]]
- Listing: https://www.realtor.com/realestateandhomes-detail/2295-Bethsaida-Rd_Riverdale_GA_30296_M57982-28943

## Log
Analyses and source files (latest used for the numbers above):
- 2026-11-09 (analysis): `/home/box/shared/deal-outcomes/analyses/2026-11-09/2295-bethsaida-rd-riverdale-ga-30296.md`
- 2026-11-09 (payload): `/home/box/shared/deal-outcomes/analyses/2026-11-09/2295-bethsaida-rd-riverdale-ga-30296.payload.json`
