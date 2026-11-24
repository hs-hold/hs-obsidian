# Eran — Decisions by Topic (Owner Answers Log)
Method (since 2026-11-24): every answer Eran gives, in any chat or call, is recorded here by topic before moving on. Before asking Eran anything, check this file first; never re-ask a settled item. Close one topic at a time: state → answer → confirm recorded → next. Open and Settled are kept separate. Settled items are append-only; a change supersedes with date.

## OPEN (awaiting Eran)
### Screening / ARV build (work plan: /workspace/exports/arv-fixes-work-plan.txt, proposal: build-and-test-proposal.txt)
- (none: all decisions collected 2026-11-24 12:53; data items below still missing)
- (added by brain sync 13:20, from the 13:09 status) Proposal items 15 and 17–21 not yet discussed; presented to Eran 13:09. Item 15 (no screen change before the 25–27 Nov monitor ends) conflicts with the 18:30 build target — needs Eran's decision.

## DATA / CHECKS STILL MISSING (not decisions)
- D1 Golden labeled set of real houses (good/bad) for Eran to approve. STATUS 12:55: acknowledged; pending Eran's review time (he needs to go through several deals). Not approved yet.
- D2 20 renovated sales for calibration (per S18: 20 per region, Indy and Atlanta separately)
- D3 (NEXT after 12:56 pause) Interior photos for sold comps: 25–37% of Atlanta sold comps have ≤1 photo; interiors and Indy not checked
- D4 School-district source (HomeHarvest nearby_schools was empty; site columns school_district/school_avg source unknown)
- D5 Indy rehab cost table by component — STATUS 13:15: research done ([[Indy Rehab Costs]]); awaits Eran's review (kitchen tier ~$36–38/sf vs $30 tier)
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

### Update 24.11 13:02 (calls 623c586a, d4413247)
- Owner instruction: keep documenting everything said from now on, across all calls, nothing omitted.
- D2 count discrepancy: 12:56 said 20 Indy + 20 Atlanta; 13:02 transcript says 10 + 10 (possibly a transcription error). Recorded as 20+20 pending confirmation.
- D3 purpose (owner, 13:02): interior photos of sold comps show what renovation is needed to reach the renovated comp's ARV, and the renovation level wanted. OPEN question: how to handle a comp without photos.
- 13:03 D2 CONFIRMED: 20 Indy + 20 Atlanta (not 10+10). Method decided: do NOT search for them separately; each time the bot analyzes a property, its results (renovated sold comps) are added to the region's calibration list, pending Eran's confirmation they are renovated. Decision only, nothing built.
- 13:04 D3 DECIDED (photo-less sold comp): first infer renovation level from listing description (fully renovated or not) and price position (high/low end of range) and estimate rehab from that. Photos can be found for every comp if searched correctly; the bot must know where to search/pull. If it can't extract this systematically and it truly hurts the analysis, find another photo source. If it happens repeatedly, the bot must notify Eran, who will fix it and find a photo source. Decision only. Remaining for D3: 10-comp Indy visual check (only on Eran's go).
- 13:05 D4 DECIDED (school source): first check whether school data already returns from the API we use or from the site; if yes, use it (school + rating) and compare whether the same schools appear for the subject and the comp. If not, take the ratings of the 3 schools near the property from Zillow, Realtor or similar sites. Decision only.
- 13:07 D5: owner approved deep web research on Indy rehab cost ranges per component (Big 5 + cosmetic, esp. windows), with sources; sent to Indianapolis Market Research. Table to be reviewed by Eran later.
- 13:08 D6 APPROVED: first PR adds tests for screen, rehab calc, queue gate and ingest before any change, and verifies tests run on every PR before merge. Decision only.
- 13:09 BUILD APPROVAL (conditional): when the Indy rehab cost research (item 14) finishes, take its results and start building everything. Eran expects to use the built system at 18:30 today and do the 18:30 checks then. Items 15 and 17-21 still open; item 15 conflicts with the timeline.

