"""Erkundung: Lorentz-Fassung des Oktanten-Tripels (13.11.2026, nicht blind, kein Datenvergleich).

(1) Lorentz-Qubit C^{1,1} (SU(1,1)): drei Zustaende mit Norm +1 -- ist rho^2 = 1/2 moeglich?
(2) Signatur (2,1) auf C^3: Gram S = X^dag eta X fuer das geladene zirkulante Tripel X, eta = 1 - 2 t t^dag mit
    nativen Zeitachsen t; Vergleich mit der H99-Forderung (rho^2 erhalten, theta um pi/12 verschoben).
Aufruf: python op3_lorentz_octant_2026_11_13.py
"""
import numpy as np

rng = np.random.default_rng(2113)
K3 = np.arange(3)


def brannen(S):
    c12, c23, c31 = S[0, 1], S[1, 2], S[2, 0]
    rho2 = (abs(c12) ** 2 + abs(c23) ** 2 + abs(c31) ** 2) / 3
    th = np.arccos(np.clip(np.real(c12 * c23 * c31) / rho2 ** 1.5, -1, 1)) / 3
    return rho2, th


if __name__ == "__main__":
    print("(1) Lorentz-Qubit: eta = diag(1, -1), Zustaende mit psi^dag eta psi = +1")
    eta2 = np.diag([1.0, -1.0])
    mins = []
    for _ in range(20000):
        r, ph = rng.uniform(0, 3, 2), rng.uniform(0, 2 * np.pi, 2)
        a = np.array([np.cosh(r[0] / 2), np.exp(1j * ph[0]) * np.sinh(r[0] / 2)])
        b = np.array([np.cosh(r[1] / 2), np.exp(1j * ph[1]) * np.sinh(r[1] / 2)])
        mins.append(abs(a.conj() @ eta2 @ b) ** 2)
    print(f"    kleinstes |<a|b>|^2 bei 20000 Paaren: {min(mins):.6f} (umgekehrte Cauchy-Schwarz: >= 1) -> rho^2 >= 1, K >= 1;"
          " kein Koide-Tripel")

    print("\n(2) Signatur (2,1) auf C^3, geladenes zirkulantes Tripel (rho^2 = 1/2, theta_e = 0.2222)")
    th_e = 0.2222
    z = np.sqrt(0.5) * np.exp(1j * th_e)
    P = np.roll(np.eye(3), 1, axis=0)
    S_e = np.eye(3) + z * P + np.conj(z) * P.T
    w, V = np.linalg.eigh(S_e)
    X = np.diag(np.sqrt(w)) @ V.conj().T                 # X^dag X = S_e, Spalten = Plaetze
    r2e, te = brannen(S_e)
    print(f"    Kontrolle: rho^2 = {r2e:.4f}, theta = {te:.4f}; Ziel H99: rho^2 = 0.5, theta = {th_e + np.pi / 12:.4f}")
    cands = {
        "Zyklusachse (1,1,1)/sqrt3 (Fourier k=0)": np.ones(3) / np.sqrt(3),
        "Fourier k=1": np.exp(2j * np.pi * K3 / 3) / np.sqrt(3),
        "Koordinatenachse e_1": np.array([1, 0, 0], complex),
        "Koordinatenachse e_2": np.array([0, 1, 0], complex),
        "Eigenvektor kleinster Eigenwert (Elektron)": V[:, 0],
        "Eigenvektor groesster Eigenwert (Tau)": V[:, 2],
        "Platzrichtung x_1 normiert": X[:, 0] / np.linalg.norm(X[:, 0]),
    }
    for lab, t in cands.items():
        t = t / np.linalg.norm(t)
        eta = np.eye(3) - 2 * np.outer(t, t.conj())
        G = X.conj().T @ eta @ X
        d = np.real(np.diag(G))
        if np.any(d <= 0):
            print(f"    {lab:44s}: ein Platz zeitartig (Norm {np.round(d, 3)}), keine Einheitsnormierung")
            continue
        Sn = G / np.sqrt(np.outer(d, d))
        r2, th = brannen(Sn)
        ev = np.sort(np.linalg.eigvalsh(Sn))
        print(f"    {lab:44s}: rho^2 = {r2:.4f}, theta = {th:.4f}, Eigenwerte {np.round(ev, 3)}")
    # Wie viele Zeitachsen erfuellen beide Bedingungen? Abtastung der reellen Zeitachsen auf der Kugel
    hits = []
    for _ in range(40000):
        t = rng.normal(size=3) + 1j * rng.normal(size=3)
        t /= np.linalg.norm(t)
        eta = np.eye(3) - 2 * np.outer(t, t.conj())
        G = X.conj().T @ eta @ X
        d = np.real(np.diag(G))
        if np.any(d <= 0):
            continue
        r2, th = brannen(G / np.sqrt(np.outer(d, d)))
        if abs(r2 - 0.5) < 0.01 and abs(th - (th_e + np.pi / 12)) < 0.01:
            hits.append(t)
    print(f"    Zufallsachsen mit rho^2 = 0.50 +- 0.01 und theta = Ziel +- 0.01: {len(hits)} von 40000 "
          "(Loesungen bilden eine Familie, keine ausgezeichnete Achse)")
