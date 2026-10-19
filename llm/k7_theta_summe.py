"""K7 / r05: Exakte Auswertung der Theta-Summen-Vermutung (Companion conj:theta-sum-B, OP5 Step B).

Vermutung:  T(T) := 2 sum_n sin(T*gamma_n/gL)/(gamma_n/gL)  =  3T/2 - log T - T^2/24 - gamma_E - bsym^2 T^2  ~ 0.893,
            T = gL^(-3/2).
Umformung:  T(T) = gL * S(a),  S(a) := 2 sum_{gamma>0} sin(a gamma)/gamma,  a = T/gL.

Exakter Weg (Riemann-von Mangoldt, x = e^a):
  psi0(x) = x - sum_rho x^rho/rho - log(2 pi) - (1/2) log(1 - x^-2)   (x > 1)
  Fuer 1 < x < 2 ist psi0(x) = 0, also  sum_rho x^rho/rho = x - log(2pi) - (1/2)log(1 - x^-2) =: F(a).
  Paarweise:  x^rho/rho + conj = 2 e^{a/2} [ (1/2)cos(a g) + g sin(a g) ] / (1/4 + g^2).
  Daraus  S(a) = e^{-a/2} F(a) - sum 2*(1/2)cos(a g)/(1/4+g^2) + sum 2*sin(a g)/(4 g (1/4+g^2)),
  beide Restsummen absolut konvergent (~1/g^2, ~1/g^3).
"""
import os
import numpy as np
import mpmath as mp

mp.mp.dps = 20
gBI = 0.2375
gs = float(mp.log(2)/(mp.pi*mp.sqrt(3)))
gL = gBI/gs
bsym2 = (gL - 1)/(gL + 1)
T = gL**-1.5
a = T/gL
gE = float(mp.euler)
conj = 1.5*T - np.log(T) - T**2/24 - gE - bsym2*T**2
print(f"gL = {gL:.6f}, T = {T:.6f}, a = T/gL = {a:.6f}  (a < log 2 = 0.6931: kein Primterm)")
print(f"Vermutete rechte Seite: {conj:.6f}")

gam = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeros.npy"))  # aus zeros_gen.py
N = len(gam)

def partial_direct(n):
    return gL*2*np.sum(np.sin(a*gam[:n])/gam[:n])

x = np.exp(a)
F = x - np.log(2*np.pi) - 0.5*np.log(1 - x**-2)
def exact(n):
    g = gam[:n]
    r1 = np.sum(np.cos(a*g)/(0.25 + g*g))
    r2 = np.sum(np.sin(a*g)/(2*g*(0.25 + g*g)))
    return gL*(np.exp(-a/2)*F - r1 + r2)

# Schwanzabschaetzung fuer r1 ueber Nullstellendichte (1/2pi) log(g/2pi): Betrag < int_{gN}^inf log(g/2pi)/(2pi g^2) dg
gN = gam[-1]
tail = (np.log(gN/(2*np.pi)) + 1)/(2*np.pi*gN)
print("\nDirekte Partialsummen (konvergieren nur bedingt):")
for n in (50, 500, N):
    print(f"   N={n:5d}: {partial_direct(n):+.6f}")
print("\nExakte Auswertung ueber die explizite Formel:")
for n in (50, 500, N):
    print(f"   N={n:5d}: T(T) = {exact(n):.6f}")
print(f"   Restfehler nach N Nullstellen < {gL*tail:.1e}")
print(f"\nErgebnis: T(T) = {exact(N):.4f}  vs. Vermutung {conj:.4f}  -> Differenz {exact(N)-conj:+.4f}")

# Was waere bsym^2, damit die Vermutung stimmt?
b2 = (1.5*T - np.log(T) - T**2/24 - gE - exact(N))/T**2
print(f"bsym^2, das die Gleichung erfuellen wuerde: {b2:.4f}  (Companion: {bsym2:.4f})")
