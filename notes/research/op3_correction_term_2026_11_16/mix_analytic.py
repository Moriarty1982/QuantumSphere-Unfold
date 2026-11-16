"""Analytische Kontrolle der dissipativen Mischung (Nachlauf): Mit nur J+ und J-^2 legt die Verschiebungsrichtung Delta p die Raten fest.
Fluesse: J+ : 0 -> +1 (2 g p0), -1 -> 0 (2 g p-);  J-^2 : +1 -> -1 (4 b p+).  Gesucht g, b >= 0 mit Delta p proportional zur Richtung."""
import numpy as np, correction_term as c
for name, s in c.STARTS.items():
    p = np.abs(s) ** 2; d = c.P_T - p
    # d = g*(2p0 - 0, ...) : Spalten = Wirkung je Einheitsrate
    vJp = np.array([2 * p[1], -2 * p[1] + 2 * p[2], -2 * p[2]])
    vJm2 = np.array([-4 * p[0], 0, 4 * p[0]])
    sol, res, *_ = np.linalg.lstsq(np.column_stack([vJp, vJm2]), d, rcond=None)
    print(f"{name}: Raten J+ = {sol[0]:.5f}, J-^2 = {sol[1]:.5f} (je Zeiteinheit x tau), Anteil J+ = {sol[0]/sol.sum():.3f}, Restfehler {np.linalg.norm(np.column_stack([vJp, vJm2]) @ sol - d):.1e}")
