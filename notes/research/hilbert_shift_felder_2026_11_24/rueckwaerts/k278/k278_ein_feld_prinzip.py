"""k278 (Erkundung, nicht blind, 24.11.2026): Legt ein Ein-Feld-Prinzip die Koeffizienten des Flavon-Potentials fest?
Frage aus r60.5: Mit gemischten Invarianten von X und CX ist die Ausrichtung (Z3 oder Z2) koeffizientenabhaengig. Hier geprueft:
A  Ein Feld Z_a = X(v) + a C X(v) (ein einziges Element der Albert-Algebra, a beliebig): alle Invarianten haengen nur von |v|^2 und xyz ab.
B  Zwei unabhaengige Felder (X und CX getrennt, oder zwei Flavons v, w): sum v^4 tritt auf.
C  Dynamik wie k274 auf dem Ein-Feld-Raum: gedaempfter Gradientenfluss von V = -mu^2/2 Tr Z^2 + kappa N(Z) + lam/4 Tr(Z^2 o Z^2)
   aus Zufallsstarts -> Ausrichtung.
D  Kein Z2 mit einem Feld: haengt V nicht von xyz ab, ist das Vakuum entartet (ganze Sphaere).
Benutzt die Albert-Algebra aus ../h127/k276_test_h127.py. Aufruf aus diesem Ordner: python3 k278_ein_feld_prinzip.py
"""
import contextlib
import io
import os
import runpy

import numpy as np
from scipy.integrate import solve_ivp

here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(os.path.join(here, '..', 'h127', 'k276_test_h127.py'))
jordan, S, Si, C = ns['jordan'], ns['S'], ns['Si'], ns['C']
Corig = Si @ C @ S
N = 27
rng = np.random.default_rng(278)
tr = lambda X: X[:3].sum()


def det(X):
    X2 = jordan(X, X); X3 = jordan(X2, X)
    return tr(X3) / 3 - tr(X) * tr(X2) / 2 + tr(X) ** 3 / 6


def X_of(v):
    x = np.zeros(N); x[10], x[18], x[26] = v; return x


def Z_of(v, a):
    X = X_of(v); return X + a * (Corig @ X)


def fit(vals, vs):
    A = np.array([[(v @ v) ** 2, (v ** 4).sum()] for v in vs])
    c = np.linalg.lstsq(A, np.array(vals), rcond=None)[0]
    return c, np.abs(A @ c - np.array(vals)).max()


print("=" * 78)
print("A  Ein Feld Z_a = X(v) + a C X(v): Invarianten")
vs = [rng.normal(size=3) for _ in range(20)]
for a in (0.0, 0.5, 1.0, -2.0, 3.7):
    t2 = [tr(jordan(Z_of(v, a), Z_of(v, a))) for v in vs]
    nz = [det(Z_of(v, a)) for v in vs]
    t4 = []
    for v in vs:
        Z = Z_of(v, a); Z2 = jordan(Z, Z); t4.append(tr(jordan(Z2, Z2)))
    c2 = np.polyfit([v @ v for v in vs], t2, 1)
    cn = np.linalg.lstsq(np.array([[np.prod(v)] for v in vs]), np.array(nz), rcond=None)[0][0]
    rn = max(abs(n - cn * np.prod(v)) for n, v in zip(nz, vs))
    c4, r4 = fit(t4, vs)
    print(f"   a={a:+.1f}: Tr Z^2 = {c2[0]:.4f}|v|^2 (Achse {c2[1]:.1e});  N(Z) = {cn:+.4f} v1v2v3 (Rest {rn:.1e});"
          f"  Tr(Z^2 o Z^2) = {c4[0]:+.4f}|v|^4 {c4[1]:+.4f} sum v^4 (Rest {r4:.1e})")
print("   Lesart: N(Z_a) = 2(3a - a^3) xyz, Tr(Z^2 o Z^2) isotrop. Ein Element einer kubischen Jordan-Algebra hat nur die")
print("   Invarianten Tr, Tr(.)^2, N; jede Potenzspur ist ein Polynom darin (Cayley-Hamilton Z^3 - T Z^2 + S Z - N = 0).")
Z = Z_of(rng.normal(size=3), 0.8); Z2 = jordan(Z, Z); Z3 = jordan(Z2, Z)
T, S2 = tr(Z), (tr(Z) ** 2 - tr(Z2)) / 2
print(f"   Kontrolle Cayley-Hamilton: |Z^3 - T Z^2 + S Z - N 1| = "
      f"{np.abs(Z3 - T * Z2 + S2 * Z - det(Z) * np.concatenate([[1, 1, 1], np.zeros(24)])).max():.1e}")

