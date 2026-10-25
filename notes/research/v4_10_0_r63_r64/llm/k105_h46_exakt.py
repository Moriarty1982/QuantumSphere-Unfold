"""k105: Nachrechnung H46 mit exaktem beta_sym = 0.549406 (Meissner-Wert) statt 0.5493; sonst unveraendert k100."""
import itertools, numpy as np
from scipy.optimize import least_squares

w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
Wl = np.array([0., 0., -3.])
TOL = 1e-9
me_ = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003]
nu = lambda m1: np.array([m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)])
R13, R23, J12 = (0.02023, 0.02376), (0.430, 0.596), (0.2918, 0.3266)
PHI = np.deg2rad(np.arange(0, 180, 2))

def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def charged(eps_grid):
    m = np.array(me_)/max(me_); out = {e: [] for e in eps_grid}
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i]*m[p[i]] for i in range(3)])
            for e in eps_grid:
                Mf = lambda x: np.diag(np.exp(e*Wl))@(F@np.diag(x)@F.conj().T)@np.diag(np.exp(-e*Wl))
                r = least_squares(lambda x: (sv_sorted(Mf(x))[0] - m)/m, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                lam = r.x; out[e].append(sv_sorted(Mf(lam))[1])
    return {e: np.array(v) for e, v in out.items() if v}
def Qphi(p, phi):
    q, r = [i for i in range(3) if i != p]
    Q = np.zeros((3, 3)); Q[p, 0] = 1
    Q[q, 1], Q[r, 1] = np.cos(phi), np.sin(phi); Q[q, 2], Q[r, 2] = -np.sin(phi), np.cos(phi)
    return Q
def angles(UE, UN):
    a = abs(np.einsum('nji,mjk->nmik', UE.conj(), UN))**2
    s13 = a[..., 0, 2]
    with np.errstate(divide='ignore', invalid='ignore'):
        s12 = a[..., 0, 1]/(1 - s13); s23 = a[..., 1, 2]/(1 - s13)
    return s12, s23, s13
def delta_of(UE, UN, mask):
    V = np.einsum('nji,mjk->nmik', UE.conj(), UN)[mask]
    a = abs(V)**2; s13 = a[:, 0, 2]; c13 = 1 - s13
    s12 = a[:, 0, 1]/c13; s23 = a[:, 1, 2]/c13
    S12, C12, S23, C23, S13 = np.sqrt(s12), np.sqrt(1 - s12), np.sqrt(s23), np.sqrt(1 - s23), np.sqrt(s13)
    J = np.imag(V[:, 0, 0]*V[:, 1, 1]*np.conj(V[:, 0, 1])*np.conj(V[:, 1, 0]))
    sd = J/(C12*S12*C23*S23*c13*S13)
    cd = (a[:, 1, 0] - s12*(1 - s23) - (1 - s12)*s23*s13)/(2*S12*C12*S23*C23*S13)
    return np.clip(sd, -1, 1), np.clip(cd, -1, 1)
def evaluate(s12, s23, s13):
    base = (s13 >= R13[0]) & (s13 <= R13[1])
    hit = base & (s23 >= R23[0]) & (s23 <= R23[1]) & (s12 >= J12[0]) & (s12 <= J12[1])
    sharp = base & (s12 >= J12[0]) & (s12 <= J12[1])
    return hit, sharp


K = {"artanh(beta exakt)": float(np.arctanh(0.549406)), "artanh(0.5493)": float(np.arctanh(0.5493))}
cand = sorted(set(round(v, 10) for v in K.values()))
name = {round(v, 10): k for k, v in K.items()}
grid = sorted(set(list(np.round(np.arange(0, 0.7 + 1e-12, 0.01), 6)) + cand))
Ce = charged(grid)
UN = []
for p in range(3):
    for phi in PHI:
        Q = Qphi(p, phi)
        for order in itertools.permutations(range(3)):
            UN.append(Q[:, list(order)])
UN = np.array(UN)
res = []
def stats(label, c, s23, s13, s12, D):
    pass
for c in cand:
    if c not in Ce: res.append(("A", name[c], c, 0, None, None)); continue
    s12, s23, s13 = angles(Ce[c], UN)
    hit, _ = evaluate(s12, s23, s13)
    if hit.any():
        sd, cd = delta_of(Ce[c], UN, hit)
        res.append(("A", name[c], c, int(hit.sum()), (s23[hit].min(), s23[hit].max()), (abs(sd).min(), abs(sd).max())))
    else: res.append(("A", name[c], c, 0, None, None))
gridB = sorted(set(list(np.round(np.arange(0, 0.7 + 1e-12, 0.02), 6)) + cand))
acc = {c: {"n": 0, "s23": [], "sd": []} for c in cand}
for m1 in M1:
    tgt = nu(m1)/nu(m1).max(); den = np.where(tgt > 0, tgt, 1.0)
    NB = {c: [] for c in cand}
    for p in range(3):
        for phi in PHI:
            Q = Qphi(p, phi)
            for order in itertools.permutations(range(3)):
                for sg in itertools.product((1, -1), repeat=2):
                    mu = np.zeros(3); sgn = (1,) + sg
                    for col, k in enumerate(order): mu[col] = sgn[col]*tgt[k]
                    for e in gridB:
                        D = np.diag(np.exp(e*Wl))
                        Mf = lambda x: D@Q@np.diag(x)@Q.T@D
                        def f(x):
                            w = np.sort(abs(np.linalg.eigvalsh(Mf(x)))); return (w - tgt)/den
                        r = least_squares(f, mu, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14)
                        if np.max(abs(r.fun)) > 1e-7: break
                        mu = r.x
                        if e in NB:
                            w, V = np.linalg.eigh(Mf(mu)); o = np.argsort(abs(w)); NB[e].append(V[:, o])
    for c in cand:
        if not NB[c] or c not in Ce: continue
        UNb = np.array(NB[c])
        s12, s23, s13 = angles(Ce[c], UNb)
        hit, _ = evaluate(s12, s23, s13)
        if hit.any():
            sd, cd = delta_of(Ce[c], UNb, hit)
            acc[c]["n"] += int(hit.sum()); acc[c]["s23"] += list(s23[hit]); acc[c]["sd"] += list(abs(sd))
for c in cand:
    a = acc[c]
    res.append(("B", name[c], c, a["n"], (min(a["s23"]), max(a["s23"])) if a["n"] else None, (min(a["sd"]), max(a["sd"])) if a["n"] else None))
ok = []
for v, nm, c, n, r23, rsd in res:
    line = f"Variante {v}, eps = {nm} ({c:.4f}): {n} Treffer"
    if n:
        w23, wsd = r23[1] - r23[0], rsd[1] - rsd[0]
        line += f"; sin^2 23 in [{r23[0]:.4f}, {r23[1]:.4f}] (Breite {w23:.4f}), |sin delta| in [{rsd[0]:.3f}, {rsd[1]:.3f}] (Breite {wsd:.3f})"
        if w23 < 0.05 and wsd < 0.3: ok.append((v, nm)); line += "  <- scharf (H45b)"
    print(line)
hitA = any(n for v, nm, c, n, *_ in res if nm == "artanh(beta_sym)")
print(f"\nH45a (Treffer bei eps = artanh(beta_sym)): {'bestaetigt' if hitA else 'widerlegt'}")
print(f"H45b (scharf): {'bestaetigt' if any(nm == 'artanh(beta_sym)' for v, nm in ok) else 'widerlegt'}")
print(f"H45c (Treffer beim Hopf-Wert): {'ja' if any(n for v, nm, c, n, *_ in res if nm == 'artanh(1/sqrt3)') else 'nein'}")
