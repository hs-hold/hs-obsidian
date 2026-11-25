---
type: project
status: active
created: 2026-11-23
updated: 2026-11-25
tags: [project, tracker]
---
# Open Items

Single tracker for open decisions and tasks. Fields: id, topic, owner agent, status, updated, next action, needs-owner-approval, source. History is kept at the bottom. Do not close an item without verification. Populated by the existing 13:00 / 23:00 sync — no new routine.

Status values: open, waiting-owner, waiting-verification, prepared, blocked, closed.

## Open

### OI-M10 — Sync time 23:00 vs 23:30
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner decides whether documentation and/or the evening routine should be 23:00 or 23:30
- Needs owner approval: yes
- Source: [[00 Profile]] (writes 13:00 and 23:30, original request 17 Nov); running brain-sync routine and `_system/scripts/README.md` use 13:00 and 23:00; last successful midday sync 2026-11-23 13:20 IST
- Notes: [verified] The 23 Nov upgrade must not change this decision. The running 23:00 routine was left untouched, and docs were not aligned to 23:00.
- Notes: raised in 25 Nov review, no answer yet.

### OI-C-WATCH — Widen and verify the Indy broker reply watch
- Owner agent: Grok Bot
- Status: waiting-verification
- Updated: 2026-11-25 11:20
- Next action: coordinator already applied the widened watch prompt (old prompt + schedule snapshotted under `/home/box/shared/backups/2026-11-23/routine-snapshots/`; schedule unchanged 09/15/21). Eight "send now" specialist messages were sent (priority false); Deal Inbox and Indy Research were told to keep reporting until verification. A read-only dry run of checklist items 1–9 on 23 Nov 14:15 Israel **passed** (report: `artifacts/e-watch-verification-dry-run-2026-11-23.md`). No A/B/C subject gap. C-4 stop-reporting messages are still **not** sent — coordinator sends them after accepting this dry run, then watches one cycle for duplicate reports. Do not disturb the Steele 16:00 send or the Nolan 18:00 call.
- Needs owner approval: no
- Source: `/home/box/shared/indy-trip/broker-replies-log.md`; artifacts in `/home/box/shared/backups/2026-11-23/artifacts/`
- Notes: 25 Nov 11:20 Israel full read-only Gmail audit (`deals@`, `after:2026/11/20`, `includeSpamTrash: true`) verified inventories A (30), B (17), C (5), Nov 23 32-broker batch, Cole Cooper, Scheetz Day 1 (Kristen Yazel & Rhonda Krebs), and Trading Post hard bounce; all deduped by Message ID in `/home/box/shared/indy-trip/broker-replies-log.md`. Found & logged previously unlogged Paul Scherrer / Welton Li intro thread (`1a20eaab39ad7504`, subject `"Paul / Eran Introduction - Indianapolis Real Estate"`) and Nolan deal-example outbound thread (`1a209d99d21b1e33`). Reported routine-prompt gaps to parent (subject filter misses Cole Cooper & Paul Scherrer; 25-msg pagination / GitHub noise; never send emails). Waiting on parent to update routine prompt.

### OI-STEEL-EMAIL — Steele call-request email
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-23 23:20
- Next action: [verified] sent 16:05 Israel (09:05 Indy) from deals@ in-thread. Steele replied 20:05 (after call with Tal): will add Tal to wholesaler lists; proposes Tue 1 Dec 10:00 ET. Continues in OI-INDY-TUE-MEETINGS.
- Needs owner approval: no for the already-approved send; yes for any new commitment
- Source: [[Steele Kruzel]], thread 1a1ff4e4244967dd


### OI-NOLAN-CALL — Tal / Nolan call
- Owner agent: Grok Bot (coordinate only; Tal calls)
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: Nolan accepted the invite (16:09) and wrote 18:49: thanks for the ZIPs, asks for an example recent deal Tal wants to repeat (purchase price, rehab scope/cost, sale or refi result). Only the partners know these numbers. Owner 21:05: do not reply for now.
- Needs owner approval: no
- Source: [[Nolan Lamkin]], thread 1a1ff1abd91802e5, event on deals@ calendar
- Notes: 25 Nov voice review — skip for now, Tal and Eran handle this; leave open.

