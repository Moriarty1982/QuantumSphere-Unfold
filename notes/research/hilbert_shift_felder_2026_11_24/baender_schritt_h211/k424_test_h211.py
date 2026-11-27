"""k424: Test H211. Normalen der Baender n_k = D^k n_0, D = Drehung um Schritt phi um eine Achse unter chi zu n_0.
Aufruf: python k424_test_h211.py > k424_out.txt"""
import itertools, math, numpy as np
from scipy.optimize import minimize_scalar
names5 = ["R", "C", "H", "O", "S"]; dim = np.array([1.0, 2, 4, 8, 16]); MAG = math.degrees(math.acos(1/math.sqrt(3)))
targets = {"90": 90.0, "70.53": math.degrees(math.acos(1/3)), "63.43": math.degrees(math.acos(1/math.sqrt(5))), "60": 60.0, "57.569": 57.569, "54.74": MAG, "45": 45.0}
def theta(chi, phi, s):            # Winkel zweier Baender mit Stufenabstand s (Grad); Band = ungerichtet, daher |cos|
    c = math.cos(chi)**2 + math.sin(chi)**2 * math.cos(s * phi); return math.degrees(math.acos(min(1.0, abs(c))))
def normals(chi, phi, n):
    return np.array([[math.sin(chi) * math.cos(k * phi), math.sin(chi) * math.sin(k * phi), math.cos(chi)] for k in range(n)])
def energy(chi, phi, W, power=1):
    n = len(W); e = 0.0
    for i, j in itertools.combinations(range(n), 2):
        t = math.radians(theta(chi, phi, j - i)); s = math.sin(t)
        if s < 1e-9: return 1e12
        e += W[i, j] / s**power
    return e
def wmat(kind, n=5):
    W = np.ones((n, n))
    if kind != "gleich":
        for i, j in itertools.combinations(range(n), 2):
            lo, hi = min(dim[i], dim[j]), max(dim[i], dim[j]); W[i, j] = W[j, i] = {"d_i d_j": dim[i]*dim[j], "min": lo, "sqrt(dmin/dmax)": math.sqrt(lo/hi)}[kind]
    return W
def best_chi(phi, W, power=1):
    grid = np.radians(np.linspace(1, 90, 1781)); E = [energy(c, phi, W, power) for c in grid]; k = int(np.argmin(E))
    lo, hi = grid[max(k - 2, 0)], grid[min(k + 2, len(grid) - 1)]
    r = minimize_scalar(energy, bounds=(lo, hi), args=(phi, W, power), method="bounded", options={"xatol": 1e-10}); return r.x, r.fun
def near(a):
    n, d = min(targets.items(), key=lambda kv: abs(kv[1] - a)); return (n, abs(d - a))
def line(chi, phi, n=5): return "  ".join(f"s={s}: {theta(chi, phi, s):6.2f}" for s in range(1, n))

PHI = math.radians(45)
print("== H211a (nicht blind): Schritt 45 Grad, Winkel nach Stufenabstand s (s=1: RC, CH, HO, OS; s=2: RH, CO, HS; s=3: RO, CS; s=4: RS) ==")
for lab, chi in (("chi = magischer Winkel 54.7356", math.radians(MAG)), ("chi = 45", math.radians(45)), ("chi = 90", math.radians(90)), ("chi = 57.569 (Materie-Frame)", math.radians(57.569))):
    print(f"   {lab}: {line(chi, PHI)}")
v = normals(math.radians(MAG), PHI, 5); M = np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1)))
print("   Kontrolle ueber die Normalen (chi magisch): " + "  ".join(f"{names5[i]}{names5[j]} {M[i,j]:.2f}" for i, j in itertools.combinations(range(5), 2)))

print("\n== H211b (Test, nicht blind): Neigung chi* aus dem Minimum der Abstossung, Schritt 45 Grad, gleiches Gewicht, Gesetz 1/sin ==")
chi, e = best_chi(PHI, wmat("gleich")); cd = math.degrees(chi)
print(f"   chi* = {cd:.4f} Grad, Energie {e:.6f}; {line(chi, PHI)}")
for lab, c0 in (("54.7356", MAG), ("45", 45.0), ("90 (R und S fallen zusammen)", 89.999)):
    print(f"   zum Vergleich Energie bei chi = {lab}: {energy(math.radians(c0), PHI, wmat('gleich')):.6f}")
print(f"   Energie der freien Lage von fuenf gleichen Baendern (k399/H192a): 11.0254; die Schraube liegt um {e - 11.0254:.4f} hoeher")
b1, b2 = abs(cd - MAG) <= 1, abs(cd - 45) <= 1
print(f"   chi* bei 54.736 +- 1: {'ja' if b1 else 'nein'}; bei 45 +- 1: {'ja' if b2 else 'nein'}")
print(f"   H211b: {'bestaetigt' if b1 else ('teilweise' if b2 else 'widerlegt')}")
print("   Treffer der Winkel bei chi* auf der Zielliste (+-1, nachtraeglich): " + str([(s, round(theta(chi, PHI, s), 2), near(theta(chi, PHI, s))[0]) for s in range(1, 5) if near(theta(chi, PHI, s))[1] <= 1]))

print("\n== H211c (Bericht): chi* fuer andere Gewichte und Gesetz 1/sin^2, Schritt 45 Grad ==")
vals = []
for kind in ("gleich", "d_i d_j", "min", "sqrt(dmin/dmax)"):
    for p in (1, 2):
        c, e = best_chi(PHI, wmat(kind), p); vals.append(math.degrees(c))
        print(f"   Gewicht {kind:16s} Gesetz 1/sin^{p}: chi* = {math.degrees(c):7.3f}; {line(c, PHI)}")
print(f"   Spannweite von chi*: {min(vals):.2f} bis {max(vals):.2f} Grad -> {'haengt an der Setzung' if max(vals) - min(vals) > 3 else 'stabil'}")

print("\n== H211d (Stichprobe): andere Schritte und acht Baender, gleiches Gewicht, Gesetz 1/sin ==")
for n in (5, 8):
    for pd in (22.5, 45.0, 60.0, 72.0, 90.0, 120.0):
        phi = math.radians(pd)
        if any(abs((s * pd) % 360) < 1e-9 for s in range(1, n)):
            print(f"   {n} Baender, Schritt {pd:5.1f}: Baender fallen fuer jedes chi zusammen (s * Schritt = 360), keine Lage"); continue
        c, e = best_chi(phi, np.ones((n, n))); hits = [(s, round(theta(c, phi, s), 2), near(theta(c, phi, s))[0]) for s in range(1, n) if near(theta(c, phi, s))[1] <= 1]
        print(f"   {n} Baender, Schritt {pd:5.1f}: chi* = {math.degrees(c):7.3f}, E = {e:9.4f}; {line(c, phi, n)}; Treffer: {hits}")
