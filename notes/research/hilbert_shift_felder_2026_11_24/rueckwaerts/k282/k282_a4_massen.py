"""k282 (Erkundung, nicht blind, 25.11.2026): Welche A4-invarianten Massenterme heben die SU(3)-Entartung aus k281 auf, und wohin?
Ein Element W im spurfreien Teil von H3(C): Diagonale d (A4: 1' + 1''), Nebendiagonale w_k = (1 + i c)(s_k + i v_k) (A4: 3 + 3), c = Ladungsmischung.
V = -q/2 + kappa N + q^2/4 + dd |d|^2/2 + dv |v|^2/2,  q = Tr W^2, N = det W.
  dv: trennt Spin 1 (v) von Spin 2 (d, s); SO(3)-invariant.      dd: trennt Diagonale von Nebendiagonale; nur A4-invariant.
A  Der C-Term: Tr((C W) o (C W)) = Tr W^2 - |d|^2 (Albert-Algebra aus k276). Ein Term dd |d|^2 ist also ein Term in C.
B  Globale Minima aus Zufallsstarts fuer ein Raster (c, dd, dv): Restgruppe in A4, Zahl der flachen Richtungen (Null-Eigenwerte der Hesse-Matrix),
   Blockwinkel, Spin-1-Anteil.
Vorab (Bilanz der Setzungen): dv allein laesst die flache Richtung stehen; dd > 0 waehlt 45 Grad, dd < 0 den V4-Punkt.
Aufruf aus diesem Ordner: python3 k282_a4_massen.py
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
rng = np.random.default_rng(282)
E = np.array([[1, -1, 0], [1, 1, -2]]) / np.array([[np.sqrt(2)], [np.sqrt(6)]])
tr = lambda X: X[:3].sum()


def W_alb(x, c):
    v, p = x[:3], x[3:]
    xv = np.zeros(27); xv[10], xv[18], xv[26] = v
    xs = np.zeros(27); xs[:3] = p[:2] @ E
    for k in range(3):
        xs[3 + 8 * k] = p[2 + k]
    return xv + c * (Corig @ xv) + xs + c * (Corig @ xs)


def W_mat(x, c):
    v, p = x[:3], x[3:]; d = p[:2] @ E; z = (1 + 1j * c) * (p[2:] + 1j * v)
    return np.array([[d[0], z[2], np.conj(z[1])], [np.conj(z[2]), d[1], z[0]], [z[1], np.conj(z[0]), d[2]]])


print("=" * 78)
print("A  Der C-Term")
e = 0
for c in (0.0, 0.5, 1.0):
    for _ in range(20):
        x = rng.normal(size=8); Wa = W_alb(x, c); CW = Corig @ Wa; d = x[3:5] @ E
        e = max(e, abs(tr(jordan(CW, CW)) - (tr(jordan(Wa, Wa)) - d @ d)))
print(f"   |Tr((CW) o (CW)) - (Tr W^2 - |d|^2)| <= {e:.1e}  -> C loescht die Diagonale und ist auf der Nebendiagonale eine Isometrie.")

print("=" * 78)
print("B  Globale Minima (kappa = -0.3, 40 Zufallsstarts je Punkt)")
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


def V(x, c, dd, dv, kappa=-0.3):
    W = W_mat(x, c); q = np.trace(W @ W).real; d = x[3:5]
    return -q / 2 + kappa * np.linalg.det(W).real + q * q / 4 + dd * (d @ d) / 2 + dv * (1 + c * c) * (x[:3] @ x[:3])


def hess(x, *args, h=1e-4):
    n = len(x); Hs = np.zeros((n, n)); I = np.eye(n)
    for i in range(n):
        for j in range(i, n):
            Hs[i, j] = Hs[j, i] = (V(x + h * I[i] + h * I[j], *args) - V(x + h * I[i] - h * I[j], *args)
                                   - V(x - h * I[i] + h * I[j], *args) + V(x - h * I[i] - h * I[j], *args)) / (4 * h * h)
    return Hs


print("   c     dd     dv   | Restgruppen der globalen Minima | flache Richtungen | Blockwinkel (Grad) | Spin-1-Anteil |v|^2/(|v|^2+|s|^2)")
for c in (0.5, 1.0):
    for dd, dv in ((0, 0), (0, 0.1), (0, -0.1), (0.1, 0), (-0.1, 0), (0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1)):
        sols = []
        for _ in range(40):
            x = rng.normal(size=8)
            for _ in range(5):
                x = minimize(V, x, args=(c, dd, dv), method="BFGS", options={"gtol": 1e-11}).x
            sols.append((V(x, c, dd, dv), x))
        vmin = min(f for f, _ in sols); glob = [x for f, x in sols if f - vmin < 1e-8]
        stabs, flats, angs, fr = {}, set(), [], []
        for x in glob:
            W = W_mat(x, c)
            k = names[int(sum(np.abs(R @ W @ R.T - W).max() < 1e-5 for R in A4))]; stabs[k] = stabs.get(k, 0) + 1
            flats.add(int((np.abs(np.linalg.eigvalsh(hess(x, c, dd, dv))) < 1e-5).sum()))
            d, s, v = x[3:5] @ E, x[5:], x[:3]
            kk = np.argmax(np.abs(s) + np.abs(v)); i, j = [m for m in range(3) if m != kk]
            off = np.hypot(s[kk], v[kk])
            angs.append(0.5 * np.degrees(np.arctan2(2 * off, abs(d[i] - d[j]))))
            fr.append(v @ v / (v @ v + s @ s + 1e-300))
        print(f"   {c:.1f}  {dd:+.1f}  {dv:+.1f}  | {str(stabs):32s}| {str(sorted(flats)):17s} | {min(angs):5.1f} bis {max(angs):5.1f}     | {min(fr):.2f} bis {max(fr):.2f}   ({len(glob)}/40 global)")
print("   Lesart: dd = dv = 0 ist k281 (vier flache Richtungen = CP^2). dv allein laesst flache Richtungen. Erst dd legt das Vakuum fest.")

print("=" * 78)
print("C  Woher die beiden Terme kommen: die zwei Strukturabbildungen des Verdopplungsschritts R -> C (Hilbert-Shift HS(0) -> HS(1))")
print("   sigma = Konjugation e7 -> -e7 (W -> W quer), C = Multiplikation mit der neuen Einheit e7 auf der Nebendiagonale.")
conj27 = np.eye(27)
for k in range(3):
    conj27[3 + 8 * k + 7, 3 + 8 * k + 7] = -1
e = [0, 0]
for c in (0.0, 0.5, 1.0):
    for _ in range(20):
        x = rng.normal(size=8); Wa = W_alb(x, c); W = W_mat(x, c); d, s, v = x[3:5] @ E, x[5:], x[:3]
        val = tr(jordan(Wa, conj27 @ Wa))
        e[0] = max(e[0], abs(val - np.trace(W @ W.conj()).real))
        e[1] = max(e[1], abs(val - (d @ d + 2 * ((1 - c * c) * (s @ s - v @ v) - 4 * c * (s @ v)))))
print(f"   |Tr(W o sigma W) Algebra - Matrix| <= {e[0]:.1e};  |Tr(W o sigma W) - (|d|^2 + 2[(1-c^2)(|s|^2-|v|^2) - 4c s.v])| <= {e[1]:.1e}")
print("   -> Fuer c = 0 ist Tr(W o sigma W) = Tr W^2 - 4|v|^2: genau der Term dv. Tr((CW) o (CW)) = Tr W^2 - |d|^2: genau der Term dd.")

# Symmetrie: Unteralgebra von su(3), die eine quadratische Form erhaelt (W -> W + i eps [T, W])
gm = []
for i in range(3):
    for j in range(i + 1, 3):
        A = np.zeros((3, 3), complex); A[i, j] = A[j, i] = 1; gm.append(A)
        B = np.zeros((3, 3), complex); B[i, j] = -1j; B[j, i] = 1j; gm.append(B)
gm += [np.diag([1, -1, 0]).astype(complex), np.diag([1, 1, -2]).astype(complex) / np.sqrt(3)]
Ws = [W_mat(rng.normal(size=8), 0.0) for _ in range(30)]


def stab_dim(forms):
    rows = []
    for W in Ws:
        for Q in forms:
            h = 1e-6
            rows.append([(Q(W + h * 1j * (T @ W - W @ T)) - Q(W - h * 1j * (T @ W - W @ T))) / (2 * h) for T in gm])
    sv = np.linalg.svd(np.array(rows), compute_uv=False)
    return int((sv < 1e-5).sum())


Q0 = lambda W: np.trace(W @ W).real
Qs = lambda W: np.trace(W @ W.conj()).real
Qd = lambda W: (np.diag(W).real ** 2).sum()
print(f"   Dimension der Symmetrie in su(3): Tr W^2 allein {stab_dim([Q0])} (ganz su(3)); mit Tr(W o sigma W) {stab_dim([Q0, Qs])} (so(3));"
      f" mit Tr((CW)^2) {stab_dim([Q0, Qd])} (Torus U(1)^2); mit beiden {stab_dim([Q0, Qs, Qd])} (diskret)")
O24 = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i, pp in enumerate(perm):
            R[i, pp] = signs[i]
        if np.linalg.det(R) > 0:
            O24.append(R)
for c in (0.0, 0.5):
    def inv(R):
        return all(abs(np.linalg.det(W_mat(x, c)).real - np.linalg.det(W_mat(xr, c)).real) < 1e-9
                   for x, xr in pairs(R, c))
    def pairs(R, c):
        out = []
        for _ in range(5):
            x = rng.normal(size=8); W0 = np.array(W_mat(x, 0.0)); Wr = R @ W0 @ R.T   # Drehung der Felder (d, s, v), dann Ladungsmischung c
            d = np.diag(Wr).real; z = np.array([Wr[1, 2], Wr[2, 0], Wr[0, 1]])
            xr = np.concatenate([z.imag, np.linalg.lstsq(E.T, d, rcond=None)[0], z.real]); out.append((x, xr))
        return out
    print(f"   c={c}: Drehungen des Wuerfels (24), die N(W) erhalten: {sum(inv(R) for R in O24)}")
print("   -> sigma bricht SU(3) auf die Familien-SO(3); C bricht weiter auf die Wuerfelgruppe; die Ladungsmischung c != 0 im kubischen Term laesst A4 (12).")
