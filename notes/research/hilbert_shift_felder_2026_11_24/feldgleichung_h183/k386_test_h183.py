"""k386 (Test H183): Sind die Sektoren (Leptonen, Down, Up) zugleich stabile statische Loesungen einer Feldgleichung auf C (x) O?
Vorab: Vorab_Notiz_H183_Sektoren_als_Vakua_einer_Feldgleichung.md (Commit a009664). Braucht cvxpy.
Aufruf: python k386_test_h183.py > k386_out.txt"""
import itertools, numpy as np, cvxpy as cp
from scipy.linalg import null_space, expm, block_diag, orth
rng = np.random.default_rng(386)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
n = 8; e = np.eye(n); C = np.array([[mul(e[i], e[j]) for j in range(n)] for i in range(n)])
rows = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            r = np.zeros((n, n)); r[k, :] += C[i, j, :]; r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]; rows.append(r.ravel())
fx = np.zeros((n, n * n))
for k in range(n): fx[k, k * n + 7] = 1
st = null_space(np.vstack([np.array(rows), fx]), rcond=1e-9)
gens8 = [st[:, a].reshape(n, n) for a in range(st.shape[1])]
U = e[7]; J8 = np.array([mul(U, conj(e[i])) for i in range(n)]).T; K8 = np.diag([1.0] + [-1.0] * 7)
L8 = np.einsum('i,ijk->kj', U, C); R8 = np.einsum('j,ijk->ki', U, C)
Q0 = 0.5 * np.eye(n) - 1j / 6 * L8 - 1j / 3 * R8
cl = lambda M: block_diag(M, M)
gens = [cl(g) for g in gens8]; J = cl(J8); K = cl(K8); N = 16
I16 = np.block([[np.zeros((8, 8)), -np.eye(8)], [np.eye(8), np.zeros((8, 8))]])
real16 = lambda z: np.concatenate([z.real, z.imag])
col = [1, 2, 3, 4, 5, 6]

# --- Invarianten Grad 2 und 4 (wie k385) ---
idx = [(i, j) for i in range(N) for j in range(i, N)]; basis = []
for (i, j) in idx:
    B = np.zeros((N, N)); B[i, j] = B[j, i] = 1; basis.append(B)
cons = [np.array([(g.T @ B + B @ g).ravel() for B in basis]).T for g in gens] + [np.array([(M.T @ B @ M - B).ravel() for B in basis]).T for M in (K, J)]
ns = null_space(np.vstack(cons), rcond=1e-9)
Q2 = [sum(ns[k, a] * basis[k] for k in range(len(basis))) for a in range(ns.shape[1])]
mons = list(itertools.combinations_with_replacement(range(N), 4)); MI = np.array(mons)
ev = lambda X: np.prod(X[:, MI], axis=2)
m = 5200; X = rng.normal(size=(m, N)); els = []
for _ in range(m):
    g = expm(sum(rng.normal() * G for G in gens)); r = rng.integers(0, 4)
    els.append([g, K @ g, J @ g, J @ K @ g][r])
Amat = ev(np.einsum('mij,mj->mi', np.array(els), X)) - ev(X)
_, s_, vt = np.linalg.svd(Amat, full_matrices=True); inv4 = vt[np.sum(s_ > 1e-8 * s_[0]):]
print(f"Invarianten: Grad 2: {len(Q2)}, Grad 4: {inv4.shape[0]}")
# symmetrische 4-Tensoren
def tensor(cf):
    T = np.zeros((N,) * 4)
    for c, mon in zip(cf, mons):
        if abs(c) < 1e-14: continue
        perms = set(itertools.permutations(mon))
        for p in perms: T[p] += c / len(perms)
    return T
T4 = [tensor(cf) for cf in inv4]
nI = len(Q2) + len(T4)
def val(k, x): return x @ Q2[k] @ x if k < len(Q2) else np.einsum('ijkl,i,j,k,l', T4[k - len(Q2)], x, x, x, x)
def grad(k, x): return 2 * Q2[k] @ x if k < len(Q2) else 4 * np.einsum('ijkl,j,k,l', T4[k - len(Q2)], x, x, x)
def hess(k, x): return 2 * Q2[k] if k < len(Q2) else 12 * np.einsum('ijkl,k,l', T4[k - len(Q2)], x, x)
xt = rng.normal(size=N); print(f"Probe Tensoren: |T[x,x,x,x] - P(x)| = {max(abs(val(len(Q2) + a, xt) - ev(xt[None, :])[0] @ inv4[a]) for a in range(len(T4))):.1e}")

