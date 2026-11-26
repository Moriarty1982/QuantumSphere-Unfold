"""k351 (Test H160, teilweise nicht blind): iterierte Auslesen zweier Proben an einem Kern.
Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H160_Iterierte_Proben_Kreisbahn.md
Modell: Ebene, Punktmasse, GM = 1. Von P_i startet eine Probe in Richtung P_j; P_i' ist der Punkt groesster Annaeherung
auf der kuenftigen Bahn. Regeln fuer die Startgeschwindigkeit: E (Energie v_inf^2/2), V (feste v0), B (gebunden, E = -1/(2a)).
Aufruf: python k351_test_h160.py > k351_out.txt
"""
import itertools
import numpy as np
from scipy.integrate import solve_ivp

STEPS, TOL, RMIN = 400, 1e-9, 1e-9

def periapsis(P, d, v):
    """Punkt groesster Annaeherung der kuenftigen Bahn; gibt (Punkt, Exzentrizitaet)."""
    r = np.linalg.norm(P); rh = P / r
    vel = v * d
    L = P[0] * vel[1] - P[1] * vel[0]
    ev = np.array([vel[1] * L, -vel[0] * L]) - rh            # Exzentrizitaetsvektor v x L - r^
    e = np.linalg.norm(ev)
    E = v * v / 2 - 1 / r
    vr = float(np.dot(vel, rh))
    if abs(L) < 1e-14:                                       # radialer Sturz
        return (np.zeros(2), 1.0) if (vr < 0 or E < 0) else (P.copy(), 1.0)
    if vr >= 0 and E >= 0:                                   # nach aussen, ungebunden
        return P.copy(), e
    rp = L * L / (1 + e)
    if e < 1e-13:
        return P.copy(), e
    return rp * ev / e, e

def speed(rule, par, r):
    if rule == "E": return np.sqrt(par ** 2 + 2 / r)
    if rule == "V": return par
    val = 2 / r - 1 / par                                    # B: v^2 = 2/r - 1/a
    return np.sqrt(val) if val > 0 else 0.0

def step(P1, P2, rule, par):
    out, ecc = [], []
    for A, Bp in ((P1, P2), (P2, P1)):
        dv = Bp - A; n = np.linalg.norm(dv)
        if n < 1e-15:
            out.append(A.copy()); ecc.append(np.nan); continue
        v = speed(rule, par, np.linalg.norm(A))
        if v == 0.0:                                         # ausserhalb des erlaubten Bereichs: Probe faellt
            out.append(np.zeros(2)); ecc.append(1.0); continue
        Pn, e = periapsis(A, dv / n, v)
        out.append(Pn); ecc.append(e)
    return out[0], out[1], ecc

def run(P1, P2, rule, par, steps=STEPS, keep=False):
    hist = [(P1.copy(), P2.copy())]; ecc = [np.nan, np.nan]
    for n in range(steps):
        N1, N2, ecc_n = step(P1, P2, rule, par)
        if min(np.linalg.norm(N1), np.linalg.norm(N2)) < RMIN:
            return dict(kind="Kollaps", n=n + 1, P1=N1, P2=N2, ecc=ecc_n, hist=hist if keep else None)
        ch = max(np.linalg.norm(N1 - P1), np.linalg.norm(N2 - P2))
        P1, P2, ecc = N1, N2, ecc_n
        if keep: hist.append((P1.copy(), P2.copy()))
        if ch < TOL and n > 2:
            return dict(kind="konvergent", n=n + 1, P1=P1, P2=P2, ecc=ecc, hist=hist if keep else None)
    return dict(kind="anderes", n=steps, P1=P1, P2=P2, ecc=ecc, hist=hist if keep else None)

