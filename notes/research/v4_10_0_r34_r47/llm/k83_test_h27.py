"""k83: Test der Vorab-Notiz H27 (Commit 614ac3e): Kompensator C_ch = 1/2 (1 + i L_e7) als Chiralitaetsprojektor der
MM-Matrix; wirksame schwache SU(2) T_a' = C_ch T_a, Hyperladung Y/2 = Q - 1/2 + (1 - C_ch) T3, Q_em = T3 + Q - 1/2."""
import numpy as np, os, sys
from collections import Counter
from fractions import Fraction
from scipy.linalg import null_space
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
rot = [K(Lh[a], I8) for a in (1, 2, 3)]; boost = [1j*x for x in rot]
col = [K(I4, s) for s in su3]
Q = K(I4, Q8)
J = 1j*K(I4, L8[7]); C = 0.5*(I32 + J)
Tp = [C@t for t in Tw]
Y2 = Q - 0.5*I32 + (I32 - C)@Tw[2]
Qem = Tw[2] + Q - 0.5*I32
cm = lambda A, B: abs(A@B - B@A).max()

# H27a
herm = abs(C - C.conj().T).max(); idem = abs(C@C - C).max(); Jsq = abs(J@J - I32).max()
comm = max(cm(C, x) for x in col + rot + boost + [K(Rh[a], I8) for a in (1, 2, 3)] + [Q])
wq, Vq = np.linalg.eigh(Q)
P_img = sum((lambda B: B@B.conj().T)(Vq[:, abs(wq - q) < 1e-9]) for q in (0, 2/3))
img_ok = abs(C - P_img).max()
rk = round(np.trace(C).real)
ok_a = max(herm, idem, Jsq, comm, img_ok) < TOL and rk == 16
print(f"H27a: C hermitesch {herm:.0e}, idempotent {idem:.0e}, J^2 = 1 {Jsq:.0e}; vertauscht mit Farbe, Lorentz, R_q, Q: {comm:.0e};"
      f" Bild = Q-Sektoren 0 und 2/3: {img_ok:.0e}, Rang {rk} -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H27b
cas = sum(t@t for t in Tp)
colcas = -sum(x@x for x in col)                   # reelle antisymmetrische Erzeuger: -sum D^2 >= 0
def frac(x): return Fraction(x).limit_denominator(12)
blocks = Counter()
for q in (0, 1/3, 2/3, 1):
    for cw in (0.75, 0.0):
        # Korrektur nach dem Erstlauf: exakte Bruchwerte statt auf 9 Stellen gerundeter Eigenwerte (die Rundung lag ueber der
        # Nullraum-Toleranz und verlor alle nicht-dyadischen Y-Werte; Erstlauf in k83_out_erstlauf.txt)
        for y in sorted({float(frac(v)) for v in np.linalg.eigvalsh(Y2)}):
            V = null_space(np.vstack([Q - q*I32, cas - cw*I32, Y2 - y*I32]), rcond=1e-10)
            if V.shape[1]:
                c3 = np.round(np.linalg.eigvalsh(V.conj().T@colcas@V), 6)
                colour = "1" if abs(c3).max() < 1e-6 else ("3" if abs(q - 2/3) < 1e-6 else "3bar")
                qe = sorted(set(np.round(np.linalg.eigvalsh(V.conj().T@Qem@V), 6)))
                blocks[(colour, "2" if cw else "1", str(frac(y)), tuple(str(frac(v)) for v in qe))] += V.shape[1]
want = {("3", "2", "1/6"): 12, ("1", "2", "-1/2"): 4, ("3bar", "1", "-2/3"): 6, ("3bar", "1", "1/3"): 6,
        ("1", "1", "1"): 2, ("1", "1", "0"): 2}
got = Counter()
for k, v in blocks.items(): got[k[:3]] += v
y_comm = max(cm(Y2, x) for x in Tp + col + rot + boost)
qcheck = abs(Qem - (Tp[2] + Y2)).max()
ok_b = dict(got) == want and y_comm < TOL and qcheck < TOL
print(f"\nH27b: Bloecke (Farbe, SU(2)', Y/2, Q_em) mit komplexer Dimension:")
for k, v in sorted(blocks.items()): print(f"   {k}: {v}")
print(f"  Y/2 vertauscht mit SU(2)', Farbe, Lorentz: {y_comm:.0e}; Q_em = T3' + Y/2: {qcheck:.0e}"
      f" -> {'bestaetigt' if ok_b else 'widerlegt'} (16 Weyl-Zustaende x 2)")

# H27c (ein Lorentz-Index: Spuren durch 2)
tr = lambda A: (np.trace(A).real)/2
P_trip = sum((lambda B: B@B.conj().T)(Vq[:, abs(wq - q) < 1e-9]) for q in (1/3, 2/3))
an = {"Tr Y": tr(Y2), "Tr Y^3": tr(Y2@Y2@Y2), "SU(2)^2 Y": tr(C@Y2), "SU(3)^2 Y": tr(P_trip@Y2)}
ok_c = all(abs(v) < TOL for v in an.values())
print(f"\nH27c: Anomalie-Spuren ueber 16 Zustaende: {dict((k, f'{v:.1e}') for k, v in an.items())}"
      f" -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H27d
ker_triv = max(abs((I32 - C)@t).max() for t in Tp)
on_img = max(abs(C@t@C - t).max() for t in Tp)
Tswap = abs(C.conj() - (I32 - C)).max()
ok_d = ker_triv < TOL and on_img < TOL and Tswap < TOL
print(f"\nH27d: SU(2)' auf dem Kern trivial {ker_triv:.0e}, lebt auf dem Bild {on_img:.0e}; T C T^-1 = 1 - C: {Tswap:.0e}"
      f" -> {'bestaetigt' if ok_d else 'widerlegt'}")

# H27e
lam0, lam1 = 1.0, -1.0
M = lam0*C + lam1*(I32 - C)
spec = null_space(M - lam0*I32); Pspec = spec@spec.conj().T
ok_e = abs(Pspec - C).max() < TOL and cm(M, C) < TOL
print(f"\nH27e: M = l0 C + l1 (1 - C): Spektralprojektor zu l0 = C: {abs(Pspec - C).max():.0e}; [M, C] = {cm(M, C):.0e}"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'} (Kontrolle)")
