"""k325 (Test H142): vier Oktonion-Kopien auf HS(5) als getrennte Traeger; alle 126 Viererauswahlen der 9 Kopien aus k321b.
Vorab: Vorab_Notiz_H142_Vier_Kopien_HS5.md. Konventionen wie k323/k324."""
import itertools, numpy as np
from scipy.optimize import minimize_scalar
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
N = 32; E = np.eye(N)
C = np.array([[mul(E[i], E[j]) for j in range(N)] for i in range(N)])
Lb = [C[i].T for i in range(N)]            # L_{e_i}: (L y)_k = sum_j C[i,j,k] y_j
Rb = [C[:, i, :].T for i in range(N)]
Lm = lambda x: np.einsum('i,ikj->kj', x, np.array(Lb)); Rm = lambda x: np.einsum('i,ikj->kj', x, np.array(Rb))
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
G2 = [np.kron(np.eye(4), D) for D in derivations(C8)]
r3 = np.sqrt(3)
# Orientierung durch Automorphismen transportiert (Nachtrag Vorab-Notiz): v = a (x) b, a, b aus f_0, f_120, f_240.
# Dieselben 9 Kopien wie k321b (bis auf Vorzeichen); Vorlauf mit den Wolfram-Vorzeichen: k325_vorlauf_out.txt.
F = [np.array([np.cos(t), np.sin(t)]) for t in (0, 2*np.pi/3, 4*np.pi/3)]
VS = np.array([np.kron(a, b) for a in F for b in F])
SED = [0, 1, 2]    # a = f_0: die drei Sedenion-Kopien (t3 = t4 = 0), wie H141
SIGNS = np.ones(9)
def emb(a, v):
    x = np.zeros(N)
    for k in range(4): x[8*k+1:8*k+8] = v[k]*a
    return x
e7 = np.zeros(7); e7[6] = 1
B = [np.array([E[0]] + [emb(np.eye(7)[i], v) for i in range(7)]) for v in VS]
P = [b.T @ b for b in B]
Qof = lambda v: 0.5*np.eye(N) - 1j/6*Lm(emb(e7, v)) - 1j/3*Rm(emb(e7, v))
Q = [Qof(v) for v in VS]
# Farbe
GV = np.array([g.ravel() for g in G2])
def stab(u):
    M = np.array([g @ u for g in G2]).T; _, sv, vt = np.linalg.svd(M); return vt[np.sum(sv > 1e-9):] @ GV
S0 = stab(emb(e7, VS[0])); Sg = [g.reshape(N, N) for g in S0]
def same(A, Bm):
    Qa, _ = np.linalg.qr(A.T); Qb, _ = np.linalg.qr(Bm.T); return np.linalg.svd(Qa.T @ Qb, compute_uv=False).min()
print("=== H142a ===")
print("su(3) gleich fuer alle 9 (min cos):", f"{min(same(S0, stab(emb(e7, v))) for v in VS):.12f}")
for k in range(9):
    leak = np.abs((np.eye(N) - P[k]) @ Q[k] @ P[k]).max()
    ev = np.sort(np.linalg.eigvals(B[k] @ Q[k] @ B[k].T).real)
    ok = np.allclose(ev, [0, 1/3, 1/3, 1/3, 2/3, 2/3, 2/3, 1], atol=1e-10)
    print(f"  Kopie {k}: v = {np.round(VS[k], 4)}, Leck {leak:.1e}, Generationsspektrum: {ok}")
# Leck-Gram fuer gemeinsame Ladung
def gram(idx, Ops):
    T = [sum(((np.eye(N) - P[k]) @ O @ P[k]).ravel() for k in []) if False else np.concatenate([((np.eye(N) - P[k]) @ O @ P[k]).ravel() for k in idx]) for O in Ops]
    T = np.array(T); return T @ T.T
def common_charge(idx):
    A = gram(idx, Lb[1:]); Bq = gram(idx, Rb[1:])
    TL = np.array([np.concatenate([((np.eye(N) - P[k]) @ O @ P[k]).ravel() for k in idx]) for O in Lb[1:]])
    TR = np.array([np.concatenate([((np.eye(N) - P[k]) @ O @ P[k]).ravel() for k in idx]) for O in Rb[1:]])
    Cr = (TL @ TR.T + TR @ TL.T) / 2
    f = lambda ph: np.linalg.eigvalsh(np.cos(ph)**2*A + np.sin(ph)**2*Bq + 2*np.sin(ph)*np.cos(ph)*Cr)[0]
    grid = np.linspace(0, np.pi, 721); vals = [f(p) for p in grid]; p0 = grid[int(np.argmin(vals))]
    r = minimize_scalar(f, bounds=(p0 - 0.01, p0 + 0.01), method='bounded', options={'xatol': 1e-12})
    return min(r.fun, min(vals))