### Update 24.11 evening (status, recorded by Grok Bot)
- 13:50 Eran approved: fix conflicts, merge and deploy in order. DONE 14:08: PRs #379–#385 merged (main f77d954), migrations 120000/120100/120200 applied, agent-rules 13cbf90 and deal-engine 99cc589 live. (Supersedes "No code, PRs or deploys today" above.)
- OPEN (awaiting Eran): monthly insurance figure; create GitHub repo hs-hold/deal-engine; ARV gap recs 1 (comp pull pipeline RentCast/HomeHarvest), 3 (low confidence → conservative ARV in analysis), 4 (photo condition as weight; D3 10-comp Indy check on Eran's go).
- 20:03 Eran approved ARV gap recs 2 (ARV −5%/−10% stress test, "thin deal" flag only, no gating) and 5 (card shows worst rehab, MAO at worst, 12-month hold). Building on engine branch + site PR; NOT live until Eran approves.

### Call 24.11 ~20:05–20:11 (voice call 0572ff8c) — rehab method, DECISIONS ONLY (nothing built)
- S29 (closes kitchen-tier question) Indy full cosmetic base rate = exactly $35/sf (not $35.9, not $30): paint, doors, ceilings, new kitchen, new bathrooms. Flexible for very small or very large homes and depends on number of bathrooms.
- S30 Example: 1,200 sf house, full cosmetic = $42,000.
- S31 Big 5 per-item defaults when nothing is known about the house (from the Indy research mids): roof $10k, HVAC furnace+AC $11k, electrical rewire+200A panel $16k, plumbing PEX repipe $7.5k, foundation allowance $8k; +1: water heater $2k, sewer line $8k; windows ~$650 each / $9k default for 12–15 windows.
- S32 Three rough rehab tiers for estimation: cosmetic only ~$42k; cosmetic + Big 5 ~$78k; more broken/older house ~$130k (1,200 sf reference).
- S33 Scaling: cosmetic, roof and windows scale automatically by square footage; electrical, plumbing and foundation are adjustable by house-size range from the research.
- S34 Goal: the system gives estimates that are not far from reality.
- S35 (2026-11-24 ~20:16, voice) ARV stress test (ARV -5%/-10%, thin-deal flag) and the worst-case card (worst rehab + MAO at worst, 12-month flip profit/ROI/MAO, conservative ARV) are DISPLAY ONLY: never used to decide pass/fail and never affect uploading a deal to the site. Eran wants them visible on the website.
- S36 (2026-11-24 ~20:18, voice; UPDATES S5/S13/S28) Super comp criteria: build year within 5 years; less than 1/3 mile; same school zone; square footage within 10%; same bedrooms and same full bathrooms. Recency: sold within the last 3 months = full super comp, may serve as a single comp. Sold 3–6 months ago = very high weight in the ARV calculation but can NOT be a single comp. Settles the open question on the definition of near-same size.
- S37 (2026-11-24 ~20:19, voice) Single-pull property profile rules: (1) the site does ONE pull and the bot receives ONE ready file; from it the bot may use school rating, finished factual data, and the asking price. (2) Any calculated numbers in the file (rent estimates, ARV, Zestimate/rentZestimate or similar) must NEVER be used by the bot in any form; the bot derives those itself with its own methods. (3) Audit the bot's current code and rules for accidental use of such numbers and report violations; no behavior change beyond logging until Eran approves.
  - S37 amendment (~20:20): Zestimate / any Zillow estimate / rentZestimate explicitly forbidden, alongside rent estimates and ARV.
- S38 (2026-11-24 ~20:21, voice; CLOSES open question 'does a single super comp raise confidence') A single super comp (per S36) raises ARV confidence to MEDIUM. If it is truly near-identical one-to-one across many parameters, it raises confidence to HIGH.
- S37 refinement / S39 (2026-11-24 ~20:24, voice) The three numbers REHAB (renovation cost), ARV and RENT are always calculated by the bot itself using all its knowledge. The bot must never use any of these three as received from the site's pulled data (site screen ARV/rehab/rent/maxOffer, Zestimate, rentZestimate, AVMs, etc.).
- S40 (2026-11-24 ~20:24, voice; CLOSES 'needs-verification blocking scope') Deals with high potential but missing or inaccurate details are NOT blocked: they upload to a NEW site page placed below Grok Analytics, named 'Deals that maybe work' (עסקאות שאולי עובדות), showing which details are missing, with a button to mark the info as completed that moves the deal into Grok Analytics. Decision only, not built.
- S41 (2026-11-24 ~20:24, voice) Grok Analytics deals list: add date filtering (default newest first) and sorting by several sensible parameters such as upload date, deal quality and profitability. Decision only, not built.
