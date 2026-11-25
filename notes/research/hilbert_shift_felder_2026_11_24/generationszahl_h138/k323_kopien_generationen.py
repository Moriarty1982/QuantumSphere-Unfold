"""k323 (Test H140): Sind die drei Sedenion-Kopien Generationen? Farbe su(3)_k, Ladung Q_k (k85-Form), S3-Vertauschung,
gemeinsame Ladung in der Familie a + b L_x + c R_x, Dimension der Summe. Vorab: Vorab_Notiz_H140_Kopien_als_Generationen.md."""
import numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(323)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
N = 16; E = np.eye(N)
C = np.array([[mul(E[i], E[j]) for j in range(N)] for i in range(N)])
Lm = lambda x: np.einsum('i,ijk->kj', x, C)
Rm = lambda x: np.einsum('j,ijk->ki', x, C)
C8 = np.array([[mul(np.eye(8)[i], np.eye(8)[j]) for j in range(8)] for i in range(8)])
def derivations(C):
    n = C.shape[0]; M = []
    for idx in range(n*n):
        D = np.zeros(n*n); D[idx] = 1; D = D.reshape(n, n); cols = []
        for i in range(n):
            for j in range(n):
                cols.append(D @ C[i, j] - np.einsum('p,pk->k', D[:, i], C[:, j]) - np.einsum('p,pk->k', D[:, j], C[i, :]))
        M.append(np.concatenate(cols))
    u, s, vt = np.linalg.svd(np.array(M).T)
    return [v.reshape(n, n) for v in vt[np.sum(s > 1e-9):]]
G2 = [np.kron(np.eye(2), D) for D in derivations(C8)]
def emb(a, f):
    x = np.zeros(N); x[1:8] = f[0]*a; x[9:16] = f[1]*a; return x
th = [0, 2*np.pi/3, 4*np.pi/3]; F = [np.array([np.cos(t), np.sin(t)]) for t in th]
e7 = np.zeros(7); e7[6] = 1
U = [emb(e7, f) for f in F]
B = [np.array([E[0]] + [emb(np.eye(7)[i], f) for i in range(7)]) for f in F]   # 8 x 16, orthonormal
P = [b.T @ b for b in B]
# psi, eps
c, s = np.cos(2*np.pi/3), np.sin(2*np.pi/3)
psi = np.eye(N)
for i in range(1, 8):
    psi[i, i] = c; psi[i+8, i+8] = c; psi[i, i+8] = -s; psi[i+8, i] = s
eps = np.diag([1]*8 + [-1]*8).astype(float)
aut = lambda A: max(np.abs(A @ mul(x, y) - mul(A @ x, A @ y)).max() for x, y in ((rng.normal(size=N), rng.normal(size=N)) for _ in range(20)))
print("[Kontrolle] psi, eps Automorphismen:", f"{aut(psi):.1e}", f"{aut(eps):.1e}")
print("[Kontrolle] psi bildet Kopie k auf k+1 ab:", [f"{np.abs(P[(k+1)%3] @ psi @ P[k] - psi @ P[k]).max():.1e}" for k in range(3)])
print("[Kontrolle] psi u_k = u_{k+1}:", [f"{np.abs(psi @ U[k] - U[(k+1)%3]).max():.1e}" for k in range(3)])

print("\n=== H140a: Farbe ===")
GV = np.array([g.ravel() for g in G2])
def stab(u):
    M = np.array([(g @ u) for g in G2]).T
    _, sv, vt = np.linalg.svd(M); null = vt[np.sum(sv > 1e-9):]
    return null @ GV   # Basis (Zeilen) des Stabilisators als 256-Vektoren
S = [stab(u) for u in U]
print("dim su(3)_k:", [len(x) for x in S])
def same(A, Bm):
    Qa, _ = np.linalg.qr(A.T); Qb, _ = np.linalg.qr(Bm.T)
    return np.linalg.svd(Qa.T @ Qb, compute_uv=False).min()