def start_points(b1, b2, vinf):
    """Punkte groesster Annaeherung zweier paralleler Strahlen (Richtung +x) mit Stossparametern +b1 und -b2."""
    pts = []
    for b, sgn in ((b1, 1.0), (b2, -1.0)):
        P0 = np.array([-1e6, sgn * b]); d = np.array([1.0, 0.0])
        L = P0[0] * 0 - P0[1] * vinf                      # x*vy - y*vx
        e = np.sqrt(1 + vinf ** 2 * L ** 2)                 # 1 + 2 E L^2 mit E = v_inf^2/2
        rp = L * L / (1 + e)
        # Richtung des Periapsis: Exzentrizitaetsvektor im Unendlichen, e_vec = v x L - r^, r^ = (-1, 0)
        vel = vinf * d
        ev = np.array([vel[1] * L, -vel[0] * L]) - np.array([-1.0, 0.0])
        pts.append(rp * ev / np.linalg.norm(ev))
    return pts[0], pts[1]

def summarize(name, results):
    kinds = [r["kind"] for r in results]; n = len(results)
    cnt = {k: kinds.count(k) for k in ("konvergent", "Kollaps", "anderes")}
    print(f"  {name}: {n} Laeufe; konvergent {cnt['konvergent']} ({100*cnt['konvergent']/n:.1f} %), Kollaps {cnt['Kollaps']} ({100*cnt['Kollaps']/n:.1f} %), anderes {cnt['anderes']}")
    conv = [r for r in results if r["kind"] == "konvergent"]
    if conv:
        sep = np.array([np.linalg.norm(r["P1"] - r["P2"]) for r in conv])
        rinf = np.array([np.linalg.norm(r["P1"]) for r in conv]); r2 = np.array([np.linalg.norm(r["P2"]) for r in conv])
        ec = np.array([np.nanmax(r["ecc"]) if not np.all(np.isnan(r["ecc"])) else np.nan for r in conv])
        nst = np.array([r["n"] for r in conv])
        print(f"    Endabstand |P1 - P2|: max {sep.max():.3e};  |r1 - r2| max {np.abs(rinf - r2).max():.3e};  Schritte bis Stillstand: Median {int(np.median(nst))}, max {nst.max()}")
        print(f"    r_inf: min {rinf.min():.5f}, Median {np.median(rinf):.5f}, max {rinf.max():.5f}")
        ok = ~np.isnan(ec)
        if ok.any():
            print(f"    e_inf: min {ec[ok].min():.5f}, Median {np.median(ec[ok]):.5f}, max {ec[ok].max():.5f};  Anteil e_inf < 1e-3: {100*np.mean(ec[ok] < 1e-3):.1f} %")
    return cnt, conv

print("== 0  Kontrolle des Bahnstuecks gegen direkte Integration ==")
def integrate_min(P, d, v, T=200.0):
    f = lambda t, y: [y[2], y[3], -y[0] / np.hypot(y[0], y[1]) ** 3, -y[1] / np.hypot(y[0], y[1]) ** 3]
    ev = lambda t, y: y[0] * y[2] + y[1] * y[3]; ev.direction = 1; ev.terminal = True
    s = solve_ivp(f, (0, T), [P[0], P[1], v * d[0], v * d[1]], events=ev, rtol=1e-12, atol=1e-13)
    return s.y_events[0][0][:2] if len(s.y_events[0]) else None
ctrl = [(np.array([1.5, 0.8]), np.array([-0.3, -1.0]), 1.4), (np.array([-0.7, 2.0]), np.array([0.9, -0.5]), 0.6), (np.array([2.0, 0.3]), np.array([-0.1, -1.0]), 0.5)]
for P, d, v in ctrl:
    d = d / np.linalg.norm(d); A, e = periapsis(P, d, v); Bn = integrate_min(P, d, v)
    print(f"  P = {P}, v = {v}: Formel {np.round(A, 9)}, e = {e:.6f}; Integration {np.round(Bn, 9)}; Differenz {np.linalg.norm(A - Bn):.2e}")

print("\n== 1  Regel E (Energie der urspruenglichen Probe) ==")
grid = list(itertools.product([0.5, 1, 2, 4], [1, 1.1, 1.5, 2], [0.5, 1, 2]))
resE = []
for b1, q, vinf in grid:
    P1, P2 = start_points(b1, b1 * q, vinf); resE.append(run(P1, P2, "E", vinf))
cntE, convE = summarize("Regel E", resE)

