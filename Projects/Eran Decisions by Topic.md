# Eran — Decisions by Topic (Owner Answers Log)
Method (since 2026-11-24): every answer Eran gives, in any chat or call, is recorded here by topic before moving on. Before asking Eran anything, check this file first; never re-ask a settled item. Close one topic at a time: state → answer → confirm recorded → next. Open and Settled are kept separate. Settled items are append-only; a change supersedes with date.

## OPEN (awaiting Eran)
### Screening / ARV build (work plan: /workspace/exports/arv-fixes-work-plan.txt, proposal: build-and-test-proposal.txt)
- (none: all decisions collected 2026-11-24 12:53; data items below still missing)

## DATA / CHECKS STILL MISSING (not decisions)
- D1 Golden labeled set of real houses (good/bad) for Eran to approve. STATUS 12:55: acknowledged; pending Eran's review time (he needs to go through several deals). Not approved yet.
- D2 20 renovated sales for calibration (per S18: 20 per region, Indy and Atlanta separately)
- D3 (NEXT after 12:56 pause) Interior photos for sold comps: 25–37% of Atlanta sold comps have ≤1 photo; interiors and Indy not checked
- D4 School-district source (HomeHarvest nearby_schools was empty; site columns school_district/school_avg source unknown)
- D5 Indy rehab cost table by component
- D6 Tests missing for screen, rehab, queueGate, ingest; CI-on-PR not checked

## DONE TODAY (24.11), nothing built
- Full read of funnel-screen, zillow-search, screen.ts; matches prod after PR 378 → deal-analysis-screening-audit.txt
- Work plan (11 PRs / 4 waves) → arv-fixes-work-plan.txt
- Build+test proposal (6 PRs) → build-and-test-proposal.txt
- ARV tiered design → arv-tiered-design.txt
- Daily quality monitor routine Nov 25–27 20:00
- One-off reminder today 18:30 (D1 labeled set + D2 20 renovated sales per region)
- Full call record 12:30–12:56: Projects/Eran Status 2026-11-24.txt
- No code, PRs or deploys today; building awaits the open decisions

## SETTLED
### Build plan (2026-11-24 12:33)
- S10 APPROVED (was O1): merge 11 PRs into 6, in order: safety first (2 PRs, site + engine) → site screening + zillow-search → ARV engine (calibration, tiered ARV, calibration again).
- S12 (O2 partial, 12:34) Auctions: we don't work much with auctions now; an auction is filtered early on the deal-pulling side and never reaches the bot.
- S13 (O2 partial + O3, 12:35) The single-comp ARV block may be overridden when that comp is a super comp (per S5). A "potential super comp" is reported to Eran and does not override automatically (confirmed by S28).
- S14 (12:35, addition to S13) Even a non-super single comp with HIGH confidence can serve as a very good indication. When suitable comps are lacking, always pull 1–2 additional comps even if they differ in size and lot area.
- S15 (12:37) Bathroom adjustment values stay exactly as in today's engine code, no changes: Indy 1→2 full bath $9,000 (comp median <$250k) / $12,000 (≥$250k); 3rd+ full bath $4,000/$6,000; half bath $4,000/$6,000 with 1 full, $3,000/$4,500 with more; missing bath count assumed 1. Atlanta: full bath = 5% of comp price, min $8,000 max $30,000; half bath = half of that.
- S16 (12:40, closes O2 entirely) Missing data: if the bot cannot close a field it must make an effort to close it; if it still cannot, it gives an estimate and marks the field as uncertain. On the site, wherever that field is shown, it must be visible to Eran that the data needs verification.
- S17 (12:42, closes O4) No fixed numeric plausibility ranges (proposed ARV $40k-1.5M / 0.5-3x ask, rehab ≤$250k / ≤$120/sf, rent $500-6,000 are REMOVED). Instead the bot itself judges whether the numbers look reasonable; if clearly unreasonable it researches the real numbers; if still unresolved it notifies Eran in chat.
- S18 (12:44, closes O5) Calibration runs SEPARATELY per region: one calibration for Indianapolis and one for Atlanta, each with its own 20 renovated sales and its own coefficients. Never merged. (Supersedes a same-minute statement that it is combined.)
- S19 (12:45, addition to S18) Whenever verified data becomes available (Eran's own closed deals or authenticated market data), it is entered into the relevant region's calibration. Implemented in code, without AI, and recorded in the code going forward (ongoing per-region calibration).
- S20 (12:46, closes O6) Atlanta rehab: research Atlanta cosmetic rehab costs, decompose into components like Indy, and build an Atlanta range and tiers similar to Indy's ($25-35/sf with tiers). DECISION ONLY (12:46 correction): no research run, no code, no implementation or deploy until ALL decisions are collected (S11).
- S21 (12:47, O7 part) APPROVED: replace fixed $550/month holding cost in BRRRR cash flow (trialMao.ts:90) with the property's actual tax and insurance.
- S22 (12:47, new requirement) Since deals reaching the site pass through the Deal Analysis bot, the bot must know all the data parameters the site needs completed, and record all relevant deal-analysis parameters for the site far more realistically and accurately. Addition to the bot's deal-analysis behavior. Decision only, nothing built yet.
- S23 (12:48, O7 part) ARV > 2x ask (queueGate.ts:101): mark instead of stop. If more than one comp supports the high ARV it may be real and the deal must not be missed; the bot checks for supporting comps before flagging.
- S24 (12:49, closes O7) Low confidence: the bot tries to raise confidence. If it suspects a deal is bad, it moves on. If it has low confidence that a deal is good, it pulls more information to decide. If all findings say good but info is still missing to confirm, it tells Eran so he can verify. Eran strongly prefers the bot obtains the missing info itself. Addition 12:50: when unsure, the bot actively pulls additional comps and performs additional comp adjustments to raise confidence.
- S25 (12:51, closes O8) Bot override limit = 70% deviation from the bot's own deal-engine number (not 30%). Under 70%: the bot's number stands, recorded with reason and evidence. Over 70%: if confidence is high the bot approves it itself; if confidence is low it notifies Eran.
- S26 (12:52, closes O9) The deal engine moves to GitHub as the primary place for all work: every change, build and history happens there; GitHub is the source of truth, accessible from anywhere without depending on a machine. A backup copy stays on the computer. (Verified: the engine currently sits at /home/box/shared/deal-engine on the bots' shared computer, not Eran's Mac.) Decision only; nothing moved yet (S11).
- S27 (12:53, closes O10, last open decision) Lot size: the bot uses calibration and judgment. An extremely different lot = don't take the comp at all. A similar house with a lot only 1.5-2x larger can still be suitable. Bot discretion.
- S28 (12:54, refines S5/S13) A super comp sold in the last 3 months, with nearly the same build year and the same building type, can override the single-comp block and be used as a single comp, but only if it truly meets these criteria. Hence a potential super comp (near-miss) does NOT override (confirms the inference in S13).
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
