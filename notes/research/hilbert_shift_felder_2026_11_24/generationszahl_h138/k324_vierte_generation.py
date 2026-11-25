"""k324 (Test H141): vierte 'Generation' aus dem Kern der Summenabbildung Phi: C_0 + C_120 + C_240 -> C(x)S.
Vorab: Vorab_Notiz_H141_Vierte_Generation_Rest.md. Baut auf k323 (gleiche Konventionen)."""
import numpy as np
rng = np.random.default_rng(324)
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
prod = lambda x, y: np.einsum('i,j,ijk->k', x, y, C)   # komplex-bilinear
def derivations(Ct):
    n = Ct.shape[0]; M = []
    for idx in range(n*n):
        D = np.zeros(n*n); D[idx] = 1; D = D.reshape(n, n); cols = []
        for i in range(n):
            for j in range(n):
                cols.append(D @ Ct[i, j] - np.einsum('p,pk->k', D[:, i], Ct[:, j]) - np.einsum('p,pk->k', D[:, j], Ct[i, :]))
        M.append(np.concatenate(cols))
    u, s, vt = np.linalg.svd(np.array(M).T)
    return [v.reshape(n, n) for v in vt[np.sum(s > 1e-9):]]
C8 = np.array([[mul(np.eye(8)[i], np.eye(8)[j]) for j in range(8)] for i in range(8)])
G2 = [np.kron(np.eye(2), D) for D in derivations(C8)]
def emb(a, f):
    x = np.zeros(N); x[1:8] = f[0]*a; x[9:16] = f[1]*a; return x
F = [np.array([np.cos(t), np.sin(t)]) for t in (0, 2*np.pi/3, 4*np.pi/3)]
e7 = np.zeros(7); e7[6] = 1; U = [emb(e7, f) for f in F]
B = [np.array([E[0]] + [emb(np.eye(7)[i], f) for i in range(7)]) for f in F]
Q = [0.5*np.eye(N) - 1j/6*Lm(u) - 1j/3*Rm(u) for u in U]
c, s = np.cos(2*np.pi/3), np.sin(2*np.pi/3); psi = np.eye(N)
for i in range(1, 8):
    psi[i, i] = c; psi[i+8, i+8] = c; psi[i, i+8] = -s; psi[i+8, i] = s
# Stabilisator su(3) von e7 (gemeinsam, H140a)
GV = np.array([g.ravel() for g in G2]); M = np.array([g @ U[0] for g in G2]).T
_, sv, vt = np.linalg.svd(M); Sg = [(v @ GV).reshape(N, N) for v in vt[np.sum(sv > 1e-9):]]
blk = lambda Ms: np.block([[Ms[k] if k == l else np.zeros((8, 8)) for l in range(3)] for k in range(3)])
Phi = np.hstack([b.T for b in B])                      # 16 x 24
u_, s_, vt_ = np.linalg.svd(Phi); r = np.sum(s_ > 1e-10)
Kb = vt_[r:]                                           # Kern, Zeilen orthonormal (reell)
PK = Kb.T @ Kb
cok = u_[:, r:]
print(f"[Kontrolle] Rang Phi = {r}, dim Kern = {len(Kb)}, dim Kokern = {cok.shape[1]}")
print("Kokern-Vektor (gerundet):", np.round(cok[:, 0], 6))
print(f"Kokern e8 Nullteiler? smin(L_e8) = {np.linalg.svd(Lm(E[8]), compute_uv=False)[-1]:.3f}")

print("\n=== H141a: Farbe und S3 auf dem Kern ===")
SV = [blk([b @ g @ b.T for b in B]) for g in Sg]
leak_c = max(np.abs((np.eye(24) - PK) @ g @ PK).max() for g in SV)
Kmat = np.array([[np.trace(a @ b) for b in SV] for a in SV]); Ki = np.linalg.inv(Kmat)
Cas = -sum(Ki[i, j] * SV[i] @ SV[j] for i in range(8) for j in range(8))
ev = np.round(np.linalg.eigvalsh(Kb @ Cas @ Kb.T), 8); vals, cnt = np.unique(ev, return_counts=True)
# Normierung: Casimir je Kopie wie k323 (-2/3 fuer 3, 3bar)
print(f"su(3)-Leck aus K: {leak_c:.1e}; Casimir auf K: {dict(zip(vals, cnt))}")
PsiV = np.zeros((24, 24))
for k in range(3):
    l = (k + 1) % 3; PsiV[8*l:8*l+8, 8*k:8*k+8] = B[l] @ psi @ B[k].T
