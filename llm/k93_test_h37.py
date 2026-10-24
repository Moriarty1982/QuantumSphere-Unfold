"""k93: Test der Vorab-Notiz H37 (Commit e1ee9ec): Kopplungen aus der Triality-Form. (a) reine Triality-Kopplung T(v), (b) Norm + Triality
alpha*1 + T(v) ohne Maske, (c) H/H~-Lesart der zirkulanten Kopplung mit Maske (u, nu und d, e in verschiedenen Formen)."""
import itertools, numpy as np
from scipy.optimize import brentq, least_squares

mu_, md_ = [1.23e-3, 0.620, 168.26], [2.67e-3, 53.16e-3, 2.839]
me_ = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003, 0.01, 0.02, 0.05, 0.1]
CKM = np.array([0.2250, 0.0418, 0.00373])
RNG = np.array([(0.275, 0.345), (0.430, 0.596), (0.02023, 0.02376)])
nu = lambda m1: [m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)]

# ---------------- H37a
print("H37a: m3 - (m1 + m2) relativ zu m3: u %.4f, d %.4f, e %.4f (Null waere noetig)" %
      tuple((m[2] - m[0] - m[1])/m[2] for m in (mu_, md_, me_)))
f = lambda m1: nu(m1)[2] - m1 - nu(m1)[1]
m1s = brentq(f, 0, 1)
sm = sum(nu(m1s))
print(f"  Dirac-Neutrinos: m1* = {m1s:.4f} eV, Massen {np.round(nu(m1s), 4)} eV, Summe {sm:.4f} eV (DESI DR2: < 0.0642 eV)"
      f" -> {'bestaetigt' if sm < 0.0642 else 'widerlegt'}")

# ---------------- H37b
def Tm(v): return np.array([[0, v[2], v[1]], [v[2], 0, v[0]], [v[1], v[0], 0]])
def curve(masses, n=500):
    m = np.array(masses, float); m = m/m.max(); out = []
    for sg in itertools.product((1, -1), repeat=2):
        lam = np.array([sg[0]*m[0], sg[1]*m[1], m[2]])
        a = lam.mean(); mu = lam - a
        S = 0.5*np.sum(mu**2); q = np.prod(mu)/2
        Us = []
        for v1 in np.linspace(-np.sqrt(S), np.sqrt(S), n + 2)[1:-1]:
            if abs(v1) < 1e-12: continue
            A, B = S - v1**2, q/v1
            if A + 2*B < 0 or A - 2*B < 0: continue
            s, d = np.sqrt(A + 2*B), np.sqrt(A - 2*B)
            for ss, dd in itertools.product((1, -1), repeat=2):
                v = np.array([v1, (ss*s + dd*d)/2, (ss*s - dd*d)/2])
                w, U = np.linalg.eigh(a*np.eye(3) + Tm(v))
                o = np.argsort(abs(w))
                assert np.allclose(abs(w[o]), m, rtol=1e-7, atol=1e-12), (abs(w[o]), m)
                Us.append(U[:, o])
        if Us: out.append(np.array(Us))
    return out

def pair_stats(UA, UB, fn, chunk=200):
    """Durchlaeuft alle Paare; fn(V-Stapel) -> (Treffer-Maske, Abstand). Rueckgabe: Treffer, Paare, bester Abstand und Werte."""
    hits = 0; tot = 0; best = (9, None)
    for A in UA:
        for B in UB:
            for i in range(0, len(A), chunk):
                V = np.einsum('nji,mjk->nmik', A[i:i+chunk].conj(), B)
                V = V.reshape(-1, 3, 3)
                h, dist, vals = fn(V)
                hits += int(h.sum()); tot += len(V)
                j = int(np.argmin(dist))
                if dist[j] < best[0]: best = (float(dist[j]), np.round(vals[j], 5))
    return hits, tot, best

def ckm_fn(V):
    a = abs(V); v = np.stack([a[:, 0, 1], a[:, 1, 2], a[:, 0, 2]], 1)
    dev = np.max(abs(v/CKM - 1), 1)
    return dev <= 0.2, dev, v
def pmns_fn(U):
    a = abs(U)**2; s13 = a[:, 0, 2]
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.stack([a[:, 0, 1]/(1 - s13), a[:, 1, 2]/(1 - s13), s13], 1)
    v = np.where(np.isfinite(v), v, 9)
    out = np.where(v < RNG[:, 0], (RNG[:, 0] - v), np.where(v > RNG[:, 1], v - RNG[:, 1], 0))/RNG.mean(1)
    dist = out.max(1)
    return dist == 0, dist, v

Cu, Cd = curve(mu_), curve(md_)
h, t, best = pair_stats(Cu, Cd, ckm_fn)
print(f"\nH37b Quarks: {h} von {t} Paaren innerhalb +-20 % ({100*h/t:.3f} %); naechster Fall {best[0]:.3f} bei |V_us|, |V_cb|, |V_ub| = {best[1]}")
ok_bq = h > 0
Ce = curve(me_); lh = 0; lt = 0; lbest = (9, None, None); per_m1 = {}
for m1 in M1:
    Cn = curve(nu(m1))
    hh, tt, bb = pair_stats(Ce, Cn, pmns_fn)
    lh += hh; lt += tt; per_m1[m1] = hh
    if bb[0] < lbest[0]: lbest = (bb[0], m1, bb[1])
print(f"H37b Leptonen: {lh} von {lt} Paaren in den 3sigma-Bereichen; je m1: {per_m1}; naechster Fall {lbest[0]:.3f} bei m1 = {lbest[1]}: sin^2 = {lbest[2]}")
ok_bl = lh > 0
print(f"H37b -> {'bestaetigt' if (ok_bq and ok_bl) else ('Teilbefund (nur Quarks)' if ok_bq else ('Teilbefund (nur Leptonen)' if ok_bl else 'widerlegt'))}")

