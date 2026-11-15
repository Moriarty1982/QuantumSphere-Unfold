"""Bruecke (A), Kandidat: die Barbero-Verbindung als Punkt des Dubletts (A+, A-) (Erkundung, nicht blind).

A_pm = Gamma +- i K (selbst- und antiselbstduale Ashtekar-Verbindung), A_gamma = Gamma + gamma K.
(1) A_gamma = c+ A+ + c- A- mit c_pm = (1 -+ i gamma)/2; reelles gamma -> |c+| = |c-| (Aequator), gamma = +-i -> Pole.
(2) Wirken die Frame-Abbildungen auf (c+, c-) wie auf chi (R = sigma_z, T = sigma_x, J_B = sigma_y), dann auf gamma als
    Moebius-Abbildungen; welche?
(3) Bildet eine Frame-Abbildung gamma_M auf gamma_T ab?
(4) Die Frame-Eigenzustaende (Pole) in gamma-Sprache.
"""
import numpy as np

rng = np.random.default_rng(1)
Gam, K = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
g = 0.37
Ap, Am = Gam + 1j * K, Gam - 1j * K
cp, cm = (1 - 1j * g) / 2, (1 + 1j * g) / 2
print(f"(1) A_gamma = c+ A+ + c- A-: {np.allclose(Gam + g * K, cp * Ap + cm * Am)}; reelles gamma: |c+| = |c-|: {np.isclose(abs(cp), abs(cm))}")


def gamma_of(c):
    # c = (c+, c-) bis auf gemeinsamen Faktor; c+ = (1 - i g)/2, c- = (1 + i g)/2  ->  g = i (c+ - c-)/(c+ + c-)
    return 1j * (c[0] - c[1]) / (c[0] + c[1])


P = {"R": np.diag([1, -1]).astype(complex), "T": np.array([[0, 1], [1, 0]], complex), "J_B": np.array([[0, -1j], [1j, 0]])}
print("(2) Wirkung auf gamma (an Zufallswerten gegen die Formeln geprueft)")
forms = {"R": lambda x: -1 / x, "T": lambda x: -x, "J_B": lambda x: 1 / x}
for k, M in P.items():
    dev = max(abs(gamma_of(M @ np.array([(1 - 1j * x) / 2, (1 + 1j * x) / 2])) - forms[k](x)) for x in rng.uniform(0.05, 3, 50))
    print(f"    {k:4s}: gamma -> {['-1/gamma', '-gamma', '1/gamma'][list(P).index(k)]} (Abweichung {dev:.1e})")
GM, GT = 0.237533, np.log(2) / (np.pi * np.sqrt(3))
imgs = {k: f(GM) for k, f in forms.items()}
print(f"(3) gamma_M = {GM}, gamma_T = {GT:.6f}; Bilder von gamma_M: " + ", ".join(f"{k}: {v:.4f}" for k, v in imgs.items())
      + f" -> keine gleich gamma_T")
print("(4) Pole in gamma-Sprache: T-Achse (Materie/Tachyon) gamma = 0 bzw. unendlich; J_B-Achse gamma = -1, +1;"
      " R-Achse (selbst-/antiselbstdual) gamma = +i, -i")
for name, x in (("gamma_M", GM), ("gamma_T", GT)):
    print(f"    {name}: Aequatorwinkel 2 arctan gamma = {np.degrees(2*np.arctan(x)):.3f} Grad")
