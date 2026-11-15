"""Nachrechnung H2 (v4.8.0-r12, Vorab 434c5a8, k15) am 15.11.2026: Reproduktion und neuere Eingaben.

Verwendet die Funktionen aus k15_test_h2.py (unveraendert). Eingabevarianten fuer Delta m^2_21 (normale Ordnung):
NuFIT 6.0 (wie vorab festgelegt) 7.49 +- 0.19; JUNO erste Daten (Nature 2026, 59,1 Tage) 7.50 +- 0.12; SNO+ 7.63 +- 0.17;
Delta m^2_31 dazu NuFIT 6.0 (2.513 +- 0.020). Zusaetzlich NuFIT 6.1 vollstaendig (Primaertabelle, wie in Ergebnis_H99):
Delta m^2_21 = 7.537 (+0.094/-0.10), Delta m^2_31 = 2.511 (+0.021/-0.020). Aufruf: python h2_recheck.py <Pfad zu notes/research/v4_8_0_r03_r12/llm>
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.abspath(sys.argv[1]))
import k15_test_h2 as k

rng = np.random.default_rng(1115)
for label, d21, s21, D31, s31 in (("NuFIT 6.0 (vorab)", 7.49e-5, 0.19e-5, k.D31_NO, k.s31_NO), ("JUNO 2026", 7.50e-5, 0.12e-5, k.D31_NO, k.s31_NO),
                                  ("SNO+", 7.63e-5, 0.17e-5, k.D31_NO, k.s31_NO), ("NuFIT 6.1", 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3)):
    sols = k.solve("NO", d21, D31)
    s = sols[0]
    sig = []
    for x, y in zip(rng.normal(d21, s21, 20000), rng.normal(D31, s31, 20000)):
        r = k.solve_fast("NO", x, y, sols)
        if 0 in r: sig.append(r[0][0])
    sig = np.array(sig)
    floor = np.sqrt(d21) + np.sqrt(D31)
    print(f"{label:18s}: m = ({s['m'][0]*1e3:.3f}, {s['m'][1]*1e3:.3f}, {s['m'][2]*1e3:.3f}) meV, Sigma = {s['Sigma']:.5f} eV,"
          f" MC {sig.mean():.5f} +- {sig.std():.5f} eV; Untergrenze NO (m1 = 0) {floor:.5f} eV; Abstand {1e3*(s['Sigma']-floor):.2f} meV")
print("Kosmologie (DESI DR2 + CMB, LCDM): Sigma < 0.0642 eV (vorab festgelegte Grenze); Feldman-Cousins-Variante < 0.053 eV")