print("\n== 2  Regel V (feste Startgeschwindigkeit v0) ==")
resV, tagsV = [], []
for (b1, q, vinf), v0 in itertools.product(grid, [0.5, 1, 2]):
    P1, P2 = start_points(b1, b1 * q, vinf); resV.append(run(P1, P2, "V", v0)); tagsV.append(v0)
cntV, convV = summarize("Regel V", resV)
for v0 in (0.5, 1, 2):
    sub = [r for r, tg in zip(resV, tagsV) if tg == v0]; c = [r for r in sub if r["kind"] == "konvergent"]
    rr = [np.linalg.norm(r["P1"]) for r in c]
    print(f"    v0 = {v0}: Kreisradius 1/v0^2 = {1/v0**2:.4f}; konvergent {len(c)}/{len(sub)}" + (f", r_inf von {min(rr):.4f} bis {max(rr):.4f}, kleinster Wert von r_inf v0^2: {min(rr)*v0**2:.4f}" if rr else ""))

print("\n== 3  Regel B (gebunden, E = -1/(2a)), 200 Zufallsstarts ==")
rng = np.random.default_rng(20261126)
resB, tagsB = [], []
for k in range(200):
    a = [1.0, 2.0][k % 2]
    r1, r2 = rng.uniform(0.5, min(3.0, 2 * a * 0.999), 2); p1, p2 = rng.uniform(0, 2 * np.pi, 2)
    P1 = r1 * np.array([np.cos(p1), np.sin(p1)]); P2 = r2 * np.array([np.cos(p2), np.sin(p2)])
    resB.append(run(P1, P2, "B", a)); tagsB.append(a)
cntB, convB = summarize("Regel B", resB)
for a in (1.0, 2.0):
    c = [r for r, tg in zip(resB, tagsB) if tg == a and r["kind"] == "konvergent"]
    if c:
        rr = np.array([np.linalg.norm(r["P1"]) for r in c]); ee = np.array([np.nanmax(r["ecc"]) for r in c])
        print(f"    a = {a}: r_inf/a von {rr.min()/a:.4f} bis {rr.max()/a:.4f}; max |e_inf - (1 - r_inf/a)| = {np.max(np.abs(ee - (1 - rr / a))):.2e}")

print("\n== 4  K-c: Anziehung oder Kontinuum? ==")
for name, conv, rule in (("E", convE, "E"), ("V", convV, "V"), ("B", convB, "B")):
    if not conv: print(f"  Regel {name}: kein konvergenter Lauf"); continue
    devs = []
    pool = {"E": [(r, g[2]) for r, g in zip(resE, grid)], "V": [(r, t) for r, t in zip(resV, tagsV)], "B": [(r, t) for r, t in zip(resB, tagsB)]}[name]
    sel = [(r, p) for r, p in pool if r["kind"] == "konvergent"][:20]
    back, stay = 0, 0
    for r, par in sel:
        r0 = np.linalg.norm(r["P1"])
        Q1 = r["P1"] * (1 + 1e-3); Q2 = r["P2"] * (1 + 1e-3)
        # kleine Winkeltrennung, damit die Zielrichtung definiert ist
        ang = 1e-3; rot = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
        Q2 = rot @ Q2
        rr = run(Q1, Q2, rule, par)
        if rr["kind"] != "konvergent": devs.append(np.nan); continue
        dev = abs(np.linalg.norm(rr["P1"]) - r0); devs.append(dev)
        back += dev < 1e-6; stay += dev >= 1e-6
    devs = np.array(devs)
    print(f"  Regel {name}: {len(sel)} Endzustaende um 1e-3 versetzt: zurueck zum alten r_inf {back}, neuer Endwert {stay}, nicht konvergent {int(np.isnan(devs).sum())};"
          + (f" Abweichung Median {np.nanmedian(devs):.2e}, max {np.nanmax(devs):.2e}" if not np.all(np.isnan(devs)) else " keine Abweichung messbar"))

