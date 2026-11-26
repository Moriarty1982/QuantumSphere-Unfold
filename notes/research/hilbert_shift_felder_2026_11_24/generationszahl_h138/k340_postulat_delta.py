"""k340 (H157): Was folgt aus dem Postulat (Tausch J als Symmetrie) fuer delta?

Lesart: J wirkt in jeder Ebene span{1, n(delta)} als phi <-> r bei festem delta.
Z3xZ2-invariante Polynome P(phi, R=r^2, C3=r^3 c), c = cos(3 delta).
J-erlaubt: P(phi, r^2, r^3 c) == P(r, phi^2, phi^3 c) identisch.
Aufruf: python3 k340_postulat_delta.py
"""
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import minimize

phi, r, c, mu2, lam, kap = sp.symbols('phi r c mu2 lam kap', real=True)


def on_plane(P):
    """P als Ausdruck in (phi, R, C3) -> Ebene."""
    R, C3 = sp.symbols('R C3')
    return P


def restrict(expr_fn):
    return sp.expand(expr_fn(phi, r**2, r**3 * c))


def jimage(expr_fn):
    return sp.expand(expr_fn(r, phi**2, phi**3 * c))


print("== H157a: H155-Form und N(W) unter der Ebenen-Lesart ==")
V155 = lambda f, R, C: -mu2 * (f**2 + R) + lam * (f**4 + R**2) + kap * f**2 * R
res = sp.simplify(restrict(V155) - jimage(V155))
print("H155-Form: Rest P - J P =", res)
NW = lambda f, R, C: f**3 / (3 * sp.sqrt(3)) - f * R / (2 * sp.sqrt(3)) + C / (3 * sp.sqrt(6))
resN = sp.expand(restrict(NW) - jimage(NW))
print("N(W): Rest P - J P =", sp.factor(resN))
coef = sp.Poly(resN, phi, r).as_dict()
print("N(W): Koeffizienten des Rests nach (phi, r)-Monomen:", {k: sp.simplify(v) for k, v in coef.items()})
sol = sp.solve([sp.simplify(v) for v in coef.values()], c, dict=True)
print("N(W): Ebenen mit Rest 0 (Loesungen in c):", sol, " -> keine reelle Ebene mit |c|<=1" if all(
    (not s) or abs(complex(s[c])) > 1 for s in sol) else "")

