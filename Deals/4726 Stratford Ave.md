---
type: deal
address: "4726 Stratford Ave, Indianapolis, IN 46201"
zip: "46201"
market: Indianapolis
strategy: brrrr
status: passed
list_price: 79900
arv: 161000
rehab: 46700
rent: 1462
source: "Invest With Ben weekly inventory 27 Nov (msg 1a21f3cee50efffa); Deal Inbox 08:00 scan 28 Nov"
created: 2026-11-28
updated: 2026-11-28
tags: [deal]
---
# 4726 Stratford Ave, Indianapolis, IN 46201

Market: [[Indianapolis]] · Zip: [[46201]] · Batch: [[2026-11-28 Indy IWB weekly (4)]] · Wholesaler: [[Invest With Ben]]

- [reported] 2026-11-28 ~08:50 Israel ([[Deal Analysis]], IWB funnel): IWB weekly inventory (msg 1a21f3cee50efffa), status Reduced (sight-unseen offers considered). Cash ask $79,900 OBO (land contract $137,900 / $21,000 down); wholesaler ARV $175k (not used). 3bd/1ba, 1,512 sf listed (official GLA 792), 1944, basement, 1-car garage, lot 6,665 sf, vacant. Walkthrough TBD, deadline 24h after, COE 9 Dec.
  - Engine ARV $161.0k (conservative $151.4k) from 2 comps (4730 Stratford super comp $165k, 4927 Diana $162k), medium. Rehab MID $46.7k. Rent $1,462 (6 comps).
  - Trial CF at ask $292, $60.0k left in. **Trial PASS at 15% off ($67.9k): CF $388, $60k in, flip +$26.3k.** MAO trial $73.8k (7.6% off), BRRRR $64.3k (19.5%), flip $55.9k (30%).
  - **Verdict: FAIL at ask / PASS at ≤15% off (trial only) — conditional lead.** Engine block `arv_over_2x_ask_unsupported` (ARV 2.01× ask); rehab tier `needs_owner_decision` (kitchen_30 at 792 sf); GLA conflict 792 vs 1,152/1,512 (1,152 scenario: ARV $130.8k, MAO $35.2k). Sensitivity: ARV $151.4k → MAO $65.4k (18.1% off); rent $1,300 → CF $150. Schools 2.00 (alert).
  - **goodPotential = TRUE** (borderline).
  - [verified file] POSTed to the site 2026-11-28 10:29 Israel: HTTP 200, outcome **passed**, dealId 7e323777-0939-4571-9977-4c1655d370a0 (`4726-stratford-ave-indianapolis-in-46201.post_result.json`), consistent with the 15% upload rule. Poster not named in the file.
  - Open owner decisions: rehab tier, ARV>2× block, GLA basis (792 vs 1,152).
  - Full write-up: `/home/box/shared/deal-outcomes/analyses/2026-11-28/funnel-iwb/4726-stratford-ave-writeup.md`
  - [verified per Grok Bot chat] 2026-11-28 13:24 follow-up: Deal Analysis called the 15%-off PASS **uncertain** (fails at 1,152 sqft; ARV >2× ask guard flagged; sqft sources 792 / 1,152 / 1,512). 10:13 Eran asked what the site problem was (Deal Inbox lacked a Supabase token); 10:24–10:29 Grok Bot, with a new token from Eran, created the deal on the site and Deal Analysis posted the analysis with caveats visible. Deal Inbox draft to IWB asking the true sqft awaits Eran's approval (OI-IWB-2811).
