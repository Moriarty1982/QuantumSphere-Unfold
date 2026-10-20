"""K9 / r06: Lesart B — Pruefungen fuer die Companion-Runde.

 (1) Veronese-Abbildung psi -> z(psi) = (psi1^2 - psi2^2, i(psi1^2 + psi2^2), -2 psi1 psi2):
     Bild liegt im Nullkegel sum z^2 = 0; jeder Nullvektor hat genau zwei Urbilder +-psi
     -> projektivierter Nullkegel = Bild von CP^1 (Kegelschnitt in CP^2).
 (2) Aequivarianz: komplexe Einheits-Biquaternion u wirkt auf z als SO(3,C); auf psi als SL(2,C).
     Pruefung: Bild eines Nullvektors bleibt Nullvektor, sum z^2 invariant fuer beliebiges z.
 (3) Orbit-Aussage: zwei Vektoren mit gleichem s != 0 lassen sich durch SO(3,C) ineinander ueberfuehren
     (konstruktiv: jeder z mit s != 0 wird auf (sqrt(s),0,0) gedreht).
 (4) Symmetrische Triole: Spinor und Nullbedingung.
"""
import numpy as np
rng = np.random.default_rng(11)

def zpsi(p): return np.array([p[0]**2 - p[1]**2, 1j*(p[0]**2 + p[1]**2), -2*p[0]*p[1]])
def psi_of(z):
    a = (z[0] - 1j*z[1])/2      # psi1^2
    b = (-z[0] - 1j*z[1])/2     # psi2^2
    p1 = np.sqrt(a); p2 = np.sqrt(b)
    for s in (1, -1):
        if np.allclose(zpsi(np.array([p1, s*p2])), z): return np.array([p1, s*p2])
    return None

print("(1) Veronese / Nullkegel")
ok_null = all(abs(np.sum(zpsi(rng.normal(size=2) + 1j*rng.normal(size=2))**2)) < 1e-12 for _ in range(200))
ok_inv = True
for _ in range(200):
    p = rng.normal(size=2) + 1j*rng.normal(size=2); z = zpsi(p); q = psi_of(z)
    ok_inv &= q is not None and (np.allclose(q, p) or np.allclose(q, -p))
print("   Bild im Nullkegel:", ok_null, "| Urbild genau +-psi:", ok_inv)

print("(2) SO(3,C)-Wirkung ueber komplexe Einheits-Biquaternionen")
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
qbar = lambda q: np.array([q[0], -q[1], -q[2], -q[3]])
N = lambda q: qmul(q, qbar(q))[0]
ok_s, ok_n = True, True
for _ in range(200):
    u = rng.normal(size=4) + 1j*rng.normal(size=4); u = u/np.sqrt(N(u))
    z = rng.normal(size=3) + 1j*rng.normal(size=3)
    w = qmul(qmul(u, np.array([0, *z])), qbar(u))
    ok_s &= np.isclose(np.sum(w[1:]**2), np.sum(z**2)) and abs(w[0]) < 1e-10
    zn = zpsi(rng.normal(size=2) + 1j*rng.normal(size=2))
    wn = qmul(qmul(u, np.array([0, *zn])), qbar(u))
    ok_n &= abs(np.sum(wn[1:]**2)) < 1e-9
print("   sum z^2 invariant, Skalarteil bleibt 0:", bool(ok_s), "| Nullkegel invariant:", bool(ok_n))

print("(3) Orbit durch s: Drehung von z auf (sqrt(s),0,0)")
def to_axis(z):
    s = np.sum(z**2); r = np.sqrt(s)
    e1 = z/r                                   # e1.e1 = 1 (komplex-bilinear)
    # Ergaenzung zu komplex-orthonormaler Basis (e1, e2, e3) mit det = 1
    v = rng.normal(size=3) + 0j
    e2 = v - (e1@v)*e1; e2 = e2/np.sqrt(e2@e2)
    e3 = np.cross(e1, e2)
    R = np.array([e1, e2, e3])                 # Zeilen: R z = (r, 0, 0)
    return R, r
ok_o = True
for _ in range(100):
    z = rng.normal(size=3) + 1j*rng.normal(size=3)
    R, r = to_axis(z)
    ok_o &= np.allclose(R @ R.T, np.eye(3)) and np.isclose(np.linalg.det(R), 1) and np.allclose(R @ z, [r, 0, 0])
print("   R in SO(3,C) und R z = (sqrt s, 0, 0):", bool(ok_o))

print("(4) Symmetrische Triole")
w = np.exp(2j*np.pi/3); T = np.array([1, w, w*w])
print("   sum z =", np.round(np.sum(T), 12), " sum z^2 =", np.round(np.sum(T**2), 12), " Spinor:", np.round(psi_of(T), 4))