print("\n== 5  Beispiel-Lauf und addierte Auslesen (Regel B, a = 1) ==")
P1 = np.array([1.6, 0.5]); P2 = np.array([-1.2, 0.9])
ex = run(P1, P2, "B", 1.0, keep=True)
print(f"  Ausgang: {ex['kind']} nach {ex['n']} Schritten")
for n, (A, Bp) in enumerate(ex["hist"][:9]):
    print(f"    n = {n}: P1 = ({A[0]:+.6f}, {A[1]:+.6f}), r1 = {np.linalg.norm(A):.6f};  P2 = ({Bp[0]:+.6f}, {Bp[1]:+.6f}), r2 = {np.linalg.norm(Bp):.6f};  Winkel zwischen ihnen {np.degrees(np.arccos(np.clip(np.dot(A, Bp)/np.linalg.norm(A)/np.linalg.norm(Bp), -1, 1))):.4f} Grad")
allp = np.array([p for pair in ex["hist"] for p in pair]); rad = np.linalg.norm(allp, axis=1); ang = np.unwrap(np.arctan2(allp[:, 1], allp[:, 0]))
print(f"  alle {len(allp)} Auslesepunkte: Radius von {rad.min():.6f} bis {rad.max():.6f}; ueberstrichener Winkelbereich {np.degrees(ang.max() - ang.min()):.2f} Grad (ein Vollkreis waere 360)")
print(f"  Endbahn: e = {np.nanmax(ex['ecc']):.6f}, Periapsis r_inf = {np.linalg.norm(ex['P1']):.6f}, Apoapsis {2 - np.linalg.norm(ex['P1']):.6f}; beide Proben starten am selben Punkt in Gegenrichtung")

print("\n== 6  Erkundung ohne Kriterium: Schwarzschild-Variante u'' + u = 1/L^2 + 3 m u^2 ==")
def peri_gr(P, d, v, m):
    r = np.linalg.norm(P); rh = P / r; th = np.array([-rh[1], rh[0]])
    vr, vt = v * np.dot(d, rh), v * np.dot(d, th)
    L = r * vt
    if abs(L) < 1e-12: return np.zeros(2), "Einfang"
    sgn = np.sign(L); u0 = 1 / r; du0 = -(vr / abs(vt)) / r                 # du/dphi, phi in Laufrichtung
    f = lambda p, y: [y[1], -y[0] + 1 / L ** 2 + 3 * m * y[0] ** 2]
    peri = lambda p, y: y[1]; peri.direction = -1; peri.terminal = True       # u maximal
    cap = lambda p, y: y[0] - 1 / (2 * m); cap.terminal = True                # Horizont r = 2m
    esc = lambda p, y: y[0] - 1e-6; esc.direction = -1; esc.terminal = True
    s = solve_ivp(f, (0, 60), [u0, du0], events=[peri, cap, esc], rtol=1e-11, atol=1e-13, max_step=0.05)
    if len(s.t_events[1]): return np.zeros(2), "Einfang"
    if len(s.t_events[0]):
        ph = s.t_events[0][0]; u = s.y_events[0][0][0]
        if ph < 1e-9 and du0 <= 0: return P.copy(), "ok"
        a0 = np.arctan2(P[1], P[0]) + sgn * ph
        return (1 / u) * np.array([np.cos(a0), np.sin(a0)]), "ok"
    return P.copy(), "ok"                                                     # entweicht ohne weitere Annaeherung

def run_gr(P1, P2, rule, par, m, steps=60):
    for n in range(steps):
        new = []
        for A, Bp in ((P1, P2), (P2, P1)):
            dv = Bp - A; nn = np.linalg.norm(dv)
            if nn < 1e-13: new.append(A.copy()); continue
            v = speed(rule, par, np.linalg.norm(A))
            if v == 0.0: return "Einfang", n + 1, P1, P2
            Pn, st = peri_gr(A, dv / nn, v, m)
            if st == "Einfang": return "Einfang", n + 1, P1, P2
            new.append(Pn)
        ch = max(np.linalg.norm(new[0] - P1), np.linalg.norm(new[1] - P2)); P1, P2 = new
        if ch < 1e-7 and n > 2: return "konvergent", n + 1, P1, P2
    return "anderes", steps, P1, P2
