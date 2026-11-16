"""Mehrere Umkehrwalzen (r02.2-r02.5, r04) auf der Generationskugel chi (Erkundung, analytisch, numerisch bestaetigt).

Bestand: auf chi wirken R = sigma_z, T = sigma_x, J_B = sigma_y (r16.7); die Dualitaetsdrehung R_a dreht chi um die Helizitaetsachse z um -2a
(op1_u1_check); C = R_pi ist auf chi die Identitaet (s+- unveraendert).  Rotor-Konjugate (Enigma-Muster r02.5): R_a^{-1} J_B R_a.
Gesucht: (1) Wirkung der Konjugate auf chi; (2) welches Konjugat bildet z_c = (1,1,1)/sqrt3 auf -z_c ab; (3) Fixpunkte; (4) als Symmetrie der
Verbindung: Flussdichte unter einer Drehung erhalten -> Kernpaar."""
import numpy as np

X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
zc = np.ones(3) / np.sqrt(3)


def rotz(phi):  # Drehung von chi um z um phi
    return np.cos(phi / 2) * np.eye(2) - 1j * np.sin(phi / 2) * Z


def R_dual(a):  # Dualitaetsdrehung um a: dreht chi um -2a
    return rotz(-2 * a)


def bloch_map(U):
    M = np.zeros((3, 3))
    P = [X, Y, Z]
    for i in range(3):
        for j in range(3):
            M[i, j] = 0.5 * np.real(np.trace(P[i] @ U @ P[j] @ U.conj().T))
    return M


C_chi = R_dual(np.pi)  # = rotz(-2 pi) = -1: auf Bloch-Vektoren die Identitaet
print("(0) C auf chi (Bloch):", np.round(bloch_map(C_chi), 6).tolist())
for a_deg in (0, 22.5, 45, 67.5, 90):
    a = np.radians(a_deg)
    U = R_dual(-a) @ Y @ R_dual(a)
    M = bloch_map(U)
    w, V = np.linalg.eig(M); ax = np.real(V[:, np.argmin(np.abs(w - 1))]); ax /= np.linalg.norm(ax)
    img = M @ zc
    print(f"(1) Rotor-Konjugat bei Dualitaetswinkel {a_deg:5.1f} Grad: Halbdrehung um Achse {np.round(ax, 4)}, z_c -> {np.round(img, 4)}"
          + ("   <- bildet z_c auf -z_c ab" if np.allclose(img, -zc, atol=1e-9) else ""))
M = bloch_map(R_dual(-np.radians(22.5)) @ Y @ R_dual(np.radians(22.5)))
oct_img = [M @ e for e in np.eye(3)]
print("(2) dieses Konjugat bildet den Oktanten (Ecken x, y, z) ab auf:", [np.round(v, 4).tolist() for v in oct_img])
print("(3) Fixpunkte auf chi: die beiden Achsenpunkte (Eigenkanaele); fixpunktfrei auf chi ist nur die Antipodenabbildung (antiunitaer, Theta).")
print("(4) det der Bloch-Matrix:", round(np.linalg.det(M), 6), "-> Drehung, erhaelt Orientierung und Flussdichte: als Symmetrie F(M n) = F(n),"
      " also Kern bei z_c => Kern bei -z_c (Kernpaar), wie bei Theta.")
