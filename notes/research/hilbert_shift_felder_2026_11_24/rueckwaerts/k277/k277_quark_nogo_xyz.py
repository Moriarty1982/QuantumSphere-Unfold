"""k277 (Erkundung, nicht blind, 24.11.2026): Quark-No-go, xyz als kubische Albert-Norm, Vakuumausrichtung.
A  No-go: Auf den Farbtripletts (18) ist der Raum der A4-invarianten Operatoren gleich dem der SO(3)-invarianten.
   Jede SO(3)-aequivariante Konstruktion aus C = L_e7 (A4-invariant) ist dort also SO(3)-invariant.
B  Flavon v in den e7-Anteilen: X(v), Y = C X(v). det Y = N(CX) = -2 v1 v2 v3, Tr Y^2 = 2|v|^2.
C  Gemischte Invarianten von X und Y vom Grad 4 enthalten sum v_i^4.
D  Ausrichtung: Potential nur aus Y -> Minimum bei |v1| = |v2| = |v3| (Z3); allgemeines A4-Potential -> Z3 oder Z2 je nach lambda'.
Benutzt die Albert-Algebra aus ../h127/k276_test_h127.py (Spurform-Koordinaten). Aufruf aus diesem Ordner: python3 k277_quark_nogo_xyz.py
"""
import contextlib
import io
import itertools
import os
import runpy

import numpy as np
from scipy.optimize import minimize

here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(os.path.join(here, '..', 'h127', 'k276_test_h127.py'))
jordan, S, Si, SO3, C = ns['jordan'], ns['S'], ns['Si'], ns['SO3'], ns['C']
idx_t = ns['idx_t']
N = 27
rng = np.random.default_rng(277)


def rep(R):  # X -> R X R^T in Spurform-Koordinaten
    return ns['rep'](R)


# A4: vorzeichenbehaftete gerade Permutationen mit det +1 (k275)
A4 = []
for perm in itertools.permutations(range(3)):
    if np.linalg.det(np.eye(3)[list(perm)]) < 0:
        continue
    for signs in itertools.product((1, -1), repeat=3):
        if np.prod(signs) < 0:
            continue
        R = np.zeros((3, 3))
        for i, p in enumerate(perm):
            R[i, p] = signs[i]
        A4.append(R)
print("=" * 78)
print(f"A  No-go fuer die Quarks ({len(A4)} Elemente in A4)")
reps = [rep(R) for R in A4]
print(f"   C = L_e7 je Platz A4-invariant auf allen 27: max|rho C rho^T - C| = {max(np.abs(r @ C @ r.T - C).max() for r in reps):.1e}")
n = len(idx_t)
rt = [r[np.ix_(idx_t, idx_t)] for r in reps]
Pavg = sum(np.kron(r, r) for r in rt) / len(rt)            # Projektor auf A4-invariante Operatoren (vec, Zeilen-Major)
dimA4 = int(round(np.trace(Pavg)))
Ts = [T[np.ix_(idx_t, idx_t)] for T in SO3]
I = np.eye(n)
M = np.vstack([np.kron(T, I) - np.kron(I, T.T) for T in Ts])
dimSO3 = n * n - np.linalg.matrix_rank(M, 1e-9)
print(f"   Operatoren auf den Tripletts (18): A4-invariant dim {dimA4}, SO(3)-invariant dim {dimSO3}")
# jede A4-invariante ist SO(3)-invariant?
B = np.linalg.svd(Pavg)[0][:, :dimA4]
leak = max(np.abs(M @ B[:, k]).max() for k in range(dimA4))
print(f"   max|[so(3), A]| ueber eine Basis der A4-invarianten Operatoren: {leak:.1e}")
print("   -> A4-invariant = SO(3)-invariant auf den Tripletts (Spin 1 x Spin 1 = l 0,1,2; A4 hat in l = 1, 2 kein Invariantes).")
print("      Jede SO(3)-aequivariante Konstruktion aus C bleibt dort SO(3)-invariant, gleich welcher Ordnung.")

print("=" * 78)
print("B  Flavon v in den e7-Anteilen: X(v), Y = C X(v)")
Corig = Si @ C @ S
tr = lambda X: X[:3].sum()


def det(X):
    X2 = jordan(X, X); X3 = jordan(X2, X)
    return tr(X3) / 3 - tr(X) * tr(X2) / 2 + tr(X) ** 3 / 6


def X_of(v):
    x = np.zeros(N); x[10], x[18], x[26] = v; return x