rng = np.random.default_rng(20261126)
starts = []
for k in range(40):
    a = [1.0, 2.0][k % 2]
    r1, r2 = rng.uniform(0.5, min(3.0, 2 * a * 0.999), 2); p1, p2 = rng.uniform(0, 2 * np.pi, 2)
    starts.append((r1 * np.array([np.cos(p1), np.sin(p1)]), r2 * np.array([np.cos(p2), np.sin(p2)]), a))
newt = [run(P1, P2, "B", a)["kind"] for P1, P2, a in starts]
print(f"  40 Starts (die ersten 40 aus Abschnitt 3), Newton: konvergent {newt.count('konvergent')}, Kollaps {newt.count('Kollaps')}, anderes {newt.count('anderes')}")
for m in (0.01, 0.05):
    out = [run_gr(P1, P2, "B", a, m) for P1, P2, a in starts]
    k = [o[0] for o in out]
    rr = [np.linalg.norm(o[2]) for o in out if o[0] == "konvergent"]
    print(f"  m = {m}: konvergent {k.count('konvergent')}, Einfang {k.count('Einfang')}, anderes {k.count('anderes')}" + (f"; r_inf von {min(rr):.4f} bis {max(rr):.4f} (innerste stabile Kreisbahn bei 6 m = {6*m:.2f})" if rr else ""))

print("\n== 7  Erkundung ohne Kriterium: harter Kern, Radius R = 0.5 ==")
def run_core(P1, P2, rule, par, R=0.5, steps=STEPS):
    hits = 0
    for n in range(steps):
        new = []
        for A, Bp in ((P1, P2), (P2, P1)):
            dv = Bp - A; nn = np.linalg.norm(dv)
            if nn < 1e-15: new.append(A.copy()); continue
            v = speed(rule, par, np.linalg.norm(A))
            if v == 0.0: new.append(R * A / np.linalg.norm(A)); hits += 1; continue
            Pn, e = periapsis(A, dv / nn, v)
            if np.linalg.norm(Pn) < R:                                      # Bahn trifft die Oberflaeche: Auftreffpunkt
                vel = v * dv / nn; L = A[0] * vel[1] - A[1] * vel[0]
                if abs(L) < 1e-14: Pn = R * A / np.linalg.norm(A)
                else:
                    ev = np.array([vel[1] * L, -vel[0] * L]) - A / np.linalg.norm(A); ee = np.linalg.norm(ev)
                    cosf = np.clip((L * L / R - 1) / ee, -1, 1); fa = -np.sign(L) * np.arccos(cosf)   # vor dem Periapsis
                    w = np.arctan2(ev[1], ev[0]) + fa; Pn = R * np.array([np.cos(w), np.sin(w)])
                hits += 1
            new.append(Pn)
        ch = max(np.linalg.norm(new[0] - P1), np.linalg.norm(new[1] - P2)); P1, P2 = new
        if ch < TOL and n > 2: return "konvergent", n + 1, P1, P2, hits
    return "anderes", steps, P1, P2, hits
out = [run_core(P1, P2, "B", a) for P1, P2, a in starts]
k = [o[0] for o in out]; onsurf = [abs(np.linalg.norm(o[2]) - 0.5) < 1e-9 and abs(np.linalg.norm(o[3]) - 0.5) < 1e-9 for o in out]
ang = [np.degrees(np.arccos(np.clip(np.dot(o[2], o[3]) / np.linalg.norm(o[2]) / np.linalg.norm(o[3]), -1, 1))) for o in out]
print(f"  40 Starts: konvergent {k.count('konvergent')}, anderes {k.count('anderes')}; beide Endpunkte auf der Oberflaeche: {sum(onsurf)};"
      f" Winkel zwischen den Endpunkten: min {min(ang):.3f}, Median {np.median(ang):.3f}, max {max(ang):.3f} Grad")
oth = [o for o in out if o[0] == "anderes"]
if oth:
    o = oth[0]; print(f"  Beispiel 'anderes': r1 = {np.linalg.norm(o[2]):.6f}, r2 = {np.linalg.norm(o[3]):.6f}, Winkel {np.degrees(np.arccos(np.clip(np.dot(o[2], o[3])/np.linalg.norm(o[2])/np.linalg.norm(o[3]), -1, 1))):.3f} Grad, Treffer {o[4]}")
