"""k67: Der Heisenberg-Kompensator umgeht die klassische 1/2-Aufenthaltswahrscheinlichkeit (Autorhinweis 2026-10-22).

Pruefungen:
 1. Klassische Mischung von Materie und Tachyonbild (z -> iz) gibt fuer jeden Zustand die Port-Gewichte 1/2, 1/2.
 2. Koharente Kombination ueber den Kompensator: Port-Gewicht haengt von der relativen Phase ab, deterministisch bei 0, pi.
 3. "Light as the Heisenberg compensator of the universe": C(beta) = (beta - beta)/2 = 0 nur amplitudenweise.
 4. Kompensator braucht eine Involution: C = (1 + J)/2 ist Projektor fuer J_B (J_B^2 = 1), nicht fuer z -> iz (i^2 = -1).
 5. Reservoir-Austausch der Staerke 1/2: koharent (theta = pi/4) gegen Markov (p = 1/2), Port-Gewichte am Attraktor.
"""
import math
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2); Cp = (I2 + sx) / 2; Ap = (I2 - sx) / 2
rho_of = lambda bx, bz: (I2 + bx * sx + bz * sz) / 2
bvec = lambda r: np.array([np.trace(r @ sx).real, np.trace(r @ sz).real])
U = lambda a: np.cos(a) * I2 - 1j * np.sin(a) * sy
rng = np.random.default_rng(5)

print("1. Klassische Mischung mit dem Tachyonbild (z -> iz)")
w = []
for _ in range(1000):
    r = rho_of(*(rng.uniform(-0.7, 0.7, 2)))
    m = 0.5 * r + 0.5 * (sy @ r @ sy)
    w.append(np.trace(Cp @ m).real)
print("   Gewicht im Kompensatorport: min %.6f, max %.6f -> immer 1/2" % (min(w), max(w)))

print("\n2. Koharente Kombination ueber den Kompensator (Amplituden f und e^{i phi} f_T)")
f = np.array([1, 0], complex)                      # E-Anteil
fT = sy @ f                                        # Tachyonbild z -> iz auf dem Dublett (bis auf Phase)
for phi in (0, math.pi / 2, math.pi, 3 * math.pi / 2):
    psi = (f + np.exp(1j * phi) * fT) / np.linalg.norm(f + np.exp(1j * phi) * fT)
    print("   phi = %5.1f Grad: Gewicht im Kompensatorport = %.4f" % (math.degrees(phi), abs(psi.conj() @ Cp @ psi)))
print("   klassisch waere es bei jeder Phase 1/2")

print("\n3. Licht als Kompensator des Universums: Materie +beta, J-Bild -beta")
b = 0.5493
print("   amplitudenweise: (beta + (-beta))/2 = %.4f;  wahrscheinlichkeitsweise: (beta^2 + beta^2)/2 = %.4f" % ((b - b) / 2, b * b))

print("\n4. Projektor-Eigenschaft von C = (1 + J)/2")
CJ = (I2 + sx) / 2
print("   J_B = sigma_x: C^2 = C ? %s" % np.allclose(CJ @ CJ, CJ))
Ji = 1j * I2          # z -> iz als lineare Abbildung auf der Amplitude
Ci = (I2 + Ji) / 2
print("   J = i (z -> iz):  C^2 = C ? %s  (C^2 = J/2 = %s)" % (np.allclose(Ci @ Ci, Ci), np.allclose(Ci @ Ci, Ji / 2)))

print("\n5. Austausch der Staerke 1/2 mit frischem Tachyon im Bezugszustand, nach jeder pi/6-Drehung")
SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
ptr = lambda tot: np.einsum("ijkj->ik", tot.reshape(2, 2, 2, 2))
rT = rho_of(-1, 0)
def run(step):
    r = rho_of(1, 0)
    for _ in range(800):
        r = step(U(math.pi / 6) @ r @ U(math.pi / 6).conj().T)
    return r
coh = run(lambda r: ptr((math.cos(math.pi / 4) * np.eye(4) - 1j * math.sin(math.pi / 4) * SW) @ np.kron(r, rT)
                        @ (math.cos(math.pi / 4) * np.eye(4) - 1j * math.sin(math.pi / 4) * SW).conj().T))
mar = run(lambda r: 0.5 * r + 0.5 * rT)
for name, r in (("koharent theta = pi/4", coh), ("Markov p = 1/2", mar)):
    bb = bvec(r)
    print("   %-22s |b| = %.4f, Gewichte Kompensator/Partner = %.4f / %.4f, Entropie %.4f Bit"
          % (name, np.linalg.norm(bb), np.trace(Cp @ r).real, np.trace(Ap @ r).real,
             -sum(l * math.log2(l) for l in np.linalg.eigvalsh(r) if l > 1e-15)))
