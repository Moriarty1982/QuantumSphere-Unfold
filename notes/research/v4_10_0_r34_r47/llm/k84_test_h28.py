"""k84: Test der Vorab-Notiz H28 (Commit 9b8b360): Klassifikation der Chiralitaetsprojektoren C = 1/2 (1 + J), Versatz s aus
Tr Y = 0, Auswahl durch Anomaliefreiheit (exakte Brueche)."""
import itertools, numpy as np, os, sys
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
fr = lambda x: Fraction(float(np.real(x))).limit_denominator(1000)

# H28a: Kommutant von Farbe und Q auf C (x) O
rowsK = [np.kron(I8, s) - np.kron(s.T, I8) for s in su3] + [np.kron(I8, Q8) - np.kron(Q8.T, I8)]
Kc = null_space(np.vstack(rowsK), rcond=1e-10)
wq, Vq = np.linalg.eigh(Q8)
sect = {q: Vq[:, abs(wq - q) < 1e-9] for q in (0, 1/3, 2/3, 1)}
proj = {q: B@B.conj().T for q, B in sect.items()}
span_ok = np.linalg.matrix_rank(np.column_stack([Kc] + [proj[q].T.ravel()[:, None] for q in proj]), 1e-8) == 4
cands = []
for signs in itertools.product((1, -1), repeat=4):
    J8 = sum(sg*proj[q] for sg, q in zip(signs, proj))
    C8 = 0.5*(I8 + J8)
    if round(np.trace(C8).real) == 4:                       # Rang 16 auf C^32 = 4 auf C (x) O
        img = tuple(q for q, sg in zip(proj, signs) if sg == 1)
        dims = [sect[q].shape[1] for q in img]
        if sorted(dims) == [1, 3]:
            cands.append((img, J8))
named = {"iL_e7": 1j*L8[7], "-iL_e7": -1j*L8[7], "iR_e7": 1j*R8[7], "-iR_e7": -1j*R8[7]}
match = {}
for img, J8 in cands:
    nm = [n for n, M in named.items() if abs(M - J8).max() < TOL]
    match[tuple(str(fr(q)) for q in img)] = nm[0] if nm else None
ok_a = Kc.shape[1] == 4 and span_ok and len(cands) == 4 and sorted(match.values()) == sorted(named)
print(f"H28a: Kommutant von Farbe und Q: Dimension {Kc.shape[1]} (= Sektor-Projektoren: {span_ok});"
      f" Projektoren mit Bild Singulett + Triplett: {len(cands)}; Zuordnung Bild -> J: {match}"
      f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H28b, c
Tw = [-(0.5j)*K(Rh[a], I8) for a in (1, 2, 3)]
Q = K(I4, Q8)
P_trip = K(I4, proj[1/3] + proj[2/3])
res = {}
for name, J8 in named.items():
    C = 0.5*(I32 + K(I4, J8))
    Y0 = Q + (I32 - C)@Tw[2]                                # Y/2 ohne Versatz
    trY0 = np.trace(Y0).real/2                              # ein Lorentz-Index: 16 Zustaende
    s_star = -trY0/16
    Y = Y0 + s_star*I32
    tr = lambda A: np.trace(A).real/2
    an = {"TrY": tr(Y), "TrY3": tr(Y@Y@Y), "SU2^2Y": tr(C@Y), "SU3^2Y": tr(P_trip@Y)}
    res[name] = (fr(s_star), {k: fr(v) for k, v in an.items()}, C)
for n, (s, an, _) in res.items():
    print(f"   J = {n:7s}: Tr Y = 0 genau fuer s = {s}; Anomalien bei diesem s: " + ", ".join(f"{k} = {v}" for k, v in an.items()))
ok_b = all(s == Fraction(-1, 2) for s, _, _ in res.values())
free = {n for n, (s, an, _) in res.items() if all(v == 0 for v in an.values())}
ok_c = free == {"iL_e7", "-iL_e7"} and all(an["SU2^2Y"] != 0 and an["TrY3"] != 0 for n, (s, an, _) in res.items() if "R" in n)
print(f"\nH28b: s = -1/2 fuer alle vier: {ok_b} -> {'bestaetigt' if ok_b else 'widerlegt'}")
print(f"H28c: anomaliefrei: {sorted(free)} -> {'bestaetigt' if ok_c else 'widerlegt'}")

# H28d
TJ = abs((1j*L8[7]).conj() + 1j*L8[7]).max()
ok_d = TJ < TOL
print(f"\nH28d: T (iL_e7) T^-1 = -iL_e7: {TJ:.0e} -> {'bestaetigt' if ok_d else 'widerlegt'}")