print(f"psi_V orthogonal: {np.abs(PsiV @ PsiV.T - np.eye(24)).max():.1e}; Phi psi_V = psi Phi: {np.abs(Phi @ PsiV - psi @ Phi).max():.1e}; psi-Leck aus K: {np.abs((np.eye(24)-PK) @ PsiV @ PK).max():.1e}")
pk = Kb @ PsiV @ Kb.T
print("  Spur von psi auf K:", round(np.trace(pk), 6), "(9 Dim.; Spur 0 bei 3 x Standard, 9 bei trivial)")
# Zerlegung: Singulett-Teil (Casimir 0) und Farbteil
w, V_ = np.linalg.eigh(Kb @ Cas @ Kb.T); sing = V_[:, np.abs(w) < 1e-8]; col = V_[:, np.abs(w) > 1e-8]
print("  Spur psi auf Singuletts:", round(np.trace(sing.T @ pk @ sing), 6), " auf Farbteil:", round(np.trace(col.T @ pk @ col), 6))

print("\n=== H141b: Ladung und Produkt auf dem Kern ===")
QV = blk([b @ q @ b.T for b, q in zip(B, Q)])
leak_q = np.linalg.norm((np.eye(24) - PK) @ QV @ PK, 2)
print(f"Ladungs-Leck ||(1-P_K) Q_V P_K|| = {leak_q:.4f}")
def vprod(x, y):   # komponentenweises Produkt in V (Koordinaten je Kopie)
    out = []
    for k in range(3):
        xk, yk = B[k].T @ x[8*k:8*k+8], B[k].T @ y[8*k:8*k+8]
        out.append(B[k] @ prod(xk, yk))
    return np.concatenate(out)
lp = max(np.linalg.norm((np.eye(24) - PK) @ vprod(Kb.T @ rng.normal(size=9), Kb.T @ rng.normal(size=9))) for _ in range(200))
print(f"Produkt-Leck (max ueber 200 Paare, normierte Faktoren ~ |K-Koeff| ~ 3): {lp:.4f}")
# welche Kern-Richtungen bleiben unter Q im Kern?
Qk = Kb @ QV @ Kb.T
inv = np.linalg.svd((np.eye(24) - PK) @ QV @ Kb.T, compute_uv=False)
print("  Singulaerwerte des Lecks je Kernrichtung:", np.round(np.sort(inv), 6))

print("\n=== H141c: Nullteiler ===")
mins = 1e9
for _ in range(500):
    x = Kb.T @ (rng.normal(size=9))
    for k in range(3):
        xk = B[k].T @ x[8*k:8*k+8]
        if np.linalg.norm(xk) > 1e-9:
            mins = min(mins, np.linalg.svd(Lm(xk / np.linalg.norm(xk)), compute_uv=False)[-1])
print(f"min smin(L_x_k) ueber Komponenten von 500 Kernelementen: {mins:.4f}")

print("\n=== H141d: gemeinsame Ladung ueber K-Komplement ===")
Pp = np.eye(24) - PK
print(f"[Q_V, P_K] = {np.abs(QV @ PK - PK @ QV).max():.4f}  (0 hiesse: Phi Q_V Phi^+ gemeinsame Ladung)")

print("\n=== Erkundung: gestauchte Ladung auf K ===")
evq = np.linalg.eigvals(Qk)
print("Spektrum P_K Q_V P_K:", np.round(np.sort_complex(evq), 6))
print("  auf Singuletts:", np.round(np.sort_complex(np.linalg.eigvals(sing.T @ Qk @ sing)), 6))
print("  auf Farbteil:  ", np.round(np.sort_complex(np.linalg.eigvals(col.T @ Qk @ col)), 6))
