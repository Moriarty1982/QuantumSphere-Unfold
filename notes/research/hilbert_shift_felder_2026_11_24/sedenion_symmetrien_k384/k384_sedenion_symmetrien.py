"""k384 (Erkundung, nicht blind): Verknuepfen die endlichen Symmetrien der Sedenionen (HS(4)) die zwei Farbbloecke aus k380,
und folgt daraus eine Beziehung fuer den Up-Sektor?
Aufruf: python k384_sedenion_symmetrien.py > k384_out.txt"""
import numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(384)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
N = 16; E = np.eye(N)
C = np.array([[mul(E[i], E[j]) for j in range(N)] for i in range(N)])
def aut(A):
    """Automorphismus-Defekt max |A(e_i e_j) - (A e_i)(A e_j)| (exakt auf der Basis, bilinear)."""
    AC = np.einsum('ijk,lk->ijl', C, A)
    CA = np.einsum('pi,qj,pqk->ijk', A, A, C)
    return np.abs(AC - CA).max()
def fam(A2, s8):
    """A2 (2x2) wirkt auf den Kopienindex der Paare (e_i, e_{i+8}), i = 1..7; e0 fest, e8 -> s8 e8."""
    M = np.zeros((N, N)); M[0, 0] = 1; M[8, 8] = s8
    for i in range(1, 8):
        M[i, i] = A2[0, 0]; M[i, i+8] = A2[0, 1]; M[i+8, i] = A2[1, 0]; M[i+8, i+8] = A2[1, 1]
    return M
rot = lambda t: np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
ref = lambda t: np.array([[np.cos(t), np.sin(t)], [np.sin(t), -np.cos(t)]])

print("== A. Endliche Symmetrien: alle Abbildungen, die mit G2 (blockweise) vertauschen ==")
print("   Familie: 1 (x) A auf Im O (x) R^2 (Paare e_i, e_{i+8}), e0 fest, e8 -> +-e8; A = Drehung oder Spiegelung um Winkel t")
ts = np.arange(0, 360, 1) * np.pi / 180
for lab, gen, s8 in (("Drehung, e8 -> +e8", rot, 1), ("Drehung, e8 -> -e8", rot, -1), ("Spiegelung, e8 -> +e8", ref, 1), ("Spiegelung, e8 -> -e8", ref, -1)):
    d = np.array([aut(fam(gen(t), s8)) for t in ts])
    zeros = [int(round(t * 180 / np.pi)) for t, x in zip(ts, d) if x < 1e-12]
    print(f"   {lab}: Automorphismus bei t = {zeros} Grad (Raster 1 Grad); kleinster Defekt sonst {d[d >= 1e-12].min():.3f}")
psi = fam(rot(2 * np.pi / 3), 1); eps = fam(ref(0), -1)
print(f"   psi (Drehung 120 Grad), eps (Vorzeichen von O*l): Defekte {aut(psi):.1e}, {aut(eps):.1e}")
print(f"   psi^3 = 1: {np.allclose(np.linalg.matrix_power(psi, 3), np.eye(N))}; eps^2 = 1: {np.allclose(eps @ eps, np.eye(N))}; eps psi eps = psi^-1: {np.allclose(eps @ psi @ eps, psi.T)}")
grp = [np.linalg.matrix_power(psi, k) @ np.linalg.matrix_power(eps, m) for k in range(3) for m in range(2)]
print(f"   erzeugte Gruppe: {len(grp)} Elemente (S3), alle Automorphismen: {max(aut(g) for g in grp) < 1e-12}")

# Derivationen, Farbe
rows = []
for i in range(N):
    for j in range(N):
        for k in range(N):
            r = np.zeros((N, N)); r[k, :] += C[i, j, :]; r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]; rows.append(r.ravel())
