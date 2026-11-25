"""k258c (Nachkontrolle zu H130, nach dem Lauf): Jacobi-Rang des Abschlussdefekts an den exakten Loesungspunkten.
Anlass: Eine von 600 Loesungen meldete in k258 zwei flache Richtungen (Parameter dort nicht normiert). Aufruf: python3 k258c_nachkontrolle.py"""
import numpy as np, k258_test_h130 as k
for tag, p in [('O_0', [1, 0, 0, 1, 0, 0, 0]), ('O_120', [-.5, 0, 3 ** .5 / 2, -.5, 0, 3 ** .5 / 2, 0]), ('B_+', [0, 1, 0, 2 ** -.5, 0, 0, 2 ** -.5])]:
    p = np.array(p, float)
    J = np.array([(k.defect(p + 1e-6 * e) - k.defect(p - 1e-6 * e)) / 2e-6 for e in np.eye(7)]).T
    sv = np.linalg.svd(J, compute_uv=False)
    print(f"{tag}: Defekt {(k.defect(p) ** 2).sum():.1e}; Singulaerwerte {np.round(sv, 4)}; flache Richtungen ausser 2 Normierungen und 1 Phase: {int((sv < 1e-5 * sv[0]).sum()) - 3}")