### OI-BOUNCE — Bounced intro recipients
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner chooses for KK Buys / Stacy Patlan (Tal calls, or new emails + approved resend). New 23 Nov: the 32-broker batch from Indy Research had 2 hard bounces (550 5.1.1): Jared Nelson jnelson@jnandarealty.com, Nicole Lloyd nicole@indyspropertyshop.com. Delay (not bounce) to salesteam@indytradingpost.com. 24 Nov 00:31 Israel: second delivery-delay notice to salesteam@indytradingpost.com (msg 1a20a88d925d75f1); Gmail retrying 18 h; still not a final bounce.
- Needs owner approval: yes
- Source: broker-replies-log.md; [[Indy Trip Nov 2026]]
- Notes: 25 Nov voice review — skip for now, Tal and Eran handle this; leave open.

### OI-CRITERIA — Trial criteria review 25 Nov
- Owner agent: Grok Bot / Deal Analysis
- Status: waiting-owner
- Updated: 2026-11-25
- Eran clarification (voice, 25 Nov ~10:58) [decision]: $250/mo cash flow = a deal fully passes and works as full BRRRR. Separately, any deal with cash flow above $100/mo is flagged as good potential and reported to Eran immediately even if it misses $250 (rule in agent-rules/deal-analysis.md, 703c705). Still open: keep trial method / return to old / combine (comparison sent 25 Nov 10:04).
- Next action: review 25 Nov 2026 10:00 Israel. Mapping of current contradictions is in [[Criteria Map]]. No business criteria will be changed before this decision. After the decision, internal docs may be updated to the approved version; code, merge, and deploy still need a separate batch approval. 24 Nov: the screening/ARV decisions (S1–S28) were collected in the 24 Nov call; review still 25 Nov 10:00. Note item 15 (no screen change before the 25–27 Nov monitor ends) conflicts with the 18:30 build timeline — owner decision needed.
- Needs owner approval: yes
- Source: [[00 Profile]] trial block 18–24 Nov; [[Criteria Map]]; [[Eran Decisions by Topic]]
- Notes: raised in 25 Nov review; $250 / >$100 clarification logged, method choice (trial / old / combine) still pending.

### OI-OFFERS — Offers submitted this week
- Owner agent: Grok Bot / מזכירה
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner to state how many offers were submitted (asked in weekly metrics)
- Needs owner approval: yes (the number comes from the owner)
- Source: [[Metrics]]
- Notes: raised in 25 Nov review, no answer yet.

### OI-SKILLS — Seven skill proposals
- Owner agent: Grok Bot / Content Insights
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner approves, drops, or revises each proposal. Summary: `_system/reports/2026-11-23-skill-proposals-summary.md`. Do not implement any skill without approval. Proposal 3 (call scripts) was already dropped for Tal's trip.
- Needs owner approval: yes
- Source: `/home/box/shared/skills-proposed/`
- Notes: raised in 25 Nov review, no answer yet.

### OI-MERGE-BATCH — Next merge/deploy batch
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-23 23:20
- Next action: [verified] 17:05 PRs 370/376/377 merged + deployed (209 tests, migration applied); see Decisions Log 2026-11-23 16:27. A next batch would be a new item.
- Needs owner approval: yes
- Source: [[Deal Pipeline]], [[Deals Site]]


### OI-SITE-UPLOAD — Five 23 Nov analyses not on the site
- Owner agent: Deal Analysis
- Status: closed
- Updated: 2026-11-23 23:20
- Next action: [stale 2026-11-23] all five near-misses REJECT well beyond 15% off ask (e.g. 2426 E 57th St MAO 43.7% below ask); under the 20:50 upload rule they do not qualify. Nothing to upload.
- Needs owner approval: yes
- Source: [[2026-11-23 Indy extra search near-misses (5)]]


