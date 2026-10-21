"""K12 / r09: Test der Vorhersagen P2 (Koide-Phase) und P3 (beta_sym-Formel).

P2: theta_K = pi - sqrt(2) arcsin(bsym) ~ 132.88 Grad, Brannen-Parametrisierung
    sqrt(m_k) = A (1 + sqrt2 cos(theta + 2 pi k/3)).  Vergleich mit Leptonmassen samt Messfehler.
P3: bsym = (1/sqrt3) exp(-gamma_1/(4 pi gL^5)), gL = gBI/gstring; bsym selbst = sqrt((gL-1)/(gL+1)).
    Pruefung: (i) wie viele aehnlich einfache Formeln passen ebenso gut (Look-elsewhere),
              (ii) welches gL loest die Gleichung exakt.
"""
import itertools
import numpy as np
import mpmath as mp

# ------------------------------------------------------------------ P2
# PDG-Werte (MeV): m_e, m_mu sehr genau; m_tau mit Fehler
me, mmu = 0.51099895000, 105.6583755
taus = {"PDG 2022 (1776.86 +- 0.12)": (1776.86, 0.12), "PDG 2024 (1776.93 +- 0.09)": (1776.93, 0.09)}

def brannen(me, mmu, mtau):
    r = np.sqrt([me, mmu, mtau]); A = r.sum()/3
    c = (r/A - 1)/np.sqrt(2)                    # cos(theta + 2 pi k/3) fuer eine Zuordnung von k
    K = (me + mmu + mtau)/r.sum()**2
    # direkt loesen: c_k = cos(theta + 2 pi k/3); nimm Zuordnung tau->k=0, e->k=1, mu->k=2 und alle Permutationen
    sols = []
    for perm in itertools.permutations(range(3)):
        cs = c[list(perm)]
        z = cs[0] + 1j*(cs[0]*np.cos(2*np.pi/3) - cs[1])/np.sin(2*np.pi/3)
        th = np.angle(z)
        pred = np.cos(th + 2*np.pi*np.arange(3)/3)
        if np.allclose(pred, cs, atol=1e-4):
            sols.append(th % (2*np.pi))
    return K, sorted(sols)

bsym = float(mp.sqrt((0.2375/(mp.log(2)/(mp.pi*mp.sqrt(3))) - 1)/(0.2375/(mp.log(2)/(mp.pi*mp.sqrt(3))) + 1)))
th_pred = np.pi - np.sqrt(2)*np.arcsin(bsym)
print(f"P2: Vorhersage theta_K = {th_pred:.6f} rad = {np.degrees(th_pred):.4f} Grad (bsym = {bsym:.6f})")
for name, (mt, dmt) in taus.items():
    K, sols = brannen(me, mmu, mt)
    th = min(sols, key=lambda x: abs(x - th_pred))
    _, s_up = brannen(me, mmu, mt + dmt); _, s_dn = brannen(me, mmu, mt - dmt)
    dth = abs(min(s_up, key=lambda x: abs(x - th)) - min(s_dn, key=lambda x: abs(x - th)))/2
    print(f"   {name}: K = {K:.7f} (2/3 = 0.6666667)  theta_obs = {th:.6f} rad = {np.degrees(th):.4f} Grad"
          f" +- {np.degrees(dth):.4f} Grad")
    print(f"      Abweichung Vorhersage - Messung = {np.degrees(th_pred - th):+.4f} Grad = {(th_pred - th)/dth:+.0f} sigma"
          f";  delta = theta - 2pi/3 = {th - 2*np.pi/3:.6f} (2/9 = {2/9:.6f})")

# ------------------------------------------------------------------ P3
g1 = float(mp.zetazero(1).imag)
gL = 0.2375/float(mp.log(2)/(mp.pi*mp.sqrt(3)))
lhs = lambda gl: np.sqrt((gl - 1)/(gl + 1))
rhs = lambda gl, n=5, c=4*np.pi: np.exp(-g1/(c*gl**n))/np.sqrt(3)
print(f"\nP3: bsym(gL) = {lhs(gL):.6f}, Formel = {rhs(gL):.6f}, relative Abweichung {rhs(gL)/lhs(gL) - 1:+.4%}")
# exakte Loesung in gL
from scipy.optimize import brentq
gstar = brentq(lambda x: lhs(x) - rhs(x), 1.5, 2.0)
print(f"   gL, das die Gleichung exakt loest: {gstar:.5f} (Eingabe gL = {gL:.5f})")
# Look-elsewhere: Exponent n = 1..8, Vorfaktor c in {1, 2, pi, 2pi, 4pi, 8pi, 16pi}, Basis 1/sqrt3
cs = {"1": 1, "2": 2, "pi": np.pi, "2pi": 2*np.pi, "4pi": 4*np.pi, "8pi": 8*np.pi, "16pi": 16*np.pi}
hits = []
for n in range(1, 9):
    for cn, c in cs.items():
        dev = rhs(gL, n, c)/lhs(gL) - 1
        hits.append((abs(dev), n, cn, dev))
hits.sort()
print(f"   {len(hits)} Formeln (gL^n, n=1..8; Vorfaktoren {list(cs)}): beste fuenf")
for a, n, cn, d in hits[:5]:
    print(f"      exp(-gamma_1/({cn} gL^{n}))/sqrt3: {d:+.4%}")
print("   Anzahl innerhalb 0.1 %:", sum(1 for h in hits if h[0] < 1e-3), "| innerhalb 1 %:", sum(1 for h in hits if h[0] < 1e-2))
# Wie dicht liegen die Werte? Erwartete Trefferzahl bei zufaelliger Verteilung der Abweichungen
devs = np.array([h[3] for h in hits])
print(f"   Spannweite der Abweichungen: {devs.min():+.2%} .. {devs.max():+.2%}")
near = np.abs(devs) < 0.05
p_chance = near.sum()*0.0004/0.10      # P(mindestens eine von near.sum() gleichverteilten Formeln in +-0.02 % von +-5 %)
print(f"   Formeln innerhalb +-5 %: {near.sum()}; Zufallswahrscheinlichkeit, dass eine davon innerhalb +-0.02 % landet: ~{p_chance:.1%}")