print("=" * 78)
print("B  Zwei unabhaengige Felder")
t_mix = []
for v in vs:
    X = X_of(v); Y = Corig @ X; XY = jordan(X, Y); t_mix.append(tr(jordan(XY, XY)))
c, r = fit(t_mix, vs)
print(f"   X und CX getrennt: Tr((X o Y)^2) = {c[0]:+.4f}|v|^4 {c[1]:+.4f} sum v^4 (Rest {r:.1e})  -> sum v^4 moeglich")
w = rng.normal(size=3)
vals = []
for v in vs:
    Zv, Zw = Z_of(v, 1.0), Z_of(w, 1.0)
    vals.append(tr(jordan(jordan(Zv, Zw), jordan(Zv, Zw))))
print(f"   zwei Flavons v, w (w fest): Tr((Z_v o Z_w)^2) haengt von der Richtung von v relativ zu w ab "
      f"(Streuung bei |v| = 1: {np.ptp([x / (v @ v) for x, v in zip(vals, vs)]):.3f})")

print("=" * 78)
print("C  Dynamik (k274-artig, gedaempft) auf dem Ein-Feld-Raum: Ausrichtung des Endzustands")
print("   Nach A ist V(v) = -mu^2/2 c2(a)|v|^2 + kappa cN(a) v1v2v3 + lam/4 c4(a)|v|^4 exakt; c2 = 2(1+a^2), cN = 2(3a - a^3), c4 = 2(1+a^2)^2.")


def coeffs(a):
    return 2 * (1 + a * a), 2 * (3 * a - a ** 3), 2 * (1 + a * a) ** 2


for a in (0.5, 1.0, 3.7):
    v = rng.normal(size=3); Z = Z_of(v, a); Z2 = jordan(Z, Z)
    c2, cN, c4 = coeffs(a)
    print(f"   Kontrolle a={a}: |Tr Z^2 - c2|v|^2| = {abs(tr(Z2) - c2 * v @ v):.1e}, |N - cN xyz| = {abs(det(Z) - cN * np.prod(v)):.1e},"
          f" |Tr Z^4 - c4|v|^4| = {abs(tr(jordan(Z2, Z2)) - c4 * (v @ v) ** 2):.1e}")


def classify(v):
    a = np.sort(np.abs(v))[::-1] / np.linalg.norm(v)
    if np.allclose(a, 1 / np.sqrt(3), atol=1e-3):
        return "(1,1,1), Rest Z3"
    if np.allclose(a, [1, 0, 0], atol=1e-3):
        return "(1,0,0), Rest Z2"
    return "andere"


def flow(a, mu2, kappa, lam, n=20):
    c2, cN, c4 = coeffs(a)
    def g(v):
        r2 = v @ v
        return -mu2 * c2 * v + kappa * cN * np.array([v[1] * v[2], v[0] * v[2], v[0] * v[1]]) + lam * c4 * r2 * v
    res, ends = {}, []
    for _ in range(n):
        y0 = np.concatenate([rng.normal(size=3), np.zeros(3)])
        sol = solve_ivp(lambda t, y: np.concatenate([y[3:], -g(y[:3]) - 1.5 * y[3:]]), (0, 200), y0, rtol=1e-10, atol=1e-12)
        e = sol.y[:3, -1]; ends.append(e); k = classify(e); res[k] = res.get(k, 0) + 1
    return res, ends


for p in ((1.0, 1.0, 0.3, 0.2), (0.5, 1.0, -0.4, 0.1), (2.0, 1.0, 0.05, 0.3), (3.7, 1.0, 0.01, 0.05)):
    print(f"   a={p[0]}, mu^2={p[1]}, kappa={p[2]:+}, lam={p[3]}: {flow(*p)[0]}")

print("=" * 78)
print("D  Ohne wirksamen xyz-Term: kappa = 0, oder cN(a) = 0 bei a in {0, +-sqrt(3)}")
for p in ((1.0, 1.0, 0.0, 0.2), (np.sqrt(3), 1.0, 0.5, 0.2), (0.0, 1.0, 0.5, 0.2)):
    res, ends = flow(*p, n=12)
    r = [np.linalg.norm(e) for e in ends]
    dirs = np.array([e / np.linalg.norm(e) for e in ends])
    print(f"   a={p[0]:.4f}, kappa={p[2]}: |v| = {min(r):.4f} ... {max(r):.4f}; Endrichtungen {res}; Streuung der Richtung {np.ptp(np.abs(dirs), axis=0).max():.2f}")
print("   -> Ein Feld gibt nur Z3 (cN kappa != 0) oder keine Ausrichtung (entartete Schale). Z2 braucht ein zweites, unabhaengiges Feld.")
