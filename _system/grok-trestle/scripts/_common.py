"""Shared helpers for grok-trestle scripts (python3 stdlib only)."""
import os, re, subprocess, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = os.environ.get("VAULT") or os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules"}

# Credential shapes (adapted from trestle tools/lib.mjs, MIT) + a few extras.
SECRET_RE = re.compile("|".join([
    r"sk-ant-[A-Za-z0-9_-]{20,}",
    r"sk-(?:proj-)?[A-Za-z0-9_-]{32,}",
    r"ghp_[A-Za-z0-9]{30,}", r"gho_[A-Za-z0-9]{30,}", r"ghs_[A-Za-z0-9]{30,}",
    r"github_pat_[A-Za-z0-9_]{30,}", r"glpat-[A-Za-z0-9_-]{20,}",
    r"xox[baprs]-[A-Za-z0-9-]{10,}",
    r"AKIA[0-9A-Z]{16}",
    r"AIza[0-9A-Za-z_-]{30,}",
    r"eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}",
    r"whsec_[A-Za-z0-9]{20,}", r"[sr]k_live_[A-Za-z0-9]{20,}",
    r"sbp_[A-Za-z0-9]{20,}", r"npm_[A-Za-z0-9]{30,}",
    r"(?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^:/\s]+:[^@\s]{6,}@",
    r"https?://[^/\s:@]+:[^@\s/]{6,}@",            # basic-auth in URL
    r"\b[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    r"(?i:x-rapidapi-key)\s*[:=]\s*['\"]?[A-Za-z0-9]{30,}",
    r"\b(?i:password|passwd|pwd|api[_-]?key|secret|token)\s*[:=]\s*['\"]?(?=[^\s'\"<>*]*\d)(?=[^\s'\"<>*]*[A-Za-z])[^\s'\"<>*]{8,}",
    r"\b(?:\d[ -]?){15,16}\b(?=.*(?i:card|visa|master|amex|כרטיס))",
]))

def mask(v):
    return f"{v[:6]}...({len(v)} chars)"

def md_files(root=VAULT, include_system=False):
    for d, dirs, files in os.walk(root):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        rel = os.path.relpath(d, root)
        if not include_system and (rel == "_system" or rel.startswith("_system" + os.sep)):
            continue
        for f in sorted(files):
            if f.endswith(".md"):
                yield os.path.join(d, f)

def read(p):
    with open(p, encoding="utf-8", errors="replace") as fh:
        return fh.read()

def frontmatter(text):
    """Return dict of top-level YAML keys, or None if no frontmatter block."""
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\s*\n(.*?)\n---\s*(\n|$)", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if mm:
            out[mm.group(1)] = re.sub(r"\s+#.*$", "", mm.group(2)).strip().strip("'\"")
    return out

def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)

def git(*args):
    r = subprocess.run(["git", "-C", VAULT, *args], capture_output=True, text=True)
    return r.stdout.strip()

def today():
    return datetime.date.today()

def parse_date(s):
    try:
        return datetime.date.fromisoformat(str(s)[:10])
    except Exception:
        return None
