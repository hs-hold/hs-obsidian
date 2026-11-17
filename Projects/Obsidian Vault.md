---
type: project
status: active
owner: H.S HOLDINGS
market: both
created: 2026-11-16
updated: 2026-11-17
tags: [project, obsidian]
---
# Obsidian Vault

## Goal
A shared "brain" for every bot and the three partners, so decisions, conclusions, owner-provided facts, deal analyses, markets, contacts, and open items are not lost. This repository (`hs-hold/hs-obsidian`).

## Key facts (verified only — add source)
- Private GitHub repo: https://github.com/hs-hold/hs-obsidian
- Clone on the box: `/home/box/shared/obsidian-vault`
- Toolkit: Grok Trestle in `_system/grok-trestle` (adapted from liormesh/trestle, MIT). Five skills (session-open, session-close, vault-health-check, vault-report, vault-setup-interview), scripts including `safe-push.sh` with a secrets scan, and Hebrew + English guides.
- Owner sync on his side: Obsidian Git plugin (not confirmed connected yet).
- Token for git push is stored for the box credential helper only — never write it into a note.

## Decisions
- 2026-11-16: Owner wants every bot to save information in Obsidian, synced via GitHub. After the vault and toolkit were built he said "רגע עצור" ("wait, stop") — registering the five skills and wiring the other bots was put on hold.
- 2026-11-17: Owner wants a **central harvest**, not each bot remembering to save. Harvest twice a day at **13:00 and 23:30 Asia/Jerusalem**, plus an immediate write when something is decided or he says to remember it. A one-time backfill of the last few weeks was approved (this work).
- 2026-11-17: A reminder was set for 20:00 Asia/Jerusalem to connect the bots; do not start the skill rollout until he confirms.

## Open tasks
- [ ] Register the 5 grok-trestle skills and tell all bots to use the vault — only when the owner says to continue
- [ ] Owner: connect Obsidian desktop/mobile via the Obsidian Git plugin (guide section 4)
- [ ] Optional: mention grok-trestle in the vault root README
- [ ] Confirm the twice-daily harvest routine is actually scheduled after this backfill

## Links
- Profile: [[00 Profile]]

## Log
- 2026-11-16: Vault structure, first Send Offers note, Grok Trestle toolkit, profile and project stubs.
- 2026-11-17: Broker-search prompt saved to Contacts/. One-time backfill of Nov 1–17 transcripts and shared files.
