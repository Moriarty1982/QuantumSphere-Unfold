"""OP3: eine Algebra je Frame-Abbildung, die vierte als Betrachter (Herleitung, Erkundung, nicht blind).

(1) Die vier Kopien von HS(8) tragen zwei Bits; die Frame-Abbildungen {1, R, T, J_B} bilden auf den Vorzeichen die Kleinsche Vierergruppe
    (r16.4(a)) und wirken auf chi als {1, sigma_z, sigma_x, sigma_y} (r16.7).  Pruefen: Bits (a,b) -> X^a Z^b ist bis auf Phase ein
    Gruppenisomorphismus Z2 x Z2 -> {1, R, T, J_B}.
(2) Auslesung je Frame-Kopie = Eigenzustand der Abbildung (r16.7) -> Oktant, Ueberlappung 1/2, Phase pi/4.
(3) Reiner Betrachter, generationssymmetrisch -> auf der Zyklusachse.  (a) Bilder F o des Betrachters: Tetraeder.  (b) Satz: Jede
    zyklussymmetrische reine Dreiergruppe auf chi liegt auf einem Kegel; Ueberlappung 1/2 legt den Kegel und damit die Phase pi/4 fest.
    Numerisch: Filter mit Achse = Zyklusachse (beliebige Staerke), danach Kegel neu auf Ueberlappung 1/2 gestellt.
(4) Gemischte Auslesungen rho_k = (1 + lam e_k . sigma)/2 (Betrachter verschraenkt mit den Frame-Kopien): Tr(rho_i rho_j) und
    arg Tr(rho_0 rho_1 rho_2) als Funktion von lam; noetiges lam fuer 2/3.  Keine Kandidatenwerte fuer lam ausgewertet.
"""
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
NAME = {(0, 0): "1", (0, 1): "R = sigma_z", (1, 0): "T = sigma_x", (1, 1): "J_B ~ sigma_y"}
OP = {(a, b): np.linalg.matrix_power(X, a) @ np.linalg.matrix_power(Z, b) for a in (0, 1) for b in (0, 1)}


def same_up_to_phase(A, B):
    k = np.vdot(A.ravel(), B.ravel()) / np.vdot(A.ravel(), A.ravel())
    return abs(abs(k) - 1) < 1e-12 and np.allclose(k * A, B)


print("(1) Kopien-Bits -> Frame-Abbildungen, Produkt = Bit-Summe mod 2 (bis auf Phase):")
ok = all(same_up_to_phase(OP[((a1 + a2) % 2, (b1 + b2) % 2)], OP[(a1, b1)] @ OP[(a2, b2)])
         for a1 in (0, 1) for b1 in (0, 1) for a2 in (0, 1) for b2 in (0, 1))
print("    ", {f"{a}{b}": NAME[(a, b)] for (a, b) in NAME}, "Homomorphismus:", ok,
      "| J_B-Kopie 11: X Z = -i sigma_y:", same_up_to_phase(Y, X @ Z))


def bloch_state(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def phase(g):
    return np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0]))


def ov2(a, b):
    return abs(np.vdot(a, b)) ** 2


octant = [bloch_state(v) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]          # +1-Eigenzustaende von R, T, J_B
print(f"(2) Oktant: Ueberlappungen^2 {[round(ov2(octant[i], octant[(i+1)%3]), 6) for i in range(3)]}, |Phase| = {abs(phase(octant)):.6f}"
      f" (pi/4 = {np.pi/4:.6f})")

n = np.ones(3) / np.sqrt(3); o = bloch_state(n)
imgs = [OP[(0, 1)] @ o, OP[(1, 0)] @ o, OP[(1, 1)] @ o]
print(f"(3a) Betrachter auf der Zyklusachse, Bilder F o: Ueberlappungen^2 mit o {[round(ov2(o, x), 6) for x in imgs]},"
      f" untereinander {[round(ov2(imgs[i], imgs[(i+1)%3]), 6) for i in range(3)]} (Tetraeder: 1/3), |Phase| = {abs(phase(imgs)):.6f}")


def cone_states(psi):
    e1 = np.cross(n, [1, 0, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
    return [bloch_state(np.cos(psi) * n + np.sin(psi) * (np.cos(2*np.pi*k/3) * e1 + np.sin(2*np.pi*k/3) * e2)) for k in range(3)]


def filt(g, mu):
    """reiner Filter exp(mu n.sigma) mit der Zyklusachse (kommutiert mit der Drehung um n) -> wieder ein Kegel"""
    ns = n[0] * X + n[1] * Y + n[2] * Z
    F = np.cosh(mu) * I2 + np.sinh(mu) * ns
    return [F @ x / np.linalg.norm(F @ x) for x in g]


print("(3b) Filter mit Achse n, Kegel jeweils auf Ueberlappung 1/2 gestellt:")
for mu in (-1.0, -0.3, 0.3, 1.0):
    f = lambda p: ov2(*filt(cone_states(p), mu)[:2]) - 0.5
    xs = np.linspace(1e-3, np.pi - 1e-3, 4001); vs = [f(x) for x in xs]
    roots = []
    for i in range(len(xs) - 1):
        if np.sign(vs[i]) != np.sign(vs[i + 1]):
            lo, hi = xs[i], xs[i + 1]
            for _ in range(70):
                m = (lo + hi) / 2
                (lo, hi) = (m, hi) if np.sign(f(m)) == np.sign(f(lo)) else (lo, m)
            roots.append((lo + hi) / 2)
    print(f"     mu = {mu:+.1f}: |Phase| bei den Loesungen {[round(abs(phase(filt(cone_states(r), mu))), 6) for r in roots]}")

print("(4) gemischte Auslesungen rho_k = (1 + lam e_k.sigma)/2 auf dem Oktanten:")
E = [np.array(v, float) for v in ([0, 0, 1], [1, 0, 0], [0, 1, 0])]
for lam in (1.0, 0.75, 0.5):
    rho = [(I2 + lam * (e[0] * X + e[1] * Y + e[2] * Z)) / 2 for e in E]
    t3 = np.trace(rho[0] @ rho[1] @ rho[2])
    print(f"     lam = {lam:.2f}: Tr(rho_i rho_j) = {np.trace(rho[0] @ rho[1]).real:.6f}, Tr(rho_i^2) = {np.trace(rho[0] @ rho[0]).real:.6f},"
          f" |arg Tr(rho0 rho1 rho2)| = {abs(np.angle(t3)):.6f}, arctan(lam^3) = {np.arctan(lam**3):.6f}")
lam_star = np.tan(0.666665) ** (1 / 3)
print(f"     noetig fuer |Phase| = 0.666665: lam^3 = tan(0.666665) = {np.tan(0.666665):.6f}, lam = {lam_star:.6f}")