### OI-OFFMARKET — Off-market lead scope
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner decides scope, runner, and budget of the off-market-lead-generation proposal. Reminder already delivered 22 Nov.
- Needs owner approval: yes
- Source: [[off-market-lead-generation]], [[Indy Trip Nov 2026]]
- Notes: raised in 25 Nov review, no answer yet.

### OI-DAILY-FUNNEL-ROUTINE — Daily funnel-run-next-zip routine
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: create only after approval (was pending)
- Needs owner approval: yes
- Source: [[Deal Pipeline]]
- Notes: raised in 25 Nov review, no answer yet.

### OI-TRIP-FLIGHTS — Tal's exact flight dates
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner confirms flight dates
- Needs owner approval: yes
- Source: [[Indy Trip Nov 2026]]
- Notes: raised in 25 Nov review, no answer yet.

### OI-SQ-MEETUP — Simple Quarters meetup 25 Nov
- Owner agent: Indianapolis Market Research
- Status: open
- Updated: 2026-11-25
- Next action: confirm whether the meetup runs on Thanksgiving eve
- Needs owner approval: no for the check; yes before any contact
- Source: [[Indy Trip Nov 2026]]
- Notes: 25 Nov voice review — skip for now, Tal and Eran handle this; leave open.

### OI-BIGGERPOCKETS — Secretary holds BiggerPockets reminder
- Owner agent: מזכירה
- Status: quiet standing reminder (owner decision 2026-11-23 16:26)
- Updated: 2026-11-23
- Next action: keep stored silently; do NOT surface proactively, in open-item lists, digests or notifications; mention only if the owner raises it
- Needs owner approval: no
- Source: [[2026-11-23]]


### OI-EDWIN-1621 — Edwin reply on 1621 E 46th St (subject-to)
- Owner agent: Deal Inbox
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: Edwin (19:08) reached ~$155k (our 19 Nov offer) with ~$12k entry; vacant, seller wants fast close; asks if we pay broker commission + his $3k fee and closing time; still missing rate/loan type and whether the contract is direct with the seller. Deal works to ~$164.8k all-in. Draft is in the Deal Inbox chat awaiting owner approval; nothing sent.
- Needs owner approval: yes
- Source: [[1621 E 46th St]], Grok Bot chat 19:08–19:22
- Notes: raised in 25 Nov review, no answer yet.

### OI-INDY-TUE-MEETINGS — Tue 1 Dec Indy meetings (Zac 9:00, Steele 10:00)
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: Steele proposes Tue 1 Dec 10:00 ET (17:00 Israel), no place; Zac Canull offers coffee Tue 9:00/9:30 ET; Cole moved to LIV Indy (colecooper@livindyrealty.com). Owner 21:05: "דואגים להכל, אל תענה לאף אחד כרגע" — no replies/drafts until the owner says. 24 Nov: Steele (23:18 Israel, 23 Nov) forwarded Tal's intro to local wholesalers and recommended the Invest With Ben opt-in list; Cole Cooper intro sent from deals@ 00:21 Israel 24 Nov (awaiting reply). Hold still in force; no replies drafted.
- Needs owner approval: yes
- Source: broker-replies-log.md (21:05 run); [[Steele Kruzel]]; [[Indy Brokers]]; [[Invest With Ben]]
- Notes: raised in 25 Nov review, no answer yet.

### OI-SITE-DISCOUNT-LABEL — Show "works at discount" on the site
- Owner agent: Grok Bot
- Status: prepared
- Updated: 2026-11-25
- Next action: Cedar Pine / Park Stream appear "rejected" on the site because they fail at ask. Offered a small PR (20:56); no answer yet.
- Needs owner approval: no (approved on 25 Nov voice review; PR merge/deploy remains gated)
- Source: Grok Bot chat 20:56
- Notes: Eran approved small site fix on 25 Nov voice review. Cloud-agent brief for hs-hold/hsdeals-claude-code (site only, TypeScript, never touch engine/, 15% "Works with discount" label instead of Rejected/Near miss) prepared and returned to coordinator to launch.

