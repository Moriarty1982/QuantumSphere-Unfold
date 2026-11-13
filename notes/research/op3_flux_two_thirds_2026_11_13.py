"""Erkundung: Woher kommt ein Fluss von 2/3 rad durch das Platzdreieck der geladenen Leptonen? (13.11.2026, nicht blind)

(1) Mechanismen fuer nicht quantisierten Fluss: Berry-Phase (halber Raumwinkel bei Qubits), U(1)-Fluss, Selbstbezug Phi = K.
(2) Fester Scan nativer Konstanten (Liste vor dem Vergleich im Skript festgelegt) gegen Phi_e = 3 theta_e und
    Delta Phi = pi/4 - 3 theta_e; Treffer = relative Abweichung <= 1 %. Kein Test; Look-elsewhere wird mitgezaehlt.
Aufruf: python op3_flux_two_thirds_2026_11_13.py
"""
import itertools
import numpy as np

POL = np.array([0.51099895, 105.6583755, 1776.93])


def lepton_phase(m):
    v = np.sqrt(m); x = v / v.mean() - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    return np.arccos(np.clip(4 * np.prod(x) / A ** 3, -1, 1)) / 3


if __name__ == "__main__":
    te = lepton_phase(POL)
    sig_te = abs(lepton_phase(POL + np.array([0, 0, 0.09])) - te)
    targets = {"Phi_e = 3 theta_e": 3 * te, "Delta Phi = pi/4 - 3 theta_e": np.pi / 4 - 3 * te}
    print(f"theta_e = {te:.7f} +- {sig_te:.1e}; Phi_e = {3 * te:.6f}; Delta Phi = {np.pi / 4 - 3 * te:.6f}")
    # (1) Berry-Phase: welcher Raumwinkel waere noetig (Qubit, Phase = Omega/2)?
    print(f"(1) als Qubit-Berry-Phase verlangt Phi_e einen Raumwinkel {2 * 3 * te:.4f} sr; der Oktant hat pi/2 = {np.pi / 2:.4f}")
    # (2) Scan
    gBI = 0.237533
    gst = np.log(2) / (np.pi * np.sqrt(3))
    gL = gBI / gst
    beta2 = (gL - 1) / (gL + 1)
    eta = np.arccosh(gL)
    consts = {"gamma_BI": gBI, "gamma_string": gst, "gamma_L": gL, "beta_sym": np.sqrt(beta2), "Omega_M = beta^2": beta2,
              "eta": eta, "eps = artanh beta": eta / 2, "alpha": 1 / 137.035999, "beta4 = 1/256": 1 / 256,
              "rho = 1/sqrt2": 1 / np.sqrt(2), "pi/12": np.pi / 12}
    mults = {"1": 1, "2": 2, "1/2": 0.5, "3": 3, "1/3": 1 / 3, "pi": np.pi, "1/pi": 1 / np.pi}
    trials, hits = 0, []
    for (cn, c), (mn, m), (tn, t) in itertools.product(consts.items(), mults.items(), targets.items()):
        trials += 1
        rel = c * m / t - 1
        if abs(rel) <= 0.01:
            hits.append((tn, f"{mn} * {cn}", c * m, rel))
    print(f"(2) Scan: {len(consts)} Konstanten x {len(mults)} Faktoren x {len(targets)} Ziele = {trials} Versuche, Treffer (<= 1 %): {len(hits)}")
    for h in hits:
        print(f"    {h[0]:30s} <- {h[1]:24s} = {h[2]:.6f} ({100 * h[3]:+.3f} %)")
    # Zufallserwartung: Anteil zufaelliger log-gleichverteilter Werte im 1-%-Fenster
    rng = np.random.default_rng(3)
    fake = 10 ** rng.uniform(-3, 1, size=(20000, trials))
    tv = np.array([t for (_, _), (_, _), (_, t) in itertools.product(consts.items(), mults.items(), targets.items())])
    exp_hits = np.mean(np.sum(np.abs(fake / tv - 1) <= 0.01, axis=1))
    print(f"    erwartete Zahl zufaelliger Treffer bei log-gleichverteilten Werten (1e-3..10): {exp_hits:.2f}")


if __name__ == "__main__":
    print("\n(3) Nachtraeglich: Schaerfe der Beziehung Delta Phi = gamma_BI/2")
    th_pred = (np.pi / 4 - gBI / 2) / 3
    dev_sig = (te - th_pred) / sig_te
    print(f"    theta_e aus der Beziehung = {th_pred:.7f}; gemessen {te:.7f} +- {sig_te:.1e} (aus m_tau): {dev_sig:+.2f} sigma")
    # verlangte Masse m_tau bei festen m_e, m_mu, K = 2/3 und theta = th_pred
    k = np.arange(3)
    s = 1 + np.sqrt(2) * np.cos(th_pred + 2 * np.pi * k / 3)
    m = np.sort(s ** 2)
    scale_mu = POL[1] / m[1]
    print(f"    Verhaeltnisse: m_e/m_mu = {m[0] / m[1]:.6e} (Daten {POL[0] / POL[1]:.6e}), m_tau aus m_mu: {m[2] * scale_mu:.3f} MeV "
          f"(PDG 1776.93 +- 0.09)")
    print("    Abhaengigkeit von der Zaehlweise: gamma_BI = 0.237533 (Domagala-Lewandowski/Meissner, L1); andere Werte der Literatur")
    for g, lab in ((0.2375, "DL/Meissner"), (0.2740, "ABCK SU(2)"), (0.1274, "gamma_string (j=1/2)")):
        print(f"      {lab:22s}: gamma/2 = {g / 2:.5f} gegen Delta Phi {np.pi / 4 - 3 * te:.5f}")


if __name__ == "__main__":
    from scipy.optimize import brentq
    print("\n(4) Konsistente Fassung: theta fest aus gamma_BI, rho^2 aus m_e/m_mu (genau bekannt), Vorhersage m_tau und K")
    def ratios(r2, th):
        s = 1 + 2 * np.sqrt(r2) * np.cos(th + 2 * np.pi * np.arange(3) / 3)
        m = np.sort(s ** 2)
        return m / m[1]
    target = POL[0] / POL[1]
    r2 = brentq(lambda r: ratios(r, th_pred)[0] - target, 0.49, 0.52)
    mm = ratios(r2, th_pred) * POL[1]
    Kp = mm.sum() / np.sqrt(mm).sum() ** 2
    print(f"    rho^2 = {r2:.7f}, K = {Kp:.7f} (Pol {POL.sum() / np.sqrt(POL).sum() ** 2:.7f} +- 5e-6), "
          f"m_tau = {mm[2]:.3f} MeV (PDG 1776.93 +- 0.09, {(mm[2] - 1776.93) / 0.09:+.2f} sigma)")
    # zum Vergleich: exaktes Koide mit m_e, m_mu
    r2k = 0.5
    thk = brentq(lambda t: ratios(r2k, t)[0] - target, 0.15, 0.26)
    mk = ratios(r2k, thk) * POL[1]
    print(f"    Vergleich exaktes Koide aus m_e, m_mu: theta = {thk:.7f}, m_tau = {mk[2]:.3f} MeV")
