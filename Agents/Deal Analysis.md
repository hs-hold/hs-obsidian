---
type: agent-log
agent: "Deal Analysis"
created: 2026-11-09
updated: 2026-11-24
tags: [agent]
---
# Deal Analysis — work log

Append-only. Each session-close adds a dated "###" entry (learned / decisions / tasks).

### 2026-11-17 — one-time vault backfill (Nov 1–17)
Durable facts from this period were written into the shared vault (daily notes, deals, markets, contacts, projects, profile). Sources: teammate transcripts where readable, shared memory, and files under `/home/box/shared` and `/workspace/indy-trip`. Grok Bot's main-chat transcript was not directly searchable from the backfill run; the parent-conversation summary was used instead.


Key durable output from this period lives in `Deals/` and `/home/box/shared/deal-outcomes/analyses/`. Rules: `/home/box/shared/agent-rules/deal-analysis.md`.

### 2026-11-17 evening — Deal Analysis (from sync 23:13)
- Counted ~210 deals since Nov 9. Deep micro-location check on [[1733 Olive St]] → REJECT on site. Added the micro-location rule. Indy-only searches through Nov 24, reminder Nov 24 10:00. Received trial criteria and the MAO rule.

### 2026-11-19 — Deal Analysis (from sync 13:15)
- [[2026-11-19 Indy ARV diagnostic (4 listings)]] and [[2026-11-19 Atlanta held deals (4)]]: all REJECT.
- New rule (owner, 11:33 in its own chat), commit 5a38484 in `agent-rules/comp-adjustments.md`: Indy above-grade GLA only; finished basement as a separate line at 50% × above-grade $/sf; unfinished basement $0; every analysis states the basis of each sqft figure.
- From Nov 19 the site prescreen passes flagged outlier comps (with % deviation and `upside_arv`), so weigh them in context.

### 2026-11-20 — Deal Analysis (from sync 13:20)
- [[4244 Canby Ln]] (New Western, Atlanta 30035): REJECT, trial MAO $105.4k vs $145k MLS / $108.4k vs $139k wholesale; payload not posted.
- [[1019 N Broadway St]] (daily funnel 46140): REJECT, trial MAO $70.8k vs $149.9k; posted as deal 35161f1b. Proposed screen lesson: "ready for full renovation" text forces the heavy rehab tier.
- Found that `GET deal-analysis-ingest` marks unpulled items 'sent'; two Avon items (Nov 19, 46123) are sent-but-unanalysed pending the owner's answer.

### 2026-11-20 evening — Deal Analysis (from sync 23:25)
- [[714 Cather Ct]] (wholesaler Adam via Deal Inbox, Atlanta 30088): REJECT, trial MAO $86.1k vs $143k ask; payload posted on owner instruction (deal b74f7b63).

### 2026-11-23 — Deal Analysis (from sync 13:20)
- [[2026-11-23 Indy extra search near-misses (5)]]: all REJECT at ask; top 2426 E 57th St 4/10 (trial MAO $137.9k). Not posted; files in deal-outcomes/analyses/2026-11-23/.

### 2026-11-23 evening (from sync 23:20; its transcript not readable this run — from Grok Bot chat + files)
- Blind analyses for the 5-property check and Indy 20-property audit. Rule (owner 20:50): properties passing at ask or ≤15% off are always uploaded, including audit/test runs; written to its rules file (reported 20:56).
- Posted 1318 Bacon St (passed), 3667 Cedar Pine Pl, 10160 Park Stream Dr (deal ids d8566553…, 78c86ae2…, 8ab78e22…).
- v3 engine research re-run ~21:44–23:10 contradicts Bacon/Park Stream (OI-V3-RECHECK).

