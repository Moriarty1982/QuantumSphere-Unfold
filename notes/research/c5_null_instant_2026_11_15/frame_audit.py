"""Frame-Audit von C5 (Erkundung, nicht blind).

Doublet (E, B) wie v4.9.0-r04/r27/r28: rho = (1 + b_x sigma_x + b_z sigma_z)/2 mit b_z = Re s/2u (Materie > 0, Tachyon < 0),
b_x = Im s/2u (Seite sign E.B); Kompensator C_HC = (1 + sigma_x)/2 = (1 + J_B)/2 (r28).
(1) Frame-Abbildungen auf der Scheibe und auf zwei Port-Begriffen:
    Scheiben-Ports (C_HC, sigma_x-Achse, r04-r28) und algebraische Ports (r42/r51, nach r16.2(b) die sigma_y-Pole).
(2) Kollar-Rekursion je Frame (r10.1, r27): drehen um alpha = pi/6, dann selektiv kompensieren. M liest C_HC, der
    Tachyon-Frame liest nach r28 die getauschten Ports. Summe der Anteile.
(3) Nullaugenblick (Beispielfeld aus null_instant.py): Anteil im Kompensatorport von M und im Kompensatorport von T ueber die Zeit.
"""
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
C = (np.eye(2) + sx) / 2; A = (np.eye(2) - sx) / 2
Hp, Hm = (np.eye(2) + sy) / 2, (np.eye(2) - sy) / 2      # algebraische Ports (sigma_y-Pole, r16.2(b))


def rho_of(E, B):
    G = np.array([[E @ E, E @ B], [B @ E, B @ B]]); u = np.trace(G) / 2
    bz, bx = (G[0, 0] - G[1, 1]) / (2 * u), 2 * G[0, 1] / (2 * u)
    return (np.eye(2) + bx * sx + bz * sz) / 2, bx, bz


maps = {"R (z -> iz)": lambda E, B: (-B, E), "T (Zeitumkehr)": lambda E, B: (E, -B), "J_B": lambda E, B: (B, E)}
rng = np.random.default_rng(5)
E, B = rng.normal(size=3), rng.normal(size=3)
r0, bx0, bz0 = rho_of(E, B)
print("(1) Wirkung auf die Scheibe und auf die Ports")
for name, f in maps.items():
    r1, bx1, bz1 = rho_of(*f(E, B))
    swap_disk = np.isclose(np.trace(C @ r1).real, np.trace(A @ r0).real) and not np.isclose(bx0, 0)
    # algebraische Ports: Wirkung von R, T, J_B auf sigma_y als Konjugation mit sigma_y, sigma_z, sigma_x (r51, r16)
    U = {"R (z -> iz)": sy, "T (Zeitumkehr)": sz, "J_B": sx}[name]
    swap_alg = np.allclose(U @ Hp @ U.conj().T, Hm)
    print(f"    {name:15s}: b_z {bz0:+.3f} -> {bz1:+.3f}, b_x {bx0:+.3f} -> {bx1:+.3f};"
          f" Scheiben-Ports getauscht: {swap_disk}; algebraische Ports getauscht: {swap_alg}")

print("(2) Kollar-Rekursion je Frame (selektiv, alpha = pi/6, Start auf der Kompensatorachse)")
a = np.pi / 6; U = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]], complex)
psi = np.array([1, 1], complex) / np.sqrt(2)              # Eigenvektor von sigma_x zu +1 = Kompensatorport
kept, sent = 1.0, 0.0
for n in range(1, 6):
    phi = U @ psi
    pC = abs(np.vdot(np.array([1, 1]) / np.sqrt(2), phi)) ** 2
    sent += kept * (1 - pC); kept *= pC
    psi = np.array([1, 1], complex) / np.sqrt(2)
    print(f"    n = {n}: M liest (Kompensator) {kept:.5f} = (3/4)^{n} {0.75**n:.5f}; T liest (Partner) {sent:.5f}; Summe {kept + sent:.5f}")
print("    'C5 = 0 in M' heisst 'T liest den ganzen Inhalt': vollstaendiger Frame-Wechsel")

print("(3) Nullaugenblick des Beispielfelds: Kompensatoranteil von M und von T")
E, B = np.array([1, 0, 0.3j]), np.array([0.7j, 1, 0])
for t in (-0.6, -0.2, 0.0, 0.2, 0.6):
    e, b = (E * np.exp(-1j * t)).real, (B * np.exp(-1j * t)).real
    r, bx, bz = rho_of(e, b)
    print(f"    t = {t:+.1f}: M-Anteil {np.trace(C @ r).real:.3f}, T-Anteil {np.trace(A @ r).real:.3f} (b_x = {bx:+.3f}, b_z = {bz:+.3f})")
