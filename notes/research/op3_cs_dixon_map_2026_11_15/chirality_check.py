"""Ergaenzung: Liegt das Bild von Phi (Farbe + Ladung) in einer Chiralitaetshaelfte C = (1 + i L_e7)/2 von C(x)H(x)O?
Und wie viele Spinzustaende traegt der Q_em-Singulettblock je Haelfte?"""
import numpy as np
import search as s
E8 = np.eye(8); E4 = np.eye(4); K = np.kron
L8 = [np.array([s.ho.mul(E8[a], E8[j]) for j in range(8)]).T for a in range(8)]
R8 = [np.array([s.ho.mul(E8[j], E8[a]) for j in range(8)]).T for a in range(8)]
Q8 = 0.5*np.eye(8) - (1j/6)*L8[7] - (1j/3)*R8[7]
Rh = [np.array([s.hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
Qem = -(0.5j)*K(Rh[3], np.eye(8)) + K(E4, Q8) - 0.5*np.eye(32)
C = 0.5*(np.eye(32) + 1j*K(E4, L8[7])); N = np.eye(32) - C
P, SU3, P0, Pc, P3, P3b, Qs = s.fs.setup()
D8 = s.ho.derivations()
c = s.fs.ch.null_space(np.array([d @ E8[7] for d in D8]).T)
su3_8 = [sum(c[k, j]*D8[k] for k in range(14)).real for j in range(c.shape[1])]
base = [(K(np.eye(2), d).astype(complex), K(E4, d).astype(complex)) for d in su3_8] + [(Qs, Qem)]
B0 = s.intertwiners(base)
print("[C, Q_em] = 0:", np.allclose(C @ Qem, Qem @ C))
for name, Pr in (("C (Kompensatorhaelfte)", C), ("N = 1 - C", N)):
    Bh = s.restrict(B0, [(np.eye(16, dtype=complex), Pr)])    # Phi = Pr Phi
    print(f"Bild in {name}: Loesungsraum dim {len(Bh)}, max. Rang {s.max_rank(Bh)} / 16, auf H_n {s.max_rank(Bh, [0, 7, 8, 15])} / 4")
for name, Pr in (("C", C), ("N", N)):
    U = np.linalg.svd(Pr)[0][:, :16]
    w = np.round(np.linalg.eigvalsh(U.conj().T @ Qem @ U), 4)
    vals, cnt = np.unique(w, return_counts=True)
    print(f"Q_em-Spektrum auf {name}: {dict(zip(vals.tolist(), cnt.tolist()))}")
