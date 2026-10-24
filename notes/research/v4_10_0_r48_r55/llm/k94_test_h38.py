"""k94: Test der Vorab-Notiz H38 (Commit d3555bf): Formen K (D C D) und S (D C D^-1) mit einem eps je Sektor."""
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

def M_of(lam, w, e, form):
    C = F@np.diag(lam)@F.conj().T
    D = np.diag(np.exp(e*w)); Di = np.diag(np.exp(-e*w))
    return D@C@D if form == "K" else D@C@Di
def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def entries(masses, w, form):
    """Alle (eps, Zweig, U) entlang der Zweige wie in H36."""
    m = np.array(masses, float); m = m/m.max(); den = np.where(m > 0, m, 1.0); E, Us = [], []
    for ib, (p, sg) in enumerate(((p, sg) for p in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3) if sg[0] == 1)):
        lam = np.array([sg[i]*m[p[i]] for i in range(3)])
        for e in EPS:
            r = least_squares(lambda x: (sv_sorted(M_of(x, w, e, form))[0] - m)/den, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
            if np.max(abs(r.fun)) > TOL: break
            lam = r.x; E.append((e, ib)); Us.append(sv_sorted(M_of(lam, w, e, form))[1])
    return np.array(E), np.array(Us)

def scan(EA, UA, EB, UB, kind, chunk=100):
    hits = []; tot = 0; best = (9, None)
    for i in range(0, len(UA), chunk):
        V = np.einsum('nji,mjk->nmik', UA[i:i+chunk].conj(), UB)
        a = abs(V)
        if kind == "ckm":
            v = np.stack([a[..., 0, 1], a[..., 1, 2], a[..., 0, 2]], -1)
            dist = np.max(abs(v/CKM - 1), -1); ok = dist <= 0.2
        else:
            a2 = a**2; s13 = a2[..., 0, 2]
            with np.errstate(divide='ignore', invalid='ignore'):
                v = np.stack([a2[..., 0, 1]/(1 - s13), a2[..., 1, 2]/(1 - s13), s13], -1)
            v = np.where(np.isfinite(v), v, 9)
            out = np.where(v < RNG[:, 0], RNG[:, 0] - v, np.where(v > RNG[:, 1], v - RNG[:, 1], 0))/RNG.mean(1)
            dist = out.max(-1); ok = dist == 0
        tot += ok.size
        for n, mm in zip(*np.nonzero(ok)): hits.append((EA[i + n][0], EB[mm][0], np.round(v[n, mm], 5)))
        n, mm = np.unravel_index(np.argmin(dist), dist.shape)
        if dist[n, mm] < best[0]: best = (float(dist[n, mm]), (EA[i + n][0], EB[mm][0], np.round(v[n, mm], 5)))
    return hits, tot, best

def region(hits):
    if not hits: return "-"
    pts = sorted(set((h[0], h[1]) for h in hits))
    a = np.array(pts)
    return (f"{len(pts)} (eps1, eps2)-Gitterpunkte, eps1 in [{a[:,0].min()}, {a[:,0].max()}], eps2 in [{a[:,1].min()}, {a[:,1].max()}]")

for form, (ha, hb) in (("K", ("H38a", "H38b")), ("S", ("H38c", "H38d"))):
    Eu, Uu = entries(mu_, Wq, form); Ed, Ud = entries(md_, Wq, form)
    hits, tot, best = scan(Eu, Uu, Ed, Ud, "ckm")
    frac = 100*len(hits)/tot
    print(f"Form {form}: {ha}: {len(hits)} von {tot} Kombinationen (eps_u, eps_d, Zweige) innerhalb +-20 % ({frac:.4f} %); Region: {region(hits)};"
          f" naechster Fall {best[0]:.3f} bei (eps_u, eps_d, |V|) = {best[1]} -> {'bestaetigt' if hits else 'widerlegt'}")
    if hits:
        ex = sorted(hits, key=lambda h: np.max(abs(h[2]/CKM - 1)))[:3]
        print("   beste Treffer:", [(h[0], h[1], list(h[2])) for h in ex])
    Ee, Ue = entries(me_, Wl, form); lh = []; lt = 0; lbest = (9, None)
    for m1 in M1:
        En, Un = entries(nu(m1), Wl, form)
        h, t, b = scan(Ee, Ue, En, Un, "pmns")
        lh += [(x[0], x[1], m1, x[2]) for x in h]; lt += t
        if b[0] < lbest[0]: lbest = (b[0], (m1,) + b[1])
    print(f"Form {form}: {hb}: {len(lh)} von {lt} Kombinationen in den 3sigma-Bereichen ({100*len(lh)/max(lt,1):.4f} %);"
          f" m1: {sorted(set(x[2] for x in lh))}; Region: {region(lh)}; naechster Fall {lbest[0]:.3f} bei (m1, eps_e, eps_nu, sin^2) = {lbest[1]}"
          f" -> {'bestaetigt' if lh else 'widerlegt'}\n")

# Nachkontrolle (nach der Auswertung, kein Teil des Kriteriums), nur Form S:
# 1. Zusammenhang der passenden Region (Nachbarschaft auf dem 0.01-Gitter, je Zweigpaar).
# 2. Wie scharf ist die dritte Groesse festgelegt? Kombinationen, die nur zwei Groessen treffen, und die Spannweite der dritten.
def components(pts):
    pts = set(pts); comps = 0
    while pts:
        stack = [pts.pop()]; comps += 1
        while stack:
            a, b = stack.pop()
            for da in (-0.01, 0, 0.01):
                for db in (-0.01, 0, 0.01):
                    q = (round(a + da, 2), round(b + db, 2))
                    if q in pts: pts.remove(q); stack.append(q)
    return comps
Eu, Uu = entries(mu_, Wq, "S"); Ed, Ud = entries(md_, Wq, "S")
two = []; full = []
for i in range(0, len(Uu), 100):
    a = abs(np.einsum('nji,mjk->nmik', Uu[i:i+100].conj(), Ud))
    v = np.stack([a[..., 0, 1], a[..., 1, 2], a[..., 0, 2]], -1)
    okus = abs(v[..., 0]/CKM[0] - 1) <= 0.2; okcb = abs(v[..., 1]/CKM[1] - 1) <= 0.2; okub = abs(v[..., 2]/CKM[2] - 1) <= 0.2
    for n, mm in zip(*np.nonzero(okus & okcb)):
        two.append(v[n, mm, 2])
        if okub[n, mm]: full.append((round(Eu[i + n][0], 2), round(Ed[mm][0], 2), int(Eu[i + n][1]), int(Ed[mm][1])))
two = np.array(two)
pts_by_pair = {}
for eu, ed, bu, bd in full: pts_by_pair.setdefault((bu, bd), set()).add((eu, ed))
print(f"Nachkontrolle S, Quarks: Zweigpaare mit Treffern {len(pts_by_pair)}, Zusammenhangskomponenten je Paar {[components(p) for p in pts_by_pair.values()]};"
      f" Kombinationen mit |V_us| und |V_cb| in +-20 %: {len(two)}, dort |V_ub| in [{two.min():.5f}, {two.max():.5f}], Median {np.median(two):.5f},"
      f" Anteil mit |V_ub| in +-20 %: {100*np.mean(abs(two/CKM[2] - 1) <= 0.2):.1f} %")
Ee, Ue = entries(me_, Wl, "S"); third = []; lfull = []
for m1 in M1:
    En, Un = entries(nu(m1), Wl, "S")
    for i in range(0, len(Ue), 100):
        a2 = abs(np.einsum('nji,mjk->nmik', Ue[i:i+100].conj(), Un))**2; s13 = a2[..., 0, 2]
        with np.errstate(divide='ignore', invalid='ignore'):
            s12 = a2[..., 0, 1]/(1 - s13); s23 = a2[..., 1, 2]/(1 - s13)
        ok12 = (s12 >= RNG[0, 0]) & (s12 <= RNG[0, 1]); ok23 = (s23 >= RNG[1, 0]) & (s23 <= RNG[1, 1])
        for n, mm in zip(*np.nonzero(ok12 & ok23)):
            third.append(s13[n, mm])
            if RNG[2, 0] <= s13[n, mm] <= RNG[2, 1]: lfull.append((m1, round(Ee[i + n][0], 2), round(En[mm][0], 2), int(Ee[i + n][1]), int(En[mm][1])))
third = np.array(third)
lp = {}
for m1, ee, en, be, bn in lfull: lp.setdefault((m1, be, bn), set()).add((ee, en))
print(f"Nachkontrolle S, Leptonen: Zweigpaare (mit m1) mit Treffern {len(lp)}, Komponenten je Paar {[components(p) for p in lp.values()]};"
      f" Kombinationen mit sin^2 12 und 23 in 3sigma: {len(third)}, dort sin^2 13 in [{third.min():.4f}, {third.max():.4f}], Median {np.median(third):.4f},"
      f" Anteil in 3sigma: {100*np.mean((third >= RNG[2,0]) & (third <= RNG[2,1])):.1f} %")