print("\n== H157b: J-erlaubter Unterraum bis Ordnung 12 (Erzeuger phi, R, C3) ==")
DMAX = 12
rows = []
for d in range(0, DMAX + 1):
    monos = [(a, b, k) for k in range(0, d // 3 + 1) for b in range(0, (d - 3 * k) // 2 + 1)
             for a in [d - 2 * b - 3 * k] if a >= 0]
    coeffs = sp.symbols(f'z0:{len(monos)}') if monos else []
    P = sum(z * phi**a * r**(2 * b + 3 * k) * c**k for z, (a, b, k) in zip(coeffs, monos))
    JP = sum(z * r**a * phi**(2 * b + 3 * k) * c**k for z, (a, b, k) in zip(coeffs, monos))
    diff = sp.Poly(sp.expand(P - JP), phi, r, c) if monos else None
    eqs = list(diff.as_dict().values()) if monos and not diff.is_zero else []
    M = sp.Matrix([[sp.diff(e, z) for z in coeffs] for e in eqs]) if eqs else sp.zeros(0, len(monos))
    ns = M.nullspace() if eqs else [sp.eye(len(monos))[:, i] for i in range(len(monos))]
    # k-Inhalt je Basisvektor
    kdim = {}
    basis_str = []
    for v in ns:
        ks = {monos[i][2] for i in range(len(monos)) if v[i] != 0}
        for kk in ks:
            kdim[kk] = kdim.get(kk, 0) + 1
        terms = [f"{v[i]}*phi^{monos[i][0]} R^{monos[i][1]} C3^{monos[i][2]}" for i in range(len(monos)) if v[i] != 0]
        basis_str.append(" + ".join(terms))
    rows.append((d, len(monos), len(ns), dict(sorted(kdim.items()))))
    print(f"Ordnung {d:2d}: invariant {len(monos):2d}, J-erlaubt {len(ns):2d}, k-Inhalt {dict(sorted(kdim.items()))}")
    if d in (6, 12) or (len(ns) and d <= 4):
        for s in basis_str:
            print("    ", s)
odd_ok = all(n == 0 for d, _, n, _ in rows if d % 2 == 1)
first_k1 = min(d for d, _, n, kd in rows if kd.get(1, 0) > 0)
first_k2 = min(d for d, _, n, kd in rows if kd.get(2, 0) > 0)
print(f"(i) keine ungerade Ordnung erlaubt: {odd_ok}")
print(f"(ii) erste Ordnung mit cos3delta (k=1): {first_k1}")
print(f"(iii) erste Ordnung mit cos^2 3delta (k=2): {first_k2}")

print("\n== H157c: Zufallsstichprobe, volle Minimierung in (phi, y1, y2) ==")


def allowed_basis(Dmax):
    """J-erlaubte Basis als Liste von (Ordnung, [(coef,a,b,k)]) ohne Ordnung 0,2,4 (die stehen fest)."""
    out = []
    for d in range(6, Dmax + 1, 2):
        monos = [(a, b, k) for k in range(0, d // 3 + 1) for b in range(0, (d - 3 * k) // 2 + 1)
                 for a in [d - 2 * b - 3 * k] if a >= 0]
        # Paare (a, m=2b+3k, k) <-> (m, a, k): Basis = Symmetrisierung
        seen = set()
        for (a, b, k) in monos:
            m = 2 * b + 3 * k
            if a < 3 * k or (a - k) % 2:
                continue
            bp = (a - 3 * k) // 2
            key = tuple(sorted([(a, b, k), (m, bp, k)]))
            if key in seen:
                continue
            seen.add(key)
            out.append((d, list(key) if key[0] != key[1] else [key[0]]))
    return out


def make_V(Dmax, rng):
    basis = allowed_basis(Dmax)
    lamq = rng.uniform(0.05, 1.0)
    kapq = rng.uniform(-1.0, 1.0) * 2 * lamq * 0.95  # Quartik beschraenkt: kap > -2 lam
    zs = rng.uniform(-1, 1, len(basis))
    top = (Dmax + 2) // 2

    def V(x):
        f, y1, y2 = x
        R = y1 * y1 + y2 * y2
        C3 = y1**3 - 3 * y1 * y2 * y2
        v = -(f * f + R) + lamq * (f**4 + R * R) + kapq * f * f * R
        for z, (d, ms) in zip(zs, basis):
            v += z * sum(f**a * R**b * C3**k for (a, b, k) in ms)
        v += (f * f + R)**top  # beschraenkender Term, positiv, J-erlaubt
        return v
    return V, basis


def global_min(V, rng, nstart=40):
    best = None
    for _ in range(nstart):
        x0 = rng.normal(0, 0.8, 3)
        res = minimize(V, x0, method='BFGS', options={'gtol': 1e-12, 'maxiter': 5000})
        if best is None or res.fun < best.fun - 1e-12:
            best = res
    return best.x


def readout(x):
    f, y1, y2 = x
    rr = np.hypot(y1, y2)
    if rr < 1e-6:
        return None
    d = np.arctan2(y2, y1)
    theta = np.arctan2(rr, abs(f))
    return d, theta, rr, f


rng = np.random.default_rng(340)
for Dmax in (10, 12):
    NS = 300
    inner = 0
    at_pi4 = 0
    valid = 0
    maxsin_end = 0.0
    sins = []
    for i in range(NS):
        V, basis = make_V(Dmax, rng)
        x = global_min(V, rng)
        ro = readout(x)
        if ro is None:
            continue
        valid += 1
        d, theta, rr, f = ro
        s = abs(np.sin(3 * d))
        sins.append(s)
        if s > 1e-4:
            inner += 1
        if abs(theta - np.pi / 4) < 1e-5:
            at_pi4 += 1
    sins = np.array(sins)
    print(f"Dmax={Dmax}: Proben {NS}, mit r>0 {valid}, innere delta (|sin3d|>1e-4) {inner}, "
          f"max|sin3d| {sins.max():.3e}, Median|sin3d| {np.median(sins):.3e}, theta=pi/4 bei {at_pi4}")
    print(f"   Groessen der Basis (Terme Ordnung 6..{Dmax}): {len(basis)}")

print("\nSkalenschaetzung fuer delta = 2/9 (nur Ordnung 6 und 12, Einheitskoeffizienten):")
cstar = np.cos(3 * 2 / 9)
Lu = (2 * cstar)**(1 / 6)
print(f"  c* = cos(2/3) = {cstar:.6f}; Lambda/u = (2 c*)^(1/6) = {Lu:.6f}; u = v/sqrt2 -> Lambda/v = {Lu / np.sqrt(2):.6f}")
print("  Vorzeichenbedingung: c* = -zeta6 Lambda^6/(2 zeta12 u^6) > 0 verlangt zeta6*zeta12 < 0 und zeta12 > 0 (nicht gesetzt, nur benannt)")

print("\n== H157d: Massenspektren an den Endpunkten bei K = 2/3 ==")
for name, d in (("delta=0", 0.0), ("delta=pi/3", np.pi / 3), ("delta=2/9", 2 / 9)):
    ck = np.array([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
    m = ck**2
    K = m.sum() / ck.sum()**2
    print(f"  {name}: m/m_max = {np.round(np.sort(m)[::-1] / m.max(), 6)}, K = {K:.12f}")
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
print(f"  Leptonen: m/m_tau = [1, {mmu / mtau:.6f}, {me / mtau:.3e}]")
