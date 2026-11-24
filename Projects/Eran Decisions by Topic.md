# Eran — Decisions by Topic (Owner Answers Log)
Method (since 2026-11-24): every answer Eran gives, in any chat or call, is recorded here by topic before moving on. Before asking Eran anything, check this file first; never re-ask a settled item. Close one topic at a time: state → answer → confirm recorded → next. Open and Settled are kept separate. Settled items are append-only; a change supersedes with date.

## OPEN (awaiting Eran)
### Screening / ARV build (work plan: /workspace/exports/arv-fixes-work-plan.txt, proposal: build-and-test-proposal.txt)
- O2 Safety auto-upload blocks stay hard? PARTIAL: auction part answered (S12). Still open: single-comp ARV block, missing-data block.
- O3 Can one super comp override the single-comp ARV block?
- O4 Ingest plausibility ranges (ARV, rehab, rent)
- O5 Calibration on Indy sales only?
- O6 Atlanta rehab ranges
- O7 Fixes for trialMao.ts:90 (holding cost in BRRRR), queueGate.ts:49 (low-confidence hold forever), queueGate.ts:101 (ARV>2x ask treated as error)
- O8 Override limit for bot discretion, and who approves beyond it
- O9 Move deal-engine into git?

## DATA / CHECKS STILL MISSING (not decisions)
- D1 Golden labeled set of real houses (good/bad) for Eran to approve
- D2 20 renovated sales for calibration
- D3 Interior photos for sold comps: 25–37% of Atlanta sold comps have ≤1 photo; interiors and Indy not checked
- D4 School-district source (HomeHarvest nearby_schools was empty; site columns school_district/school_avg source unknown)
- D5 Indy rehab cost table by component
- D6 Tests missing for screen, rehab, queueGate, ingest; CI-on-PR not checked

## DONE TODAY (24.11), nothing built
- Full read of funnel-screen, zillow-search, screen.ts; matches prod after PR 378 → deal-analysis-screening-audit.txt
- Work plan (11 PRs / 4 waves) → arv-fixes-work-plan.txt
- Build+test proposal (6 PRs) → build-and-test-proposal.txt
- ARV tiered design → arv-tiered-design.txt
- Daily quality monitor routine Nov 25–27 20:00
- No code, PRs or deploys today; building awaits the open decisions

## SETTLED
### Build plan (2026-11-24 12:33)
- S10 APPROVED (was O1): merge 11 PRs into 6, in order: safety first (2 PRs, site + engine) → site screening + zillow-search → ARV engine (calibration, tiered ARV, calibration again).
- S12 (O2 partial, 12:34) Auctions: we don't work much with auctions now; an auction is filtered early on the deal-pulling side and never reaches the bot.
- S11 CONSTRAINT: implement or deploy NOTHING until ALL open decisions are collected.
### Screening / ARV (2026-11-24)
- S1 No % pass target; criterion = quality (good deals pass, bad blocked). 11:36
- S2 Indy full cosmetic rehab $25–35/sf, replacing the $55 default. 11:40
- S3 Indy sub-tiers: <25 paint/light; 25 popcorn/doors/sometimes kitchen; 30 with credit incl. kitchen. Starting point only; research rather than guess; decompose into components. 11:41–11:42
- S4 Wide discretion: rules are guidelines; the bot closes open numbers and records reasons. 11:43
- S5 Super comp = near 1:1 comp: ±5y built, same or neighboring street <0.3mi, same school district and amenities, near-same size and layout, sold ≤3 months. Near-miss → "potential super comp" reported to Eran, never decided silently. 11:44–11:45
- S6 Daily quality monitor Nov 25–27, 20:00, read-only. 11:35–11:36
- S8 Stage 13 reserve: fractional buffer per unverified system (1/3–1/2 by age; full gut separate from cosmetic). Eran liked it (11:00–11:03 call). Not approved to build.
- S9 Comp order: best-matching comps first, then less-matching, then adjustments. "Sounds good" (11:08).
- S7 ARV design rules: comp photos mandatory (2–5 best comps); AI judgment gate; output = one number + range; relaxed search 1mi/1y with lowered confidence; clear thresholds; comp order best-first then adjustments. (morning 24.11)
