"""k39: Der Heisenberg-Kompensator C = (1 + J)/2 in Lesart B mit J = J_B (Strukturrechnung, kein Datenvergleich).

J_B z = i zbar, also E -> B, B -> E (v4.9.0-r02.3). Geprueft wird (v4.9.0-r03):
  1. Interferometer: C und A = (1 - J)/2 sind die beiden Ausgaenge eines Zweiarm-Interferometers mit J in einem Arm.
  2. antilineares J: C, A nur reell-linear; A(f) = -i C(i f), ran A = i ran C.
  3. Punktladung: J_B -> Feld einer magnetischen Ladung; C(f), A(f) -> Dyon-Felder (q/2, +-q/2).
  4. ebene Lichtwelle: J_B kehrt die Ausbreitungsrichtung um und dreht die Polarisation um 90 Grad.
  5. Produkt statt Summe: z x J_B z = 2 E x B (Poynting), orthogonal zu E und B; z . J_B z = i(E^2 + B^2).
"""
import numpy as np

rng = np.random.default_rng(39)
J = lambda z: 1j * np.conj(z)
C = lambda z: 0.5 * (z + J(z))
A = lambda z: 0.5 * (z - J(z))
s_of = lambda z: z @ z
z = rng.normal(size=3) + 1j * rng.normal(size=3)

print("1. Zweiarm-Interferometer: Ausgang 1 = (f + Jf)/2, Ausgang 2 = (f - Jf)/2")
print("   C + A = 1:", np.allclose(C(z) + A(z), z), "| C^2 = C:", np.allclose(C(C(z)), C(z)),
      "| C A = 0:", np.allclose(C(A(z)), 0))
ip = lambda u, v: np.real(np.vdot(u, v))
print("   Energieaufteilung |Cz|^2 + |Az|^2 = |z|^2:", np.isclose(ip(C(z), C(z)) + ip(A(z), A(z)), ip(z, z)),
      "| reell orthogonal Re<Cz, Az> = %.1e" % ip(C(z), A(z)))

print("\n2. Antilinearitaet")
print("   C(i z) = i C(z)?", np.allclose(C(1j * z), 1j * C(z)), "| C(i z) = i A(z):", np.allclose(C(1j * z), 1j * A(z)),
      "| A(z) = -i C(i z):", np.allclose(A(z), -1j * C(1j * z)))
print("   ran A = i ran C: i*C(z) ist J-ungerade:", np.allclose(J(1j * C(z)), -1j * C(z)))

print("\n3. Punktladung q am Ursprung, Feldpunkt r")
q = 1.0; r = np.array([0.3, -0.5, 0.8]); rh = r / np.linalg.norm(r); E0 = q * rh / (r @ r)
f = E0 + 0j
for name, w in (("f (Ladung)", f), ("J_B f", J(f)), ("C(f)", C(f)), ("A(f)", A(f))):
    E, B = w.real, w.imag
    qe = E @ rh * (r @ r); qm = B @ rh * (r @ r)
    print("   %-12s elektrische Ladung %+.2f, magnetische Ladung %+.2f, s = %s" % (name, qe, qm, np.round(s_of(w), 4)))

print("\n4. ebene Lichtwelle E = x, B = y (Ausbreitung +z)")
w = np.array([1, 1j, 0])
for name, v in (("Welle", w), ("J_B Welle", J(w)), ("T Welle (zbar)", np.conj(w))):
    E, B = v.real, v.imag
    print("   %-15s E = %s, B = %s, E x B = %s, s = %s" % (name, E, B, np.cross(E, B), s_of(v)))
print("   C(Welle):", np.round(C(w), 3), " s =", s_of(C(w)), "(kein Licht: E parallel B)")

print("\n5. Produkt statt Summe")
E, B = z.real, z.imag
cr = np.cross(z, J(z))
print("   z x J_B z = 2 E x B:", np.allclose(cr, 2 * np.cross(E, B)), "| reell:", np.allclose(cr.imag, 0))
print("   orthogonal zu E und B:", np.isclose(cr.real @ E, 0), np.isclose(cr.real @ B, 0))
print("   z . J_B z = i (E^2 + B^2):", np.isclose(z @ J(z), 1j * (E @ E + B @ B)))
u = 0.5 * (E @ E + B @ B); S = np.cross(E, B)
print("   u^2 - |S|^2 = |s|^2 / 4:", np.isclose(u * u - S @ S, abs(s_of(z)) ** 2 / 4))
print("   Licht (s = 0): |S| = u:", np.isclose(np.linalg.norm(np.cross(w.real, w.imag)), 0.5 * (w.real @ w.real + w.imag @ w.imag)))

print("\n6. Interferometer mit Dualitaetsphase phi im Referenzarm: D(phi) = |Ausgang 1|^2 - |Ausgang 2|^2")
def D(z, phi):
    a = np.exp(1j * phi) * z
    o1 = 0.5 * (a + J(z)); o2 = 0.5 * (a - J(z))
    return ip(o1, o1) - ip(o2, o2)
phis = np.linspace(0, 2 * np.pi, 9)
print("   D(phi) = Im(e^{i phi} s):", all(np.isclose(D(z, p), np.imag(np.exp(1j * p) * s_of(z))) for p in phis))
print("   D(0) = Im s = 2 E.B:", np.isclose(D(z, 0), 2 * (z.real @ z.imag)))
for name, v in (("Ladung (Materie)", f), ("J_B Ladung (Tachyon)", J(f)), ("Lichtwelle", w)):
    amp = max(abs(D(v, p)) for p in np.linspace(0, 2 * np.pi, 721)); tot = ip(v, v)
    ph = [round(D(v, p) / (amp or 1), 2) for p in (np.pi / 2, 3 * np.pi / 2)]
    print("   %-22s Sichtbarkeit |s|/|z|^2 = %.3f  D(pi/2), D(3pi/2) normiert: %s" % (name, amp / tot, ph))

print("\n7. Sichtbarkeit und Ruhesystem des Feldes (Landau-Lifschitz par. 25: v/(1+v^2) = |E x B|/(E^2 + B^2))")
def boost(E, B, n, eta):
    # aktive Lorentztransformation der Felder, Boost-Richtung n, Rapiditaet eta
    g, bv = np.cosh(eta), np.tanh(eta) * n
    Ep = g * (E + np.cross(bv, B)) - (g - 1) * (E @ n) * n
    Bp = g * (B - np.cross(bv, E)) - (g - 1) * (B @ n) * n
    return Ep, Bp
for k in range(3):
    zz = rng.normal(size=3) + 1j * rng.normal(size=3); E, B = zz.real, zz.imag
    S = np.cross(E, B); u = 0.5 * (E @ E + B @ B); n = S / np.linalg.norm(S)
    eta = 0.5 * np.arctanh(np.linalg.norm(S) / u)
    Ep, Bp = boost(E, B, n, eta)
    V = abs(s_of(zz)) / (2 * u)
    print("   Feld %d: nach Boost um eta = %.4f |E' x B'| = %.1e;  V = %.5f, 1/cosh(2 eta) = %.5f" %
          (k, eta, np.linalg.norm(np.cross(Ep, Bp)), V, 1 / np.cosh(2 * eta)))
eta_sym = np.arctanh(0.5495)
print("   Arithmetik bei eta_sym = %.4f: 1/cosh(2 eta) = %.4f, Energiegeschwindigkeit tanh(2 eta) = %.4f"
      % (eta_sym, 1 / np.cosh(2 * eta_sym), np.tanh(2 * eta_sym)))
