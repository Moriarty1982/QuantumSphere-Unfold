"""k98: Test der Vorab-Notiz H43 (Commit 59d8d04): CP-Phase delta der Treffer von H41 (Modelle und Gitter wie k97)."""
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

# ---- Variante A
Ce = charged(np.round(np.arange(0, 2.0 + 1e-12, 0.01), 6))
UN = []
for p in range(3):
    for phi in PHI:
        Q = Qphi(p, phi)
        for order in itertools.permutations(range(3)):
            UN.append(Q[:, list(order)])
UN = np.array(UN)
nh = 0; tot = 0; s23s = []; s12h = []; info = []; DA = []
for e, UE in Ce.items():
    s12, s23, s13 = angles(UE, UN)
    hit, sharp = evaluate(s12, s23, s13)
    nh += int(hit.sum()); tot += hit.size; s23s += list(s23[sharp]); s12h += list(s12[hit])
    if hit.any():
        info.append(e); sd, cd = delta_of(UE, UN, hit); DA.append(np.column_stack([sd, cd]))
print(f"H41a (Variante A): {nh} von {tot} Faellen treffen (theta13, theta23 NuFIT 3sigma, theta12 JUNO 2sigma); eps_e mit Treffer: "
      f"{(min(info), max(info)) if info else '-'} -> {'bestaetigt' if nh else 'widerlegt'}")
if s23s: print(f"  sin^2 23 bei theta12 (JUNO 2sigma) und theta13 (3sigma): [{min(s23s):.4f}, {max(s23s):.4f}], Breite {max(s23s) - min(s23s):.4f}")
okA = nh > 0; sharpA = bool(s23s) and (max(s23s) - min(s23s) < 0.05)

# ---- Variante B
EB = np.round(np.arange(0, 1.5 + 1e-12, 0.02), 6)
nhB = 0; totB = 0; s23B = []; infoB = []; DB = []
for m1 in M1:
    tgt = nu(m1)/nu(m1).max(); den = np.where(tgt > 0, tgt, 1.0)
    NB = {e: [] for e in EB}
    for p in range(3):
        for phi in PHI:
            Q = Qphi(p, phi)
            for order in itertools.permutations(range(3)):
                for sg in itertools.product((1, -1), repeat=2):
                    mu = np.zeros(3); sgn = (1,) + sg
                    for col, k in enumerate(order): mu[col] = sgn[col]*tgt[k]
                    for e in EB:
                        D = np.diag(np.exp(e*Wl))
                        Mf = lambda x: D@Q@np.diag(x)@Q.T@D
                        def f(x):
                            w = np.sort(abs(np.linalg.eigvalsh(Mf(x)))); return (w - tgt)/den
                        r = least_squares(f, mu, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14)
                        if np.max(abs(r.fun)) > 1e-7: break
                        mu = r.x
                        w, V = np.linalg.eigh(Mf(mu)); o = np.argsort(abs(w)); NB[e].append(V[:, o])
    for e in EB:
        if not NB[e] or e not in Ce: continue
        s12, s23, s13 = angles(Ce[e], np.array(NB[e]))
        hit, sharp = evaluate(s12, s23, s13)
        nhB += int(hit.sum()); totB += hit.size; s23B += list(s23[sharp])
        if hit.any():
            infoB.append((e, m1)); sd, cd = delta_of(Ce[e], np.array(NB[e]), hit); DB.append(np.column_stack([sd, cd]))
print(f"\nH41b (Variante B): {nhB} von {totB} Faellen treffen; (eps, m1) mit Treffer: {sorted(set(infoB))[:10]}{' ...' if len(set(infoB)) > 10 else ''}"
      f" -> {'bestaetigt' if nhB else 'widerlegt'}")
if s23B: print(f"  sin^2 23 bei theta12 (JUNO 2sigma) und theta13 (3sigma): [{min(s23B):.4f}, {max(s23B):.4f}], Breite {max(s23B) - min(s23B):.4f}")
okB = nhB > 0; sharpB = bool(s23B) and (max(s23B) - min(s23B) < 0.05)
def report(name, D, label):
    D = np.vstack(D); asd = abs(D[:, 0]); cd = D[:, 1]
    deg = np.degrees(np.arctan2(D[:, 0], D[:, 1])) % 360
    wa, wc = asd.max() - asd.min(), cd.max() - cd.min()
    print(f"{label} ({name}): {len(D)} Treffer; |sin delta| in [{asd.min():.3f}, {asd.max():.3f}] (Breite {wa:.3f}), cos delta in [{cd.min():.3f}, {cd.max():.3f}]"
          f" (Breite {wc:.3f}); delta-Quantile 5/50/95 %: {np.round(np.quantile(deg, [0.05, 0.5, 0.95]), 1)} Grad -> {'bestaetigt' if (wa < 0.3 or wc < 0.3) else 'widerlegt'}")
print()
report("Variante A", DA, "H43a")
report("Variante B", DB, "H43b")
