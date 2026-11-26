"""k362 (H167): Skala als Setzung. Konjugationsterm gegen Spin-1-Term, Ladungsmischung c, Oktant, Rolle der Skala.
Vorab-Notiz Vorab_Notiz_H167_Skala_Setzung_Dipol.md (Commit c968be9).
Aufruf: python3 k362_test_h167.py > k362_out.txt
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize, brentq

DSTAR = 0.2222220470731
BETA = 0.5494056410


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


print("== H167a: die zwei Terme auf dem Zirkulantensektor ==")
a, s, v, c, r, de, al, alp = sp.symbols('a s v c r delta alpha alphap', real=True)
S = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
z = (1 + sp.I * c) * (s + sp.I * v)
W = a * sp.eye(3) + z * S + sp.conjugate(z) * S.T
Wc = W.conjugate()                                   # sigma: Konjugation der Eintraege
Tsig = sp.simplify(sp.expand((W * Wc + Wc * W).trace() / 2))
print("Tr(W o sigma W) =", sp.factor(Tsig), "; minus (3a^2 + 6 Re z^2):", sp.simplify(Tsig - 3 * a**2 - 6 * sp.re(sp.expand(z**2))))
print("k282-Form: 3 a^2 + 6[(1-c^2)(s^2-v^2) - 4 c s v] - Tr(W o sigma W) =",
      sp.simplify(3 * a**2 + 6 * ((1 - c**2) * (s**2 - v**2) - 4 * c * s * v) - Tsig))
chi = sp.atan(c)
sub = {s: r * sp.cos(de - chi) / sp.sqrt(1 + c**2), v: r * sp.sin(de - chi) / sp.sqrt(1 + c**2)}
print("z - r e^{i delta} mit s, v = r cos/sin(delta - chi)/sqrt(1+c^2):",
      sp.simplify(sp.expand_complex(z.subs(sub) - r * sp.exp(sp.I * de))))
print("Re z^2 - r^2 cos 2 delta =", sp.simplify(sp.re(sp.expand(z**2)).subs(sub) - r**2 * sp.cos(2 * de)))
print("(1+c^2) v^2 - r^2 sin^2(delta - chi) =", sp.simplify(((1 + c**2) * v**2).subs(sub) - r**2 * sp.sin(de - chi)**2))
# V_delta = alpha cos 2d - alphap cos 2(d - chi)
Vd = al * sp.cos(2 * de) - alp * sp.cos(2 * (de - chi))
X = al - alp * sp.cos(2 * chi); Y = -alp * sp.sin(2 * chi)
print("V_delta - (X cos 2d + Y sin 2d) =", sp.simplify(sp.expand_trig(Vd - (X * sp.cos(2 * de) + Y * sp.sin(2 * de)))),
      " mit X = alpha - alphap cos 2chi, Y = -alphap sin 2chi; Minima: 2 delta = atan2(Y, X) + pi (mod 2 pi)")


def minima(alpha, alphap, cc):
    ch = np.arctan(cc)
    Xv = alpha - alphap * np.cos(2 * ch); Yv = -alphap * np.sin(2 * ch)
    d0 = 0.5 * (np.arctan2(Yv, Xv) + np.pi)
    return d0, d0 + np.pi


for lab, (A_, Ap_, cc) in {"alphap = 0, alpha = +1, c = 0.7": (1, 0, 0.7), "alphap = 0, alpha = -1, c = 0.7": (-1, 0, 0.7),
                           "alpha = 0, alphap = +1, c = 1": (0, 1, 1.0), "alpha = 0, alphap = -1, c = 1": (0, -1, 1.0),
                           "alpha = 0, alphap = +1, c = 0": (0, 1, 0.0)}.items():
    m1, m2 = minima(A_, Ap_, cc)
    print(f"  {lab}: Minima delta = {m1:.6f}, {m2:.6f}; gefaltet {fold(m1):.6f}, {fold(m2):.6f}")
print(f"  pi/12 = {np.pi/12:.6f}, pi/6 = {np.pi/6:.6f}, pi/4 = {np.pi/4:.6f}")
x = sp.symbols('x')
detK = sp.simplify((sp.eye(3) + (sp.exp(sp.I * x) * S + sp.exp(-sp.I * x) * S.T) / sp.sqrt(2)).det())
print("det W bei K = 2/3 (a = 1, r = 1/sqrt2):", sp.simplify(sp.expand_trig(detK)), "; bei delta = pi/12:", sp.simplify(detK.subs(x, sp.pi / 12)),
      "; bei pi/4:", sp.simplify(detK.subs(x, sp.pi / 4)))

print("\n== H167b: wo die Skala eintritt ==")
A, B = sp.symbols('A B', real=True)
quad = B**2 / 2 * sp.cos(2 * de)                       # r^2 cos 2 delta, B = sqrt2 r
print("quadratischer Term r^2 cos 2d unter A <-> B:", sp.simplify(quad - quad.subs({A: B, B: A}, simultaneous=True)), "(ungleich 0: nicht J-symmetrisch)")
q4 = A**2 * B**2 / 2 * sp.cos(2 * de)
print("Ordnung 4, A^2 r^2 cos 2d unter A <-> B:", sp.simplify(q4 - q4.subs({A: B, B: A}, simultaneous=True)), "(J-symmetrisch, dimensionslos)")
V4 = sp.symbols('mu2') * (A**2 + B**2) + sp.symbols('lam') * (A**4 + B**4) + sp.symbols('kap') * A**2 * B**2 + A**2 * B**2 * Vd
print("V bis Ordnung 4: V(A) - V(-A) =", sp.simplify(V4 - V4.subs(A, -A)), "; V(delta + pi) - V(delta) =", sp.simplify(V4.subs(de, de + sp.pi) - V4))
o6 = A**3 * B**3 * sp.cos(3 * de)
print("Ordnung 6, A^3 B^3 cos 3d: V(delta + pi) + V(delta) =", sp.simplify(o6.subs(de, de + sp.pi) + o6), "(ungerade: hebt die Entartung)")


def spec(d):
    return np.sort([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def Vfull(p, mu2, lam, kap, alpha, alphap, cc, b3=0.0, b1=0.0):
    Av, Bv, d = p
    ch = np.arctan(cc)
    return (mu2 * (Av**2 + Bv**2) + lam * (Av**4 + Bv**4) + kap * Av**2 * Bv**2
            + Av**2 * Bv**2 * (alpha * np.cos(2 * d) - alphap * np.cos(2 * (d - ch)))
            + Av**3 * Bv**3 * (b3 * np.cos(3 * d) + b1 * np.cos(d)))


def gmin(args, n=60, seed=1):
    rng = np.random.default_rng(seed); best = None
    for _ in range(n):
        p0 = [rng.uniform(0.2, 1.5), rng.uniform(0.2, 1.5), rng.uniform(0, 2 * np.pi)]
        res = minimize(Vfull, p0, args=args, method='BFGS', options={'gtol': 1e-13})
        res = minimize(Vfull, res.x, args=args, method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-16, 'maxiter': 20000})
        if best is None or res.fun < best.fun - 1e-14:
            best = res
    return best


print("Numerische Kontrolle am vollen V(A, B, delta), mu2 = -1, lam = 1, kap = 0.5:")
for (alpha, alphap, cc) in ((0.0, 0.1, 1.0), (0.03, 0.2, 1.0), (0.1, -0.15, 0.6)):
    res = gmin((-1.0, 1.0, 0.5, alpha, alphap, cc))
    Av, Bv, d = res.x
    K = (1 + (Bv / Av)**2) / 3
    pred = minima(alpha, alphap, cc)
    err = min(abs(((d - p + np.pi / 2) % np.pi) - np.pi / 2) for p in pred)
    print(f"  alpha = {alpha}, alphap = {alphap}, c = {cc}: K - 2/3 = {K - 2/3:+.1e}; delta = {d % (2*np.pi):.7f}, Abstand zur Formel (mod pi) = {err:.1e}")
print("Zweige (alpha = 0, alphap = 0.1, c = 1): Spektren (Wurzeln, Summe 3) und Massenverhaeltnisse")
for d in minima(0.0, 0.1, 1.0):
    ev = spec(d)
    print(f"  delta = {d:.6f} (gefaltet {fold(d):.6f}): Wurzeln {np.round(ev, 6)}, m_klein/m_gross = {ev[0]**2/ev[2]**2:.6f}, m_mittel/m_gross = {ev[1]**2/ev[2]**2:.6f}")
for b3 in (+0.02, -0.02):
    res = gmin((-1.0, 1.0, 0.5, 0.0, 0.1, 1.0, b3, 0.0))
    Av, Bv, d = res.x
    print(f"  mit Ordnung 6, beta3 = {b3:+.2f}: globales Minimum bei delta gefaltet = {fold(d if Av > 0 else d + np.pi):.5f}, K - 2/3 = {(1 + (Bv/Av)**2)/3 - 2/3:+.1e}")

print("\n== H167c: Elektronmasse gegen alpha/alphap (c = 1, Oktant-Zweig) ==")


def lepton_ratio(rho):
    """c = 1, alphap = 1, alpha = rho: Minimum am Oktant-Zweig, m_e/m_tau."""
    ms = minima(rho, 1.0, 1.0)
    d = min(ms, key=lambda t: abs(fold(t) - np.pi / 12))
    ev = spec(d)
    return fold(d), ev[0]**2 / ev[2]**2


rhos = np.logspace(-3, -2, 9)
vals = np.array([lepton_ratio(rh) for rh in rhos])
slope = np.polyfit(np.log(rhos), np.log(vals[:, 1]), 1)[0]
slope_d = np.polyfit(np.log(rhos), np.log(np.abs(vals[:, 0] - np.pi / 12)), 1)[0]
print(f"Exponent von m_e/m_tau in alpha/alphap: {slope:.4f}; Exponent von |delta - pi/12|: {slope_d:.4f}")
print(f"analytisch: delta - pi/12 = -(1/2) arctan(rho) fuer rho > 0 (Kontrolle bei rho = 0.01: {lepton_ratio(0.01)[0] - np.pi/12:+.8f} gegen {-0.5*np.arctan(0.01):+.8f})")

print("\n== H167d: Zielverhaeltnisse rho* = alpha/alphap fuer delta* (c = 1) ==")
targets = []
for sg in (+1, -1):
    for m in range(3):
        for k in range(2):
            dm = sg * DSTAR + 2 * np.pi * m / 3 + k * np.pi          # Minimum soll hier liegen
            # 2 dm = atan2(Y, X) + pi, Y = -alphap, X = alpha (c = 1): Richtung (X, Y) = -(cos 2dm, sin 2dm)
            X_, Y_ = -np.cos(2 * dm), -np.sin(2 * dm)
            if abs(Y_) < 1e-14:
                continue
            alphap_ = -Y_; rho = X_ / alphap_
            targets.append((round(rho, 12), np.sign(alphap_)))
targets = sorted(set(targets))
for rho, sgn in targets:
    print(f"  rho* = {rho:+.10f} mit Vorzeichen(alphap) = {sgn:+.0f}")
okt = [t for t in targets if abs(t[0]) < 0.5]
print(f"d2: Oktant-Zweig |rho*| = {abs(okt[0][0]):.10f} (tan(pi/6 - 2 delta*) = {np.tan(np.pi/6 - 2*DSTAR):.10f})")
eps0 = np.arctanh(BETA)
L = {"9/10": 0.9, "10/9": 10 / 9, "1/10": 0.1, "1/9": 1 / 9, "1/19": 1 / 19, "1/2": 0.5, "2": 2.0, "1/3": 1 / 3, "2/3": 2 / 3, "2/9": 2 / 9,
     "1/sqrt2": 2**-0.5, "sqrt2": 2**0.5, "1/sqrt3": 3**-0.5, "sqrt3": 3**0.5, "beta_sym": BETA, "beta_sym^2": BETA**2, "eps0": eps0,
     "gamma_M": 0.237533, "gamma_M/2": 0.237533 / 2, "1/(4pi)": 1 / (4 * np.pi), "alpha_em": 1 / 137.035999}
hits = 0; best = (9, None)
for nm, val in L.items():
    for sg in (+1, -1):
        for rho, _ in targets:
            rel = abs(sg * val - rho) / abs(rho)
            if rel < 1e-4:
                hits += 1
            if rel < best[0]:
                best = (rel, (("+" if sg > 0 else "-") + nm, rho))
print(f"d1: {2 * len(L)} Kandidaten gegen {len(targets)} Zielverhaeltnisse: Treffer {hits}; naechster: {best[1][0]} gegen {best[1][1]:+.6f}, relativ {best[0]:.2e}")
print(f"    Zufallserwartung grob: {2 * len(L) * len(targets) * 2e-4 / 3:.3f} (Kandidaten ueber etwa drei Groessenordnungen gestreut)")

print("\n== Kontrolle zu c (alpha = 0) ==")
cst = np.tan(DSTAR + np.pi / 6)
print(f"c* = tan(delta* + pi/6) = {cst:.10f}, Kehrwert {1/cst:.10f}; cos(pi/8) = {np.cos(np.pi/8):.10f}")
dc = np.arctan(np.cos(np.pi / 8)) - np.pi / 6
print(f"c = cos(pi/8) gaebe delta = {dc:.10f}; Abstand zu delta* = {dc - DSTAR:+.3e} (Unsicherheit von delta*: 4e-10; aus m_tau allein 7.8e-7)")
print(f"\nH167d1: {'bestaetigt (kein Treffer)' if hits == 0 else 'widerlegt (Treffer)'}")
