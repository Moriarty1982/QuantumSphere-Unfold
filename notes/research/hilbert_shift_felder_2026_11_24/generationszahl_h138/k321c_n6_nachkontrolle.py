"""k321c (nachtraeglich, Erkundung): HS(6) aus k321_out_n6.txt: groesste orthogonale Menge, Typ ihrer Mitglieder,
Nullteiler-Eigenschaft (smin L_x auf A6) fuer oktonionische und nicht alternative Kopien. Aufruf aus diesem Ordner."""
import re, itertools, numpy as np
rng = np.random.default_rng(3213)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
txt = open('k321_out_n6.txt').read()
vs, alts = [], []
for m in re.finditer(r"v = \[([^\]]*)\].*?Alternator ([0-9.e+-]+)", txt, re.S):
    vs.append(np.array([float(x) for x in m.group(1).replace('\n', ' ').split(',')])); alts.append(float(m.group(2)))
vs = np.array(vs); vs /= np.linalg.norm(vs, axis=1)[:, None]; okt = np.array(alts) < 1e-9
G = np.abs(vs @ vs.T); n = len(vs)
adj = {a: {b for b in range(n) if b != a and G[a, b] < 1e-4} for a in range(n)}
best = []
def bk(R, P, X):
    global best
    if not P and not X:
        if len(R) > len(best): best = sorted(R)
        return
    for u in list(P):
        bk(R | {u}, P & adj[u], X & adj[u]); P = P - {u}; X = X | {u}
bk(set(), set(range(n)), set())
print(f"Kopien gelesen: {n}, oktonionisch {okt.sum()}; groesste orthogonale Menge {len(best)}, davon oktonionisch {okt[best].sum()}")
E = np.eye(64); C = np.zeros((64, 64, 64))
for i in range(64):
    for j in range(64): C[i, j] = mul(E[i], E[j])
def smin_im(v):
    a = rng.normal(size=7); x = np.zeros(64)
    for k in range(8): x[8*k+1:8*k+8] = v[k]*a
    x /= np.linalg.norm(x)
    return np.linalg.svd(np.einsum('i,ijk->kj', x, C), compute_uv=False)[-1]
so = [smin_im(v) for v in vs[okt]]; sn = [smin_im(v) for v in vs[~okt]]
print(f"oktonionisch: min smin(L_x) imaginaeres Element = {min(so):.3e}")
print(f"nicht alternativ: max smin = {max(sn):.1e}, Anteil Nullteiler (< 1e-10): {np.mean(np.array(sn) < 1e-10):.3f}")
print("Mitglieder der orthogonalen Menge, smin:", [f"{smin_im(vs[k]):.1e}" for k in best])
