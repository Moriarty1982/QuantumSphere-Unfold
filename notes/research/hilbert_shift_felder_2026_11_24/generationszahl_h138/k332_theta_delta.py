"""k332 (H149): Was legt theta = pi/4 und delta = 2/9 fest?

Vorab-Notiz: Vorab_Notiz_H149_Was_legt_Theta_und_Delta_fest.md (Commit 42f0900).
Aufruf: python k332_theta_delta.py > k332_out.txt  (Laufzeit wenige Sekunden).
Vorzeichen werden nicht gesetzt; wo ein Ergebnis vom Vorzeichen abhaengt, stehen beide Faelle.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import brentq

th, de, al = sp.symbols('theta delta alpha', real=True)

# ---------- Oktonionen (Cayley-Dickson, l^2 = -1) fuer die explizite Kontrolle ----------
def cd_mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    conj = lambda z: np.concatenate([z[:1], -z[1:]])
    return np.concatenate([cd_mul(a, c) - cd_mul(conj(d), b), cd_mul(d, a) + cd_mul(b, conj(c))])

def conj8(z):
    return np.concatenate([z[:1], -z[1:]])

E = np.eye(8)
print("=== H149a: theta = pi/4 <=> Re Psi^2 = 0 <=> lichtartig <=> Tausch-Fixpunkt ===")
# im Unterkoerper {1, U} gilt U -> i
z = sp.cos(th) + sp.I * sp.sin(th)
print("Re Psi^2 =", sp.simplify(sp.re(sp.expand(z**2))), "  (exakt cos 2 theta)")
mink = sp.cos(th)**2 - sp.sin(th)**2
print("Minkowski x0^2 - |x|^2 =", sp.simplify(mink), "; Differenz zu Re Psi^2:", sp.simplify(mink - sp.re(sp.expand(z**2))))
# Tausch J: psi -> U * conj(psi)
Jz = sp.I * sp.conjugate(z)
print("J(Psi) =", sp.simplify(sp.re(Jz)), "+ U *", sp.simplify(sp.im(Jz)), " -> theta -> pi/2 - theta")
print("J(J(Psi)) - Psi =", sp.simplify(sp.I * sp.conjugate(Jz) - z))
print("Fixpunkte J(Psi) = Psi in [0, pi):", sp.solve(sp.Eq(sp.cos(th), sp.sin(th)), th))
print("Anteile HS(0) = cos^2, Kopie = sin^2; gleich bei", sp.solve(sp.Eq(sp.cos(th)**2, sp.sin(th)**2), th))
# explizit in den Oktonionen mit U = cos(d) e1 + sin(d) e2 ... fuer mehrere delta und eine zweite Richtung
err = 0.0
for d in np.linspace(0, 2 * np.pi, 7):
    for (i, j) in [(1, 2), (3, 7)]:
        U = np.cos(d) * E[i] + np.sin(d) * E[j]
        err = max(err, np.abs(cd_mul(U, U) + E[0]).max())
        P = np.cos(np.pi / 4) * E[0] + np.sin(np.pi / 4) * U
        err = max(err, abs(cd_mul(P, P)[0]))                           # Re Psi^2 = 0
        JP = cd_mul(U, conj8(P))
        err = max(err, np.abs(JP - P).max())                           # Fixpunkt
print(f"Oktonionen explizit (U in e1/e2 und e3/e7, 7 Werte delta): max Fehler {err:.1e}")

print("\n=== H149b: V(N, Re Psi) sieht delta nicht; V(N) sieht auch theta nicht ===")
Psi = sp.Matrix([sp.cos(th), sp.sin(th) * sp.cos(de), sp.sin(th) * sp.sin(de)])
N = sp.simplify(sum(x**2 for x in Psi)); Re = Psi[0]
print("N(Psi) =", N, ", Re Psi =", Re)
cs = sp.symbols('v0:15')
mons = [(p, q) for p in range(5) for q in range(5) if 0 < p + q <= 4]
V = sum(cs[k] * N**p * Re**q for k, (p, q) in enumerate(mons))
print("allgemeines V(N, Re) bis Grad 4 (", len(mons), "Koeffizienten): dV/ddelta =", sp.simplify(sp.diff(V, de)))
VN = sum(cs[k] * N**k for k in range(1, 5))
print("V(N): dV/dtheta =", sp.simplify(sp.diff(VN, th)), ", dV/ddelta =", sp.simplify(sp.diff(VN, de)))
# U(1)-Drehung exp(alpha U) verschiebt theta
rot = sp.expand(sp.exp(sp.I * al) * z)
print("exp(alpha U) Psi = cos(theta+alpha) + U sin(theta+alpha):",
      sp.simplify(sp.re(rot) - sp.cos(th + al)) == 0 and sp.simplify(sp.im(rot) - sp.sin(th + al)) == 0)

print("\n=== H149c: allgemeines Potential 4. Ordnung, wann ist theta = pi/4 stationaer? ===")
m0, m1, a, b, c = sp.symbols('mu0sq mu1sq a b c', real=True)
phi, chi = sp.cos(th), sp.sin(th)
V4 = sp.Rational(1, 2) * m0 * phi**2 + sp.Rational(1, 2) * m1 * chi**2 + a * phi**4 + b * phi**2 * chi**2 + c * chi**4
dV = sp.simplify(sp.diff(V4, th).subs(th, sp.pi / 4))
print("dV/dtheta bei pi/4 =", sp.factor(dV))
lin = sp.Poly(dV, m0, m1, a, b, c)
print("Koeffizienten (mu0^2, mu1^2, a, b, c):", [lin.coeff_monomial(s) for s in (m0, m1, a, b, c)],
      "-> genau eine lineare Bedingung")
# Tausch J: phi <-> chi
VJ = V4.subs({m1: m0, c: a})
print("mit Tausch (mu1 = mu0, c = a): dV/dtheta bei pi/4 =", sp.simplify(sp.diff(VJ, th).subs(th, sp.pi / 4)))
d2 = sp.simplify(sp.diff(VJ, th, 2).subs(th, sp.pi / 4))
print("   zweite Ableitung bei pi/4 =", sp.factor(d2), " (Vorzeichen frei: Minimum fuer", sp.factor(d2), "> 0)")
d20 = sp.simplify(sp.diff(VJ, th, 2).subs(th, 0))
print("   zweite Ableitung bei 0 =", sp.factor(d20), " (Gegenstueck theta = 0, K = 1/3)")
VJ0 = VJ.subs({m0: 0})
print("   mit k291 (mu = 0): V =", sp.simplify(sp.expand(sp.trigsimp(VJ0))))
print("   V - [(2a - b)/8 cos 4theta + (3a + b)/4 ... konst.]: Rest =",
      sp.simplify(sp.expand_trig(VJ0 - (2 * a - b) / 8 * sp.cos(4 * th) - (VJ0.subs(th, sp.pi / 8)))),
      " -> V = konst. + (2a - b)/8 * Re Psi^4, Extrema bei theta = 0 und pi/4 (mod pi/2)")
# Lesart k297: tan theta = mu
bs = 0.5493
for name, t in [("HC Materie-Frame tan th = beta^2", np.arctan(bs**2)), ("HC Tachyon-Frame tan th = beta^-2", np.arctan(bs**-2)),
                ("Tausch-Fixpunkt mu = 1", np.pi / 4)]:
    print(f"   {name}: theta = {t:.6f}, K = 1/(3cos^2) = {1 / (3 * np.cos(t)**2):.6f}")

print("\n=== H149d: delta sieht nur die kubische Norm N(W) = c0 c1 c2 ===")
ck = [sp.cos(th) / sp.sqrt(3) + sp.sqrt(sp.Rational(2, 3)) * sp.sin(th) * sp.cos(de - 2 * sp.pi * k / 3) for k in range(3)]
T1 = sp.simplify(sum(ck)); T2 = sp.simplify(sp.expand_trig(sum(x**2 for x in ck)))
T3 = sp.simplify(sp.expand_trig(sp.expand(ck[0] * ck[1] * ck[2])))
print("Tr W =", T1); print("Tr W^2 =", sp.simplify(T2))
print("N(W) =", sp.simplify(sp.fu(T3)))
A_ = sp.simplify(T3.subs(de, sp.pi / 6))                         # cos 3delta = 0
B_ = sp.simplify(T3.subs(de, 0) - A_)
print("N(W) - (A + B cos 3delta) =", sp.simplify(sp.expand_trig(T3 - A_ - B_ * sp.cos(3 * de))))
print("bei theta = pi/4: A =", sp.nsimplify(sp.simplify(A_.subs(th, sp.pi / 4))), ", B =", sp.nsimplify(sp.simplify(B_.subs(th, sp.pi / 4))))
dN = sp.simplify(sp.diff(T3, de)); print("dN/ddelta =", sp.factor(sp.simplify(sp.fu(dN))))

Af = float(A_.subs(th, sp.pi / 4)); Bf = float(B_.subs(th, sp.pi / 4))
def amps(d, t=np.pi / 4):
    return np.array([np.cos(t) / np.sqrt(3) + np.sqrt(2 / 3) * np.sin(t) * np.cos(d - 2 * np.pi * k / 3) for k in range(3)])
def reduce_delta(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)                              # Z3 und Spiegelung delta -> -delta
grid = np.linspace(0, 2 * np.pi, 20001)
hits, total, interior = [], 0, 0
for deg in (2, 3):
    for coef in itertools.product(range(-3, 4), repeat=deg):
        if coef[-1] == 0:
            continue
        Nn = Af + Bf * np.cos(3 * grid)
        V = sum(coef[k] * Nn**(k + 1) for k in range(deg))
        idx = [i for i in range(1, len(grid) - 1) if V[i] < V[i - 1] and V[i] <= V[i + 1]]
        for i in idx:
            total += 1
            dr = reduce_delta(grid[i])
            m = np.sort(amps(grid[i])**2)
            distinct = min(np.diff(m)) > 1e-3 * m[-1]
            if distinct:
                interior += 1
            if distinct and abs(dr - 2 / 9) < 0.01 * 2 / 9:
                hits.append((coef, dr))
print(f"Abtastung V = sum alpha_k N^k (Grad 2 und 3, alpha in -3..3): {total} Minima, davon {interior} mit drei verschiedenen Massen;")
print(f"   Treffer innerhalb 1 % von 2/9: {len(hits)}", hits[:5])
# welche reduzierten delta kommen ueberhaupt vor (mit drei verschiedenen Massen)?
vals = set()
for deg in (2, 3):
    for coef in itertools.product(range(-3, 4), repeat=deg):
        if coef[-1] == 0:
            continue
        x = np.cos(3 * grid); Nn = Af + Bf * x
        V = sum(coef[k] * Nn**(k + 1) for k in range(deg))
        for i in range(1, len(grid) - 1):
            if V[i] < V[i - 1] and V[i] <= V[i + 1]:
                m = np.sort(amps(grid[i])**2)
                if min(np.diff(m)) > 1e-3 * m[-1]:
                    vals.add(round(reduce_delta(grid[i]), 4))
print("   vorkommende reduzierte delta (drei verschiedene Massen):", sorted(vals))
x0 = -Af / Bf
print(f"   N(W) = 0 bei cos 3delta = {x0:.6f} = 1/sqrt2 -> delta = {np.arccos(x0) / 3:.6f} = pi/12 (masseloses Elektron, H101); Massen dort:", np.round(np.sort(amps(np.pi / 12)**2), 6))
x_need = np.cos(3 * 2 / 9)
print(f"   noetig: cos 3delta = cos(2/3) = {x_need:.6f}, N* = {Af + Bf * x_need:.6f}; fuer V = alpha N + beta N^2: alpha/beta = {-2 * (Af + Bf * x_need):.6f}")

print("\n=== H149e: strukturelle Kandidaten fuer delta (vorab fest) ===")
mlep = np.array([0.51099895, 105.6583755, 1776.93])
d_fit = brentq(lambda d: (lambda m: m[1] / m[0])(np.sort(amps(d)**2)) - mlep[1] / mlep[0], 0.15, 0.3)
print(f"delta_fit (theta = pi/4, aus m_mu/m_e) = {d_fit:.9f}")
gM = 0.237533
cands = {"pi/12": np.pi / 12, "artanh(beta_sym)/3": np.arctanh(bs) / 3, "gamma_M": gM, "arctan(beta_sym^2)": np.arctan(bs**2)}
nh = 0
for k_, v in cands.items():
    r = abs(v / d_fit - 1); nh += r < 0.01
    print(f"   {k_:22s} = {v:.6f}, relativ {r * 100:.2f} %  -> {'Treffer' if r < 0.01 else 'kein Treffer'}")
print("   Treffer:", nh)

print("\n=== Nicht gewertet: bekannte Beziehungen und vorab gesehener Zahlentreffer ===")
print(f"   CT-002: pi/12 - gamma_M/6 = {np.pi / 12 - gM / 6:.6f} (relativ {abs((np.pi / 12 - gM / 6) / d_fit - 1):.1e})")
print(f"   H1: K/3 = 1/(9 cos^2 pi/4) = {2 / 9:.6f} (relativ {abs(2 / 9 / d_fit - 1):.1e})")
# delta aus allen drei Massen (Brannen-Fourier), Tau-Fehler 0.09 MeV
def brannen_delta(m):
    # sqrt m_k = t (1 + sqrt2 r cos(delta + 2 pi k/3)); Reihenfolge egal nach Reduktion (Z3, Spiegelung)
    s = np.sqrt(m)
    z = sum(s[k] * np.exp(-2j * np.pi * k / 3) for k in range(3)) * 2 / 3
    return reduce_delta(np.angle(z))
rng = np.random.default_rng(332)
ds = [brannen_delta(np.array([0.51099895, 105.6583755, rng.normal(1776.93, 0.09)])) for _ in range(20000)]
dB, sB = brannen_delta(mlep), np.std(ds)
print(f"   delta aus drei Massen (Brannen, Tau +- 0.09 MeV): {dB:.6f} +- {sB:.6f}")
dpi = np.arccos(np.pi / 4) / 3
print(f"   arccos(pi/4)/3 = {dpi:.6f}: Abstand {abs(dpi - dB) / sB:.1f} sigma (Massen-delta), {abs(dpi - 2 / 9) / (2 / 9) * 100:.3f} % von 2/9")
print(f"   -4 cos(2/3) = {-4 * np.cos(2 / 3):.6f} gegen -pi = {-np.pi:.6f}")
