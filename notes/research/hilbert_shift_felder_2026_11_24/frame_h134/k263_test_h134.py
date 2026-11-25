"""k263 (Test H134, Vorab-Notiz a0ab92e vom 25.11.2026): Frame-Korrektur (Maske W_l, eps = Rapiditaet des Materie-Frames) auf die TM1-Klasse aus k262.
Regel und Funktionen (charged, angles, delta_of) unveraendert aus notes/research/v4_10_0_r56_r60/llm/k100_test_h45.py uebernommen.
Neutrinos: reelle Form, invariant unter einer ungeraden Z2 = <A> (k262, Lesart B). Variante A: eps_nu = 0; Variante B: eps_nu = eps_e.
Aufruf: python3 k263_test_h134.py [Schritt in Grad, Vorgabe 2]
"""
import itertools, sys, numpy as np
from scipy.optimize import least_squares

w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
Wl = np.array([0., 0., -3.])
TOL = 1e-9
me_ = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003]
nu = lambda m1: np.array([m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)])
R13, R23 = (0.02023, 0.02376), (0.430, 0.596)
J25 = (0.2918, 0.3266)                      # JUNO 2025, 2 sigma (k100; nur fuer Kontrolle ii)
J26, J26_1 = (0.2908, 0.3164), (0.2972, 0.3100)   # JUNO 2026: 0.3036 +- 0.0064, 2 sigma und 1 sigma
JMEAN = 0.3036
STEP = float(sys.argv[1]) if len(sys.argv) > 1 else 2.0        # Raster in phi (Grad); Vorab-Notiz: 2
PHI = np.deg2rad(np.arange(0, 180, STEP))
PHI2 = np.deg2rad(np.arange(0, 180, 2))                         # Raster von k100 fuer Kontrolle (ii)

def sv_sorted(M):
    U, s, Vh = np.linalg.svd(M); o = np.argsort(s); return s[o], U[:, o]
