"""Koide-Phase und die Helizitaetsachse des (E,B)-Dubletts (Erkundung, nicht blind).

Bezug: v4.9.0-r04.2 (Zustandsscheibe), r05.2(b) (dritte Achse = Helizitaet, sigma_y-Teil -2 Im(E*.B)),
r51 (z -> iz als sigma_y; Ports als Eigenraeume von iL_e7), v4.10.0-r07.2 (Dualitaet vertauscht mit Boosts).
Aufruf: python helicity_axis.py <Pfad zu notes/research/v4_10_0_r32_r33/llm>
"""
import sys, os
import numpy as np

rng = np.random.default_rng(1115)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)

def stokes(E, B):
    F = np.stack([E, B], axis=1)            # 3x2
    G = F.conj().T @ F
    t = np.trace(G).real
    return np.array([np.trace(G @ s).real / t for s in (sz, sx, sy)])   # (b1, b2, by)

# (1) z -> iz auf (E,B): (E,B) -> (-B,E) ist die Dualitaetsdrehung um 90 Grad; Wirkung auf den Stokes-Vektor
E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
b0, bR = stokes(E, B), stokes(-B, E)
print("(1) Dualitaetsdrehung 90 Grad:", np.round(b0, 4), "->", np.round(bR, 4),
      "| b1,b2 kippen, by bleibt:", np.allclose(bR, b0 * [-1, -1, 1]))
bT = stokes(E, -B)                      # T: z -> conj z mit z = E + iB, d.h. (E,B) -> (E,-B), linear fortgesetzt
bJ = stokes(B, E)                       # J_B = R o T: (E,B) -> (E,-B) -> (B,E)
print("    T: (E,B)->(E,-B):", np.allclose(bT, b0 * [1, -1, -1]), " J_B: (E,B)->(B,E):", np.allclose(bJ, b0 * [-1, 1, -1]),
      "  (T und J_B kippen by, R erhaelt by)")

# (2) Ebene Wellen: zirkular -> by = +-1, linear -> 0 (r05.2(b))
k = np.array([0, 0, 1.0])
for name, Eh in (("zirkular +", np.array([1, 1j, 0]) / np.sqrt(2)), ("zirkular -", np.array([1, -1j, 0]) / np.sqrt(2)),
                 ("linear", np.array([1, 0, 0.0]))):
    print(f"(2) {name}: Stokes {np.round(stokes(Eh, np.cross(k, Eh)), 4)}")

# (3) Oktant: Summe der quadrierten by-Komponenten = 1 fuer jede Drehung; ebene Tripel haben Phase 0 oder pi
def rand_rot():
    q, r = np.linalg.qr(rng.normal(size=(3, 3))); return q * np.sign(np.diag(r))
dev = max(abs(sum(rand_rot()[:, 2] ** 2) - 1) for _ in range(1000))
print(f"(3) Oktant (drei orthonormale Bloch-Vektoren): Summe by^2 = 1, max. Abweichung {dev:.1e}")
def state(n):
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
# Bloch-Koordinaten hier (x,y,z) = (b2, by, b1); ebene Tripel: by = 0
ph_flat = []
for _ in range(500):
    a = rng.uniform(0, 2 * np.pi, 3); ns = [np.array([np.cos(t), 0, np.sin(t)]) for t in a]
    s = [state(n) for n in ns]
    ph_flat.append(abs(np.angle(np.vdot(s[0], s[1]) * np.vdot(s[1], s[2]) * np.vdot(s[2], s[0]))))
ph_flat = np.array(ph_flat)
print(f"    Tripel in der Scheibe (by = 0): Bargmann-Phase stets 0 oder pi: "
      f"{np.all((ph_flat < 1e-9) | (abs(ph_flat - np.pi) < 1e-9))}")

# (4) Boosts: Dualitaet vertauscht mit Boosts; was passiert mit by?
def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    Ep = g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n
    Bp = g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n
    return Ep, Bp
chg_y, chg_hel, comm = 0.0, 0.0, 0.0
for _ in range(300):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    v, n = rng.uniform(0.1, 0.9), rng.normal(size=3)
    Ep, Bp = boost(E, B, v, n)
    chg_y = max(chg_y, abs(stokes(Ep, Bp)[2] - stokes(E, B)[2]))
    Fp, Fm = E + 1j * B, E - 1j * B                       # Helizitaetsanteile (Riemann-Silberstein)
    Fpp = Ep + 1j * Bp
    # F+ transformiert nur mit sich selbst: Fpp haengt nur von Fp ab
    E2, B2 = boost(Fp / 2, Fp / (2j), v, n)               # Feld mit reinem F+-Anteil
    chg_hel = max(chg_hel, np.linalg.norm((E2 - 1j * B2)))  # F- bleibt null
    Er, Br = boost(-B, E, v, n); Rb = (-Bp, Ep)
    comm = max(comm, np.linalg.norm(Er - Rb[0]) + np.linalg.norm(Br - Rb[1]))
print(f"(4) Boost: by aendert sich (max. |Delta by| = {chg_y:.3f}); reine Helizitaetsanteile bleiben rein "
      f"(F- nach Boost {chg_hel:.1e}); Dualitaet vertauscht mit Boost ({comm:.1e})")

# (5) Ports von r51 und die sigma_y-Pole
sys.path.insert(0, os.path.abspath(sys.argv[1]))
from k69_test_h17 import omul  # noqa: E402
Eo = np.eye(8); L7 = np.array([omul(Eo[7], Eo[j]) for j in range(8)]).T
pp, pm = Eo[0] + 1j * Eo[7], Eo[0] - 1j * Eo[7]           # Bilder der sigma_y-Eigenvektoren (1, +-i) unter phi
print(f"(5) iL_e7 (1 + i e7) = {np.round((1j * L7 @ pp)[[0, 7]], 6)} (Eigenwert +1),"
      f" iL_e7 (1 - i e7) = {np.round((1j * L7 @ pm)[[0, 7]], 6)} (Eigenwert -1);"
      f" Konjugation tauscht sie: {np.allclose(pp.conj(), pm)}")
