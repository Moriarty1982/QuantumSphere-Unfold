"""Erkundung: Ladung des Objekts, das den Schatten sieht. Spin-j-Koharente Zustaende |n> haben die Berry-Ladung j:
Bargmann-Phase eines geodaetischen Dreiecks = j * Raumwinkel. Ueberlappung |<n|n'>|^2 = cos^(4j)(theta/2).
Spin 1/2: Ueberlappung 1/2 bei 90 Grad (Oktant, Phase pi/4). Spin 1: Ueberlappung 1/2 bei cos theta = sqrt2 - 1."""
import numpy as np
def coh(j, n):
    th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0])
    m = np.arange(j, -j - 1, -1)
    from math import comb
    c = np.array([np.sqrt(comb(int(2*j), int(j - mm))) * np.cos(th/2)**(j+mm) * np.sin(th/2)**(j-mm) * np.exp(-1j*(j-mm)*ph) for mm in m])
    return c / np.linalg.norm(c)
def tri(cosa):
    # drei Einheitsvektoren mit paarweisem Kosinus cosa, symmetrisch um z
    s = np.sqrt((2*(1-cosa))/3); z = np.sqrt(1 - s**2)
    return [np.array([s*np.cos(2*np.pi*k/3), s*np.sin(2*np.pi*k/3), z]) for k in range(3)]
for j, cosa in ((0.5, 0.0), (1.0, np.sqrt(2) - 1)):
    v = tri(cosa); st = [coh(j, n) for n in v]
    ov = [abs(np.vdot(st[a], st[(a+1) % 3]))**2 for a in range(3)]
    B = np.vdot(st[0], st[1]) * np.vdot(st[1], st[2]) * np.vdot(st[2], st[0])
    A = np.arccos(cosa/(1+cosa)); omega = 3*A - np.pi
    G = np.array([[np.vdot(a, b) for b in st] for a in st])
    print(f"Spin {j}: Seite {np.degrees(np.arccos(cosa)):.3f} Grad, Ueberlappung {np.round(ov,6)}, |Bargmann-Phase| {abs(np.angle(B)):.6f}, "
          f"j*Raumwinkel {j*omega:.6f}, Gram-Rang {np.linalg.matrix_rank(G, 1e-9)}")
print("Lepton-Phase 2/3 =", round(2/3, 6), "; pi/4 =", round(np.pi/4, 6))
# Massenverhaeltnisse (Wurzeln = Gram-Eigenwerte, Brannen-Form) fuer die Spin-1-Phase und die Lepton-Phase
for name, phi in (("Spin-1-Dreieck", 3*np.arccos(1 - 1/np.sqrt(2)) - np.pi), ("Leptonen (2/3)", 2/3)):
    d = phi/3; v = np.sort([1 + np.sqrt(2)*np.cos(d + 2*np.pi*k/3) for k in range(3)])
    print(f"{name:16s} phi = {phi:.6f}: Wurzel-Verhaeltnisse 1 : {v[1]/v[0]:.2f} : {v[2]/v[0]:.2f}; Rest bis 2/3: {phi - 2/3:+.6f}")
