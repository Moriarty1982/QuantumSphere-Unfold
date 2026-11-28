"""k449 (Erkundung, nicht blind): Wie koennten HS(-1), HS(0), HS(1) aus einem inneren und aeusseren Feld mit Vakuumschicht entstehen?
Standardrechnungen (Kink, Casimir zwischen Platten, Casimir mit Verdrehung) und ihre Zuordnung zu den Stufen (Lesart).
Aufruf aus diesem Ordner: python3 k449_innen_aussen.py > k449_out.txt
"""
import numpy as np
from mpmath import mp, zeta, nsum, cos, inf, pi, mpf, polylog, expj, re

mp.dps = 30
print("=" * 90)
print("k449  Inneres und aeusseres Feld mit Vakuumschicht: Wand, Spalt, Verdrehung")
print("=" * 90)

# 1 Wand zwischen zwei Vakua (HS(0) mit Einheitssphaere S^0 = {+1,-1})
print("\n1 Wand: V = lam (phi^2 - 1)^2, Vakua phi = +-1 (= S^0, Einheitssphaere von HS(0)); Kink phi = tanh(sqrt(2 lam) x)")
lam = 0.7
x = np.linspace(-8, 8, 4001)
ph = np.tanh(np.sqrt(2 * lam) * x)
dph = np.gradient(ph, x)
bps = np.max(np.abs(dph - np.sqrt(2 * lam) * (1 - ph ** 2)))
E = np.trapezoid(0.5 * dph ** 2 + lam * (ph ** 2 - 1) ** 2, x)
print(f"  BPS-Rest max|phi' - sqrt(2lam)(1-phi^2)| = {bps:.2e}; Wandenergie {E:.6f} (exakt 4/3 sqrt(2 lam) = {4/3*np.sqrt(2*lam):.6f})")
print(f"  topologische Ladung (phi(+inf) - phi(-inf))/2 = {(ph[-1]-ph[0])/2:+.6f}  (Werte 0, +-1: innen und aussen gleich oder entgegengesetzt)")

# 2 Spiegelstufe R + R j (HS(-1)): Idempotente = Projektoren auf innen/aussen
print("\n2 Spiegelstufe R[Z2] = R + R j, j^2 = +1: e_pm = (1 +- j)/2")
j = np.array([[0, 1], [1, 0]], float)
I = np.eye(2)
ep, em = (I + j) / 2, (I - j) / 2
print(f"  e+^2 - e+ = {np.abs(ep@ep-ep).max():.0e}, e-^2 - e- = {np.abs(em@em-em).max():.0e}, e+ e- = {np.abs(ep@em).max():.0e}, e+ + e- = 1: {np.allclose(ep+em, I)}")
print("  Lesart: e+ projiziert auf das innere, e- auf das aeussere Feld; j = Vorzeichen ueber die Wand")

# 3 Casimir im Spalt zwischen innen und aussen (Skalarfeld, 3+1): E/A = -(pi^2/(12 d^3)) * zeta_H(-3, a)
print("\n3 Casimir im Spalt der Breite d: Moden (n + a) pi/d; E/A = -(pi^2/(12 d^3)) zeta(-3, a)")
for lab, a in (("DD (gleiche Randbedingung, a = 1)", 1), ("DN (gemischte Randbedingung, a = 1/2)", mpf(1) / 2)):
    z = zeta(-3, a)
    print(f"  {lab}: zeta(-3,a) = {mp.nstr(z, 12)}, E/A * d^3 = {mp.nstr(-pi**2/12*z, 12)}  ({'anziehend' if z > 0 else 'abstossend'})")
r = zeta(-3, mpf(1) / 2) / zeta(-3, 1)
print(f"  Verhaeltnis E_DN/E_DD = {mp.nstr(r, 15)} (= -7/8)")

# 4 Verdrehung alpha ueber einen Umlauf (komplexes Feld, Phase alpha): E(alpha) ~ -sum cos(n alpha)/n^4
print("\n4 Verdrehung: komplexes Feld mit Phase alpha ueber den Umlauf; E(alpha) proportional -S(alpha), S = sum cos(n alpha)/n^4")
# nsum ist fuer die oszillierende Reihe bei alpha = pi/4 nur auf ~1e-4 genau (erster Lauf); daher exakt ueber Re Li_4(e^{i alpha})
S = lambda al: re(polylog(4, expj(al)))
Sn = lambda al: nsum(lambda n: cos(n * al) / n ** 4, [1, inf])
B = lambda al: pi ** 4 / 90 - pi ** 2 * al ** 2 / 12 + pi * al ** 3 / 12 - al ** 4 / 48
for al in (0, pi / 4, pi / 2, pi, 3 * pi / 2):
    print(f"  alpha = {mp.nstr(al, 6):>8}: S = {mp.nstr(S(al), 14)}, geschlossene Form (Bernoulli) {mp.nstr(B(al), 14)}, Differenz {mp.nstr(S(al)-B(al), 3)}; nsum {mp.nstr(Sn(al), 14)}")
print(f"  S(pi)/S(0) = {mp.nstr(S(pi)/S(0), 15)} (= -7/8, dieselbe Zahl wie DN/DD)")
print("  Bosonen (Vorzeichen +): Minimum der Energie bei alpha = 0; Fermionen (Vorzeichen -): bei alpha = pi")
al = np.linspace(0, 2 * np.pi, 721)
Sv = np.array([float(B(a)) for a in al])
print(f"  numerisch: argmin(-S) = {al[np.argmin(-Sv)]:.4f}, argmin(+S) = {al[np.argmin(Sv)]:.4f} (pi = {np.pi:.4f})")

print("\nZuordnung (Lesart, nicht hergeleitet):")
print("  alpha = 0  : innen und aussen gleich, Casimir anziehend -> Spalt schliesst, ein Feld          ~ HS(0)  (R)")
print("  alpha = pi : Vorzeichenwechsel ueber den Spalt, abstossend -> zwei getrennte Haelften         ~ HS(-1) (R + R j)")
print("  alpha frei : Phase zwischen beiden, U(1) mit Z2 = {0, pi} als Teilmenge                      ~ HS(1)  (C)")