# Casimir auf V
def run(idx, sg=None):
    m = len(idx)
    Qs = [Q[k] if sg is None or sg[j] > 0 else Qof(-VS[k]) for j, k in enumerate(idx)]
    Phi = np.hstack([B[k].T for k in idx])
    u_, s_, vt_ = np.linalg.svd(Phi); r = int(np.sum(s_ > 1e-10)); Kb = vt_[r:]; PK = Kb.T @ Kb
    blk = lambda Ms: np.block([[Ms[a] if a == b else np.zeros((8, 8)) for b in range(m)] for a in range(m)])
    QV = blk([B[k] @ q @ B[k].T for k, q in zip(idx, Qs)])
    SV = [blk([B[k] @ g @ B[k].T for k in idx]) for g in Sg]
    Km = np.array([[np.trace(a @ b) for b in SV] for a in SV]); Ki = np.linalg.inv(Km)
    Cas = -sum(Ki[i, j] * SV[i] @ SV[j] for i in range(8) for j in range(8))
    res = dict(rank_v=np.linalg.matrix_rank(VS[list(idx)]), dimK=len(Kb), cok=N - r)
    if len(Kb):
        cw = np.round(np.linalg.eigvalsh(Kb @ Cas @ Kb.T), 6); res['cas'] = tuple(np.unique(np.abs(cw) > 1e-6, return_counts=True)[1])
        ev = np.sort(np.linalg.eigvals(Kb @ QV @ Kb.T).real); res['spec'] = tuple(np.round(ev, 6))
        res['leak'] = round(float(np.linalg.norm((np.eye(8*m) - PK) @ QV @ PK, 2)), 6)
        res['lepton'] = bool(np.any(np.abs(ev) < 1e-6) or np.any(np.abs(ev - 1) < 1e-6))
    return res
print("\n=== Kontrolle: drei Sedenion-Kopien in A5 ===")
print(run(SED))
print("\n=== H142b-d: alle 126 Viererauswahlen ===")
classes = {}
for idx in itertools.combinations(range(9), 4):
    r = run(idx); key = (r['rank_v'], r['dimK'], r.get('cas'), r.get('spec'), r.get('leak'), r.get('lepton'))
    classes.setdefault(key, []).append(idx)
for key, lst in classes.items():
    cc = common_charge(lst[0])
    print(f"Rang v {key[0]}, dim K {key[1]}, Casimir (Singulett, Farbe) {key[2]}, Spektrum K {key[3]}, Ladungs-Leck {key[4]}, Leptonen 0/1 im Kern: {key[5]}")
    print(f"   {len(lst)} Auswahlen, davon mit allen drei Sedenion-Kopien: {sum(set(SED) <= set(l) for l in lst)}; min Leck^2 gemeinsame Ladung (Beispiel {lst[0]}): {cc:.4f}")

print("\n=== Zusatz: freie Vorzeichen (alle 2^3 relativen Orientierungen je Auswahl, nicht gewertet) ===")
cnt = {}; lep = []
for idx in itertools.combinations(range(9), 4):
    for sg in itertools.product([1, -1], repeat=3):
        r = run(idx, (1,) + sg)
        if r.get('lepton'): lep.append((idx, (1,) + sg, r['spec']))
print(f"Auswahl-Orientierungs-Paare mit 0 und 1 im Kern: {len(lep)} von {126*8}")
for l in lep[:6]: print("  ", l[0], l[1], l[2])
q3 = sum(1 for idx in itertools.combinations(range(9), 3) for sg in itertools.product([1, -1], repeat=2) if run(idx, (1,) + sg).get('lepton'))
print(f"Zum Vergleich drei Kopien (84 Auswahlen x 4 Orientierungen): mit 0 und 1 im Kern: {q3}")
print("Drei Sedenion-Kopien, alle Orientierungen:")
for sg in itertools.product([1, -1], repeat=2):
    print("  ", (1,) + sg, run(SED, (1,) + sg).get('spec'))
