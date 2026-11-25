"""k260 (Erkundung, nicht blind, 25.11.2026): Die drei Oktonion-Kopien O_0, O_120, O_240 der Sedenionen auf den drei Plaetzen von H3(S).
A: S3-Automorphismen von S explizit; Kopien als Bilder von O_0.
B: Teilraum W = {Diagonale reell, Eintrag k in Kopie k} (27 Dim.): Abschluss unter dem Jordan-Produkt, wohin das Leck geht.
C: Welche Elemente von (24 Wuerfeldrehungen) x S3 erhalten W? Welche Derivationen von H3(S)?
D: Ladung je Platz in der Richtung der jeweiligen Kopie: welche Elemente vertauschen damit?
E: Massenform K aus H128 auf dem farbneutralen Feld in W.
F: Kommutant von su(3)_c auf dem Triplett-Teil (Vollstaendigkeit der Parametrisierung aus H130).
Aufruf: python3 k260_drei_kopien_plaetze.py   (benutzt ../kollaps_h128/k283_test_h128.py und ../ladungsrichtung_h130/k258_test_h130.py)
"""
import sys, os, itertools, numpy as np
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'kollaps_h128')); sys.path.insert(0, os.path.join(here, '..', 'ladungsrichtung_h130'))
import k283_test_h128 as k
import k258_test_h130 as h
rng = np.random.default_rng(260)
n = 4; J, T, d, N = k.albert(n)
E = np.eye(d); mul = lambda x, y: np.einsum('i,j,ijk->k', x, y, T)

print("=" * 78); print("A  S3 auf den Sedenionen")
def rot(phi, s=1):
    M = np.eye(d); c, sn = np.cos(phi), np.sin(phi)
    for i in range(1, 8):
        M[i, i] = c; M[i + 8, i] = s * sn; M[i, i + 8] = -s * sn; M[i + 8, i + 8] = c
    return M
def is_aut(M):
    return max(np.abs(M @ mul(x, y) - mul(M @ x, M @ y)).max() for x, y in [(rng.normal(size=d), rng.normal(size=d)) for _ in range(20)])
refl = np.diag([1.0] * 8 + [-1.0] * 8)
rho = rot(2 * np.pi / 3)
print(f"   Drehung um 120 Grad in den Ebenen (e_i, e_i+8), e8 fest: Automorphismus-Rest {is_aut(rho):.1e}; um 90 Grad (Gegenprobe): {is_aut(rot(np.pi / 2)):.1e}")
print(f"   Spiegelung (a, b) -> (a, -b): Rest {is_aut(refl):.1e}")
S3 = {'1': np.eye(d), 'r': rho, 'r2': rho @ rho, 's': refl, 'sr': refl @ rho, 'sr2': refl @ rho @ rho}
copies = [np.linalg.matrix_power(rho, kk)[:, :8].T for kk in range(3)]      # Basis (8 x 16) der Kopie k = rho^k(O_0)
us = [np.linalg.matrix_power(rho, kk) @ E[7] for kk in range(3)]
for kk in range(3): print(f"   Kopie {kk}: Ladungsrichtung u_{kk} = {us[kk][7]:+.4f} e7 {us[kk][15]:+.4f} e15")
perm_of = {}
for nm, M in S3.items():
    pm = []
    for kk in range(3):
        img = copies[kk] @ M.T
        pm.append([j for j in range(3) if np.linalg.matrix_rank(np.vstack([copies[j], img]), tol=1e-9) == 8][0])
    perm_of[nm] = tuple(pm)
print("   Wirkung auf die Kopien (Kopie k -> ...):", perm_of)

print("=" * 78); print("B  Teilraum W: Kopie k auf Platz k")
def Wbasis(assign=(0, 1, 2)):
    rows = [np.eye(N)[i] for i in range(3)]
    for kk in range(3):
        for b in copies[assign[kk]]:
            v = np.zeros(N); v[3 + kk * d:3 + (kk + 1) * d] = b; rows.append(v)
    return np.array(rows)
