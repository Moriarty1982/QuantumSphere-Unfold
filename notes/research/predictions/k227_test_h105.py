"""k227: Vorhersage zu H105 (nur Vorhersage, keine Daten).

Unter der Querungs-Lesart (v4.10.0-r24.4) mit Setzung V1 aendert jede Querung die Horizontflaeche um 4 ln 2 l_P^2
(Bekenstein-Mukhanov, alpha = 4 ln 2).  Ein Kerr-Loch nimmt Energie nur bei
    omega_n = n * alpha * kappa / (8 pi) + m * Omega_H
auf.  Das Skript gibt fuer eine Endmasse M (Sonnenmassen, Quelle-Ruhesystem) und einen Endspin a:
  - den Linienabstand in Hz,
  - die Frequenz des Grundtons (l = m = 2, n = 0) nach dem Fit von Berti, Cardoso, Will (2006), exakt bei a = 0,
  - seine Lage n zwischen den Linien und den Abstand zur naechsten Linie (in Linienabstaenden).
Aufruf: python k227_test_h105.py [M_sonne a] ...   (ohne Argumente: eine Beispieltabelle)
Die Beispielwerte sind runde Zahlen, keine Ereignisparameter.
"""
import sys
import numpy as np

G, c, MSUN = 6.67430e-11, 2.99792458e8, 1.98847e30
ALPHA = 4 * np.log(2)


def omega220(a):
    if a == 0:
        return 0.37367
    return 1.5251 - 1.1568 * (1 - a) ** 0.1292


def lines(M_sun, a):
    tM = G * M_sun * MSUN / c ** 3                       # M in Sekunden
    r = np.sqrt(1 - a * a)
    kappa, Om = r / (2 * (1 + r)), a / (2 * (1 + r))     # in Einheiten 1/M
    step = ALPHA * kappa / (8 * np.pi)
    w = omega220(a)
    n = (w - 2 * Om) / step
    to_hz = 1 / (2 * np.pi * tM)
    return step * to_hz, w * to_hz, n, abs(n - round(n))


def main(argv):
    pairs = [(float(argv[i]), float(argv[i + 1])) for i in range(0, len(argv) - 1, 2)] or \
            [(10, 0.0), (30, 0.7), (60, 0.7), (60, 0.9), (1e6, 0.7)]
    print(f"alpha = 4 ln 2 = {ALPHA:.6f}")
    print("   M/Msun     a   Linienabstand/Hz   f_220/Hz   Lage n   Abstand zur Linie")
    for M, a in pairs:
        s, f, n, d = lines(M, a)
        print(f"{M:9.3g}  {a:4.2f}   {s:14.5g}   {f:9.4g}   {n:6.3f}   {d:.3f}")


if __name__ == '__main__':
    main(sys.argv[1:])