# ---------------- H37c
w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
Wq = np.array([0., -2., -1.]); Wl = np.array([0., 0., -3.])
EPS = np.round(np.arange(0, 6.0 + 1e-12, 0.01), 6)
TOL = 1e-9
def M_of(lam, w, e, form):
    C = F@np.diag(lam)@F.conj().T
    D = np.diag(np.exp(e*w)); Di = np.diag(np.exp(-e*w))
    return D@C@D if form == "K" else D@C@Di
def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def branches(masses, w, form):
    m = np.array(masses, float); m = m/m.max(); den = np.where(m > 0, m, 1.0); out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i]*m[p[i]] for i in range(3)]); br = {}
            for e in EPS:
                r = least_squares(lambda x: (sv_sorted(M_of(x, w, e, form))[0] - m)/den, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                lam = r.x; br[e] = sv_sorted(M_of(lam, w, e, form))[1]
            out.append(br)
    return out
cache = {}
def B(key, masses, w, form):
    if (key, form) not in cache: cache[(key, form)] = branches(masses, w, form)
    return cache[(key, form)]
ok_c_any = False
for name, (fu, fd) in (("u, nu in S; d, e in K", ("S", "K")), ("u, nu in K; d, e in S", ("K", "S"))):
    Bu, Bd = B("u", mu_, Wq, fu), B("d", md_, Wq, fd)
    good = []; tot = 0; best = (9, None)
    for e in EPS:
        for bu in Bu:
            if e not in bu: continue
            for bd in Bd:
                if e not in bd: continue
                tot += 1; a = abs(bu[e].conj().T@bd[e]); v = np.array([a[0, 1], a[1, 2], a[0, 2]]); dev = np.max(abs(v/CKM - 1))
                if dev <= 0.2: good.append(e)
                if dev < best[0]: best = (dev, (e, np.round(v, 5)))
    eg = set(good); hits = 0
    if eg:
        Be = B("e", me_, Wl, fd)
        for m1 in M1:
            Bn = B(f"nu{m1}", nu(m1), Wl, fu)
            for be in Be:
                for bn in Bn:
                    for e in eg & set(be) & set(bn):
                        h_, d_, v_ = pmns_fn((be[e].conj().T@bn[e])[None])
                        hits += int(h_[0])
    ok = len(good) > 0 and hits > 0; ok_c_any |= ok
    print(f"\nH37c [{name}]: CKM {len(good)} von {tot} innerhalb +-20 %; naechster Fall {best[0]:.3f} bei (eps, |V|) = {best[1]};"
          f" PMNS-Treffer bei diesen eps: {hits}")
print(f"H37c -> {'bestaetigt' if ok_c_any else 'widerlegt'} (zwei Zuordnungen gerechnet)")

# Nachkontrolle (nach der Auswertung, kein Teil des Kriteriums): Die Quark-Kurven waren duenn besetzt, weil nur ein schmaler Teil des v1-Gitters
# zulaessig ist. Hier werden die zulaessigen v1-Intervalle zuerst bestimmt und dann je Intervall dicht abgetastet.
def curve_dense(masses, n=2000):
    m = np.array(masses, float); m = m/m.max(); out = []
    for sg in itertools.product((1, -1), repeat=2):
        lam = np.array([sg[0]*m[0], sg[1]*m[1], m[2]]); a = lam.mean(); mu = lam - a
        S = 0.5*np.sum(mu**2); q = np.prod(mu)/2
        g = np.linspace(-np.sqrt(S), np.sqrt(S), 200001)[1:-1]; g = g[abs(g) > 1e-14]
        ok = (S - g**2 + 2*q/g >= 0) & (S - g**2 - 2*q/g >= 0)
        if not ok.any(): continue
        idx = np.where(ok)[0]; segs = np.split(idx, np.where(np.diff(idx) > 1)[0] + 1)
        Us = []
        for sgm in segs:
            lo, hi = g[sgm[0]], g[sgm[-1]]
            for v1 in np.linspace(lo, hi, n):
                A, B = S - v1**2, q/v1
                if A + 2*B < 0 or A - 2*B < 0: continue
                s, d = np.sqrt(A + 2*B), np.sqrt(A - 2*B)
                for ss, dd in itertools.product((1, -1), repeat=2):
                    v = np.array([v1, (ss*s + dd*d)/2, (ss*s - dd*d)/2])
                    w, U = np.linalg.eigh(a*np.eye(3) + Tm(v)); o = np.argsort(abs(w))
                    if np.allclose(abs(w[o]), m, rtol=1e-6, atol=1e-12): Us.append(U[:, o])
        if Us: out.append(np.array(Us))
    return out
Du, Dd = curve_dense(mu_, 400), curve_dense(md_, 400)
h, t, best = pair_stats(Du, Dd, ckm_fn)
print(f"\nNachkontrolle H37b Quarks (dicht): {sum(len(x) for x in Du)} u-Punkte, {sum(len(x) for x in Dd)} d-Punkte; {h} von {t} Paaren innerhalb"
      f" +-20 %; naechster Fall {best[0]:.3f} bei |V_us|, |V_cb|, |V_ub| = {best[1]}")
print("Nachkontrolle Leptonen: Treffer nur bei m1 = 0.05 und 0.1 eV, also Summe der Neutrinomassen",
      {m1: round(sum(nu(m1)), 4) for m1 in (0.05, 0.1)}, "eV gegen DESI DR2 < 0.0642 eV")
