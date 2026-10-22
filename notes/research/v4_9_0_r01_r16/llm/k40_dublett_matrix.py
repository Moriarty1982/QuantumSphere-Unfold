"""k40: Kompensator als 2x2-Matrix auf dem (E, B)-Dublett (Strukturrechnung, kein Datenvergleich).

F = [E | B] in R^{3x2} statt z = E + iB in C^3. Geprueft wird (v4.9.0-r04):
  1. Dualitaet, J_B, T, C wirken als reelle 2x2-Matrizen von rechts (O(2)); Drehungen von links; Boosts faktorisieren nicht.
  2. Kompensator C_HC = (1 + sx)/2, Partner (1 - sx)/2: gewoehnliche orthogonale Projektoren; Enigma-Relation als Matrixidentitaet.
  3. Zustandsmatrix G = F^T F = u 1 + (Re s sz + Im s sx)/2, det G = |E x B|^2; Bloch-Vektor b = (Re s, Im s)/2u, |b| = 1/cosh 2 eta_f.
  4. Boosts: s fest, u waechst, b schrumpft Richtung Mitte (Licht).
  5. Interferometer: Ausgangsenergie u + E.B = 2u tr(rho C_HC); D(phi) = 2u b.n_phi.
  6. Leckdiagnosen in Matrixform.
"""
import numpy as np

rng = np.random.default_rng(40)
sx = np.array([[0., 1], [1, 0]]); sz = np.array([[1., 0], [0, -1]]); I2 = np.eye(2)
Rm = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])
toF = lambda z: np.column_stack([z.real, z.imag])
toz = lambda F: F[:, 0] + 1j * F[:, 1]
Chc = 0.5 * (I2 + sx); Ahc = 0.5 * (I2 - sx)


def boost(F, n, eta):
    E, B = F[:, 0], F[:, 1]
    g, bv = np.cosh(eta), np.tanh(eta) * n
    Ep = g * (E + np.cross(bv, B)) - (g - 1) * (E @ n) * n
    Bp = g * (B - np.cross(bv, E)) - (g - 1) * (B @ n) * n
    return np.column_stack([Ep, Bp])