W = Wbasis(); PW = W.T @ W
P = np.einsum('pa,qb,abc->pqc', W, W, J)
leak = P - P @ PW
print(f"   dim W = {np.linalg.matrix_rank(W)}; Abschlussdefekt max {np.abs(leak).max():.4f}")
lk = np.abs(leak).reshape(-1, N).max(axis=0)
comp = sorted(set((int((i - 3) % d)) for i in np.nonzero(lk > 1e-9)[0] if i >= 3))
print(f"   Leck in den Sedenion-Komponenten {comp} der Nebendiagonale (also nicht nur e8), Diagonale: {lk[:3].max():.1e}")
Wp = np.vstack([W] + [np.eye(N)[3 + kk * d + 8][None] for kk in range(3)]); PWp = np.linalg.qr(Wp.T)[0]
Pp = np.einsum('pa,qb,abc->pqc', Wp, Wp, J)
print(f"   W + e8 je Platz (30 Dim.): Abschlussdefekt {np.abs(Pp - (Pp @ PWp) @ PWp.T).max():.4f}")

print("=" * 78); print("C  Symmetrie von W")
pos = [(1, 2), (2, 0), (0, 1)]
Bm = np.zeros((N, 3, 3, d))
for kk in range(3): Bm[kk, kk, kk, 0] = 1.0
for kk, (i, j) in enumerate(pos):
    for p in range(d):
        ee = np.zeros(d); ee[p] = 1 / np.sqrt(2); Bm[3 + kk * d + p, i, j] = ee; Bm[3 + kk * d + p, j, i] = k.conj(ee)
def to_coords(C):
    M = np.zeros((N, N))
    for kk in range(3): M[kk] = C[:, kk, kk, 0]
    for kk, (i, j) in enumerate(pos): M[3 + kk * d:3 + (kk + 1) * d] = np.sqrt(2) * C[:, i, j, :].T
    return M
repR = lambda R: to_coords(np.einsum('ik,akjp,lj->ailp', R, Bm, R))
repS = lambda M: to_coords(np.einsum('aijp,qp->aijq', Bm, M))
cube = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.linalg.det(R) > 0: cube.append(R)
keep = lambda M, Pr: np.abs((np.eye(N) - Pr) @ M @ Pr).max() < 1e-9
G = [(R, nm, repR(R) @ repS(M)) for R in cube for nm, M in S3.items()]
aut = max(np.abs(g @ np.einsum('a,b,abc->c', x, y, J) - np.einsum('a,b,abc->c', g @ x, g @ y, J)).max()
          for (_, _, g) in G[::7] for x, y in [(rng.normal(size=N), rng.normal(size=N))])
stab = [(R, nm, g) for (R, nm, g) in G if keep(g, PW)]
print(f"   (24 Wuerfeldrehungen) x S3 = {len(G)} Automorphismen von H3(S) (Rest {aut:.1e}); davon erhalten W: {len(stab)}")
only_cube = [1 for (R, nm, g) in stab if nm == '1']
print(f"   davon reine Wuerfeldrehungen (ohne S3-Anteil): {len(only_cube)}; je Wuerfeldrehung hoechstens ein passendes S3-Element: {len(set(tuple(R.ravel()) for R, _, _ in stab)) == len(stab)}")
mats = [g for _, _, g in stab]
def order(g):
    m = g.copy(); o = 1
    while np.abs(m - np.eye(N)).max() > 1e-8: m = m @ g; o += 1
    return o
from collections import Counter
closed = all(any(np.abs(a @ b - c).max() < 1e-8 for c in mats) for a in mats[:6] for b in mats)
print(f"   abgeschlossen: {closed}; Elementordnungen {dict(sorted(Counter(order(g) for g in mats).items()))}  (S4: 1x1, 9x2, 8x3, 6x4)")
Ds, gap, res = k.der_alg(J, N, pairs=N + 25)
M = np.array([((np.eye(N) - PW) @ D @ PW).ravel() for D in Ds]).T
Vs, _ = k.nullspace(M)
St = [np.einsum('i,ijk->jk', v, Ds) for v in Vs]
so3 = k.so3_ders(J, N, d); g2 = k.known_ders(T, d, N)
fl = lambda Ms: np.array([m.ravel() for m in Ms])
print(f"   Derivationen von H3(S) (dim {len(Ds)}), die W erhalten: dim {len(St)}; zusammen mit g2 Rang {np.linalg.matrix_rank(np.vstack([fl(St), fl(g2)]), tol=1e-9)} -> stetig bleibt nur g2")

print("=" * 78); print("D  Ladung je Platz in der Richtung der Kopie")
def slot3(Ms):
    O = np.zeros((N, N))
    for kk in range(3): O[3 + kk * d:3 + (kk + 1) * d, 3 + kk * d:3 + (kk + 1) * d] = Ms[kk]
    return O
