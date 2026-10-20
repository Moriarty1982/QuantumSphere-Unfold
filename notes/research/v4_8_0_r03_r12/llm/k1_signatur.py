"""Signatur- und Lorentzanalyse des Biquaternion-Kerns q = it*1 + z1 e1 + z2 e2 + z3 e3 (Companion v4.8.0, def:biquaternion)."""
import sympy as sp
import numpy as np

I = sp.I

# --- Biquaternionen als 4-Tupel (a0, a1, a2, a3) mit komplexen Koeffizienten, e1 e2 = e3 ---
def qmul(p, q):
    a0, a1, a2, a3 = p
    b0, b1, b2, b3 = q
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)

def qbar(q):            # Quaternionenkonjugation (komplexe Koeffizienten bleiben)
    return (q[0], -q[1], -q[2], -q[3])

def cconj(q):           # komplexe Konjugation der Koeffizienten
    return tuple(sp.conjugate(c) for c in q)

def dagger(q):          # beide Konjugationen
    return qbar(cconj(q))

t = sp.symbols('t', real=True)
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
z = [x[k] + I*y[k] for k in range(3)]
q = (I*t, z[0], z[1], z[2])

print("== 1. Norm des Companion: |q|^2 = -t^2 + sum |z_k|^2 ==")
comp = -t**2 + sum(sp.expand(zk*sp.conjugate(zk)) for zk in z)
H = sp.hessian(comp, (t,)+x+y)/2
ev = H.eigenvals()
print("  Form:", sp.simplify(comp))
print("  Eigenwerte:", ev, "-> Signatur (neg,pos) =",
      (sum(m for e,m in ev.items() if e < 0), sum(m for e,m in ev.items() if e > 0)))

print("\n== 2. Natuerliche Norm N(q) = q * qbar (komplex-bilinear) ==")
N = sp.expand(qmul(q, qbar(q))[0])
print("  N(q) =", N)
print("  = -t^2 + sum z_k^2 :", sp.simplify(N - (-t**2 + sum(zk**2 for zk in z))) == 0)
print("  Vektorteile von q*qbar verschwinden:", all(sp.simplify(c) == 0 for c in qmul(q, qbar(q))[1:]))
ReN = sp.re(N); ImN = sp.im(N)
print("  Re N =", sp.simplify(ReN), "   Im N =", sp.simplify(ImN))

print("\n== 3. Lesart A: reeller Schnitt z_k reell (q^dagger = -q) ==")
qA = (I*t, x[0], x[1], x[2])
print("  q^dagger = -q:", all(sp.simplify(a + b) == 0 for a, b in zip(dagger(qA), qA)))
print("  N(q_A) =", sp.expand(qmul(qA, qbar(qA))[0]), "-> Minkowski (1,3)")

rng = np.random.default_rng(1)
def num(q): return np.array([complex(sp.N(c)) for c in q])
def nmul(p, q):
    a0,a1,a2,a3 = p; b0,b1,b2,b3 = q
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
def nbar(q): return np.array([q[0], -q[1], -q[2], -q[3]])
def ndag(q): return nbar(np.conj(q))
def nN(q): return nmul(q, nbar(q))[0]
def unit_biquat():
    u = rng.normal(size=4) + 1j*rng.normal(size=4)
    return u/np.sqrt(nN(u))            # N(u) = 1  (Gruppe ~ SL(2,C))

vA = np.array([1j*0.7, 0.3, -1.1, 0.5])
u = unit_biquat()
wA = nmul(nmul(u, vA), ndag(u))
print("  Wirkung q -> u q u^dagger, N(u)=1:")
print("    N vorher/nachher:", np.round(nN(vA), 12), np.round(nN(wA), 12))
print("    bleibt im Schnitt (w^dagger = -w):", np.allclose(ndag(wA), -wA))
print("    zeitliche Komponente aendert sich (echter Boost):", np.round(vA[0], 4), "->", np.round(wA[0], 4))

print("\n== 4. Companion-Wirkung q -> u q u^-1 mit reellem u in H^x ==")
ur = rng.normal(size=4).astype(complex); ur = ur/np.sqrt(nN(ur))
wR = nmul(nmul(ur, vA), nbar(ur))      # u^-1 = ubar fuer N(u)=1
print("  Skalarteil (Zeit) unveraendert:", np.allclose(wR[0], vA[0]), "-> nur Drehungen SO(3)")

print("\n== 5. Lesart B: komplexes z in C^3, u q u^-1 mit komplexem Einheits-u ==")
vB = np.array([1j*0.7, 0.3+0.2j, -1.1+0.9j, 0.5-0.4j])
u = unit_biquat()
wB = nmul(nmul(u, vB), nbar(u))
sumz2 = lambda v: np.sum(v[1:]**2)
abs2 = lambda v: np.sum(np.abs(v[1:])**2)
print("  Skalarteil invariant:", np.allclose(wB[0], vB[0]))
print("  sum z^2 invariant (SO(3,C) ~ Lorentz):", np.round(sumz2(vB), 10), np.round(sumz2(wB), 10))
print("  Companion-Norm sum|z|^2 invariant?   :", np.round(abs2(vB), 6), np.round(abs2(wB), 6))

print("\n== 6. Triolen-Lemma: sum z = 0 und sum z^2 = 0 ==")
w = sp.Rational(-1, 2) + sp.sqrt(3)/2*I
c = sp.symbols('c')
tri = [c, c*w, c*w**2]
print("  symmetrische Triole c(1,w,w^2): sum z =", sp.simplify(sum(tri)), ", sum z^2 =", sp.simplify(sum(v**2 for v in tri)))
Z1, Z2, Z3, lam = sp.symbols('Z1 Z2 Z3 lam')
e1 = Z1+Z2+Z3; e2 = Z1*Z2+Z1*Z3+Z2*Z3; e3 = Z1*Z2*Z3
p2 = Z1**2+Z2**2+Z3**2
print("  Identitaet p2 = e1^2 - 2 e2:", sp.expand(p2 - (e1**2 - 2*e2)) == 0)
print("  => aus e1 = 0, p2 = 0 folgt e2 = 0; die z_k sind Nullstellen von lam^3 - e3,")
print("     also die drei Kubikwurzeln von e3: z = c(1, w, w^2) bis auf Reihenfolge.")
print("  Gegenprobe nicht-symmetrisch (1,-1,0): sum z^2 =", 1+1+0)

print("\n== 7. Physikalische Gegenstueck-Pruefung (Riemann-Silberstein F = E + iB) ==")
print("  sum z^2 = |x|^2-|y|^2 + 2i x.y  <->  E^2-B^2 + 2i E.B  (die beiden Feldinvarianten)")
E = np.array([0.3, -1.1, 0.5]); B = np.array([0.9, 0.2, -0.4])
F = E + 1j*B
print("  numerisch:", np.round(np.sum(F**2), 10), " vs ", np.round(E@E - B@B + 2j*(E@B), 10))
