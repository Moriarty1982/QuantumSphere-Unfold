"""k71: Konsistenzpruefung (keine Vorhersage): Laesst sich das Generationen-Tripel aus v4.8.0-r14/r15 in der
Dixon-Ablage HS(6) ablegen?  Kanalindex alpha = (a, b, c), a in {0,1} (C), b in {0..3} (H), c in {0..7} (O).
H (x) O = O + Im(H) (x) O, und Im(H) (x) O = i(x)O + j(x)O + k(x)O hat die 24 Dimensionen von O^3."""
import numpy as np, itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul, oc

rng = np.random.default_rng(71)
t = lambda x, y, z: omul(omul(x, y), z)[0]
def dev(f, N=300):
    return max(abs(t(*f(*X)) - t(*X)) for X in [rng.normal(size=(3, 8)) for _ in range(N)])

# 1. Ablage: Masken in {0,1}^64
idx = [(a, b, c) for a in range(2) for b in range(4) for c in range(8)]
bit = {al: i for i, al in enumerate(idx)}
tripel = sum(1 << bit[(0, b, c)] for b in (1, 2, 3) for c in range(8))
farbig = sum(1 << bit[(0, b, c)] for b in (1, 2, 3) for c in (4, 5, 6))
print(f"Tripel-Maske (a = 0, b in i,j,k, c beliebig): {bin(tripel).count('1')} aktive Bits von 64")
print(f"farbige Zustaende (c in e4,e5,e6, Rahmen u = e7): {bin(farbig).count('1')} aktive Bits, Teilmaske: {farbig & tripel == farbig}")

# 2. Symmetrien: Triality-S3 gegen die Vorzeichen-Permutationen in SO(3) = Aut(H) auf i, j, k
print("\nTriality-S3: zyklisch", f"{dev(lambda x, y, z: (y, z, x)):.0e},",
      "(x,y,z) -> (x*,z*,y*)", f"{dev(lambda x, y, z: (oc(x), oc(z), oc(y))):.0e}")
inv = []; total = 0
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i, p in enumerate(perm): M[p, i] = sg[i]
        if abs(np.linalg.det(M) - 1) > 1e-9: continue
        total += 1
        f = lambda x, y, z, perm=perm, sg=sg: tuple(sg[k]*[x, y, z][perm[k]] for k in range(3))
        if dev(f) < 1e-9: inv.append(M)
even = all(np.isclose(np.linalg.det(np.abs(M)), 1) for M in inv)   # nur gerade Permutationen
print(f"Vorzeichen-Permutationen in SO(3): {total}; davon lassen Re((xy)z) invariant: {len(inv)}"
      f" (nur gerade Permutationen: {even}) -> Gruppe der Ordnung 12 = A4 (Drehgruppe des Tetraeders)")
G = {tuple(np.round(M).astype(int).ravel()) for M in inv}
closed = all(tuple(np.round(np.array(A).reshape(3, 3) @ np.array(B).reshape(3, 3)).astype(int).ravel()) in G for A in G for B in G)
print(f"  abgeschlossen unter Multiplikation: {closed}")
# 3. Transposition: geht nur mit Oktonion-Konjugation; die ist auf O ein Anti-Automorphismus
x, y = rng.normal(size=(2, 8))
print(f"\nKonjugation: (xy)* = y* x* (Abweichung {np.abs(oc(omul(x, y)) - omul(oc(y), oc(x))).max():.0e}),"
      f" (xy)* - x* y* = {np.abs(oc(omul(x, y)) - omul(oc(x), oc(y))).max():.2f}  -> kein Automorphismus")