### OI-V3-RECHECK — v3 re-run contradicts 20:56 uploads
- Owner agent: Deal Analysis
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: [reported, files] engine v3 research re-run (~21:44–23:10) shows 1318 Bacon St FAIL at ask and 15% off, 10160 Park Stream FAIL at both, 3667 Cedar Pine PASS at 15% off. Reconcile which verdict stands and whether Bacon / Park Stream stay on the site; tell the owner.
- Needs owner approval: yes for removing anything from the site
- Source: /home/box/shared/deal-engine/reports/2026-11-23-rerun/summary.md; /home/box/shared/deal-outcomes/analyses/2026-11-23/rerun-v3/REPORT.md
- Notes: 25 Nov voice review — Eran decided to remove all three (1318 Bacon St, 10160 Park Stream Dr, 3667 Cedar Pine Pl) from the site. Verified via read-only `deal-analysis-ingest?resolve=` that all three remain in `deals` (`analysis_source: deal analysis bot`), even though `post_results.json` (Nov 23) already posted `outcome: rejected`. `deal-analysis-ingest` has no delete/hide endpoint and `classifyAnalyst` uses a 25% band ignoring `outcome`, so Park Stream (21.2% off) and Cedar Pine (0.4% off in DB; 17.0% off after Nov 24 S44 $20K bath update) still render on Relevant. Removal requires either a direct Supabase DB write (delete/un-source the 3 rows on `ywvdyogbdptfyclgjbpf`) or a site-code filter/15%-band change; nothing modified directly.

### OI-REPO-TEMPLATES — Templates from hoangtng/real-estate-agents
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: owner decides which template adaptations to apply (market report template, analysis output/offer brief, contract timeline/disclosures, tenant screening later). No new bot. Nothing built.
- Needs owner approval: yes
- Source: Grok Bot chat 21:15
- Notes: raised in 25 Nov review, no answer yet.

### OI-1830-CHECKS — 18:30 owner checks (labeled set + calibration sales)
- Owner agent: Grok Bot
- Status: waiting-owner
- Updated: 2026-11-25
- Next action: one-off reminder today 18:30 Israel. D1: golden labeled set of good/bad houses for Eran to approve (not prepared yet). D2: 20 Indy + 20 Atlanta renovated sales (confirmed 13:03), collected from each bot analysis rather than a separate search, pending Eran's confirmation they are renovated.
- Needs owner approval: yes
- Source: [[Eran Decisions by Topic]] D1/D2
- Notes: raised in 25 Nov review, no answer yet.

### OI-ATL-REHAB-RESEARCH — Atlanta cosmetic rehab research (S20)
- Owner agent: Atlanta Market Research
- Status: in-progress
- Updated: 2026-11-25
- Next action: [decision] 12:46 research Atlanta cosmetic rehab by component and build Atlanta range + tiers like Indy. Recorded as decision only; not dispatched yet (S11 constraint was lifted at 13:09 for the build, but Atlanta research was not explicitly sent).
- Needs owner approval: no (decided)
- Source: [[Eran Decisions by Topic]] S20
- Output: `/home/box/shared/atl-rehab-costs/`
- Notes: 25 Nov — dispatched to Atlanta Market Research; in progress.

### OI-SECRETARY-SYNC — reconcile מזכירה task list with reality, then auto-update
- Owner agent: Grok Bot
- Status: open
- Updated: 2026-11-24 23:15
- Next action: Grok Bot reviewing the 34 items against vault/mail evidence (first pass read-only); show Eran the list before changing anything; then build automatic closing of evidenced items.
- Needs owner approval: yes (before updating the list / new routine)
- Source: owner chat t830u 23:09; [[מזכירה]]

