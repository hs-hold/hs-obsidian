#!/usr/bin/env python3
"""Tiny Markdown -> self-contained mobile HTML converter (stdlib only) used for the guides.
Usage: build-guide.py IN.md OUT.html --dir rtl|ltr --title "..."
Supports: # headings (TOC from ##), fenced code (always LTR, copy button), tables, - / 1. lists,
> notes, **bold**, `code`, [text](url), paragraphs.
"""
import re, sys, html, argparse
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--dir", default="ltr"); ap.add_argument("--title", default="Guide"); ap.add_argument("--copy", default="Copy")
a = ap.parse_args()
E = html.escape
def inline(t):
    parts = re.split(r"(`[^`]+`)", t); out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append(f"<code>{E(p[1:-1])}</code>"); continue
        p = E(p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", p)
        p = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', p)
        out.append(p)
    return "".join(out)
lines = open(a.src, encoding="utf-8").read().splitlines()
body, toc, i, n = [], [], 0, 0
while i < len(lines):
    l = lines[i]
    if l.startswith("```"):
        j = i + 1; code = []
        while j < len(lines) and not lines[j].startswith("```"):
            code.append(lines[j]); j += 1
        n += 1
        body.append(f'<div class="code"><button onclick="cp(\'c{n}\',this)">{E(a.copy)}</button><pre dir="ltr" id="c{n}">{E(chr(10).join(code))}</pre></div>')
        i = j + 1; continue
    m = re.match(r"^(#{1,4}) (.*)", l)
    if m:
        lvl = len(m.group(1)); txt = m.group(2); hid = f"s{len(toc)+1}"
        if lvl == 2: toc.append((hid, txt))
        body.append(f'<h{lvl} id="{hid}">{inline(txt)}</h{lvl}>'); i += 1; continue
    if l.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].startswith("|"):
            if not re.match(r"^\|[\s:|-]+\|$", lines[i]): rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
            i += 1
        h = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
        b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
        body.append(f'<div class="tw"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'); continue
    if re.match(r"^\s*([-*]|\d+\.) ", l):
        mm = re.match(r"^\s*(\d+)\.", l); tag = "ol" if mm else "ul"; items = []
        start = f' start="{mm.group(1)}"' if mm and mm.group(1) != "1" else ""
        while i < len(lines) and re.match(r"^\s*([-*]|\d+\.) ", lines[i]):
            ind = len(lines[i]) - len(lines[i].lstrip())
            items.append(f'<li{" class=sub" if ind >= 2 else ""}>{inline(re.sub(r"^\s*([-*]|\d+\.) ", "", lines[i]))}</li>'); i += 1
        body.append(f"<{tag}{start}>{''.join(items)}</{tag}>"); continue
    if l.startswith(">"):
        q = []
        while i < len(lines) and lines[i].startswith(">"):
            q.append(lines[i].lstrip("> ")); i += 1
        body.append(f'<div class="note">{inline(" ".join(q))}</div>'); continue
    if l.strip():
        p = [l]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|```|\||>|\s*([-*]|\d+\.) )", lines[i]):
            p.append(lines[i]); i += 1
        body.append(f"<p>{inline(' '.join(p))}</p>"); continue
    i += 1
tochtml = "".join(f'<li><a href="#{h}">{inline(t)}</a></li>' for h, t in toc)
lang = "he" if a.dir == "rtl" else "en"
doc = f"""<!doctype html><html lang="{lang}" dir="{a.dir}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(a.title)}</title><style>
:root{{--b:#d0d7de;--bg:#f6f8fa;--acc:#0969da}}*{{box-sizing:border-box}}
body{{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Arial,sans-serif;background:var(--bg);color:#1f2328;line-height:1.6;font-size:16px}}
header{{position:sticky;top:0;z-index:5;background:#24292f;color:#fff;padding:10px 14px;font-weight:600}}
main{{max-width:860px;margin:auto;padding:10px 14px 60px}}
h1{{font-size:1.5em}}h2{{font-size:1.25em;border-bottom:2px solid var(--b);padding-bottom:4px;margin-top:30px}}h3{{font-size:1.07em;margin-top:20px}}
nav{{background:#fff;border:1px solid var(--b);border-radius:10px;padding:8px 12px}}nav ol{{margin:4px 0;padding-inline-start:22px}}
a{{color:var(--acc)}}code{{background:#eaeef2;border-radius:4px;padding:1px 5px;font-size:.9em;direction:ltr;unicode-bidi:isolate;word-break:break-word}}
.code{{position:relative;margin:8px 0}}pre{{background:#0d1117;color:#e6edf3;padding:12px;border-radius:8px;overflow-x:auto;font-size:.85em;text-align:left;margin:0;white-space:pre}}
.code button{{position:absolute;top:6px;{'left' if a.dir=='rtl' else 'right'}:6px;background:#30363d;color:#fff;border:0;border-radius:6px;padding:4px 10px;font-size:.8em;cursor:pointer}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;background:#fff;margin:8px 0}}th,td{{border:1px solid var(--b);padding:6px 8px;text-align:start;vertical-align:top;font-size:.93em}}th{{background:#eaeef2}}
.note{{background:#fff8c5;border:1px solid #d4a72c;border-radius:8px;padding:8px 12px;margin:10px 0}}li.sub{{margin-inline-start:22px;list-style:circle}}li{{margin:3px 0}}
</style></head><body><header>{E(a.title)}</header><main><nav><b>{'תוכן עניינים' if a.dir=='rtl' else 'Contents'}</b><ol>{tochtml}</ol></nav>
{chr(10).join(body)}</main><script>
function cp(id,b){{var t=document.getElementById(id).innerText,o=b.innerText;function ok(){{b.innerText='✓';setTimeout(function(){{b.innerText=o}},1200)}}
if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(t).then(ok,fb)}}else fb();
function fb(){{var x=document.createElement('textarea');x.value=t;document.body.appendChild(x);x.select();try{{document.execCommand('copy');ok()}}catch(e){{}}document.body.removeChild(x)}}}}
</script></body></html>"""
open(a.out, "w", encoding="utf-8").write(doc); print("BUILT", a.out)
