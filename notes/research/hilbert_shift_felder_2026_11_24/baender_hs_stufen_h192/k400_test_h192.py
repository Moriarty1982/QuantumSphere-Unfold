"""k400: Test H192. Fünf Bänder (Großkreise auf S²) = HS-Stufen R,C,H,O,S; Gewicht = Dimension; Energie = sum_{i<j} w_i w_j / sin(theta_ij).
Aufruf: python k400_test_h192.py > k400_out.txt"""
import itertools, math, numpy as np
from scipy.optimize import minimize
rng = np.random.default_rng(11)
names = ["R", "C", "H", "O", "S"]; dim = np.array([1.0, 2, 4, 8, 16])
targets = {"Oktant 90": 90.0, "Wuerfel arccos(1/3) 70.53": math.degrees(math.acos(1/3)), "Ikosaeder arccos(1/sqrt5) 63.43": math.degrees(math.acos(1/math.sqrt(5))),
           "Hopf 60": 60.0, "Materie-Frame M 57.569": 57.569, "magisch arccos(1/sqrt3) 54.74": math.degrees(math.acos(1/math.sqrt(3))), "Koide/theta 45": 45.0}
def unit(x): v = x.reshape(-1, 3); return v / np.linalg.norm(v, axis=1, keepdims=True)
def energy(x, w, s):
    v = unit(x); e = 0.0
    for i, j in itertools.combinations(range(len(v)), 2):
        c = abs(np.clip(v[i] @ v[j], -1, 1)); sin = max(math.sqrt(1 - c*c), 1e-9); e += w[i]*w[j] / sin**s
    return e
def solve(w, s, n=5, tries=400):
    best = None
    for _ in range(tries):
        r = minimize(energy, rng.standard_normal(3*n), args=(w, s), method="BFGS", options={"maxiter": 500})
        if best is None or r.fun < best.fun - 1e-9: best = r
    v = unit(best.x); M = np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1))); return best.fun, M
def nearest(a):
    n, d = min(targets.items(), key=lambda kv: abs(kv[1]-a)); return n, abs(d-a)
def show(w, s, label, pred=False):
    e, M = solve(w, s); print(f"\n   [{label}] Gewicht {list(w.astype(int) if (w==w.astype(int)).all() else np.round(w,3))}, Gesetz 1/sin^{s}; Energie {e:.4f}")
    for i, j in itertools.combinations(range(5), 2):
        nm, dd = nearest(M[i, j]); mark = " <= vorab benannt" if pred and {names[i],names[j]} in ({"O","S"},{"C","H"}) else ""
        print(f"      {names[i]}-{names[j]}: {M[i,j]:6.2f} Grad  (naechster: {nm}, Abstand {dd:.2f}){mark}")
    return M

print("== H192a (nicht blind): gleiche Gewichte -> platonische Winkel ==")
Ma = show(np.ones(5), 1, "Kontrolle, alle gleich")
# fuer 5 Punkte ist die symmetrische Lage nicht platonisch; pruefe stattdessen die Teilmengen 3 und 4 mit gleichem Gewicht
def subset(n, s=1):
    e, M = solve(np.ones(n), s, n=n, tries=200); ang = sorted(M[i,j] for i,j in itertools.combinations(range(n),2)); return ang
print("   Kontrolle Teilmengen (k399 reproduziert):")
for n, exp in ((2,"90"),(3,"90"),(4,"70.53"),(6,"63.43")):
    ang = subset(n); print(f"      n = {n}: {np.round(ang,2)} (erwartet {exp})")

print("\n== H192b (Test): Gewicht = Dimension, Gesetz 1/sin ==")
Mb = show(dim, 1, "Test", pred=True)
os_ang = Mb[3,4]; ch_ang = Mb[1,2]
nm_os, d_os = nearest(os_ang); nm_ch, d_ch = nearest(ch_ang)
b_os = d_os <= 1.0 and abs(os_ang-90) <= 1.0
b_ch = min(abs(ch_ang-57.569), abs(ch_ang-math.degrees(math.acos(1/math.sqrt(3))))) <= 1.0
print(f"\n   vorab benannte Paare: O-S = {os_ang:.2f} (90 gefordert: {'ja' if b_os else 'nein'}); C-H = {ch_ang:.2f} (57.569 oder 54.74 gefordert: {'ja' if b_ch else 'nein'})")
verd = "bestaetigt" if (b_os and b_ch) else ("teilweise" if b_os else "widerlegt")
print(f"   H192b: {verd}")

print("\n== H192c (Robustheit): Gewicht und Gesetz variiert ==")
res = {}
for w, wl in ((dim,"dim"),(np.sqrt(dim),"sqrt(dim)")):
    for s in (1,2):
        _, M = solve(w, s); res[(wl,s)] = (M[3,4], M[1,2])
        print(f"   Gewicht {wl}, 1/sin^{s}: O-S = {M[3,4]:.2f}, C-H = {M[1,2]:.2f}")
os_vals = [v[0] for v in res.values()]; ch_vals = [v[1] for v in res.values()]
print(f"   Spannweite O-S {min(os_vals):.2f}..{max(os_vals):.2f}; C-H {min(ch_vals):.2f}..{max(ch_vals):.2f}")
print(f"   H192c: O-S {'stabil' if max(os_vals)-min(os_vals) < 3 else 'laeuft'} ueber die vier Wahlen; C-H {'stabil' if max(ch_vals)-min(ch_vals) < 3 else 'haengt von Gewicht/Gesetz ab'}")
