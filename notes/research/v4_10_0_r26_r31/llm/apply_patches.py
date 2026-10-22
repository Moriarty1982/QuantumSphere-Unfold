r"""Wendet Ueberarbeitungs-Patches (Liste exakter (alt, neu)-Paare) auf eine Datei oder alle .tex eines Ordners an.

Aufruf: python llm/apply_patches.py <datei oder Ordner> <spec.py>
Jedes alte Textstueck muss genau einmal im Ziel vorkommen; sonst bricht das Skript ab, ohne etwas zu schreiben.
"""
import glob
import io
import os
import sys

target, spec = sys.argv[1], sys.argv[2]
ns = {}
exec(io.open(spec, encoding="utf-8").read(), ns)
files = [target] if os.path.isfile(target) else sorted(glob.glob(os.path.join(target, "**", "*.tex"), recursive=True))
texts = {f: io.open(f, encoding="utf-8", newline="").read() for f in files}
plan = []
for old, new in ns["PATCHES"]:
    hits = [(f, t.count(old)) for f, t in texts.items() if old in t]
    assert len(hits) == 1 and hits[0][1] == 1, ("Fundstellen", old[:70], hits)
    plan.append((hits[0][0], old, new))
for f, old, new in plan:
    texts[f] = texts[f].replace(old, new, 1)
for f in {p[0] for p in plan}:
    io.open(f, "w", encoding="utf-8", newline="").write(texts[f])
    print("geaendert:", f)
