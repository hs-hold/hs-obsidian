#!/usr/bin/env python3
"""Generate a self-contained HTML status report of the vault (Hebrew, RTL, mobile-friendly).

Usage: vault-report.py [--out PATH]   (default: <vault>/_system/reports/vault-report.html)
Contents: health check, notes per folder, projects (status/updated), open tasks, agent activity,
last 15 commits. No external CSS/JS; opens offline and in Obsidian.
"""
import os, re, sys, html, argparse, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import VAULT, md_files, read, frontmatter, strip_code, git
import importlib.util
spec = importlib.util.spec_from_file_location("vh", os.path.join(os.path.dirname(os.path.abspath(__file__)), "vault-health.py"))
vh = importlib.util.module_from_spec(spec); sys.argv = sys.argv[:1] + [a for a in sys.argv[1:]]; spec.loader.exec_module(vh)

ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(VAULT, "_system", "reports", "vault-report.html"))
a = ap.parse_args()
E = html.escape
health = vh.run()
files = list(md_files())
folders, projects, tasks, agents = {}, [], [], []
for p in files:
    rel = os.path.relpath(p, VAULT); top = rel.split(os.sep)[0] if os.sep in rel else "(root)"
    folders[top] = folders.get(top, 0) + 1
    t = read(p); fm = frontmatter(t) or {}
    if rel.startswith("Projects" + os.sep):
        projects.append((os.path.basename(rel)[:-3], fm.get("status", "?"), fm.get("updated") or fm.get("date") or "?", fm.get("owner", "")))
    if rel.startswith("Agents" + os.sep):
        heads = re.findall(r"^### (\d{4}-\d{2}-\d{2} \d{2}:\d{2})", t, re.M)
        agents.append((os.path.basename(rel)[:-3], heads[-1] if heads else "-", len(heads)))
    for line in strip_code(t).splitlines():
        if re.match(r"^\s*[-*] \[ \]\s*\S", line):
            tasks.append((rel[:-3], line.strip()[6:]))
commits = [l.split("\x1f") for l in git("log", "-15", "--date=format-local:%Y-%m-%d %H:%M", "--pretty=%h\x1f%ad\x1f%s").splitlines() if l]
color = {"OK": "#1a7f37", "INFO": "#0969da", "WARN": "#9a6700", "FAIL": "#cf222e"}

def table(head, rows):
    h = "".join(f"<th>{E(x)}</th>" for x in head)
    b = "".join("<tr>" + "".join(f"<td>{E(str(c))}</td>" for c in r) + "</tr>" for r in rows) or f'<tr><td colspan="{len(head)}">אין</td></tr>'
    return f"<div class=tw><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>"

hrows = ""
for k, (lvl, s, det) in health.items():
    d = "".join(f"<li>{E(x)}</li>" for x in det[:20])
    hrows += f'<div class=card><b style="color:{color[lvl]}">{lvl}</b> <code>{k}</code> — {E(s)}' + (f"<ul dir=ltr>{d}</ul>" if d else "") + "</div>"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
doc = f"""<!doctype html><html lang=he dir=rtl><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>דוח מצב כספת — {now}</title><style>
body{{font-family:system-ui,-apple-system,"Segoe UI",Arial,sans-serif;margin:0;background:#f6f8fa;color:#1f2328;line-height:1.5}}
header{{position:sticky;top:0;background:#24292f;color:#fff;padding:10px 14px}}main{{padding:12px;max-width:900px;margin:auto}}
h2{{font-size:1.1em;margin:18px 0 6px}}.card{{background:#fff;border:1px solid #d0d7de;border-radius:8px;padding:8px 10px;margin:6px 0}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;background:#fff}}th,td{{border:1px solid #d0d7de;padding:5px 7px;text-align:start;font-size:.92em}}
th{{background:#eaeef2}}code{{background:#eaeef2;padding:0 4px;border-radius:4px;direction:ltr;unicode-bidi:embed}}.kpi{{display:flex;gap:8px;flex-wrap:wrap}}
.kpi div{{flex:1;min-width:110px;background:#fff;border:1px solid #d0d7de;border-radius:8px;padding:8px;text-align:center}}.kpi b{{display:block;font-size:1.5em}}
</style></head><body><header><b>H.S HOLDINGS — דוח מצב כספת</b><br><small>{now} (שעון ישראל)</small></header><main>
<div class=kpi><div><b>{len(files)}</b>פתקים</div><div><b>{len(projects)}</b>פרויקטים</div><div><b>{len(tasks)}</b>משימות פתוחות</div><div><b>{len(agents)}</b>יומני בוטים</div></div>
<h2>בדיקת בריאות</h2>{hrows}
<h2>פתקים לפי תיקייה</h2>{table(["תיקייה","פתקים"], sorted(folders.items()))}
<h2>פרויקטים</h2>{table(["פרויקט","סטטוס","עודכן","אחראי"], projects)}
<h2>משימות פתוחות</h2>{table(["פתק","משימה"], tasks[:100])}
<h2>פעילות בוטים</h2>{table(["בוט","רישום אחרון","מספר רישומים"], agents)}
<h2>15 השינויים האחרונים</h2>{table(["commit","זמן","תיאור"], commits)}
<p><small>נוצר אוטומטית ע"י <code>_system/grok-trestle/scripts/vault-report.py</code></small></p></main></body></html>"""
os.makedirs(os.path.dirname(a.out), exist_ok=True)
open(a.out, "w", encoding="utf-8").write(doc)
print("REPORT:", os.path.relpath(a.out, VAULT) if a.out.startswith(VAULT) else a.out)