def rot3(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


z = rng.normal(size=3) + 1j * rng.normal(size=3); F = toF(z)
s = z @ z; E, B = F[:, 0], F[:, 1]; u = 0.5 * (E @ E + B @ B)

print("1. Operationen als 2x2-Matrizen von rechts")
a = 0.7
print("   Dualitaet e^{ia}: F R(a)^T:", np.allclose(toF(np.exp(1j * a) * z), F @ Rm(a).T))
print("   J_B = i zbar:     F sx:     ", np.allclose(toF(1j * np.conj(z)), F @ sx))
print("   T = zbar:         F sz:     ", np.allclose(toF(np.conj(z)), F @ sz))
print("   C = -z:           F (-1):   ", np.allclose(toF(-z), -F))
print("   sx, sz Spiegelungen, R(a) Drehungen: O(2); sx R(a) = R(-a) sx:", np.allclose(sx @ Rm(a), Rm(-a) @ sx))
R3 = rot3([1, 2, -1], 0.9)
print("   Drehung wirkt von links, vertauscht mit allen rechten Matrizen:", np.allclose((R3 @ F) @ sx, R3 @ (F @ sx)))
n = np.array([0, 0, 1.])
Fb = boost(F, n, 0.6)
print("   Boost von der Form L F M?  vertauscht mit sx:", np.allclose(boost(F @ sx, n, 0.6), Fb @ sx))

print("\n2. Kompensator als Matrix")
print("   C_HC^2 = C_HC, C_HC A = 0, symmetrisch:", np.allclose(Chc @ Chc, Chc), np.allclose(Chc @ Ahc, 0), np.allclose(Chc, Chc.T))
print("   F C_HC = Kompensator aus r02/r03:", np.allclose(F @ Chc, toF(0.5 * (z + 1j * np.conj(z)))))
print("   Enigma: R(pi/2)^T... rechts: F R(a)^T sx R(a)^T^-1 bei a = pi/2 gleich F (-sx):",
      np.allclose(Rm(np.pi / 2).T @ sx @ np.linalg.inv(Rm(np.pi / 2).T), -sx))

print("\n3. Zustandsmatrix G = F^T F")
G = F.T @ F
print("   G = u 1 + (Re s sz + Im s sx)/2:", np.allclose(G, u * I2 + 0.5 * (s.real * sz + s.imag * sx)))
print("   det G = |E x B|^2:", np.isclose(np.linalg.det(G), np.cross(E, B) @ np.cross(E, B)))
print("   u^2 - det G = |s|^2/4:", np.isclose(u * u - np.linalg.det(G), abs(s) ** 2 / 4))
b = np.array([s.real, s.imag]) / (2 * u)
S = np.cross(E, B); eta_f = 0.5 * np.arctanh(np.linalg.norm(S) / u)
print("   |b| = %.5f, 1/cosh(2 eta_f) = %.5f" % (np.linalg.norm(b), 1 / np.cosh(2 * eta_f)))
bd = lambda F: (lambda G: np.array([G[0, 0] - G[1, 1], 2 * G[0, 1]]) / np.trace(G))(F.T @ F)
print("   Dualitaet a dreht b um 2a:", np.allclose(bd(F @ Rm(a).T), Rm(2 * a) @ b))
print("   J_B: b -> (-b1, b2):", np.allclose(bd(F @ sx), [-b[0], b[1]]), "| T: b -> (b1, -b2):", np.allclose(bd(F @ sz), [b[0], -b[1]]))
print("   kein sy-Anteil: G symmetrisch:", np.allclose(G, G.T))

print("\n4. Boost entlang E x B")
nS = S / np.linalg.norm(S)
for eta in (0.0, 0.5 * eta_f, eta_f, 2 * eta_f, 3.0):
    Fe = boost(F, nS, eta); ze = toz(Fe); Ge = Fe.T @ Fe; ue = np.trace(Ge) / 2
    print("   eta = %+.3f: s = %s, u = %8.3f, |b| = %.4f, |E x B| = %.4f" %
          (eta, np.round(ze @ ze, 5), ue, np.linalg.norm(bd(Fe)), np.linalg.norm(np.cross(Fe[:, 0], Fe[:, 1]))))

print("\n5. Interferometer als Messung von b")
print("   Ausgang 1: |F C_HC|^2 = u + E.B = 2u tr(rho C_HC):",
      np.isclose(np.sum((F @ Chc) ** 2), u + E @ B), np.isclose(np.sum((F @ Chc) ** 2), np.trace(G @ Chc)))
for phi in (0.0, 0.8, 2.0):
    D = np.imag(np.exp(1j * phi) * s)
    print("   phi = %.1f: D = Im(e^{i phi} s) = %.5f, 2u b.(sin phi, cos phi) = %.5f" % (phi, D, 2 * u * b @ [np.sin(phi), np.cos(phi)]))

print("\n6. Leckdiagnosen in Matrixform (J = sx rechts, C = C_HC rechts)")
def leak(M):
    comm = np.linalg.norm(M(F @ sx) - M(F) @ sx) / np.linalg.norm(F)
    X = M(F @ Chc); lk = np.linalg.norm(X @ Ahc) / np.linalg.norm(F @ Chc)
    return comm, lk
for name, M in (("Drehung (links)", lambda X: R3 @ X), ("Boost eta = 0.6174", lambda X: boost(X, n, 0.6174)),
                ("Dualitaet a = 0.4 (rechts)", lambda X: X @ Rm(0.4).T)):
    c, l = leak(M)
    print("   %-26s |[M,J]|/|F| = %.4f   |(1-C) M C|/|FC| = %.4f" % (name, c, l))
