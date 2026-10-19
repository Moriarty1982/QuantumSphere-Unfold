"""K2: Raumzeit-Punkte aus Spinoren (Informationsebene) und Takten (Riemann-Taktgeber).

Behauptungen, die hier numerisch/symbolisch geprueft werden:
 (a) k(psi) = (|psi|^2, psi^+ sigma psi) ist lichtartig; die Raumrichtung ist die Hopf-Abbildung S^3 -> S^2.
 (b) Jeder zukunftsgerichtete zeitartige Vektor x ist Summe zweier zukunftsgerichteter Nullvektoren,
     x = tau_a k(psi_a) + tau_b k(psi_b), tau_a, tau_b > 0  (Ereignis = zwei Spinoren + zwei Takte).
 (c) Mit Takten aus endlich vielen Zeta-Nullstellen-Ordinaten (numerisch bekannt, ohne RH) entsteht eine
     endliche, diskrete Punktmenge im Zukunftskegel.
"""
import numpy as np
import mpmath as mp

sig = [np.array([[0, 1], [1, 0]], complex),
       np.array([[0, -1j], [1j, 0]]),
       np.array([[1, 0], [0, -1]], complex)]
eta = np.diag([-1.0, 1, 1, 1])

def k(psi):
    psi = np.asarray(psi, complex)
    return np.array([np.vdot(psi, psi).real] + [np.vdot(psi, s @ psi).real for s in sig])

def mink(a, b): return a @ eta @ b

def spinor_of_null(kv):
    """Spinor psi mit k(psi) = kv fuer zukunftsgerichteten Nullvektor kv (bis auf Phase)."""
    t, x, y, zc = kv
    if t + zc > 1e-14:
        a = np.sqrt((t + zc)/2)
        return np.array([a, (x + 1j*y)/(2*a)])
    return np.array([0, np.sqrt(t)])

rng = np.random.default_rng(7)

print("(a) Lichtartigkeit und Hopf-Abbildung")
for _ in range(3):
    psi = rng.normal(size=2) + 1j*rng.normal(size=2)
    kv = k(psi)
    print("   <k,k> =", f"{mink(kv, kv):+.2e}", "  Richtung |n| =", round(np.linalg.norm(kv[1:]/kv[0]), 12))

print("(b) Zeitartiges Ereignis = zwei Spinoren + zwei Takte")
for _ in range(3):
    v = rng.normal(size=3); x = np.array([np.linalg.norm(v) + abs(rng.normal()) + 0.1, *v])
    # Zerlegung im Ruhesystem-artigen Ansatz: waehle Einheitsrichtung n, x = a(1,n) + b(1,-n) + Korrektur
    # allgemein: x = tau_a k_a + tau_b k_b mit k_a, k_b Nullvektoren; konstruktiv:
    m = np.sqrt(-mink(x, x))                       # Eigenzeit
    n = rng.normal(size=3); n -= (n @ x[1:])/(x[1:] @ x[1:] + 1e-300)*x[1:] if np.linalg.norm(x[1:]) > 0 else 0
    n /= np.linalg.norm(n)
    # Boost-freie Konstruktion: k_pm = (x +- m*e)/2 mit e raumartig, <e,x>=0, <e,e>=1
    e = np.array([0, *n])                          # <e,x> = n.v = 0 per Wahl von n
    e = e/np.sqrt(mink(e, e))
    kp, km = (x + m*e)/2, (x - m*e)/2
    psa, psb = spinor_of_null(kp), spinor_of_null(km)
    rec = k(psa) + k(psb)
    print("   <k+,k+>,<k-,k-> =", f"{mink(kp,kp):+.1e}, {mink(km,km):+.1e}",
          " k+0,k-0 > 0:", kp[0] > 0 and km[0] > 0, "  Rekonstruktion exakt:", np.allclose(rec, x))

print("(c) Takte aus Zeta-Nullstellen (erste 6 Ordinaten, numerisch)")
mp.mp.dps = 20
gam = [float(mp.zetazero(n).imag) for n in range(1, 7)]
print("   gamma_n =", [round(g, 6) for g in gam])
psi_a = np.array([1, 0], complex); psi_b = np.array([0, 1], complex)   # zwei Qubits: Nord-/Suedpol
pts = [ta*k(psi_a) + tb*k(psi_b) for ta in gam for tb in gam]
tau = sorted({round(np.sqrt(-mink(p, p)), 6) for p in pts})
print("   Eigenzeiten der 36 Ereignisse (zwei feste Qubits):", tau[:8], "...")
print("   Eigenzeit = 2*sqrt(tau_a*tau_b):", np.isclose(np.sqrt(-mink(pts[1], pts[1])), 2*np.sqrt(gam[0]*gam[1])))
