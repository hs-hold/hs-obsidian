#!/usr/bin/env python3
"""Build `00 Memory.md` at the vault root: one compressed, always-fresh memory file.

Deterministic, stdlib only, no network/LLM calls. Overwrites the file on every run.
Sources: Agents/*.md, 00 Profile.md, Projects/*.md, Notes/Daily/*.md (last N days),
and (optional, read-only) bot profiles at /home/box/agent-data/agents/*/profile.json.

Usage: python3 _system/scripts/build_memory_file.py [--days 7] [--out "00 Memory.md"]
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import re
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo

VAULT = Path(__file__).resolve().parents[2]
TZ = ZoneInfo("Asia/Jerusalem")
PROFILES_GLOB = "/home/box/agent-data/agents/*/profile.json"
BACKFILL_MARK = "one-time vault backfill"
SECRET_RE = re.compile(
    r"(gh[pousr]_[A-Za-z0-9]{20,}|github_pat_\w{20,}|sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
    r"eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}|xox[abpr]-[A-Za-z0-9-]{10,}|\b\d{13,19}\b|"
    r"(?i:password|passwd|api[_ -]?key|secret|token)\s*[:=]\s*\S{6,})"
)
DATE_RE = re.compile(r"(20\d\d-\d\d-\d\d)")
SCHED_RE = re.compile(r"\b(routine|reminders?|weekly|cron|check-in|drip|daily (?:search|run|scan|routine)|twice-daily|morning update)\b", re.I)

# Daily-note heading -> category
CATS = [
    ("decision", "decisions"),
    ("conclusion", "conclusions"),
    ("info from the owner", "owner"),
    ("agent work", "agents"),
    ("what happened", "happened"),
    ("open", "open"),
    ("gap", "skip"),
]
OUTCOME_ORDER = ["decisions", "owner", "conclusions", "happened", "agents"]
OUTCOME_LABEL = {"decisions": "D", "owner": "Owner", "conclusions": "C", "happened": "H", "agents": "A"}

# 00 Profile.md sections that hold owner rules / criteria
PROFILE_RULE_SECTIONS = [
    "deal criteria", "financing", "analysis rules", "buy box", "how the deals site",
    "deal-search pipeline", "off-market", "how bots should work",
]


# ---------------------------------------------------------------- helpers
def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def strip_frontmatter(text: str) -> tuple[dict, str]:
    fm: dict = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"')
            text = text[end + 4:]
    return fm, text


def sections(text: str) -> list[tuple[list[str], list[str]]]:
    """Return [(heading_path, body_lines)] for every heading (path = [h1.., hN])."""
    out: list[tuple[list[str], list[str]]] = []
    path: list[tuple[int, str]] = []
    cur: list[str] = []
    out.append(([], cur))
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            lvl = len(m.group(1))
            path = [p for p in path if p[0] < lvl] + [(lvl, m.group(2).strip())]
            cur = []
            out.append(([h for _, h in path], cur))
        else:
            cur.append(line)
    return out


def bullets(lines: list[str]) -> list[str]:
    """Top-level bullets, with nested bullets folded into the parent ("; ")."""
    items: list[str] = []
    for line in lines:
        if re.match(r"^- ", line):
            items.append(line[2:].strip())
        elif re.match(r"^\s{2,}[-*] ", line) and items:
            items[-1] += "; " + line.strip()[2:].strip()
        elif re.match(r"^\s{2,}\S", line) and items and not line.strip().startswith("#"):
            items[-1] += " " + line.strip()
    return [i for i in items if i]


def clean(s: str, limit: int = 240) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("**", "")
    if len(s) > limit:
        cut = s[:limit].rsplit(" ", 1)[0]
        s = cut.rstrip(",;:") + " …"
    return s


def norm_key(s: str) -> str:
    s = re.sub(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]", r"\1", s.lower())
    s = re.sub(r"^\[[ x]\]\s*", "", s)
    s = re.sub(r"\(([^)]*\d\d:\d\d[^)]*|owner,? [^)]*)\)", "", s)
    s = re.sub(r"[^\w\u0590-\u05ff$%]+", " ", s)
    return " ".join(s.split())[:70]


def dedupe(items, key=lambda x: x):
    seen, out = set(), []
    for it in items:
        k = norm_key(key(it))
        if k and k not in seen:
            seen.add(k)
            out.append(it)
    return out


def git_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(VAULT), "log", "-1", "--format=%h %cd", "--date=format:%Y-%m-%d %H:%M"],
            text=True, stderr=subprocess.DEVNULL, env={"TZ": "Asia/Jerusalem", "PATH": "/usr/bin:/bin"},
        ).strip()
    except Exception:
        return "unknown"


# ---------------------------------------------------------------- loaders
def load_profiles() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for p in sorted(glob.glob(PROFILES_GLOB)):
        try:
            d = json.loads(Path(p).read_text(encoding="utf-8"))
        except Exception:
            continue
        if d.get("name"):
            out[d["name"]] = d
    return out


def daily_notes(days: int, today: dt.date) -> list[tuple[dt.date, Path]]:
    out = []
    for p in sorted((VAULT / "Notes" / "Daily").glob("*.md")):
        try:
            d = dt.date.fromisoformat(p.stem[:10])
        except ValueError:
            continue
        if (today - d).days < days:
            out.append((d, p))
    return out


def categorize(path: list[str]) -> str | None:
    for h in reversed(path):
        hl = h.lower()
        for kw, cat in CATS:
            if kw in hl:
                return cat
    return None


def parse_daily(p: Path) -> dict[str, list[str]]:
    _, body = strip_frontmatter(read(p))
    res: dict[str, list[str]] = {}
    for path, lines in sections(body):
        cat = categorize(path)
        for b in bullets(lines):
            if b.startswith("[x]") or b.startswith("[X]"):
                continue
            c = "open" if b.startswith("[ ]") else cat
            if c and c != "skip":
                res.setdefault(c, []).append(re.sub(r"^\[ \]\s*", "", b))
    return res


# ---------------------------------------------------------------- bot blocks
BOILER_RE = re.compile(r"reply in hebrew|replies in hebrew|writes in hebrew|^at the start of every|change that file|"
                       r"speaks hebrew|^always speaks", re.I)


def compact_description(desc: str) -> tuple[str, str]:
    """(role, job) from a bot's profile description: first sentence + first substantive sentences."""
    text = re.sub(r"(?:\s+for)?,?\s+a small (?:US )?real estate investment LLC[^.]*?(?=\.|$)", "", desc)
    text = re.sub(r" for H\.S HOLDINGS| for a small real estate investment LLC", "", text)
    text = re.sub(r"\s*\((?:partners|flip and)[^)]*\)", "", text)
    sents = [x.strip() for x in re.split(r"(?<=\.)\s+|\n+", text) if x.strip()]
    role = sents[0] if sents else ""
    m = re.search(r"(?:Your job|Job):\s*(.+?)(?:\n|$)", text)
    if m:
        return role, m.group(1)
    rest = [x for x in sents[1:] if not BOILER_RE.search(x) and len(x) > 25]
    return role, " ".join(rest[:2])


