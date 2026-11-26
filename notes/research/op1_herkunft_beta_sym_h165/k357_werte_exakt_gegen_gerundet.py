"""k357 (Erkundung, kein Test): abgeleitete Zahlen beim exakten beta_sym gegen den Wert aus gerundeten Eingaben.
Aufruf: python k357_werte_exakt_gegen_gerundet.py
"""
import mpmath as mp
mp.mp.dps = 30
c = lambda k: mp.sqrt(mp.mpf(k) * (k + 2) / 3)
gL = mp.findroot(lambda g: mp.nsum(lambda k: 2 ** (1 - g * c(k)), [1, mp.inf]) - 1, 1.9)
b_ex = mp.sqrt((gL - 1) / (gL + 1))
b_rd = mp.sqrt((mp.mpf("0.2375") - mp.mpf("0.1274")) / (mp.mpf("0.2375") + mp.mpf("0.1274")))
b_old = mp.mpf("0.5493482")
deg = lambda x: x * 180 / mp.pi
def row(b):
    g = (1 + b * b) / (1 - b * b)
    return [("beta", b), ("beta^2 (Omega_M in H96)", b * b), ("gamma_L", g), ("gamma_L^5", g ** 5), ("1/gamma_L", 1 / g),
            ("epsilon = artanh beta", mp.atanh(b)), ("theta_H [Grad]", deg(2 * mp.asin(b))), ("pi - theta_H [Grad]", 180 - deg(2 * mp.asin(b))),
            ("alpha = arctan beta [Grad]", deg(mp.atan(b))), ("2 alpha [Grad]", 2 * deg(mp.atan(b))),
            ("Besetzung 1/(1+beta^2)", 1 / (1 + b * b)), ("Besetzung beta^2/(1+beta^2)", b * b / (1 + b * b)),
            ("Mischung (1+beta)/2", (1 + b) / 2), ("K = (1+beta^4)/3", (1 + b ** 4) / 3), ("kappa = (gamma_L+1/gamma_L)/2", (g + 1 / g) / 2),
            ("Hopf-Luecke in beta [%]", (1 / mp.sqrt(3) / b - 1) * 100), ("Hopf-Luecke in gamma_L [%]", (2 / g - 1) * 100)]
print("exakt (Zaehlregel):", mp.nstr(b_ex, 12), "; aus gerundeten Eingaben 0.2375/0.1274:", mp.nstr(b_rd, 12), "; im Bestand gefuehrt:", mp.nstr(b_old, 9))
print(f"{'Groesse':34s} {'exakt':>16s} {'Bestand 0.5493482':>18s} {'rel. Unterschied':>18s}")
for (n, a), (_, o) in zip(row(b_ex), row(b_old)):
    print(f"{n:34s} {mp.nstr(a, 10):>16s} {mp.nstr(o, 10):>18s} {mp.nstr(a / o - 1, 3):>18s}")
print("\nSchwellen:")
print("Leptonfenster [0.545; 0.570] (r61.1e): exakt drin =", 0.545 <= b_ex <= 0.570, "; Bestand drin =", 0.545 <= b_old <= 0.570)
print("Fenster der Dimensionsleiter fuer gamma_T [0.127384; 0.137033): unberuehrt (haengt nicht an beta)")
print("H96: Omega_M = beta^2 exakt =", mp.nstr(b_ex ** 2, 7), "(im Bestand schon 0.30185, r61.2); mit 0.5493482 waere es", mp.nstr(b_old ** 2, 7))
