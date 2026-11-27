"""k399 (Erkundung, kein Test): Moebiusband, Band am Aequator, mehrere Baender gleichzeitig auf der Sphaere, Baender als Stufen des HS-Turms.
Aufruf: python k399_baender_sphaere.py > k399_out.txt"""
import math, itertools, numpy as np
from scipy.optimize import minimize
from scipy.special import gamma as G
rng = np.random.default_rng(7)

print("== 1 Moebiusband und Torus (Zahlenprobe zu bekannter Geometrie) ==")
# Moebiusband: Mittellinie = Kreis; Rand laeuft zweimal um. Schlauch um die Mittellinie = Torus; der Rand ist darauf eine (2,1)-Kurve.
t = np.linspace(0, 4 * np.pi, 400001); R, w = 1.0, 0.3
edge = np.array([(R + w * np.cos(t / 2)) * np.cos(t), (R + w * np.cos(t / 2)) * np.sin(t), w * np.sin(t / 2)])
print(f"   Rand des Moebiusbands (Halbbreite {w}): schliesst sich nach t = 4 pi (Abstand Anfang-Ende {np.linalg.norm(edge[:, 0] - edge[:, -1]):.1e}), nach 2 pi noch nicht ({np.linalg.norm(edge[:, 0] - edge[:, 100000]):.3f})")
rho = np.hypot(np.hypot(edge[0], edge[1]) - R, edge[2]); print(f"   der Rand liegt auf dem Torus mit Schlauchradius {w}: Abstand von der Mittellinie {rho.min():.6f} bis {rho.max():.6f}")
wind_long = (np.unwrap(np.arctan2(edge[1], edge[0]))[-1]) / (2 * np.pi); wind_mer = (np.unwrap(np.arctan2(edge[2], np.hypot(edge[0], edge[1]) - R))[-1]) / (2 * np.pi)
print(f"   Windungszahlen des Rands auf diesem Torus: {wind_long:.3f} mal lang herum, {wind_mer:.3f} mal um den Schlauch: eine (2,1)-Kurve")
print("   Also: Moebiusband mit Dicke = Volltorus; seine Oberflaeche ist ein Torus. Zwei Moebiusbaender am Rand verklebt = Kleinsche Flasche (bekannt, nicht gerechnet).")

print("\n== 2 Band auf der Sphaere der Feldzustaende und sein Urbild in S^3 (Hopf) ==")
# Punkt in S^3: (cos(th/2) e^{i p1}, sin(th/2) e^{i p2}); Hopf-Bild hat Polwinkel th. Urbild des Breitenkreises th = Torus.
def torus_area(th, n=400):
    p1, p2 = np.meshgrid(np.linspace(0, 2 * np.pi, n, endpoint=False), np.linspace(0, 2 * np.pi, n, endpoint=False), indexing="ij")
    X = np.stack([np.cos(th / 2) * np.cos(p1), np.cos(th / 2) * np.sin(p1), np.sin(th / 2) * np.cos(p2), np.sin(th / 2) * np.sin(p2)])
    d1 = (np.roll(X, -1, 1) - X); d2 = (np.roll(X, -1, 2) - X)
    g11, g22, g12 = (d1 * d1).sum(0), (d2 * d2).sum(0), (d1 * d2).sum(0); return np.sqrt(np.clip(g11 * g22 - g12 ** 2, 0, None)).sum()
print("   Polwinkel   Laenge des Bands / 2 pi   Torusflaeche numerisch   2 pi^2 sin(th)")
for deg in (10, 30, 54.7356, 57.569, 60, 90):
    th = math.radians(deg); print(f"   {deg:8.3f}   {math.sin(th):22.6f}   {torus_area(th):22.5f}   {2 * math.pi ** 2 * math.sin(th):14.5f}")
