"""k281 (Erkundung, nicht blind, 25.11.2026): Legt die Algebra die Kopplung der beiden Felder fest (Vorzeichen, Spalte aus k280)?
Naheliegendes Prinzip (k278 fortgesetzt): Beide Felder sind Teile EINES Elements W = Z_v(a) + Z_S(b) der Albert-Algebra, V = f(Tr W^2, N(W)).
Dann sind alle Kopplungen aus k280 festgelegt (eps = -mu^2, kappa1 = kappa2, ...).
A  W in Albert-Koordinaten gegen 3x3-Matrix: Tr W^2, N(W). Die Abbildung (s_k, v_k) -> w_k = (1 + i b) s_k + (-a + i) v_k hat Determinante 1 + a b.
   Fuer a b != -1 durchlaeuft W ALLE spurfreien Elemente von H3(C) (8 = 3 + 5 Dimensionen).
B  Folge: V ist SU(3)-invariant, das Vakuum ist die ganze Bahn W = r(3 psi psi^+ - 1), ein CP^2. Numerisch: Maxima von N auf der Schale aus Zufallsstarts.
   Frei bleiben: Restgruppe in A4, Anteil Spin 1 / Spin 2, die Spalte |U_w^+ psi|^2.
C  Die Zwei-Feld-Vakua aus k280 als Punkte der Bahn.
D  Die Einzelfeld-Vakua aus k278 (v ~ (1,1,1), S = 0) im vollen Raum: Hoehe sin(3 phi)/sqrt 54, Sattel ausser bei a = +-1/sqrt 3.
Aufruf aus diesem Ordner: python3 k281_ein_element_beide_felder.py
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
jordan, S_, Si, C = ns['jordan'], ns['S'], ns['Si'], ns['C']
Corig = Si @ C @ S_
rng = np.random.default_rng(281)
E = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[np.sqrt(2)], [np.sqrt(6)]])
tr = lambda X: X[:3].sum()


def det_alb(X):
    X2 = jordan(X, X); X3 = jordan(X2, X)
    return tr(X3) / 3 - tr(X) * tr(X2) / 2 + tr(X) ** 3 / 6


def W_alb(x, a, b):  # x = (v1..v3, 2 Diagonalparameter, s1..s3)
    v, p = x[:3], x[3:]
    xv = np.zeros(27); xv[10], xv[18], xv[26] = v
    xs = np.zeros(27); xs[:3] = p[:2] @ E
    for k in range(3):
        xs[3 + 8 * k] = p[2 + k]
    return xv + a * (Corig @ xv) + xs + b * (Corig @ xs)


def W_mat(x, a, b):
    v, p = x[:3], x[3:]; d = p[:2] @ E; z = (-a + 1j) * v + (1 + 1j * b) * p[2:]
    return np.array([[d[0], z[2], np.conj(z[1])], [np.conj(z[2]), d[1], z[0]], [z[1], np.conj(z[0]), d[2]]])


def qN(x, a, b):
    W = W_mat(x, a, b); return np.trace(W @ W).real, np.linalg.det(W).real


print("=" * 78)
print("A  Ein Element W = Z_v(a) + Z_S(b)")
for a, b in ((1.0, 0.5), (0.3, 2.0), (0.7, 0.7)):
    e = [0, 0]
    for _ in range(20):
        x = rng.normal(size=8); Wa = W_alb(x, a, b); q, n = qN(x, a, b)
        e[0] = max(e[0], abs(tr(jordan(Wa, Wa)) - q)); e[1] = max(e[1], abs(det_alb(Wa) - n))
    J = np.array([[1, -a], [b, 1]])  # (s, v) -> (Re w, Im w)
    print(f"   a={a}, b={b}: |Tr W^2 Algebra - Matrix| <= {e[0]:.1e}, |N| <= {e[1]:.1e}; det der Abbildung (s,v)->w = {np.linalg.det(J):.3f} = 1 + ab")
print("   -> Fuer ab != -1 ist jede spurfreie hermitesche 3x3-Matrix ein W. V = f(Tr W^2, det W) ist dann SU(3)-invariant (W -> U W U^+).")

print("=" * 78)
print("B  Maxima von N(W) auf der Schale Tr W^2 = 1 (60 Zufallsstarts je (a, b)), erwartet 1/sqrt 54 auf der Bahn (3 psi psi^+ - 1)/sqrt 6")
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
om = np.exp(2j * np.pi / 3)
Uw = np.array([[om ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
Nmax = 1 / np.sqrt(54)


def f(x, a, b):
    q, n = qN(x, a, b); return -n / q ** 1.5


for a, b in ((1.0, 0.5), (0.3, 2.0), (0.7, 0.7)):
    hit, stabs, frac, cols, eig = 0, {}, [], [], []
    for _ in range(60):
        x = rng.normal(size=8)
        for _ in range(4):
            x = minimize(f, x, args=(a, b), method="BFGS", options={"gtol": 1e-12}).x
        q, n = qN(x, a, b); x = x / np.sqrt(q); W = W_mat(x, a, b)
        hit += abs(n / q ** 1.5 - Nmax) < 1e-9
        k = int(sum(np.abs(R @ W @ R.T - W).max() < 1e-6 for R in A4)); stabs[k] = stabs.get(k, 0) + 1
        qv = np.trace(W_mat(np.concatenate([x[:3], np.zeros(5)]), a, b) @ W_mat(np.concatenate([x[:3], np.zeros(5)]), a, b)).real
        frac.append(qv)
        w, U = np.linalg.eigh(W); eig.append(np.sort(w * np.sqrt(6)))
        psi = U[:, np.argmax(np.abs(w - np.median(w)))]
        cols.append(np.sort(np.abs(Uw.conj().T @ psi) ** 2)[::-1])
    cols, eig = np.array(cols), np.array(eig)
    print(f"   a={a}, b={b}: N_max = 1/sqrt 54 in {hit}/60; Eigenwerte*sqrt6 = {np.round(eig.mean(0), 6)} (Streuung {np.ptp(eig, 0).max():.1e});")
    print(f"      Ordnung der Restgruppe in A4: {stabs}; Tr Z_v^2 (Spin-1-Anteil) von {min(frac):.2f} bis {max(frac):.2f};"
          f" groesste Spalte |U_w^+ psi|^2 von {cols[:, 0].min():.2f} bis {cols[:, 0].max():.2f}")
print("   -> Alle Starts erreichen dieselbe Hoehe, aber an verschiedenen Punkten: keine Restgruppe, kein fester Anteil, keine feste Spalte.")

print("=" * 78)
print("C  Liegen die Zwei-Feld-Vakua aus k280 (v ~ (1,1,1) plus S auf dem Kreis bei 45 Grad) auf der Bahn?")
for a, b in ((1.0, 0.5), (0.3, 2.0)):
    for sgn in (+1, -1):
        u = np.array([1, sgn, 0]) / np.sqrt(2); M = (3 * np.outer(u, u) - np.eye(3)) / np.sqrt(6)
        p = np.concatenate([np.linalg.lstsq(E.T, np.diag(M), rcond=None)[0], np.array([M[1, 2], M[2, 0], M[0, 1]]) / np.sqrt(1 + b * b)])
        best = max(qN(np.concatenate([r * np.ones(3), np.cos(t) * p]), a, b)[1] / qN(np.concatenate([r * np.ones(3), np.cos(t) * p]), a, b)[0] ** 1.5
                   for t in np.linspace(0, np.pi, 181) for r in [np.sin(t)] if abs(np.cos(t)) + abs(r) > 0)
        print(f"   a={a}, b={b}, u = (1,{sgn:+d},0)/sqrt2: max ueber das Mischungsverhaeltnis von N/q^1.5 = {best:.6f} (Bahn: {Nmax:.6f})")

print("   -> Ja, bei passendem Mischungsverhaeltnis, und zwar fuer beide Vorzeichen. Sie sind Punkte der entarteten Bahn, aber nicht ausgezeichnet.")
print("=" * 78)
print("D  Einzelfeld-Vakuum aus k278 (v = (1,1,1), S = 0) im vollen Raum: Hoehe und Hesse-Matrix von -N/q^1.5")
for a in (0.5, 1 / np.sqrt(3), 1.0, 3.7):
    b = 0.5
    x0 = np.concatenate([np.ones(3) * np.sign(3 * a - a ** 3), np.zeros(5)])
    h = 1e-4; Hs = np.zeros((8, 8)); I8 = np.eye(8)
    for i in range(8):
        for j in range(8):
            Hs[i, j] = (f(x0 + h * I8[i] + h * I8[j], a, b) - f(x0 + h * I8[i] - h * I8[j], a, b)
                        - f(x0 - h * I8[i] + h * I8[j], a, b) + f(x0 - h * I8[i] - h * I8[j], a, b)) / (4 * h * h)
    ev = np.linalg.eigvalsh(Hs)
    print(f"   a={a:.4f}: N/q^1.5 = {-f(x0, a, b):.6f} = {abs(3 * a - a ** 3) / (1 + a * a) ** 1.5:.4f}/sqrt 54; negative Hesse-Eigenwerte: {(ev < -1e-6).sum()}"
          f" (kleinster {ev.min():+.4f})")
print("   -> Ausser bei a = +-1/sqrt 3 (dort liegt (1,1,1) selbst auf der Bahn) ist das Z3-Vakuum im vollen Raum ein Sattel (drei instabile Richtungen).")
