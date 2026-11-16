# Grok Trestle — Full Guide

Guide to the shared-memory toolkit for the H.S HOLDINGS bots in our Obsidian vault. Version 1.0, November 16, 2026.

## 1. What it is and what it's based on

**Grok Trestle** is a toolkit that makes all our bots (Grok Bot, Deal Analysis, Atlanta Market Research, Indianapolis Market Research, Contract Desk, Zip Intel, Content Insights, Deal Inbox and מזכירה, the secretary) work from one shared memory: an Obsidian vault stored in the private GitHub repo `hs-hold/hs-obsidian`.

The core idea is that every piece of work starts with an **opening ritual**: the bot pulls the latest notes and reads the context. It ends with a **closing ritual**: the bot writes back what it learned, what was decided and what is still open, checks the vault is healthy, and pushes to GitHub. Knowledge piles up from session to session instead of getting lost between chats and bots.

It is based on the open-source project [trestle](https://github.com/liormesh/trestle) by Lior Meshullam (MIT license), which was originally built for Claude Code. We took its method and adapted it to Grok Bot agents and to our real estate work.

What's included:
- 5 bot skills: setup interview, session open, session close, health check, status report.
- 6 small scripts that run on the box with nothing to install (python3 and bash only).
- 6 note templates: profile, project, deal, contact, meeting, agent log.
- The company profile `00 Profile.md` and two starter projects in `Projects/`.

## 2. Differences from the original

| Topic | Original trestle | Our Grok Trestle |
|---|---|---|
| Who | One user running Claude Code on their own machine | 9 Grok bots sharing one box, plus three partners |
| Where memory lives | A local folder plus Claude memory files | An Obsidian vault in a private GitHub repo, synced to every device |
| How it's triggered | Commands `/cq`, `/73`, `/onboard` | A plain sentence to a bot: "open session Indy", "close session" |
| Guardrails | Claude Code hooks block writing secrets | Grok has no hooks, so the scan runs on every commit through `safe-push.sh`, which refuses to push if it finds a secret |
| Scripts | Node.js | python3 and bash only, nothing to install |
| Concurrency | Not relevant | A `flock` lock so two bots never run git at once, and `pull --rebase` before every push |
| Content | Software development | Real estate: deals, contacts, markets, flip and BRRRR criteria |
| Report | General-purpose `/visualize` | A Hebrew HTML status report saved inside the vault |
| License | MIT | Same MIT, with full credit in `LICENSE-trestle-MIT.txt` |

## 3. Folder structure

```
hs-obsidian/                         (the vault = the GitHub repo)
├── 00 Profile.md                    company profile, criteria, rules, bots
├── 00 Inbox/                        quick notes not filed yet
├── Projects/                        one note per project
│   ├── Indy Trip Nov 2026.md
│   └── Deal Pipeline.md
├── Deals/                           one note per deal (address.md)
├── Contacts/                        brokers, wholesalers, contractors, lenders
├── Markets/Atlanta/ , Markets/Indianapolis/
├── Meetings/                        YYYY-MM-DD title.md
├── Notes/                           owner notes
├── Agents/<bot name>.md             append-only work log per bot
├── .gitignore                       _private/, .env, workspace files
└── _system/
    ├── reports/vault-report.html    latest status report
    └── grok-trestle/
        ├── README.md, LICENSE-trestle-MIT.txt
        ├── GUIDE-he.md/.html, GUIDE-en.md/.html
        ├── skills/<5 skills>/SKILL.md
        ├── scripts/                 python3 + bash, stdlib only
        └── templates/               profile, project, deal, contact, meeting, agent-log
```

On the box, the vault lives at `/home/box/shared/obsidian-vault`.

## 4. One-time setup

### 4.1 Already done (nothing to do)
- The private repo `hs-hold/hs-obsidian` exists, and the bots connect to it with a token scoped to that repo only.
- The toolkit, templates, profile and projects are already pushed.
- What's left: register the 5 skills with the bots (Grok Bot does this), and connect Obsidian on your devices.

### 4.2 A token for your devices
Use a separate token for each of your devices, so you can revoke one without breaking the bots:
1. Open GitHub's [new fine-grained token page](https://github.com/settings/personal-access-tokens/new).
2. Token name: for example `obsidian-laptop`. Expiration: your choice (one year is convenient).
3. Resource owner: `hs-hold`. Repository access: **Only select repositories**, then pick only `hs-obsidian`.
4. Permissions → Repository permissions → **Contents: Read and write**. (Metadata: Read-only is added automatically.)
5. Click Generate token and copy it right away. GitHub shows it only once.
6. Save it in your password manager. **Not** in the vault, and not in chat.

### 4.3 Connect Obsidian on desktop (Windows or Mac)
1. Install Git. On Windows, get it from [git-scm.com](https://git-scm.com/download/win) and keep the default Git Credential Manager. On Mac, run `git --version` in Terminal and accept the install prompt if one appears.
2. Open a terminal (on Windows: Git Bash or PowerShell) and clone the repo where you want the vault to live:

```bash
cd ~/Documents
git clone https://github.com/hs-hold/hs-obsidian.git
```

3. When prompted, enter your GitHub username as Username and **the token** as Password (not your GitHub password). On Windows, a Git Credential Manager window opens, where you can also sign in through the browser. On Mac, first run this command so the token is saved in Keychain:

```bash
git config --global credential.helper osxkeychain
```

4. In Obsidian, choose **Open folder as vault** and pick the `hs-obsidian` folder.
5. Go to Settings → **Community plugins** → **Turn on community plugins** → **Browse**, search for **Git** (by Vinzent03), then **Install** → **Enable**.
6. In Settings → Git, set:
   - **Pull on startup**: on.
   - **Auto pull interval (minutes)**: `5`.
   - **Auto commit-and-sync interval (minutes)**: `10`.
7. To test: open the command palette (Ctrl/Cmd+P) and run **Git: Pull**. You should see `00 Profile.md` with the company details.

### 4.4 Connect Obsidian on mobile (Android or iPhone)
> The plugin's own author calls the mobile version "very unstable", and it can crash on large repos. It works for a small vault like ours. If it gives you trouble, the alternatives are the GitSync app (Android and iOS) or Working Copy (iOS, paid).

1. Install Obsidian from the app store and create a **new, empty vault** named `hs-obsidian`. On iPhone, do **not** tick Store in iCloud.
2. Go to Settings → Community plugins → Turn on → Browse → **Git** → Install → Enable.
3. In Settings → Git, under **Authentication/Identity**, enter your GitHub username as Username and this device's token (from 4.2) as Password/Personal access token. Leave the Advanced settings alone.
4. In the command palette, run **Git: Clone an existing remote repo**.
5. Paste the URL, ending in `.git`, and tap the button below the field:

```
https://github.com/hs-hold/hs-obsidian.git
```

6. When asked for a folder, choose the vault root. When asked about `.obsidian`, answer based on what's shown (usually NO; you don't need to download settings). Wait for the **Restart Obsidian** message, then restart the app.
7. Then set Pull on startup and Auto pull the same way as on desktop.

### 4.5 Register the skills with the bots
Grok Bot does this. These are the 5 skill folders to register:

```
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-setup-interview
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/session-open
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/session-close
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-health-check
/home/box/shared/obsidian-vault/_system/grok-trestle/skills/vault-report
```

## 5. Daily usage

### 5.1 Opening a session
Tell any bot, for example:
- "open session Indy" / "פתח סשן Indy"
- "open session Deal Pipeline"
- "open session" (no project: profile, the bot's log and open tasks)

The bot pulls from GitHub and reads the profile, the project note, the last 40 lines of its own log, every open task and the health status. It then replies with a short summary. Behind the scenes it's one command:

```bash
python3 /home/box/shared/obsidian-vault/_system/grok-trestle/scripts/session-open.py --agent "Deal Analysis" --project "Indy"
```

### 5.2 Closing a session
At the end of a piece of work, say "close session" or "save to Obsidian". The bot:
1. Picks only verified items from the conversation: what was learned (with a source), what was decided, what's still open, and what got done.
2. Appends a dated entry to its own log `Agents/<bot>.md` and to the project note, under `## Log`.
3. Ticks finished tasks (`- [ ]` becomes `- [x]`).
4. Runs the health check.
5. Pushes safely to GitHub. The changes show up in your Obsidian within minutes.

```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/session-close.py --agent "Deal Analysis" --project "Deal Pipeline" \
  --summary "Screened 3 Atlanta deals" \
  --learned "ARV for 123 Main St is 250k (source: URL)" \
  --decision "Pass on 123 Main St - ROI 9%" \
  --task "Get rehab quote for 45 Oak Ave"
python3 $S/vault-health.py
bash $S/safe-push.sh "Deal Analysis" "session close: Deal Pipeline"
```

### 5.3 Tips
- You can also ask mid-task: "save this to Obsidian". That's the same as closing a session.
- A new deal goes to `Deals/<address>.md`, built from the template. A contact goes to `Contacts/<name>.md`. A meeting goes to `Meetings/YYYY-MM-DD <title>.md`.
- You can write notes in Obsidian as usual. They sync automatically, and the bots see them at their next session open.
- A task is a line starting with `- [ ]`. That's how every bot and the report recognize it.

## 6. The skills, one by one

### 6.1 vault-setup-interview
- **When:** "setup interview", "update profile", "add a project", or when session-open reports the profile is missing.
- **What:** up to 8 questions, one at a time: company and partners, markets, criteria, style and rules, bots, projects, facts and tasks.
- **Writes:** `00 Profile.md` and `Projects/<name>.md` from the templates. It records only what you said, with no guesses.
- You can run it again at any time. On a re-run, it asks only about what's missing or has changed.

### 6.2 session-open
- **When:** "open session <project>", or at the start of any substantial task.
- **What:** a pull, then the profile, project, bot log, open tasks, inbox and health, all in one token-cheap call.
- **Writes nothing.**

### 6.3 session-close
- **When:** "close session", "save to Obsidian", at the end of a task, or after an important decision or finding.
- **What:** a dated entry in the log and the project, finished tasks ticked, a health check, and a safe commit and push.
- **Iron rule:** append only; never delete other people's content. Only verified facts, each with a source.

### 6.4 vault-health-check
- **When:** "vault health check", before a large write, or when a close shows a WARN.
- **What:** broken links, notes missing frontmatter or `type:`, active projects not updated in 14 days, inbox notes older than 7 days, an open-task count, a secrets scan, and sync state.

### 6.5 vault-report
- **When:** "vault report", "what's the status in Obsidian".
- **What:** one self-contained HTML file in Hebrew that opens on a phone and offline. It covers health, notes per folder, projects, open tasks, each bot's activity and the 15 latest changes. It's saved to `_system/reports/vault-report.html`.

## 7. Health check and report

```bash
S=/home/box/shared/obsidian-vault/_system/grok-trestle/scripts
python3 $S/vault-health.py                 # full check
python3 $S/vault-health.py --stale-days 30 # looser staleness
python3 $S/secrets-scan.py                 # secrets only
python3 $S/vault-report.py                 # HTML report into the vault
```

| Result | Meaning | What to do |
|---|---|---|
| `OK` | Healthy | Nothing |
| `INFO` | Information (task count) | Nothing |
| `WARN FRONTMATTER` | Missing `---` block or `type:` | Copy the header from the matching template |
| `WARN LINKS` | `[[link]]` to a note that doesn't exist | Fix the name or create the note |
| `WARN STALE` | Active project not moving, or an old inbox note | Decide the next step or change `status:` |
| `WARN SYNC` | Changes not pushed | Close the session or run `safe-push.sh` |
| `FAIL SECRETS` | Something that looks like a password or token | **Do not push.** Delete it and leave a pointer instead |

Exit codes: 0 = healthy, 1 = WARN, 2 = FAIL.

## 8. Security rules

1. **Never** write passwords, tokens, API keys, card numbers or login details into the vault. Write only where they're stored, for example "password is in the owner's password manager".
2. `safe-push.sh` scans every commit. If it finds a secret, **nothing is pushed** and it returns `PUSH: BLOCKED`.
3. The scan is a safety net, not perfect protection (the original author says the same). The real rule is not to write secrets in the first place.
4. If a secret was already pushed to GitHub, deleting it isn't enough, because it stays in git history. **Revoke it and issue a new one** (rotate it).
5. The bots' token is limited to the `hs-obsidian` repo and to Contents only. Give each of your devices its own token, so you can revoke one without affecting the others.
6. The `_private/` folder is excluded from git (`.gitignore`), so nothing in it is ever pushed. Even so, it's better not to keep secrets there.
7. The repo must stay **Private**.
8. Tokens expire on the date you picked. Issue a new one before then, or syncing will stop.

## 9. Troubleshooting

| Problem | Fix |
|---|---|
| `PULL: FAIL` / `Authentication failed` | The token expired or was revoked. Issue a new one (section 4.2): for the bots, through Grok Bot; for Obsidian, in the plugin settings or the sign-in prompt |
| `PUSH: BLOCKED secrets found` | Delete the value from the file named and run it again. Nothing was pushed |
| `PUSH: FAIL ... conflict` | Two writers edited the same line. The bot runs `git status`, keeps both versions, runs `git add -A && git rebase --continue`, and pushes again |
| `could not get vault lock` | Another bot is writing right now. Try again in a minute |
| No updates showing in Obsidian | Command palette → **Git: Pull**. Make sure Auto pull is set |
| Conflict in Obsidian | The plugin flags the file. Open it, keep both versions, and run **Git: Commit-and-sync** |
| The phone crashes while cloning | Retry on Wi-Fi with free memory, or switch to GitSync / Working Copy (section 4.4) |
| `WARN LINKS` after renaming a note | In Obsidian, turn on Settings → Files and links → **Automatically update internal links** |

Manual check on the box:

```bash
git -C /home/box/shared/obsidian-vault status -sb
git -C /home/box/shared/obsidian-vault log --oneline -5
```

## 10. FAQ

**Do I need Claude Code, Node.js, or any install?**
No. Everything runs on the box with python3 and bash, which are already there. On your side you only need Obsidian and the Git plugin, plus Git itself on desktop.

**What if two bots close a session at the same moment?**
There's a lock. The second bot waits up to 120 seconds, runs `pull --rebase`, then pushes. If someone else pushed in the meantime, it retries up to 3 times.

**Can a bot delete my notes?**
The skills' rule is to append, not delete. Even if something gets deleted by mistake, it stays in git history and can be restored.

**Where can I see what each bot did?**
In `Agents/<bot name>.md`, or in the "bot activity" table of the status report.

**How do I add a new project?**
Tell a bot "add project X" (the setup interview), or copy `templates/project.md` into `Projects/`.

**How do I add a new bot?**
Add its name to the bots list in `00 Profile.md` and register the 5 skills for it. Its log is created automatically at its first session close.

**How much does it cost in tokens?**
Opening is one call and closing is 1–2 calls. It was designed to be cheap, like the original.

**Can I turn it off?**
Yes. Unregister the skills from the bots. The vault and your notes stay yours.

## Credit
Based on [trestle](https://github.com/liormesh/trestle) by Lior Meshullam, under the MIT license. The full text is in `LICENSE-trestle-MIT.txt`.
