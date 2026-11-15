"""Setzung (S2): Traegt R^2 = -1 die fermionische Lesart der Straenge in T? (Erkundung, nicht blind)

R auf einem Strang: z -> iz, auf chi als i sigma_z (R^2 = -1; v4.10.0-r14.3(d)); R^2 ist z -> -z = C = PT (v4.9.0-r02).
(1) Auf einem Buendel aus n Straengen wirkt R^2 als (-1)^n. Welche Spins ueberleben die Bedingung "R^2 = -1 auf der
    Punktierung" (ungerade n, symmetrisch) gegen "fermionischer Austausch" (Lambda^n)?
(2) Die drei Frame-Abbildungen haben auf chi die Determinante -1; Wirkung auf Lambda^2 (Singulett) und Sym^2.
"""
import numpy as np
from math import comb

print("(1) Bedingungen an ein Buendel aus n Straengen")
rows = []
for n in range(1, 9):
    j_sym = n / 2
    r2 = (-1) ** n
    lam = "j = 1/2" if n == 1 else ("j = 0" if n == 2 else "leer")
    rows.append((n, j_sym, r2, lam))
    print(f"    n = {n}: symmetrisch j = {j_sym}, R^2 = {r2:+d}; antisymmetrisch: {lam}")
kramers = [r[1] for r in rows if r[2] == -1]
print(f"    'R^2 = -1' waehlt die symmetrischen Buendel mit j = {kramers} (alle halbzahligen j = Kramers-Regel)")
print("    'fermionischer Austausch' waehlt nur j = 1/2")

print("(2) Frame-Abbildungen auf chi")
P = {"R": np.diag([1, -1]).astype(complex), "T": np.array([[0, 1], [1, 0]], complex), "J_B": np.array([[0, -1j], [1j, 0]])}
eps = np.array([[0, 1], [-1, 0]])
swap = np.zeros((4, 4))
for a in range(2):
    for b in range(2):
        swap[2 * b + a, 2 * a + b] = 1
Psym, Panti = (np.eye(4) + swap) / 2, (np.eye(4) - swap) / 2
for k, M in P.items():
    MM = np.kron(M, M)
    print(f"    {k:4s}: det = {np.linalg.det(M).real:+.0f}; auf Lambda^2: {np.trace(Panti @ MM).real:+.0f};"
          f" Spur auf Sym^2: {np.trace(Psym @ MM).real:+.0f}; vertauscht mit dem Austausch: {np.allclose(MM @ swap, swap @ MM)}")
print("    Die Frame-Abbildungen vertauschen mit dem Austausch; sie unterscheiden symmetrische und antisymmetrische Paare nicht.")