print("   Befund: Laenge des Bands und Flaeche seines Torus gehen beide wie sin(th); beide sind am Aequator maximal (Clifford-Torus, Flaeche 2 pi^2).")
gL = 1.8646997646
print(f"   Einordnung der Frames (r70: R am Pol, M bei b_C = 1/gamma_L): Polwinkel von M = {math.degrees(math.acos(1 / gL)):.3f} Grad, sin = {math.sqrt(1 - 1 / gL ** 2):.6f};")
print(f"   am Hopf-Punkt (b = 1/2, k395): 60 Grad, sin = {math.sqrt(3) / 2:.6f} = sqrt(3)/2 (dieselbe Zahl wie sqrt(j(j+1)) fuer j = 1/2; nachtraeglich bemerkt, kein Befund).")
print(f"   Vektormodell des Spins 1/2: cos(th) = m/sqrt(j(j+1)) = 1/sqrt(3), th = {math.degrees(math.acos(1 / math.sqrt(3))):.4f} Grad; 1/sqrt(3) ist beta am Hopf-Punkt.")

print("\n== 3 Ein Band abseits des Aequators: wie muss sich die Flaeche verformen? ==")
print("   Setzung: Das Band hat die feste Laenge L = 2 pi (maximal gedehnt). Es liegt beim Polwinkel th einer Drehflaeche (Sphaeroid mit Halbachsen a, a, c).")
print("   Bedingung 'Weg wieder maximal': der Breitenkreis des Bands ist der laengste, also der Aequator des Sphaeroids, mit Umfang 2 pi a = L, d. h. a = 1.")
print("   Die Sphaere dreht also nur ihre Achse zum Band (kostet nichts) oder, wenn die Achse festgehalten wird, verformt sie sich:")
for deg in (90, 75, 60, 57.569, 45, 30):
    th = math.radians(deg)
    # Flaeche mit festem Volumen 4 pi/3, Drehflaeche r(z) so, dass der Kreis in Hoehe z0 = cos(th) den Radius 1 hat: einfachstes Modell Sphaeroid, Mittelpunkt nach z0 verschoben
    # Sphaeroid a = 1 (Band = Aequator des verschobenen Sphaeroids), Volumen fest: c = 1; die Form bleibt eine Kugel, nur ihr Mittelpunkt wandert um cos(th).
    print(f"      th = {deg:6.2f}: Band-Laenge auf der ruhenden Kugel {math.sin(th):.4f} * 2 pi; noetige Verschiebung des Kugelmittelpunkts {math.cos(th):.4f} (oder Dehnung des Breitenkreises um den Faktor {1 / math.sin(th):.4f})")
print("   Befund: Ein einzelnes Band erzwingt keine neue Form. Die Kugel kann sich immer so legen, dass das Band ihr Aequator ist. Zahlen entstehen erst, wenn mehrere Baender")
print("   gleichzeitig maximal sein wollen und sich dabei stoeren.")

print("\n== 4 Mehrere Baender gleichzeitig: Grosskreise, die sich moeglichst wenig stoeren ==")
print("   Je zwei Grosskreise schneiden sich in zwei Gegenpunkten. Alle n Baender koennen also gleichzeitig maximal lang sein, aber nicht kreuzungsfrei.")
print("   Setzung: Die Baender stossen sich ab; Energie = Summe ueber Paare von 1/sin^s(Winkel zwischen den Ebenen), s = 1 und s = 2 (zwei Gesetze, um die Abhaengigkeit zu sehen).")
def normals(x): v = x.reshape(-1, 3); return v / np.linalg.norm(v, axis=1)[:, None]
def energy(x, wts, s):
    v = normals(x); e = 0.0
    for i, j in itertools.combinations(range(len(v)), 2):
        c = abs(v[i] @ v[j]); e += wts[i] * wts[j] / max(1 - c * c, 1e-12) ** (s / 2)
    return e
