"""k436 (Erkundung, nicht blind): Legen J, Stabilitaet oder die kubische Norm das Vorzeichen des Zweigwahl-Terms (H222) fest?
Keine Vorab-Notiz (Erkundung): die Antworten auf 1 und 2 folgen vorab aus den J-Regeln von H158c bzw. aus phi -> -phi.
Aufruf aus diesem Ordner: python3 k436_vorzeichen.py > k436_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import minimize

# --- J-Regel aus H158c (k341): Monom phi^a r^m cos(n delta) erlaubt, wenn (m, n) und (a, n) in MN (A4-erlaubt) ---
def allowed_mn(maxm):
    out = set()
    for m in range(0, maxm + 1):
        for parts in itertools.product(range(m + 1), repeat=3):
            if sum(parts) != m or len({p % 2 for p in parts}) != 1:
                continue
            for pk in itertools.product(*[range(mk + 1) for mk in parts]):
                p = sum(pk); out.add((m, abs(2 * p - m)))
    return out


MN = allowed_mn(8)
ph, r, d, x = sp.symbols('phi r delta x', real=True)

print("=" * 84)
print("1  Ist N^2 (Quadrat der kubischen Norm) unter J erlaubt?")
print("=" * 84)
N = ph**3 - 3 * ph * r**2 + 2 * r**3 * sp.cos(3 * d)          # det der Zirkulante a=phi, |b|=r, arg b = delta
lam = sp.symbols('l0:3')
chk = sp.simplify(sp.expand_trig(sp.Matrix([[ph, r*sp.exp(sp.I*d), r*sp.exp(-sp.I*d)], [r*sp.exp(-sp.I*d), ph, r*sp.exp(sp.I*d)],
                                            [r*sp.exp(sp.I*d), r*sp.exp(-sp.I*d), ph]]).det()) - N)
print("Kontrolle det(Zirkulante) - N =", sp.simplify(chk.rewrite(sp.cos)))
N2 = sp.expand(sp.expand_trig(N**2).rewrite(sp.cos))
N2f = sp.expand(sp.fu(N2)) if False else None
# Fourier-Zerlegung in delta: N^2 = sum c_n(phi, r) cos(n delta)
coeffs = {}
for n in range(0, 7):
    cn = sp.integrate(sp.expand(N**2) * sp.cos(n * d), (d, 0, 2 * sp.pi)) / (sp.pi * (2 if n == 0 else 1))
    cn = sp.expand(sp.simplify(cn))
    if cn != 0:
        coeffs[n] = cn
viol = []
for n, cn in coeffs.items():
    for term in sp.Add.make_args(cn):
        a_ = sp.degree(term, ph); m_ = sp.degree(term, r)
        okJ = (m_, n) in MN and (a_, n) in MN
        print(f"  cos({n} delta): {term}   (phi^{a_} r^{m_}) J-erlaubt: {'ja' if okJ else 'NEIN'}")
        if not okJ:
            viol.append((term, n))
print(f"  -> N^2 {'ist nicht J-erlaubt' if viol else 'ist J-erlaubt'}; verbotene Teile: {viol}")
print("  J-erlaubter sextischer Term mit cos 3delta (H158c): nur phi^3 r^3 cos 3delta; dazu phi^3 r^3 cos delta")

print("\n" + "=" * 84)
print("2  Legt Stabilitaet das Vorzeichen fest?  F6 = J-erlaubte Ordnung 6")
print("=" * 84)
c1, c2, c3, c4, b3 = sp.symbols('c1 c2 c3 c4 beta3', real=True)
F6 = (c1 * (ph**6 + r**6) + c2 * (ph**2 * r**4 + ph**4 * r**2) + c3 * (ph**2 * r**4 + ph**4 * r**2) * sp.cos(2 * d)
      + c4 * ph**3 * r**3 * sp.cos(d) + b3 * ph**3 * r**3 * sp.cos(3 * d))
ident = sp.simplify(F6.subs({c4: -c4, b3: -b3}, simultaneous=True) - F6.subs(ph, -ph))
print("F6(phi; -c4, -beta3) - F6(-phi; c4, beta3) =", ident, " -> Feldraum enthaelt phi < 0, also gleiche Beschraenktheit fuer beide Vorzeichen")
f6 = sp.lambdify((ph, r, d, c1, c2, c3, c4, b3), F6, 'numpy')


def minF(cs):
    best = np.inf
    for t in np.linspace(0, 2 * np.pi, 721):
        for dd in np.linspace(0, 2 * np.pi, 361):
            best = min(best, f6(np.cos(t), np.sin(t), dd, *cs))
    return best


for cs in ((1.0, 0.5, 0.2, 0.0, 0.3), (1.0, 0.5, 0.2, 0.0, -0.3), (1.0, 0.5, 0.2, 0.4, 0.3), (1.0, 0.5, 0.2, -0.4, -0.3),
           (1.0, 0.0, 0.0, 0.0, 9.0), (1.0, 0.0, 0.0, 0.0, -9.0)):
    print(f"  (c1,c2,c3,c4,beta3) = {cs}: min F6 auf dem Einheitskreis = {minF(cs):+.5f} -> {'beschraenkt' if minF(cs) > 0 else 'unbeschraenkt'}")

print("\n" + "=" * 84)
print("3  Zweigwahl mit beiden J-erlaubten Termen (beta3 cos 3delta + c4 cos delta), phi > 0, nach gemeinsamer Drehung p")
print("=" * 84)
DSTAR = 0.2222220470731; P = np.pi / 12 - DSTAR
# Zweige ungefaltet: Im (alphap=+1, chi=pi/4+p): Daten 5pi/4+p, andere pi/4+p; Re (alphap=-1, chi=p): Daten pi/2+p, andere 3pi/2+p
br = {"Im": (5 * sp.pi / 4, sp.pi / 4), "Re": (sp.pi / 2, 3 * sp.pi / 2)}
pp = sp.symbols('p', real=True)
for s, (D0, O0) in br.items():
    dV = sp.simplify(sp.expand_trig((b3 * sp.cos(3 * (D0 + pp)) + c4 * sp.cos(D0 + pp)) - (b3 * sp.cos(3 * (O0 + pp)) + c4 * sp.cos(O0 + pp))))
    dV = sp.simplify(sp.expand_trig(dV))
    print(f"  {s}: V(Daten) - V(andere) = {sp.simplify(dV)}   bei p = x_lepton: {sp.N(dV.subs(pp, P), 6)}")
angs = np.linspace(0, 2 * np.pi, 360000, endpoint=False)
B, C = np.cos(angs), np.sin(angs)
dIm = 2 * B * np.cos(np.pi / 4 - 3 * P) - 2 * C * np.cos(np.pi / 4 + P)
dRe = 2 * B * np.sin(3 * P) - 2 * C * np.sin(P)
both = (dIm < 0) & (dRe < 0)
print(f"  Anteil der Richtungen (beta3, c4), die in beiden Sektoren den Daten-Zweig waehlen: {both.mean():.4f}")
print(f"  nur cos 3delta (c4 = 0): beta3 < 0 -> {'ja' if (2*np.cos(np.pi/4-3*P) > 0 and 2*np.sin(3*P) > 0) else 'nein'};"
      f"  nur cos delta (beta3 = 0): c4 > 0 -> {'ja' if (np.cos(np.pi/4+P) > 0 and np.sin(P) > 0) else 'nein'}")
bd = np.degrees(angs[both]); print(f"  Keil (Winkel von beta3-Achse): {bd.min():.2f} deg bis {bd.max():.2f} deg  (beta3 = -1: 180 deg, c4 = +1: 90 deg)")
print(f"  Grenzen: Re-Sektor beta3/c4 = sin p/sin 3p = {np.sin(P)/np.sin(3*P):.4f}; Im-Sektor beta3/c4 = cos(pi/4+p)/cos(pi/4-3p) = {np.cos(np.pi/4+P)/np.cos(np.pi/4-3*P):.4f}")
