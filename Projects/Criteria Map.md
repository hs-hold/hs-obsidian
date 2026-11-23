---
type: project
status: active
created: 2026-11-23
updated: 2026-11-23
tags: [project, criteria]
---
# Criteria Map

Read-only mapping of deal criteria as they stand on 2026-11-23. **No business decision is made here.** After the owner chooses the official version on 25 Nov 2026 10:00, internal files may be pointed at that one source; code changes still need a separate PR and merge approval.

Sources opened this turn: [[00 Profile]], `/home/box/shared/agent-rules/deal-analysis.md`, `/home/box/shared/agent-rules/deal-search.md`, [[Deal Pipeline]], `profile.json` of Deal Analysis, Atlanta Market Research, Indianapolis Market Research, and Content Insights, and site code `src/utils/funnel/screen.ts` on `hs-hold/hsdeals-claude-code` (main, read-only via GitHub).

## Comparison

Flip minimum profit
- 00 Profile (standing): ≥ $30k and ROI ≥ 15%, price ≥ 15% below ARV including selling costs; a listing may pass the pre-filter at ask or after about 15–25% off (owner 10 Nov).
- 00 Profile (trial 18–24 Nov): flip profit about $20–25k+.
- deal-analysis.md: profit ≥ $30k after selling costs and ROI ≥ 15%. Trial numbers are not in this file.
- deal-search.md: profit ≥ $30k, ROI ≥ 15%, ≥ 15% below ARV; pass at ask or up to 25% off.
- Deal Pipeline table: profit ≥ $30k and ROI ≥ 15%, price ≥ 15% below ARV.
- profile.json (Deal Analysis, Atlanta MR, Indy MR, Content Insights): $30k profit and 15% ROI language; trial $20–25k is not in these profiles.
- Site pre-screen (`DEFAULT_ASSUMPTIONS` in `src/utils/funnel/screen.ts`): `minFlipProfit: 30_000`, `minFlipRoi: 0.15`. [verified] from main.

Flip discount allowed in the screen
- 00 Profile: about 15–25% off asking for the pre-filter.
- deal-search.md: up to 25% off.
- Site code: `maxDiscount: 0.25` (25% off list). A house is rejected only when both flip and rental rules can be computed and both fail even at that discount. Borderline or incomplete data goes onward, not to a hard reject.

BRRRR / rental
- 00 Profile standing: equity ≥ 15% and ≥ $30k; cash left after a 65% LTV refi ≤ $60k; cash flow ≥ $250/mo; rental screen near the 1% rule.
- 00 Profile trial: 65% LTV refi (30-year, 7.5%), up to $60k own cash left in, cash flow ≥ $250/mo self-managed, 12% reserves; prefer ARV $200–300k; also mark old BRRRR pass/fail; MAO required in every analysis.
- deal-analysis.md: 1% rule on total investment; equity (cash-flip style) ≥ 15% of purchase+rehab and ≥ $30k; cash flow after refinance > $250; primary strategy is BRRRR (owner 12 Nov). Expenses in that file: vacancy 8%, maintenance 5%, capex 5%, no management (self-managed). This does not match the later 12% combined reserves and $150/mo base management in 00 Profile (with auto-adjust to $0).
- deal-search.md: ~1% rule; BRRRR equity ≥ 15% and ≥ $30k; cash left ≤ $60k; cash flow > $250/mo.
- Deal Pipeline table: equity ≥ 15% and ≥ $30k; cash left ≤ $60k; cash flow ≥ $250/mo.
- Site pre-screen: `minRentRatio: 0.01` (1% of purchase + rehab per month); `NEAR_RENT_RATIO = 0.009` (0.9%) still counts as a near pass. The site screen does not apply the $60k cash-in cap, the $250/mo cash-flow test, or the trial $20–25k flip profit. [verified]

Primary strategy
- 00 Profile, deal-analysis.md, Deal Pipeline: BRRRR is primary, flip is secondary (owner 12 Nov).
- Site pre-screen: a listing passes stage 1 if *either* flip *or* near-1% rental clears at list or at the discount. It is a gate into analysis, not the final BRRRR verdict.

Holding costs in the screen
- Site defaults: selling 8%, buy closing 2%, holding $550/mo × 6 months.
- 00 Profile: base flip hold 6 months, 12 months as a stress case; first loan assumptions live in the profile (hard money etc.) and are used in full analysis, not necessarily in this pre-screen.

## What this means (hypothesis, not a decision)
The code pre-screen is aligned with the older written $30k / 15% / 1% rules, not with the 18–24 Nov trial (flip $20–25k, 65% refi, $60k cash-in, $250/mo). That is a plausible reason recent zips produced 0 passes. [hypothesis] Confirm only after the 25 Nov review and, if the owner wants a code change, a dry run on known deals (the five 23 Nov near-misses, Draper, Olive, 2426 E 57th St) before any PR merge.

## Dry-run set (for after 25 Nov, not run as a code change now)
- 2426 E 57th St, 3618 Ferncliff Ave, 5509 S Randolph St, 9926 Montery Rd, 6029 Barth Ave (all REJECT at ask in full analysis, 23 Nov)
- 1613 Draper St, 1733 Olive St
