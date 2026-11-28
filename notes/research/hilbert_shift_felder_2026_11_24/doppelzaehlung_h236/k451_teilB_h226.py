"""k451 Teil B (Test H236, blind): H226 Teil B in der Phi-Lesart nachgerechnet, q in {-1e-2, -1e-3} statt -0,0852.
Funktionen unveraendert aus ../tauschbruch_phi_h226/k440_test_h226.py; Gitter der Koeffizienten fuer T1/T4 mit |q|/0,0852 skaliert.
Aufruf aus diesem Ordner: python3 k451_teilB_h226.py > k451_teilB_out.txt
"""
import sys, os
import numpy as np
from scipy.optimize import brentq
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "..", "tauschbruch_phi_h226", "k440_test_h226.py")).read().split('print("=" * 92)')[0]
exec(src)

print("H236 Teil B: H226 B bei kleinem q (Phi-Lesart). Kriterium: Urteil bleibt, wenn kein Term T1-T3 delta_Im = delta* am globalen"
      " Minimum UND x_nu innerhalb 2 sigma gibt.")
kippt = False
for q in (-1e-2, -1e-3):
    s = abs(q) / 0.0852
    print(f"\n q = {q:g}")
    for name, mk in list(TERMS.items())[:3]:
        grid = np.linspace(-1, 1, 81) * s if name.startswith("T1") else np.linspace(0.05, 3, 60)
        rows = []
        for c in grid:
            pg, eg, _, _ = global_min(q, n=240, **mk(c))
            (eI, dI), (eR, dR) = sectors(pg, q, **mk(c))
            rows.append((c, pg, fold(dI), fold(dR)))
        f = [r[2] - DSTAR for r in rows]
        sols = []
        for i in range(len(rows) - 1):
            if np.sign(f[i]) != np.sign(f[i + 1]) and abs(f[i] - f[i + 1]) < 0.05:
                def g(c):
                    pg, _, _, _ = global_min(q, n=240, **mk(c))
                    return fold(sectors(pg, q, **mk(c))[0][1]) - DSTAR
                try:
                    c0 = brentq(g, rows[i][0], rows[i + 1][0], xtol=1e-11)
                except ValueError:
                    continue
                pg, _, _, _ = global_min(q, n=240, **mk(c0))
                (eI, dI), (eR, dR) = sectors(pg, q, **mk(c0))
                sols.append((c0, pg, fold(dI), np.pi / 6 - fold(dR)))
        print(f"  {name}: delta_Im am globalen Minimum ueber dem Gitter {min(r[2] for r in rows):.4f} bis {max(r[2] for r in rows):.4f}"
              f" (Ziel {DSTAR:.4f})")
        if not sols:
            print("     keine Loesung")
        for c0, pg, dI, xnu in sols:
            ok = abs(xnu - XNU) < 2 * SXNU
            kippt |= ok
            print(f"     Koeffizient {c0:+.6e}: phi* = {pg:+.6f}, delta_Im = {dI:.7f}, x_nu,pred = {xnu:+.5f} ({(xnu-XNU)/SXNU:+.1f} sigma)"
                  f" -> {'innerhalb 2 sigma' if ok else 'ausserhalb'}")
print(f"\nTeil B: Urteil von H226 {'KIPPT' if kippt else 'BLEIBT'}")
