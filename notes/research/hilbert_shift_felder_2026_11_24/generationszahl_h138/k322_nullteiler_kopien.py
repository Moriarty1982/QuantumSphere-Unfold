"""k322 (Test H139): Nullteiler und Kopienprofil. HS(4): Profil der Nullteiler; HS(5): Nullteiler in den 15 abgeschlossenen O_v.
Vorab-Notiz: Vorab_Notiz_H139_Nullteiler_jenseits_drei_Kopien.md. Konvention wie k253."""
import itertools, numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm
rng = np.random.default_rng(322)

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
def table(N):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N): C[i, j] = mul(E[i], E[j])
    return C
def derivations(C):
    N = C.shape[0]; M = []
    for idx in range(N*N):
        D = np.zeros(N*N); D[idx] = 1; D = D.reshape(N, N); cols = []
        for i in range(N):
            for j in range(N):
                cols.append(D @ C[i, j] - np.einsum('p,pk->k', D[:, i], C[:, j]) - np.einsum('p,pk->k', D[:, j], C[i, :]))
        M.append(np.concatenate(cols))
    u, s, vt = np.linalg.svd(np.array(M).T)
    return [v.reshape(N, N) for v in vt[np.sum(s > 1e-9):]]

C16 = table(16); C32 = table(32)
L = lambda C, x: np.einsum('i,ijk->kj', x, C)   # L_x als Matrix: (L_x y)_k
smin = lambda M: np.linalg.svd(M, compute_uv=False)[-1]
G2 = derivations(table(8))

def profile(x, m):  # M(x) 7 x m und Singulett-Anteil
    M = np.array([x[8*k+1:8*k+8] for k in range(m)]).T
    sing = np.array([x[8*k] for k in range(m)])
    return M, sing

print("=== Kontrolle ===")
E = np.eye(16)
print("(e1+e10)(e4-e15) =", np.abs(mul(E[1]+E[10], E[4]-E[15])).max())

print("\n=== H139b: Nullteiler von S und ihr Kopienprofil ===")
diag = []
for i, j in itertools.combinations(range(1, 16), 2):
    for s in (1, -1):
        x = (E[i] + s*E[j]) / np.sqrt(2)
        if smin(L(C16, x)) < 1e-10: diag.append(x)
print(f"Basis-Diagonalen e_i +- e_j, die Nullteiler sind: {len(diag)} (Paare i<j: {len(diag)//2 if all(True for _ in diag) else ''})")
dev = 0.0; sing_max = 0.0
for x in diag:
    M, sg = profile(x, 2); dev = max(dev, np.abs(M.T @ M - 0.5*np.eye(2)).max()); sing_max = max(sing_max, np.abs(sg).max())
print(f"  max |M^T M - 1/2|: {dev:.1e}, max Singulett-Anteil (1, e8): {sing_max:.1e}")
# 500 Nullteiler aus Kernen von L_x zufaelliger G2-Bilder von (e1+e10)/sqrt2 und von Kernvektoren
Gb = [np.kron(np.eye(2), D) for D in G2]
dev = 0.0; sing_max = 0.0; cnt = 0
x0 = (E[1] + E[10]) / np.sqrt(2)
for _ in range(250):
    g = expm(sum(rng.normal() * D for D in Gb))
    x = g @ x0
    # Kern von L_x: weitere Nullteiler
    u, s, vt = np.linalg.svd(L(C16, x)); ker = vt[s < 1e-9]
    y = rng.normal(size=len(ker)) @ ker; y /= np.linalg.norm(y)
    for z in (x, y):
        assert smin(L(C16, z)) < 1e-9
        M, sg = profile(z, 2); dev = max(dev, np.abs(M.T @ M - 0.5*np.eye(2)).max()); sing_max = max(sing_max, np.abs(sg).max()); cnt += 1
print(f"  {cnt} Nullteiler aus G2-Bahn und Kernen: max |M^T M - 1/2| = {dev:.1e}, max Singulett-Anteil = {sing_max:.1e}")
# Gewicht auf den drei Kopien
dirs = [np.array([np.cos(t), np.sin(t)]) for t in (0, np.pi/3, 2*np.pi/3)]
w = [np.linalg.norm(profile(x0, 2)[0] @ v)**2 for v in dirs]
print("  Gewicht von (e1+e10)/sqrt2 auf den Kopien 0, 60, 120 Grad:", np.round(w, 12))

