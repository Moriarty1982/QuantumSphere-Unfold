"""k283c (Erkundung NACH dem Test H128, nachtraeglich): Was sind die 22 Derivationen von H3(S), und was bleibt fuer ein Feld in der Ladungsebene?
A: Kommutant des g2-Anteils in Der(H3(S)), Killing-Form, Wirkung auf H3(C_e8).
B: Stabilisator des Teilraums H3(C_u) in Der(H3(S)) und seine Wirkung darauf, fuer u = e7 (Ladungsrichtung) und u = e8 (Verdopplungseinheit).
C: r(u) fuer u = cos(t) e7 + sin(t) e8 und fuer Zufallseinheiten.
D: Wuerfeldrehungen, die mit der Ladung je Platz (x -> u x, x -> x u) vertauschen.
Aufruf: python3 k283c_struktur.py
"""
import itertools, numpy as np
import k283_test_h128 as k
rng = np.random.default_rng(2831)
n = 4
J, T, d, N = k.albert(n)
Ds, gap, res = k.der_alg(J, N, pairs=N + 25)
print(f"Der(H3(S)): dim {len(Ds)} (Luecke {gap:.1e})")
G2 = k.known_ders(T, d, N); SO3 = k.so3_ders(J, N, d)
flat = lambda Ms: np.array([m.ravel() for m in Ms])
rank = lambda M: np.linalg.matrix_rank(M, tol=1e-9)

# A: Kommutant von g2 in Der
rows = []
for g in G2:
    rows.append(np.array([(D @ g - g @ D).ravel() for D in Ds]).T)
V, _ = k.nullspace(np.vstack(rows))
Com = [np.einsum('i,ijk->jk', v, Ds) for v in V]
print(f"A: Kommutant von g2 in Der: dim {len(Com)}; g2 + Kommutant spannt dim {rank(flat(G2 + Com))}; so(3) liegt im Kommutanten: Rang bleibt {rank(flat(Com + SO3))}")
# Abgeschlossenheit und Killing-Form des Kommutanten
Cf = flat(Com); Q, _ = np.linalg.qr(Cf.T)
cl = max(np.abs((a @ b - b @ a).ravel() - Q @ (Q.T @ (a @ b - b @ a).ravel())).max() for a in Com for b in Com)
coef = lambda M: np.linalg.lstsq(Cf.T, M.ravel(), rcond=None)[0]
ad = [np.array([coef(a @ b - b @ a) for b in Com]).T for a in Com]
Kil = np.array([[np.trace(x @ y) for y in ad] for x in ad])
ev = np.linalg.eigvalsh(Kil)
print(f"   abgeschlossen (Rest {cl:.1e}); Killing-Form Eigenwerte von {ev.min():.3f} bis {ev.max():.3f} (negativ definit -> kompakt halbeinfach, dim 8 -> su(3))")
# Wirkung auf H3(C_e8)
def plane(u):
    S, Vv = k.field_basis(d, N, u)
    one = np.zeros(N); one[:3] = 1 / np.sqrt(3)
    return np.vstack([one[None], S, Vv])     # 9 Vektoren, orthonormal
e = lambda i: np.eye(d)[i]
for tag, u in [('e8', e(8)), ('e7', e(7))]:
    Pl = plane(u); Pr = Pl.T @ Pl
    leak = max(np.abs((np.eye(N) - Pr) @ D @ Pl.T).max() for D in Com)
    print(f"   Kommutant auf H3(C_{tag}): Leck aus dem Teilraum {leak:.1e}; Rang der eingeschraenkten Wirkung {rank(flat([Pl @ D @ Pl.T for D in Com]))}")

# B: Stabilisator von H3(C_u) in ganz Der
for tag, u in [('e7', e(7)), ('e8', e(8)), ('e15', e(15))]:
    Pl = plane(u); Pr = Pl.T @ Pl
    M = np.array([((np.eye(N) - Pr) @ D @ Pl.T).ravel() for D in Ds]).T
    Vs, _ = k.nullspace(M) if np.abs(M).max() > 1e-9 else (np.eye(len(Ds)), None)
    St = [np.einsum('i,ijk->jk', v, Ds) for v in Vs]
    act = [Pl @ D @ Pl.T for D in St]
    ra = rank(flat(act)) if act else 0
    # liegt die Wirkung in der so(3)?
    so3act = flat([Pl @ D @ Pl.T for D in SO3])
    print(f"B: u = {tag}: Stabilisator von H3(C_u) in Der: dim {len(St)}; wirksame Dimension auf H3(C_u): {ra}; zusammen mit so(3): Rang {rank(np.vstack([flat(act), so3act]))}")

# C: r(u)
def ratio(u):
    S, Vv = k.field_basis(d, N, u)
    K, _ = k.forms(J, N, np.vstack([S, Vv]))
    return np.diag(K)[5:].mean() / np.diag(K)[:5].mean(), np.ptp(np.diag(K)[5:])
print("C: r(u) fuer u = cos(t) e7 + sin(t) e8:")
for t in [0, 15, 30, 45, 60, 75, 90]:
    c, s = np.cos(np.radians(t)), np.sin(np.radians(t))
    r, sp = ratio(c * e(7) + s * e(8))
    print(f"   t = {t:2d} Grad: r = {r:.10f}   (1 - cos^2(t)/10 = {1 - c * c / 10:.10f})")
rs = []
for _ in range(6):
    u = np.zeros(d); u[1:] = rng.normal(size=d - 1); u /= np.linalg.norm(u)
    r, sp = ratio(u); rs.append((r, 1 - (1 - u[8] ** 2) / 10, sp))
print("   Zufallseinheiten: r, 1 - (1 - u8^2)/10, Streuung:", "; ".join(f"{a:.8f}, {b:.8f}, {c:.1e}" for a, b, c in rs))

# D: Wuerfeldrehungen und Ladung
def slot_op(M):
    O = np.zeros((N, N))
    for kk in range(3): O[3 + kk * d:3 + (kk + 1) * d, 3 + kk * d:3 + (kk + 1) * d] = M
    return O
pos = [(1, 2), (2, 0), (0, 1)]
B = np.zeros((N, 3, 3, d))
for kk in range(3): B[kk, kk, kk, 0] = 1.0
for kk, (i, j) in enumerate(pos):
    for p in range(d):
        ee = np.zeros(d); ee[p] = 1 / np.sqrt(2); B[3 + kk * d + p, i, j] = ee; B[3 + kk * d + p, j, i] = k.conj(ee)
def rep(R):
    C = np.einsum('ik,akjp,lj->ailp', R, B, R)
    M = np.zeros((N, N))
    for kk in range(3): M[kk] = C[:, kk, kk, 0]
    for kk, (i, j) in enumerate(pos): M[3 + kk * d:3 + (kk + 1) * d] = np.sqrt(2) * C[:, i, j, :].T
    return M
cube = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3): R[i, perm[i]] = sg[i]
        if np.linalg.det(R) > 0: cube.append(R)
for tag, i in [('e7', 7), ('e8', 8)]:
    Lu, Ru = slot_op(T[i].T), slot_op(T[:, i, :].T)
    ok = [R for R in cube if max(np.abs(rep(R) @ X - X @ rep(R)).max() for X in (Lu, Ru)) < 1e-10]
    so = max(np.abs(D @ X - X @ D).max() for D in SO3 for X in (Lu, Ru))
    print(f"D: Ladung u = {tag}: {len(ok)} von {len(cube)} Wuerfeldrehungen vertauschen mit L_u, R_u je Platz; [so(3), Ladung] max {so:.2f}")
