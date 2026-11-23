# RapidAPI sources and timeout zip-skip (read-only, 2026-11-23)

No RapidAPI calls were made for this note. The timeout bug is **not** fixed in production. A PR may be prepared; merge, deploy, and a live test need separate approval.

## What is verified
- Watch 22 Nov 08:56 Israel: 2,117 / 6,000 used; **155 calls in 24 hours** (threshold 75); mostly zillow-search / for-sale (**129**). Reset 27 Nov 17:52 Israel. Pace then cited as 57.3/day. Source: [[2026-11-22]].
- Watch 23 Nov 09:03 Israel: 2,220 / 6,000 used; **96 calls in 24 hours**; **90** from zillow-search for-sale. Pace 87.3/day. Source: [[2026-11-23]].
- Target cited in the audit and owner brief: about **25 calls/day**.
- 21 Nov daily search: RapidAPI timeouts on **46143** (07:54) and **46168** (08:06), 0 properties, nothing analyzed. Source: [[2026-11-21]], [[Deal Pipeline]].
- 23 Nov extra search: zip **46236** failed on timeout and was not pulled (reported in the main chat / daily note: zips attempted 46229, 46235, 46236, 46239; 552 listings from the successful pulls). Source: [[2026-11-23]].
- Site code on `main` (read-only, `supabase/functions/funnel-run-next-zip/index.ts`): a failed pull leaves `last_pulled_at` alone, writes `last_run_status: "retry_later"` and `pull_retry_after`, records the run as `retry_later`, then calls `pickNextZip` on the deferred candidate list and returns `success: true`, `status: "retry_later"`, and `nextZip`. A daily job that treats `success: true` or a non-null `nextZip` as "this slot is done" will skip the failed zip and spend the slot on another zip. Pull timeout used here is 25 seconds (`PULL_TIMEOUT_MS = 25_000`), with earlier backoff retries described in the file header. [verified] from GitHub main, SHA of this file at read: bc0ca676394a8520b6654cf6fef854fd90da70f4.
- Pre-screen defaults in `src/utils/funnel/screen.ts`: flip $30,000 and 15% ROI, rent 1% (near 0.9%), max 25% off list. [verified]

## What is not yet verified (needs a read-only DB look, no new RapidAPI)
- Row-level breakdown of the 155 and 96 calls in table `rapidapi_usage` (timestamps, function, zip, cache hit/miss, retries).
- Whether the owner's local tools also called zillow-search on those days (mentioned as a possible legitimate source in planning; not confirmed from this pass).
- Exact call count of the 23 Nov extra search (the coordinator reported about 21 calls) vs the daily two-zip run.
- Whether timeout retries themselves multiplied calls on 46143 / 46168 / 46236.
- Cache behaviour in `zillow-search` and `refresh-zip-inventory` (functions exist; not opened line-by-line in this pass).

## Suspected mix [hypothesis]
Scheduled daily funnel (two zips, plus health checks that should use no RapidAPI), retries after timeouts, the 23 Nov extra search, and any unscheduled or local pulls. The gap between a ~25/day target and 96–155/day is large enough that "two zips a day only" does not explain it. Do not stop the scheduled daily search without the owner; do stop inventing extra pulls until the DB breakdown exists.

## Timeout fix intent (for a future PR, not done)
On `retry_later` / timeout, do not pick or return a different zip for the same daily slot. Keep the failed zip due. Tests must be mocks or replay fixtures with **zero** RapidAPI calls. After merge+deploy+live test only, re-pull 46143, 46168, and 46236.
