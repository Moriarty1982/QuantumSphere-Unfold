"""k90: Test der Vorab-Notiz H34 (Commit 8d8b761): CKM- und PMNS-Mischung aus der Maske von r47 mit einem gemeinsamen epsilon."""
import itertools, numpy as np
from scipy.optimize import least_squares

w3 = np.exp(2j*np.pi/3)
F = np.array([[w3**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
Wq = np.diag([0., -2., -1.]); Wl = np.diag([0., 0., -3.])
EPS = np.round(np.arange(0, 3.0 + 1e-12, 0.005), 6)
TOL = 1e-9

def M_of(lam, W, e):
    C = F@np.diag(lam)@F.conj().T
    return C + e*(W@C + C@W)

def eig_sorted(M):
    w, U = np.linalg.eigh(M)
    o = np.argsort(abs(w))
    return abs(w[o]), U[:, o]

def branches(masses, W):
    """Alle Zweige lambda(eps) fuer die Zielmassen; Rueckgabe: Liste von dicts eps -> U (Spalten nach Masse)."""
    m = np.array(masses, float); m = m/m.max()
    den = np.where(m > 0, m, 1.0)                       # m1 = 0: absolute statt relative Abweichung
    out = []
    starts = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            if s[0] == -1: continue                      # lambda -> -lambda ist dieselbe Loesung
            starts.append(np.array([s[i]*m[p[i]] for i in range(3)]))
    for lam in starts:
        br = {}
        for e in EPS:
            f = lambda x: (eig_sorted(M_of(x, W, e))[0] - m)/den
            r = least_squares(f, lam, method='lm', xtol=1e-15, ftol=1e-15, gtol=1e-15)
            if np.max(abs(r.fun)) > TOL: break
            lam = r.x
            br[e] = eig_sorted(M_of(lam, W, e))[1]
        out.append(br)
    return out

def ckm(V): a = abs(V); return a[0, 1], a[1, 2], a[0, 2]
def pmns(U):
    a = abs(U)**2; s13 = a[0, 2]
    return a[0, 1]/(1 - s13), a[1, 2]/(1 - s13), s13

mq = dict(u=[1.23e-3, 0.620, 168.26], d=[2.67e-3, 53.16e-3, 2.839])
me = [0.48307e-3, 101.766e-3, 1728.56e-3]
dm21, dm31 = 7.49e-5, 2.534e-3
M1 = [0, 0.001, 0.003, 0.01, 0.02, 0.05, 0.1]
CKM = np.array([0.2250, 0.0418, 0.00373])
R12, R23, R13 = (0.275, 0.345), (0.430, 0.596), (0.02023, 0.02376)

Bu, Bd = branches(mq['u'], Wq), branches(mq['d'], Wq)
print(f"Zweige: u {len(Bu)} (bis eps=3 durchgehend: {sum(len(b) == len(EPS) for b in Bu)}), d {len(Bd)} "
      f"({sum(len(b) == len(EPS) for b in Bd)})")

# H34a
total = 0; good = []
for e in EPS:
    for iu, bu in enumerate(Bu):
        if e not in bu: continue
        for id_, bd in enumerate(Bd):
            if e not in bd: continue
            total += 1
            v = np.array(ckm(bu[e].conj().T@bd[e]))
            if np.all(abs(v/CKM - 1) <= 0.2): good.append((e, iu, id_, v))
ok_a = len(good) > 0
eps_good = sorted(set(g[0] for g in good))
print(f"\nH34a: {len(good)} von {total} (eps, Zweigpaar)-Kombinationen innerhalb +-20 % ({100*len(good)/max(total,1):.3f} %);"
      f" eps-Werte: {eps_good[:12]}{' ...' if len(eps_good) > 12 else ''} -> {'bestaetigt' if ok_a else 'widerlegt'}")
best = min(((np.max(abs(np.array(ckm(bu[e].conj().T@bd[e]))/CKM - 1)), e, iu, id_)
            for e in EPS for iu, bu in enumerate(Bu) if e in bu for id_, bd in enumerate(Bd) if e in bd), key=lambda t: t[0])
bu, bd = Bu[best[2]], Bd[best[3]]
print(f"  bester Fall: max. relative Abweichung {best[0]:.3f} bei eps = {best[1]}: |V_us|, |V_cb|, |V_ub| = "
      f"{np.round(ckm(bu[best[1]].conj().T@bd[best[1]]), 5)} (Daten {CKM})")
for e0 in (0.0, 0.01, 0.1):
    vals = [np.array(ckm(bu.conj().T@bd)) for Bu_ in [Bu] for b1 in Bu_ for b2 in Bd
            for bu, bd in [(b1.get(e0), b2.get(e0))] if bu is not None and bd is not None]
    vals = np.array(vals)
    if len(vals) == 0:
        print(f"  eps = {e0}: keine Zweigpaare"); continue
    print(f"  eps = {e0}: Spannweite ueber alle Zweigpaare |V_us| [{vals[:,0].min():.2e}, {vals[:,0].max():.2e}],"
          f" |V_cb| [{vals[:,1].min():.2e}, {vals[:,1].max():.2e}], |V_ub| [{vals[:,2].min():.2e}, {vals[:,2].max():.2e}]")

# H34b, H34c
Be = branches(me, Wl)
lep = {}
for m1 in M1:
    mn = [m1, np.sqrt(m1**2 + dm21), np.sqrt(m1**2 + dm31)]
    lep[m1] = branches(mn, Wl)
ok_b = False; hits = []; ok_c = True; cmin = 9
for e in eps_good:
    th12q = max(np.arcsin(g[3][0]) for g in good if g[0] == e)
    for m1, Bn in lep.items():
        for ie, be in enumerate(Be):
            if e not in be: continue
            for inu, bn in enumerate(Bn):
                if e not in bn: continue
                s12, s23, s13 = pmns(be[e].conj().T@bn[e])
                if R12[0] <= s12 <= R12[1] and R23[0] <= s23 <= R23[1] and R13[0] <= s13 <= R13[1]:
                    ok_b = True; hits.append((e, m1, ie, inu, s12, s23, s13))
                big = max(np.arcsin(np.sqrt(min(x, 1))) for x in (s12, s23, s13))
                cmin = min(cmin, big - th12q)
                if big <= th12q: ok_c = False
print(f"\nH34b: {len(hits)} Treffer; m1-Werte mit Treffer: {sorted(set(h[1] for h in hits))}"
      + (f"; Beispiel eps = {hits[0][0]}, m1 = {hits[0][1]}: sin^2 = {np.round(hits[0][4:], 4)}" if hits else "")
      + f" -> {'bestaetigt' if ok_b else 'widerlegt'}")
print(f"\nH34c: " + ("kein eps erfuellt H34a, H34c zaehlt nicht" if not eps_good else f"kleinste Differenz (groesster PMNS-Winkel - theta12^CKM) = {cmin:.3f} rad") + " -> "
      f"{'bestaetigt' if (ok_c and ok_a) else 'widerlegt'}")

# Nachkontrolle (nach der Auswertung, kein Teil des Kriteriums; korrigiert war vorher nur die Ausgabe bei eps ohne Zweigpaar)
print("\nNachkontrolle 1: groesstes eps mit Loesung je Sektor (Zweigende):",
      {k: max(max(b) for b in B if b) for k, B in (("u", Bu), ("d", Bd), ("e", Be))},
      {f"nu(m1={m1})": max((max(b) for b in Bn if b), default=None) for m1, Bn in lep.items()})
near = [(e, iu, id_, np.array(ckm(bu[e].conj().T@bd[e]))) for e in EPS for iu, bu in enumerate(Bu) if e in bu
        for id_, bd in enumerate(Bd) if e in bd]
vus_ok = [n for n in near if abs(n[3][0]/CKM[0] - 1) <= 0.2]
print(f"Nachkontrolle 2: Kombinationen mit |V_us| in +-20 %: {len(vus_ok)}; dort |V_cb| in [{min(n[3][1] for n in vus_ok):.2e},"
      f" {max(n[3][1] for n in vus_ok):.2e}], |V_ub| in [{min(n[3][2] for n in vus_ok):.2e}, {max(n[3][2] for n in vus_ok):.2e}]"
      if vus_ok else "Nachkontrolle 2: keine Kombination mit |V_us| in +-20 %")
lhits = []
for m1, Bn in lep.items():
    for be in Be:
        for bn in Bn:
            for e in set(be) & set(bn):
                s12, s23, s13 = pmns(be[e].conj().T@bn[e])
                if R12[0] <= s12 <= R12[1] and R23[0] <= s23 <= R23[1] and R13[0] <= s13 <= R13[1]:
                    lhits.append((e, m1))
print(f"Nachkontrolle 3: Leptonen allein (eigenes eps): {len(lhits)} Treffer in den 3sigma-Bereichen; "
      f"eps-Bereich {min(h[0] for h in lhits) if lhits else '-'} bis {max(h[0] for h in lhits) if lhits else '-'}, "
      f"m1-Werte {sorted(set(h[1] for h in lhits))}")
def outside(x, R): return 0.0 if R[0] <= x <= R[1] else min(abs(x - R[0]), abs(x - R[1]))/((R[0] + R[1])/2)
bestl = (9, None)
for m1, Bn in lep.items():
    for be in Be:
        for bn in Bn:
            for e in set(be) & set(bn):
                v = pmns(be[e].conj().T@bn[e])
                if not np.all(np.isfinite(v)): continue
                d = max(outside(v[0], R12), outside(v[1], R23), outside(v[2], R13))
                if d < bestl[0]: bestl = (d, (e, m1, np.round(v, 4)))
print(f"Nachkontrolle 4: naechster Lepton-Fall: groesste relative Entfernung zum 3sigma-Bereich {bestl[0]:.2f} bei eps, m1, "
      f"(sin^2 12, 23, 13) = {bestl[1]}")
