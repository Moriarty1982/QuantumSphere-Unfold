"""Stichwortsuche über families.json als Gegenkontrolle zur Lesesichtung.

Aufruf: python -I keyword_screen.py <ordner_mit_families.json>
"""
import json
import os
import re
import sys

fams = json.load(open(os.path.join(sys.argv[1], "families.json"), encoding="utf-8"))
groups = {
    "OP1 Zählung/Fraktal/LQG": r"immirzi|loop quantum|spin network|black hole entrop|area spectrum|moran|hausdorff dimension|self-similar|fractal|microcanonical|SL\(2,\s*\\?mathbb ?C\)|principal series",
    "OP2 Operator": r"self-adjoint|deficiency ind|berry.?keating|xp operator|dilation operator|hardy space|essential(ly)? self",
    "OP3/OP4 Algebra/Generationen": r"octonion|sedenion|cayley.?dickson|triality|spin\(8\)|dixon|hurwitz|binary tetrahedral|koide|mutually unbiased|SIC|bargmann|geometric phase|gram matri|neutrino|mixing matri|exceptional jordan|E_?8|G_?2",
    "OP5 PDE/Integrabilität": r"cartan.?k[aä]hler|involutiv|spencer|formal(ly)? integrab|prolongation|overdetermined|jet space|exterior differential system",
    "OP5 Gravitation/Λ": r"cosmological constant|de sitter|unimodular|vacuum energy|massive gravit|fierz|bigravit|einstein equation|einstein.?cartan|lorentzian|causal|light ?cone|hyperbolic pde|wave equation|nambu|string",
    "C5/C6 Nullen/Terminierung": r"finite.?time extinction|extinction|finite time|lyapunov|terminat|certificate|undecidab|polarization singular|riemann.?silberstein|optical vortex|nodal set|zero set",
    "Q1/Q2 Zeitpfeil/Spinoren": r"time revers|arrow of time|orientation|spinor|dirac operator|clifford|fierz identit",
    "RH": r"riemann hypothesis|zeta|zero.?free|l-function|explicit formula|weil positiv|de bruijn|newman|davenport|pair correlation|GUE|random matri|hilbert.?p[oó]lya|connes|adele",
    "Werkzeuge": r"\bSAT\b|exponential time hypothesis|automat|circuit|quantum circuit|lean",
}
for g, pat in groups.items():
    rx = re.compile(pat, re.I)
    hits = []
    for f in fams:
        blob = " ".join([f["title"], f["desc"]] + [p["title"] + " " + p["abstract"] for p in f["papers"]])
        found = sorted({m.group(0).lower() for m in rx.finditer(blob)})
        if found:
            hits.append(f"{f['nr']} {f['title'][:70]} [{', '.join(found[:4])}]")
    print(f"\n=== {g}: {len(hits)}")
    for h in hits:
        print("  ", h)
