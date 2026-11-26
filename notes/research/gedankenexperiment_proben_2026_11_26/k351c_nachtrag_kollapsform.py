"""k351c (nachtraeglich, nach dem Lauf von k351): Form des Kollapses. Kein Teil des Tests H160.
Frage: Welche Gestalt hat die Folge der Auslesepunkte, wenn die Radien gegen null laufen, und was sind die Laeufe 'anderes'?
Aufruf: python k351c_nachtrag_kollapsform.py > k351c_out.txt
"""
import itertools, importlib.util, io, contextlib, os
import numpy as np
spec = importlib.util.spec_from_file_location("k351", os.path.join(os.path.dirname(os.path.abspath(__file__)), "k351_test_h160.py"))
k = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(k)
ang = lambda A, B: np.degrees(np.arccos(np.clip(np.dot(A, B) / np.linalg.norm(A) / np.linalg.norm(B), -1, 1)))

def trace(P1, P2, rule, par, steps=400, floor=1e-12):
    rows = []
    for n in range(steps):
        N1, N2, ecc = k.step(P1, P2, rule, par)
        r1, r2 = np.linalg.norm(N1), np.linalg.norm(N2)
        if min(r1, r2) < floor: break
        rows.append((r1, r2, ang(N1, N2), r1 / np.linalg.norm(P1), r2 / np.linalg.norm(P2), np.linalg.norm(N1 - P1) + np.linalg.norm(N2 - P2)))
        P1, P2 = N1, N2
    return np.array(rows)

print("== 1  Grenzform im Kollaps (Regel B, 200 Zufallsstarts wie k351), ausgewertet solange beide Radien > 1e-12 ==")
rng = np.random.default_rng(20261126); lim = []
for i in range(200):
    a = [1.0, 2.0][i % 2]
    r1, r2 = rng.uniform(0.5, min(3.0, 2 * a * 0.999), 2); p1, p2 = rng.uniform(0, 2 * np.pi, 2)
    t = trace(r1 * np.array([np.cos(p1), np.sin(p1)]), r2 * np.array([np.cos(p2), np.sin(p2)]), "B", a, steps=60, floor=1e-12)
    if len(t) >= 4:
        # Schrumpffaktor ueber zwei Schritte gegen cos^4(Winkel/2)
        f2 = np.sqrt((t[-1, 0] * t[-1, 1]) / (t[-3, 0] * t[-3, 1]))
        lim.append((t[-1, 2], abs(t[-1, 2] - t[-2, 2]), f2, np.cos(np.radians(t[-1, 2]) / 2) ** 4, len(t)))
lim = np.array(lim)
print(f"  {len(lim)} von 200 Laeufen haben mindestens 4 Schritte oberhalb von 1e-12")
print(f"  Winkel zwischen den zwei Auslesepunkten am Ende: von {lim[:,0].min():.3f} bis {lim[:,0].max():.3f} Grad (kein gemeinsamer Wert);"
      f" Aenderung im letzten Schritt: Median {np.median(lim[:,1]):.2e}, max {lim[:,1].max():.2e} Grad")
q = np.percentile(lim[:, 0], [10, 25, 50, 75, 90]); print("  Quantile des Endwinkels (10, 25, 50, 75, 90 %):", np.round(q, 2))
rel = np.abs(lim[:, 2] / lim[:, 3] - 1)
print(f"  Schrumpffaktor ueber zwei Schritte gegen cos^4(Winkel/2): relative Abweichung Median {np.median(rel):.2e}, 90 %-Quantil {np.percentile(rel, 90):.2e}")

print("\n== 2  Parabel-Grenzfall (v^2 = 2/r, skalenfrei), symmetrischer Fall r1 = r2: Winkel bleibt, Radius mal cos^2(Winkel/2) ==")
def sym_map(D):
    P1 = np.array([np.cos(D / 2), np.sin(D / 2)]); P2 = np.array([np.cos(D / 2), -np.sin(D / 2)])
    out = []
    for A, B in ((P1, P2), (P2, P1)):
        d = (B - A) / np.linalg.norm(B - A); Pn, e = k.periapsis(A, d, np.sqrt(2.0)); out.append(Pn)
    swap = max(np.linalg.norm(out[0] / np.linalg.norm(out[0]) - P2), np.linalg.norm(out[1] / np.linalg.norm(out[1]) - P1))
    return np.linalg.norm(out[0]), np.radians(ang(out[0], out[1])), swap