### 2026-11-24 (sync 13:20; from vault commits + /home/box/shared files)
- 08:23 [[303 N Franklin Rd]] (Indy, InvestWithBen, ask $84.9k): REJECT, flip MAO $69.3k = 18.4% off; single comp; not posted (>15% off).
- Analyzed the 5 Atlanta deals from the Deal Inbox 08:00 scan: all REJECT/INCOMPLETE, not posted (Indy-only trial; Atlanta needs owner OK) — [[2026-11-24 Atlanta Deal Inbox batch (5)]].
- New owner requirements for this bot (24 Nov call, [[Eran Decisions by Topic]]): wide discretion with recorded reasons (S4); super-comp rules (S5/S13/S28); missing data → estimate + 'needs verification' (S16); bot judges plausibility itself (S17); know every site data parameter and record them realistically (S22); raise low confidence by pulling more comps (S24); override limit 70% vs engine number (S25); photo-less comps inferred from description/price (D3); school ratings from API or 3 nearby schools (D4); add each analysis's renovated sold comps to the region's calibration list (D2). Build pending ([[Open Items]] OI-ARV-BUILD).

### 2026-11-25 (sync 13:20; from /home/box/shared files)
- New rule (owner voice ~10:56, agent-rules 703c705): CF > $100/mo in any scenario at ask or ≤15% off → flag "good potential" and report to Eran immediately, separate from pass/fail; $250/mo = full BRRRR pass.
- ~08:15 [[1827 N Rochester Ave]] REJECT (trial MAO 27.6% off); Eran passed 10:02.
- 09:02 [[2026-11-25 Indy funnel 46205 (5)]]: 5 FAIL, all POSTed rejected. [[3910 Hillside Ave]] CF +$126 self at ask (pre-rule) → OI-GOODPOT-HILLSIDE.
- 11:23–11:26 [[3667 Cedar Pine Pl]] re-run REJECT (17.7% off), re-POSTed rejected; good-potential check = true ($148/mo at 15% off).

### 2026-11-26 (sync 13:20; from /home/box/shared files)
- ~09:33 Atlanta (owner OK'd 26 Nov via Deal Inbox): [[2170 Lilac Ln]] REJECT (goodPotential mechanical TRUE, ~$133k stays in), [[7080 Stone St]] REJECTED (no official ARV, flip only). Both POSTed rejected.
- Funnel 46201+46203: [[2026-11-26 Indy funnel 46201+46203 (4)]] — 4 FAIL, all POSTed rejected; goodPotential YES on [[2856 S State Ave]] (+$497/mo) and [[321 S Hamilton Ave]] (+$199/mo).
- Note: in these subagent runs the good-potential report went to the parent instead of a priority message to Grok Bot (no-contact instruction) — whether Eran was told is tracked in OI-GOODPOT-2611.
- Local prc.py partial-story fix applied in the run's raw/ only, not committed to the shared engine.

### 2026-11-27 (sync 13:15; from /home/box/shared files)
- Funnel 46208+46218: [[2026-11-27 Indy funnel 46208+46218 (4)]] — [[3350 N Gladstone Ave]] PASS (auto-posted), 3 FAIL POSTed rejected; goodPotential YES on Gladstone, [[1043 W 36th St]], [[1315 W 34th St]] (delivery to Eran tracked in OI-GOODPOT-2711).
- prc.py partial-story fix again local only; Plans A/B/C have no written definition (analyst used an assumption); box rollback mid-run handled, no duplicate posts.

### 2026-11-28 (sync 13:30; from /home/box/shared files)
- IWB weekly funnel: [[2026-11-28 Indy IWB weekly (4)]] — [[4726 Stratford Ave]] FAIL at ask / trial PASS at 15% off (posted 10:29, passed, 7e323777; owner decisions on rehab tier, ARV>2× block, GLA), [[3457 N Hartman Dr]] FAIL, [[2116 N Arlington Ave]] FAIL, [[332 N Fleming St]] INCOMPLETE (0 comps). goodPotential TRUE on Stratford, Hartman, Arlington (OI-GOODPOT-2811).
- Applied the owner's 27 Nov comp complaints: hard zip boundaries as geometry, wider-GLA tier off (local patch only), fallback only on zero strict survivors, road-class check for subject and comps. Calibration rows added (not committed). Tax district 701 IPS vs MSD Warren conflict raised (OI-IWB-2811).
- 13:24 follow-up [reported, Grok Bot chat]: Deal Analysis told the chain the Stratford 15%-off PASS is uncertain (fails at 1,152 sqft; ARV >2× ask guard; sqft 792 / 1,152 / 1,512). After Grok Bot created the deal on the site (~10:24–10:29), Deal Analysis posted the analysis with caveats visible.
