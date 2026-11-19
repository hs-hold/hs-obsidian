# Indy prescreen ARV diagnostic: 4 listings, 2026-11-19

Requested by the owner via [[Grok Bot]]: 4 Indy listings where the site prescreen ARV was more than 2.5× the ask. Analyzed by [[Deal Analysis]] under the trial criteria for Nov 18–24, including the 2.5% buyer agent + $600 on-market costs. **All 4 REJECT**, posted to the site. MAO is the trial-criteria max (% below ask). Research only: nobody was contacted.

| Address | Status | Ask | Prescreen ARV | Real ARV | Rehab | Rent | MAO |
|---|---|---|---|---|---|---|---|
| 3956 Boulevard Pl 46208 | pending | $125k | $626k | $301k (micro-revised $272k) | $115k | $2,100 | $96.3k (23%); $82.7k (34%) at micro-revised ARV |
| 256 W Gimber St 46225 | pending | $85k | $233k | $176k | $65k | $1,150 | $34k (60%) |
| 8296 E 46th St 46226 | for sale | $40k | $384k | ~$215k ceiling (insufficient comps) | $235k (fire gut) | $1,575 | none |
| 3871 Farnsworth St 46241 | for sale | $90k | $464k | n/a: commercial building | — | — | none |

Why the prescreen ARV was wrong:
- **Boulevard:** 9 of 14 comps were across N Meridian St (Meridian-Kessler) and 5 were north Butler-Tarkington near Butler University. Luxury outliers ran up to $505/sf. The largest nearby "renovated" sale counted its finished basement in GLA. The house is a de facto up/down 2-unit. The subject block has 19 vacant/abandoned records within about 1/8 mi.
- **Gimber:** The 1,250 sf includes about 300 sf of unfinished attic, so the real figure is about 950 sf. Comps were 1.2–1.5 mi away across rail and Madison Ave (46203 / Bates-Hendricks), plus a 5-acre Perry Twp sale.
- **E 46th:** The one comp was across I-465 and rail. The prescreen applied $/sf to a 3,147 sf fire-damaged shell in a pocket that tops out around $206k. The city referred it to demolition in 2025.
- **Farnsworth:** The assessor class is COMMERCIAL 420 (small retail). It's in flood zone AE, and the property itself is on the city Abandoned list. The prescreen used a zip-median fallback with no comps.

Prescreen fixes proposed (need the owner's approval):
- Above-grade GLA only.
- Highways, rail, Meridian, Madison and zip-notes edges are hard boundaries; 0.5 mi radius.
- Trim outliers to ±25% of median $/sf.
- Gate on assessor property class (510 only).
- Gate on fire, demolition or no-access condition.
- Cap ARV for over-improvement.
- No zip-median fallback.
- Treat ARV/ask > 2× as a data-error flag; skip pending listings.

Lesson: an ARV of 2.5× or more the ask is almost always a data error (property type, sqft basis, or comps from another pocket), not hidden equity.

Files: `/home/box/shared/deal-outcomes/analyses/2026-11-19/arv-diagnostic/` (SUMMARY.md + 4 Hebrew write-ups + payloads).
