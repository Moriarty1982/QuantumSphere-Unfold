"""Erkundung: Suche nach der Form eta im neutralen Sektor (13.11.2026, nicht blind, kein Datenvergleich).

Bedingung aus H99: eta erhaelt die mittlere quadratische Ueberlappung rho^2 und verschiebt die Brannen-Phase um den
Bogenrand theta_b (pi/12 bei rho^2 = 1/2).
(1) Brannen-Phase einer komplexen Gram-Matrix: cos 3 theta = Re(c12 c23 c31)/rho^3; bei gleichen Betraegen ist
    3 theta = Bargmann-Phase Phi = arg(c12 c23 c31).
(2) Ausschluesse: reelle Form und reelle Plaetze; Umphasen der Plaetze; eta diagonal in der Eigenbasis von S.
(3) Kandidat Lesart B: dieselben komplexen Plaetze, geladen hermitesch, neutral bilinear (x^T y).
Aufruf: python op3_eta_form_search_2026_11_13.py
"""
import numpy as np

rng = np.random.default_rng(1113)
K3 = np.arange(3)


def unit_cols(X):
    return X / np.linalg.norm(X, axis=0)


def brannen(S):
    """rho^2 und theta aus einer Gram-Matrix mit Einheitsdiagonale (hermitesch oder komplex-symmetrisch)."""
    c12, c23, c31 = S[0, 1], S[1, 2], S[2, 0]
    rho2 = (abs(c12) ** 2 + abs(c23) ** 2 + abs(c31) ** 2) / 3
    th = np.arccos(np.clip(np.real(c12 * c23 * c31) / rho2 ** 1.5, -1, 1)) / 3
    return rho2, th


def eig_formula(rho2, th):
    return np.sort(1 + 2 * np.sqrt(rho2) * np.cos(th + 2 * np.pi * K3 / 3))