def charged(eps_grid):
    m = np.array(me_)/max(me_); out = {e: [] for e in eps_grid}; worst = 0.0
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if sg[0] == -1: continue
            lam = np.array([sg[i]*m[p[i]] for i in range(3)])
            for e in eps_grid:
                Mf = lambda x: np.diag(np.exp(e*Wl))@(F@np.diag(x)@F.conj().T)@np.diag(np.exp(-e*Wl))
                r = least_squares(lambda x: (sv_sorted(Mf(x))[0] - m)/m, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
                if np.max(abs(r.fun)) > TOL: break
                worst = max(worst, np.max(abs(r.fun)))
                lam = r.x; out[e].append(sv_sorted(Mf(lam))[1])
    return {e: np.array(v) for e, v in out.items() if v}, worst
def Qphi_tm2(p, phi):            # k100: Z2 = diag-Spiegelung, feste Spalte e_p (TM2)
    q, r = [i for i in range(3) if i != p]
    Q = np.zeros((3, 3)); Q[p, 0] = 1
    Q[q, 1], Q[r, 1] = np.cos(phi), np.sin(phi); Q[q, 2], Q[r, 2] = -np.sin(phi), np.cos(phi)
    return Q
def Qphi_odd(p, sgn, phi):       # k262: ungerade Z2, einfacher Eigenvektor w = (e_q + sgn e_r)/sqrt2
    q, r = [i for i in range(3) if i != p]
    w = np.zeros(3); w[q] = 1/np.sqrt(2); w[r] = sgn/np.sqrt(2)
    u = np.zeros(3); u[q] = 1/np.sqrt(2); u[r] = -sgn/np.sqrt(2); ep = np.eye(3)[p]
    return np.column_stack([w, np.cos(phi)*ep + np.sin(phi)*u, -np.sin(phi)*ep + np.cos(phi)*u])
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
    return np.clip(sd, -1, 1)
in_ = lambda x, R: (x >= R[0]) & (x <= R[1])

ETA, HOPF = float(np.arctanh(0.5493)), float(np.arctanh(1/np.sqrt(3)))
cand = {0.0: "eps = 0", round(ETA, 10): "eps = artanh(beta_sym)", round(HOPF, 10): "eps = artanh(1/sqrt3)"}
grid = sorted(set(list(np.round(np.arange(0, 0.7 + 1e-12, 0.01), 6)) + list(cand)))
Ce, worst = charged(grid)
print("=" * 78); print("Kontrollen")
print(f"   (iii) Massen der geladenen Leptonen: groesster relativer Rest {worst:.1e}; Zweige je eps: " + ", ".join(f"{cand[c]}: {len(Ce[c]) if c in Ce else 0}" for c in cand))
# Kontrolle (ii): TM2-Lesart wie k100, Variante A, Bereiche von k100
UN2 = np.array([Qphi_tm2(p, phi)[:, list(o)] for p in range(3) for phi in PHI2 for o in itertools.permutations(range(3))])
c = round(ETA, 10); s12, s23, s13 = angles(Ce[c], UN2)
h2 = in_(s13, R13) & in_(s23, R23) & in_(s12, J25)
print(f"   (ii) TM2-Lesart, Variante A, eps = artanh(beta_sym), Bereiche von k100: {int(h2.sum())} Treffer (H45: 120); sin^2 23 in [{s23[h2].min():.4f}, {s23[h2].max():.4f}]")

CASES = [(p, sg) for p in range(3) for sg in (1, -1)]
ORD = list(itertools.permutations(range(3)))
def unA(p, sg): return np.array([Qphi_odd(p, sg, phi)[:, list(o)] for phi in PHI for o in ORD])
# Klasse bei eps = 0: feste Spalte (2/3,1/6,1/6) -> TM1, (0,1/2,1/2) -> theta13 = 0
cls = {}
for p, sg in CASES:
    w = Qphi_odd(p, sg, 0.0)[:, 0]; col = np.sort(abs(F.conj().T @ w)**2)
    cls[(p, sg)] = 'TM1' if abs(col[2] - 2/3) < 1e-9 else ('theta13=0' if abs(col[0]) < 1e-9 else 'andere')
print("   Klasse der sechs ungeraden Z2 bei eps = 0:", {f"p={p},{'+' if sg > 0 else '-'}": v for (p, sg), v in cls.items()})
# Kontrolle (i): eps = 0
s12a, s23a, sda, n0 = [], [], [], 0
for (p, sg) in CASES:
    if cls[(p, sg)] != 'TM1': continue
    UN = unA(p, sg); s12, s23, s13 = angles(Ce[0.0], UN)
    base = in_(s13, R13) & (abs(abs(np.einsum('nji,mjk->nmik', Ce[0.0].conj(), UN))**2 - 0)[..., 0, 0] > 0.6)   # TM1-Spalte als nu_1, Zeile e
    if base.any():
        s12a += list(s12[base]); s23a += list(s23[base]); sda += list(abs(delta_of(Ce[0.0], UN, base)))
        n0 += int((base & in_(s23, R23) & in_(s12, J26)).sum())
s12a, s23a, sda = map(np.array, (s12a, s23a, sda))
print(f"   Raster in phi: {STEP} Grad ({len(PHI)} Werte)")
if len(s12a) == 0: print("   (i) eps = 0, TM1-Klasse: auf diesem Raster KEIN Fall mit theta13 in 3 sigma (Fenster in phi etwa 1,3 Grad breit); Kontrolle (i) hier nicht auswertbar")
else: print(f"   (i) eps = 0, TM1-Klasse, theta13 in 3 sigma, TM1-Spalte als nu_1: {len(s12a)} Faelle; sin^2 12 in [{s12a.min():.4f}, {s12a.max():.4f}] (Formel [0.3172, 0.3196]);")
if len(s12a): print(f"       sin^2 23 in [{s23a.min():.6f}, {s23a.max():.6f}]; |sin delta| in [{sda.min():.6f}, {sda.max():.6f}]; Treffer im JUNO-2026-2-sigma-Bereich: {n0}")

def summarize(tag, rows):
    """rows: Liste (klasse, s12, s23, s13, |sin delta| oder None-Array)"""
    out = {}
    for kl in ('TM1', 'theta13=0'):
        sel = [r for r in rows if r[0] == kl]
        if not sel: continue
        s12 = np.concatenate([r[1] for r in sel]); s23 = np.concatenate([r[2] for r in sel]); s13 = np.concatenate([r[3] for r in sel]); sd = np.concatenate([r[4] for r in sel])
        b13 = in_(s13, R13); hit = b13 & in_(s23, R23) & in_(s12, J26); sharp = b13 & in_(s12, J26); dirn = b13 & in_(s23, R23)
        line = f"   {tag}, Klasse {kl}: Faelle {len(s12)}; theta13 in 3 sigma: {int(b13.sum())}; Treffer (13, 23 in 3 sigma, 12 in JUNO 2 sigma): {int(hit.sum())}"
        if hit.any():
            line += f"; davon 12 in JUNO 1 sigma: {int((hit & in_(s12, J26_1)).sum())}"
            line += f"\n      Treffer: sin^2 12 in [{s12[hit].min():.4f}, {s12[hit].max():.4f}], sin^2 23 in [{s23[hit].min():.4f}, {s23[hit].max():.4f}], |sin delta| in [{sd[hit].min():.3f}, {sd[hit].max():.3f}]"
        if sharp.any():
            line += f"\n      Schaerfe (13 in 3 sigma, 12 in JUNO 2 sigma): sin^2 23 in [{s23[sharp].min():.4f}, {s23[sharp].max():.4f}] (Breite {np.ptp(s23[sharp]):.4f}), |sin delta| in [{sd[sharp].min():.3f}, {sd[sharp].max():.3f}] (Breite {np.ptp(sd[sharp]):.3f})"
        if dirn.any():
            j = np.argmin(abs(s12[dirn] - JMEAN))
            line += f"\n      Richtung (13, 23 in 3 sigma): sin^2 12 in [{s12[dirn].min():.4f}, {s12[dirn].max():.4f}]; naechster Wert zu 0.3036: {s12[dirn][j]:.4f} (Abstand {abs(s12[dirn][j] - JMEAN):.4f}; ohne Korrektur 0.0136)"
        else:
            line += "\n      Richtung: kein Fall mit 13 und 23 in 3 sigma"
        print(line)
        out[kl] = dict(n=int(len(s12)), hit=int(hit.sum()), sharp23=float(np.ptp(s23[sharp])) if sharp.any() else None, sharpsd=float(np.ptp(sd[sharp])) if sharp.any() else None,
                       dist=float(np.min(abs(s12[dirn] - JMEAN))) if dirn.any() else None)
    return out
def sd_all(UE, UN):
    return abs(delta_of(UE, UN, np.ones((len(UE), len(UN)), bool))).reshape(len(UE), len(UN))

CB = [c for c in cand if c != 0.0]
gridB = sorted(set(list(np.round(np.arange(0, 0.7 + 1e-12, 0.02), 6)) + CB)); gridB = [e for e in gridB if e <= max(CB) + 1e-12]
def workB(job):
    """Variante B fuer ein (m1, p, sg, phi): Fortsetzung in eps wie k100, Eigenvektoren bei den Kandidaten."""
    m1, p, sg, phi = job
    tgt = nu(m1)/nu(m1).max(); den = np.where(tgt > 0, tgt, 1.0); Q = Qphi_odd(p, sg, phi); out = {c: [] for c in CB}
    for order in ORD:
        for sgs in itertools.product((1, -1), repeat=2):
            mu = np.zeros(3); sgn = (1,) + sgs
            for col, k in enumerate(order): mu[col] = sgn[col]*tgt[k]
            for e in gridB:
                D = np.diag(np.exp(e*Wl)); Mf = lambda x: D@Q@np.diag(x)@Q.T@D
                def f(x):
                    w = np.sort(abs(np.linalg.eigvalsh(Mf(x)))); return (w - tgt)/den
                r = least_squares(f, mu, method='lm', xtol=1e-14, ftol=1e-14, gtol=1e-14)
                if np.max(abs(r.fun)) > 1e-7: break
                mu = r.x
                if e in out:
                    w, V = np.linalg.eigh(Mf(mu)); o = np.argsort(abs(w)); out[e].append(V[:, o])
    return (p, sg), out

if __name__ == '__main__':
    import multiprocessing as mp
    RES = {}
    rowsA = {c: [] for c in CB}
    for c in CB:
        for (p, sg) in CASES:
            UN = unA(p, sg); s12, s23, s13 = angles(Ce[c], UN); sd = sd_all(Ce[c], UN)
            ok = np.isfinite(s12) & np.isfinite(s23) & np.isfinite(sd)
            rowsA[c].append((cls[(p, sg)], s12[ok], s23[ok], s13[ok], sd[ok]))
    jobs = [(m1, p, sg, phi) for m1 in M1 for (p, sg) in CASES for phi in PHI]
    with mp.Pool(mp.cpu_count()) as pool: resB = pool.map(workB, jobs, chunksize=8)
    rowsB = {c: [] for c in CB}; nB = {c: 0 for c in CB}
    for c in CB:
        for case in CASES:
            NB = [V for cs, out in resB if cs == case for V in out[c]]
            if not NB: continue
            nB[c] += len(NB); UNb = np.array(NB); s12, s23, s13 = angles(Ce[c], UNb); sd = sd_all(Ce[c], UNb)
            ok = np.isfinite(s12) & np.isfinite(s23) & np.isfinite(sd)
            rowsB[c].append((cls[case], s12[ok], s23[ok], s13[ok], sd[ok]))
    for c in CB:
        nm = cand[c]; print("=" * 78); print(f"{nm} ({c:.4f})")
        RES[(nm, 'A')] = summarize("Variante A", rowsA[c])
        print(f"   Variante B: {nB[c]} angepasste Neutrino-Matrizen")
        RES[(nm, 'B')] = summarize("Variante B", rowsB[c])
    print("=" * 78); print("Entscheidung (eps = artanh(beta_sym), Klasse TM1)")
    a = {v: RES[("eps = artanh(beta_sym)", v)].get('TM1', {}) for v in 'AB'}
    ha = any(a[v].get('hit', 0) > 0 for v in 'AB')
    hb = any(a[v].get('hit', 0) > 0 and a[v]['sharp23'] is not None and a[v]['sharp23'] < 0.05 and a[v]['sharpsd'] < 0.3 for v in 'AB')
    ds = [a[v]['dist'] for v in 'AB' if a[v].get('dist') is not None]
    hc = bool(ds) and min(ds) < 0.0136
    print(f"   H134a (Treffer in A oder B): {'bestaetigt' if ha else 'widerlegt'}")
    print(f"   H134b (Schaerfe): {('bestaetigt' if hb else 'widerlegt') if ha else 'nicht anwendbar'}")
    print(f"   H134c (Richtung): {'bestaetigt' if hc else 'widerlegt'}" + (f" (kleinster Abstand {min(ds):.4f})" if ds else " (kein Fall mit 13 und 23 in 3 sigma)"))