# --- Konfigurationen ---
w, V = np.linalg.eig(Q0[np.ix_(col, col)])
def nvec(q):
    v = V[:, np.argmin(np.abs(w - q))]; v = v / np.linalg.norm(v); z = np.zeros(8, dtype=complex); z[col] = v; return z
thd, thu = np.radians(48.114), np.radians(52.207)
vac = {"L": real16(((e[0] + e[7]) / np.sqrt(2)).astype(complex)),
       "D": real16(np.cos(thd) * e[0].astype(complex) + np.sin(thd) * nvec(1 / 3)),
       "U": real16(np.cos(thu) * e[0].astype(complex) + np.sin(thu) * nvec(2 / 3))}


sym2 = lambda M: (M + M.T) / 2
def build(vacs, phase=False, free=False):
    """Koeffizientenraum, Stationaritaet an allen Punkten, reduzierte zweite Variationen.
    free = False: feste Norm (Kugel). free = True: freie Norm (alle 16 Richtungen, voller Gradient)."""
    if phase:
        Xs = rng.normal(size=(400, N)); Lie = np.array([[grad(k, x) @ (I16 @ x) for k in range(nI)] for x in Xs]); S = null_space(Lie, rcond=1e-9)
    else: S = np.eye(nI)
    symg = gens + ([I16] if phase else [])
    Gs, Hs, Ws, nz = [], {}, {}, {}
    for name, x in vacs.items():
        P = np.eye(N) - np.outer(x, x) / (x @ x) if not free else np.eye(N)
        Gs.append(np.array([P @ grad(k, x) for k in range(nI)]).T @ S)
        orb = P @ np.array([g @ x for g in symg]).T
        ob = orth(orb, rcond=1e-9) if np.abs(orb).max() > 1e-12 else np.zeros((N, 0))
        nz[name] = ob.shape[1]
        rows = ([x[None, :]] if not free else []) + ([ob.T] if ob.shape[1] else [])
        W = null_space(np.vstack(rows), rcond=1e-9) if rows else np.eye(N); Ws[name] = W
        lam = (lambda k: (x @ grad(k, x)) / (x @ x)) if not free else (lambda k: 0.0)
        Hk = [W.T @ (hess(k, x) - lam(k) * np.eye(N)) @ W for k in range(nI)]
        Hs[name] = [sum(S[k, a] * Hk[k] for k in range(nI)) for a in range(S.shape[1])]
    Z = null_space(np.vstack(Gs), rcond=1e-9)
    Hred = {nm: [sym2(sum(Z[a, b] * Hs[nm][a] for a in range(S.shape[1]))) for b in range(Z.shape[1])] for nm in vacs}
    return S, Z, Hred, Ws, nz
def solve(Hred, ny, obj=None, sense="max", tmin=None):
    y = cp.Variable(ny); t = cp.Variable(); consr = [cp.norm(y, 2) <= 1]
    for nm in Hred:
        d = Hred[nm][0].shape[0]; consr.append(sum(y[b] * Hred[nm][b] for b in range(ny)) - t * np.eye(d) >> 0)
    if obj is None: prob = cp.Problem(cp.Maximize(t), consr)
    else:
        consr.append(t >= tmin); prob = cp.Problem(cp.Maximize(obj @ y) if sense == "max" else cp.Minimize(obj @ y), consr)
    prob.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
    return prob.status, float(t.value), y.value, float(prob.value)
def tstar(vacs, **kw):
    S, Z, Hred, Ws, nz = build(vacs, **kw)
    if Z.shape[1] == 0: return float("nan"), 0
    return solve(Hred, Z.shape[1])[1], Z.shape[1]
TOL = 1e-5
sub = lambda *names: {k: vac[k] for k in names}

print("\n== H183a: gemeinsame Stabilitaet (feste Norm, volle Fassung, 40 Koeffizienten) ==")
print("   t* = groesster erreichbarer kleinster Eigenwert der zweiten Variation ausserhalb der Symmetrierichtungen, bei normierten Koeffizienten.")
print("   t* > 0: gemeinsam stabil moeglich; t* = 0: nur die triviale Loesung V = 0, also nicht moeglich.")
S, Z, Hred, Ws, nz = build(vac)
print(f"   Stationaritaet an L, D, Up laesst frei: {Z.shape[1]} von {S.shape[1]} Koeffizienten (H183c)")
print("   Symmetrierichtungen: " + ", ".join(f"{nm}: {nz[nm]}" for nm in vac) + "; gepruefte Richtungen: " + ", ".join(f"{nm}: {Ws[nm].shape[1]}" for nm in vac))
res = {}
for names in (("L",), ("D",), ("U",), ("D", "U"), ("L", "D"), ("L", "U"), ("L", "D", "U")):
    res[names] = tstar(sub(*names)); print(f"   {' + '.join(names):10s}: t* = {res[names][0]:+.6f}  (freie Koeffizienten {res[names][1]})")