def bot_block(name: str, note: Path | None, prof: dict | None, profile_text: str,
              dailies: list[tuple[dt.date, dict, str]], rule_bullets: list[str]) -> list[str]:
    out = [f"### {name}" + (f" — [[{name}]]" if note else " — (no Agents/ note)")]
    desc = (prof or {}).get("description", "")
    role, job = compact_description(desc) if desc else ("", "")
    m = re.search(r"\[\[" + re.escape(name) + r"\]\]\s*\(([^)]*)\)", profile_text)
    tag = m.group(1) if m else ""
    if name == "Grok Bot" or len(desc) < 100:
        role = (tag + "; " if tag else "") + "coordinates the other bots, the deals site/pipeline, the vault and Drive library; talks to the owner (chat + voice)."
        job = ""
    elif tag and tag.lower() not in role.lower():
        role = f"{tag}; {role}"
    if role:
        out.append(f"- Role: {clean(role, 260)}")
    if job:
        out.append(f"- Job: {clean(job, 300)}")
    text_all = desc + "\n" + (read(note) if note else "")
    paths = dedupe(re.findall(r"/home/box/shared/[\w\-./<>]+[\w>]", text_all))
    if paths:
        out.append("- Rules/data: " + ", ".join(f"`{p}`" for p in paths[:4]))
    # Owner rules naming this bot
    pat = re.compile(r"\[\[" + re.escape(name) + r"\]\]|\b" + re.escape(name) + r"\b")
    rules = [r for r in rule_bullets if pat.search(r)]
    for r in rules[:3]:
        out.append(f"- Rule: {clean(r, 220)}")
    # Schedules / routines mentioning this bot (profile + recent dailies)
    sched: list[str] = []
    for r in rule_bullets:
        if pat.search(r) and SCHED_RE.search(r) and r not in rules[:3]:
            sched.append(r)
    for d, parsed, _ in dailies:
        for b in parsed.get("open", []) + parsed.get("decisions", []):
            if pat.search(b) and SCHED_RE.search(b):
                sched.append(b)
    for s in dedupe(sched)[:2]:
        out.append(f"- Schedule: {clean(s, 200)}")
    # Status: latest real ### entry in Agents note
    last_dates: list[str] = []
    if note:
        fm, body = strip_frontmatter(read(note))
        if fm.get("updated"):
            last_dates.append(fm["updated"][:10])
        entries = [(path, lines) for path, lines in sections(body) if len(path) >= 2 and path[-1]]
        real = [e for e in entries if BACKFILL_MARK not in e[0][-1]]
        for path, _ in entries:
            last_dates += DATE_RE.findall(path[-1])
        if real:
            h, lines = real[-1]
            bl = [b for b in bullets(lines) if not b.startswith("[")]
            txt = " ".join(bl) if bl else " ".join(l.strip() for l in lines if l.strip())
            out.append(f"- Latest log ({clean(h[-1], 60)}): {clean(txt, 300)}")
        todos = re.findall(r"^- \[ \] (.+)$", body, re.M)
        for t in todos[:3]:
            out.append(f"- Open: {clean(t, 160)}")
    # Recent mentions in daily notes, "(Bot ...)" prefix
    mpat = re.compile(r"^\(" + re.escape(name) + r"[ ,)]")
    recent = []
    for d, parsed, ref in dailies:
        for cat in ("agents", "conclusions", "decisions", "happened"):
            for b in parsed.get(cat, []):
                if mpat.match(b):
                    recent.append((d, ref, b))
    if recent:
        last_dates.append(recent[-1][0].isoformat())
        for d, ref, b in recent[-2:]:
            out.append(f"- Recent ({ref}): {clean(b, 220)}")
    out.append(f"- Last activity seen in vault: {max(last_dates) if last_dates else 'unknown'}")
    return out