if __name__ == "__main__":
    print("(1) Brannen-Phase als Bargmann-Phase")
    err = 0
    for _ in range(500):
        X = unit_cols(rng.normal(size=(4, 3)) + 1j * rng.normal(size=(4, 3)))
        S = X.conj().T @ X
        r2, th = brannen(S)
        err = max(err, np.abs(np.sort(np.linalg.eigvalsh(S)) - eig_formula(r2, th)).max())
    print(f"    Eigenwerte = 1 + 2 rho cos(theta + 2 pi k/3) mit cos 3theta = Re(c12 c23 c31)/rho^3: max. Fehler {err:.1e}")
    # gleiche Betraege: zirkulante hermitesche Gram-Matrix
    rho, Phi = np.sqrt(0.5), 0.7
    z = rho * np.exp(1j * Phi / 3)
    P = np.roll(np.eye(3), 1, axis=0)
    S = np.eye(3) + z * P + np.conj(z) * P.T
    r2, th = brannen(S)
    print(f"    zirkulant, Phi = arg(c12 c23 c31) = {np.angle(S[0, 1] * S[1, 2] * S[2, 0]):.4f}: 3 theta = {3 * th:.4f}")
    tb = np.pi / 12
    print(f"    H99 als Bargmann-Bedingung: Delta Phi = 3 theta_b = {3 * tb:.5f} = pi/4 bei rho^2 = 1/2; "
          f"NuFIT 6.1 verlangt 3 * 0.25802 = {3 * 0.25802:.5f}")

    print("\n(2) Ausschluesse")
    X = unit_cols(rng.normal(size=(3, 3)))
    S = X.T @ X
    print(f"    (a) reell: Phi = arg(c12 c23 c31) in {{0, pi}} (hier {np.angle(S[0, 1] * S[1, 2] * S[2, 0] + 0j):.4f}); "
          "theta aendert sich dann nur ueber die Betraege der einzelnen Ueberlappungen")
    X = unit_cols(rng.normal(size=(4, 3)) + 1j * rng.normal(size=(4, 3)))
    S = X.conj().T @ X
    ph = np.exp(1j * rng.uniform(0, 2 * np.pi, 3))
    S2 = (X * ph).conj().T @ (X * ph)
    print(f"    (b) Umphasen der Plaetze: Phi vorher {np.angle(S[0, 1] * S[1, 2] * S[2, 0]):.6f}, "
          f"nachher {np.angle(S2[0, 1] * S2[1, 2] * S2[2, 0]):.6f}  (invariant)")
    z = np.sqrt(0.5) * np.exp(1j * 0.2222)
    Sc = np.eye(3) + z * P + np.conj(z) * P.T                 # zirkulant, Brannen-Form der geladenen Leptonen
    w, V = np.linalg.eigh(Sc)
    for signs in ((1, 1, -1), (1, -1, 1), (-1, 1, 1)):
        Sn = V @ np.diag(np.array(signs) * w) @ V.conj().T
        d = np.sqrt(np.abs(np.diag(Sn)))
        ev = np.sort(np.abs(np.linalg.eigvalsh(Sn / np.outer(d, d))))
        same = np.allclose(ev / ev.sum(), np.sort(w) / w.sum(), atol=1e-9)
        print(f"    (c) zirkulant, eta diagonal in der Eigenbasis {signs}: Betraege der Wurzeln wie geladen: {same}")

    print("\n(3) Lesart B: geladen hermitesch, neutral bilinear auf denselben Plaetzen")
    dphi, dr2, n = [], [], 0
    while n < 4000:
        X = unit_cols(rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)))
        Se = X.conj().T @ X
        r2e, the = brannen(Se)
        if abs(r2e - 0.5) > 0.02:
            continue
        B = X.T @ X
        dB = np.sqrt(np.diag(B))
        if np.min(np.abs(dB)) < 1e-3:
            continue
        Sn = B / np.outer(dB, dB)
        r2n, thn = brannen(Sn)
        dphi.append(np.angle(Sn[0, 1] * Sn[1, 2] * Sn[2, 0]) - np.angle(Se[0, 1] * Se[1, 2] * Se[2, 0]))
        dr2.append(r2n - r2e)
        n += 1
    dphi = (np.array(dphi) + np.pi) % (2 * np.pi) - np.pi
    dr2 = np.array(dr2)
    print(f"    {n} Plaetze-Tripel mit rho_e^2 = 0.50 +- 0.02: Delta Phi Mittel {dphi.mean():+.3f}, Streuung {dphi.std():.3f}; "
          f"Delta rho^2 Mittel {dr2.mean():+.3f}, Streuung {dr2.std():.3f}")
    print(f"    Anteil mit |Delta rho^2| < 0.02 und |Delta Phi - pi/4| < 0.05: "
          f"{np.mean((np.abs(dr2) < 0.02) & (np.abs(dphi - np.pi / 4) < 0.05)):.3f}")


