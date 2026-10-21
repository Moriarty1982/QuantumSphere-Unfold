"""K5: Einbettung des Primzahl-Registers in das Bost-Connes-System.

Bost-Connes (1995): Hilbertraum l^2(N*) mit Basis eps_n, Hamiltonoperator H eps_n = log(n) eps_n,
Zustandssumme Tr e^{-beta H} = zeta(beta). KMS-Struktur:
  beta > 1 : Gibbs-Zustaende existieren (Spurklasse), Symmetrie Z^-hat^x ~ Gal(Q^ab/Q) spontan gebrochen
  beta <= 1: genau ein KMS-Zustand, symmetrisch, KEINE Dichtematrix mehr (nur Zustand auf der Algebra)
Geprueft:
 (a) Bosonisches Register (K3) = l^2(N*) mit H = log n: Rueckkehramplitude zeta(beta+i tau)/zeta(beta).
 (b) Fermionisches Register (K4) = Unterraum der quadratfreien n.
 (c) Normierungsdivergenz am Phasenuebergang beta -> 1+.
 (d) Hochtemperatur-KMS-Zustand (beta <= 1) auf den Phasen e(a/b):
     phi_beta(e(a/b)) = b^-beta * prod_{p|b} (1 - p^(beta-1)) / (1 - p^-1)   [Bost-Connes, Prop. 24/Thm. 25]
     Plausibilitaet: bei beta = 1 verschwinden alle nichttrivialen Phasen (maximal ungeordnet).
"""
import numpy as np
import mpmath as mp
import sympy as sp

mp.mp.dps = 20
print("(a) Bosonische Rueckkehramplitude, beta = 2")
N = 300000
n = np.arange(1, N + 1, dtype=float)
for tau in (0.0, 3.0, 14.1347):
    reg = np.sum(n**(-2.0 - 1j*tau))/np.sum(n**-2.0)
    an = complex(mp.zeta(mp.mpc(2, tau))/mp.zeta(2))
    print(f"   tau={tau:8.4f}: Register {reg:.6f}  zeta(2+i tau)/zeta(2) {an:.6f}")

print("(b) Fermionisches Register als Unterraum: quadratfreie n bis 30:",
      [k for k in range(1, 31) if all(e == 1 for e in sp.factorint(k).values())])

print("(c) Zustandssumme am Phasenuebergang")
for beta in (2.0, 1.5, 1.1, 1.01, 1.001):
    print(f"   beta={beta:6.3f}: zeta(beta) = {float(mp.zeta(beta)):10.3f}")

print("(d) Hochtemperatur-KMS-Zustand auf Phasen e(a/b)")
def phi(beta, b):
    val = b**(-beta)
    for p in sp.primefactors(b):
        val *= (1 - p**(beta - 1))/(1 - 1/p)
    return val
for beta in (0.5, 0.9, 1.0):
    print(f"   beta={beta}: " + ", ".join(f"b={b}: {phi(beta, b):+.4f}" for b in (2, 3, 4, 6, 12)))
