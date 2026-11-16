"""OP3: Woran scheitert die Biegung?  Logikkette rueckwaerts (Erkundung, nicht blind).

(a) Ziel: Brannen-Form sqrt(m_k) ~ 1 + 2|c| cos(delta + 2 pi k/3) ist fuer JEDE positive Dreiergruppe moeglich (DC + eine Fourier-Komponente).
    K legt nur |c| fest (|c| = 1/sqrt2), delta ist eine zweite, unabhaengige Zahl.  Gram-Lesart: zirkulante Gram-Matrix mit G01 = c,
    Bargmann-Phase = arg c^3 = 3 delta.  Pruefen an den Polmassen.
(b) Starrheit: reine, zyklussymmetrische Bahn von Spin-j-koharenten Zustaenden: Ueberlappung legt den Kegel fest, der Kegel die Phase.
    Werte fuer j = 1/2, 1, 3/2 bei Ueberlappung^2 = 1/2.
(c) Spin-1-Bahn unter U = diag(w, 1, w-bar): Gewichte (p+, p0, p-) fuer K = 2/3 und phi = 2/3; Koharenzmass r = 2 sqrt(p+ p-)/p0
    (koharent: r = 1, notwendig fuer Rang 1 von S nach r16.8).  Spanne des Takagi-Verhaeltnisses ueber die freie relative Phase.
(d) Zahlentyp: geometrische Phase = halber Raumwinkel; phi = 2/3 rad entspraeche Omega = 4/3 sr.
"""
import numpy as np

m = {"e": 0.51099895, "mu": 105.6583755, "tau": 1776.86}
r = np.sqrt(np.array([m["e"], m["mu"], m["tau"]]))
K = (m["e"] + m["mu"] + m["tau"]) / r.sum() ** 2
F = np.fft.fft(r) / 3
c_abs = abs(F[1]) / F[0].real / 2 * 2  # |amplitude| relativ zum Mittel: sqrt m = mu(1 + 2|F1|/F0 cos(...))
amp = 2 * abs(F[1]) / F[0].real
delta = np.angle(F[1])
print(f"(a) K = {K:.6f}; Amplitude 2|F1|/F0 = {amp:.6f} (fuer K = 2/3 noetig sqrt2 = {np.sqrt(2):.6f})")
print(f"    delta aus der Fourier-Komponente = {abs(delta):.6f} (mod 2pi/3: {min(abs(delta) % (2*np.pi/3), 2*np.pi/3 - abs(delta) % (2*np.pi/3)):.6f}),"
      f" 3 delta = {3 * min(abs(delta) % (2*np.pi/3), 2*np.pi/3 - abs(delta) % (2*np.pi/3)):.6f}")
lam = r / r.mean() * 1.0                                   # Gram-Eigenwerte ~ sqrt m, Spur 3
w3 = np.exp(2j * np.pi / 3)
# zirkulante Matrix mit Eigenwerten lam: G = F^-1 diag(lam) F
Fm = np.array([[w3 ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
G = Fm.conj().T @ np.diag(lam) @ Fm
print(f"    Gram aus sqrt m: |G01|^2 = {abs(G[0,1])**2:.6f}, Bargmann-Phase |arg(G01 G12 G20)| = {abs(np.angle(G[0,1]*G[1,2]*G[2,0])):.6f}")


def coh_spin(j, n):
    """Spin-j-koharenter Zustand entlang n, Basis m = j..-j."""
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    from math import comb
    d = int(round(2 * j))
    return np.array([np.sqrt(comb(d, k)) * np.cos(th / 2) ** (d - k) * (np.exp(1j * ph) * np.sin(th / 2)) ** k for k in range(d + 1)])


def orbit_phase(j):
    def st(psi):
        return [coh_spin(j, np.array([np.sin(psi) * np.cos(2*np.pi*k/3), np.sin(psi) * np.sin(2*np.pi*k/3), np.cos(psi)])) for k in range(3)]
    f = lambda p: abs(np.vdot(*st(p)[:2])) ** 2 - 0.5
    lo, hi = 1e-4, np.pi / 2
    for _ in range(100):
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if f(mid) > 0 else (lo, mid)
    g = st(lo)
    return np.degrees(lo), abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


for j in (0.5, 1.0, 1.5):
    psi, ph = orbit_phase(j); print(f"(b) Spin {j}: Kegel psi = {psi:.4f} Grad, Phase = {ph:.6f}")

# (c) Gewichte fuer K = 2/3, phi = 2/3:  <psi|U psi> = p0 + p+ w + p- w-bar, |.|^2 = 1/2, 3 arg = 2/3
target = 0.666665
z = np.exp(1j * target / 3) / np.sqrt(2)
# p0 + p+ w + p- wbar = z,  p0 + p+ + p- = 1  -> drei reelle Gleichungen
A = np.array([[1, np.cos(2*np.pi/3), np.cos(2*np.pi/3)], [0, np.sin(2*np.pi/3), -np.sin(2*np.pi/3)], [1, 1, 1]])
p0, pp, pm = np.linalg.solve(A, [z.real, z.imag, 1.0])
print(f"(c) Gewichte fuer K = 2/3, phi = {target}: p0 = {p0:.6f}, p+ = {pp:.6f}, p- = {pm:.6f} (r16.9(a): 0.793146/0.193404/0.013450 bis auf Umbenennung)")
ws = sorted([p0, pp, pm], reverse=True)
r_target = 2 * np.sqrt(ws[0] * ws[2]) / ws[1]
psi1, _ = orbit_phase(1.0); t = np.radians(psi1)
coh = [np.cos(t/2)**4, 2*np.cos(t/2)**2*np.sin(t/2)**2, np.sin(t/2)**4]
print(f"    Koharenzmass r = 2 sqrt(p_gross p_klein)/p_mitte: Ziel {r_target:.6f}, Spin-1-Dreieck {2*np.sqrt(coh[0]*coh[2])/coh[1]:.6f} (koharent = 1)")
xs, ys, zs = np.sqrt(ws[0]), np.sqrt(ws[1] / 2), np.sqrt(ws[2])
rat = []
for a in np.linspace(0, np.pi, 721):
    S = np.array([[xs, ys * np.exp(1j * a)], [ys * np.exp(1j * a), zs]])
    sv = np.linalg.svd(S, compute_uv=False); rat.append(sv[1] / sv[0])
print(f"    Takagi-Verhaeltnis sigma2/sigma1 des Zielzustands ueber die freie relative Phase: {min(rat):.4f} ... {max(rat):.4f} (koharent: 0)")
print(f"(d) Raumwinkel fuer phi = 2/3 rad: Omega = 2 phi = {2*target:.6f} sr; Oktant pi/4 -> Omega = pi/2 (ein Achtel der Kugel)")