if __name__ == "__main__":
    print("\n(4) Nachtrag Paar-Phase: Fluss durch das Platzdreieck")
    # gerichtete Phase auf jeder Kante a -> a+1 (Gegenrichtung konjugiert): hermitesch bleibt hermitesch
    z = np.sqrt(0.5) * np.exp(1j * 0.2222)
    Se = np.eye(3) + z * P + np.conj(z) * P.T
    tb = np.pi / 12
    Sn = np.eye(3) + z * np.exp(1j * tb) * P + np.conj(z * np.exp(1j * tb)) * P.T
    r2e, the = brannen(Se); r2n, thn = brannen(Sn)
    print(f"    gerichtete Kantenphase theta_b: hermitesch {np.allclose(Sn, Sn.conj().T)}, rho^2 {r2e:.4f} -> {r2n:.4f}, "
          f"theta {the:.4f} -> {thn:.4f} (Differenz {thn - the:.4f} = pi/12)")
    # Eichinvarianz: Umphasen verteilt die Kantenphasen um, der Fluss (Summe) bleibt
    ph = np.exp(1j * np.array([0.3, -1.1, 2.0]))
    Sg = np.diag(ph.conj()) @ Sn @ np.diag(ph)
    print(f"    Fluss nach Umphasen: {np.angle(Sg[0, 1] * Sg[1, 2] * Sg[2, 0]):.4f} (vorher {np.angle(Sn[0, 1] * Sn[1, 2] * Sn[2, 0]):.4f})")
    # native Phasen: omega (Triole, tau, Sedenion psi), i (L_e7, Q_J, z -> iz), -1 (Spiegelungen, eta)
    fluxes = sorted({round(((a * 2 * np.pi / 3 + b * np.pi / 2 + c * np.pi) % (2 * np.pi)) / (np.pi / 12)) % 24
                     for a in range(3) for b in range(4) for c in range(2)})
    print(f"    erzeugte Fluesse in Einheiten pi/12: {fluxes}")
    print(f"    pi/4 = 3 * pi/12 enthalten: {3 in fluxes}; naechste: pi/6 und pi/3 (Abstand pi/12)")
    # Rand des Bogens: der Fluss pi/4 ist die Bargmann-Phase eines koplanaren Koide-Tripels
    zb = np.sqrt(0.5) * np.exp(1j * tb)
    Sb = np.eye(3) + zb * P + np.conj(zb) * P.T
    print(f"    koplanares Koide-Tripel (theta = pi/12): det S = {np.real(np.linalg.det(Sb)):.1e}, Fluss = "
          f"{np.angle(Sb[0, 1] * Sb[1, 2] * Sb[2, 0]):.5f} (pi/4 = {np.pi / 4:.5f})")


if __name__ == "__main__":
    print("\n(5) Nachtrag: pi/4 = (3/2) * pi/6 (Vorschlag des Autors)")
    print(f"    pi/6 nativ: omega * i^-1 = e^(i(2pi/3 - pi/2)), Fluss {np.angle(np.exp(2j * np.pi / 3) / 1j):.5f} = pi/6 {np.pi / 6:.5f}")
    # (b) 3/2 als 3 rho^2 oder 1/K: gilt die Beziehung nur bei rho^2 = 1/2?
    print("    Rand-Fluss Phi_b(rho) = 3 theta_b gegen (pi/6) * 3 rho^2 und (pi/6) / K:")
    for r2 in (0.40, 0.45, 0.50, 0.55, 0.60):
        Phib = np.arccos(np.clip((3 * r2 - 1) / (2 * r2 ** 1.5), -1, 1))
        K = (1 + 2 * r2) / 3
        print(f"      rho^2 = {r2:.2f}: Phi_b = {Phib:.4f}, (pi/6)*3rho^2 = {np.pi / 6 * 3 * r2:.4f}, (pi/6)/K = {np.pi / 6 / K:.4f}")
    # (a) 3/2 = 3 Kanten * 1/2 (Spinor): Drehung um pi/6 im Vektorbild wirkt auf Spinoren mit e^(i pi/12)
    a = np.pi / 6
    Rspin = np.array([[np.exp(-1j * a / 2), 0], [0, np.exp(1j * a / 2)]])   # SU(2)-Bild einer Drehung um a
    print(f"    Spinorbild einer Drehung um pi/6: Phasen {np.round(np.angle(np.diag(Rspin)), 5)} (= -+pi/12); "
          f"drei Kanten: Fluss {3 * a / 2:.5f} = pi/4")


def su2(axis, angle):
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
    n = np.array(axis) / np.linalg.norm(axis)
    G = n[0] * sx + n[1] * sy + n[2] * sz
    return np.cos(angle / 2) * np.eye(2) - 1j * np.sin(angle / 2) * G


