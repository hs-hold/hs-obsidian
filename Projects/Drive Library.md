---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-17
updated: 2026-11-27
tags: [project, drive]
---
# Drive Library

## Goal
ספריית Google Drive לכל תוצר חשוב של הבוטים. הבעלים פותח תיקייה נקייה לפי נושא; הבוטים שומרים גלם וגרסאות ישנות בארכיון, ומחפשים שם לפי בקשה. **כל הבוטים ניגשים רק לתיקיית השורש הזו — לא לשאר דרייב.**

## Key facts (verified only — add source)
- Root folder (created earlier by Content Insights, reused 2026-11-17): [Content Insights](https://drive.google.com/drive/folders/1LCduQCgprfikz1znRJBnyjY3mQuG6UYB) — id `1LCduQCgprfikz1znRJBnyjY3mQuG6UYB`
- Owner folder: [📂 למסמכים שלי](https://drive.google.com/drive/folders/13wHRhbwc8lFbCefS7wTMcFcgtAKtdWFc) — id `13wHRhbwc8lFbCefS7wTMcFcgtAKtdWFc`
- Archive: [_ארכיון (לבוט)](https://drive.google.com/drive/folders/1_-XnoF7Bd_E0cHpFdKtKzJhcBA5Z-hvp) — id `1_-XnoF7Bd_E0cHpFdKtKzJhcBA5Z-hvp`
- Index: [אינדקס - מה יש איפה](https://docs.google.com/document/d/1j9oKh3ZwRDGckPfLzC4LLdlzLSqN9Nu3iEQm9hhgNyc/edit?usp=drivesdk)
- Existing subfolder left in place: [Project X Israel](https://drive.google.com/drive/folders/1jQ5hYBPOb3MK6QEfjCi_petQxZmnt-00) — id `1jQ5hYBPOb3MK6QEfjCi_petQxZmnt-00`
- Connector: `user-Google-drive`. Do not share the library with anyone unless the owner asks. Do not delete or move files that were already in Drive.
- The Obsidian vault remains the living brain; Drive holds openable documents and an archive the bots can search on request.

## Structure and folder IDs
Owner-facing (`📂 למסמכים שלי`):
- עסקאות — `1lhQm1K6sXgStlx2brmxTJagmu9WM970q`
- שווקים ומיקודים — `1w_5uerDP1dlNt8DvQvx6GlNfgoHNYbAV`
- אנשי קשר — `1lBChRK5e1k_6SddCeRLj-sCojNqJUkQ6`
- טיול אינדי (טל) — `1mzE8Mkcqneptn10H37Hsui6wfDorlGqL`
- חוזים ומשפטי — `1BQcGA3_OUC96Rc3KV0u_QJBZB5_ZwXId`
- דוחות ומחקר — `13MdZj_Xdh5HUgu0ZsarhfV7iAf7xsiSL`

Archive (`_ארכיון (לבוט)`):
- טיול-אינדי — `1ZCPyInXkucADMXItoqUgo0i5372wr1U4`
- ניתוחי-עסקאות — `1ZPYPdxxP68UyfcS42QTRrSf9nHsxaE5I`
- zip-intel — `1VUEJTVj1HrYOCTdo73PhR5KiV-javje1`
- inbox-scans — `1_wp9wWQq5sixzbF6WtikrrTdOooxl0pr`
- מקורות-מחקר — `1cseUcSoXhqJonbw1JTBjCheAOHInSX8C`
- כללי-סוכנים — `1A3N3ffWbIB1B-1SSjPjQEuFZAMyY5WXp`

## Decisions
- 2026-11-17: Reuse the existing Content Insights folder as the single library root rather than creating a duplicate.
- 2026-11-17: Owner-facing folder holds only the latest human-readable version of each document (PDF / Excel / Google Doc / HTML for phone lists). Raw, older, JSON, CSV, and Markdown dumps go to the archive as zip files.
- 2026-11-17: Secrets, tokens, passwords, `.env`, and anything under `/home/box/shared/secrets` are never uploaded. Pages are linked from the index, not copied.
- 2026-11-17 (owner): Bots must stay strictly inside this library folder and not browse the rest of Drive. Folder IDs belong in shared memory so bots do not need to ask for permission each time.

## Rule for new outputs
When a bot produces something the owner may want to open later:
1. Put the latest clean file in the matching topic folder under `📂 למסמכים שלי`.
2. If it replaces an older version, move the previous file into `_ארכיון (לבוט)` (do not delete it) or add it to that topic's archive zip.
3. Update [[Drive Library]] and the Drive index doc with a one-line Hebrew description and the link.
4. Raw working files (JSON, payloads, drafts) go only to the archive, or stay on the box if they are huge datasets — see the leftover-files note in מקורות-מחקר.

## Open tasks
- [x] Drive step is part of the twice-daily brain sync routine (from 2026-11-17)
- [ ] Contract Desk and מזכירה still have no document outputs to file
- [ ] דוחות ומחקר is ready for future reports; current research lives in Pages (linked in the index) and in שווקים ומיקודים

## Links
- Profile: [[00 Profile]]
- Vault: [[Obsidian Vault]]
- Trip: [[Indy Trip Nov 2026]]
- Learning: [[Project X Israel - full text]]

## Log
- 2026-11-17: Library structure created inside the existing Content Insights folder. First harvest of bot documents from `/home/box/shared`, `/workspace`, deal-outcomes, zip-intel, and indy-trip. Index doc written at the root.
- 2026-11-17 23:20: evening sync added index lines for the Project X Israel insights + work plan and the other Project X Club course text folders (Content Insights files left in place in its own topic folders). Olive micro-location doc was already filed in עסקאות.
- 2026-11-18 13:25: midday sync filed 2 deal analyses as Google Docs in עסקאות (1621 E 46th St, 902 Hearthside Ct) + index lines; raw files archived (46112 search summary → ניתוחי-עסקאות, Deal Inbox handoff 2026-11-18 → inbox-scans, zip-intel 46112 → zip-intel).
- 2026-11-18 23:30: the evening sync filed:
  - In עסקאות, as Google Docs: the 13-listing Indy batch summary and the 1735 N Oxford St analysis.
  - In אנשי קשר: the Indy contacts drip page for day 1 (HTML).
  - Archived: the Nov 18 research zip in מקורות-מחקר (prefilter dry-run, no-ARV root cause, GitHub tools, dedupe/review), and the raw batch + Oxford files in ניתוחי-עסקאות (no images; the sheet JPGs stay on the box).
  - Added 3 index lines.
- 2026-11-19 13:30: the midday sync filed:
  - In עסקאות, as Google Docs: the Indy ARV diagnostic (4 listings) and the Atlanta held deals (4).
  - In דוחות ומחקר: the Indianapolis basement / above-grade ARV research (Google Doc).
  - Archived: `analyses-2026-11-19-raw.zip` in ניתוחי-עסקאות (no images) and `research-2026-11-19.zip` in מקורות-מחקר.
  - Added 3 index lines. Nothing was replaced, since these are new topics.
- 2026-11-19 23:20: the evening sync filed in אנשי קשר (HTML): the 10 new Indy brokers (`מתווכים אינדי — 10 חדשים 19.11.html`) and the contacts drip day 2 (`אנשי קשר אינדי — טפטוף 19.11.html`, a proper text/html copy). The drip run's text/plain copy in טיול אינדי was moved to the archive's טיול-אינדי folder and its index line repointed. Added 1 index line.
- 2026-11-20 13:21: the midday sync filed in עסקאות, as Google Docs: 4244 Canby Ln (Decatur 30035) and 1019 N Broadway St (Greenfield 46140) analyses, both rejected. Archived `analyses-2026-11-20-raw.zip` (no images) in ניתוחי-עסקאות. Added 2 index lines. Content Insights had already filed its 10-1 notes/transcript and skill-proposal drafts itself.
- 2026-11-20 23:25: the evening sync filed 714 Cather Ct analysis (Google Doc, עסקאות), Indy contacts drip day 3 (`אנשי קשר אינדי — טפטוף 20.11.html`, אנשי קשר), and archived `analyses-2026-11-20-evening-raw.zip` (no images/photos page/PDF) in ניתוחי-עסקאות. Added 2 index lines. Nothing replaced.
- 2026-11-21 13:15: the system overview (Hebrew Word, written 13:11 on the owner's voice request) is in דוחות ומחקר (file 184ouimmwV5Afob6GoDuP0wnmnl-F4IeI, not shared); midday sync added 1 index line. Nothing else new to file.
- 2026-11-23 23:25: the evening sync filed in אנשי קשר (HTML) the 50 Indy brokers for 30.11–1.12 meetings; in דוחות ומחקר (Google Doc) the Indy 20-property filter audit; archived filter-audit-indy-20-2026-11-23-raw.zip in ניתוחי-עסקאות. Added 2 index lines. Nothing replaced.
- 2026-11-24 13:25: the midday sync filed in עסקאות (Google Docs) the 303 N Franklin Rd analysis and the 5 Atlanta Deal Inbox analyses summary; in דוחות ומחקר (Google Docs) the Indy rehab cost-by-component research, the ARV AI sources research (Content Insights had put the .md in the root Research folder; left in place) and Eran's screening/rehab/ARV decisions status; archived analyses-2026-11-24-raw.zip (no images) in ניתוחי-עסקאות and research-2026-11-24.zip (rehab CSV/MD, ARV sources, /workspace/exports audit + work-plan texts) in מקורות-מחקר. Added 5 index lines. Nothing replaced.
- 2026-11-25 13:20 (brain sync): added [עלויות שיפוץ לפי רכיב — אטלנטה 25.11.2026](https://docs.google.com/document/d/1M2LRu1t7x3o1_zOmiCcwB9fnKwrcVe-Zu8iR20MXx5U/edit) (דוחות ומחקר), [1827 N Rochester Ave — ניתוח 2026-11-25](https://docs.google.com/document/d/1pQKySEpMN6JMyvTC5klccEqITqX5S3aHx6bsHlxQsEI/edit) and [אינדי 46205 — 5 נכסים + Cedar Pine](https://docs.google.com/document/d/1b01eN3hCTWv-8xOxT1mmHD6zq22AeB0YsuUnozZGSSs/edit) (עסקאות). Archive: analyses-2026-11-25-raw.zip (ניתוחי-עסקאות), atl-rehab-costs-raw-2026-11-25.zip (מקורות-מחקר). Index doc updated.
- 2026-11-25 23:25 sync: uploaded "דוח איכות הסינון — 24 שעות עד 25.11.2026" (Google Doc, id `1kD_7dYzw7itIU4fFiCxQ4v9tP2hfw2vxa_pKgGoFN1E`) to דוחות ומחקר and added an index line. The 23 Nov 20-property screening check stays (different scope).
- 2026-11-26 13:20 sync: filed in עסקאות (Google Docs) [2170 Lilac Ln — ניתוח 2026-11-26](https://docs.google.com/document/d/18FNfhnNDYCXh857wWJqj34LqCzPYeWs-dzvsQrLR6hQ/edit), [7080 Stone St — ניתוח 2026-11-26](https://docs.google.com/document/d/1BBASQrPu5PsgdNTxltXx5lUA53yBKfpuNWuktnqlhp8/edit), [אינדי 46201+46203 — 4 נכסים](https://docs.google.com/document/d/15SvhBUF0T4XMAuIXt-BVhWUvk-pn-TyoIck8jYFuC5o/edit); archived `analyses-2026-11-26-raw.zip` (no images/HTML, file 1JYwQ48FXDmIYVvCGTg6eRdDf2w-TQ82i) in ניתוחי-עסקאות. Added 3 index lines. Nothing replaced.
- 2026-11-26 23:15 sync: filed [דוח איכות הסינון — 24 שעות עד 26.11.2026](https://docs.google.com/document/d/1j42idf2UMSq6nlosxKsUgfPIzNoBZVSAQqjkehRpne0/edit) (Google Doc) in דוחות ומחקר; moved the 25.11 report (`1kD_7dYzw7itIU4fFiCxQ4v9tP2hfw2vxa_pKgGoFN1E`) to archive מקורות-מחקר (same series, replaced). Added 1 index line.
- 2026-11-27 13:15 sync: filed in עסקאות (Google Doc) [אינדי 46208+46218 — 4 נכסים (27.11.2026)](https://docs.google.com/document/d/1K0xO0jdgv4fk-ve9zrB1KE6DfU8IXUdDKj98c2eJOF4/edit); archived `analyses-2026-11-27-raw.zip` (md/json/py + handoff; no images/HTML/rent_raw; file 1mLNrtwZEI-UoyOn3I-aOs7aOEwnAMXVu) in ניתוחי-עסקאות. Added 1 index line. Nothing replaced.
- 2026-11-27 23:19: the evening sync filed in דוחות ומחקר the Google Doc [דוח איכות הסינון — סופי 27.11.2026 + 8 בתים שלא נכנסו לתור](https://docs.google.com/document/d/1JKfn73pPXtIXYPJnpzi6MP_QL4dvDeiJ_Gy4zq-Zln0/edit) (final 3-day monitor + queue-gap investigation); raw low_comps build prompt archived in מקורות-מחקר (`1bQuvpL45X9ljgvYUsyh6TC_GiCCtDDzC`). The 26.11 daily report stays (separate dated report). Added 1 index line.
