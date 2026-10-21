"""k41: Millennium-Matrix auf dem Dublett, dritte Achse und Kerr, Photon aus Materie + Tachyon (Strukturrechnung).

Kein Datenvergleich. Geprueft wird (v4.9.0-r05):
  a. Kommutant von J = sx und C_HC = (1 + sx)/2 in den reellen 2x2-Matrizen: genau lambda_+ C + lambda_- A.
     Welche Transporte von Lesart B erfuellen (T4) M J = J M, M C = C M?
  b. komplexe Amplituden: hermitesche Zustandsmatrix, sy-Anteil -2 Im(E*.B) = Helizitaet (zirkular).
     Kerr: Psi_2 = -M/(r - i a cos th)^3; Im(Psi_2^2) (Pontrjagin-Anteil) wechselt das Vorzeichen zwischen den Halbkugeln.
  c. Materie + Tachyon gleicher |s|: s(z_M + z_T) = 2 z_M.z_T; Photon genau bei Orthogonalitaet.
     Rueckweg eines Photons zum Ursprung des Tachyons: Ankunft immer nach dem Abflug.
"""
import numpy as np

rng = np.random.default_rng(41)
sx = np.array([[0., 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1., 0], [0, -1]]); I2 = np.eye(2)
Chc = 0.5 * (I2 + sx); Ahc = 0.5 * (I2 - sx)
Rm = lambda a: np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])

print("a. Kommutant von sx (und damit von C_HC) in M_2(R)")
# lineare Bedingung M sx = sx M, Basis der Loesungen
basis = [np.array(v, float).reshape(2, 2) for v in np.eye(4)]
Acon = np.array([(b @ sx - sx @ b).ravel() for b in basis]).T
null = np.linalg.svd(Acon)[2][np.sum(np.linalg.svd(Acon)[1] > 1e-12):]
print("   Dimension des Kommutanten:", len(null))
for v in null:
    M = v.reshape(2, 2); lp = np.trace(M @ Chc); lm = np.trace(M @ Ahc)
    print("   Basiselement ist lambda_+ C + lambda_- A:", np.allclose(M, lp * Chc + lm * Ahc))
for name, M in (("Dualitaet a = 0.4", Rm(0.4)), ("Dualitaet pi (= C)", Rm(np.pi)), ("T = sz", sz), ("J_B = sx", sx),
                ("e^{t sx}, t = 0.6174", np.cosh(0.6174) * I2 + np.sinh(0.6174) * sx)):
    print("   %-22s [M, sx] = 0: %-5s  [M, C_HC] = 0: %s" % (name, np.allclose(M @ sx, sx @ M), np.allclose(M @ Chc, Chc @ M)))
t = 0.6174; M = np.cosh(t) * I2 + np.sinh(t) * sx
print("   e^{t sx} = e^t C + e^-t A:", np.allclose(M, np.exp(t) * Chc + np.exp(-t) * Ahc),
      "| erhaelt Re s (M^T sz M = sz):", np.allclose(M.T @ sz @ M, sz))
print("   Spektralprojektor: Eigenraum zu e^t ist ran C_HC:", np.allclose(M @ Chc, np.exp(t) * Chc))

print("\nb. komplexe Amplituden, dritte Achse")
E = np.array([1, 1j, 0]) / np.sqrt(2); B = -1j * E            # zirkulare Welle laengs +z, B = z x E
for name, (Ee, Bb) in (("zirkular", (E, B)), ("zirkular, andere Helizitaet", (np.conj(E), np.conj(B))),
                       ("linear", (np.array([1, 0, 0j]), np.array([0, 1, 0j])))):
    F = np.column_stack([Ee, Bb]); G = F.conj().T @ F
    comp = [np.real(np.trace(G @ P)) / np.real(np.trace(G)) for P in (sz, sx, sy)]
    print("   %-28s (sz, sx, sy)-Anteil = %s,  -2 Im(E*.B)/tr = %.3f" % (name, np.round(comp, 3), -2 * np.imag(np.vdot(Ee, Bb)) / np.real(np.trace(G))))
print("   Kerr, Psi_2 = -M/(r - i a cos th)^3, M = 1, a = 0.9, r = 3:")
for th in (np.pi / 4, np.pi / 2, 3 * np.pi / 4):
    p2 = -1 / (3 - 1j * 0.9 * np.cos(th)) ** 3
    print("     th = %5.1f Grad: Psi_2 = %s, Im(Psi_2^2) = %+.5f" % (np.degrees(th), np.round(p2, 5), np.imag(p2 ** 2)))
print("   Schwarzschild (a = 0): Im(Psi_2^2) =", np.imag((-1 / 3 ** 3) ** 2))

print("\nc. Materie + Tachyon gleicher |s|")
a = 1.0; zM = np.array([a, 0, 0], complex)
for th in (0, np.pi / 4, np.pi / 2):
    zT = 1j * a * np.array([np.cos(th), np.sin(th), 0])
    z = zM + zT; s = z @ z; Ef, Bf = z.real, z.imag; u = 0.5 * (Ef @ Ef + Bf @ Bf)
    print("   Winkel %5.1f Grad: s(z_M)=%s s(z_T)=%s s(Summe)=%s = 2 z_M.z_T: %s, b = %s, |E x B|/u = %.3f, Fluss %s" %
          (np.degrees(th), np.round(zM @ zM, 3), np.round(zT @ zT, 3), np.round(s, 3), np.isclose(s, 2 * zM @ zT),
           np.round(np.array([s.real, s.imag]) / (2 * u), 3), np.linalg.norm(np.cross(Ef, Bf)) / u, np.round(np.cross(Ef, Bf), 3)))
print("   Rueckweg: Tachyon O=(0,0) -> K=(d/v, d), Photon K -> P=(d/v + d, 0)")
v, d = 1 / 0.5495, 1.0
O = np.array([0, 0.]); K = np.array([d / v, d]); P = np.array([d / v + d, 0.])
for uu in (0.0, 0.5, 0.6, 0.9):
    g = 1 / np.sqrt(1 - uu * uu); tp = lambda X: g * (X[0] - uu * X[1])
    print("     Beobachter u = %.1f: t'(O) = %+.3f, t'(K) = %+.3f, t'(P) = %+.3f  (Reihenfolge O,K vertauscht: %s)" %
          (uu, tp(O), tp(K), tp(P), tp(K) < tp(O)))
print("   P - O zeitartig, Zukunft: %s; Verzug d(1 + 1/v) = %.4f d" % ((P - O)[0] > abs((P - O)[1]), 1 + 1 / v))