## History (closed, keep)
### OI-TIMEOUT — Timeout advances the next zip
- Owner agent: Grok Bot (cloud agent may open a PR)
- Status: closed
- Updated: 2026-11-25
- Next action: [verified] timeout fix deployed 17:05 and returned the new retry_later contract live; 46236 still had 5 rows unscreened (HTTP 546) — confirm on next daily runs that the same zip is retried.
- Needs owner approval: yes for merge/deploy/live test; PR preparation is in the approved plan
- Source: `supabase/functions/funnel-run-next-zip/index.ts` (retry_later sets pull_retry_after and returns nextZip); [[Deal Pipeline]]
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-DROPPED-AUDIT — Audit deals dropped for missing ARV/API data
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: partly done 23 Nov: 5-property blind check and Indy 20-property filter audit (rejects correct; hold rules hide deals). Remaining: audit of items dropped for missing ARV/API data (needs_comps).
- Needs owner approval: no to start after the precondition; report results
- Source: [[Deal Pipeline]]
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-ZIPINTEL-GAPS — Zip intel files still missing
- Owner agent: Zip Intel
- Status: closed
- Updated: 2026-11-25
- Next action: notes still missing for 46107, 46113, 46142, 46143, 46168, 46214, 46229, 46236, 46239 (checked on disk 2026-11-23). 46112, 46123, and 46140 exist.
- Needs owner approval: no
- Source: `/home/box/shared/zip-intel/`
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-LOG-SYNTAX — 22 Nov "log write syntax error"
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: [verified] not found in vault, shared files, the audit text, Deal Inbox transcript, or this helper's session. The main Grok Bot transcript is still not searchable from the executor. Coordinator can close this if a search of the main chat also finds nothing; otherwise leave open only if the main chat has a hit.
- Needs owner approval: no
- Source: agent audit 23 Nov; rechecked 23 Nov 14:15
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-46168-QUEUE — Two 46168 passes not yet analysed
- Owner agent: Deal Analysis
- Status: closed
- Updated: 2026-11-25
- Next action: 605 S East St and 4099 N Cheltonham Ct (Plainfield) passed the 17:05 re-pull and wait in the queue; confirm they reach Deal Analysis.
- Needs owner approval: no
- Source: [[Decisions Log]] 2026-11-23 16:27
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-ATL-DEALS-1124 — Five Atlanta Deal Inbox analyses (24 Nov) not posted
- Owner agent: Deal Analysis
- Status: closed
- Updated: 2026-11-25
- Next action: analyzed but not posted because the Indy-only trial was in force (owner 10:00 check-in outcome not found in files). Verdicts: 7604 Briar Crest Ct REJECT at ask (trial ~$138k = 7.1% off only on a single-comp ARV; conservative needs ~17% off); 5472 Forest East Ln (subject-to) REJECT as cash, tight sub-to; 342 Trilby Pl SE REJECT (flip pass rests on one stretched comp); Lithonia 30058 and Decatur 30032 New Western INCOMPLETE (no address). Owner decides on Atlanta posting; Briar Crest is the only one inside the ≤15% band and only on the low-confidence engine ARV.
- Needs owner approval: yes
- Source: /home/box/shared/deal-outcomes/analyses/2026-11-24/SUMMARY.md
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-VAN-SPRONSEN — 12428 Van Spronsen Way (46236) not analysed
- Owner agent: Deal Inbox / Deal Analysis
- Status: closed
- Updated: 2026-11-25
- Next action: Invest With Ben marketing email 01:00 Israel 24 Nov (3/2, 1,440 sf, 1991, vacant). Not in the 08:00 handoff; confirm whether it goes to Deal Analysis.
- Needs owner approval: no
- Source: [[Invest With Ben]]; broker-replies-log.md 09:49
- [stale] 2026-11-25: not relevant per Eran voice review.

### OI-FRANKLIN-OFFER — 303 N Franklin Rd offer decision
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25 10:58
- Evidence: Eran on voice call 25 Nov ~10:58 Israel: ignoring this deal for now; no offer, no reply. Mark done.
- Source: [[303 N Franklin Rd]]; [[Steele Kruzel]]

