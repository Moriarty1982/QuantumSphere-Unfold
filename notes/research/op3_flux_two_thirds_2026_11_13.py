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


if __name__ == "__main__":
    print("\n(5) Mechanismus-Suche: gamma aus den Zaehlregeln je Frame (r09, r10)")
    js = np.arange(1, 400) / 2
    a = np.sqrt(js * (js + 1))
    gM = brentq(lambda g: np.sum(2 * np.exp(-2 * np.pi * g * a)) - 1, 0.05, 1.0)          # M: alle Spins, Gewicht 2
    gT = brentq(lambda g: 2 * np.exp(-2 * np.pi * g * np.sqrt(0.75)) - 1, 0.05, 1.0)    # T: nur j = 1/2, Gewicht 2
    print(f"    gamma_M (alle Spins, Gewicht 2) = {gM:.6f}; gamma_T (nur j = 1/2) = {gT:.6f} = ln2/(pi sqrt3) {np.log(2) / (np.pi * np.sqrt(3)):.6f}")
    print(f"    gamma_M/2 = {gM / 2:.6f} gegen Delta Phi = {np.pi / 4 - 3 * te:.6f};  gamma_T/2 = {gT / 2:.6f}")
    print("    Lesart: Phase eines Spin-1/2-Objekts unter einer gamma-gewichteten Holonomie, Phi = gamma * m mit m = 1/2;")
    print("    der Oktant liefert Omega/2 = pi/4, also beide Teile von Phi_e als Spin-1/2-Phasen: Phi_e = pi/4 - gamma_M/2.")


def su2_spin(j):
    m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m)
    Jp = np.zeros((len(m), len(m)))
    for k in range(1, len(m)):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (Jp + Jp.T) / 2, (Jp - Jp.T) / 2j, Jz


if __name__ == "__main__":
    print("\n(6) Holonomie-Fluss-Paarung: Fluss E erzeugt Phasendrehungen der Holonomie, Kommutator mit Faktor gamma")
    g = gM
    # Flussoperator auf einer Kante mit Spin j: E^i = c * gamma * J^i (c = Flaecheneinheit); exp(i * alpha * E_3) dreht die Kante
    for j in (0.5,):
        Jx, Jy, Jz = su2_spin(j)
        m = 0.5
        psi = np.array([1.0, 0.0])                       # m = +1/2
        for lab, c, area_form in (("kappa-Einheiten (8 pi G hbar = 1), |m|", 1.0, abs(m)),
                                  ("kappa-Einheiten, sqrt(j(j+1))", 1.0, np.sqrt(j * (j + 1))),
                                  ("Planck-Einheiten (G hbar = 1), |m|", 8 * np.pi, abs(m)),
                                  ("Planck-Einheiten, sqrt(j(j+1)) (wie r10)", 8 * np.pi, np.sqrt(j * (j + 1)))):
            phase = c * g * area_form                     # Phase von exp(i E) auf dem Eigenzustand
            print(f"    {lab:44s}: Fluss-Eigenwert = Phase pro Einheitsdrehung = {phase:.5f} rad "
                  f"({'= gamma/2' if abs(phase - g / 2) < 1e-12 else f'{phase / (g / 2):.3f} x gamma/2'})")
        # Kontrolle der Erzeuger-Eigenschaft: [E_3, h] fuer h = exp(i theta J_x) eines Spin-1/2-Kantenstuecks
        E3 = g * Jz
        U = lambda a: np.diag(np.exp(1j * a * np.diag(E3)))
        print(f"    Kontrolle: exp(i E_3) auf |m = +1/2>: Phase {np.angle(U(1.0)[0, 0]):.5f} rad (= gamma * m)")
    print("    Ergebnis: gamma/2 entsteht nur mit Flaecheneinheit 8 pi G hbar und U(1)-Wert |m| statt sqrt(j(j+1));")
    print("    mit den Konventionen von r10 (8 pi gamma l_P^2 sqrt(j(j+1))) ergaebe sich 8 pi gamma sqrt(3)/2.")