print("\n=== H139c: Umkehrung ===")
flat_bad = 0; non_bad = 0; fmax = 0.0; nmin = 1e9
for _ in range(500):
    a = rng.normal(size=7); b = rng.normal(size=7); b -= (a @ b) / (a @ a) * a; b *= np.linalg.norm(a) / np.linalg.norm(b)
    x = np.zeros(16); x[1:8] = a; x[9:16] = b; x /= np.linalg.norm(x)
    s = smin(L(C16, x)); fmax = max(fmax, s)
    x2 = np.zeros(16); x2[1:8] = rng.normal(size=7); x2[9:16] = rng.normal(size=7); x2[[0, 8]] = rng.normal(size=2) * rng.integers(0, 2)
    x2 /= np.linalg.norm(x2); M, _ = profile(x2, 2)
    s2 = smin(L(C16, x2)); nmin = min(nmin, s2)
print(f"  flaches Profil: max kleinster Singulaerwert {fmax:.1e} (Kriterium < 1e-10)")
print(f"  generisches (nicht flaches) Profil: min kleinster Singulaerwert {nmin:.3e} (Kriterium > 1e-6)")
# Profil-Abstand und Singulaerwert: Zusammenhang
print("  Stichprobe: Flachheit d = |M^T M - 1/2|, smin(L_x):")
for t in (0.0, 0.01, 0.1, 0.3, 0.5):
    a = np.zeros(7); a[0] = 1; b = np.zeros(7); b[1] = 1; b2 = np.zeros(7); b2[2] = 1
    x = np.zeros(16); x[1:8] = a*np.sqrt(0.5 + t); x[9:16] = (b*np.cos(0.0) )*np.sqrt(0.5 - t); x /= np.linalg.norm(x)
    M, _ = profile(x, 2)
    print(f"    t = {t:4.2f}: d = {np.abs(M.T @ M - 0.5*np.eye(2)).max():.3f}, smin = {smin(L(C16, x)):.4f}")

print("\n=== H139a: HS(5), Nullteiler in den 15 abgeschlossenen O_v ===")
r3 = np.sqrt(3); r2 = np.sqrt(2)
V = [[-1,0,0,0],[-.5,0,-r3/2,0],[-.5,0,r3/2,0],[-.5,-r3/2,0,0],[-.5,r3/2,0,0],
     [-.25,-r3/4,-r3/4,-.75],[-.25,-r3/4,r3/4,.75],[-.25,r3/4,-r3/4,.75],[-.25,r3/4,r3/4,-.75],
     [-1/r2,0,0,-1/r2],[-1/r2,0,0,1/r2],[-1/(2*r2),-np.sqrt(1.5)/2,-np.sqrt(1.5)/2,1/(2*r2)],
     [-1/(2*r2),-np.sqrt(1.5)/2,np.sqrt(1.5)/2,-1/(2*r2)],[-1/(2*r2),np.sqrt(1.5)/2,-np.sqrt(1.5)/2,-1/(2*r2)],
     [-1/(2*r2),np.sqrt(1.5)/2,np.sqrt(1.5)/2,1/(2*r2)]]   # aus k321b (Wolfram exakt)
E32 = np.eye(32)
def basis(v):
    B = [E32[0]]
    for i in range(7):
        x = np.zeros(32)
        for k in range(4): x[8*k+1+i] = v[k]
        B.append(x)
    return np.array(B)
for idx, v in enumerate(V):
    v = np.array(v); B = basis(v)
    def inner_smin(c):
        x = c @ B; x /= np.linalg.norm(x)
        return smin(B @ L(C32, x) @ B.T)   # L_x eingeschraenkt auf O_v (O_v abgeschlossen)
    def glob_smin(c):
        x = c @ B; x /= np.linalg.norm(x)
        return smin(L(C32, x))
    best_in = min(minimize(inner_smin, rng.normal(size=8), method='Nelder-Mead', options={'maxiter': 6000, 'xatol': 1e-13, 'fatol': 1e-15}).fun for _ in range(20))
    rand_glob = min(glob_smin(rng.normal(size=8)) for _ in range(1000))
    best_glob = min(rand_glob, min(minimize(glob_smin, rng.normal(size=8), method='Nelder-Mead', options={'maxiter': 6000, 'xatol': 1e-13, 'fatol': 1e-15}).fun for _ in range(20)))
    alt = max(np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max() for x, y in ((rng.normal(size=8) @ B, rng.normal(size=8) @ B) for _ in range(30)))
    typ = "oktonionisch" if alt < 1e-9 else "nicht alternativ"
    print(f"  O_v {idx+1:2d} ({typ:16s}): innerer Nullteiler min smin = {best_in:.2e}, Nullteiler von A5 min smin = {best_glob:.2e}")
