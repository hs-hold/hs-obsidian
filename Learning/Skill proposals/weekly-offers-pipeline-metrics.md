---
name: weekly-offers-pipeline-metrics
description: Use when reporting weekly acquisition activity, when the pipeline looks idle, or when setting a simple offer-volume dashboard for flips and BRRRR deals.
---

# Weekly offers and pipeline metrics

## Why it helps H.S HOLDINGS
Makes "are we actually buying?" visible with a short weekly count of offers, contracts, and bottlenecks, which the course treated as the basic health check of an acquisition business.

## Suggested runner
Existing bot: the **secretary** (a short weekly recap) with deal status from **Deal Inbox** and offer numbers from **Deal Analysis**. **Grok Bot** can receive the recap and raise a flag if offer volume is zero. No new bot needed unless the pipeline later includes paid lead-gen funnels (then Off-Market Desk would add funnel metrics).

## When to use
- End of week, or when a partner asks how acquisition is going.
- After a market trip or a batch of wholesaler meetings, to record follow-ups.
- When no offers have gone out and the week needs a diagnosis, not a pep talk.

## The health question from the training
"How many offers did you or your team submit in the last week?" If the answer is zero, nothing in the deal machine is moving. Class examples of active investors submitting 5, 10, 20, 30, or 40 offers a week are **illustrations of volume, not a quota**. Set a local, realistic target from current capacity.

An offer, in this skill, means a written number actually sent (email, text, portal, or contract), not an internal MAO sitting in a spreadsheet.

## Minimum weekly counts
Track for the active market only:

1. New leads received, by source (wholesaler, realtor, MLS / on-market, FSBO, off-market, other).
2. Leads that received a full four-number analysis (`offer-mao-calculation`).
3. **Offers submitted**, and how many were at or below MAO.
4. Offers still waiting for a seller/wholesaler reply (age them).
5. Properties under contract, and the inspection-period clock on each.
6. Passes, with a one-line reason (price, rehab, rent, title, neighborhood, capacity).
7. Follow-ups due in the next 7 days.

Optional later: list / skip-trace / call funnel numbers from `off-market-lead-generation`.

## How to read the week
- Zero offers and a full lead list usually means analysis or decision bottleneck.
- Many analyses and zero offers may mean MAO rules are unclear, or fear of sending a written number. The training point: until an offer is submitted, nothing happens.
- Many offers and zero contracts may mean offers are not reaching decision makers, terms are uncompetitive, or follow-up is slow.
- A contract with a weak inspection exit is not "success"; send it through `purchase-contract-protections`.

## Example defaults (H.S HOLDINGS)
- Active market: Indianapolis. Do not mix paused-market browsing into the "offers submitted" score.
- There is no mandatory 20-offers-per-week target until the partners set one. Until then, report the raw counts and flag a **zero-offer week**.
- Quality still beats volume: an offer above MAO does not count as a healthy offer.

## Outdated items
- Class stories of 20–40 offers a week came from full-time students and mentors in an earlier market. Do not treat them as a 2026 quota for a small team.
