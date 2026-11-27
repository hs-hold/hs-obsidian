---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-17
updated: 2026-11-17
tags: [project, site]
---
# Deals Site

## Goal
The partners' deal website (Grok Deals / Grok Analyses) — the only place analyzed deals should be viewed. Repo: `hs-hold/hsdeals-claude-code`. Production is on Vercel + Supabase.

## Key facts (verified only — add source)
- Grok Deals = agent-analyzed deals only, high quality (comps, rehab breakdown, verdict, true time-to-sell, highway flag). Agent numbers override API estimates.
- Tabs (owner, 2026-11-15 and 2026-11-17): Market (default), Email, and Unavailable (PR 367, shipped 2026-11-17).
- After PR 367 (counts checked against site data, not a signed-in browser): 22 deals in Relevant (10 Market / 12 Email) and 2 in Unavailable — [[1544 Boulder Walk Way SE]] and [[5301 Essex Farms Pl]], both under contract. Auction tags on [[983 N Cumberland Cir]] and [[5811 Shadow Rock Dr]]. [[1564 Columbia Dr]], [[2295 Bethsaida Rd]], and [[3425 Longleaf Dr]] marked for sale again. If a deal in Unavailable comes back for sale, it should return to Relevant automatically.
- Two site prices were stale on 2026-11-17: Boulder Walk's price had risen to $399k; Essex Farms' real list price was $290k, not $205k.
- Owner also asked (2026-11-17) for a market filter at the top of Grok Analyses: All / Indianapolis / Georgia. A cloud agent was started for that; confirm it is live before treating it as done.
- RapidAPI is used only by site code, never directly by an agent. Plan 6,000 calls/month, reset around 27 Nov 17:52 Asia/Jerusalem. A 24h spike (175 calls vs a 75-call alert) was reported 2026-11-17, mostly zillow-search; month-to-date 1,923 / 6,000 at that check.

## Decisions
- Site UX and display rules: see [[00 Profile]] (tabs, ranking, unanalyzed deals hidden, BRRRR badge, auto-adjust money-in-deal, schools sum, inventory months).
- 2026-11-17: on-market deals that are pending, under contract, contingent, sold, or off the market leave Relevant and go to Unavailable. Off-market (email) deals are not moved by that listing-status check. Auction listings stay in Relevant with an Auction badge.

## Open tasks
- [x] Indianapolis / Georgia filter live on Grok Deals and Funnel Grok analyses (PR 368, 369)
- [ ] PR 370 motivated-seller flag: owner decided 2026-11-19 to keep it loose (any motivation phrase flags); merge in the next batch with PR 376
- [ ] Owner may still want a signed-in browser check of the 22 / 2 split
- [ ] Duplicate-deals request from a voice call on 2026-11-17 was not received in full — waiting for the owner to restate it

## Links
- Pipeline: [[Deal Pipeline]]
- Profile: [[00 Profile]]

## Log
- 2026-11-10–11: PR 329 (Indy ARV), PR 334 (funnel-screen / run-next-zip), PR 335 (mobile comps) deployed.
- 2026-11-15: ingest fix so email/Grok deal ids are accepted (cloud agent; merge/deploy approved that day).
- 2026-11-17: PR 367 — status badges + Unavailable tab.
- 2026-11-17: PR 368 — All / Indianapolis / Georgia filter on Grok Deals (merge 80a35d9). PR 369 — same filter on Funnel Grok analyses (/funnel/grok, merge 2b0f7ca). Both live.
- 2026-11-17: PR 370 — motivated-seller flag (code-only phrase matcher in src/utils/motivatedSeller.ts; strong phrases score 3). Backfill matched 2,120 / 13,674 listings and 381 / 1,992 deals. Not merged, edge functions not deployed; suggestion: show the badge only on strong phrases.
- 2026-11-27 11:36: PR #398 (Works with discount ≤15% off, else Rejected) merged by Eran himself (hs-hold account), merge 98eaef97. Live per the 12:25 Supabase check; deploy not independently confirmed. Relevant 7: 2202 Woodlawn, 1446 Spann, 3425 Longleaf, 3350 N Gladstone, 4436 Malibu, 1613 Draper, 607 E 50th.
