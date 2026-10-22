"""k38: Rundlauf um das Photon und Umkehrwalze in Lesart B (Strukturrechnung, kein Datenvergleich).

z = E + iB in C^3, s = z.z = E^2 - B^2 + 2i E.B, SO(3,C) = SO+(1,3), Dualitaet z -> e^{i alpha} z.
Geprueft wird (v4.9.0-r02):
  1. Rundlauf M -> P -> T -> P -> M: gleicher Drehsinn -> z -> -z, Rueckweg auf demselben Weg -> z -> z.
  2. z -> -z ist auf den Feldstaerken C (E, B ungerade) = PT = Dualitaet um pi; zentral.
  3. keine C-lineare Involution vertauscht Materie und Tachyon; antilinear: J z = i R zbar, R R^bar = 1.
  4. J_B z = i zbar (E <-> B): Eigenkanaele auf den beiden imaginaeren Halbachsen, Projektorbild.
  5. J_B kehrt den Drehsinn der Dualitaet um; Enigma-Komposit R^-1 J_B R bei alpha = pi/2 ist -J_B.
  6. Leckdiagnosen [M, J], (1-C) M C fuer reelle Drehungen und Boosts.
"""
import numpy as np

rng = np.random.default_rng(38)
dot = lambda a, b: a @ b
s_of = lambda z: dot(z, z)


def rand_z():
    return rng.normal(size=3) + 1j * rng.normal(size=3)


def rot(axis, ang):
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def complex_rot(axis, ang):
    # exp(ang K) mit komplexem Winkel; ang = i*eta ist ein Boost in SO(3,C)
    a = np.asarray(axis, float); a /= np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]], complex)
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


J_B = lambda z: 1j * np.conj(z)
C_hc = lambda z: 0.5 * (z + J_B(z))
EB = lambda z: (z.real, z.imag)

print("1. Rundlauf um das Photon (z = sqrt(s) n, n reell, n.n = 1)")
n = np.array([1.0, 0, 0]); a = 2.0
def transport(theta_path):
    # stetige Wurzel entlang s = a e^{i theta}
    return np.sqrt(a) * np.exp(1j * theta_path[-1] / 2) * n
z0 = np.sqrt(a) * n
same = transport(np.linspace(0, 2 * np.pi, 400))          # hin oben, zurueck unten
retr = transport(np.concatenate([np.linspace(0, np.pi, 200), np.linspace(np.pi, 0, 200)]))
half = transport(np.linspace(0, np.pi, 200))
print("   M -> T (oben):           z/z0 = %s, s = %.3f" % (np.round(half[0] / z0[0], 6), s_of(half).real))
print("   gleicher Drehsinn:       z/z0 = %s  (Z2-Holonomie)" % np.round(same[0] / z0[0], 6))
print("   derselbe Weg zurueck:    z/z0 = %s" % np.round(retr[0] / z0[0], 6))
z = rand_z()
print("   Seite des Durchgangs = sign Im s = sign(E.B); Lorentz-invariant:",
      np.isclose(s_of(complex_rot([1, 2, 3], 0.7j) @ z), s_of(z)))

print("\n2. z -> -z auf den Feldstaerken (Paritaeten nach Jackson, Tab. 6.1)")
E, B = EB(z)
P = lambda z: -E + 1j * B; T = lambda z: E - 1j * B; Cc = lambda z: -E - 1j * B
PT = -(E) - 1j * B   # P nach T: E -> -E, B -> -B
print("   C: z -> -z:", np.allclose(Cc(z), -z), "| PT: z -> -z:", np.allclose(PT, -z),
      "| Dualitaet pi:", np.allclose(np.exp(1j * np.pi) * z, -z))
print("   T: z -> zbar:", np.allclose(T(z), np.conj(z)), "| P: z -> -zbar:", np.allclose(P(z), -np.conj(z)))
print("   E.B (Im s / 2) unter P, T, C:", [round(float(np.imag(s_of(w)) / np.imag(s_of(z))), 3) for w in (P(z), T(z), Cc(z))])
L = complex_rot([0.3, -1, 2], 0.4 + 0.9j)
print("   -1 zentral: [Lambda, -1] = 0, [e^{i a}, -1] = 0 (trivial); Projektor (1 + (-1))/2 = 0")

