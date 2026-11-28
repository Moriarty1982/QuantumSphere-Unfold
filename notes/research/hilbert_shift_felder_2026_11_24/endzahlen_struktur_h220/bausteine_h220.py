"""Bausteine fuer H220: nur strukturelle Groessen des Rahmens. Nutzt die Aufzaehlung aus H219 mit anderen Blaettern/Operationen."""
import os
import sys

import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, nsum, findroot, inf

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "endzahlen_suche_h219"))
import enum_h219 as E  # noqa: E402

mp.dps = 30
GL = float(findroot(lambda g: nsum(lambda k: 2 ** (1 - g * msqrt(k * (k + 2) / mpf(3))), [1, inf]) - 1, 1.86))

LEAVES = {
    # Cayley-Dickson-Dimensionen und Imaginaerteile
    "1": 1.0, "2": 2.0, "4": 4.0, "8": 8.0, "16": 16.0, "3": 3.0, "7": 7.0,
    # Spin/Peirce und Koide-Form
    "1/2": 0.5, "2/3": 2.0 / 3.0,
    # Casimir-Flaechen sqrt(j(j+1)) fuer j = 1/2, 1, 3/2, 2
    "C(1/2)": np.sqrt(0.75), "C(1)": np.sqrt(2.0), "C(3/2)": np.sqrt(3.75), "C(2)": np.sqrt(6.0),
    # Zaehlregel r67
    "gL": GL,
}
UN = {"sqrt": np.sqrt, "sq": np.square, "inv": lambda x: 1.0 / x}


def enumerate_struct(smax):
    E.UN = UN
    return E.enumerate_exprs(smax, leaves=LEAVES)


if __name__ == "__main__":
    import time
    smax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    t = time.time()
    L = enumerate_struct(smax)
    tot = 0
    for s in sorted(L):
        tot += len(L[s][1])
        print(s, len(L[s][1]), tot, f"{time.time()-t:.1f}s")
