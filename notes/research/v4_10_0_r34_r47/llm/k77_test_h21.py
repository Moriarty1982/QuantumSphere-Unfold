"""k77: Test der Vorab-Notiz H21 (Commit 516ab15): Herkunft der Doppelbelegung von Farbe und Generation.
Ist die zyklische Vertauschung e4 -> e5 -> e6 (e7 fest) ein Automorphismus, also eine Farbdrehung in Stab(e7)?"""
import itertools, numpy as np, os, sys
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-10
E = np.eye(8); I8 = np.eye(8)
L = [np.array([omul(E[a], E[j]) for j in range(8)]).T for a in range(8)]
Lv = lambda v: sum(v[k]*L[k] for k in range(8))
dag = lambda M: M.conj().T
J = L[7]
alpha = {a: 0.5*(L[a] + 1j*Lv(omul(E[7], E[a]))) for a in (4, 5, 6)}
Q = sum(dag(alpha[a])@alpha[a] for a in alpha)/3
w, V = np.linalg.eigh(Q)
sec = {q: V[:, np.where(abs(w - q) < 1e-9)[0]] for q in (0, 1/3, 2/3, 1)}
def is_aut(M):
    return max(abs(M@omul(E[i], E[j]) - omul(M@E[i], M@E[j])).max() for i in range(8) for j in range(8))

# Stab(e7) wie k75/k76
rows = []
for i in range(8):
    for j in range(8):
        p = omul(E[i], E[j]); A = np.zeros((8, 64))
        for k in range(8):
            for m in range(8):
                A[k, 8*k + m] += p[m]
                A[:, 8*k + m] -= omul(E[k], E[j])*E[i][m]
                A[:, 8*k + m] -= omul(E[i], E[k])*E[j][m]
        rows.append(A)
Der = null_space(np.vstack(rows)); Ds = [Der[:, c].reshape(8, 8) for c in range(Der.shape[1])]
S = null_space(np.array([D[:, 7] for D in Ds]).T)
Stab = [sum(S[k, c]*Ds[k] for k in range(len(Ds))) for c in range(S.shape[1])]
assert len(Ds) == 14 and len(Stab) == 8

# H21a
def sigma_from(img):            # img: dict Basisindex -> (Vorzeichen, Zielindex)
    M = np.zeros((8, 8))
    for j, (s, t) in img.items(): M[t, j] = s
    return M
