r"""Ueberarbeitung aus v4.9.0-r25 auf den modularen GitHub-Kandidaten uebertragen (neue Basis fuer 4.10).

Dieselben Eingriffe wie llm/aufraeumen_v490.py, aber auf die bisher eingefrorenen Fragmente
sources/research/parts/v470/*.tex angewandt. Das Archiv kommt in eine eigene Datei parts/v4100-archive.tex,
die Makros in parts/working-preamble.tex. Aufruf mit dem Pfad zu sources/research:
    python llm/aufraeumen_v410_github.py <.../sources/research>
"""
import glob
import io
import os
import re
import sys

ROOT = sys.argv[1]
FR = {}
for p in sorted(glob.glob(os.path.join(ROOT, "parts", "v470", "*.tex"))):
    FR[os.path.basename(p)] = io.open(p, encoding="utf-8", newline="").read()
ENVS = "theorem|proposition|corollary|lemma|definition|remark|conjecture"
edits = {k: [] for k in FR}
archive = []

def locate(s):
    hits = [(k, v.index(s)) for k, v in FR.items() if s in v]
    assert len(hits) == 1 and FR[hits[0][0]].count(s) == 1, (s[:60], [h[0] for h in hits])
    return hits[0]

def find_env(label):
    k, pos = locate("\\label{%s}" % label)
    t = FR[k]
    m = list(re.finditer(r"\\begin\{(" + ENVS + r")\}(\[(?:[^\[\]]|\[[^\]]*\])*\])?", t[:pos]))[-1]
    env = m.group(1)
    end = t.index("\\end{%s}" % env, pos) + len("\\end{%s}" % env)
    pend = end
    if re.match(r"\s*\\begin\{proof\}", t[end:]):
        pend = end + t[end:].index("\\end{proof}") + len("\\end{proof}")
    return k, m.start(), end, pend, env, (m.group(2) or "")[1:-1]

def status_box(text):
    return "\n\\qsstatus{%s}\n" % text

def do_archive(label, new_title, stub, verdict):
    k, s, end, pend, env, title = find_env(label)
    body = FR[k][s:pend].replace("\\label{%s}" % label, "", 1)
    edits[k].append((s, pend, "\\begin{%s}[%s]\\label{%s}\n%s\n\\emph{Archived in the v4.9.0 revision; original text in "
                     "\\S\\ref{sec:v490-archive}.}\n\\end{%s}" % (env, new_title, label, stub, env)))
    archive.append((label, env, title, verdict, body))

def do_status(label, text):
    k, _, _, pend, _, _ = find_env(label)
    edits[k].append((pend, pend, status_box(text)))

def do_replace(old, new):
    k, i = locate(old)
    edits[k].append((i, i + len(old), new))

def after(anchor, text):
    k, i = locate(anchor)
    edits[k].append((i + len(anchor), i + len(anchor), status_box(text)))

exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "revision_spec_v490.py"), encoding="utf-8").read())

for k, es in edits.items():
    if not es:
        continue
    es.sort()
    for a, b in zip(es, es[1:]):
        assert a[1] <= b[0], (k, a[:2], b[:2])
    t = FR[k]; out = []; last = 0
    for s, e, rep in es:
        out.append(t[last:s]); out.append(rep); last = e
    out.append(t[last:])
    io.open(os.path.join(ROOT, "parts", "v470", k), "w", encoding="utf-8", newline="").write("".join(out))
    print("%-40s %d Eingriffe" % (k, len(es)))

io.open(os.path.join(ROOT, "parts", "v4100-archive.tex"), "w", encoding="utf-8", newline="").write(archive_tex(archive))
print("Archiv: %d Eintraege" % len(archive))
