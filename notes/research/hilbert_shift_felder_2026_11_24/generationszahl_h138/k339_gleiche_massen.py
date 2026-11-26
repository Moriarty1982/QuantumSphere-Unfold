"""k339 (H156): Verlangt die Algebra gleiche Massenterme mu_A^2 = mu_B^2?

Vorab-Notiz: Vorab_Notiz_H156_Gleiche_Massenterme.md (Commit fdac350).
Aufruf: python -W ignore k339_gleiche_massen.py > k339_out.txt
"""
import itertools
import numpy as np
import sympy as sp

ph, y = sp.symbols("phi y", real=True)
print("=== H156a: Automorphismen lassen N und Re Psi^2 invariant ===")
N = ph**2 + y**2; R2 = ph**2 - y**2
print("   Konjugation in C = {1, U}: (phi, y) -> (phi, -y): dN =", sp.expand(N.subs(y, -y) - N), ", dRe Psi^2 =", sp.expand(R2.subs(y, -y) - R2))
# Oktonionen: e_i e_{i+1} = e_{i+3} (Indizes mod 7, 1..7); zyklischer Shift i -> i+1 ist ein Automorphismus (G2-Element)
trip = [((i % 7) + 1, ((i + 1) % 7) + 1, ((i + 3) % 7) + 1) for i in range(7)]
M = np.zeros((8, 8, 8))
for i in range(8):
    M[0, i, i] = 1; M[i, 0, i] = 1
for i in range(1, 8):
    M[i, i, 0] = -1
for a, b, c in trip:
    for (p, q, r) in [(a, b, c), (b, c, a), (c, a, b)]:
        M[p, q, r] = 1; M[q, p, r] = -1
mul = lambda x, z: np.einsum("i,j,ijk->k", x, z, M)
P = np.zeros((8, 8)); P[0, 0] = 1
for i in range(1, 8):
    P[(i % 7) + 1, i] = 1
rng = np.random.default_rng(1)
err = max(np.max(np.abs(P @ mul(x, z) - mul(P @ x, P @ z))) for x, z in (rng.normal(size=(2, 8)) for _ in range(20)))
print(f"   Oktonionen: zyklischer Shift der Einheiten ist Automorphismus (max. Fehler {err:.1e}); haelt den Realteil fest")
x = rng.normal(size=8); Px = P @ x
print(f"   N vorher/nachher: {x @ x:.12f} / {Px @ Px:.12f}; Re Psi^2 = x0^2 - |Im|^2 vorher/nachher: {x[0]**2 - x[1:] @ x[1:]:.12f} / {Px[0]**2 - Px[1:] @ Px[1:]:.12f}")
print("   -> beide quadratischen Formen sind automorphismeninvariant; mu_A^2 != mu_B^2 ist erlaubt.")
print("   Zerlegung: muA A + muB B = (muA + muB)/2 N + (muA - muB)/2 Re Psi^2:", sp.simplify(sp.Symbol("mA") * ph**2 + sp.Symbol("mB") * y**2 - ((sp.Symbol("mA") + sp.Symbol("mB")) / 2 * N + (sp.Symbol("mA") - sp.Symbol("mB")) / 2 * R2)) == 0)

print("\n=== H156b: Invarianten in der Ebene {1, U} ===")
LU = sp.Matrix([[0, -1], [1, 0]])      # Psi -> U Psi: phi + yU -> -y + phi U
CJ = sp.Matrix([[1, 0], [0, -1]])      # Konjugation
JJ = sp.Matrix([[0, 1], [1, 0]])       # J: Psi -> U conj(Psi): (phi, y) -> (y, phi)
print("   J = L_U * Konjugation:", JJ == LU * CJ)
def closure(gens):
    G = [sp.eye(2)]; changed = True
    while changed:
        changed = False
        for g in list(G):
            for h in gens:
                n = g * h
                if all(n != q for q in G):
                    G.append(n); changed = True
    return G
groups = {"Z4 = <L_U>": closure([LU]), "Z2 = <J>": closure([JJ]), "D4 = <L_U, Konjugation>": closure([LU, CJ])}
v = sp.Matrix([ph, y])
def invariants(G, deg):
    mons = [ph**a * y**(deg - a) for a in range(deg + 1)]
    avgs = []
    for m in mons:
        tot = sum(m.subs({ph: (g * v)[0], y: (g * v)[1]}, simultaneous=True) for g in G)
        avgs.append(sp.expand(tot / len(G)))
    Mx = sp.Matrix([[sp.Poly(a, ph, y).coeff_monomial(ph**e * y**(deg - e)) for e in range(deg + 1)] for a in avgs])
    basis = []
    for row in Mx.rref()[0].tolist():
        if any(c != 0 for c in row):
            basis.append(sp.expand(sum(c * ph**e * y**(deg - e) for c, e in zip(row, range(deg + 1)))))
    return basis