# ---------------------------------------------------------------- main
def build(days: int) -> tuple[str, list[str]]:
    now = dt.datetime.now(TZ)
    today = now.date()
    gaps: list[str] = []

    _, profile_body = strip_frontmatter(read(VAULT / "00 Profile.md"))
    rule_bullets: list[str] = []
    for path, lines in sections(profile_body):
        if path and any(k in path[-1].lower() for k in PROFILE_RULE_SECTIONS):
            rule_bullets += bullets(lines)
    project_decisions: list[tuple[str, str]] = []
    project_open: list[tuple[str, str]] = []
    for p in sorted((VAULT / "Projects").glob("*.md")):
        _, body = strip_frontmatter(read(p))
        for path, lines in sections(body):
            if not path:
                continue
            h = path[-1].lower()
            if h.startswith("decisions"):
                project_decisions += [(p.stem, b) for b in bullets(lines)]
            elif h.startswith("open") or "known gaps" in h:
                for line in lines:
                    m = re.match(r"^(?:- \[ \] |\d+\. )(.+)", line)
                    if m:
                        pre = "Known gap: " if "known gaps" in h else ""
                        project_open.append((p.stem, pre + m.group(1)))

    dailies = []
    for d, p in daily_notes(days, today):
        dailies.append((d, parse_daily(p), f"[[{p.stem}]]"))

    # Bots
    agent_notes = {p.stem: p for p in sorted((VAULT / "Agents").glob("*.md"))}
    profiles = load_profiles()
    if not profiles:
        gaps.append("bot profile.json files not readable; roles come from vault only")
    listed = re.findall(r"^- \[\[([^\]]+)\]\]", profile_body.split("## Bots", 1)[-1].split("\n## ", 1)[0], re.M)
    names = []
    for n in listed + sorted(agent_notes) + sorted(profiles):
        if n not in names:
            names.append(n)
    for n in names:
        if n not in agent_notes:
            gaps.append(f"bot '{n}' has no Agents/ note")
        if profiles and n not in profiles:
            gaps.append(f"bot '{n}' has no readable profile.json")

    L: list[str] = []
    L += ["---", "type: memory", "generated: true", "tags: [memory]", "---",
          "# 00 Memory — compressed team brain",
          f"Generated {now:%Y-%m-%d %H:%M} Asia/Jerusalem from commit {git_head()} by "
          "`_system/scripts/build_memory_file.py`. Do not edit by hand (overwritten every run).",
          "Read this first. If a topic is missing, search the vault (folder map at the bottom), then answer.", ""]

    L.append(f"## Bots ({len(names)})")
    for n in names:
        L += bot_block(n, agent_notes.get(n), profiles.get(n), profile_body, dailies, rule_bullets)
    L.append("")

    L.append("## Owner rules & active criteria (from [[00 Profile]] + project decisions)")
    for b in dedupe(rule_bullets):
        L.append(f"- {clean(b, 260)}")
    for src, b in dedupe(project_decisions, key=lambda x: x[1]):
        if norm_key(b) not in {norm_key(r) for r in rule_bullets}:
            L.append(f"- {clean(b, 220)} ([[{src}]])")
    L.append("")

    L.append(f"## Open decisions / items (last {days} days + projects; unchecked only)")
    opens: list[tuple[str, str]] = []
    for d, parsed, ref in reversed(dailies):
        opens += [(ref, b) for b in parsed.get("open", [])]
    opens += [(f"[[{s}]]", b) for s, b in project_open]
    for ref, b in dedupe(opens, key=lambda x: x[1]):
        L.append(f"- {clean(b, 200)} — {ref}")
    L.append("")

    L.append(f"## Key recent outcomes (last {days} days, newest first; D=decision, Owner=owner info, C=conclusion, H=happened, A=agent work)")
    all_out = []
    for d, parsed, ref in reversed(dailies):
        day = []
        for cat in OUTCOME_ORDER:
            for b in parsed.get(cat, []):
                if re.match(r"^(none|no new)\b", b, re.I):
                    continue
                day.append((cat, b))
        day = dedupe(day, key=lambda x: x[1])
        day = [x for x in day if norm_key(x[1]) not in {norm_key(y[1]) for y in all_out}]
        all_out += day
        if day:
            L.append(f"### {ref}")
            for cat, b in day:
                L.append(f"- {OUTCOME_LABEL[cat]}: {clean(b, 200)}")
    L.append("")

    L.append("## Where to look (folder map)")
    L.append("[[00 Profile]] rules/criteria · Agents/ bot logs · Projects/ project notes "
             "(pipeline: [[Deal Pipeline - How It Works]]) · Notes/Daily/ daily notes · Deals/ one note per property · "
             "Markets/ Atlanta + Indianapolis zip notes · Contacts/ · Meetings/ · Learning/ course notes · "
             "00 Inbox/ · _system/ tooling. Box-only rules: `/home/box/shared/agent-rules/`.")
    if gaps:
        L.append("")
        L.append("## Gaps in sources")
        L += [f"- {g}" for g in gaps]

    text = "\n".join(L).rstrip() + "\n"
    # Safety: never emit secret-looking strings.
    text = SECRET_RE.sub("[redacted]", text)
    return text, gaps


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", default="00 Memory.md")
    a = ap.parse_args()
    text, gaps = build(a.days)
    out = VAULT / a.out
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out} ({text.count(chr(10))} lines, {len(text)} bytes; gaps: {len(gaps)})")


if __name__ == "__main__":
    main()