A = np.array(rows); der = null_space(A, rcond=1e-9)
fix = np.zeros((N, N * N))
for k in range(N): fix[k, k * N + 7] = 1
st = null_space(np.vstack([A, fix]), rcond=1e-9)
gens = [st[:, a].reshape(N, N) for a in range(st.shape[1])]
dgens = [der[:, a].reshape(N, N) for a in range(der.shape[1])]
print(f"   dim Der(S) = {der.shape[1]} (zusammenhaengender Teil G2); Farbe = Stabilisator von e7: {len(gens)}")
print(f"   S3 vertauscht mit ganz G2: max |[D, psi]| = {max(np.abs(D @ psi - psi @ D).max() for D in dgens):.1e}, max |[D, eps]| = {max(np.abs(D @ eps - eps @ D).max() for D in dgens):.1e}")

print("\n== B. Wirkung auf U = e7, auf den Tausch J und auf die Sektoren ==")
U = E[7]; J = np.array([mul(U, conj(E[i])) for i in range(N)]).T
Kc = np.diag([1.0] + [-1.0] * (N - 1))
print(f"   eps U = U: {np.allclose(eps @ U, U)}; psi U = U: {np.allclose(psi @ U, U)}; psi U = -1/2 e7 + (sqrt3/2) e15: {np.allclose(psi @ U, -0.5 * E[7] + np.sqrt(3) / 2 * E[15])}")
print(f"   eps J eps = J: {np.allclose(eps @ J @ eps, J)}; |psi J psi^-1 - J| = {np.abs(psi @ J @ psi.T - J).max():.4f}")
c1 = list(range(1, 7)); c2 = list(range(9, 15)); s1 = [0, 7]; s2 = [8, 15]
blk = lambda M, a, b: np.abs(M[np.ix_(a, b)]).max()
print(f"   eps: Block 1 (e1..e6) -> +Block 1, Block 2 (e9..e14) -> -Block 2: {np.allclose(eps[np.ix_(c1, c1)], np.eye(6)) and np.allclose(eps[np.ix_(c2, c2)], -np.eye(6))}")
print(f"   psi mischt die Farbbloecke: |psi(Block 2 <- Block 1)| = {blk(psi, c2, c1):.4f} (sqrt3/2 = {np.sqrt(3)/2:.4f}); mischt e7 mit e15: {blk(psi, [15], [7]):.4f}; laesst e0, e8 fest: {np.allclose(psi[np.ix_([0, 8], [0, 8])], np.eye(2))}")
print("   Die zwei Farbbloecke sind also die zwei Komponenten eines S3-Dubletts: (3 + 3bar) (x) 2; ebenso (e7, e15); e0 trivial, e8 Vorzeichendarstellung.")

print("\n== C. Invariante quadratische Formen (Massenterme) je nach geforderter Symmetrie ==")
idx = [(i, j) for i in range(N) for j in range(i, N)]
basis = []
for (i, j) in idx:
    B = np.zeros((N, N)); B[i, j] = B[j, i] = 1; basis.append(B)
def forms(extra):
    cons = [np.array([(g.T @ B + B @ g).ravel() for B in basis]).T for g in gens]
    cons += [np.array([(M.T @ B @ M - B).ravel() for B in basis]).T for M in extra]
    ns = null_space(np.vstack(cons), rcond=1e-9)
    return [sum(ns[k, a] * basis[k] for k in range(len(basis))) for a in range(ns.shape[1])]
rk = lambda Qs, a, b: int(np.linalg.matrix_rank(np.array([Q[np.ix_(a, b)].ravel() for Q in Qs]), tol=1e-9)) if Qs else 0
print("   Spalten: gesamt | Block 1 | Block 2 | zwischen den Farbbloecken | farblos (e0,e7,e8,e15)")
res = {}
for lab, ex in (("nur Farbe", []), ("Farbe + eps", [eps]), ("Farbe + psi (Z3)", [psi]), ("Farbe + S3", [psi, eps]),
                ("Farbe + Konjugation + J", [Kc, J]), ("Farbe + Konjugation + J + eps", [Kc, J, eps]),
                ("Farbe + Konjugation + S3", [Kc, psi, eps])):
    Qs = forms(ex); res[lab] = Qs
    print(f"   {lab:32s}: {len(Qs):2d} | {rk(Qs, c1, c1)} | {rk(Qs, c2, c2)} | {rk(Qs, c1, c2)} | {rk(Qs, s1 + s2, s1 + s2)}")
