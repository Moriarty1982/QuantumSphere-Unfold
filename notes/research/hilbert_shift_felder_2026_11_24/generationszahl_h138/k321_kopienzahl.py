"""k321 (Test H138): G2-stabile unitale Oktonion-Unteralgebren O_v = span{1} + Im(O) (x) v in A_n, n = 4, 5, 6.
Vorab-Notiz: Vorab_Notiz_H138_Kopienzahl_im_Turm.md. Produkt wie k253: (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))."""
import itertools, numpy as np

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y

def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])

def table(N):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N): C[i, j] = mul(E[i], E[j])
    return C
from scipy.optimize import least_squares
rng = np.random.default_rng(321)

# --- G2: Derivationen von O als 8x8-Matrizen (Nullraum) ---
C8 = table(8)
# einfacher: Nullraum von D -> D(xy) - D(x)y - xD(y) linear in D
def derivations(C):
    N = C.shape[0]; E = np.eye(N); M = []
    for idx in range(N*N):
        D = np.zeros(N*N); D[idx] = 1; D = D.reshape(N, N)
        cols = []
        for i in range(N):
            for j in range(N):
                cols.append(D @ C[i, j] - np.einsum('p,pk->k', D[:, i], C[:, j]) - np.einsum('p,pk->k', D[:, j], C[i, :]))
        M.append(np.concatenate(cols))
    M = np.array(M).T
    u, s, vt = np.linalg.svd(M)
    null = vt[np.sum(s > 1e-9):]
    return [v.reshape(N, N) for v in null]
G2 = derivations(C8)
print(f"[Kontrolle] dim Der(O) = {len(G2)}")

def maxclique(nodes, G):
    """Bron-Kerbosch: groesste Menge paarweise orthogonaler Kopien (|v.w| < 1e-9)."""
    adj = {a: {b for b in nodes if b != a and G[a, b] < 1e-9} for a in nodes}
    best = [0]
    def bk(R, P, X):
        if not P and not X: best[0] = max(best[0], len(R)); return
        for u in list(P):
            bk(R | {u}, P & adj[u], X & adj[u]); P = P - {u}; X = X | {u}
    bk(set(), set(nodes), set())
    return best[0]

def run(n):
    N = 2**n; m = N // 8
    C = table(N)
    # blockweise G2
    Ds = [np.kron(np.eye(m), D) for D in G2]
    E = np.eye(N); err = 0.0
    for D in Ds[:14]:
        for _ in range(3):
            x, y = rng.normal(size=N), rng.normal(size=N)
            err = max(err, np.abs(D @ mul(x, y) - mul(D @ x, y) - mul(x, D @ y)).max())
    # Kommutant-Zerlegung: Singuletts e_{8k}, Blocke e_{8k+i}
    def emb(a, v):  # a in R^7 (Im O), v in R^m
        x = np.zeros(N)
        for k in range(m): x[8*k+1:8*k+8] = v[k] * a
        return x
    Ei = np.eye(7)
    def basis(v):
        B = [E[0]] + [emb(Ei[i], v) for i in range(7)]
        return np.array(B)
    # Q[i,j,k,l,:] = e_{8k+1+i} * e_{8l+1+j}
    Q = np.array([[[[C[8*k+1+i, 8*l+1+j] for l in range(m)] for k in range(m)] for j in range(7)] for i in range(7)])
    def defect_vec(v):
        v = v / np.linalg.norm(v)
        B = basis(v); P = B.T @ B  # orthonormale Basis -> Projektor
        Z = np.einsum('ijklx,k,l->ijx', Q, v, v).reshape(49, N)
        return (Z - Z @ P).ravel()
    def defect(v): return np.linalg.norm(defect_vec(v))
    sols = []
    starts = (2000 if m < 8 else 600) if m > 1 else 50
    for s in range(starts):
        v0 = rng.normal(size=m)
        if m == 1: v0 = np.array([1.0])
        r = least_squares(defect_vec, v0, xtol=1e-15, ftol=1e-15, gtol=1e-15)
        v = r.x / np.linalg.norm(r.x)
        if s % 100 == 0: print(f'  [n={n}] Start {s}, bisher {len(sols)} Loesungen', flush=True)
        if defect(v) < 1e-10:
            if not any(min(np.linalg.norm(v - w), np.linalg.norm(v + w)) < 1e-6 for w in sols): sols.append(v)
    # Hesse auf der Sphaere (Gauss-Newton J^T J im Tangentialraum)
    info = []
    for v in sols:
        h = 1e-6; J = []
        for k in range(m):
            dv = np.zeros(m); dv[k] = h
            J.append((defect_vec(v + dv) - defect_vec(v - dv)) / (2*h))
        J = np.array(J).T
        T = np.eye(m) - np.outer(v, v)
        H = T @ (J.T @ J) @ T
        ev = np.sort(np.linalg.eigvalsh(H))[1:] if m > 1 else np.array([np.inf])
        # Alternativitaet, Normmultiplikativitaet
        B = basis(v); alt = nm = 0.0
        for _ in range(50):
            x, y = rng.normal(size=8) @ B, rng.normal(size=8) @ B
            alt = max(alt, np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max())
            nm = max(nm, abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x)*np.linalg.norm(y)))
        info.append((v, defect(v), ev.min() if len(ev) else np.inf, alt, nm))
    G = np.array([[abs(a @ b) for b in sols] for a in sols]) if sols else np.zeros((0, 0))
    # Rang der Imaginaerteile
    Ims = [basis(v)[1:] for v in sols]
    r = np.linalg.matrix_rank(np.vstack(Ims), tol=1e-8) if sols else 0
    # groesste Orthogonal-Clique (exakt, kleine Zahl)
    best = maxclique(list(range(len(sols))), G)
    print(f"\n=== n = {n} (dim {N}, m = {m} Bloecke) ===")
    print(f"[Kontrolle] Derivationsdefekt blockweise G2: {err:.1e}")
    print(f"N_{n} (Kopien bis auf +-v) = {len(sols)}")
    for v, d, hmin, alt, nm in info:
        print("  v =", np.array2string(np.round(v, 6), separator=', '), f" Defekt {d:.1e}, min Hesse {hmin:.3e}, Alternator {alt:.1e}, Norm {nm:.1e}")
    print(f"r_{n} (Rang Imaginaerteile / 7) = {r/7:.3f}  (obere Schranke m = {m})")
    okt = [k for k, (v, d, hmin, alt, nm) in enumerate(info) if alt < 1e-9 and nm < 1e-9]
    print(f"davon oktonionisch (alternativ und normmultiplikativ): {len(okt)}, nicht alternativ: {len(sols) - len(okt)}")
    if okt:
        ro = np.linalg.matrix_rank(np.vstack([Ims[k] for k in okt]), tol=1e-8) / 7
        bo = maxclique(okt, G)
        print(f"  oktonionisch: Rang/7 = {ro:.3f}, groesste orthogonale Menge = {bo}")
    print(f"o_{n} (groesste paarweise orthogonale Menge) = {best}")
    if len(sols) > 1:
        ang = sorted(set(np.round(np.degrees(np.arccos(np.clip(G[np.triu_indices(len(sols), 1)], 0, 1))), 4)))
        print(f"  auftretende Winkel zwischen Kopien (Grad, mod +-): {ang}")
    return sols

import sys
for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else (4, 5, 6)):
    run(n)
