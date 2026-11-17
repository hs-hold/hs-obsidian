---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-17
updated: 2026-11-17
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
- [ ] Consider adding a Drive step to the twice-daily brain sync routine (suggested; do not change the routine until the owner approves)
- [ ] Contract Desk and מזכירה still have no document outputs to file
- [ ] דוחות ומחקר is ready for future reports; current research lives in Pages (linked in the index) and in שווקים ומיקודים

## Links
- Profile: [[00 Profile]]
- Vault: [[Obsidian Vault]]
- Trip: [[Indy Trip Nov 2026]]
- Learning: [[Project X Israel - full text]]

## Log
- 2026-11-17: Library structure created inside the existing Content Insights folder. First harvest of bot documents from `/home/box/shared`, `/workspace`, deal-outcomes, zip-intel, and indy-trip. Index doc written at the root.
