"""k82: Test der Vorab-Notiz H26 (Commit 1876b55): Aufteilung D der Rollen des H-Faktors; Hyperladung Y/2 = Q - 1/2,
T3 = -(i/2) R_k (rechts), Q_em = T3 + Y/2; Frame T als Ladungskonjugation; fehlende schwache Singuletts.
Komplexe Darstellung: der C-Faktor ist der Skalar i; T = komplexe Konjugation (antilinear), R = Multiplikation mit i."""
import numpy as np, os, sys
from collections import Counter
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L8 = [np.array([omul(E[a], E[j]) for j in range(8)]).T for a in range(8)]
R8 = [np.array([omul(E[j], E[a]) for j in range(8)]).T for a in range(8)]
Q = 0.5*np.eye(8) - (1j/6)*L8[7] - (1j/3)*R8[7]
def hmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
E4 = np.eye(4)
Lh = [np.array([hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
Rh = [np.array([hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
# Farbe su(3) = Stab(e7) in G2
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
I4, I8 = np.eye(4), np.eye(8)
K = np.kron
weak = [K(Rh[a], I8) for a in (1, 2, 3)]
T1, T2, T3 = [-(0.5j)*K(Rh[a], I8) for a in (1, 2, 3)]
rot = [K(Lh[a], I8) for a in (1, 2, 3)]
boost = [1j*K(Lh[a], I8) for a in (1, 2, 3)]
col = [K(I4, s) for s in su3]
Qw = K(I4, Q); Y2 = Qw - 0.5*np.eye(32); Qem = T3 + Y2
c = lambda A, B: abs(A@B - B@A).max()
a_ = lambda A, B: abs(A@B + B@A).max()
Tc = lambda A: A.conj()                                   # T A T^-1 fuer antilineares T = Konjugation
Rf = lambda A: A                                          # R = Multiplikation mit i: vertauscht mit allen C-linearen A

# H26a
w_vs = max([c(w, x) for w in weak for x in rot + boost + col + [Qw]])
rot_T = max(abs(Tc(r) - r).max() for r in rot)            # Drehungen reell: vertauschen mit T, J_B
boost_T = max(abs(Tc(b) + b).max() for b in boost)        # Boosts: T b T^-1 = -b
ok_a = w_vs < TOL and rot_T < TOL and boost_T < TOL
print(f"H26a: schwache SU(2) (rechts) vertauscht mit Lorentz, Farbe, Q: {w_vs:.0e}; Lorentz-Drehungen unter T fest: {rot_T:.0e};"
      f" Boosts unter T umgekehrt: {boost_T:.0e}; R vertauscht mit allen C-linearen Abbildungen -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H26b
su2 = max(abs((T1@T2 - T2@T1) - 1j*T3).max(), abs((T2@T3 - T3@T2) - 1j*T1).max(), abs((T3@T1 - T1@T3) - 1j*T2).max())
Tp = T1 + 1j*T2
ladder = abs((T3@Tp - Tp@T3) - Tp).max()
herm = abs(Qem - Qem.conj().T).max()
wq, Vq = np.linalg.eigh(Qw); wt = np.linalg.eigvalsh(T3)
table = {}
for q in (0, 1/3, 2/3, 1):
    Pq = Vq[:, abs(wq - q) < 1e-9]; Pq = Pq@Pq.conj().T
    for t in (0.5, -0.5):
        # gemeinsamer Eigenraum von Qw = q und T3 = t
        Mx = np.vstack([Qw - q*np.eye(32), T3 - t*np.eye(32)])
        Vs = null_space(Mx, rcond=1e-10)
        if Vs.shape[1]:
            e = np.round(np.linalg.eigvalsh(Vs.conj().T@Qem@Vs), 9)
            table[(round(q, 4), t)] = (Vs.shape[1], sorted(set(e)))
want = {(0, 0.5): [0.0], (0, -0.5): [-1.0], (0.6667, 0.5): [0.666666667], (0.6667, -0.5): [-0.333333333],
        (0.3333, 0.5): [0.333333333], (0.3333, -0.5): [-0.666666667], (1, 0.5): [1.0], (1, -0.5): [0.0]}
dims = {k: v[0] for k, v in table.items()}
ok_b = (su2 < TOL and ladder < TOL and herm < TOL and
        all(abs(table[k][1][0] - want[k][0]) < 1e-6 and len(table[k][1]) == 1 for k in want) and
        dims == {(0, 0.5): 2, (0, -0.5): 2, (0.6667, 0.5): 6, (0.6667, -0.5): 6, (0.3333, 0.5): 6, (0.3333, -0.5): 6,
                 (1, 0.5): 2, (1, -0.5): 2})
print(f"\nH26b: su(2)-Relationen {su2:.0e}, Leiter T+ hebt T3 um 1: {ladder:.0e}, Q_em hermitesch {herm:.0e}")
for k, v in sorted(table.items(), key=lambda kv: (kv[0][0], -kv[0][1])):
    print(f"   Q-Sektor {k[0]:.4f}, Y/2 = {k[0] - 0.5:+.4f}, T3 = {k[1]:+.1f}: Dimension {v[0]}, Q_em = {v[1]}")
print(f"  -> H26b {'bestaetigt' if ok_b else 'widerlegt'}")
print("  Spektrum Q_em mit Vielfachheiten:", dict(sorted(Counter(np.round(np.linalg.eigvalsh(Qem), 6)).items())))

# H26c
cQ = abs(Tc(Qem) + Qem).max(); cY = abs(Tc(Y2) + Y2).max()
ok_c = cQ < TOL and cY < TOL
print(f"\nH26c: T Q_em T^-1 = -Q_em: {cQ:.0e}; T (Y/2) T^-1 = -Y/2: {cY:.0e} -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H26d
sing = null_space(np.vstack([T1, T2, T3]), rcond=1e-10).shape[1]
cas = T1@T1 + T2@T2 + T3@T3
ok_d = sing == 0 and abs(cas - 0.75*np.eye(32)).max() < TOL
print(f"\nH26d: schwache Singuletts: {sing}; Casimir T^2 = 3/4 auf allem: {abs(cas - 0.75*np.eye(32)).max():.0e}"
      f" -> {'bestaetigt' if ok_d else 'widerlegt'} (D liefert nur Dubletts)")

# H26e: C (x) H (x) O^3, Generationen-Z3 = tau auf den Plaetzen
P3 = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
I3 = np.eye(3)
tau = K(I4, K(P3, I8))
lift = lambda A4, A8: K(A4, K(I3, A8))
others = [lift(Lh[a], I8) for a in (1, 2, 3)] + [lift(Rh[a], I8) for a in (1, 2, 3)] + [lift(I4, s) for s in su3] + [lift(I4, Q)]
ce = max(c(tau, x) for x in others)
ok_e = ce < TOL
print(f"\nH26e: Generationen-Z3 auf den Plaetzen vertauscht mit L_q, R_q, Farbe und Q: {ce:.0e}"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'}")
