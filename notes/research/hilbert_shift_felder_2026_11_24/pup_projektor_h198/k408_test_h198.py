"""k408 (Test H198): Ist der Up-Typ-Projektor P_up = 3(Q0-1/3) die chirale Projektion der Ladungs-U(1)?
  a  Operatoridentitaet P_up = 1/2 (1 + i L_U) auf dem Farbblock (L_U = Linksmult. mit U=e7)
     + Projektor-Eigenschaften, Zuordnung zu Ladung 2/3 (Up).
  b  Konsequenz: ein chiraler (holomorpher) l_k^2-Term koppelt nur an Up -> b_down=0 (= D=B),
     waehrend ladungsblind D=0 und die J-Form (Q0-1/2) B=0 gibt.
Aufruf: python k408_test_h198.py > k408_out.txt
"""
import numpy as np
# ---- Oktonion-Algebra und Farbblock-Operatoren (wie k389) ----
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
LU = np.einsum('i,ijk->kj', e[7], C)[1:7, 1:7]          # L_U auf den 6 Farbrichtungen (Komp. 1..6)
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])       # Multiplikation mit i auf (Re,Im)
Ii = np.kron(J2, np.eye(18))                             # "i" auf dem 36-dim Farbblock (2x3x6)
LUc = np.kron(I2, np.kron(np.eye(3), LU))                # L_U auf dem Farbblock
Qc = 0.5 * np.eye(36) + Ii @ LUc / 6                     # Q0 = 1/2 + (i/6) L_U
iLU = Ii @ LUc                                           # i L_U (reelle 36x36-Darstellung)

print("=" * 72)
print("H198a  Operatoridentitaet und Projektor-Eigenschaften")
print("=" * 72)
Pup = 3 * (Qc - np.eye(36) / 3)                          # P_up = 3(Q0 - 1/3)
Pup_chiral = 0.5 * (np.eye(36) + iLU)                    # 1/2 (1 + i L_U)
print(f"  || P_up  -  1/2(1 + i L_U) ||_max            = {np.abs(Pup - Pup_chiral).max():.2e}")
print(f"  || (i L_U)^2  -  1 ||_max  (Chiralitaet +-1) = {np.abs(iLU @ iLU - np.eye(36)).max():.2e}")
print(f"  || P_up^2 - P_up ||_max   (Projektor)        = {np.abs(Pup @ Pup - Pup).max():.2e}")
Pdn = 0.5 * (np.eye(36) - iLU)
print(f"  || P_up + P_down - 1 ||_max                  = {np.abs(Pup + Pdn - np.eye(36)).max():.2e}")
print(f"  || P_up P_down ||_max                        = {np.abs(Pup @ Pdn).max():.2e}")
# Zuordnung: P_up projiziert auf Ladung 2/3
wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2)
up_space = Vq[:, wq > 0.5]; dn_space = Vq[:, wq < 0.5]
print(f"  Q0-Eigenwerte: {sorted(set(np.round(wq,6)))}  (1/3 = Down, 2/3 = Up)")
print(f"  P_up auf Up-Raum   (soll 1): {np.round(np.diag(up_space.T @ Pup @ up_space).mean(),6)}")
print(f"  P_up auf Down-Raum (soll 0): {np.round(np.abs(dn_space.T @ Pup @ dn_space).max(),6)}")
rank_up = int(np.round(np.trace(Pup)))
print(f"  Spur P_up = {np.trace(Pup):.4f} (Dim des Up-Raums = {rank_up}); +i-Eigenraum von L_U.")
print("  -> P_up ist der Projektor auf eine CHIRALITAET der Ladungs-U(1): P_up = 1/2(1 + i L_U).")

print("\n" + "=" * 72)
print("H198b  Konsequenz: wie koppelt das l_k^2-Glied je nach Ladungsstruktur?")
print("=" * 72)
# Der l_k^2-Koeffizient ist ein Operator O im Ladungsraum; auf Up (iL_U=+1), Down (iL_U=-1):
def split(O, name):
    up = up_space.T @ O @ up_space; dn = dn_space.T @ O @ dn_space
    cu = np.diag(up).real.mean(); cd = np.diag(dn).real.mean()
    even = (cu + cd) / 2; odd = (cu - cd) / 2
    print(f"  {name:32s}: Up={cu:+.4f}  Down={cd:+.4f}  (gerade B={even:+.4f}, ungerade D={odd:+.4f}, D/B={odd/even if abs(even)>1e-9 else float('inf'):+.3f})")
    return even, odd
print("  Ein l_k^2-Term mit Operator O gibt b_up = <O>_up, b_down = <O>_down:")
split(np.eye(36), "O = 1        (ladungsblind, F4)")
split(iLU / 1.0, "O = i L_U    (J-Form Q0-1/2)")
split(Pup, "O = P_up     (chiral, 1/2(1+iL_U))")
print("\n  Lesart:")
print("  - ladungsblind (F4-invariant): Up=Down -> D=0 (kein Up/Down-Unterschied).")
print("  - J-Form (Q0-1/2 ~ i L_U): Up=-Down -> rein ungerade, B=0 (antisymmetrisch).")
print("  - chiral (P_up): Up!=0, Down=0 -> b_down=0, also D=B. GENAU 'Down linear'.")
print("  => D=B ist aequivalent dazu, dass das l_k^2-Glied HOLOMORPH (chiral) unter der")
print("     Ladungs-U(1) ist: es benutzt nur die +Chiralitaet. P_up ist deren Projektor.")
print("     Das identifiziert P_up mit einem bekannten Objekt (Chiralitaet der Ladung),")
print("     erzwingt die Chiralitaet aber nicht (die U(1) ist nach H178 nicht gefordert).")
