"""k280 (Erkundung, nicht blind, 25.11.2026): Kopplung des Spin-1-Felds (k278, Z3-Vakuum) an das Spin-2-Feld (k279, flache Kreise).
Felder im farbneutralen Teil H3(C) (e7 <-> i): Z_v mit Eintraegen (-a + i) v_k, Z_S mit Diagonale d (Summe 0) und Eintraegen (1 + i b) s_k.
A  Gemischte Invarianten I11 = Tr(Z_v o Z_S) = 2(b - a) sum v_k s_k (Albert-Algebra aus k276 gegen 3x3-Matrizen).
B  Auf dem Kreis u = (cos th, sin th, 0) und v = v0(1,1,1) sind I11, I21 = Tr(Z_v^2 Z_S), I12 = Tr(Z_v Z_S^2) alle proportional zu sin 2th (k280b).
   Die Kopplung waehlt also th = pi/4 oder 3pi/4: Block mit gleicher Diagonale, Achse u = (1, +-1, 0)/sqrt 2.
C  Volles Minimum von V = V1(Z_v) + V2(Z_S) + eps I11 aus Zufallsstarts: Restgruppe, Winkel, Fehlausrichtung als Funktion von eps.
D  Lesart als Mischung (Setzung): Spalte |U^+ u|^2 der Achse u in der Z3-Eigenbasis des ersten Felds.
Aufruf aus diesem Ordner: python3 k280_kopplung.py
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
rng = np.random.default_rng(280)
E = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[np.sqrt(2)], [np.sqrt(6)]])


def H(d, z):
    return np.array([[d[0], z[2], np.conj(z[1])], [np.conj(z[2]), d[1], z[0]], [z[1], np.conj(z[0]), d[2]]])


def Zv(v, a):
    return H(np.zeros(3), (-a + 1j) * np.asarray(v))


def ZS(p, b):
    return H(p[:2] @ E, (1 + 1j * b) * np.asarray(p[2:]))


def alb_v(v, a):
    x = np.zeros(27); x[10], x[18], x[26] = v; return x + a * (Corig @ x)


def alb_S(p, b):
    x = np.zeros(27); x[:3] = p[:2] @ E
    for k in range(3):
        x[3 + 8 * k] = p[2 + k]
    return x + b * (Corig @ x)


rtr = lambda M: np.trace(M).real
print("=" * 78)
print("A  Gemischte Invarianten: Albert-Algebra gegen 3x3-Matrizen und Formel")
for a, b in ((1.0, 0.5), (0.3, 2.0), (0.7, 0.7)):
    e = [0, 0, 0, 0]
    for _ in range(20):
        v, p = rng.normal(size=3), rng.normal(size=5)
        A, B = alb_v(v, a), alb_S(p, b); Av, Bs = Zv(v, a), ZS(p, b)
        i11 = jordan(A, B)[:3].sum()
        e[0] = max(e[0], abs(i11 - rtr(Av @ Bs)))
        e[1] = max(e[1], abs(i11 - 2 * (b - a) * v @ p[2:]))
        e[2] = max(e[2], abs(jordan(jordan(A, A), B)[:3].sum() - rtr(Av @ Av @ Bs)))
        e[3] = max(e[3], abs(jordan(A, jordan(B, B))[:3].sum() - rtr(Av @ Bs @ Bs)))
    print(f"   a={a}, b={b}: |I11 Algebra - Matrix| <= {e[0]:.1e}, |I11 - 2(b-a) v.s| <= {e[1]:.1e}, I21 <= {e[2]:.1e}, I12 <= {e[3]:.1e}")
print("   -> I11 verschwindet genau fuer a = b. Sonst mischt schon die Bilinearform Spin 1 und die Nebendiagonale von Spin 2 (beide A4-Tripletts).")

print("=" * 78)
print("B  Kopplung entlang der flachen Richtung (v = (1,1,1)/sqrt 3 v0, Kreis u3 = 0), a = 1, b = 0.5")
a, b = 1.0, 0.5
th = np.linspace(0, np.pi, 9)
rows = []
for t_ in th:
    u = np.array([np.cos(t_), np.sin(t_), 0]); M = (3 * np.outer(u, u) - np.eye(3)) / np.sqrt(6)
    p = np.concatenate([np.linalg.lstsq(E.T, np.diag(M), rcond=None)[0], np.array([M[1, 2], M[2, 0], M[0, 1]]) / np.sqrt(1 + b * b)])
    Av, Bs = Zv(np.ones(3), a), ZS(p, b)
    rows.append((rtr(Av @ Bs), rtr(Av @ Av @ Bs), rtr(Av @ Bs @ Bs)))
rows = np.array(rows)
for k, name in enumerate(("I11", "I21", "I12")):
    c = rows[:, k] @ np.sin(2 * th) / (np.sin(2 * th) @ np.sin(2 * th))
    print(f"   {name}(th) = {c:+.4f} sin 2th, Rest {np.abs(rows[:, k] - c * np.sin(2 * th)).max():.1e}")
print("   -> Extrema bei th = pi/4 und 3pi/4, fuer jede der drei Kopplungen. Dort ist d1 = d2 (gleiche Diagonale im Block) und u = (1, +-1, 0)/sqrt 2.")

print("=" * 78)
print("C  Volles Minimum von V = V1 + V2 + eps I11 (a = 1, b = 0.5; 40 Zufallsstarts je eps)")
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
names = {1: "trivial", 2: "Z2", 3: "Z3", 4: "V4", 12: "A4"}


def stab(Ms, tol=1e-6):
    return sum(all(np.abs(R @ M @ R.T - M).max() < tol for M in Ms) for R in A4)


def V(x, eps, k1=0.3, k2=0.3):
    v, p = x[:3], x[3:]
    Av, Bs = Zv(v, a), ZS(p, b)
    q1, q2 = rtr(Av @ Av), rtr(Bs @ Bs)
    return (-q1 / 2 + k1 * np.linalg.det(Av).real + q1 ** 2 / 4 - q2 / 2 + k2 * np.linalg.det(Bs).real + q2 ** 2 / 4
            + eps * rtr(Av @ Bs))


def solve(eps):
    best = []
    for _ in range(40):
        x = rng.normal(size=8)
        for _ in range(6):
            x = minimize(V, x, args=(eps,), method="BFGS", options={"gtol": 1e-11}).x
        best.append((V(x, eps), x))
    vmin = min(f for f, _ in best)
    return vmin, [x for f, x in best if f - vmin < 1e-9], len(best)


om = np.exp(2j * np.pi / 3)
Uw = np.array([[om ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
for eps in (0.0, 1e-4, 1e-3, 1e-2, 3e-2, 1e-1, -1e-3, -1e-2):
    vmin, xs, n = solve(eps)
    out = {}
    for x in xs:
        v, p = x[:3], x[3:]
        Av, Bs = Zv(v, a), ZS(p, b)
        g = (names[stab([Av])], names[stab([Bs])], names[stab([Av, Bs])])
        d, s = p[:2] @ E, p[2:]
        o = np.argsort(np.abs(s)); k = o[-1]                     # groesste Nebendiagonale s_k, Block (i, j)
        i, j = [m for m in range(3) if m != k]
        tt = np.sqrt(1 + b * b) * s
        M = np.diag(d).astype(float); M[1, 2] = M[2, 1] = tt[0]; M[2, 0] = M[0, 2] = tt[1]; M[0, 1] = M[1, 0] = tt[2]
        ang = 0.5 * np.degrees(np.arctan2(2 * abs(tt[k]), d[i] - d[j])) if abs(tt[k]) > 1e-9 else 0.0   # Drehwinkel im Block
        w, U = np.linalg.eigh(M); u = U[:, np.argmax(np.abs(w - np.median(w)))]
        col = np.sort(np.abs((np.diag(np.sign(v)) @ Uw).conj().T @ u) ** 2)[::-1]
        key = (g, round(ang, 2), round(abs(s[o[1]]) / abs(s[k]), 4), tuple(float(c) for c in np.round(col, 3)),
               round(np.ptp(np.abs(v)) / np.abs(v).mean(), 4), int(np.sign(s[k] * v[i] * v[j])))
        out[key] = out.get(key, 0) + 1
    print(f"   eps={eps:g}: V_min = {vmin:.6f}, {len(xs)}/{n} Starts im globalen Minimum")
    for key, cnt in sorted(out.items(), key=lambda kv: -kv[1])[:3 if eps == 0 else 2]:
        g, ang, ratio, col, dv, sg = key
        print(f"      {cnt:2d}x Rest (Z_v, Z_S, beide) = {g}; Blockwinkel {ang:5.2f} Grad; |s_klein/s_gross| = {ratio:.4f};"
              f" Streuung |v_k| {dv:.4f}; sgn(s v v) = {sg:+d}; Spalte |U^+ u|^2 = {col}")
print("   Lesart: eps = 0 laesst den Winkel frei (k279). Fuer eps != 0 waehlt die Kopplung den Blockwinkel 45 Grad, bricht aber zugleich")
print("   die Z2 des zweiten Felds in erster Ordnung in eps (kleine Nebendiagonalen ~ eps). Gemeinsame Restgruppe: keine.")

print("=" * 78)
print("D  Lesart als Mischung (Setzung: Massenmatrix des zweiten Sektors ~ reeller Teil von Z_S, erster Sektor Z3-diagonal)")
for sgn, nm in ((+1, "u = (1,+1,0)/sqrt 2"), (-1, "u = (1,-1,0)/sqrt 2")):
    col = np.abs(Uw.conj().T @ (np.array([1, sgn, 0]) / np.sqrt(2))) ** 2
    print(f"   {nm}: |U_w^+ u|^2 = {np.round(col, 4)}")
print("   -> (2/3, 1/6, 1/6) ist die erste Spalte der tribimaximalen Matrix (TM1); (0, 1/2, 1/2) ist ihre dritte Spalte (theta13 = 0).")
print("      Welche auftritt, haengt am Vorzeichen von eps (b - a) kappa1 cN(a) kappa2 (in C: eps > 0 gibt die erste, eps < 0 die dritte).")
print("      Die anderen beiden Eigenwerte sind entartet (2, -1, -1): nur diese eine Spalte ist festgelegt, und nur in nullter Ordnung in eps.")