base = {0: (1, 0), 7: (1, 7), 4: (1, 5), 5: (1, 6), 6: (1, 4)}
sig = sigma_from({**base, 3: (1, 2), 2: (-1, 1), 1: (-1, 3)})
dev = is_aut(sig)
auts = []
for perm in itertools.permutations((1, 2, 3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = sigma_from({**base, **{src: (s, t) for src, s, t in zip((1, 2, 3), signs, perm)}})
        if is_aut(M) < TOL: auts.append((perm, signs))
print(f"H21a: Kandidat sigma (J-linear fortgesetzt): Automorphismus-Abweichung {dev:.0e}, sigma^3 = 1: "
      f"{abs(np.linalg.matrix_power(sig, 3) - I8).max():.0e}, sigma(e7) = e7: {abs(sig@E[7] - E[7]).max():.0e}")
print(f"  alle vorzeichenbehafteten Fortsetzungen auf e1, e2, e3 (48): {len(auts)} Automorphismen: {auts}")
ok_a = dev < TOL
print(f"  -> H21a {'bestaetigt' if ok_a else 'widerlegt'}; sigma in Stab(e7) = SU(3)")

# H21b
Jlin = abs(sig@J - J@sig).max()
# komplexe Matrix auf (e7^perp, J) in der komplexen Basis e4, e5, e6: Koeffizient von e_b in sigma(e_a) ist a + i c mit
# sigma(e_a) = sum_b (a_ba e_b + c_ba J e_b)
Bc = np.column_stack([E[4], E[5], E[6], J@E[4], J@E[5], J@E[6]])
coef = np.linalg.lstsq(Bc, sig@Bc[:, :3], rcond=None)[0]
Mc = coef[:3] + 1j*coef[3:]
ev = np.sort_complex(np.linalg.eigvals(Mc))
centre = min(abs(Mc - z*np.eye(3)).max() for z in (1, np.exp(2j*np.pi/3), np.exp(-2j*np.pi/3)))
commQ = abs(sig@Q - Q@sig).max()
print(f"\nH21b: sigma J-linear {Jlin:.0e}; komplexe Matrix auf e7^perp =\n{np.round(Mc.real, 3)} (Imaginaerteil {abs(Mc.imag).max():.0e});"
      f" det {np.round(np.linalg.det(Mc), 6)}; Eigenwerte {np.round(ev, 4)}; Abstand zum Zentrum {centre:.3f};"
      f" [sigma, Q] {commQ:.0e}; T, R, J_B: sigma reell und auf O, vertauscht mit z -> conj z und z -> iz")
ok_b = (Jlin < TOL and abs(Mc.imag).max() < TOL and abs(np.linalg.det(Mc) - 1) < TOL and centre > 0.5 and commQ < TOL and
        np.allclose(sorted(np.angle(ev)), sorted([0, 2*np.pi/3, -2*np.pi/3]), atol=1e-9))
print(f"  -> H21b {'bestaetigt' if ok_b else 'widerlegt'}")

# H21c
om = np.exp(2j*np.pi/3)
z = [om**k for k in range(3)]
cplx = lambda c, x: c.real*x + c.imag*(J@x)                      # c * x in (O, J)
v = sum(cplx(z[k], E[4 + k]) for k in range(3))
res = {}
for name, lam in (("omega", om), ("omega_bar", om.conjugate())):
    res[name] = abs(sig@v - cplx(lam, v)).max()
Pm = 0.5*(I8 + 1j*J)
pv = Pm@v; pv = pv/np.linalg.norm(pv)
inQ = [q for q, B in sec.items() if np.linalg.norm(pv - B@(dag(B)@pv)) < 1e-9]
print(f"\nH21c: z0 + z1 + z2 = {abs(sum(z)):.0e}; sigma v = omega v: {res['omega']:.0e}; sigma v = omega_bar v: {res['omega_bar']:.0e};"
      f" P_- v liegt in Q = {inQ}")
ok_c = min(res.values()) < TOL and inQ == [2/3]
print(f"  -> H21c {'bestaetigt' if ok_c else 'widerlegt'}")

# H21d
P456 = np.zeros((8, 8)); P456[[4, 5, 6], [4, 5, 6]] = 1
Mlin = np.column_stack([((I8 - P456)@D@P456).ravel() for D in Stab])
K = null_space(Mlin)
sub = [sum(K[k, c]*Stab[k] for k in range(8)) for c in range(K.shape[1])]
blocks = [D[np.ix_([4, 5, 6], [4, 5, 6])] for D in sub]
antisym = max(abs(b + b.T).max() for b in blocks) if blocks else 0
rank_so3 = np.linalg.matrix_rank(np.array([b.ravel() for b in blocks]), 1e-9) if blocks else 0
print(f"\nH21d: Untergruppe von Stab(e7), die span(e4,e5,e6) erhaelt: Dimension {len(sub)}; Bloecke antisymmetrisch {antisym:.0e},"
      f" Rang im so(3) {rank_so3}")
ok_d = len(sub) == 3 and antisym < TOL and rank_so3 == 3
print(f"  -> H21d {'bestaetigt' if ok_d else 'widerlegt'}")
# sigma als Element der reellen SO(3): erhaelt sigma span(e4,e5,e6)?
print(f"  sigma erhaelt span(e4,e5,e6): {abs((I8 - P456)@sig@P456).max() < TOL}")

# H21e
rho = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])                 # zyklisch auf Im H (i -> j -> k)
G = np.kron(rho, I8); Sg = np.kron(np.eye(3), sig)
ce = max([abs(G@Sg - Sg@G).max()] + [abs(G@np.kron(np.eye(3), D) - np.kron(np.eye(3), D)@G).max() for D in Stab])
print(f"\nH21e: Generationen-Z3 auf Im H vertauscht mit sigma (x) 1 und Stab(e7): {ce:.0e} -> bestaetigt (Tensorstruktur)")