worst = [0, 0, 0, 0]
for _ in range(50):
    v = rng.normal(size=3); X = X_of(v); Y = Corig @ X
    worst[0] = max(worst[0], abs(det(Y) + 2 * np.prod(v)))
    worst[1] = max(worst[1], abs(tr(jordan(Y, Y)) - 2 * v @ v))
    worst[2] = max(worst[2], abs(det(X)), abs(tr(Y)))
    worst[3] = max(worst[3], abs(tr(jordan(X, Y))))
print(f"   |det Y + 2 v1 v2 v3| <= {worst[0]:.1e};  |Tr Y^2 - 2|v|^2| <= {worst[1]:.1e};  det X, Tr Y <= {worst[2]:.1e};  Tr(X o Y) <= {worst[3]:.1e}  (50 Stichproben)")
print("   -> Der xyz-Term ist die kubische Norm der Albert-Algebra nach der Ladungsdrehung: N(C X(v)) = -2 v1 v2 v3.")

print("=" * 78)
print("C  Gemischte Invarianten vom Grad 4 (Anpassung an |v|^4 und sum v^4)")
rows, vals = [], {k: [] for k in ("Tr((XoY)^2)", "Tr(X^2 o Y^2)", "Tr((X^2)^2)", "Tr((Y^2)^2)")}
for _ in range(20):
    v = rng.normal(size=3); X = X_of(v); Y = Corig @ X; XY = jordan(X, Y)
    rows.append([(v @ v) ** 2, (v ** 4).sum()])
    vals["Tr((XoY)^2)"].append(tr(jordan(XY, XY)))
    vals["Tr(X^2 o Y^2)"].append(tr(jordan(jordan(X, X), jordan(Y, Y))))
    vals["Tr((X^2)^2)"].append(tr(jordan(jordan(X, X), jordan(X, X))))
    vals["Tr((Y^2)^2)"].append(tr(jordan(jordan(Y, Y), jordan(Y, Y))))
A = np.array(rows)
for k, b in vals.items():
    c = np.linalg.lstsq(A, np.array(b), rcond=None)[0]
    print(f"   {k:14s} = {c[0]:+.4f} |v|^4 {c[1]:+.4f} sum v^4  (Rest {np.abs(A @ c - b).max():.1e})")
print("   -> Invarianten nur aus Y haengen nur von |v|^2 und xyz ab; gemischte bringen sum v^4 (freier Koeffizient).")

print("=" * 78)
print("D  Ausrichtung des Minimums (|v| auf der Schale frei, 40 Startpunkte je Fall)")


def classify(v):
    a = np.sort(np.abs(v))[::-1] / np.linalg.norm(v)
    if np.allclose(a, 1 / np.sqrt(3), atol=1e-4):
        return "(1,1,1)-Typ, Rest Z3"
    if np.allclose(a, [1, 0, 0], atol=1e-4):
        return "(1,0,0)-Typ, Rest Z2"
    return f"andere {np.round(a, 3)}"


def run(V, label):
    found = {}
    for _ in range(40):
        r = minimize(V, rng.normal(size=3), method="BFGS", options={"gtol": 1e-12})
        if np.linalg.norm(r.x) > 1e-6:
            k = classify(r.x); found[k] = found.get(k, 0) + 1
    best = min((minimize(V, rng.normal(size=3), method="BFGS", options={"gtol": 1e-12}) for _ in range(40)), key=lambda r: r.fun)
    print(f"   {label}: Minima {found}; globales Minimum {classify(best.x)}, V = {best.fun:.6f}")


def Vy(v, kappa, lam):  # nur aus Y: Tr Y^2 = 2|v|^2, det Y = -2xyz
    q = 2 * v @ v; d = -2 * np.prod(v)
    return -q + kappa * d + lam * q ** 2


for kappa, lam in ((0.5, 0.2), (-0.5, 0.2), (0.05, 0.1)):
    run(lambda v: Vy(v, kappa, lam), f"nur Y: kappa={kappa:+.2f}, lambda={lam}")


def Vg(v, kappa, lam, lamp):
    return -v @ v + kappa * np.prod(v) + lam * (v @ v) ** 2 + lamp * (v ** 4).sum()


for lamp in (+0.3, -0.15):
    run(lambda v: Vg(v, 0.2, 0.5, lamp), f"gemischt: kappa=0.2, lambda=0.5, lambda'={lamp:+.2f}")
print("   -> Nur aus Y: Z3-Ausrichtung erzwungen (fuer jedes kappa != 0). Mit sum v^4: Z3 oder Z2 je nach lambda' (Literatur).")
