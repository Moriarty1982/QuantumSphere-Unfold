"""k96: Test der Vorab-Notiz H40 (Commit fdb27ae): Kalibrierung der Ausleseschicht (Form S, ein eps je Sektor) und Suche nach Struktur in den
Einstellungen mit Zufalls-Gegenprobe."""
import itertools, numpy as np
from scipy.optimize import least_squares

w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
Wq = np.array([0., -2., -1.]); Wl = np.array([0., 0., -3.])
EPS = np.round(np.arange(0, 6.0 + 1e-12, 0.01), 6)
TOL = 1e-9
mu_, md_ = [1.23e-3, 0.620, 168.26], [2.67e-3, 53.16e-3, 2.839]
me_ = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003]
nu = lambda m1: [m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)]
CKM = np.array([0.2250, 0.0418, 0.00373])
RNG = np.array([(0.275, 0.345), (0.430, 0.596), (0.02023, 0.02376)])

def M_of(lam, w, e):
    C = F@np.diag(lam)@F.conj().T
    return np.diag(np.exp(e*w))@C@np.diag(np.exp(-e*w))
def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def entries(masses, w):
    m = np.array(masses, float); m = m/m.max(); den = np.where(m > 0, m, 1.0); E, Us, L = [], [], []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i]*m[p[i]] for i in range(3)])
            for e in EPS:
                r = least_squares(lambda x: (sv_sorted(M_of(x, w, e))[0] - m)/den, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                lam = r.x; E.append(e); Us.append(sv_sorted(M_of(lam, w, e))[1]); L.append(lam.copy())
    return np.array(E), np.array(Us), np.array(L)
def brannen(lam):
    C = F@np.diag(lam)@F.conj().T
    a = np.real(C[0, 0]); b = C[1, 0]
    th = np.angle(b) % (2*np.pi/3)
    if th > np.pi/3: th = 2*np.pi/3 - th
    return abs(b)/abs(a), th

def passing(EA, UA, EB, UB, kind, chunk=100):
    out = []
    for i in range(0, len(UA), chunk):
        a = abs(np.einsum('nji,mjk->nmik', UA[i:i+chunk].conj(), UB))
        if kind == "ckm":
            v = np.stack([a[..., 0, 1], a[..., 1, 2], a[..., 0, 2]], -1); ok = np.all(abs(v/CKM - 1) <= 0.2, -1)
        else:
            a2 = a**2; s13 = a2[..., 0, 2]
            with np.errstate(divide='ignore', invalid='ignore'):
                v = np.stack([a2[..., 0, 1]/(1 - s13), a2[..., 1, 2]/(1 - s13), s13], -1)
            ok = np.all((v >= RNG[:, 0]) & (v <= RNG[:, 1]), -1)
        out += [(i + n, mm) for n, mm in zip(*np.nonzero(ok))]
    return out

Eu, Uu, Lu = entries(mu_, Wq); Ed, Ud, Ld = entries(md_, Wq)
q = passing(Eu, Uu, Ed, Ud, "ckm")
Ee, Ue, Le = entries(me_, Wl)
lep = []
for m1 in M1:
    En, Un, Ln = entries(nu(m1), Wl)
    lep += [(ie, Ln[jn], En[jn]) for ie, jn in passing(Ee, Ue, En, Un, "pmns")]
print(f"Zulaessige Kombinationen: Quarks {len(q)}, Leptonen {len(lep)} (wie H38: 294 und 1008)")

S = {}
S["eps_u"] = [Eu[i] for i, j in q]; S["eps_d"] = [Ed[j] for i, j in q]
S["eps_e"] = [Ee[i] for i, _, _ in lep]; S["eps_nu"] = [e for _, _, e in lep]
S["eps_u/eps_d"] = [Eu[i]/Ed[j] for i, j in q]; S["eps_e/eps_nu"] = [Ee[i]/e for i, _, e in lep]
for nm, (A, B) in {"eps_d/eps_e": ("eps_d", "eps_e"), "eps_u/eps_nu": ("eps_u", "eps_nu")}.items():
    S[nm] = [min(S[A])/max(S[B]), max(S[A])/min(S[B])]
for nm, vals in (("u", [brannen(Lu[i]) for i, j in q]), ("d", [brannen(Ld[j]) for i, j in q]),
                 ("e", [brannen(Le[i]) for i, _, _ in lep]), ("nu", [brannen(L) for _, L, _ in lep])):
    S[f"|b|/|a| {nm}"] = [v[0] for v in vals]; S[f"theta {nm}"] = [v[1] for v in vals]
R = {k: (min(v), max(v)) for k, v in S.items()}
print("\nKalibrierte Einstellungen (Bereich ueber alle zulaessigen Kombinationen):")
for k, (lo, hi) in R.items(): print(f"  {k:14s} [{lo:.4f}, {hi:.4f}]")

K = {"1/3": 1/3, "1/2": 0.5, "2/3": 2/3, "3/4": 0.75, "1": 1.0, "1/sqrt3": 1/np.sqrt(3), "1/sqrt2": 1/np.sqrt(2), "sqrt3": np.sqrt(3),
     "2/9": 2/9, "pi/6": np.pi/6, "pi/9": np.pi/9, "beta_sym^2": 0.5493**2, "beta_sym": 0.5493, "gamma_L": 1.864}
def count(vals): return sum(lo <= v <= hi for (lo, hi) in R.values() for v in vals)
hits = [(k, c) for k, (lo, hi) in R.items() for c, v in K.items() if lo <= v <= hi]
n_obs = len(hits)
rng = np.random.default_rng(40)
rand = np.array([count(np.exp(rng.uniform(np.log(0.2), np.log(2), 14))) for _ in range(10000)])
p = np.mean(rand >= n_obs)
print(f"\nTreffer der Kandidaten: {n_obs}: {hits}")
print(f"Gegenprobe: Zufallssaetze im Mittel {rand.mean():.2f} Treffer (95 %-Quantil {np.quantile(rand, 0.95):.0f}); p = {p:.4f}")
print(f"H40a -> {'bestaetigt' if p < 0.01 else 'widerlegt'}")
eq = [k for k in ("eps_u/eps_d", "eps_e/eps_nu", "eps_d/eps_e", "eps_u/eps_nu") if R[k][0] <= 1 <= R[k][1]]
print(f"H40b: Verhaeltnisse mit 1 im Bereich: {eq} -> {'bestaetigt' if eq else 'widerlegt'}")

# Lesarten nach der Rechnung (kein Kriterium)
print("\nLesart Beltrami (kein Kriterium): K = exp(eps * Spannweite W), |mu| = (K-1)/(K+1)")
for nm, sp in (("eps_u", 2), ("eps_d", 2), ("eps_e", 3), ("eps_nu", 3)):
    lo, hi = R[nm]
    f = lambda e: (np.exp(e*sp) - 1)/(np.exp(e*sp) + 1)
    print(f"  {nm}: K in [{np.exp(lo*sp):.2f}, {np.exp(hi*sp):.2f}], |mu| in [{f(lo):.4f}, {f(hi):.4f}]")
