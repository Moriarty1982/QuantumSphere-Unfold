"""k453c (Nachtrag, nachtraeglich): Waehlt die Wellenbedingung die drei Kopien aus, oder gilt sie fuer jeden Winkel theta?
U_theta = {cos(theta) e_i + sin(theta) e_(8+i), i = 1..7} (G2-stabil als Richtungsraum fuer jedes theta; als Algebra nur fuer drei theta, H138).
Aufruf aus diesem Ordner: python3 k453c_kreis.py > k453c_out.txt
"""
import numpy as np
src = open("k453_test_h237.py").read().split('print("=" * 100)')[0]
exec(src)
print("k453c  Wellendefekt und Abgeschlossenheit als Funktion von theta")
for deg in (0, 15, 30, 45, 60, 90, 120, 180, 240, 300, 37.5):
    t = np.deg2rad(deg)
    U = [np.cos(t) * E[i] + np.sin(t) * E[8 + i] for i in range(1, 8)]
    d, dw, W = wave(U)
    # Abgeschlossenheit: liegt u_a u_b in span{1, U}?
    B = np.array([E[0]] + U); P = B.T @ B
    cl = max(np.abs(mul(a, b) - P @ mul(a, b)).max() for a in U for b in U)
    print(f"  theta = {deg:6.1f} Grad: delta = {d:.1e}, dim W = {dw}, Abgeschlossenheitsdefekt {cl:.2e} ({'Unteralgebra' if cl < 1e-9 else 'keine Unteralgebra'})")
