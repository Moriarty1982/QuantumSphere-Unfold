"""k21: Wie bricht die Fano-Symmetrie? Reine Gruppen-/Geometrierechnung, kein Datenvergleich.
GL(3,2) wirkt auf die Fano-Ebene (7 Punkte = F2^3 ohne 0, 7 Linien). Stab(P) wirkt treu auf die
4 Linien nicht durch P -> S4; daraus die 3-dim. Darstellung (Summe-Null-Unterraum)."""
import itertools, numpy as np
from collections import Counter, defaultdict

pts = [np.array(v) for v in itertools.product((0, 1), repeat=3) if any(v)]
key = lambda v: tuple(int(x) % 2 for x in v)
lines = sorted({frozenset([key(a), key(b), key((a + b) % 2)]) for a in pts for b in pts if key(a) != key(b)},
               key=sorted)
G = [np.array(m).reshape(3, 3) for m in itertools.product((0, 1), repeat=9)
     if round(np.linalg.det(np.array(m).reshape(3, 3))) % 2]
act = lambda g, p: key(g @ np.array(p))
def order(g):
    I = np.eye(3, dtype=int); h = g % 2; k = 1
    while not (h == I).all(): h = (h @ g) % 2; k += 1
    return k

P = (1, 0, 0)
St = [g for g in G if act(g, P) == P]
far = [L for L in lines if P not in L]             # 4 Linien nicht durch P
near = [L for L in lines if P in L]                # 3 Linien durch P
def perm4(g):
    return [far.index(frozenset(act(g, p) for p in L)) for L in far]
# 3-dim. Darstellung: Permutationsdarstellung auf 4 Objekten, eingeschraenkt auf Summe-Null-Raum
B = np.linalg.qr(np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]]).T)[0]   # ONB 4x3
def rep3(g):
    M = np.zeros((4, 4));
    for i, j in enumerate(perm4(g)): M[j, i] = 1
    return B.T @ M @ B
assert len(St) == 24 and len({tuple(perm4(g)) for g in St}) == 24, "Wirkung nicht treu"

def fixpts(g): return [p for p in map(key, pts) if act(g, p) == p]
def center(g):  # Transvektion: Bild von (g + I) ist ein Punkt
    im = {key(((g + np.eye(3, dtype=int)) @ np.array(p)) % 2) for p in map(key, pts)} - {(0, 0, 0)}
    return im.pop() if len(im) == 1 else None

# Dreier-Element (geladene Leptonen) und seine feste Linie
g3s = [g for g in St if order(g) == 3]
g3 = g3s[0]
Lfix = [L for L in lines if frozenset(act(g3, p) for p in L) == L]
L = [l for l in Lfix if P not in l][0]
print(f"Dreier-Element: fester Punkt {fixpts(g3)}, feste Linie nicht durch P: {sorted(L)} "
      f"(Punkte zyklisch vertauscht: {[act(g3, p) for p in sorted(L)]})")
# Eigenbasis von rep3(g3): Eigenwert 1 = 'symmetrische' Richtung
w, V = np.linalg.eig(rep3(g3))
idx1 = int(np.argmin(abs(w - 1)))
print("Eigenwerte g3:", np.round(w, 3), " -> Eigenwert-1-Richtung Index", idx1)

print("\nInvolutionen in Stab(P) (Fano-Typ, S4-Klasse, erhaltene Spalte in der g3-Eigenbasis):")
V4 = None
table = defaultdict(list)
for h in [g for g in St if order(g) == 2]:
    c = center(h); axis = frozenset(fixpts(h))
    if c == P: typ = "Zentrum = P"
    elif c in L: typ = "Achse durch P, Zentrum auf L (Triolen-Linie)"
    else: typ = "Achse durch P, Zentrum nicht auf L"
    ev, EV = np.linalg.eig(rep3(h))
    vals = np.round(ev.real).astype(int)
    single = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    wcol = EV[:, single]
    coef = np.linalg.solve(V, wcol)                 # in g3-Eigenbasis
    mod = np.abs(coef)**2 / np.sum(np.abs(coef)**2)
    table[typ].append((round(mod[idx1], 4), tuple(sorted(np.round(mod, 4)))))
for typ, rows in table.items():
    print(f"  {typ}: {len(rows)} Elemente")
    for r in sorted(set(rows)):
        print(f"     Anteil auf Eigenwert-1-Richtung = {r[0]:.4f};  Betragsquadrate {r[1]}  (x{rows.count(r)})")
# Klassen in S4: Doppeltranspositionen (3) vs. Transpositionen (6) ueber Zykeltyp auf 4 Linien
ct = Counter()
for h in [g for g in St if order(g) == 2]:
    p = perm4(h); fixed = sum(1 for i in range(4) if p[i] == i)
    ct[("Zentrum = P" if center(h) == P else "Achse durch P"), "Transposition" if fixed == 2 else "Doppeltransp."] += 1
print("\nZuordnung zu S4-Klassen:", dict(ct))
print("Vergleich: TM1-Spalte (2/3, 1/6, 1/6), TM2-Spalte (1/3, 1/3, 1/3), TBM-3. Spalte (0, 1/2, 1/2)")
