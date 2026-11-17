"""Ist das flussentgegengesetzte Beobachterpaar aus r11.5(b) das Paar (M, T)?  (Erkundung, analytisch vorher entschieden.)

Boost mit Geschwindigkeit v entlang n: E' = g(E + v n x B) - (g-1)(n.E)n,  B' = g(B - v n x E) - (g-1)(n.B)n  (c = 1).
(1) Ein Boost laesst s = (E + iB)^2 fest.  Frame-Abbildungen: R (E,B)->(-B,E): s -> -s;  T (E,B)->(E,-B): s -> conj s;  J_B (E,B)->(B,E): s -> -conj s.
    Konvention F: T-Frame = J_B-Bild von M; ein Materiefeld (s > 0) geht auf s < 0 (Tachyonseite).  Kein reeller Boost kann das.
(2) Was das Paar ist: vom flussfreien Profil (R) aus um +eta und -eta geboostet; beide sehen r = |s|/u = 1/cosh 2 eta, entgegengesetzten Fluss,
    gleiches s; Abstand: Drehung um pi.  Relativer Lorentz-Faktor cosh 2 eta.
(3) Energiedichte: u(eta)/u(R) = cosh 2 eta.
(4) Imaginaere Rapiditaet: Boost um i pi/2 (komplexe Lorentz-Transformation) schickt die Breite tanh^2 eta auf coth^2 eta (x -> 1/x), vgl. p_position.py.
"""
import numpy as np
rng = np.random.default_rng(9)

def boost(E, B, n, v):
    g = 1 / np.sqrt(1 - v * v)
    Ep = g * (E + v * np.cross(n, B)) - (g - 1) * np.dot(n, E) * n
    Bp = g * (B - v * np.cross(n, E)) - (g - 1) * np.dot(n, B) * n
    return Ep, Bp

s = lambda E, B: (E + 1j * B) @ (E + 1j * B)
u = lambda E, B: 0.5 * (E @ E + B @ B)
dev = 0.0
for _ in range(500):
    E, B = rng.normal(size=3), rng.normal(size=3); n = rng.normal(size=3); n /= np.linalg.norm(n); v = rng.uniform(-0.95, 0.95)
    dev = max(dev, abs(s(*boost(E, B, n, v)) - s(E, B)))
print(f"(1) Boost laesst s fest: max. Abweichung {dev:.1e}.  Materiefeld s = 1 -> J_B-Bild s = {-np.conj(1+0j).real:+.0f} (Tachyonseite): kein Boost verbindet M mit T.")

# (2) Feld im flussfreien Profil R: reines E (s > 0, Materie), dann +-eta entlang z
beta = 0.549406; eta = np.arctanh(beta)
E0, B0 = np.array([1.0, 0, 0]), np.zeros(3); z = np.array([0, 0, 1.0])
Ep, Bp = boost(E0, B0, z, np.tanh(eta)); Em, Bm = boost(E0, B0, z, -np.tanh(eta))
P = lambda E, B: np.cross(E, B)
r = lambda E, B: abs(s(E, B)) / (2 * u(E, B))
print(f"(2) Beobachter +eta: r = {r(Ep,Bp):.4f}, Fluss {P(Ep,Bp).round(4)};  -eta: r = {r(Em,Bm):.4f}, Fluss {P(Em,Bm).round(4)};  1/cosh 2eta = {1/np.cosh(2*eta):.4f}")
Rx = np.diag([1, -1, -1])   # Drehung um pi um die x-Achse
print(f"    s gleich: {abs(s(Ep,Bp)-s(Em,Bm)):.1e};  -eta-Feld = Drehung um pi des +eta-Feldes: {np.allclose(Rx@Ep, Em) and np.allclose(Rx@Bp, Bm)}")
g_rel = np.cosh(2 * eta)
print(f"    relativer Lorentz-Faktor zwischen beiden = cosh 2 eta = {g_rel:.6f} = gamma_L")
print(f"(3) Energiedichte u(+eta)/u(R) = {u(Ep,Bp)/u(E0,B0):.6f} = cosh 2 eta")
# T-Abbildung (E, -B) auf einem Feld mit E.B = 0 ist eine Drehung um pi um E
E1, B1 = np.array([2.0, 0, 0]), np.array([0, 1.0, 0])
print(f"    T-Bild (E,-B) eines Feldes mit E.B = 0 gleich Drehung um pi um E: {np.allclose(Rx@E1, E1) and np.allclose(Rx@B1, -B1)}")
x = np.tanh(eta) ** 2; xT = np.tanh(eta + 1j * np.pi / 2) ** 2
print(f"(4) Breite x = tanh^2 eta = {x:.4f}; bei eta + i pi/2: {xT.real:.4f} = 1/x = {1/x:.4f} (Tachyon-Ast, Konvention F)")