Qs = res["Farbe + S3"]
col = c1 + c2
# unter S3: sind die Koeffizienten auf Block 1 und Block 2 gleich?
ratios = []
for Q in Qs:
    a1 = np.trace(Q[np.ix_(c1, c1)]) / 6; a2 = np.trace(Q[np.ix_(c2, c2)]) / 6
    ratios.append((a1, a2))
print("   Farbe + S3: Koeffizient je Form auf Block 1 / Block 2 (Spur/6): " + "; ".join(f"{a:+.4f} / {b:+.4f}" for a, b in ratios))
print(f"   Farbe + S3: groesste Abweichung Block 1 gegen Block 2: {max(abs(a - b) for a, b in ratios):.1e}; Form auf (e7, e15) proportional zur Eins: {max(abs(Q[7, 7] - Q[15, 15]) + abs(Q[7, 15]) for Q in Qs):.1e}")
# Zerlegung der Brechung: welche S3-Darstellungen tragen die Formen von 'Farbe + eps'?
Qe = res["Farbe + eps"]
print(f"   Bricht U = e7 die S3 auf Z2 = {{1, eps}}, kommen {len(Qe) - len(Qs)} freie Brechungskoeffizienten dazu (Farbe + eps: {len(Qe)}, Farbe + S3: {len(Qs)}).")

print("\n== D. Folge fuer Up und Down ==")
rho = {"e": 1.0, "d": 1.115, "u": 1.290}; Kv = {"e": 0.66666, "d": 0.7478, "u": 0.8876}
print("   Ungebrochene S3 gaebe gleiche Massenterme fuer beide Farbbloecke, also K_u = K_d und rho_u = rho_d.")
print(f"   Daten (M_Z): K_d = {Kv['d']}, K_u = {Kv['u']}; rho_d = {rho['d']}, rho_u = {rho['u']}")
print(f"   Brechung in rho: Mittel a = {(rho['u'] + rho['d']) / 2:.4f}, Dublettanteil b = {(rho['u'] - rho['d']) / 2:.4f}, b/a = {(rho['u'] - rho['d']) / (rho['u'] + rho['d']):.4f}")
print(f"   Brechung in K:   Mittel a = {(Kv['u'] + Kv['d']) / 2:.4f}, Dublettanteil b = {(Kv['u'] - Kv['d']) / 2:.4f}, b/a = {(Kv['u'] - Kv['d']) / (Kv['u'] + Kv['d']):.4f}")
print("   Zwei Farbbloecke, zwei Koeffizienten (a, b): keine Beziehung fuer Up aus S3 allein.")

print("\n== E. Zusatz: S3 zusammen mit dem Tausch, und die Ladung auf den Bloecken ==")
Js = [np.linalg.matrix_power(psi, k) @ J @ np.linalg.matrix_power(psi, k).T for k in range(3)]     # Tausch zu U_k = psi^k U
Qa = forms([Kc, psi, eps] + Js)
print(f"   Farbe + Konjugation + S3 + alle drei Tausche J_k: {len(Qa)} Formen | Farbe {rk(Qa, col, col)} | farblos {rk(Qa, s1 + s2, s1 + s2)}")
for Q in Qa:
    print("      Diagonale (e0, e7, e8, e15 | Block 1 | Block 2): " + ", ".join(f"{Q[i, i]:+.4f}" for i in (0, 7, 8, 15)) + f" | {Q[1, 1]:+.4f} | {Q[9, 9]:+.4f}")
