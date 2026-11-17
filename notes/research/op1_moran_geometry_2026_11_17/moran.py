"""OP1: Die Zaehlgleichung als Moran-Gleichung eines selbstaehnlichen Fraktals.  (Erkundung, nicht blind: gamma-Werte bekannt.)

Zaehlgleichung je Frame: sum_j g(j) exp(-2 pi gamma a(j)) = 1.  In Einheiten des T-Quants (2 pi gamma_T a(1/2) = ln 2) mit D = gamma/gamma_T:
  sum_j g(j) r_j^D = 1,  r_j = 2^{-a(j)/a(1/2)}.
Das ist die Moran-Gleichung: Ein selbstaehnliches Fraktal mit g(j) Kopien auf der Skala r_j (offene-Mengen-Bedingung) hat die
Hausdorff-Dimension D (fuer abzaehlbar viele Abbildungen: Mauldin-Urbanski).  Also D_frame = gamma_frame/gamma_T.
Geprueft: D fuer M, P, T in mehreren Spektren; ob die Kopien ueberlappungsfrei in R^d passen (Regalpackung von Quadraten bzw. Wuerfeln).
"""
import numpy as np
from scipy.optimize import brentq

n = np.arange(1, 200001)   # n = 2j
specs = {"sqrt(j(j+1))": lambda j: np.sqrt(j * (j + 1)), "j": lambda j: j, "j+1/2": lambda j: j + 0.5}
rules = {"T": lambda n: (n == 1) * 2.0, "M": lambda n: 2.0 + 0 * n, "P": lambda n: n + 1.0}

def moran(g, r):
    return brentq(lambda D: np.sum(g * r ** D) - 1, 0.01, 10)

res = {}
for sn, a in specs.items():
    r = 2.0 ** (-a(n / 2) / a(0.5))
    line = []
    for rn, g in rules.items():
        D = moran(g(n), r); res[(sn, rn)] = (D, g(n), r); line.append(f"{rn}: D = {D:.6f}")
    print(f"{sn:13s} " + ", ".join(line))
print(f"Vergleich: gamma_M/gamma_T = {0.237533/0.127384:.6f}, gamma_P/gamma_T = {0.274067/0.127384:.6f}, log2 3 = {np.log2(3):.6f}")

# Regalpackung: passen die Kopien (Seitenlaenge r) ueberlappungsfrei in den Einheitswuerfel der Dimension d?
def shelf_pack_2d(sizes):
    sizes = sorted(sizes, reverse=True); y = 0.0; x = 0.0; h = 0.0
    for s in sizes:
        if s > 1: return False
        if x + s > 1 + 1e-12: y += h; x = 0.0; h = 0.0
        if y + s > 1 + 1e-12: return False
        x += s; h = max(h, s)
    return True

def shelf_pack_3d(sizes):
    # Schichten: jede Schicht ist eine 2D-Regalpackung, Schichthoehe = groesste Kante der Schicht
    sizes = sorted(sizes, reverse=True); z = 0.0; i = 0
    while i < len(sizes):
        layer = []; hz = sizes[i]
        y = x = h = 0.0
        while i < len(sizes):
            s = sizes[i]
            if x + s > 1 + 1e-12: y += h; x = 0.0; h = 0.0
            if y + s > 1 + 1e-12: break
            x += s; h = max(h, s); layer.append(s); i += 1
        if not layer: return False
        z += hz
        if z > 1 + 1e-12: return False
    return True

for sn in ("sqrt(j(j+1))",):
    for rn in ("T", "M", "P"):
        D, g, r = res[(sn, rn)]
        sizes = np.repeat(r[:400], g[:400].astype(int))
        sizes = sizes[sizes > 0]
        s2, s3 = np.sum(g * r ** 2), np.sum(g * r ** 3)
        print(f"{sn} {rn}: D = {D:.4f}; Flaeche sum g r^2 = {s2:.4f}, Volumen sum g r^3 = {s3:.4f}; "
              f"passt in Quadrat: {shelf_pack_2d(sizes) if rn != 'T' else 'Strecke (zwei Haelften)'}; in Wuerfel: {shelf_pack_3d(sizes)}")
D, g, r = res[("sqrt(j(j+1))", "M")]
print(f"Breite von M: b_M = 1/D_M = {1/D:.4f} (Konvention F: 0,5363); beta^2 = (D-1)/(D+1) = {(D-1)/(D+1):.4f}")