def best(n, wts, s, tries=60):
    out = None
    for _ in range(tries):
        r = minimize(energy, rng.standard_normal(3 * n), args=(wts, s), method="BFGS")
        if out is None or r.fun < out.fun - 1e-10: out = r
    v = normals(out.x); ang = sorted(math.degrees(math.acos(min(1, abs(v[i] @ v[j])))) for i, j in itertools.combinations(range(n), 2)); return out.fun, ang, v
for n in (2, 3, 4, 5, 6):
    for s in (1, 2):
        e, ang, _ = best(n, np.ones(n), s); uniq = sorted(set(round(a, 2) for a in ang))
        print(f"   n = {n}, s = {s}: Winkel zwischen den Baendern (Grad): {', '.join(f'{a:.2f}' for a in ang)}")
print(f"   Vergleichswerte: 3 Baender senkrecht = Koordinatenebenen (acht Oktanten); 4 Baender: arccos(1/3) = {math.degrees(math.acos(1 / 3)):.2f}; 6 Baender: arccos(1/sqrt(5)) = {math.degrees(math.acos(1 / math.sqrt(5))):.2f}")
print("   Befund: Fuer 2, 3, 4 und 6 gleiche Baender ist die Lage eindeutig und haengt nicht vom Abstossungsgesetz ab (Symmetrie: Kreuz, Oktaeder, Wuerfel-Diagonalen, Ikosaeder).")
print("   Fuer 5 gleiche Baender gibt es keine solche Lage; die Winkel haengen vom Gesetz ab.")

print("\n== 5 Jedes Band eine Stufe des HS-Turms: Gewichte nach Dimension (1, 2, 4, 8, 16) ==")
dims = np.array([1.0, 2, 4, 8, 16]); names = ["R (HS0)", "C (HS1)", "H (HS2)", "O (HS3)", "S (HS4)"]
for label, wts in (("Gewicht = Dimension", dims), ("Gewicht = Wurzel der Dimension", np.sqrt(dims)), ("alle gleich", np.ones(5))):
    for s in (1, 2):
        e, ang, v = best(5, wts, s, tries=120); M = np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1)))
        pairs = ", ".join(f"{names[i][0]}{names[j][0]} {M[i, j]:.1f}" for i, j in itertools.combinations(range(5), 2))
        print(f"   {label}, s = {s}: {pairs}")
print("   Befund: Die schweren Baender (O, S) stellen sich nahezu senkrecht; die leichten ordnen sich danach ein. Die Winkel haengen vom Gewicht und vom Gesetz ab:")
print("   ohne hergeleitetes Abstossungsgesetz liefert das Bild keine Zahl.")

print("\n== 6 Hopf-Faserungen des Turms (bekannte Mathematik, hier nur die Zahlen) ==")
def vol(n): return 2 * math.pi ** ((n + 1) / 2) / G((n + 1) / 2)       # Volumen der Einheits-S^n
print("   Stufe   Faserung            Urbild des Aequators        Volumen des Urbilds beim Polwinkel th (relativ zum Aequator)")
for name, n, tot, fib in (("R", 1, 1, 0), ("C", 2, 3, 1), ("H", 4, 7, 3), ("O", 8, 15, 7)):
    print(f"   {name}       S^{tot} -> S^{n}, Faser S^{fib}    S^{n - 1} x S^{fib}{'':14s} sin^{n - 1}(th): bei 60 Grad {math.sin(math.radians(60)) ** (n - 1):.5f}, bei 57.569 Grad {math.sin(math.radians(57.569)) ** (n - 1):.5f}")
print("   S (Sedenionen): keine Hopf-Faserung (Adams 1960: nur Dimension 1, 2, 4, 8); die Sedenionen haben Nullteiler.")
print("   Stufe R ist das Moebiusband selbst: S^1 -> S^1 mit Faser aus zwei Punkten ist der Rand, der zweimal umlaeuft (Teil 1).")
print("   Stufe C ist der Torus ueber dem Band (Teil 2). Die Folge 'Moebiusband, Torus, ...' ist also die Folge der Hopf-Faserungen, und sie endet bei O.")
