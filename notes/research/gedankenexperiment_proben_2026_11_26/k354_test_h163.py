"""k354 (H163): Minimalpunkte als neue Startpunkte; Kraft fuer die Kreisbahn; Schwung holen. GM = 1, Ebene.
K-a kleinster Abstand (Newton, Auslegungen T und P);  K-b Stoss und Zusatzkraft fuer die Kreisbahn;  K-c Schwung holen;
K-d Schwarzschild: Radius ohne noetige Zusatzkraft;  Erkundung: addierte Auslesen, Stoss an der Grenzbahn, Periheldrehung.
Aufruf: python k354_test_h163.py > k354_out.txt
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def rhs(gm):
    return lambda t, y: [y[2], y[3], -gm * y[0] / (y[0]**2 + y[1]**2)**1.5, -gm * y[1] / (y[0]**2 + y[1]**2)**1.5]
def integ(y0, T, gm=1.0, events=None, n=4000):
    return solve_ivp(rhs(gm), [0, T], y0, method="DOP853", rtol=1e-13, atol=1e-15, events=events, t_eval=np.linspace(0, T, n) if events is None else None)
def peri_state(pos, vel):
    """Punkt groesster Annaeherung der ganzen Bahn (beide Zeitrichtungen) ueber den Exzentrizitaetsvektor."""
    h = pos[0] * vel[1] - pos[1] * vel[0]; r = np.hypot(*pos)
    ev = np.array([vel[1] * h, -vel[0] * h]) - pos / r; e = np.hypot(*ev)
    return h * h / (1 + e) * ev / e, e
def rp_of(b, v):   # Hyperbel: Stossparameter b, Geschwindigkeit v im Unendlichen
    return (-1 + np.sqrt(1 + b * b * v**4)) / v**2

print("== K-a  kleinster Abstand (Newton) ==")
print("  Auslegung T (Fortsetzung): Start am Auslesepunkt mit der dortigen Geschwindigkeit")
worst = 0
for b in (0.25, 0.5, 1, 2, 4, 8):
    for v in (0.5, 1, 2):
        rp = rp_of(b, v); vp = np.sqrt(v * v + 2 / rp)
        p2, e = peri_state(np.array([rp, 0.0]), np.array([0.0, vp])); worst = max(worst, abs(np.hypot(*p2) - rp) / rp)
print(f"    18 Gitterpunkte: neuer Auslesepunkt = alter Auslesepunkt, groesste relative Abweichung {worst:.1e}  (die Bahn ist dieselbe; nichts wird kuerzer)")
print(f"    erster Auslesepunkt r_p(b, v) = (-1 + sqrt(1 + b^2 v^4))/v^2: fuer b -> 0 geht r_p -> 0, z. B. v = 1: " + ", ".join(f"b = {b:g}: {rp_of(b, 1):.3e}" for b in (1, 0.1, 0.01, 0.001)))
print("  Auslegung P (parallel): Start am Auslesepunkt, Betrag bleibt, Richtung = urspruengliche Einflugrichtung")
print("    Befund beim Umsetzen (nach der Vorab-Notiz): mit dieser Richtung laeuft die Probe vom Auslesepunkt weg nach aussen")
for b, v in ((1, 1), (4, 0.5), (0.5, 2)):
    rp = rp_of(b, v); e = np.sqrt(1 + b * b * v**4); vp = np.sqrt(v * v + 2 / rp)
    P = np.array([rp, 0.0]); phi = np.pi - np.arccos(-1 / e); d = np.array([np.cos(phi), np.sin(phi)])
    p2, e2 = peri_state(P, vp * d); bnew = abs(P[0] * d[1] - P[1] * d[0])
    print(f"    b = {b}, v = {v}: r_p = {rp:.6f}; radiale Geschwindigkeit am Neustart {vp * (P @ d) / rp:+.4f} (> 0: nach aussen); "
          f"die ganze Spur (auch rueckwaerts) hat b' = {bnew:.6f} (Formel r_p sqrt(1 - 1/e^2) = {rp * np.sqrt(1 - 1 / e**2):.6f}) und Kleinstabstand {np.hypot(*p2):.6f}")
print("    vorwaerts gerechnet bleibt der Auslesepunkt also stehen; nimmt man die ganze Spur (beide Richtungen), entsteht die Folge b -> b':")
for b0, v in ((1, 1), (4, 0.5), (8, 1), (8, 2)):
    b = b0; seq = []
    for n in range(200):
        rp = rp_of(b, v); seq.append(rp)
        if rp < 1e-12: break
        b = rp * np.sqrt(1 - 1 / (1 + b * b * v**4))
    print(f"      b = {b0}, v = {v}: Kleinstabstaende " + ", ".join(f"{x:.3e}" for x in seq[:6]) + (f" ... unter 1e-12 nach {len(seq)} Schritten" if seq[-1] < 1e-12 else f" ... nach 200 Schritten {seq[-1]:.3e}"))
print("  K-a: in T steht der erste Punkt, in P (ganze Spur) faellt die Folge gegen null; kein r_min > 0")

print("\n== K-b  Kraft fuer die Kreisbahn (Newton) ==")
cases = [(b, v, rp_of(b, v)) for b in (0.25, 0.5, 1, 2, 4, 8) for v in (0.5, 1, 2)] + [(None, 0, rp) for rp in (0.5, 1, 2)]
w1 = w2 = 0; rows = []
for b, v, rp in cases:
    vp = np.sqrt(v * v + 2 / rp); vc = np.sqrt(1 / rp); T = 2 * np.pi * rp**1.5
    s = integ([rp, 0, 0, vc], 5 * T); d1 = np.ptp(np.hypot(s.y[0], s.y[1])) / rp          # (i) Stoss: v_p -> v_c
    f = 1 + v * v * rp; T2 = 2 * np.pi * rp / vp
    s = integ([rp, 0, 0, vp], 5 * T2, gm=1 + f); d2 = np.ptp(np.hypot(s.y[0], s.y[1])) / rp  # (ii) Zusatzkraft f/r^2
    w1, w2 = max(w1, d1), max(w2, d2); rows.append((b, v, rp, vp / vc, np.sqrt(2 + v * v * rp), f, 0.5 * vp**2 - 0.5 * vc**2))
print(f"  {len(cases)} Faelle; Radiusschwankung ueber 5 Umlaeufe: nach dem Stoss hoechstens {w1:.1e}, mit Zusatzkraft hoechstens {w2:.1e}")
print("     b     v_inf   r_p        v_p/v_c    sqrt(2+v^2 r_p)   Zusatzkraft f (in Einheiten der Schwerkraft)   abzugebende Energie")
for b, v, rp, q, q2, f, dE in rows:
    if (b, v) in ((0.5, 1), (2, 1), (8, 1), (2, 2), (2, 0.5)) or b is None:
        print(f"    {'Parabel' if b is None else format(b, '<7g')} {v:<6g} {rp:<10.6f} {q:<10.6f} {q2:<17.6f} {f:<46.6f} {dE:.6f}")
print("  Einfall aus der Ruhe (v_inf = 0): v_p/v_c = sqrt(2), Zusatzkraft = 1 mal Schwerkraft (zusammen das Doppelte), abzugebende Energie = 1/(2 r_p) = Bindungsenergie der Kreisbahn")

print("\n== K-c  Schwung holen von der Kreisbahn (r = 1, v_c = 1) ==")
for k in (1.1, 1.2, 1.3, 1.4, np.sqrt(2), 1.5):
    E = 0.5 * k * k - 1
    if E < -1e-12:
        a = 1 / (2 - k * k); T = 2 * np.pi * a**1.5; s = integ([1, 0, 0, k], T, n=20001)
        r = np.hypot(s.y[0], s.y[1])
        print(f"  k = {k:.4f}: Energie {E:+.5f}, geschlossen: Abstand zum Startpunkt nach einem Umlauf {np.hypot(s.y[0][-1] - 1, s.y[1][-1]):.1e}; fernster Punkt {r.max():.6f} (Formel k^2/(2 - k^2) = {k*k/(2-k*k):.6f}); Umlaufzeit {T/(2*np.pi):.3f} Kreisumlaeufe")
    else:
        ev = lambda t, y: np.hypot(y[0], y[1]) - 1e4; ev.terminal = True
        s = integ([1, 0, 0, k], 1e9, events=ev); y = s.y[:, -1]; vr = (y[0] * y[2] + y[1] * y[3]) / np.hypot(y[0], y[1])
        vr_all = (s.y[0] * s.y[2] + s.y[1] * s.y[3]); print(f"  k = {k:.4f}: Energie {E:+.5f}, {'Parabel' if abs(E) < 1e-12 else 'Hyperbel'}: erreicht r = 1e4, radiale Geschwindigkeit dort {vr:.5f} (Formel {np.sqrt(max(2*E,0) + 2/1e4 - k*k/1e8):.5f}), kein Umkehrpunkt: {bool((vr_all[1:] > 0).all())}")
print("  Schwelle k = sqrt(2): genau der Stoss aus K-b rueckwaerts (Kreis -> Parabel braucht dieselbe Energie 1/(2r), die der Einfang abgegeben hat)")

print("\n== K-d  Schwarzschild, m = 0.05: Radius, an dem keine Zusatzkraft noetig ist ==")
m = 0.05
def bahn(E, L, licht=False):
    """u(phi) = 1/r von aussen (u = 0) nach innen; liefert Ausgang, Umlaeufe, innersten Radius."""
    f = (lambda p, y: [y[1], 3 * m * y[0]**2 - y[0]]) if licht else (lambda p, y: [y[1], m / L**2 + 3 * m * y[0]**2 - y[0]])
    du0 = 1 / L if licht else np.sqrt(max(E * E - 1, 0)) / L
    out = lambda p, y: y[0] - 0.02; out.terminal = True; out.direction = -1   # wieder draussen: r > 50 = 1000 m
    cap = lambda p, y: y[0] - 1 / (2 * m); cap.terminal = True
    s = solve_ivp(f, [0, 400], [0.0, du0], method="DOP853", rtol=1e-13, atol=1e-15, events=[out, cap], first_step=1e-6, max_step=0.05)
    return ("Einfang" if len(s.t_events[1]) else "entkommt"), s.t[-1] / (2 * np.pi), 1 / s.y[0].max()
print("  Kreisbahn bei r hat E^2 = (1 - 2m/r)^2/(1 - 3m/r), L^2 = m r^2/(r - 3m); gesucht r(E) mit der Energie der einfallenden Probe")
for E in (1.0, 1.1, 1.5, 3.0, None):
    if E is None:
        rc, Lc, name = 3 * m, 3 * np.sqrt(3) * m, "Licht"
    else:
        rc = 4 * m if E == 1 else brentq(lambda r: (1 - 2 * m / r)**2 / (1 - 3 * m / r) - E * E, 3 * m * (1 + 1e-12), 4 * m)
        Lc, name = np.sqrt(m * rc * rc / (rc - 3 * m)), f"E = {E}"
    line = f"  {name}: r(E) = {rc/m:.5f} m, kritischer {'Stossparameter' if E is None else 'Drehimpuls'} {Lc/m:.5f} m" + ("" if E in (None, 1.0) else f" (Stossparameter {Lc/np.sqrt(E*E-1)/m:.5f} m)")
    print(line)
    for d in (1e-2, 1e-4, 1e-6, 1e-8):
        o1, n1, r1 = bahn(E, Lc * (1 + d), E is None); o2, n2, r2 = bahn(E, Lc * (1 - d), E is None)
        print(f"      Abstand {d:.0e}: darueber {o1}, {n1:.3f} Umlaeufe, innerster Radius {r1/m:.6f} m;  darunter {o2}, {n2:.3f} Umlaeufe bis zum Horizont")
print("  Newton-Grenzfall zum Vergleich: dieselbe Rechnung ohne den Term 3 m u^2 hat keinen kritischen Wert (jede Probe mit L > 0 entkommt)")

print("\n== Erkundung ohne Kriterium ==")
print("  (1) Stoss an der Grenzbahn r = 4m (E = 1, L = 4m), Drehimpuls mal (1 + eps):")
def radial(L, r0, T):
    f = lambda t, y: [y[1], -m / y[0]**2 + L * L / y[0]**3 - 3 * m * L * L / y[0]**4, L / y[0]**2]
    far = lambda t, y: y[0] - 200 * m; far.terminal = True
    hor = lambda t, y: y[0] - 2.0001 * m; hor.terminal = True
    return solve_ivp(f, [0, T], [r0, 0.0, 0.0], method="DOP853", rtol=1e-12, atol=1e-14, events=[far, hor])
for eps in (1e-2, 1e-4, 1e-6, -1e-6, -1e-4, -1e-2):
    L = 4 * m * (1 + eps); s = radial(L, 4 * m, 1e5); E2 = (1 - 2 * m / (4 * m)) * (1 + L * L / (4 * m)**2)
    aus = "entkommt nach aussen" if len(s.t_events[0]) else ("faellt in den Horizont" if len(s.t_events[1]) else "bleibt")
    print(f"      eps = {eps:+.0e}: E = {np.sqrt(E2):.8f}, {aus} nach {s.y[2][-1]/(2*np.pi):.2f} Umlaeufen")
print("      nach aussen gestossen ist E knapp ueber 1: die Flucht ist im Grenzfall die Parabel; nach innen gestossen faellt die Probe hinein")
print("  (2) stabile Kreisbahnen gibt es erst ab r = 6m. Schwung holen von der Kreisbahn bei r = 20m, 100m, 400m (L mal k), gebundene Bahn schliesst nicht, sie dreht sich:")
for r0m, k in ((20, 1.02), (20, 1.05), (20, 1.1), (100, 1.05), (400, 1.05)):
    r0 = r0m * m; L = np.sqrt(m * r0 * r0 / (r0 - 3 * m)) * k
    f = lambda t, y: [y[1], -m / y[0]**2 + L * L / y[0]**3 - 3 * m * L * L / y[0]**4, L / y[0]**2]
    apo = lambda t, y: y[1]; apo.direction = 1
    s = solve_ivp(f, [0, 2e5], [r0, 0.0, 0.0], method="DOP853", rtol=1e-12, atol=1e-14, events=apo, dense_output=True)
    tp = [t for t in s.t_events[0] if t > 1e-6][0]; ymax = s.sol(tp / 2); dphi = s.sol(tp)[2] - 2 * np.pi
    ra, rpp = max(s.y[0].max(), ymax[0]), r0; a = (ra + rpp) / 2; e = (ra - rpp) / (ra + rpp)
    print(f"      r = {r0m} m, k = {k}: nah {rpp/m:.2f} m, fern {ra/m:.2f} m, Drehung des nahen Punkts je Umlauf {np.degrees(dphi):.2f} Grad (Naeherung 6 pi m/(a(1 - e^2)) = {np.degrees(6*np.pi*m/(a*(1-e*e))):.2f} Grad)")
print("  (3) addierte Auslesen: Summe der Orte zweier gegenlaeufiger Kreisbahnen, z(t) = r1 e^{i w1 t} + r2 e^{-i w2 t}, w = r^(-3/2)")
t = np.linspace(0, 400, 400001)
for r1, r2 in ((1, 1), (1, 1.5), (1, 1 / 0.30178)):
    w1, w2 = r1**-1.5, r2**-1.5; z = r1 * np.exp(1j * w1 * t) + r2 * np.exp(-1j * w2 * t)
    print(f"      r2/r1 = {r2/r1:.4f}: |z| zwischen {abs(z).min():.4f} und {abs(z).max():.4f} (|r1 - r2| = {abs(r1-r2):.4f}, r1 + r2 = {r1+r2:.4f}); groesster Abstand von der x-Achse {abs(z.imag).max():.4f}; "
          f"Achse der momentanen Ellipse dreht mit (w1 - w2)/2 = {(w1-w2)/2:+.4f}")
print("      gleiche Radien: eine Strecke durch den Kern (mu = 1, der Photonpunkt P aus H159). Ungleiche Radien: Ellipse mit mu = kleinerer/groesserer Radius, die sich dreht,")
print("      weil die zwei Kreise nach Kepler verschieden schnell laufen; ueber lange Zeit fuellt die Spur den Ring zwischen |r1 - r2| und r1 + r2.")
print("  (4) Faktor 2: Einfall aus der Ruhe braucht fuer die Kreisbahn die doppelte Schwerkraft (K-b); der Ablenkwinkel der ART ist das Doppelte des Newton-Werts (k353).")
print("      Beides sind Lehrbuchzahlen mit verschiedener Herkunft (Energiesatz bzw. Raumkruemmung); eine Verbindung wird hier nicht behauptet.")