if __name__ == "__main__":
    print("\n(6) Nachtrag Spinor-Transport")
    eps = np.array([[0, 1], [-1, 0]], complex)
    # (a) Lorentz-Transport auf den Kanten: Drehung (SU(2)) und Boost (SL(2,C))
    U = su2((0.3, -0.5, 0.8), np.pi / 6)
    Bst = np.diag([np.exp(0.4), np.exp(-0.4)]).astype(complex)
    print(f"    Drehung: U^dag U = 1 {np.allclose(U.conj().T @ U, np.eye(2))}, U^T eps U = eps {np.allclose(U.T @ eps @ U, eps)}")
    print(f"    Boost:   B^T eps B = eps {np.allclose(Bst.T @ eps @ Bst, eps)}  (Majorana-Paarung invariant)")
    # Lorentz-invariante Massenterme zwischen transportierten Plaetzen: Kantenfaktoren heben sich auf
    rng2 = np.random.default_rng(7)
    chis = [rng2.normal(size=2) + 1j * rng2.normal(size=2) for _ in range(3)]
    L = [su2((0, 0, 1), np.pi / 6) for _ in range(3)]             # gleiche Drehung um pi/6 auf jeder Kante
    def maj(a, b, with_link):
        Ub = L[a] if with_link else np.eye(2)
        return (Ub @ chis[a]) @ eps @ (Ub @ chis[b])               # beide Partner mit demselben Kantenfaktor
    flux0 = np.angle(maj(0, 1, False) * maj(1, 2, False) * maj(2, 0, False))
    flux1 = np.angle(maj(0, 1, True) * maj(1, 2, True) * maj(2, 0, True))
    print(f"    Majorana-Paarung psi^T eps psi mit Kantendrehung: Fluss vorher {flux0:.5f}, nachher {flux1:.5f} (unveraendert)")
    # nicht invariante Uebergangsamplitude chi^dag U chi (kein Massenterm): traegt pi/12 je Kante
    chi = np.array([1, 0], complex)
    c = chi.conj() @ su2((0, 0, 1), np.pi / 6) @ chi
    print(f"    zum Vergleich chi^dag U chi (kein Lorentz-Skalar): Phase {np.angle(c):.5f} je Kante, Fluss {3 * np.angle(c):.5f}")
    # (b) innerer Transport: Familien-U(1), Kantenwinkel A je Ladungseinheit, Fluss F = 3A je Ladungseinheit.
    # Ein Block sieht q_transp * F (Ladung des transportierten Partners): Dirac transportiert e_R, Majorana l_L.
    # Normierter Bargmann-Fluss eines Blocks M_ab = f_a W_ab^q f_b, numerisch:
    A = np.pi / 6
    W = np.exp(1j * A)
    def block_flux(q):
        f = np.exp(1j * rng2.uniform(0, 2 * np.pi, 3)) * (1 + rng2.uniform(0, 1, 3))
        M = np.array([[f[a] * f[b] * (W ** q if (b - a) % 3 == 1 else (np.conj(W) ** q if (a - b) % 3 == 1 else 1))
                       for b in range(3)] for a in range(3)])
        d = np.sqrt(np.diag(M))
        Mn = M / np.outer(d, d)
        return np.angle(Mn[0, 1] * Mn[1, 2] * Mn[2, 0])
    print(f"    innerer Transport, A = pi/6: Block mit Ladung q sieht Fluss q*3A: q=1 -> {block_flux(1):.5f}, q=1/2 -> {block_flux(0.5):.5f}")
    print("    Sektorunterschied Phi_nu - Phi_e = (q_L - q_R) * 3A; verlangt pi/4:")
    for lab, qL, qR in (("Sumino (3, +1) / (3bar, -1)", 1.0, -1.0), ("vektorartig q_L = q_R", 1.0, 1.0),
                        ("L halbe Ladung, R neutral", 0.5, 0.0), ("Sumino mit halben Ladungen", 0.5, -0.5)):
        print(f"      {lab:30s}: Delta = {(qL - qR) * 3 * A:.5f}  (pi/4 = {np.pi / 4:.5f}; mit A = pi/6 noetig q_L - q_R = 1/2)")
