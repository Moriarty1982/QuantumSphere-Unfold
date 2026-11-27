"""k421: Test H209. Spannungsgesetz der Bänder aus dem Überlapp; Paargewicht aus der Cayley-Dickson-Schachtelung.
Aufruf: python k421_test_h209.py > k421_out.txt"""
import itertools, math, numpy as np
from numpy.polynomial import legendre as L
from scipy.optimize import minimize
rng = np.random.default_rng(209)
names = ["R", "C", "H", "O", "S"]; dim = np.array([1.0, 2, 4, 8, 16]); P = list(itertools.combinations(range(5), 2))
targets = {"Oktant 90": 90.0, "Wuerfel 70.53": math.degrees(math.acos(1/3)), "Ikosaeder 63.43": math.degrees(math.acos(1/math.sqrt(5))),
           "Hopf 60": 60.0, "M 57.569": 57.569, "magisch 54.74": math.degrees(math.acos(1/math.sqrt(3))), "Koide 45": 45.0}
MAG = math.degrees(math.acos(1/math.sqrt(3)))
def unit(x): v = x.reshape(-1, 3); return v / np.linalg.norm(v, axis=1, keepdims=True)
def energy(x, W):
    v = unit(x); e = 0.0
    for i, j in P:
        c = abs(np.clip(v[i] @ v[j], -1, 1)); e += W[i, j] / max(math.sqrt(1 - c*c), 1e-9)
    return e
def solve(W, tries=600):
    res = []
    for _ in range(tries):
        r = minimize(energy, rng.standard_normal(15), args=(W,), method="BFGS", options={"maxiter": 800}); res.append(r)
    res.sort(key=lambda r: r.fun); best = res[0]
    nbest = sum(1 for r in res if r.fun < best.fun + 1e-6); second = next((r.fun for r in res if r.fun > best.fun + 1e-4), None)
    v = unit(best.x); return best.fun, np.degrees(np.arccos(np.clip(np.abs(v @ v.T), 0, 1))), v, nbest, second
def nearest(a):
    n, d = min(targets.items(), key=lambda kv: abs(kv[1]-a)); return n, abs(d-a)

print("== H209a (nicht blind): Ueberlappflaeche zweier Streifen auf der Sphaere gegen 2 a_i a_j / sin(theta) ==")
def overlap(alpha, theta, ns=400, nt=400000):
    n2 = np.array([math.sin(theta), 0.0, math.cos(theta)])       # Band 1: Normale z; Band 2: Normale um theta gekippt
    s, ws = np.polynomial.legendre.leggauss(ns); s = s * alpha; ws = ws * alpha
    t = (np.arange(nt) + 0.5) * 2 * math.pi / nt; ct = np.cos(t); area = 0.0
    for sk, wk in zip(s, ws):
        d = math.cos(sk) * ct * n2[0] + math.sin(sk) * n2[2]
        area += wk * math.cos(sk) * np.count_nonzero(np.abs(d) < math.sin(alpha)) * 2 * math.pi / nt
    return area
for adeg in (2.0, 5.0, 10.0):
    for tdeg in (90, 60, 45, 30, 15):
        al, th = math.radians(adeg), math.radians(tdeg); A = overlap(al, th); flat = 2 * (2*al)**2 / math.sin(th)
        print(f"   halbe Breite {adeg:4.1f} Grad, theta {tdeg:3d} Grad: Flaeche {A:.6f}, 2 a^2/sin = {flat:.6f}, Verhaeltnis {A/flat:.4f}")

def weights(kind):
    W = np.zeros((5, 5))
    for i, j in P:
        lo, hi = min(dim[i], dim[j]), max(dim[i], dim[j])
        W[i, j] = W[j, i] = {"N0": dim[i]*dim[j], "N1": lo, "N2": math.sqrt(lo/hi)}[kind]
    return W
LMAX = 80
def green(c, m2):
    co = np.zeros(LMAX + 1)
    for l in range(2, LMAX + 1, 2): co[l] = (2*l + 1)/2 * L.legval(0.0, [0]*l + [1]) / (l*(l + 1) + m2)
    return L.legval(c, co)
g = np.random.default_rng(1).standard_normal((100000, 3)); g /= np.linalg.norm(g, axis=1, keepdims=True)

out = {}
for kind, label in (("N0", "H192: w_ij = d_i d_j (Vergleich)"), ("N1", "w_ij = min(d_i, d_j)"), ("N2", "w_ij = sqrt(d_min/d_max)")):
    W = weights(kind); e, M, v, nb, sec = solve(W); out[kind] = (M, v)
    print(f"\n== {kind}: {label}, Gesetz 1/sin ==\n   Energie {e:.6f}; {nb} von 600 Starts im besten Minimum; naechstes anderes Minimum: {sec if sec is None else round(sec, 6)}")
    for i, j in P:
        nm, dd = nearest(M[i, j]); mark = "  <= vorab benannt" if {names[i], names[j]} in ({"O", "S"}, {"C", "H"}) else ""
        print(f"      {names[i]}-{names[j]}: {M[i,j]:6.2f} Grad  (w = {W[i,j]:7.3f}; naechster: {nm}, Abstand {dd:.2f}){mark}")
    os_, ch = M[3, 4], M[1, 2]; b_os = abs(os_ - 90) <= 1.0; b_ch = min(abs(ch - 57.569), abs(ch - MAG)) <= 1.0
    verd = "bestaetigt" if (b_os and b_ch) else ("teilweise" if b_os else "widerlegt")
    print(f"   vorab benannte Paare: O-S = {os_:.2f} (90 +- 1: {'ja' if b_os else 'nein'}); C-H = {ch:.2f} (57.569 oder 54.74 +- 1: {'ja' if b_ch else 'nein'})")
    print(f"   H209b [{kind}]: {verd}" if kind != "N0" else f"   (N0 ist der Vergleich mit H192: {verd})")
    # H209c: Kreuzenergie je Band = Staerke des Zugs bei erhaltenem Inhalt
    E = np.array([sum(W[i, j] / math.sin(math.radians(M[i, j])) for j in range(5) if j != i) for i in range(5)])
    print("   H209c: Kreuzenergie je Band E_i (Zug nach aussen, Anteil): " + ", ".join(f"{names[i]} {E[i]:.3f} ({E[i]/E.sum():.3f})" for i in range(5)))
    for m2 in (2.0, 6.0, 20.0):
        u = sum(E[i] * green(np.clip(g @ v[i], -1, 1), m2) for i in range(5)); k = u.argmax(); x = g[k]
        onb = sorted(range(5), key=lambda i: abs(x @ v[i]))[:2]
        print(f"      m2 = {m2:4.1f}: groesste Beule liegt auf den Baendern {names[onb[0]]} und {names[onb[1]]} "
              f"(|x.n| = {abs(x @ v[onb[0]]):.3f}, {abs(x @ v[onb[1]]):.3f}); Delle/Beule = {u.min()/u.max():+.3f}")

print("\n== H209d (Bericht): Treffer auf der Zielliste (+-1 Grad), nachtraeglich ausser den benannten Paaren ==")
for kind in ("N1", "N2"):
    M = out[kind][0]; hits = [(names[i]+"-"+names[j], round(M[i, j], 2), nearest(M[i, j])[0]) for i, j in P if nearest(M[i, j])[1] <= 1.0]
    print(f"   {kind}: {hits}")
print("   Skala: keine. Die Energie ist homogen in der Streifenbreite und im Feldbetrag; das Verhaeltnis Zug zu Elastizitaet der Flaeche bleibt frei.")