Lop = lambda u: np.einsum('i,ijk->kj', u, T); Rop = lambda u: np.einsum('j,ijk->ki', u, T)
CL, CR = slot3([Lop(u) for u in us]), slot3([Rop(u) for u in us])
ok = [(R, nm) for (R, nm, g) in stab if max(np.abs(g @ X - X @ g).max() for X in (CL, CR)) < 1e-9]
okpm = [(R, nm) for (R, nm, g) in stab if min(max(np.abs(g @ CL - s1 * CL @ g).max(), np.abs(g @ CR - s2 * CR @ g).max()) for s1 in (1, -1) for s2 in (1, -1)) < 1e-9
        or min(max(np.abs(g @ CL - s1 * CR @ g).max(), np.abs(g @ CR - s2 * CL @ g).max()) for s1 in (1, -1) for s2 in (1, -1)) < 1e-9]
print(f"   von den {len(stab)} Elementen vertauschen {len(ok)} mit L_u und R_u je Platz; bis auf Vorzeichen und Tausch L <-> R: {len(okpm)}")
print(f"   Ordnungen der vertauschenden Elemente: {dict(sorted(Counter(order(g) for (R, nm, g) in stab if (tuple(R.ravel()), nm) in set((tuple(a.ravel()), b) for a, b in ok)).items()))}  (A4: 1x1, 3x2, 8x3)")

print("=" * 78); print("E  Massenform K auf dem farbneutralen Feld in W (Eintrag k in span(1, u_k))")
S = []
v = np.zeros(N); v[0], v[1] = 1, -1; S.append(v / np.sqrt(2))
v = np.zeros(N); v[0], v[1], v[2] = 1, 1, -2; S.append(v / np.sqrt(6))
for kk in range(3): v = np.zeros(N); v[3 + kk * d] = 1; S.append(v)
V = []
for kk in range(3): v = np.zeros(N); v[3 + kk * d:3 + (kk + 1) * d] = us[kk]; V.append(v)
K, T2 = k.forms(J, N, np.array(S + V))
print(f"   K diagonal: {np.round(np.diag(K), 8)}; groesstes Nebendiagonalelement {np.abs(K - np.diag(np.diag(K))).max():.1e}")
Vsame = []
for kk in range(3): v = np.zeros(N); v[3 + kk * d + 7] = 1; Vsame.append(v)
K0, _ = k.forms(J, N, np.array(S + Vsame))
print(f"   zum Vergleich alle drei Plaetze mit u = e7 (H128): {np.round(np.diag(K0), 8)}")
# kubische Invariante: Tr(Z o Z o Z) auf dem Spin-1-Teil, Kopien gegen gleiche Richtung
def cubic(vs, c):
    z = sum(ci * vi for ci, vi in zip(c, vs)); zz = np.einsum('a,b,abc->c', z, z, J); return float(np.einsum('a,b,abc->c', zz, z, J)[:3].sum())
c = np.array([1, 1, 1]) / np.sqrt(3)
print(f"   Tr(Z^3) fuer Z = (v1 + v2 + v3)/sqrt3: drei Kopien {cubic(V, c):+.6f}, gleiche Richtung {cubic(Vsame, c):+.6f}")
mix = [np.cos(0.7) * s_ + np.sin(0.7) * v_ for s_, v_ in zip(S[2:], V)]; mix0 = [np.cos(0.7) * s_ + np.sin(0.7) * v_ for s_, v_ in zip(S[2:], Vsame)]
print(f"   mit Realteil gemischt (Winkel 0.7): drei Kopien {cubic(mix, c):+.6f}, gleiche Richtung {cubic(mix0, c):+.6f}")

print("=" * 78); print("F  Vollstaendigkeit der Parametrisierung aus H130")
SU3 = h.der_S(fix=7)
Tidx = [i for i in range(16) if i not in (0, 7, 8, 15)]
rows = [np.kron(np.eye(12), D[np.ix_(Tidx, Tidx)]) - np.kron(D[np.ix_(Tidx, Tidx)].T, np.eye(12)) for D in SU3]
com = h.nullspace(np.vstack(rows))
print(f"   Kommutant von su(3)_c auf dem Triplett-Teil T (12 Dim.): dim {len(com)} (= M_2(C); stabile 6-dim. Teilraeume = Punkte von CP^1 = V(a,b,c,d))")