th = sp.symbols("theta", real=True)
for name, G in groups.items():
    q2 = invariants(G, 2); q4 = invariants(G, 4)
    shift = [b for b in q4 if sp.simplify(sp.diff(b.subs({ph: sp.cos(th), y: sp.sin(th)}), th).subs(th, sp.pi / 4)) != 0]
    print(f"   {name} (Ordnung {len(G)}): quadratisch {q2}; quartisch {q4}; quartische Terme mit d/dtheta != 0 bei pi/4: {shift}")
print("   SO(2) aus exp(aU): einzige Invarianten N, N^2 -> mu_A^2 = mu_B^2 und kappa = 2 lambda (volle Norm, kein Koide-Kondensat, H150)")

print("\n=== H156c: Ist die Tauschlinie im Fluss anziehend? ===")
mA, mB, lA, ka, lB = sp.symbols("mA mB lA ka lB", real=True)
def betas(nB):
    ys = sp.symbols(f"u0:{nB}", real=True); Bf = sum(w**2 for w in ys); Af = ph**2
    Vf = mA * Af + mB * Bf + lA * Af**2 + ka * Af * Bf + lB * Bf**2
    H = sp.hessian(Vf, [ph] + list(ys)); rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    cs = sp.symbols("q0:6"); basis = [1, Af, Bf, Af**2, Af * Bf, Bf**2]
    so = sp.solve(sp.Poly(sp.expand(rhs - sum(c * b for c, b in zip(cs, basis))), ph, *ys).coeffs(), cs, dict=True)[0]
    return [sp.factor(so[c]) for c in cs[1:]]
m, l, k, dm, dl, eps = sp.symbols("m l k dm dl epsilon", real=True)
for nB in (1, 2):
    bt = betas(nB)
    sub = {mA: m + eps * dm / 2, mB: m - eps * dm / 2, lA: l + eps * dl / 2, ka: k, lB: l - eps * dl / 2}
    flow = [-q.subs(sub) for q in bt]    # 16 pi^2 dg/dt ins Infrarote
    d_dm = flow[0] - flow[1]; d_dl = flow[2] - flow[4]; d_m = (flow[0] + flow[1]) / 2; d_l = (flow[2] + flow[4]) / 2
    # relative Abweichungen s = dm/m, r = dl/l
    ds = sp.expand(sp.series((d_dm * m - eps * dm * d_m) / m**2, eps, 0, 2).removeO())
    dr = sp.expand(sp.series((d_dl * l - eps * dl * d_l) / l**2, eps, 0, 2).removeO())
    src = [sp.simplify(ds.subs(eps, 0)), sp.simplify(dr.subs(eps, 0))]
    Jm = sp.Matrix([[sp.diff(ds, eps).diff(dm) * m, sp.diff(ds, eps).diff(dl) * l], [sp.diff(dr, eps).diff(dm) * m, sp.diff(dr, eps).diff(dl) * l]]).applyfunc(sp.simplify)
    print(f"   n_B = {nB}: Quelle (Abweichung, die der Fluss auf der Tauschlinie selbst erzeugt) d(s, r)/dt =", src)
    print(f"      lineare Matrix fuer (s, r): {Jm.tolist()}")
    for L_, kr in itertools.product([0.05, 0.1, 0.2], [-1.0, -0.5, 0.5, 1.0]):
        ev = [complex(e) for e in Jm.subs({l: L_, k: kr * L_, m: -1}).eigenvals()]
        sv = [float(s_.subs({l: L_, k: kr * L_, m: -1})) for s_ in src]
        print(f"      lam = {L_}, k/lam = {kr:+.1f}: Eigenwerte {np.round([e.real for e in ev], 4).tolist()} (negativ = anziehend), Quelle {np.round(sv, 4).tolist()}")

print("\n=== H156d: Ist J eine Symmetrie der Multiplikation? ===")
z1, z2 = sp.symbols("z1 z2")
Jc = lambda z: sp.I * sp.conjugate(z)    # in C mit U = i
print("   J(1) J(1) =", sp.simplify(Jc(1) * Jc(1)), "; J(1 * 1) =", Jc(1), "-> kein Automorphismus")
print("   J(1) J(1) gegen J(conj(1 * 1)) (Antiautomorphismus):", sp.simplify(Jc(1) * Jc(1)), "vs", Jc(1), "-> auch kein Antiautomorphismus")
a_, b_ = sp.symbols("a b", real=True); zz = a_ + sp.I * b_
print("   |J(z)|^2 - |z|^2 =", sp.simplify(sp.expand(Jc(zz) * sp.conjugate(Jc(zz)) - zz * sp.conjugate(zz))), "-> Isometrie der Norm")
print("   J(z w) - J(z) conj(w) =", sp.simplify(Jc(z1 * z2) - Jc(z1) * sp.conjugate(z2)), "-> J ist mit der Multiplikation nur bis auf Konjugation vertraeglich")