### OI-AVON — Two sent-but-unanalysed Avon items
- Owner agent: Deal Analysis
- Status: closed
- Updated: 2026-11-25
- Next action: owner yes/no on analysing 7228 Lockford Walk N and 1881 Wynnewood Ln. Recommendation on file: no
- Needs owner approval: yes
- Source: [[Deal Pipeline]]
- Evidence: [verified] 2026-11-25: skipped by Eran on 20 Nov 2026 10:02 (Deal Analysis transcript) — do not analyse or upload 7228 Lockford Walk N or 1881 Wynnewood Ln; leave them 'sent'. Source: secretary-tasks-reconcile-24-11.txt.

### OI-TAX-ENGINE — Engine tax-change proposal
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: owner yes/no
- Needs owner approval: yes
- Source: [[Deal Pipeline]]
- Evidence: [verified] 2026-11-25: S21 live — PRs 381/388. PR 381 (actual tax + insurance instead of $550) was in the 24 Nov 14:08 deploy; PR 388 (insurance template) merged 20:46 (100c951). Decisions Log 24 Nov 13:50/14:08 and 20:46.

### OI-HOLD-RULES — Screen hold rules hide workable deals
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: owner asked for conclusions + proposal, "אל תעשה כלום עדיין" (20:46). Proposal to present: revisit low-comps, ARV>2x price and basement-unknown holds (send to full analysis instead of holding). Also pending: whether Atlanta moves to the Indy ARV method (decide after conclusions). [decision] 24 Nov 12:40–12:53 call partly resolves this: ARV>2x ask → mark, don't stop (S23); missing data → estimate + 'needs verification' marker (S16); single-comp block overridable only by a true super comp (S13/S28). Implemented only via the OI-ARV-BUILD PRs.
- Needs owner approval: yes
- Source: /home/box/shared/deal-outcomes/filter-audit/2026-11-23-indy-20/; [[Eran Decisions by Topic]]
- Evidence: [verified] 2026-11-25: S16/S23/S24 live 14:08 on 24 Nov 2026 (PRs 381 and 385). ARV>2x is a flag not a stop; low-confidence goes to the bot; unverified fields are marked on the site. Decisions Log 24 Nov 14:08.

### OI-ARV-BUILD — 6-PR screening / rehab / ARV build
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: [decision] 13:09 owner: when the Indy rehab research (D5) finishes, take its results and start building everything; he expects to use the built system at 18:30 today. D5 research returned 13:15 ([[Indy Rehab Costs]]). Order (S10): tests-first PR + CI on every PR (S6/D6) → safety (site + engine) → site screening + zillow-search → ARV engine (calibration, tiered ARV, calibration). Still open: items 15 and 17–21 not yet discussed; item 15 conflicts with the 18:30 timeline. Merge/deploy only with owner approval. Fresh cloud agent per PR (owner rule).
- Needs owner approval: yes (items 15, 17–21; merge/deploy)
- Source: [[Eran Decisions by Topic]]; Projects/Eran Status 2026-11-24.txt; /workspace/exports/build-and-test-proposal.txt, arv-fixes-work-plan.txt
- Evidence: [verified] 2026-11-25: build wave merged through PR 397 (9968292) on 24 Nov 22:54. PRs 379–385 went live at 14:08; after S46, PRs 387–392 and 394–397 merged. Leftover work stays in other Open Items. Decisions Log 24 Nov 13:50/14:08 and 22:55.