Lm = lambda x: np.einsum('i,ijk->kj', x, C); Rm = lambda x: np.einsum('j,ijk->ki', x, C)
Q0 = 0.5 * np.eye(N) - 1j / 6 * Lm(U) - 1j / 3 * Rm(U)                                            # Ladung der Kopie 0 (k85-Form, wie k323)
def spec(ix):
    P = np.zeros((N, N)); P[ix, ix] = 1
    leak = np.abs((np.eye(N) - P) @ Q0 @ P).max()
    ev = np.sort(np.linalg.eigvals(Q0[np.ix_(ix, ix)]).real)
    return leak, ", ".join(f"{v:.4f}" for v in ev)
for lab, ix in (("farblose Ebene {e0, e7}", s1), ("Farbblock 1 (in O)", c1), ("farblose Ebene {e8, e15}", s2), ("Farbblock 2 (in O*l)", c2)):
    lk, sp = spec(ix); print(f"   Q_0 auf {lab:26s}: Leck {lk:.1e}; Eigenwerte {sp}")
print(f"   [Q_0, eps] = 0: {np.allclose(Q0 @ eps, eps @ Q0)}; Q_0 vertauscht mit der Farbe: {max(np.abs(Q0 @ g - g @ Q0).max() for g in gens):.1e}")

print("\n== F. Zusatz: hermitesche Formen auf C (x) A, die mit Farbe und Ladung vertauschen ==")
def herm_count(n, extra=()):
    e = np.eye(n); Cn = np.array([[mul(e[i], e[j]) for j in range(n)] for i in range(n)])
    rows = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r = np.zeros((n, n)); r[k, :] += Cn[i, j, :]; r[:, i] -= Cn[:, j, k]; r[:, j] -= Cn[i, :, k]; rows.append(r.ravel())
    fx = np.zeros((n, n * n))
    for k in range(n): fx[k, k * n + 7] = 1
    s = null_space(np.vstack([np.array(rows), fx]), rcond=1e-9)
    gs = [s[:, a].reshape(n, n) for a in range(s.shape[1])]
    Ln = np.einsum('i,ijk->kj', e[7], Cn); Rn = np.einsum('j,ijk->ki', e[7], Cn)
    Q = 0.5 * np.eye(n) - 1j / 6 * Ln - 1j / 3 * Rn
    ops = gs + [Q] + [M[:n, :n] if n == 16 else M for M in extra]
    # Kommutant (komplexe Dimension = reelle Dimension der hermiteschen Matrizen darin, da die Menge unter Adjungieren abgeschlossen ist)
    cons = [np.kron(np.eye(n), X) - np.kron(X.T, np.eye(n)) for X in ops]
    sv = np.linalg.svd(np.vstack(cons), compute_uv=False)
    ev = np.round(np.linalg.eigvals(Q).real, 4)
    return int(np.sum(sv < 1e-9)), sorted(float(x) for x in ev)
d8, ev8 = herm_count(8); d16, ev16 = herm_count(16); d16e, _ = herm_count(16, (eps,))
print(f"   O: Ladungen {ev8}")
print(f"   O: hermitesche Formen (Farbe + Q_0): {d8}  (erwartet 4: je eine fuer Ladung 0, 1/3, 2/3, 1)")
print(f"   S: Ladungen {ev16}")
print(f"   S: hermitesche Formen (Farbe + Q_0): {d16}; zusaetzlich eps: {d16e}")
Jc = J.astype(complex)
print(f"   Tausch J (komplex-linear fortgesetzt) und Ladung: auf {{e0, e7}} J Q_0 J^-1 = 1 - Q_0: {np.allclose((Jc @ Q0 @ np.linalg.inv(Jc))[np.ix_(s1, s1)], (np.eye(N) - Q0)[np.ix_(s1, s1)])}; auf den Farbbloecken J Q_0 J^-1 = Q_0: {np.allclose((Jc @ Q0 @ np.linalg.inv(Jc))[np.ix_(col, col)], Q0[np.ix_(col, col)])}")
