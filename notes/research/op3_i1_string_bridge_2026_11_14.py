"""Erkundung (nicht blind): I1 als Ausweg fuer CT-002 - ein String vom Lepton-Sektor zu einer Horizont-Punktierung.

Rueckwaerts verlangt (CT-001, Schritte 1-3): Delta Phi = gamma_M * w * kappa mit w * kappa = 1/2
(gleichwertig: Delta Phi = gamma_M * normierte Sektorflaeche). Daten: kappa = 0.99964 +- 0.00016 rad bei w = 1/2.

Geometrie (euklidisches Rindler-Bild aus r10.1): Horizont = Zentrum, euklidische Zeit = Drehwinkel phi.
Ein gerader String vom Horizont (rho = 0) bis rho = l ueberstreicht in phi einen Kreissektor:
  Weltflaeche A_ws = l^2 phi / 2, Bogen des freien Endes s = l phi, A_ws/s = l/2, A_ws/l^2 = phi/2.
Kandidatenbedingungen fuer die Dauer (vor dem Rechnen aufgelistet; phi = 1 ist mit bekanntem Ziel gewaehlt):
  (a) eine Lichtquerung: Eigenzeit des freien Endes = Stringlaenge, s = l      -> phi = 1
  (b) halbe Querung s = l/2                                                    -> phi = 1/2
  (c) Hin und zurueck s = 2 l                                                  -> phi = 2
  (d) ein thermischer Umlauf phi = 2 pi (Zaehlregel)
Lesart: Delta Phi = gamma_M * A_ws / l^2 (gamma-K-Fluss durch die normierte Weltflaeche).
Lorentzsch: phi -> Rapiditaet eta; Eigenzeit des freien Endes l*eta, Lichtquerung eines Stabes der Laenge l im
momentanen Ruhesystem dauert l -> eta = 1.
Aufruf: python op3_i1_string_bridge_2026_11_14.py
"""
import numpy as np

GAMMA_M = 0.237533
NEED, SNEED = 0.118724, 0.000019        # Delta Phi aus den Massen (PDG 2024), 1 sigma


def sector(l, phi):
    A = l * l * phi / 2
    s = l * phi
    return A, s


if __name__ == "__main__":
    l = 3.3
    print("(1) Weltflaechen-Sektor eines am Horizont endenden Strings (l beliebig, hier 3.3):")
    cands = {"(a) eine Lichtquerung s = l": 1.0, "(b) halbe Querung s = l/2": 0.5,
             "(c) hin und zurueck s = 2l": 2.0, "(d) thermischer Umlauf 2 pi": 2 * np.pi}
    for name, phi in cands.items():
        A, s = sector(l, phi)
        dphi = GAMMA_M * A / l ** 2
        z = (dphi - NEED) / SNEED
        print(f"    {name:30s}: phi = {phi:.4f}, A/s = {A / s:.3f} (= l/2), A/l^2 = {A / l ** 2:.4f}, "
              f"Delta Phi = gamma_M A/l^2 = {dphi:.6f}, Abstand zu den Daten {z:+.1f} sigma")
    print("    Nur (a) trifft die Groessenordnung; (a) gibt genau gamma_M/2 (die 2,3 sigma von H102).")
    # Autorhinweis Schritt 2: A/s = r/2; mit s = r folgt A/r^2 = 1/2
    print("\n(2) Bezug zum Autorhinweis: A/s = l/2 fuer jeden Sektor; mit s = l (eine Querung) wird A/l^2 = 1/2 -> w = 1/2 aus der Flaeche.")
    # Lorentzsche Fassung
    for eta in (1.0,):
        tau_end = l * eta
        print(f"(3) Lorentzsch: Rapiditaet eta = {eta}: Eigenzeit des freien Endes {tau_end:.3f} = Stablaenge {l} "
              f"(Lichtquerung im momentanen Ruhesystem): {np.isclose(tau_end, l)}")
    # Identitaet mit der gamma-K-Lesart (Schritt 3): gamma * w * kappa mit kappa = phi
    phi = 1.0
    print(f"(4) gamma-K-Lesart: gamma * w * kappa mit kappa = phi = 1 und w = 1/2: {GAMMA_M * 0.5 * phi:.6f}; "
          f"Weltflaechen-Lesart gamma * A/l^2: {GAMMA_M * sector(l, phi)[0] / l ** 2:.6f} (identisch)")
    print(f"(5) Daten verlangen phi = {NEED / (GAMMA_M / 2):.5f} +- {SNEED / (GAMMA_M / 2):.5f}: "
          f"eine Querung ist 1 - {1 - NEED / (GAMMA_M / 2):.5f}, also 2.3 sigma daneben (wie H102).")