### OI-INDY-REHAB-REVIEW — Owner review of Indy rehab cost table
- Owner agent: Indianapolis Market Research
- Status: closed
- Updated: 2026-11-25
- Next action: [reported] table done 13:15: <$25 and $25 tiers supported (~$18.5 and ~$25.9/sf on a 1,200 sf 3/1), but "with kitchen" lands ~$36–38/sf, above the $30 tier and the $35 cap (~$31 only with a ~$6k rental-turn kitchen). Eran reviews later; rehab defaults unchanged until he approves.
- Needs owner approval: yes
- Source: [[Indy Rehab Costs]]; /home/box/shared/indy-rehab-costs/
- Evidence: [verified] 2026-11-25: Eran approved the figures in use ($35/sf, three tiers, $8,000 per extra bath; S29/S30/S45). PR 395 merged 3a0bd90 on 24 Nov 22:45. secretary-tasks-reconcile-24-11.txt; daily note 24 Nov.

### OI-ENGINE-GITHUB — Move deal engine to GitHub (S26)
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: [decision] 12:52 GitHub becomes source of truth for the deal engine (now at /home/box/shared/deal-engine; backup deal-engine-backup-20261124 exists on the box). Not moved yet.
- Needs owner approval: no (decided)
- Source: [[Eran Decisions by Topic]] S26
- Evidence: [verified] 2026-11-25: engine lives under engine/ in hs-hold/hsdeals-claude-code; GitHub is the source of truth. PR 387 merged 20:46 (07ae2d7); PR 396 merged 9e74c05 at 22:54 (157 tests). Decisions Log 24 Nov 20:46 and 22:55.

### OI-PRESREEN — Pre-screen vs trial criteria
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: filter audit 23 Nov: rejects correct, but hold rules (low comps, ARV>2x price, basement unknown) hid 3 workable deals — see OI-HOLD-RULES. Still wait for OI-CRITERIA (25 Nov); no code change without approval.
- Needs owner approval: yes (business rule and later merge)
- Source: [[Criteria Map]], [[Deal Pipeline]]
- [stale] 2026-11-25: superseded by the 24 Nov build wave (owner approved merge+deploy at 13:50; PRs 379–385 live 14:08). What remains is the 25 Nov criteria review (OI-CRITERIA).

### OI-RAPIDAPI — RapidAPI pace above the ~25/day target
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: live `rapidapi_usage` for the Nov 22 155-call window is still not queryable from this helper (no Supabase connector; secrets were not used). A pre-existing dump `/workspace/deal-search-2026-11-23-extra/rapidapi_today.json` (no new RapidAPI calls) covers 23 Nov 01:24–07:25 UTC only: 113 calls, 86 of them Atlanta zips under trigger `zillow_search` (burst 06:50–07:03 UTC / 08:50–09:03 Israel), and 27 Indy under trigger `funnel`. That Atlanta burst is the likely driver of the 09:03 alert (96 calls / 24h, 90 zillow-search for-sale). Do not start further unscheduled pulls. See the RapidAPI note in progress.md.
- Needs owner approval: no for further read-only investigation; yes to change schedules or deploy
- Source: RapidAPI watch 22–23 Nov; that report
- [stale] 2026-11-25: Eran, 23 Nov 14:39 — call volume is not an issue; do not limit owner-requested searches. Decisions Log 23 Nov 14:39.

### OI-PROPERTYCOUNT — Health propertyCount always 0
- Owner agent: Grok Bot
- Status: closed
- Updated: 2026-11-25
- Next action: treat as a stale/unused field unless a later PR is approved to fix the health payload
- Needs owner approval: yes to change/deploy
- Source: [[2026-11-23]] daily search note
- [stale] 2026-11-25: field unused. The item already said to treat propertyCount as a stale/unused field unless a later PR is approved to fix the health payload; no such PR exists.

### OI-46140 — Zip intel note for 46140 claimed missing
- Owner agent: Zip Intel
- Status: closed
- Updated: 2026-11-23
- Next action: none
- Needs owner approval: no
- Source: [[2026-11-20]] open checkbox; file `/home/box/shared/zip-intel/46140.md`
- Evidence: [verified] 2026-11-23, the file exists, 29,297 bytes, mtime 2026-11-21 21:40 IST, and is a full Greenfield / Hancock County note (mentions 1019 N Broadway St). The 20 Nov daily checkbox was marked done and [stale], not deleted.