print("Hauptwinkel-cos min (1 = gleich): su3_0~su3_120", f"{same(S[0], S[1]):.12f}", " su3_0~su3_240", f"{same(S[0], S[2]):.12f}")
com = max(max(np.abs(g.reshape(N, N) @ A - A @ g.reshape(N, N)).max() for g in S[0]) for A in (psi, eps))
print(f"max |[su3, psi]|, |[su3, eps]|: {com:.1e}")
# Casimir auf jeder Kopie
Sg = [g.reshape(N, N) for g in S[0]]
K = np.array([[np.trace(a @ b) for b in Sg] for a in Sg]); Kinv = np.linalg.inv(K)
Cas = -sum(Kinv[i, j] * Sg[i] @ Sg[j] for i in range(8) for j in range(8))
for k in range(3):
    ev = np.round(np.linalg.eigvalsh(B[k] @ Cas @ B[k].T), 8)
    vals, cnt = np.unique(ev, return_counts=True)
    print(f"  Kopie {k}: Casimir-Eigenwerte {dict(zip(vals, cnt))}; Leck der Farbe aus C_k: {max(np.abs((np.eye(N)-P[k]) @ g @ P[k]).max() for g in Sg):.1e}")

print("\n=== H140b: Ladung je Kopie ===")
Q = [0.5*np.eye(N) - 1j/6*Lm(u) - 1j/3*Rm(u) for u in U]
for k in range(3):
    leak = np.abs((np.eye(N) - P[k]) @ Q[k] @ P[k]).max()
    ev = np.sort(np.linalg.eigvals(B[k] @ Q[k] @ B[k].T).real)
    print(f"  Q_{k} auf C_{k}: Leck {leak:.1e}, Spektrum {np.round(ev, 10)}")
    # Ladung vertauscht mit Farbe auf C_k?
    print(f"     [Q_{k}, su3] auf C_{k}: {max(np.abs(B[k] @ (Q[k] @ g - g @ Q[k]) @ B[k].T).max() for g in Sg):.1e}")
print("  psi Q_k psi^-1 = Q_{k+1}:", [f"{np.abs(psi @ Q[k] @ psi.T - Q[(k+1)%3]).max():.1e}" for k in range(3)])
print(f"  |psi Q_0 psi^-1 - Q_0| = {np.abs(psi @ Q[0] @ psi.T - Q[0]).max():.3f};  |[Q_0, Q_1]| = {np.abs(Q[0] @ Q[1] - Q[1] @ Q[0]).max():.3f}")
print("  Q_0 bildet C_120 in sich ab? Leck", f"{np.abs((np.eye(N)-P[1]) @ Q[0] @ P[1]).max():.3f}")

print("\n=== H140c: gemeinsame Ladung a + b L_x + c R_x ===")
Lb = [Lm(E[i]) for i in range(N)]; Rb = [Rm(E[i]) for i in range(N)]
def leak(p):
    x = p[:15]; x = np.concatenate([[0], x]) / np.linalg.norm(x)
    bc = p[15:17] + 1j*p[17:19]; bc /= np.linalg.norm(bc)
    M = bc[0] * np.einsum('i,ijk->jk', x, np.array(Lb)) + bc[1] * np.einsum('i,ijk->jk', x, np.array(Rb))
    return sum(np.linalg.norm((np.eye(N) - P[k]) @ M @ P[k])**2 for k in range(3))
best = min((minimize(leak, rng.normal(size=19), method='BFGS') for _ in range(500)), key=lambda r: r.fun)
print(f"  min Leck^2 ueber 500 Starts: {best.fun:.4e}  (Kriterium: > 1e-3 heisst keine gemeinsame Ladung)")
x = np.concatenate([[0], best.x[:15]]); x /= np.linalg.norm(x)
print("  bestes x (gerundet):", np.round(x, 3))

print("\n=== H140d: Dimension ===")
print("  dim(C_0 + C_120 + C_240) =", np.linalg.matrix_rank(np.vstack(B), tol=1e-9), "(3 Generationen braeuchten 24)")
