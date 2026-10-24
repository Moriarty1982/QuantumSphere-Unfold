"""k92: Test der Vorab-Notiz H36 (Commit 66c12ab): Kopplungsformen der Maske aus r47. Form K: M = D C D, Form S: M = D C D^-1, D = exp(eps W);
CKM und PMNS mit einem gemeinsamen eps."""
import itertools, numpy as np
from scipy.optimize import least_squares

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
    U, s, Vh = np.linalg.svd(M)
    o = np.argsort(s)
    return s[o], U[:, o]

def branches(masses, w, form):
    m = np.array(masses, float); m = m/m.max()
    den = np.where(m > 0, m, 1.0)
    out = []
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i]*m[p[i]] for i in range(3)])
            br = {}
            for e in EPS:
                f = lambda x: (sv_sorted(M_of(x, w, e, form))[0] - m)/den
                r = least_squares(f, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                lam = r.x
                br[e] = sv_sorted(M_of(lam, w, e, form))[1]
            out.append(br)
    return out

def ckm(V): a = abs(V); return np.array([a[0, 1], a[1, 2], a[0, 2]])
def pmns(U):
    a = abs(U)**2; s13 = a[0, 2]
    return np.array([a[0, 1]/(1 - s13), a[1, 2]/(1 - s13), s13]) if s13 < 1 else np.array([np.nan]*3)

mu, md = [1.23e-3, 0.620, 168.26], [2.67e-3, 53.16e-3, 2.839]
me = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003, 0.01, 0.02, 0.05, 0.1]
CKM = np.array([0.2250, 0.0418, 0.00373])
RNG = [(0.275, 0.345), (0.430, 0.596), (0.02023, 0.02376)]
inside = lambda v: all(R[0] <= x <= R[1] for x, R in zip(v, RNG))
def outside(v): return max(0.0 if R[0] <= x <= R[1] else min(abs(x - R[0]), abs(x - R[1]))/((R[0] + R[1])/2) for x, R in zip(v, RNG))

for form, (ha, hb) in (("K", ("H36a", "H36b")), ("S", ("H36c", "H36d"))):
    Bu, Bd = branches(mu, Wq, form), branches(md, Wq, form)
    total = 0; good = []; best = (9, None)
    for e in EPS:
        for bu in Bu:
            if e not in bu: continue
            for bd in Bd:
                if e not in bd: continue
                total += 1
                v = ckm(bu[e].conj().T@bd[e]); dev = np.max(abs(v/CKM - 1))
                if dev <= 0.2: good.append((e, v))
                if dev < best[0]: best = (dev, (e, np.round(v, 5)))
    eps_good = sorted(set(g[0] for g in good))
    print(f"Form {form}: Zweige bis eps = 6 durchgehend: u {sum(len(b) == len(EPS) for b in Bu)}/24, d {sum(len(b) == len(EPS) for b in Bd)}/24;"
          f" groesstes eps mit Loesung u {max(max(b) for b in Bu if b)}, d {max(max(b) for b in Bd if b)}")
    print(f"{ha}: {len(good)} von {total} Kombinationen innerhalb +-20 % ({100*len(good)/max(total, 1):.3f} %); eps-Bereich "
          f"{(min(eps_good), max(eps_good)) if eps_good else '-'}; naechster Fall: max. relative Abweichung {best[0]:.3f} bei (eps, |V_us|, |V_cb|, |V_ub|) = {best[1]}"
          f" -> {'bestaetigt' if good else 'widerlegt'}")
    Be = branches(me, Wl, form)
    lep = {m1: branches([m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)], Wl, form) for m1 in M1}
    hits = []; bestl = (9, None); hits_any = []; ltot = 0
    for m1, Bn in lep.items():
        for be in Be:
            for bn in Bn:
                for e in set(be) & set(bn):
                    v = pmns(be[e].conj().T@bn[e])
                    if not np.all(np.isfinite(v)): continue
                    ltot += 1
                    if inside(v):
                        hits_any.append((e, m1))
                        if e in eps_good: hits.append((e, m1, np.round(v, 4)))
                    d = outside(v)
                    if d < bestl[0]: bestl = (d, (e, m1, np.round(v, 4)))
    print(f"{hb}: {len(hits)} Treffer bei eps aus {ha}" + (f", z. B. {hits[0]}" if hits else "") + f" -> {'bestaetigt' if hits else 'widerlegt'}")
    print(f"  Nachkontrolle (kein Kriterium): Leptonen allein mit eigenem eps: {len(hits_any)} von {ltot} Kombinationen"
          + (f", eps in [{min(h[0] for h in hits_any)}, {max(h[0] for h in hits_any)}], m1 {sorted(set(h[1] for h in hits_any))}" if hits_any else "")
          + f"; naechster Fall {bestl[0]:.2f} bei (eps, m1, sin^2) = {bestl[1]}\n")
