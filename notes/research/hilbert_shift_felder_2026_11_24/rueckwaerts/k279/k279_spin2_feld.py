"""k279 (Erkundung, nicht blind, 24.11.2026): Zweites Feld im Spin-2-Teil. Gibt ein Ein-Feld-Potential dort eine Z2-Ausrichtung?
Feld: S reell symmetrisch spurfrei (Diagonale a, reelle Nebendiagonale s), Ladungsmischung Z_b = S + b C S (Eintraege s_k(1 + b e7)).
A  N(Z_b) = a1a2a3 + 2(1-3b^2) s1s2s3 - (1+b^2) sum a_k s_k^2, Tr Z^2 = |a|^2 + 2(1+b^2)|s|^2 (Albert-Algebra aus k276).
B  Mit t = sqrt(1+b^2) s und gamma = (1-3b^2)/(1+b^2)^(3/2) = cos 3phi (tan phi = b) gilt
   N = [(1+gamma) det(D+T) + (1-gamma) det(D-T)]/2. Daraus: max N auf der Schale = max det, erreicht genau dort, wo D+T und D-T beide maximal sind.
C  Numerisch: Maxima von N auf der Schale Tr Z^2 = 1 aus Zufallsstarts, Stabilisator in A4, Streuung der Maxima.
Jedes Ein-Feld-Potential ist V = f(Tr Z^2, N) (Cayley-Hamilton, k278), die Ausrichtung ist also die der Extrema von N.
Aufruf aus diesem Ordner: python3 k279_spin2_feld.py
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
jordan, S, Si, C = ns['jordan'], ns['S'], ns['Si'], ns['C']
Corig = Si @ C @ S
N = 27
rng = np.random.default_rng(279)
tr = lambda X: X[:3].sum()
E = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[np.sqrt(2)], [np.sqrt(6)]])  # Basis spurfreier Diagonalen


def det(X):
    X2 = jordan(X, X); X3 = jordan(X2, X)
    return tr(X3) / 3 - tr(X) * tr(X2) / 2 + tr(X) ** 3 / 6


def Z_of(p, b):  # p = (2 Diagonalparameter, s1, s2, s3); Platz k = reeller Anteil von Slot k
    x = np.zeros(N); x[:3] = p[:2] @ E
    for k in range(3):
        x[3 + 8 * k] = p[2 + k]
    return x + b * (Corig @ x)


def parts(p):
    return p[:2] @ E, np.asarray(p[2:])


def N_formula(p, b):
    a, s = parts(p)
    return np.prod(a) + 2 * (1 - 3 * b * b) * np.prod(s) - (1 + b * b) * (a * s ** 2).sum()


def q_formula(p, b):
    a, s = parts(p)
    return a @ a + 2 * (1 + b * b) * s @ s


print("=" * 78)
print("A  Invarianten des Spin-2-Felds Z_b = S + b C S (Albert-Algebra gegen Formel)")
for b in (0.0, 0.5, 1.0, np.sqrt(3), 4.0):
    eN = eq = eT = 0
    for _ in range(30):
        p = rng.normal(size=5); Z = Z_of(p, b)
        eN = max(eN, abs(det(Z) - N_formula(p, b)))
        eq = max(eq, abs(tr(jordan(Z, Z)) - q_formula(p, b)))
        eT = max(eT, abs(tr(Z)))
    print(f"   b={b:.4f}: |N - Formel| <= {eN:.1e}, |Tr Z^2 - Formel| <= {eq:.1e}, |Tr Z| <= {eT:.1e}")
print("   Lesart: Platz k (Slot k) gehoert zur Diagonale k, also s_k = X_{k+1,k+2}.")

print("=" * 78)
print("B  Zerlegung N = [(1+g) det(D+T) + (1-g) det(D-T)]/2 mit t = sqrt(1+b^2) s, g = cos 3phi")


def M_of(a, t):
    M = np.diag(a).astype(float)
    M[1, 2] = M[2, 1] = t[0]; M[2, 0] = M[0, 2] = t[1]; M[0, 1] = M[1, 0] = t[2]
    return M


def gam(b):
    return (1 - 3 * b * b) / (1 + b * b) ** 1.5


for b in (0.5, 1.0, 2.0):
    err = 0
    for _ in range(30):
        p = rng.normal(size=5); a, s = parts(p); t = np.sqrt(1 + b * b) * s; g = gam(b)
        rhs = ((1 + g) * np.linalg.det(M_of(a, t)) + (1 - g) * np.linalg.det(M_of(a, -t))) / 2
        err = max(err, abs(N_formula(p, b) - rhs))
    print(f"   b={b}: gamma = {gam(b):+.4f} = cos(3 arctan b) = {np.cos(3 * np.arctan(b)):+.4f};  |N - Zerlegung| <= {err:.1e}")
print("   gamma = +-1 genau bei b = 0 und b = +-sqrt(3): dann ist N = det(D+-T), also SO(3)-invariant (volle Entartung).")
print("   Auf der Schale |a|^2 + 2|t|^2 = 1 ist max det = 1/sqrt(54) (Eigenwerte (2,-1,-1)/sqrt 6), also max N = 1/sqrt(54) fuer |gamma| < 1,")
print("   erreicht genau auf der det-Bahn mit t1 t2 t3 = 0 (dann ist D-T zu D+T konjugiert).")

print("=" * 78)
print("C  Maxima von N auf der Schale Tr Z^2 = 1 (60 Zufallsstarts je b), Stabilisator in A4")
A4 = []
for perm in itertools.permutations(range(3)):
    if np.linalg.det(np.eye(3)[list(perm)]) < 0:
        continue
    for signs in itertools.product((1, -1), repeat=3):
        if np.prod(signs) < 0:
            continue
        R = np.zeros((3, 3))
        for i, pp in enumerate(perm):
            R[i, pp] = signs[i]
        A4.append(R)
reps = [ns['rep'](R) for R in A4]
names = {1: "trivial", 2: "Z2", 3: "Z3", 4: "V4 (Klein)", 12: "A4"}


def stab(p, b):
    z = S @ Z_of(p, b)
    return sum(np.abs(r @ z - z).max() < 1e-5 for r in reps)


def axis_info(p, b):  # Achse u der Bahn (2,-1,-1): Eigenvektor zum Einzel-Eigenwert der reellen Matrix D + T
    a, s = parts(p); M = M_of(a, np.sqrt(1 + b * b) * s); w, U = np.linalg.eigh(M)
    return U[:, np.argmax(np.abs(w - np.median(w)))]


Nmax = 1 / np.sqrt(54)
for b in (0.0, 0.25, 0.5, 1.0, np.sqrt(3), 2.0, 4.0):
    res, vals, axes, zeros = {}, [], [], 0
    for _ in range(60):  # N ist homogen vom Grad 3: maximiere N(p)/q(p)^(3/2), danach auf q = 1 normieren
        p = rng.normal(size=5)
        for _ in range(8):  # Neustarts: nahe gamma = -1 ist die Kruemmung quer zum Kreis klein (1 + gamma)
            r = minimize(lambda p: -N_formula(p, b) / q_formula(p, b) ** 1.5, p, method="BFGS", options={"gtol": 1e-13})
            p = r.x / np.sqrt(q_formula(r.x, b))
        vals.append(N_formula(p, b)); Z = Z_of(p, b)
        assert abs(det(Z) - vals[-1]) < 1e-9
        if abs(vals[-1] - Nmax) > 1e-9:
            print(f'      nicht konvergiert: b={b:.4f}, N={vals[-1]:.6f}, p={np.round(p, 4)}')
        k = names.get(stab(p, b), str(stab(p, b))); res[k] = res.get(k, 0) + 1
        u = axis_info(p, b); axes.append(np.abs(u))
        zeros += np.min(np.abs(parts(p)[1])) < 1e-4
    axes = np.array(axes)
    print(f"   b={b:.4f} (gamma {gam(b):+.3f}): N_max = {max(vals):.6f} (1/sqrt54 = {Nmax:.6f}), erreicht in {sum(abs(v - Nmax) < 1e-9 for v in vals)}/60 (min {min(vals):.4f});"
          f" Stabilisatoren {res}; ein s_k = 0 in {zeros}/60; Achse |u| Streuung {np.ptp(axes, axis=0).max():.2f}")
print("   Lesart: Fuer |gamma| < 1 liegen alle Maxima auf derselben Hoehe, aber nicht an einem Punkt: Achse u auf den drei Grosskreisen u_k = 0.")
print("   Generisch Z2 (Drehung um die Koordinatenachse senkrecht zum Kreis), an den Achsen u = e_k Klein V4. Kein isoliertes Z2-Vakuum.")

print("=" * 78)
print("D  Flache Richtung: N entlang des Grosskreises u = (cos th, sin th, 0) auf der Schale")
for b in (0.5, 2.0):
    th = np.linspace(0, np.pi / 2, 7); out = []
    for t_ in th:
        u = np.array([np.cos(t_), np.sin(t_), 0]); M = (3 * np.outer(u, u) - np.eye(3)) / np.sqrt(6)
        a = np.diag(M); tt = np.array([M[1, 2], M[2, 0], M[0, 1]]); s = tt / np.sqrt(1 + b * b)
        p = np.concatenate([np.linalg.lstsq(E.T, a, rcond=None)[0], s])
        out.append((det(Z_of(p, b)), stab(p, b)))
    print(f"   b={b}: N = " + ", ".join(f"{n:.6f}" for n, _ in out) + "  | Stabilisator-Ordnung " + ", ".join(str(o) for _, o in out))
print("   -> N konstant entlang des Kreises: exakt flache Richtung. Ein Ein-Feld-Potential waehlt zwischen Z2- und V4-Punkten nicht.")
