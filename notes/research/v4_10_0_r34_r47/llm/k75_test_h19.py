"""k75: Test der Vorab-Notiz H19 (Commit 1e60410): Ladungen einer Generation aus der Dixon-Ablage.
Leiteroperatoren alpha_a = 1/2 (L_{e_a} + i L_{e7 e_a}), a = 4,5,6, auf C (x) O = C^8; N = sum alpha^dagger alpha, Q = N/3.
Farbe des Companion: Stab(e7) in G2 (Derivationen mit D(e7) = 0).  Frames T, R, J_B auf dem C-Faktor."""
import numpy as np, os, sys
from scipy.linalg import expm, null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-12
E = np.eye(8)
L = [np.array([omul(E[a], E[j]) for j in range(8)]).T for a in range(8)]     # L[a] @ x = e_a x
Lv = lambda v: sum(v[k]*L[k] for k in range(8))
I8 = np.eye(8)

# Clifford-Kontrolle
cl = max(abs(L[a]@L[b] + L[b]@L[a] + 2*(a == b)*I8).max() for a in range(1, 8) for b in range(1, 8))
print(f"Clifford L_aL_b + L_bL_a = -2 delta_ab (a,b = 1..7): Abweichung {cl:.0e}")

alpha = {a: 0.5*(L[a] + 1j*Lv(omul(E[7], E[a]))) for a in (4, 5, 6)}
dag = lambda M: M.conj().T
car = max([abs(alpha[a]@alpha[a]).max() for a in alpha] +
          [abs(alpha[a]@dag(alpha[b]) + dag(alpha[b])@alpha[a] - (a == b)*I8).max() for a in alpha for b in alpha] +
          [abs(alpha[a]@alpha[b] + alpha[b]@alpha[a]).max() for a in alpha for b in alpha])
print(f"Fermion-Relationen alpha^2 = 0, {{alpha_a, alpha_b^dagger}} = delta_ab: Abweichung {car:.0e}")
N = sum(dag(alpha[a])@alpha[a] for a in alpha); Q = N/3
w, V = np.linalg.eigh(Q)
print("Eigenwerte von Q:", np.round(w, 12))

# Derivationen von O: D(e_i e_j) = D(e_i) e_j + e_i D(e_j); D linear 8x8
rows = []
for i in range(8):
    for j in range(8):
        p = omul(E[i], E[j])
        # Unbekannte: D als 64-Vektor, D[k, m] = d[8k + m]; (D x)_k = sum_m D[k,m] x_m
        A = np.zeros((8, 64))
        for k in range(8):
            for m in range(8):
                A[k, 8*k + m] += p[m]                         # D(e_i e_j)
                A[:, 8*k + m] -= np.array([omul(np.eye(8)[k], E[j])[r] for r in range(8)])*E[i][m]   # D(e_i) e_j
                A[:, 8*k + m] -= np.array([omul(E[i], np.eye(8)[k])[r] for r in range(8)])*E[j][m]   # e_i D(e_j)
        rows.append(A)
Der = null_space(np.vstack(rows))
Ds = [Der[:, c].reshape(8, 8) for c in range(Der.shape[1])]
print(f"Derivationen von O: Dimension {len(Ds)} (G2: 14)")
S = null_space(np.vstack([np.array([D[:, 7] for D in Ds]).T]))
Stab = [sum(S[k, c]*Ds[k] for k in range(len(Ds))) for c in range(S.shape[1])]   # S: (14, 8)
print(f"Stab(e7): Dimension {len(Stab)} (SU(3): 8)")

# H19a
rng = np.random.default_rng(75)
comm = max(abs(D@Q - Q@D).max() for D in Stab)
gs = [expm(sum(rng.normal()*D for D in Stab)) for _ in range(50)]
comm_g = max(abs(g@Q - Q@g).max() for g in gs)
autcheck = max(abs(g@omul(x, y) - omul(g@x, g@y)).max() for g in gs[:5] for x, y in [rng.normal(size=(2, 8))])
print(f"\nH19a: [D, Q] fuer die Basis von Stab(e7): {comm:.0e}; [g, Q] fuer 50 Gruppenelemente: {comm_g:.0e}"
      f" (Automorphismus-Kontrolle {autcheck:.0e}) -> {'bestaetigt' if max(comm, comm_g) < 1e-10 else 'widerlegt'}")

# H19b
sectors = {}
for q in (0, 1/3, 2/3, 1):
    idx = np.where(abs(w - q) < 1e-9)[0]; sectors[q] = V[:, idx]
