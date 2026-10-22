"""k66: Woher koennte das nachgefuellte Tachyon-Reservoir aus v4.9.0-r28 kommen?

Kriterien (vorab): (i) liefert fortlaufend nach, (ii) Tachyon polarisiert auf der Partnerport-Achse (Bezugszustand
b_T = (-1, 0)), (iii) Kopplung ueber T bzw. koharenter Austausch, (iv) keine verbotene Aussage.
Kandidaten aus dem Dokument (vorab): K1 Horizont/Hawking-Paare (thm:hawking-triolic, thm:core), K2 virtuelle Paare aus dem
Vakuum (prop:shared-vacuum-planck; Vakuum = Bezugsframe R nach v4.9.0-r24), K3 Kaskadenzufluss (thm:dark-energy:
P(S8 -> S4) = beta^2), K4 die uebrigen Moden des Feldes, K5 thermisches Bad ueber die Wick-Rotation (thm:wick),
K6 Tachyon-Trefferkette (v4.9.0-r06).
"""
import math
import numpy as np

sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)
U = lambda a: np.cos(a) * I2 - 1j * np.sin(a) * sy
rho_of = lambda bx, bz: (I2 + bx * sx + bz * sz) / 2
bvec = lambda r: np.array([np.trace(r @ sx).real, np.trace(r @ sz).real])
SW = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], complex)
ptr = lambda tot: np.einsum("ijkj->ik", tot.reshape(2, 2, 2, 2))
a6 = math.pi / 6
gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))

def coherent(rho, rT, th):
    V = math.cos(th) * np.eye(4) - 1j * math.sin(th) * SW
    return ptr(V @ np.kron(rho, rT) @ V.conj().T)
def markov(rho, rT, p):
    return (1 - p) * rho + p * rT
def fixpoint(step, rT, par, n=800):
    r = rho_of(1, 0)
    for _ in range(n):
        r = step(U(a6) @ r @ U(a6).conj().T, rT, par)
    return bvec(r)

print("K2: Bild des Vakuums R unter z -> iz:", tuple(np.round(bvec(sy @ rho_of(1, 0) @ sy), 6)), "= Tachyon-Bezugszustand (-1, 0)")

print("\n1. Polarisation des Reservoirs: Attraktor faellt mit |b_T| (nicht linear, der Kreuzterm des Tauschs haengt mit ab)")
th = math.asin(1 / math.sqrt(3))
for bT in (1.0, 0.5, 0.0):
    b = fixpoint(coherent, rho_of(-bT, 0), th)
    print("   |b_T| = %.2f: Attraktor |b| = %.4f" % (bT, np.linalg.norm(b)))
print("   K1 Horizont: am Photon-Fixpunkt von F (beta -> 1, v4.9.0-r23) ist b_T = 0 -> Attraktor 0, keine Stabilisierung")
print("   K5 thermisch: |b_T| = tanh(E/2kT) < 1 -> Attraktor verkleinert; T -> 0 gibt den Bezugszustand (= K2)")

print("\n2. Koharenter Austausch gegen Markov-Ersetzung, Staerke beta^2 (Kaskade K3)")
for name, b2 in (("Hopf", 1 / 3), ("gemessen", (gL - 1) / (gL + 1))):
    bc = fixpoint(coherent, rho_of(-1, 0), math.asin(math.sqrt(b2)))
    bm = fixpoint(markov, rho_of(-1, 0), b2)
    target = (1 - b2) / (1 + b2)
    print("   %-9s beta^2 = %.4f: koharent |b| = %.4f, Markov |b| = %.4f (Richtung %+.1f Grad), Selbstkonsistenz verlangt %.4f"
          % (name, b2, np.linalg.norm(bc), np.linalg.norm(bm), math.degrees(math.atan2(bm[1], -bm[0])), target))
c = 0.5
f = lambda p: p / math.sqrt(1 - 2 * (1 - p) * c + (1 - p) ** 2) - (1 - p) / (1 + p)
lo, hi = 0.01, 0.99
for _ in range(80):
    m = (lo + hi) / 2
    lo, hi = (m, hi) if f(lo) * f(m) > 0 else (lo, m)
print("   Markov selbstkonsistent bei p = %.4f (nicht 1/3); koharent genau bei beta^2 = 1/3 (r28)" % ((lo + hi) / 2))

print("\n3. Energiebilanz je Kick am Attraktor (koharent, Hopf): Abgabe an das Reservoir")
r = rho_of(*(-fixpoint(coherent, rho_of(-1, 0), th)))  # nur zur Form; Bilanz unten direkt
bfix = fixpoint(coherent, rho_of(-1, 0), th)
rf = rho_of(*bfix)
r1 = U(a6) @ rf @ U(a6).conj().T
V = math.cos(th) * np.eye(4) - 1j * math.sin(th) * SW
tot = V @ np.kron(r1, rho_of(-1, 0)) @ V.conj().T
rT_out = np.einsum("ijil->jl", tot.reshape(2, 2, 2, 2))
print("   Tachyon vorher b_T = (-1, 0), nachher b_T = (%.4f, %.4f): das Reservoir nimmt Polarisation auf und muss ersetzt werden"
      % tuple(bvec(rT_out)))

print("\n4. K4 uebrige Moden: liefern Dephasierung (r28.2(b)), keine Polarisation -> Attraktor 0")
print("   K6 Trefferkette: ein Tachyon trifft viele Materiesysteme gleichzeitig (r06) und ist danach nicht mehr im Bezugszustand;")
print("   er liefert nicht nach, sondern verteilt einen Bezugszustand. Das Paarereignis am Punkt unendlicher Geschwindigkeit (r06) ist K2.")
