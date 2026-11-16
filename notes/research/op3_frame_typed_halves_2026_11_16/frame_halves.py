"""OP3: Kann man die Haelften von HS(8) in verschiedenen Frames lesen?  (Erkundung, nicht blind, Rueckwaertssuche vor einem Test.)

Bestand (v4.10.0-r16.7): auf dem Dublett chi wirken die Frame-Abbildungen als halbe Drehungen R = sigma_z, T = sigma_x, J_B = sigma_y um drei
senkrechte Achsen; das Oktant hat die Zyklusachse (1,1,1)/sqrt3.  Die Generationszustaende von r25/H107 liegen auf einem Kegel um die
Zyklusachse.
Bedingung fuer ein gemeinsames Singulettgewicht w (wie in H106-H108): Die Lesung einer Haelfte muss fuer alle drei Generationen dasselbe
Gewicht geben.
(1) Halbe Drehung um eine Frame-Achse (geneigt zur Zyklusachse): Kastengewichte je Generation gleich?
(2) Welche halben Drehungen achten den Zyklus?  (Drehungen um die Zyklusachse; halbe Drehungen um Achsen senkrecht dazu.)
(3) Was geben die zulaessigen Lesungen?  Vergleich mit den Werten der H107-Familie.
"""
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
zc = np.ones(3) / np.sqrt(3)                                  # Zyklusachse des Oktanten in den Frame-Koordinaten


def coh(n):
    n = n / np.linalg.norm(n); th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def cone(psi, axis):
    a = axis / np.linalg.norm(axis); e1 = np.cross(a, [1, 0, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(a, e1)
    return [np.cos(psi) * a + np.sin(psi) * (np.cos(2 * np.pi * k / 3) * e1 + np.sin(2 * np.pi * k / 3) * e2) for k in range(3)]


def basis_of(axis):
    """Orthonormalbasis des Qubits mit |0> entlang der Achse (Kopien-Bits werden in der Zyklusachse gelesen)."""
    up = coh(axis); dn = coh(-axis)
    return np.column_stack([up, dn])


def box_weights(state2, axis):
    B = np.kron(basis_of(axis), basis_of(axis))
    amp = B.conj().T @ state2
    return np.round(np.abs(amp) ** 2, 6)


psi = np.radians(38.6763)                                     # Spin-1-Dreieck (Ueberlappung 1/2)
gens = [np.kron(coh(n), coh(n)) for n in cone(psi, zc)]
print("(0) ohne Frame-Lesung, Kaesten 00/01/10/11 je Generation:")
for g in gens: print("   ", box_weights(g, zc))
for name, U in (("R = sigma_z", sz), ("T = sigma_x", sx), ("J_B = sigma_y", sy)):
    print(f"(1) Lesung nach {name} (halbe Drehung um eine Frame-Achse), je Generation:")
    for g in gens: print("   ", box_weights(np.kron(U, U) @ g, zc))

# (2) zulaessige Lesungen: halbe Drehung um eine Achse senkrecht zur Zyklusachse
perp = np.cross(zc, [1, 0, 0]); perp /= np.linalg.norm(perp)
Uperp = perp[0] * sx + perp[1] * sy + perp[2] * sz            # halbe Drehung um perp (bis auf Phase)
th = 2 * np.pi / 3; Uz = np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (zc[0] * sx + zc[1] * sy + zc[2] * sz)
print("(2) halbe Drehung um eine Achse senkrecht zur Zyklusachse, je Generation:")
for g in gens: print("   ", box_weights(np.kron(Uperp, Uperp) @ g, zc))
print("    Drehung um die Zyklusachse (2pi/3), je Generation:")
for g in gens: print("   ", box_weights(np.kron(Uz, Uz) @ g, zc))
w0 = box_weights(gens[0], zc); wf = box_weights(np.kron(Uperp, Uperp) @ gens[0], zc)
print(f"(3) senkrechte halbe Drehung vertauscht die Kaesten 00 <-> 11: {w0} -> {wf};"
      f" in einer Haelfte normiert: 01/H0 = {w0[1]/(w0[0]+w0[1]):.4f}, gelesen nach der Drehung = {wf[1]/(wf[0]+wf[1]):.4f}"
      f" = 10/H1 ohne Drehung {w0[2]/(w0[2]+w0[3]):.4f} (Werte schon in H107)")