print("\n3. Involutionen, die Materie und Tachyon vertauschen")
print("   C-linear: L = iM, M in O(3,C), L^2 = 1 => M^2 = -1 => det(M)^2 = -1: unmoeglich (det M = +-1).")
for name, R in (("R = 1 (J_B)", np.eye(3)), ("R reell, Drehung 1.1", rot([1, 1, 0], 1.1)),
                ("R reell, Drehung pi", rot([1, 1, 0], np.pi)),
                ("R = Boost^2", complex_rot([0, 0, 1], 0.8j) @ complex_rot([0, 0, 1], 0.8j))):
    Jr = lambda w, R=R: 1j * R @ np.conj(w)
    ok_inv = np.allclose(Jr(Jr(z)), z)
    ok_s = np.isclose(s_of(Jr(z)), -np.conj(s_of(z)))
    print("   %-22s J^2 = 1: %s   s -> -sbar: %s   (R Rbar = 1: %s)" % (name, ok_inv, ok_s, np.allclose(R @ np.conj(R), np.eye(3))))

print("\n4. J_B z = i zbar")
E2, B2 = EB(J_B(z))
print("   E' = B, B' = E:", np.allclose(E2, B) and np.allclose(B2, E), "| J_B^2 = 1:", np.allclose(J_B(J_B(z)), z))
print("   = Dualitaet(pi/2) nach T:", np.allclose(1j * T(z), J_B(z)))
print("   Nullkegel -> Nullkegel:", np.isclose(s_of(J_B(np.array([1, 1j, 0]))), 0))
ev = C_hc(z); od = 0.5 * (z - J_B(z))
print("   gerader Kanal  (E = B):  s = %s   (Re s = 0, Im s > 0)" % np.round(s_of(ev), 4))
print("   ungerader Kanal (E = -B): s = %s   (Re s = 0, Im s < 0)" % np.round(s_of(od), 4))
print("   Bild von C = (1 + J_B)/2 ist nie null ausser z_even = 0:", abs(s_of(ev)) > 1e-9)
pts = [C_hc(rand_z()) for _ in range(1000)]
print("   1000 Proben: max |Re s| = %.1e, min Im s = %.3f" % (max(abs(s_of(p).real) for p in pts), min(s_of(p).imag for p in pts)))

print("\n5. J_B und Dualitaetsdrehung R_a z = e^{i a} z")
for al in (0.3, 1.0):
    print("   J_B R_a = R_-a J_B (a = %.1f):" % al, np.allclose(J_B(np.exp(1j * al) * z), np.exp(-1j * al) * J_B(z)))
for al, lab in ((np.pi / 4, "pi/4"), (np.pi / 2, "pi/2 (M -> T)"), (np.pi, "pi")):
    comp = np.exp(-1j * al) * J_B(np.exp(1j * al) * z)
    print("   R_a^-1 J_B R_a, a = %-14s = %s" % (lab,
          "J_B" if np.allclose(comp, J_B(z)) else "-J_B" if np.allclose(comp, -J_B(z))
          else "T (z -> zbar)" if np.allclose(comp, np.conj(z)) else "?"))

print("\n6. Leckdiagnosen des Hauptkorpus (def:working-shared-matrix-leakage) mit J = J_B")
for name, M in (("reelle Drehung", rot([1, 2, -1], 0.9)), ("Boost eta = 0.6174", complex_rot([0, 0, 1], 0.6174j)),
                ("Dualitaet a = 0.4", np.exp(0.4j) * np.eye(3))):
    comm = np.linalg.norm(M @ J_B(z) - J_B(M @ z)) / np.linalg.norm(z)
    zc = C_hc(z); Mz = M @ zc
    leak = np.linalg.norm(0.5 * (Mz - J_B(Mz))) / np.linalg.norm(zc)
    print("   %-20s |[M,J]z|/|z| = %.4f   |(1-C) M C z|/|Cz| = %.4f" % (name, comm, leak))

print("\n7. Spinorhebung (r06.4): z(e^{i phi} psi) = e^{2 i phi} z(psi)")
zpsi = lambda p: np.array([p[0] ** 2 - p[1] ** 2, 1j * (p[0] ** 2 + p[1] ** 2), -2 * p[0] * p[1]])
psi = rng.normal(size=2) + 1j * rng.normal(size=2)
print("   phi = pi/2: z -> -z:", np.allclose(zpsi(1j * psi), -zpsi(psi)), "| psi -> -psi laesst z fest:", np.allclose(zpsi(-psi), zpsi(psi)))
print("   ein Rundlauf: psi -> i psi; zwei Rundlaeufe: psi -> -psi (720-Grad-Periode)")
