"""Erkundung (nicht blind): Flaeche gegen Winkel am Kreissektor, Schritt 2 fuer CT-001 (14.11.2026).

Hinweis des Autors: einmal wird eine Kreisflaeche im Verhaeltnis zur Bogenlaenge gemessen, einmal der eingeschlossene Winkel.
Sektor mit Oeffnungswinkel theta, Radius r: Flaeche A = r^2 theta / 2, Bogen s = r theta, A/s = r/2, A/r^2 = theta/2.
Lesart: Der Flaechenbeitrag einer Punktierung, A_j = 8 pi gamma a(j) l_P^2 (r10), ist die Flaeche eines Sektors mit
Oeffnungswinkel theta = gamma; daraus r_j^2 = 2 A_j / gamma = 16 pi a(j) l_P^2 (unabhaengig von gamma).
Drei Messweisen derselben Flaeche:
  (i)   relativ zum eigenen Kreis: A/r^2 = gamma/2            (unabhaengig von j und von Einheiten)
  (ii)  in Einheiten 8 pi G hbar: A/(8 pi l_P^2) = gamma a(j)
  (iii) in Einheiten G hbar (r10): A/l_P^2 = 8 pi gamma a(j)
Prueft: Reproduziert das die Konventionstabelle von CT-001 (gamma/2; 1,73-fach; 43,5-fach)?
Dazu r10.1 (Frodden-Ghosh-Perez, Unruh): E_j = A_j/(8 pi G l), beta = 2 pi l -> E beta = A_j/(4 G hbar) = 2 pi gamma a(j);
Phase pro Radiant der euklidischen Drehung = gamma a(j) = Messweise (ii).
Aufruf: python ct001_sector_reading_2026_11_14.py
"""
import numpy as np

GAMMA_M = 0.237533
TABLE = {"8piGhbar=1, |m|=1/2": 0.11877, "8piGhbar=1, sqrt(j(j+1))": 0.2057, "Ghbar=1, sqrt(j(j+1)) (r10)": 5.170}


def a(j):
    return np.sqrt(j * (j + 1))


if __name__ == "__main__":
    print("(0) Sektor: A = r^2 theta/2, s = r theta -> A/s = r/2, A/r^2 = theta/2 (Kontrolle numerisch):")
    for r, th in ((1.0, GAMMA_M), (3.7, GAMMA_M), (2.0, 1.0)):
        A, s = r * r * th / 2, r * th
        print(f"    r = {r}, theta = {th}: A/s = {A / s:.6f} (= r/2 {r / 2}), A/r^2 = {A / r ** 2:.6f} (= theta/2 {th / 2:.6f})")
    print("\n(1) Punktierung j als Sektor mit Oeffnungswinkel gamma_M (l_P = 1):")
    for j in (0.5, 1.0, 1.5):
        Aj = 8 * np.pi * GAMMA_M * a(j)
        r2 = 2 * Aj / GAMMA_M
        m1, m2, m3 = Aj / r2, Aj / (8 * np.pi), Aj
        print(f"    j = {j}: r_j^2 = {r2:.4f} (= 16 pi a(j) = {16 * np.pi * a(j):.4f}); (i) A/r^2 = {m1:.6f}, "
              f"(ii) A/8pi = {m2:.6f}, (iii) A = {m3:.4f}; Verhaeltnisse (ii)/(i) = {m2 / m1:.4f}, (iii)/(i) = {m3 / m1:.4f}")
    print("\n(2) Abgleich mit der Konventionstabelle von CT-001 (j = 1/2):")
    Aj = 8 * np.pi * GAMMA_M * a(0.5); r2 = 2 * Aj / GAMMA_M
    mine = [Aj / r2, Aj / (8 * np.pi), Aj]
    for (k, v), w in zip(TABLE.items(), mine):
        print(f"    {k:30s}: Tabelle {v:.5f}, Sektor-Lesart {w:.5f}, Abweichung {abs(v - w) / v:.1e}")
    print(f"    Faktoren: 2 a(1/2) = sqrt3 = {2 * a(0.5):.4f} (Tabelle 1,73), 16 pi a(1/2) = 8 pi sqrt3 = {16 * np.pi * a(0.5):.3f} (Tabelle 43,5)")
    print("\n(3) r10.1 (Unruh): E beta = A_j/(4 G hbar) = 2 pi gamma a(j) -> Phase pro Radiant gamma a(j) = Messweise (ii):")
    for j in (0.5,):
        print(f"    j = {j}: 2 pi gamma a(j) = {2 * np.pi * GAMMA_M * a(j):.6f}, pro Radiant {GAMMA_M * a(j):.6f}")
    print("\n(4) Verlangt (Massen, CT-001 Schritt 1): Delta Phi = 0.118724 (1 sigma 0.118705 .. 0.118743); "
          f"Messweise (i) gibt gamma_M/2 = {GAMMA_M / 2:.6f}")