worst = [0, 0, 0]
for D in np.radians(np.linspace(1, 179, 179)):
    fac, Dn, swap = sym_map(D)
    worst = [max(worst[0], abs(Dn - D)), max(worst[1], abs(fac - np.cos(D / 2) ** 2)), max(worst[2], swap)]
print(f"  179 Winkel von 1 bis 179 Grad: groesste Abweichung neuer Winkel - alter Winkel {worst[0]:.2e} rad; Faktor - cos^2(Winkel/2) {worst[1]:.2e};")
print(f"  neuer Punkt von Probe 1 liegt auf dem Strahl des alten Punkts von Probe 2 (und umgekehrt), Abweichung {worst[2]:.2e}")
print("  Herleitung: Parabel mit L = sqrt(2) cos(D/2), Periapsis q = L^2/2 = cos^2(D/2); aus 1 = 2q/(1 + cos f) folgt cos f = cos D, also f = D.")
for D in (30, 90, 120, 150, 179):
    print(f"    Winkel {D:3d} Grad: Radius je Schritt mal {np.cos(np.radians(D)/2)**2:.6f}; Schritte fuer einen Faktor 10: {np.log(10)/-np.log(np.cos(np.radians(D)/2)**2):.2f}")

print("\n== 3  Was sind die Laeufe 'anderes' und 'konvergent' der Regeln E und V? ==")
grid = list(itertools.product([0.5, 1, 2, 4], [1, 1.1, 1.5, 2], [0.5, 1, 2]))
for rule, pars in (("E", [None]), ("V", [0.5, 1, 2])):
    stat = {}
    for (b1, q, vinf), par in itertools.product(grid, pars):
        P1, P2 = k.start_points(b1, b1 * q, vinf); p = vinf if rule == "E" else par
        r = k.run(P1, P2, rule, p)
        r1, r2 = np.linalg.norm(r["P1"]), np.linalg.norm(r["P2"])
        N1, N2, _ = k.step(r["P1"], r["P2"], rule, p)
        moving = np.linalg.norm(N1 - r["P1"]) + np.linalg.norm(N2 - r["P2"])
        if r["kind"] == "Kollaps": key = "Kollaps"
        elif min(r1, r2) < 1e-6: key = "laeuft gegen null (langsam oder unter der Toleranz)"
        elif np.linalg.norm(r["P1"] - r["P2"]) < 1e-6: key = "zusammengelaufen, r > 0"
        elif moving < 1e-9: key = "steht, zwei getrennte Punkte"
        else: key = "bewegt sich noch, r > 0"
        stat.setdefault(key, []).append((b1, q, vinf, par, r1, r2, ang(r["P1"], r["P2"]) if min(r1, r2) > 0 else np.nan))
    print(f"  Regel {rule}:", {kk: len(v) for kk, v in stat.items()})
    for kk, v in stat.items():
        if kk != "Kollaps":
            for row in v[:4]:
                print(f"    {kk}: b1 = {row[0]}, b2/b1 = {row[1]}, v_inf = {row[2]}, v0 = {row[3]}: r1 = {row[4]:.6g}, r2 = {row[5]:.6g}, Winkel {row[6]:.4f} Grad")

print("\n== 4  Regel E, symmetrischer Start (b1 = b2 = 1, v_inf = 1): langsamer Kollaps ==")
P1, P2 = k.start_points(1, 1, 1.0); t = trace(P1, P2, "E", 1.0, steps=2000)
for n in (0, 1, 2, 5, 10, 50, 200, 1000, len(t) - 1):
    if n < len(t): print(f"    Schritt {n+1}: r1 = {t[n,0]:.6e}, r2 = {t[n,1]:.6e}, Winkel {t[n,2]:.6f} Grad, Faktor {t[n,3]:.6f}")
print(f"  r mal Schrittzahl am Ende: {t[-1,0]*len(t):.5f};  Winkel^2 mal Schrittzahl: {np.radians(t[-1,2])**2*len(t):.5f}  (r ~ 1/n, Winkel ~ n^(-1/2): die Punkte laufen zusammen und zugleich nach innen)")
