"""Selbstpruefung zur Rueckwaertssuche Stringrelaxation (12.11.2026).

Nicht blind; prueft nur die analytischen Aussagen der Notiz
op3_string_relaxation_backward_2026_11_12.md an Zahlenbeispielen.
Aufruf: python op3_string_relaxation_backward_2026_11_12.py
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

rng = np.random.default_rng(20261112)


def maxwell_fixed_sum():
    """B3: Reihe, feste Summe, Maxwell. Endanteile = r0 + Ueberschuss * Fluiditaetsanteil."""
    k = rng.uniform(0.5, 3, 3)
    eta = rng.uniform(0.5, 3, 3)
    r0 = rng.uniform(0.05, 0.2, 3)
    L = 1.0
    c, f = (1 / k).sum(), (1 / eta).sum()

    def rhs(t, r):
        lam = (L - r.sum()) / c
        return lam / eta

    sol = solve_ivp(rhs, [0, 200 * c / f], r0, rtol=1e-11, atol=1e-13)
    r_end = sol.y[:, -1]
    pred = r0 + (L - r0.sum()) * (1 / eta) / f
    lam_end = (L - r_end.sum()) / c
    # Energie: alles Elastische dissipiert
    U0 = (L - r0.sum()) ** 2 / (2 * c)
    return np.abs(r_end - pred).max(), lam_end, U0


def driven_growing_sum(H=0.7):
    """B4: Summe waechst wie a = exp(Ht). Anteile -> (1/eta_i + H/k_i)/Summe."""
    k = rng.uniform(0.5, 3, 3)
    eta = rng.uniform(0.5, 3, 3)
    c, f = (1 / k).sum(), (1 / eta).sum()
    L0 = 1.0
    ell0 = np.array([0.2, 0.3, 0.5])

    def rhs(t, y):
        ell, lam = y[:3], y[3]
        dlam = (H * L0 * np.exp(H * t) - lam * f) / c
        return np.append(dlam / k + lam / eta, dlam)

    sol = solve_ivp(rhs, [0, 30 / H], np.append(ell0, 0.0), rtol=1e-11, atol=1e-13)
    ell = sol.y[:3, -1]
    share = ell / ell.sum()
    pred = (1 / eta + H / k) / (f + H * c)
    return np.abs(share - pred).max()


def softening_identical():
    """B5: identische Strings, F = ell*exp(-ell) (ein Hoecker bei ell = 1).

    Gebrochener Zustand (lang, kurz, kurz); Stabilitaet ueber die auf
    Summe delta = 0 eingeschraenkte Hesse-Matrix diag(F'(ell_i)).
    """
    F = lambda x: x * np.exp(-x)
    dF = lambda x: (1 - x) * np.exp(-x)
    q = 4 + 3 * np.sqrt(2)                 # K = 2/3 fuer q:1:1
    s = np.log(q) / (q - 1)                # F(s) = F(q s)
    L = (q + 2) * s
    ell = np.array([q * s, s, s])
    K = (ell ** 2).sum() / L ** 2
    kk = dF(ell)
    # Basis des Tangentialraums Summe delta = 0
    B = np.array([[1, -1, 0], [1, 1, -2]]).T / np.array([np.sqrt(2), np.sqrt(6)])
    eig = np.linalg.eigvalsh(B.T @ np.diag(kk) @ B)
    # symmetrischer Zustand beim selben L
    k_sym = dF(L / 3)
    # (kurz, lang, lang): zwei auf dem fallenden Ast -> instabil
    g = lambda x: F(x) - F((L - x) / 2)
    try:
        x = brentq(g, 1e-6, 0.9)
        ell2 = np.array([x, (L - x) / 2, (L - x) / 2])
        eig2 = np.linalg.eigvalsh(B.T @ np.diag(dF(ell2)) @ B)
    except ValueError:
        eig2 = None
    return dict(L=L, s=s, K=K, force_spread=np.ptp(F(ell)), eig_broken=eig,
                sum_inv_k=(1 / kk).sum(), k_sym=k_sym, eig_kurz_lang_lang=eig2)


def lepton_shares():
    m = np.array([0.51099895, 105.6583755, 1776.86])  # MeV, bekannte Werte
    x = np.sqrt(m)
    x /= x.sum()
    return x, (x ** 2).sum()


if __name__ == "__main__":
    d, lam, U0 = maxwell_fixed_sum()
    print(f"B3 Maxwell feste Summe: max|r_end - Formel| = {d:.2e}, Restkraft {lam:.1e}, dissipiert U0 = {U0:.4f}")
    print(f"B4 wachsende Summe: max|Anteil - Formel| = {driven_growing_sum():.2e}")
    r = softening_identical()
    print(f"B5 ein Hoecker: L/ell_c = {r['L']:.6f}, kurz = {r['s']:.6f}, K = {r['K']:.12f}, Kraftdifferenz {r['force_spread']:.1e}")
    print(f"   Hesse (lang,kurz,kurz) = {r['eig_broken']}, Summe 1/k = {r['sum_inv_k']:.4f}")
    print(f"   symmetrisch F'(L/3) = {r['k_sym']:.5f} (>0: ebenfalls stabil), (kurz,lang,lang) Hesse = {r['eig_kurz_lang_lang']}")
    x, K = lepton_shares()
    print(f"Leptonanteile sqrt(m)/Summe = {x}, K = {K:.6f}")
