"""Erkundung: Potential fuer rho^2 = 1/2 (Koide) auf der Gram-Matrix S (13.11.2026, nicht blind, kein Datenvergleich).

Gram-Lesart A: sqrt(m) ~ s_k = 1 + 2 rho cos(theta + 2 pi k/3), Einheitsdiagonale, tr S = 3.
(1) Invarianten: tr S^2 = 3 + 6 rho^2, tr S^3 = 3 + 18 rho^2 + 6 rho^3 cos 3theta (numerisch geprueft).
(2) Potentiale in X (S = X^dag X quadratisch in X): Grad 4 linear in rho^2 -> kein inneres Extremum; Grad 6 -> rho^2 = 1/2
    nur bei abgestimmtem Koeffizientenverhaeltnis und ohne cos 3theta-Term.
(3) Gleichwertige Lesarten von K = 2/3: Reinheit von S/3; Mitte von [1/3, 1]; Gleichverteilung Diagonale/Nebendiagonale;
    paarweise Treue 1/2 (zirkulant).
(4) Ein nicht abgestimmter Kandidat: 'doppelter Projektor' V = tr (S^2 - 2S)^2.
Aufruf: python op3_koide_potential_2026_11_13.py
"""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(1113)
K3 = np.arange(3)


def s_of(rho2, th):
    return 1 + 2 * np.sqrt(rho2) * np.cos(th + 2 * np.pi * K3 / 3)


if __name__ == "__main__":
    err2 = err3 = 0
    for _ in range(200):
        r2, th = rng.uniform(0, 1), rng.uniform(0, np.pi / 3)
        s = s_of(r2, th)
        err2 = max(err2, abs((s ** 2).sum() - (3 + 6 * r2)))
        err3 = max(err3, abs((s ** 3).sum() - (3 + 18 * r2 + 6 * r2 ** 1.5 * np.cos(3 * th))))
    print(f"(1) tr S^2 = 3 + 6 rho^2 (Fehler {err2:.1e}); tr S^3 = 3 + 18 rho^2 + 6 rho^3 cos3theta (Fehler {err3:.1e})")
    print("(2) Grad 4: a tr S^2 + b (tr S)^2 = a(3 + 6 rho^2) + 9b, linear in rho^2: Extremum nur am Rand.")
    print("    Grad 6: alpha rho^2 + beta rho^4 + gamma rho^3 cos3theta; rho^2 = 1/2 fuer jedes theta nur mit gamma = 0 und")
    print("    alpha/beta = -1 (abgestimmt). Passt zu r16 (Grad <= 4 hoechstens zwei Normen) und r26 (Grad 6 noetig).")
    # (3) gleichwertige Lesarten
    s = s_of(0.5, 0.2222)
    p = s / s.sum()
    print(f"(3) bei rho^2 = 1/2: Reinheit von S/3 = {np.sum(p ** 2):.6f}; Mitte von [1/3, 1] = {(1 / 3 + 1) / 2:.6f}; "
          f"||S - 1||^2 = {6 * 0.5:.1f} = ||1||^2 = 3")
    # (4) doppelter Projektor: minimiere sum (s^2 - 2s)^2 unter sum s = 3, s >= 0
    best = None
    for _ in range(200):
        x0 = rng.dirichlet(np.ones(3)) * 3
        res = minimize(lambda s: np.sum((s ** 2 - 2 * s) ** 2), x0, constraints=[{"type": "eq", "fun": lambda s: s.sum() - 3}],
                       bounds=[(0, 3)] * 3)
        if best is None or res.fun < best.fun - 1e-12:
            best = res
    sb = np.sort(best.x)
    print(f"(4) V = tr(S^2 - 2S)^2 bei tr S = 3: Minimum bei s = {np.round(sb, 4)}, V = {best.fun:.4f}, "
          f"K = {np.sum(sb ** 2) / sb.sum() ** 2:.4f} (Koide 0.6667)")


def haar_states(n, d, rng):
    z = rng.normal(size=(n, d)) + 1j * rng.normal(size=(n, d))
    return z / np.linalg.norm(z, axis=1, keepdims=True)


if __name__ == "__main__":
    print("\n== Auswahlprinzip: Koide als qubitartige Treue ==")
    N = 200000
    for d in (2, 3, 4):
        r2s, Ks, phis = [], [], []
        for _ in range(N // 10):
            X = haar_states(3, d, rng)
            S = X.conj() @ X.T
            r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
            r2s.append(r2); Ks.append((1 + 2 * r2) / 3)
        r2s, Ks = np.array(r2s), np.array(Ks)
        print(f"    C^{d} (Haar): Mittel rho^2 = {r2s.mean():.4f} (1/d = {1 / d:.4f}), Mittel K = {Ks.mean():.4f}, Streuung K = {Ks.std():.4f}, "
              f"Anteil |K - 2/3| < 1e-5: {np.mean(np.abs(Ks - 2 / 3) < 1e-5):.1e}")
    # Qubit-Tripel haben Rang 2: theta folgt aus rho (det = 0)
    X = haar_states(3, 2, rng)
    S = X.conj() @ X.T
    print(f"    Qubit-Tripel: det S = {abs(np.linalg.det(S)):.1e} (immer Rang 2); bei rho^2 = 1/2 also theta = pi/12 (Rand)")
    # drei Koide-Fakten in einer Zeile
    print("    Zusammenfassung: rho^2 = 1/2 ist (a) die mittlere Treue zufaelliger Qubits, (b) die Treue der Qubits an orthogonalen")
    print("    Achsen (Oktant, Rand), (c) unter Spins j an orthogonalen Achsen nur fuer j = 1/2 erreicht.")
    print(f"    Geladene Leptonen: Rang 3 mit rho^2 = 1/2, Bargmann-Phase 3 theta_e = {3 * 0.22222:.4f} < pi/4 = {np.pi / 4:.4f}: "
          "qubitartige Treue, aber aus der Qubit-Ebene herausgehoben.")
