"""k353 (Erkundung, keine H-Nummer, kein Entscheidungskriterium): Zahlen zu den Ideen (1) und (2) des Autors vom 26.11.2026.
Teil A (Idee 1, zwei Bahnen am Mittelpunkt vorbei): Ablenkwinkel eines Strahls mit Stossparameter b an der Masse m = GM/c^2
  - Newton, Teilchen mit v = c (Bahngleichung u'' + u = m/b^2),
  - Schwarzschild, Nullgeodaete (u'' + u = 3 m u^2),
  - skalare Gravitation mit Kopplung an die Spur des Energie-Impuls-Tensors: Lehrbuchwert 0 (nicht gerechnet, nur genannt).
Teil B (Idee 2, 10^122): Verhaeltnis Planck-Dichte zu beobachteter Vakuumdichte und dieselbe Zahl als Horizontflaeche.
Aufruf: python k353_erkundung_ideen_1_2.py > k353_out.txt
"""
import numpy as np
from scipy.integrate import solve_ivp

print("== Teil A  Ablenkwinkel, in Einheiten von m/b ==")
def ablenkung(rhs, m, b=1.0):
    # Start weit draussen: u = 0, du/dphi = 1/b; laufen bis u wieder 0 wird
    ev = lambda phi, y: y[0]; ev.terminal = True; ev.direction = -1
    s = solve_ivp(lambda phi, y: [y[1], rhs(y[0], m, b) - y[0]], [0, 4 * np.pi], [0.0, 1.0 / b], events=ev, rtol=1e-12, atol=1e-14, first_step=1e-6)
    return s.t_events[0][0] - np.pi
for m in (1e-2, 1e-3, 1e-4):
    aN = ablenkung(lambda u, m, b: m / b**2, m)
    aS = ablenkung(lambda u, m, b: 3 * m * u**2, m)
    print(f"  m/b = {m:.0e}: Newton (v = c) {aN/m:.5f},  Schwarzschild {aS/m:.5f},  Verhaeltnis {aS/aN:.5f}")
print("  Grenzwerte: Newton 2 m/b, Schwarzschild 4 m/b, Verhaeltnis 2 (gemessen: 1.0 in Einheiten von 4 m/b, VLBI auf etwa 1e-4)")
print("  skalare Gravitation (Nordstroem, Kopplung an die Spur): 0, weil die Spur fuer Licht verschwindet (Lehrbuchwert)")

print("\n== Teil B  die Zahl 10^122 ==")
c, G, hbar = 2.99792458e8, 6.67430e-11, 1.054571817e-34
H0 = 67.4e3 / 3.0857e22; OL = 0.685                                # Planck 2018 (gerundet)
Lam = 3 * OL * H0**2 / c**2                                         # 1/m^2
lP2 = hbar * G / c**3; mP = np.sqrt(hbar * c / G)
rhoL = Lam * c**2 / (8 * np.pi * G); rhoP = c**5 / (hbar * G**2)
print(f"  Lambda = {Lam:.3e} 1/m^2,  l_P^2 = {lP2:.3e} m^2,  Lambda*l_P^2 = {Lam*lP2:.3e}")
print(f"  rho_Planck / rho_Lambda = 8 pi/(Lambda l_P^2) = {rhoP/rhoL:.3e}  (log10 = {np.log10(rhoP/rhoL):.2f})")
L = np.sqrt(3 / Lam)
print(f"  de-Sitter-Radius L = sqrt(3/Lambda) = {L:.3e} m;  L/l_P = {L/np.sqrt(lP2):.3e}  (log10 = {np.log10(L/np.sqrt(lP2)):.2f})")
print(f"  Horizontflaeche/(4 l_P^2) = 3 pi/(Lambda l_P^2) = {3*np.pi/(Lam*lP2):.3e}  (log10 = {np.log10(3*np.pi/(Lam*lP2)):.2f})")
print(f"  also rho_Planck/rho_Lambda = (8/3)*(Horizontflaeche in Planck-Einheiten/4) = 8 pi/3 * (L/l_P)^2: Probe {8*np.pi/3*(L**2/lP2)/(rhoP/rhoL):.6f}")
E_hor = rhoL * c**2 * 4 / 3 * np.pi * L**3
print(f"  Vakuumenergie im Horizontvolumen / Planck-Energie = {E_hor/(mP*c**2):.3e} = (1/2) L/l_P: Probe {E_hor/(mP*c**2)/(0.5*L/np.sqrt(lP2)):.6f}")
print(f"  ein Schwarzes Loch der Planck-Masse: Masse {mP:.3e} kg, Energie {mP*c**2:.3e} J, Verdampfungszeit von der Ordnung der Planck-Zeit {np.sqrt(lP2)/c:.2e} s")
print("  Lesart: die 'falsche' Zahl 10^122 ist das Quadrat von L/l_P. Sie misst kein Energiebudget, sondern das Verhaeltnis zweier Laengen.")