ok = res[("L", "D", "U")][0] > TOL
print("   Urteil H183a:", "BESTAETIGT" if ok else "WIDERLEGT (L, D und Up sind in keinem Potential bis Grad 4 zugleich stabil; schon L mit einem Quarkzustand geht nicht)")
tp = {names: tstar(sub(*names), phase=True)[0] for names in (("L",), ("D", "U"), ("L", "D", "U"))}
print("   Bericht Phasenfassung: " + ", ".join(f"{' + '.join(k)}: t* = {v:+.6f}" for k, v in tp.items()))
print("   H183b entfaellt in der vorab geschriebenen Form (kein gemeinsamer loesbarer Bereich).")

print("\n== Zusatz (nachtraeglich, Erkundung): Woran es liegt ==")
# duales Zertifikat fuer L + D: P_L, P_D >= 0, Spur 1, Summe tr(P H_b) = 0 fuer alle b
S, Z, Hred, Ws, nz = build(sub("L", "D")); ny = Z.shape[1]
Pv = {nm: cp.Variable((Hred[nm][0].shape[0],) * 2, PSD=True) for nm in Hred}
consd = [sum(cp.trace(Pv[nm]) for nm in Pv) == 1] + [sum(cp.trace(Pv[nm] @ Hred[nm][b]) for nm in Pv) == 0 for b in range(ny)]
pr = cp.Problem(cp.Minimize(0), consd); pr.solve(solver=cp.SCS, eps=1e-9, max_iters=200000)
print(f"   Zertifikat fuer L + D (positive Gewichte auf Richtungen, deren Kruemmungen sich fuer jedes Potential zu null summieren): Status {pr.status}")
for nm in Pv:
    wv, vv = np.linalg.eigh(Pv[nm].value); big = [(wv[-k], Ws[nm] @ vv[:, -k]) for k in range(1, len(wv) + 1) if wv[-k] > 1e-4]
    desc = []
    for wgt, u in big:
        z = u[:8] + 1j * u[8:]; parts = {"1": abs(z[0])**2, "U": abs(z[7])**2, "Farbe": float(np.sum(np.abs(z[1:7])**2))}
        desc.append(f"{wgt:.3f} auf (" + ", ".join(f"{k}: {v:.2f}" for k, v in parts.items()) + ")")
    print(f"      {nm}: " + "; ".join(desc))
print("   Reelle Unterfamilie zum Nachrechnen (X = x0^2, Y = xU^2, q = |c|^2, X + Y + q = 1): V = f(q) + delta X Y, f quadratisch.")
print("      L (q = 0, X = Y = 1/2) stabil in der Leptonebene verlangt delta < 0; D (Y = 0, q = t_d) stabil gegen einen U-Anteil verlangt delta (1 - t_d) > 0. Widerspruch.")
# Winkelabhaengigkeit, andere Form des Quarkzustands, freie Norm
Lv = vac["L"]
qv = lambda th, ch: real16(np.cos(th) * e[0].astype(complex) + np.sin(th) * nvec(ch))
q45 = lambda th, ch: real16(np.cos(th) * ((e[0] + e[7]) / np.sqrt(2)).astype(complex) + np.sin(th) * nvec(ch))
print("   Abhaengigkeit vom Winkel (L + Quarkzustand mit Ladung 1/3 bzw. 2/3; Quarkzustand allein):")
for deg in (10, 30, 45, 48.114, 52.207, 60, 80):
    th = np.radians(deg)
    print(f"      theta = {deg:7.3f}: L + Q(1/3): {tstar({'L': Lv, 'Q': qv(th, 1/3)})[0]:+.5f}; L + Q(2/3): {tstar({'L': Lv, 'Q': qv(th, 2/3)})[0]:+.5f}; Q(1/3) allein: {tstar({'Q': qv(th, 1/3)})[0]:+.5f}")
