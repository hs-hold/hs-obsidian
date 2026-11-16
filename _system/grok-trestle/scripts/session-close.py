#!/usr/bin/env python3
"""Close a session: append dated learnings / decisions / open tasks to the agent log
(Agents/<bot>.md) and, if given, to the project note (Projects/<project>.md, under "## Log").

Usage:
  session-close.py --agent "<bot name>" [--project "<project>"] [--summary "..."]
                   [--learned "..."]... [--decision "..."]... [--task "..."]... [--done "..."]...
  --done "<text>" ticks the first matching "- [ ] <text>" in the project note to "- [x]".
Then run: vault-health.py  and  safe-push.sh "<bot>" "session close: <project>"
Only appends - never deletes other people's content.
"""
import os, sys, argparse, datetime, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import VAULT, read

ap = argparse.ArgumentParser()
ap.add_argument("--agent", required=True); ap.add_argument("--project"); ap.add_argument("--summary", default="")
for k in ("learned", "decision", "task", "done"):
    ap.add_argument("--" + k, action="append", default=[])
a = ap.parse_args()
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
day = now[:10]
HERE = os.path.dirname(os.path.abspath(__file__))

def block(proj_link, checkbox=True):
    out = [f"\n### {now} — {a.agent}" + (f" — [[{proj_link}]]" if proj_link else "")]
    if a.summary: out.append(a.summary)
    out += [f"- Learned: {x}" for x in a.learned]
    out += [f"- Decision: {x}" for x in a.decision]
    out += [(f"- [ ] {x}" if checkbox else f"- Task (tracked in project): {x}") for x in a.task]
    out += [f"- Done: {x}" for x in a.done]
    return "\n".join(out) + "\n"

def set_updated(text):
    if text.startswith("---"):
        head, sep, rest = text[3:].partition("\n---")
        lines = head.split("\n")
        if any(l.startswith("updated:") for l in lines):
            lines = [f"updated: {day}" if l.startswith("updated:") else l for l in lines]
        else:
            lines.insert(len(lines) - 1 if lines and lines[-1] == "" else len(lines), f"updated: {day}")
        return "---" + "\n".join(lines) + sep + rest
    return text

proj_path = proj_link = None
if a.project:
    exact = os.path.join(VAULT, "Projects", a.project + ".md")
    c = [exact] if os.path.exists(exact) else [p for p in sorted(glob.glob(os.path.join(VAULT, "Projects", "*.md"))) if a.project.lower() in os.path.basename(p).lower()]
    if not c:
        sys.exit(f"Project '{a.project}' not found in Projects/. Create it from _system/grok-trestle/templates/project.md first.")
    proj_path = c[0]; proj_link = os.path.basename(proj_path)[:-3]

# agent log
agent_path = os.path.join(VAULT, "Agents", a.agent + ".md")
if not os.path.exists(agent_path):
    os.makedirs(os.path.dirname(agent_path), exist_ok=True)
    tpl = read(os.path.join(HERE, "..", "templates", "agent-log.md"))
    open(agent_path, "w", encoding="utf-8").write(tpl.replace("{{agent}}", a.agent).replace("{{date}}", day))
t = read(agent_path).rstrip("\n") + "\n" + block(proj_link, checkbox=not proj_path)
open(agent_path, "w", encoding="utf-8").write(set_updated(t))
print("WROTE", os.path.relpath(agent_path, VAULT))

if proj_path:
    t = read(proj_path)
    for d in a.done:
        i = t.find(f"- [ ] {d}")
        if i >= 0: t = t[:i] + "- [x]" + t[i+5:]
    if "\n## Log" not in t:
        t = t.rstrip("\n") + "\n\n## Log\n"
    # project log entries keep tasks as real checkboxes too
    t = t.rstrip("\n") + "\n" + block(None)
    open(proj_path, "w", encoding="utf-8").write(set_updated(t))
    print("WROTE", os.path.relpath(proj_path, VAULT))