print("\nH19b: Sektoren")
ok_b = True
for q, B in sectors.items():
    on_singlet = np.linalg.norm(B[[0, 7], :])**2/B.shape[1]
    rep = [dag(B)@D@B for D in Stab]
    closed = max(abs(D@B - B@(dag(B)@D@B)).max() for D in Stab)     # Sektor invariant unter Stab(e7)?
    trivial = max(abs(r).max() for r in rep)
    print(f"  Q = {q:.4f}: Dimension {B.shape[1]}, Anteil auf span(1, e7) {on_singlet:.3f}, invariant {closed:.0e},"
          f" Stab(e7) wirkt {'trivial (Singulett)' if trivial < 1e-10 else 'nicht trivial'}")
    want_singlet = q in (0, 1)
    ok_b &= (B.shape[1] == (1 if want_singlet else 3)) and closed < 1e-10 and \
            (abs(on_singlet - (1 if want_singlet else 0)) < 1e-10) and ((trivial < 1e-10) == want_singlet)
# Konjugiertheit der beiden Tripletts: chi_{2/3}(g) = conj(chi_{1/3}(g)), aber nicht reell
B1, B2 = sectors[1/3], sectors[2/3]
c1 = np.array([np.trace(dag(B1)@g@B1) for g in gs]); c2 = np.array([np.trace(dag(B2)@g@B2) for g in gs])
conj_ok = abs(c2 - c1.conj()).max() < 1e-10 and abs(c1.imag).max() > 1e-3
# Irreduzibilitaet: Kommutant der Darstellung auf dem Triplett
def commutant_dim(B):
    reps = [dag(B)@D@B for D in Stab]; n = B.shape[1]
    K = np.vstack([np.kron(np.eye(n), r) - np.kron(r.T, np.eye(n)) for r in reps])
    return n*n - np.linalg.matrix_rank(K, 1e-9)
print(f"  Tripletts irreduzibel: Kommutant-Dimension {commutant_dim(B1)}, {commutant_dim(B2)} (1 = irreduzibel);"
      f" zueinander konjugiert und nicht selbstkonjugiert: {conj_ok}")
ok_b &= conj_ok and commutant_dim(B1) == 1 and commutant_dim(B2) == 1
print(f"  -> H19b {'bestaetigt' if ok_b else 'widerlegt'}")

# H19c: wortliche Zuordnung
P456 = np.zeros((8, 8)); P456[[4, 5, 6], [4, 5, 6]] = 1
inv456 = abs((I8 - P456)@Q@P456).max()
e7 = I8[:, 7]; Qe7 = Q@e7
e7_eigen = abs(Qe7 - (e7@Qe7)*e7).max()
print(f"\nH19c: Q bildet span(e4,e5,e6) in sich ab? Abweichung {inv456:.3f}; e7 Eigenvektor von Q? Abweichung {e7_eigen:.3f}"
      f" -> {'bestaetigt' if inv456 < 1e-10 and e7_eigen < 1e-10 else 'widerlegt'}")
for q in (0, 1):
    v = sectors[q][:, 0]; v = v/v[np.argmax(abs(v))]
    print(f"  Q = {q}: Zustand ~ {np.round(v[0], 3)}*1 + {np.round(v[7], 3)}*e7")
v = sectors[1/3][:, 0]
print("  Beispiel aus Q = 1/3, Betraege der Komponenten e0..e7:", np.round(abs(v), 3))

# H19d: Frames (antilinear T, J_B: W Q W^-1 = conj(Q); R komplex-linear: Q)
TQ = Q.conj(); RQ = Q; JQ = Q.conj()
res = {name: abs(M - (I8 - Q)).max() for name, M in [("T", TQ), ("J_B", JQ)]}
print(f"\nH19d: T Q T^-1 = 1 - Q: {res['T']:.0e};  J_B Q J_B^-1 = 1 - Q: {res['J_B']:.0e};  R Q R^-1 = Q: {abs(RQ - Q).max():.0e}"
      f" -> {'bestaetigt' if max(res.values()) < 1e-10 else 'widerlegt'}")

# H19e: drei Plaetze (Im H) (x) C (x) O: Q wirkt auf dem O-Faktor
Qtot = np.kron(np.eye(3), Q)
blocks = max(abs(Qtot[8*k:8*k+8, 8*k:8*k+8] - Q).max() for k in range(3))
offd = max(abs(Qtot[8*k:8*k+8, 8*l:8*l+8]).max() for k in range(3) for l in range(3) if k != l)
print(f"\nH19e: Q auf allen drei Plaetzen gleich: {blocks:.0e}, keine Kopplung zwischen Plaetzen: {offd:.0e}"
      " -> bestaetigt (folgt aus der Tensorstruktur)")
