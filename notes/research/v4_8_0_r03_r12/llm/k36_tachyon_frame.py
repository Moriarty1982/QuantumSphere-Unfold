"""k36: Der Tachyon-Frame unter Holonomie und Spinorstruktur (Strukturrechnung, kein Datenvergleich).

(a) Dualitaet und SO(3,C) vertauschen -> gleiche Holonomie im Tachyon-Sektor
(b) Hauptspinoren (Hauptnullrichtungen) von z und i z
(c) Rapiditaet einer Ueberlichtgeschwindigkeit: artanh(v) = artanh(1/v) + i pi/2; Vorzeichenwechsel der Norm
(d) Kreuzterme aus r18 mit komplexer Tachyon-Rapiditaet
(e) Tribonacci-Bedingung aus thm:tribonacci als Identitaet in Rapiditaeten
"""
import numpy as np, cmath, math
rng = np.random.default_rng(36)

def rot_c(axis, theta):
    """komplexe Drehung um Achse (reell, normiert) um komplexen Winkel theta: Element von SO(3,C)."""
    a = np.asarray(axis, float); a = a/np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]], dtype=complex)
    return np.eye(3) + np.sin(theta)*K + (1-np.cos(theta))*(K@K)

s = lambda z: z@z

# (a) Boost mit Rapiditaet eta = Drehung um imaginaeren Winkel i*eta auf z = E + iB
print("(a) Dualitaet und Lorentz-Wirkung vertauschen")
zm = rng.normal(size=3) + 0j; zm *= 1/np.sqrt(s(zm).real) if s(zm).real > 0 else 1
for _ in range(3):
    L = rot_c(rng.normal(size=3), 1j*rng.normal()) @ rot_c(rng.normal(size=3), rng.normal())
    lhs, rhs = L @ (1j*zm), 1j*(L @ zm)
    print("   |L(iz) - i L(z)| = %.1e   s(z) = %+.3f, s(iz) = %+.3f, s(L iz) = %+.3f"
          % (abs(lhs-rhs).max(), s(zm).real, s(1j*zm).real, s(lhs).real))
print("   -> jede Schleife hat im Tachyon-Sektor dieselbe Holonomie wie ihr Materie-Bild (delta = 28,56 Grad fuer die Triole).")

# (b) Hauptspinoren: F11 = (z1 - i z2)/2, F22 = (-z1 - i z2)/2, F12 = -z3/2;  Wurzeln von F11 l^2 + 2 F12 l + F22
def principal(z):
    F11, F22, F12 = (z[0]-1j*z[1])/2, (-z[0]-1j*z[1])/2, -z[2]/2
    return np.sort_complex(np.roots([F11, 2*F12, F22]))
print("\n(b) Hauptspinoren (Verhaeltnis psi1/psi2) eines Materie-Feldes und seines Tachyon-Bildes")
print("   z  :", np.round(principal(zm), 6))
print("   i z:", np.round(principal(1j*zm), 6))
print("   -> identisch: Materie und Tachyon mit z_T = i z_M haben dieselben zwei Hauptnullrichtungen;")
print("      sie unterscheiden sich nur in der Gesamtphase des Spinorprodukts.")

# (c) Ueberlichtgeschwindigkeit
print("\n(c) Rapiditaet einer Ueberlichtgeschwindigkeit")
gL = 0.2375/(math.log(2)/(math.pi*math.sqrt(3))); b = math.sqrt((gL-1)/(gL+1)); eta = math.atanh(b)
v = 1/b
et = cmath.atanh(v)
print("   v = 1/beta_sym = %.5f:  artanh(v) = %.5f %+.5fi   (artanh(1/v) = %.5f, pi/2 = %.5f)"
      % (v, et.real, et.imag, math.atanh(1/v), math.pi/2))
u_m = np.array([math.cosh(eta), math.sinh(eta)])
u_t = np.array([cmath.cosh(eta+1j*math.pi/2), cmath.sinh(eta+1j*math.pi/2)])
norm = lambda u: -u[0]**2 + u[1]**2
w = (u_t/1j).real                                   # u_t = i * w mit reellem w
print("   u(eta + i pi/2) = i * w mit w = (%.4f, %.4f) = (sinh eta, cosh eta);  Norm von w: %+.4f (Materie: %+.4f)"
      % (w[0], w[1], norm(w), norm(u_m)))
print("   -> die reelle Vierergeschwindigkeit wird raumartig, der Faktor i traegt die Phase (komplexe Norm bleibt %+.4f)."
      % norm(u_t).real)
print("   Dualitaet alpha = pi/2 auf z: z_T = i z_M, s -> -s.  Gleiche Struktur: Phase pi/2, Vorzeichen der reellen Invariante gekippt.")
print("   Fuer Tachyonen tauschen cosh und sinh die Rollen (Energie ~ sinh, Impuls ~ cosh).")
print("   r82 (erlaubte Aussage): l_T^2 = -lambda_T^2, also l_T = i lambda_T - derselbe Faktor i.")

# (d) Kreuzterme mit komplexer Tachyon-Rapiditaet  (Tachyon bei -eta + i pi/2)
print("\n(d) Kreuzterme aus r18 mit Tachyon bei -eta + i pi/2")
pos = {"+": eta, "0": 0.0, "-": -eta + 1j*math.pi/2}
for a, c in [("+", "0"), ("0", "-"), ("+", "-")]:
    d = pos[a]-pos[c]; ch = cmath.cosh(d)
    print("   %s%s: Rapiditaet %.4f %+.4fi, cosh = %.4f %+.4fi, |cosh| = %.4f"
          % (a, c, d.real, d.imag, ch.real, ch.imag, abs(ch)))
print("   reell gerechnet (r18): +0 -> %.4f, +- -> %.4f = gamma_L" % (math.cosh(eta), math.cosh(2*eta)))

# (e) Tribonacci
T = 1.8392867552
bT = math.sqrt((T-1)/(T+1)); eT = math.atanh(bT)
print("\n(e) thm:tribonacci: mu = 1/beta_sym(mu).  In Rapiditaeten: cosh(2 eta) = coth(eta)")
print("   eta_T = %.6f:  cosh(2 eta) = %.6f,  coth(eta) = %.6f,  tanh(eta + i pi/2) = %s"
      % (eT, math.cosh(2*eT), 1/math.tanh(eT), cmath.tanh(eT+1j*math.pi/2)))
print("   -> die Fixpunktbedingung setzt den Lorentzfaktor des Gegenueber-Terms gleich der Geschwindigkeit")
print("      eines Tachyons mit reeller Rapiditaet eta.")
