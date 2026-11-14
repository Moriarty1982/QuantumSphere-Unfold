"""Erkundung (nicht blind): CT-001 nach der Platzhalter-Methode verkleinern (14.11.2026).

CT-001: Delta Phi = kappa * s * gamma_M mit gesetzter Einheit kappa*s = 1/2.
(a) Rueckwaerts: welches kappa*s verlangen die Massen (m_e, m_mu, m_tau PDG 2024)?
(b) Kann die Berry-/Bargmann-Phase des Qubit-Tripels selbst Delta Phi liefern? (Bargmann = Omega/2)
(c) Externer Fluss auf ein Spin-1/2- bzw. Dirac-Paar: Phase = q g Omega, minimal q g = 1/2 -> kappa*s = 1/2 pro Steradiant.
Aufruf: python ct001_shrink_2026_11_14.py
"""
import numpy as np

ME, MMU = 0.51099895, 105.6583755
MTAU, SMTAU = 1776.93, 0.09            # PDG 2024 (fitted_on von CT-001)
GAMMA_M = 0.237533


def koide_theta(m):
    """Brannen-Parametrisierung sqrt(m_k) = A (1 + sqrt(2 rho2)... ) : K, rho^2 und theta aus den Massen."""
    r = np.sqrt(np.array(m))
    K = sum(m) / r.sum() ** 2
    rho2 = (3 * K - 1) / 2
    # sqrt(m_k) = M (1 + b cos(theta + 2 pi k / 3)), b = sqrt(2) * sqrt(2 rho2) / ... -> theta aus normierten Wurzeln
    x = r / r.mean() - 1                     # = b cos(theta + 2 pi k/3)
    b = np.sqrt(2 * np.mean(x ** 2))
    best = None
    for perm in ((0, 1, 2),):
        c = x[list(perm)] / b
        th = np.arctan2(-(c[1] - c[2]) / np.sqrt(3), c[0])   # cos-Zerlegung
        best = th
    return K, rho2, best, b


def bloch_triangle_omega(alpha):
    """Raumwinkel des gleichseitigen geodaetischen Dreiecks mit Kantenwinkel alpha (Bloch-Vektoren)."""
    ca = np.cos(alpha)
    # a.(b x c) fuer gleichseitiges Dreieck: Volumen = sqrt(1 - 3 ca^2 + 2 ca^3)
    vol = np.sqrt(max(0.0, 1 - 3 * ca ** 2 + 2 * ca ** 3))
    return 2 * np.arctan2(vol, 1 + 3 * ca)


if __name__ == "__main__":
    # (a) rueckwaerts
    res = []
    for mt in (MTAU - SMTAU, MTAU, MTAU + SMTAU):
        m = [ME, MMU, mt]
        K, rho2, th, b = koide_theta(m)
        # Konvention der H102-Notiz: theta_e = Elektronphase, Phi_e = 3 theta_e = pi/4 - Delta Phi
        r = np.sqrt(np.array(m)); x = r / r.mean() - 1
        the = np.arccos(np.clip(x[0] / b, -1, 1))          # Phase des Elektrons im Bogen
        theta_e = abs(the - 2 * np.pi / 3) if the > np.pi / 3 else the
        res.append((mt, K, rho2, theta_e))
    print("(a) Rueckwaerts aus den Massen (m_tau = PDG 2024 +- 1 sigma):")
    for mt, K, rho2, te in res:
        dphi = np.pi / 4 - 3 * te
        print(f"    m_tau = {mt:8.2f}: K = {K:.6f}, rho^2 = {rho2:.6f}, theta_e = {te:.6f}, "
              f"Delta Phi = pi/4 - 3 theta_e = {dphi:.6f}, verlangtes kappa*s = Delta Phi / gamma_M = {dphi / GAMMA_M:.5f}")
    print(f"    Kontrolle gegen H102: theta_e(H102) = (pi/4 - gamma_M/2)/3 = {(np.pi / 4 - GAMMA_M / 2) / 3:.7f}")
    # (b) interne Berry-Phase des Qubit-Tripels
    print("\n(b) Bargmann-Phase eines gleichseitigen Qubit-Tripels = Omega/2 (Raumwinkel der Bloch-Vektoren):")
    for rho2 in (0.5, res[1][2]):
        alpha = np.arccos(2 * rho2 - 1)
        om = bloch_triangle_omega(alpha)
        print(f"    rho^2 = {rho2:.6f}: Kantenwinkel {np.degrees(alpha):.4f} Grad, Omega = {om:.6f} (Oktant pi/2 = {np.pi / 2:.6f}), "
              f"Phase Omega/2 = {om / 2:.6f}; Abweichung von pi/4: {om / 2 - np.pi / 4:+.2e}")
    # Kontrolle der Formel mit expliziten Spinoren
    def spinor(n):
        th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0]); return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    a, b_, c = np.eye(3)
    s = [spinor(v) for v in (a, b_, c)]
    barg = np.angle(np.vdot(s[0], s[1]) * np.vdot(s[1], s[2]) * np.vdot(s[2], s[0]))
    print(f"    Kontrolle Oktant mit Spinoren: |Bargmann-Phase| = {abs(barg):.6f} = pi/4")
    print(f"    -> Das Qubit-Tripel selbst kann Delta Phi = {np.pi / 4 - 3 * res[1][3]:.4f} nicht liefern (Abweichung ~1e-5):"
          " Delta Phi muss ein aeusserer Fluss sein.")
    # (c) externer Fluss: Dirac
    print("\n(c) Aeusserer Fluss als Aharonov-Bohm-/Dirac-Phase: Phase = q g Omega_ext; Dirac: q g in Z/2, minimal 1/2.")
    print(f"    minimal q g = 1/2 -> kappa*s = 1/2 pro Steradiant, ohne Flaecheneinheit; verlangt: {res[1][3] and (np.pi / 4 - 3 * res[1][3]) / GAMMA_M:.5f}")
    lo = (np.pi / 4 - 3 * res[2][3]) / GAMMA_M; hi = (np.pi / 4 - 3 * res[0][3]) / GAMMA_M
    print(f"    1-sigma-Band (m_tau) fuer kappa*s: [{min(lo, hi):.5f}, {max(lo, hi):.5f}]; 1/2 darin: {min(lo, hi) <= 0.5 <= max(lo, hi)}")
    print(f"    Restplatzhalter: Omega_ext = 2 Delta Phi = {2 * (np.pi / 4 - 3 * res[1][3]):.6f} sr gegen gamma_M = {GAMMA_M} sr")
