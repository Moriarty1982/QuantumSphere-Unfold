"""Spannung „P zwischen M und T“ (Konvention F) gegen „P aussen“ (Zaehlung): Lage von P in verschiedenen Koordinaten (Erkundung, analytisch).

Konvention F (r22): x = beta_sym^2, M bei x, T bei 1/x, P beim Fixpunkt x = 1 (p+ = p- = 1/2).  Rapiditaet: x = tanh^2(eta) (gamma = cosh 2 eta);
T = Tachyon-Boden bei eta + i pi/2 (r63.3, r68.1(c)), tanh^2(eta + i pi/2) = coth^2(eta) = 1/x.
Verglichen werden die Ordnungen nach x, nach der Sichtbarkeit |b| = (1-x)/(1+x) (frame-frei), nach der reellen Rapiditaet, nach der Register-Entropie
und nach der Zaehlung (gamma).  Dazu: Rang einer Maske kann im Grenzwert nicht steigen.
"""
import numpy as np

beta = 0.549406
x = beta ** 2
eta = np.arctanh(beta)
xT = np.tanh(eta + 1j * np.pi / 2) ** 2
print(f"x_M = tanh^2(eta) = {x:.6f}, x_T = tanh^2(eta + i pi/2) = {xT.real:.6f} (1/x_M = {1/x:.6f}, Imaginaerteil {abs(xT.imag):.1e})")
for e in (1.0, 2.0, 4.0, 8.0):
    print(f"   eta = {e}: x_M = {np.tanh(e)**2:.6f}, x_T = {1/np.tanh(e)**2:.6f}  (beide -> 1 = P fuer eta -> unendlich)")


def H(p):
    p = np.array([p, 1 - p]); p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


rows = {"R (eta = 0)": 0.0, "M": x, "P": 1.0, "T": 1 / x}
print("Frame | x | |b| | Register-Entropie (bit) | reelle Rapiditaet | Zaehlung gamma")
gam = {"R (eta = 0)": "-", "M": "0.2375", "P": "0.2741 (Vorschlag)", "T": "0.1274"}
for k, xv in rows.items():
    pplus = 1 / (1 + xv)
    b = abs(1 - xv) / (1 + xv)
    rap = "0" if xv == 0 else ("unendlich" if xv == 1 else (f"{np.arctanh(np.sqrt(xv)):.4f}" if xv < 1 else f"{np.arctanh(1/np.sqrt(xv)):.4f} + i pi/2"))
    print(f"{k} | {xv:.4f} | {b:.4f} | {H(pplus):.4f} | {rap} | {gam[k]}")
# Rang im Grenzwert: Folge von Rang-2-Projektoren konvergiert gegen Rang <= 2
j = 2; d = int(2 * j + 1)
rng = np.random.default_rng(1)
ranks = []
for n in range(1, 6):
    A = rng.normal(size=(d, 2)) + 1j * rng.normal(size=(d, 2)); Q, _ = np.linalg.qr(A)
    P = Q @ Q.conj().T
    ranks.append(int(round(np.trace(P).real)))
print(f"Rang von Projektoren in einer Folge (Spur, stetig): {ranks} -> der Grenzwert hat Spur 2, nie 2j + 1 = {d}")
