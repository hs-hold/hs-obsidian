---
type: project
status: active
owner: H.S HOLDINGS
created: 2026-11-22
updated: 2026-11-22
tags: [project, metrics]
---
# Metrics

Weekly business snapshot for H.S HOLDINGS. Each row is Sunday–Saturday, Asia/Jerusalem. Sources are existing data only (vault notes, routine results, teammate transcripts, and read-only Supabase). No RapidAPI calls are made for this snapshot. Offers submitted are whatever the partners told a bot; if nobody said a number, the cell is `unknown` and the owner is asked.

## Weekly snapshots

| Week (Sun–Sat, IL) | Zips pulled | Listings screened | Analyzed | Pass trial (at ask) | Pass old BRRRR (at ask) | Pass flip (at ask) | Motivated seller | Offers submitted | New contacts | RapidAPI calls | Weekly usage % |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---:|---|
| 2026-11-15 – 2026-11-21 | 14 attempted / 12 with listings | 1,800 | 34 | 0 | 0 | 1 | 0 of this week's 34 analyses; 381/2,037 deals flagged in the DB (site badge PR 370 not merged yet) | unknown | 52 new, plus a 190-row trip list compiled this week | 397 quota drop (4,287 → 3,890 left of 6,000); 369 logged | 90.2% just before the Sat 21 Nov 14:29 IL reset (limit shared with other apps on the plan) |

## Notes for 2026-11-15 – 2026-11-21

This is the first weekly row, so week-over-week for most columns has no prior Metrics row. Funnel_runs for the previous Sunday–Saturday (8–14 Nov) show 4 distinct zips, 403 listings, and 19 queued, versus 14 zips, 1,800 listings, and 22 queued this week.

### Zips and listings
Real funnel pulls only (health-check rows excluded). Listing counts come from `funnel_runs.listing_count`.

- 15 Nov: 30035 (121, 5 queued), 30088 (155, 1 q), 30080 (116, 4 q), 30032 (331, 0 q)
- 16 Nov: 30294 (183, 5 q)
- 17 Nov: 30273 — run row stored listing_count 0; the daily note said 55 properties and none passed screening
- 18 Nov: 46107 (43, 0 q), 46112 (184, 3 q)
- 19 Nov: 46113 (first attempt error, then 108, 0 q), 46123 (227, 3 q)
- 20 Nov: 46140 (223, 1 q), 46142 (109, 0 q)
- 21 Nov: 46143 and 46168 timed out (`retry_later`), 0 listings; the run advanced the zip pointer (open fix)

`screen_total` was recorded for 1,524 of the 1,800 listings (the 15 Nov pulls of 30035 and 30088 predate that field). 22 listings entered `deal_queue` this week (2 analyzed, 7 sent, 13 expired).

### Analyses and passes
34 full Deal Analysis reviews, counted from daily notes and vault deal notes (not the 15 Nov ingest write-back of earlier email/Grok deals, and not legacy FindMeDeals rows).

- 15 Nov (pre-trial): 5301 Essex Farms Pl, 5811 Shadow Rock Dr, 4799 Oak Ct, 2195 Trailwood Dr SE — all reject at ask
- 17 Nov: 4213 River Rd, 1733 Olive St (re-analysis) — both reject
- 18 Nov (trial started): 1621 E 46th St, 902 Hearthside Ct, 1735 N Oxford St, plus the 13-listing Indy batch — all reject under trial, old BRRRR, and flip
- 19 Nov: 4 Indy ARV-diagnostic listings and 4 Atlanta held wholesale leads — all reject under all three tests
- 20 Nov: 4244 Canby Ln, 1019 N Broadway St, 714 Cather Ct — all reject under all three tests
- 21 Nov: 1375 Kipling St SE — reject at $99k ask on the trial (MAO $90.9k, 8.2% off); flip passes at ask

Trial criteria apply from 18 Nov. The 17 Nov listing-status pass of 24 on-market "Relevant" deals also found none that hit $250/mo BRRRR at asking (that check is not included in the 34).

### Motivated seller
The matcher and DB columns exist. A backfill has 381 of 2,037 deals flagged. PR 370 (the site badge) is not merged yet. None of this week's 34 Deal Analysis reviews were flagged.

### Offers submitted
Unknown. No partner told any bot a count for this week.

### New contacts
52 people added after the Nov 16 trip workbook, from the daily notes: 9 brokers (17 Nov batch), 1 drip (18 Nov, Pat McNeill), 10 brokers + 2 drip (19 Nov), 10 drip + wholesalers Annabelle Furr and Adam (20 Nov), 18 investor-agent addresses emailed (21 Nov). Separately, the Nov 16 Indianapolis trip research compiled a 190-row contacts workbook, backfilled into the vault on 17 Nov. That backfill is not double-counted in the 52.

### RapidAPI
Quota remaining was 4,287 just before the week (14 Nov 19:21 IL) and 3,890 at 21 Nov 12:41 IL, a drop of 397 (plan 6,000, reset around 27 Nov 17:52 IL). The `rapidapi_usage` log has 369 rows in the week (the logger does not cover the whole billing period). Daily logged calls: 15 Nov 19, 16 Nov 175, 17 Nov 2, 18–20 Nov 7 each, 21 Nov 152. The 16 Nov and 21 Nov spikes were mostly zillow-search.

### Weekly usage
Grok Bot weekly usage was 90.2% on the morning of 21 Nov, just before the Saturday 14:29 IL reset. That weekly limit is shared with the other apps on the plan. The report cannot show the exact percent of the prior week's limit as a single official figure; 90.2% is the last stated reading before the reset. After the reset, usage on the morning of 22 Nov was 6.7% of the new week (not used as this row's metric).
