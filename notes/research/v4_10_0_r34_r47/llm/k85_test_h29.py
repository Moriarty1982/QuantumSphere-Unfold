"""k85: Test der Vorab-Notiz H29 (Commit 85d065a): lineare und antilineare Verbinder zwischen den Chiralitaetshaelften
(farb- und Lorentz-vertraeglich), ihre Quantenzahlen, eichinvariante Verbinder; Massen und Mischung ueber die Triality-Plaetze."""
import numpy as np, os, sys
from collections import Counter
from fractions import Fraction
from scipy.linalg import null_space, orth
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L8 = [np.array([omul(E[a], E[j]) for j in range(8)]).T for a in range(8)]
R8 = [np.array([omul(E[j], E[a]) for j in range(8)]).T for a in range(8)]
Q8 = 0.5*np.eye(8) - (1j/6)*L8[7] - (1j/3)*R8[7]
def hmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
E4 = np.eye(4)
Lh = [np.array([hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
Rh = [np.array([hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
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
su3 = [sum(S[k, c]*Ds[k] for k in range(len(Ds))) for c in range(S.shape[1])]
K = np.kron; I4, I8, I32 = np.eye(4), np.eye(8), np.eye(32)
Tw = [-(0.5j)*K(Rh[a], I8) for a in (1, 2, 3)]
Q = K(I4, Q8); C = 0.5*(I32 + 1j*K(I4, L8[7])); N = I32 - C
Tp = [C@t for t in Tw]
Y2 = Q - 0.5*I32 + N@Tw[2]
Qem = Tw[2] + Q - 0.5*I32
fr = lambda x: Fraction(float(np.real(x))).limit_denominator(12)

# H29a: Kommutant von Farbe und Linkswirkung von H (zeilenweise vec: AX -> (A (x) I) x, XA -> (I (x) A^T) x)
cons = [K(I4, s) for s in su3] + [K(Lh[a], I8) for a in (1, 2, 3)]
Mc = np.vstack([np.kron(A, I32) - np.kron(I32, A.T) for A in cons])
Bv = null_space(Mc, rcond=1e-10)
basis = [Bv[:, c].reshape(32, 32) for c in range(Bv.shape[1])]
ok_a = len(basis) == 24
print(f"H29a: Verbinder-Raum (vertauscht mit Farbe und L_q): Dimension {len(basis)} (fuer X linear wie fuer Phi = X T) "
      f"-> {'bestaetigt' if ok_a else 'widerlegt'}")

def block(f):
    V = orth(np.column_stack([f(X).ravel() for X in basis]), rcond=1e-9)
    return [V[:, c].reshape(32, 32) for c in range(V.shape[1])]
def op_matrix(B, act):
    Vb = np.column_stack([X.ravel() for X in B])
    return np.linalg.lstsq(Vb, np.column_stack([act(X).ravel() for X in B]), rcond=None)[0]
def decompose(B, anti):
    if not B: return Counter()
    if anti: ad = lambda G: (lambda X: G@X + X@G.conj())
    else: ad = lambda G: (lambda X: G@X - X@G)
    A_T = [op_matrix(B, ad(t)) for t in Tp]
    cas = sum(a@a for a in A_T)
    AY = op_matrix(B, ad(Y2)); AQ = op_matrix(B, ad(Qem))
    rnd = cas + np.pi*AY + np.e*AQ
    w, V = np.linalg.eig(rnd)
    out = Counter()
    for c in range(V.shape[1]):
        v = V[:, c]
        cv = (v.conj()@cas@v)/(v.conj()@v); yv = (v.conj()@AY@v)/(v.conj()@v); qv = (v.conj()@AQ@v)/(v.conj()@v)
        out[(str(fr(cv)), str(fr(yv)), str(fr(qv)))] += 1
    return out

# Bloecke: antilinear Phi = X T: Bild <- Kern  <=>  X = C X C;  Kern <- Kern <=> X = N X C
#          linear X:            Bild <- Kern  <=>  X = C X N
anti_ik = block(lambda X: C@X@C); anti_kk = block(lambda X: N@X@C)
lin_ik = block(lambda X: C@X@N)
w8, V8 = np.linalg.eigh(Q8)
Pq = {q: K(I4, V8[:, abs(w8 - q) < 1e-9]@V8[:, abs(w8 - q) < 1e-9].conj().T) for q in (0, 1/3, 2/3, 1)}
def sectors(B, anti):
    # Lepton-Teil: Abbildungen, die Singulett-Sektoren verbinden; Quark-Teil: Triplett-Sektoren
    lep = sum(np.linalg.norm((Pq[0] + Pq[1])@X@(Pq[0] + Pq[1]))**2 for X in B)
    qua = sum(np.linalg.norm((Pq[1/3] + Pq[2/3])@X@(Pq[1/3] + Pq[2/3]))**2 for X in B)
    dl = np.linalg.matrix_rank(np.column_stack([((Pq[0] + Pq[1])@X@(Pq[0] + Pq[1])).ravel() for X in B]), 1e-8) if B else 0
    dq = np.linalg.matrix_rank(np.column_stack([((Pq[1/3] + Pq[2/3])@X@(Pq[1/3] + Pq[2/3])).ravel() for X in B]), 1e-8) if B else 0
    return dl, dq
dec_b = decompose(anti_ik, True)
dl_b, dq_b = sectors(anti_ik, True)
ok_b = (len(anti_ik) == 8 and dl_b == 4 and dq_b == 4 and
        dict(dec_b) == {("3/4", "1/2", "1"): 2, ("3/4", "1/2", "0"): 2, ("3/4", "-1/2", "0"): 2, ("3/4", "-1/2", "-1"): 2})
print(f"\nH29b: antilinear Bild <- Kern: Dimension {len(anti_ik)} (Lepton {dl_b}, Quark {dq_b}); (Casimir, Y/2, Q_em): {dict(dec_b)}"
      f" -> {'bestaetigt' if ok_b else 'widerlegt'}")

dec_c = decompose(lin_ik, False)
dl_c, dq_c = sectors(lin_ik, False)
ys = {k[1] for k in dec_c}
ok_c = dq_c == 0 and dl_c > 0 and ("-3/2" in ys or "3/2" in ys)
print(f"\nH29c: linear Bild <- Kern: Dimension {len(lin_ik)} (Lepton {dl_c}, Quark {dq_c}); (Casimir, Y/2, Q_em): {dict(dec_c)}"
      f" -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H29d: eichinvariante antilineare Verbinder
def invariant(B):
    if not B: return []
    ad = lambda G: (lambda X: G@X + X@G.conj())
    Ms = [op_matrix(B, ad(G)) for G in Tp + [Y2]]
    Nn = null_space(np.vstack(Ms), rcond=1e-9)
    return [sum(Nn[k, c]*B[k] for k in range(len(B))) for c in range(Nn.shape[1])]
inv_ik = invariant(anti_ik); inv_kk = invariant(anti_kk)
ker_states = null_space(np.vstack([C, Qem]), rcond=1e-10)     # nu^c: Kern von C mit Q_em = 0
Pnu = ker_states@ker_states.conj().T
on_nu = max((abs(X@(N - Pnu).conj()).max() for X in inv_kk), default=0)   # Phi v = X conj(v): verschwindet ausserhalb nu^c
ok_d = len(inv_ik) == 0 and len(inv_kk) > 0 and on_nu < 1e-8
print(f"\nH29d: eichinvariante antilineare Verbinder: Bild <- Kern {len(inv_ik)}, Kern <- Kern {len(inv_kk)};"
      f" diese wirken nur auf nu^c (Rest {on_nu:.0e}) -> {'bestaetigt' if ok_d else 'widerlegt'}")

# H29e
rng = np.random.default_rng(85)
P = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex); R = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
w3 = np.exp(2j*np.pi/3)
def herm_circ(a, b): return a*np.eye(3) + b*P + np.conj(b)*P.conj().T
i_ok = ii_ok = iii_ok = koide_ok = True
for _ in range(200):
    a = rng.normal(); b = rng.normal() + 1j*rng.normal()
    Ms3 = herm_circ(a, b.real)                                   # S3: b = c reell
    assert abs(R@Ms3@R - Ms3).max() < TOL
    ev = np.sort(np.linalg.eigvalsh(Ms3)); i_ok &= min(abs(np.diff(ev))) < 1e-9
    Mz = herm_circ(a, b); ev = np.sort(np.linalg.eigvalsh(Mz))
    th = np.angle(b); br = np.sort([a + 2*abs(b)*np.cos(th + 2*np.pi*k/3) for k in range(3)])
    ii_ok &= abs(ev - br).max() < 1e-9 and min(abs(np.diff(ev))) > 1e-9
    Mu = herm_circ(rng.normal(), rng.normal() + 1j*rng.normal()); Md = herm_circ(rng.normal(), rng.normal() + 1j*rng.normal())
    Uu = np.linalg.eigh(Mu)[1]; Ud = np.linalg.eigh(Md)[1]
    Vm = abs(Uu.conj().T@Ud)
    iii_ok &= abs(np.sort(Vm.ravel()) - np.array([0]*6 + [1]*3)).max() < 1e-8
    a0 = abs(rng.normal()) + 1; bk = a0/np.sqrt(2)*np.exp(1j*rng.uniform(0, 2*np.pi))
    lam = np.linalg.eigvalsh(herm_circ(a0, bk)); Kk = (lam**2).sum()/(lam.sum())**2
    koide_ok &= abs(Kk - 2/3) < 1e-9
ok_e = i_ok and ii_ok and iii_ok and koide_ok
print(f"\nH29e: (i) S3-symmetrisch: entartetes Paar {i_ok}; (ii) Z3: drei verschiedene, Brannen-Form {ii_ok};"
      f" Koide 2/3 bei |b| = a/sqrt2: {koide_ok}; (iii) up und down zirkulant: |V| Permutation {iii_ok}"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'}")
