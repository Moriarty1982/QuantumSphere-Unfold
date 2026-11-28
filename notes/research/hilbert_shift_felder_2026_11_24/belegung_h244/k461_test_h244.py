"""k461 (Test H244): Folgt die Belegung (2/3, 1/6, 1/6) von Baum und v0 aus der Kopien-Regel H242?
Vorab Vorab_H244_Belegung.md (b2f0677). Maschinerie k370 unveraendert. Aufruf aus diesem Ordner: python3 k461_test_h244.py > k461_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import brentq

src = open("../mischung_h174/k370_test_h174.py").read().split('print("== Kontrolle')[0]
ns = {}; exec(src, ns)
T, Nhat = ns["T"], ns["Nhat"]
w = np.exp(2j * np.pi / 3)
ev, V = np.linalg.eig(T)
tk = [V[:, np.argmin(abs(ev - w ** k))] for k in range(3)]
tk = [v / np.linalg.norm(v) for v in tk]
Tb = np.column_stack(tk)
D = np.diag([1, -1, 1])  # mit e2 -> -e2 wird T zyklisch
TARGET = np.array([2 / 3, 1 / 6, 1 / 6])


def W_state(z):  # z in der vorzeichengedrehten Basis
    a = Tb.conj().T @ (D @ z); a = abs(a) ** 2; return a / a.sum()


def W_major(N):
    M = Tb.T @ N @ Tb; tot = np.sum(abs(M) ** 2)
    return np.array([sum(abs(M[i, j]) ** 2 for i in range(3) for j in range(3) if (i + j) % 3 == c) for c in range(3)]) / tot


print("=" * 96)
print("H244 (k461)  Belegung (2/3, 1/6, 1/6) und Kopien-Regel")
print("=" * 96)
print(f"D T D zyklisch (Permutationsmatrix): {np.allclose(D @ T @ D, np.abs(D @ T @ D)) and np.allclose(np.abs(D @ T @ D).sum(0), 1)}")
print(f"Kontrolle v0 = (1,0,1)/sqrt2: W = {np.round(W_state(np.array([1, 0, 1]) / np.sqrt(2)), 6)}")

# A: schliessende Vollbelegungen
print("\nA (nicht blind): Vollbelegungen z_j = w^{g_j}")
full = list(itertools.product(range(3), repeat=3))
Wcl = []
for g in full:
    z = np.array([w ** gi for gi in g]) / np.sqrt(3); Wg = W_state(z)
    if sum(g) % 3 == 0:
        Wcl.append(Wg); print(f"  g = {g} (schliesst): W = {np.round(Wg, 6)}")
print(f"  Mittel ueber die 9 schliessenden: {np.round(np.mean(Wcl, 0), 6)};  eine davon = Ziel: {any(np.allclose(x, TARGET) for x in Wcl)}")
print(f"  Mittel ueber alle 27: {np.round(np.mean([W_state(np.array([w**gi for gi in g])/np.sqrt(3)) for g in full], 0), 6)}")

# B: alle 63 Muster
print("\nB: alle nicht leeren Muster z_j in {0, w^g}")
pats = [p for p in itertools.product([None, 0, 1, 2], repeat=3) if any(x is not None for x in p)]
M, S, Sinv = set(), set(), set()
cnt_by_occ = {}
for p in pats:
    z = np.array([0 if x is None else w ** x for x in p]); z = z / np.linalg.norm(z)
    Wp = W_state(z); occ = [x for x in p if x is not None]
    closes = sum(occ) % 3 == 0
    closes_inv = any(sum((x + h) % 3 for x in occ) % 3 == 0 for h in range(3))
    if np.allclose(Wp, TARGET, atol=1e-12): M.add(p)
    if closes: S.add(p)
    if closes_inv: Sinv.add(p)
    key = (len(occ), tuple(np.round(Wp, 6)))
    cnt_by_occ[key] = cnt_by_occ.get(key, 0) + 1
print(f"  Muster: {len(pats)};  |M| (Ziel in Reihenfolge) = {len(M)};  |S| (schliesst, H242) = {len(S)};  |S_inv| (schliesst nach Drehung) = {len(Sinv)}")
print(f"  M = S: {M == S};  M Teilmenge S: {M <= S};  S Teilmenge M: {S <= M};  |M ∩ S| = {len(M & S)}")
print(f"  M = S_inv: {M == Sinv};  M Teilmenge S_inv: {M <= Sinv}")
print("  M =", sorted(M, key=str))
print("  Anteilsklassen nach Zahl der besetzten Kopien (Anzahl Muster):")
for (n, Wt), c in sorted(cnt_by_occ.items()):
    print(f"    {n} besetzt, W = {Wt}: {c}")
print("  Nur Bericht, Z6-Phasen (Vorzeichen):")
for nm, z in (("(1,0,-1)", [1, 0, -1]), ("(1,-1,0)", [1, -1, 0]), ("(1,1,-1)", [1, 1, -1]), ("(1,0,1)", [1, 0, 1])):
    z = np.array(z, float); print(f"    {nm}: W = {np.round(W_state(z / np.linalg.norm(z)), 6)}")

# C: Baum entlang delta_nu
print("\nC (blind): W0(N-hat(delta_nu)) auf [0, pi/3], Zweig b >= 0")
f = lambda d: W_major(Nhat(d, 1))[0] - 2 / 3
ds = np.linspace(0, np.pi / 3, 6001)
vals = np.array([f(d) for d in ds])
for d in (0, np.pi / 12, np.pi / 6 - 0.0395773407, np.pi / 6, np.pi / 4, np.pi / 3):
    N = Nhat(d, 1); print(f"  delta_nu = {d:.6f}: b = {N[0,1]:+.6f}, c = {N[0,2]:+.6f}, W = {np.round(W_major(N), 8)}")
roots = []
for i in range(len(ds) - 1):
    if vals[i] == 0: roots.append(ds[i])
    elif vals[i] * vals[i + 1] < 0: roots.append(brentq(f, ds[i], ds[i + 1], xtol=1e-15))
near = ds[abs(vals) < 1e-10]
print(f"  Nullstellen von W0 - 2/3: {[round(r, 10) for r in roots]}  (pi/6 = {np.pi/6:.10f})")
print(f"  Gitterpunkte mit |W0 - 2/3| < 1e-10: {np.round(near, 6)};  max |W0 - 2/3| auf dem Gitter: {abs(vals).max():.4f}")
real = ds <= np.pi / 6
b2 = np.array([((lambda l: ((l[1]-l[2])**2 - (l[0]-1)**2) / 8)(sorted([1 + np.sqrt(2)*np.cos(d + 2*np.pi*k/3) for k in range(3)], key=abs))) for d in ds])
print(f"  b^2 >= 0 (Baum reell) genau fuer delta_nu <= pi/6: {bool(np.all(b2[real] >= -1e-12) and np.all(b2[~real] < 0))};  jenseits klemmt Nhat b auf 0 (kein gueltiger Baum)")
print(f"  W0 auf [0, pi/6] streng steigend: {bool(np.all(np.diff(vals[real]) > 0))};  Maximum 2/3 am Rand pi/6 (b = 0)")
cs = np.linspace(-2, 2, 9)
print("  Nur Bericht, W0 fuer b = 0 als Funktion von c (Formel (3 + 2c^2/3)/(3 + 2c^2)):")
for c in cs:
    N = np.array([[1, 0, c], [0, 1, 0], [c, 0, 1]]); print(f"    c = {c:+.2f}: W0 = {W_major(N)[0]:.6f}, Formel {(3 + 2*c**2/3)/(3 + 2*c**2):.6f}")
onlyC = len(roots) >= 1 and all(abs(r - np.pi / 6) < 1e-8 for r in roots) and all(abs(x - np.pi / 6) < 1e-3 for x in near)
print("\n" + "=" * 96)
print(f"B (M = S): {M == S};  C (W0 = 2/3 nur bei pi/6): {onlyC}")
