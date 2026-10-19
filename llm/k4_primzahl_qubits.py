"""K4: Jede Primzahlmode ein Qubit.

Konstruktion: fermionisches Primon-Gas = Register aus Qubits, eines pro Primzahl p.
  |0>_p = Mode leer, |1>_p = Mode besetzt;  H = sum_p log(p) * n_p.
  Basiszustand |n> (n quadratfrei) = Qubits der Primteiler von n auf |1>.
Gepruefte Aussagen:
 (A) Tr exp(-sH) = prod_p (1 + p^-s) = zeta(s)/zeta(2s)                         (Register = fermionisches Primon-Gas)
 (B) Thermischer Produktzustand: Qubit p mit Gewicht |beta_p|^2/|alpha_p|^2 = p^-sigma.
     Rueckkehramplitude A(tau) = <Psi|exp(-i H tau)|Psi> = prod_p (1 + p^-(sigma+i tau)) / prod_p (1 + p^-sigma)
                                = Z_F(sigma + i tau) / Z_F(sigma)     (fuer sigma > 1 konvergent)
 (C) Jedes Qubit praezediert auf seiner Bloch-Kugel mit Frequenz log p um die z-Achse (Hopf-Faser-Phase).
 (D) Bei sigma = 1/2 (nur ueber analytische Fortsetzung definiert) verschwindet Z_F genau an den
     Nullstellen von zeta(1/2 + i tau): das Register erreicht dort einen zum Start ORTHOGONALEN Zustand.
     Numerischer Test: endliche Register (P Primzahlen) vs. analytische Fortsetzung.
"""
import numpy as np
import mpmath as mp
from functools import reduce

mp.mp.dps = 20

def primes_upto(N):
    s = np.ones(N + 1, bool); s[:2] = False
    for p in range(2, int(N**0.5) + 1):
        if s[p]: s[p*p::p] = False
    return np.nonzero(s)[0]

print("(A) Register-Spur = fermionische Zustandssumme")
P = primes_upto(7)                      # 4 Qubits: 2,3,5,7
s = 2.0
H_diag = np.array([sum(np.log(p) for p, b in zip(P, bits) if b)
                   for bits in np.ndindex(*([2]*len(P)))])
print(f"   Qubits {list(P)}: Tr e^-sH = {np.sum(np.exp(-s*H_diag)):.10f}  prod(1+p^-s) = {np.prod(1+P**-s):.10f}")
print(f"   16 Basiszustaende <-> quadratfreie n | 210:",
      sorted(int(round(np.exp(h))) for h in H_diag))

print("(B) Rueckkehramplitude = Z_F(sigma+i tau)/Z_F(sigma), sigma = 2, alle Primzahlen < 10^5")
Pb = primes_upto(100000).astype(float)
sig = 2.0
for tau in (0.0, 1.0, 5.0, 14.1347):
    A_reg = np.prod((1 + Pb**(-sig - 1j*tau)) / (1 + Pb**-sig))
    zf = lambda z: mp.zeta(z)/mp.zeta(2*z)
    A_an = complex(zf(mp.mpc(sig, tau))/zf(sig))
    print(f"   tau={tau:7.4f}: Register {A_reg:.6f}   analytisch {A_an:.6f}")

print("(C) Bloch-Praezession eines Qubits")
p = 5; a, b = np.sqrt(1/(1+p**-1.0)), np.sqrt(p**-1.0/(1+p**-1.0))
for tau in (0.0, 1.0, 2.0):
    psi = np.array([a, b*np.exp(-1j*np.log(p)*tau)])
    bx, by, bz = 2*np.real(np.conj(psi[0])*psi[1]), 2*np.imag(np.conj(psi[0])*psi[1]), abs(psi[0])**2-abs(psi[1])**2
    print(f"   p=5, tau={tau}: Bloch=({bx:+.4f},{by:+.4f},{bz:+.4f})  Azimut={np.arctan2(by,bx):+.4f} = -log5*tau mod 2pi")

print("(D) Kritische Linie sigma = 1/2: Orthogonalitaetszeiten")
gam = [float(mp.zetazero(k).imag) for k in range(1, 6)]
print("   Nullstellen gamma_k:", [round(g, 4) for g in gam])
taus = np.linspace(10, 34, 4801)
zF = np.array([abs(complex(mp.zeta(mp.mpc(0.5, t))/mp.zeta(mp.mpc(1.0, 2*t)))) for t in taus])
mins = [round(taus[i], 3) for i in range(1, len(taus)-1) if zF[i] < zF[i-1] and zF[i] < zF[i+1] and zF[i] < 1e-2]
print("   Minima von |Z_F(1/2+i tau)| (analytisch fortgesetzt):", mins)
for Pmax in (100, 10000, 1000000):
    Pr = primes_upto(Pmax).astype(float)
    logabs = np.array([np.sum(np.log(np.abs(1 + Pr**(-0.5 - 1j*t)))) for t in taus[::8]])
    tt = taus[::8]
    loc = [round(tt[i], 2) for i in range(1, len(tt)-1) if logabs[i] < logabs[i-1] and logabs[i] < logabs[i+1]]
    near = [min(loc, key=lambda u: abs(u-g)) if loc else None for g in gam]
    print(f"   endliches Register, {len(Pr):6d} Qubits: lokale Minima naechst an gamma_k: {near}")
