---
type: deal-batch
market: Indianapolis
created: 2026-11-28
updated: 2026-11-28
tags: [deal, batch]
---
# 2026-11-28 Indy IWB weekly (4)

Source: [[Invest With Ben]] weekly inventory email (Claire & Shannon, msg 1a21f3cee50efffa, 01:00 Israel 28 Nov). [[Deal Inbox]] 08:00 scan sent the 4 buy-box Indy addresses to [[Deal Analysis]] (handoff `/home/box/shared/deal-outcomes/deal-analysis-handoff-2026-11-28.md`); site entry by Deal Inbox failed (SUPABASE_ACCESS_TOKEN missing in that run). Summary `/home/box/shared/deal-outcomes/analyses/2026-11-28/funnel-iwb/SUMMARY.md`. Research only, nobody contacted. Wholesaler ARVs not used.

| House | Ask / wholesaler ARV | Engine ARV (comps) | Verdict ask / 15% off | goodPotential | Site |
|---|---|---|---|---|---|
| [[3457 N Hartman Dr]] | $94.9k / $160k | $148.2k (3, medium) | FAIL / FAIL | TRUE (thin rent) | not posted |
| [[4726 Stratford Ave]] | $79.9k / $175k | $161.0k (2, medium) | FAIL / **PASS (trial)** | TRUE (borderline) | **posted 10:29, passed, 7e323777** |
| [[332 N Fleming St]] | $62.9k / $160k | none (0) | INCOMPLETE | FALSE | not posted |
| [[2116 N Arlington Ave]] | $99.9k / $170k | $113.6k (1, very low) | FAIL / FAIL | TRUE (fails all else) | not posted |

- Rules applied after the owner's 27 Nov complaint: zip-note hard boundaries as geometry (Pendleton Pike, Washington St, interstates, rail, township/school corp); wider-GLA tier OFF (local patch, shared engine untouched); fallback only on zero strict survivors; road class (Indy GIS) checked for subject and comps; listing history looked up (HomeHarvest had none; IWB dates only).
- [reported] Tax district 701 conflict: engine says IPS, `districts.md` says MSD Warren, Census says IPS — owner to confirm canonical source.
- Outside buy box in the same email (Deal Inbox, no reply): Bloomington 4416 E Clayton Ct, Kokomo, Martinsville ×2, South Bend, Greenwood, 46250 condo (6404 Bayside S Dr), 46214, 46227, 46220.
- Run logs `/home/box/shared/deal-engine/reports/runs/2026-11-28/`; calibration rows added to `deal-engine/data/calibration/indy.jsonl` (not committed).
- Open items: OI-GOODPOT-2811, OI-IWB-2811.
- Drive: [אינדי IWB — 4 נכסים (28.11.2026)](https://docs.google.com/document/d/1YSxzb5-sy2BxBg5uX00RosY9vDO1uE9A0IMN6YSV8T0/edit)