print("   Quarkzustand mit farblosem Anteil bei 45 Grad, cos(theta) (1 + U)/sqrt2 + sin(theta) n:")
print(f"      L + D': {tstar({'L': Lv, 'Q': q45(thd, 1/3)})[0]:+.5f}; D' allein: {tstar({'Q': q45(thd, 1/3)})[0]:+.5f}  (Grund: entlang q ist V dort quadratisch, g(q); L verlangt g'(0) > 0, D' verlangt g'(q_d) = 0 mit g'' > 0)")
print("   Freie Norm (Skala nicht gesetzt; Zustaende r * x, voller Gradient null):")
for rd, ru in ((1, 1), (0.5, 0.5), (0.8, 1.25), (1.25, 0.8), (2, 2)):
    print(f"      r_D = {rd}, r_U = {ru}: L + D: {tstar({'L': Lv, 'D': rd * vac['D']}, free=True)[0]:+.5f}; L + D + Up: {tstar({'L': Lv, 'D': rd * vac['D'], 'U': ru * vac['U']}, free=True)[0]:+.5f}; D + Up: {tstar({'D': rd * vac['D'], 'U': ru * vac['U']}, free=True)[0]:+.5f}")

print("\n== Zusatz (nachtraeglich, Erkundung): Was geht ==")
# D + Up gemeinsam: Vorzeichen
S, Z, Hred, Ws, nz = build(sub("D", "U")); st_, t, y, _ = solve(Hred, Z.shape[1])
lep = lambda th: real16((np.cos(th) * e[0] + np.sin(th) * e[7]).astype(complex))
ths = np.linspace(0.1, 1.4, 12); tt = np.sin(ths) ** 2; Tm = np.vstack([np.ones_like(tt), tt, tt ** 2]).T
def ab(nv):
    F = np.array([[val(k, real16(np.cos(a) * e[0].astype(complex) + np.sin(a) * nv)) for k in range(nI)] for a in ths])
    co = np.linalg.lstsq(Tm, F, rcond=None)[0]; return co[1], co[2]
aD, bD = ab(nvec(1 / 3)); aU, bU = ab(nvec(2 / 3))
print(f"   D + Up gemeinsam stabil: t* = {t:+.5f} (freie Koeffizienten {Z.shape[1]}). Vorzeichen im loesbaren Bereich (|y| <= 1, Rand t >= 0):")
for lab, f in (("A = (a_u + a_d)/2", (aU + aD) / 2), ("B = (b_u + b_d)/2", (bU + bD) / 2), ("C = (a_u - a_d)/2", (aU - aD) / 2), ("D = (b_u - b_d)/2", (bU - bD) / 2),
               ("V_L(45) - V_L(0) in der Leptonebene", np.array([val(k, lep(np.pi / 4)) - val(k, lep(0.0)) for k in range(nI)]))):
    o = (np.array(f) @ S) @ Z; hi = solve(Hred, Z.shape[1], o, "max", 0.0)[3]; lo = solve(Hred, Z.shape[1], o, "min", 0.0)[3]
    forced = ("erzwungen > 0" if lo > -1e-6 else "erzwungen < 0") if (lo > -1e-6 or hi < 1e-6) else "frei"
    print(f"      {lab:38s}: [{lo:+.4f}, {hi:+.4f}] -> {forced}")
# ein Vakuum L: Schwingungen nach Farbe und Ladung
S, Z, Hred, Ws, nz = build(sub("L")); st_, t, y, _ = solve(Hred, Z.shape[1])
Hm = sum(y[b] * Hred["L"][b] for b in range(len(y))); wv, vv = np.linalg.eigh(Hm)
print(f"   Ein Vakuum L allein: t* = {t:+.5f}. Schwingungen um L am Punkt mit groesstem t* (Frequenzquadrat, Farbanteil):")
groups = {}
for k in range(len(wv)):
    u = Ws["L"] @ vv[:, k]; z = u[:8] + 1j * u[8:]; fc = float(np.sum(np.abs(z[1:7])**2)); groups.setdefault(round(float(wv[k]), 4), []).append(fc)
print("      " + "; ".join(f"{k:.4f} x {len(v)} (Farbanteil {np.mean(v):.2f})" for k, v in sorted(groups.items())))
# allgemeine Zerlegung der zweiten Variation bei L: Zahl unabhaengiger Frequenzquadrate
rk = np.linalg.matrix_rank(np.array([H.ravel() for H in Hred["L"]]), tol=1e-9)
rnd = sum(rng.normal() * H for H in Hred["L"]); wr = np.round(np.linalg.eigvalsh(rnd), 6)
mult = sorted([int(np.sum(np.abs(wr - v) < 1e-5)) for v in sorted(set(wr))], reverse=True)
print(f"      allgemeines Potential: {rk} unabhaengige Matrizen der zweiten Variation bei L; Vielfachheiten der Frequenzquadrate bei zufaelligen Koeffizienten: {mult}")
