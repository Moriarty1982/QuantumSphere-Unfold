"""k80: Test der Vorab-Notiz H24 (Commit 8c89481): Generationenketten verschiedener Laenge unter Hilbert-Shift-Zoom
(Schritt 2^j) und gemischten Masken (Lesarten Sigma: Schritt k = sum 2^j; Vee: erzeugte Untergruppe)."""
import itertools, numpy as np
from math import gcd
from functools import reduce

TOL = 1e-9
# Gruppe G = <tau, rho, T, R> auf C (x) O^3 wie k78
I8 = np.eye(8); Cj = np.diag([1] + [-1]*7)
def slot_op(perm, conj):
    S = np.zeros((24, 24))
    for s, src in enumerate(perm):
        S[8*s:8*s + 8, 8*src:8*src + 8] = Cj if conj else I8
    return S
tau = np.kron(np.eye(2), slot_op((1, 2, 0), False)); rho = np.kron(np.eye(2), slot_op((0, 2, 1), True))
Tm = np.kron(np.diag([1., -1.]), np.eye(24)); Rm = np.kron(np.array([[0., -1.], [1., 0.]]), np.eye(24))
key = lambda A: tuple(np.round(A, 6).ravel())
G = {key(np.eye(48)): np.eye(48)}; fr = [np.eye(48)]
while fr:
    nw = []
    for A in fr:
        for g in (tau, rho, Tm, Rm):
            B = g@A
            if key(B) not in G: G[key(B)] = B; nw.append(B)
    fr = nw
Id = np.eye(48)
def order(A):
    P = A.copy()
    for n in range(1, 200):
        if np.allclose(P, Id): return n
        P = A@P
mp = np.linalg.matrix_power
assert len(G) == 48

# H24a
odd_ok = all(all(m//gcd(m, 2**j) == m for j in range(12)) for m in range(1, 65, 2))
tinv = mp(tau, 2)
orient = {j: ("tau" if np.allclose(mp(tau, 2**j), tau) else "tau^-1" if np.allclose(mp(tau, 2**j), tinv) else "?") for j in range(8)}
mirror = np.allclose(rho@tau@rho, tinv)
ok_a = odd_ok and all(orient[j] == ("tau" if j % 2 == 0 else "tau^-1") for j in orient) and mirror
print(f"H24a: ungerade m <= 63: Laenge auf allen Stufen j <= 11 unveraendert: {odd_ok}; tau^(2^j) = {orient};"
      f" tau^-1 = rho tau rho: {mirror} -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H24b
pow2_ok = all(2**a//gcd(2**a, 2**j) == (2**(a - j) if j < a else 1) for a in range(7) for j in range(10))
orders_j = {j: sorted({order(mp(A, 2**j)) for A in G.values()}) for j in range(6)}
Z3 = [Id, tau, tinv]
inZ3 = all(any(np.allclose(mp(A, 2**j), z) for z in Z3) for j in range(2, 6) for A in G.values())
ok_b = pow2_ok and orders_j[0] == [1, 2, 3, 4, 6, 12] and orders_j[1] == [1, 2, 3, 6] and \
       all(orders_j[j] == [1, 3] for j in range(2, 6)) and inZ3
print(f"\nH24b: Zweierketten 2^a: Laenge 2^(a-j) bzw. 1: {pow2_ok}; sichtbare Ordnungen in G je Stufe: {orders_j};"
      f" fuer j >= 2 liegt jedes g^(2^j) in <tau>: {inZ3} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H24c
C = 6
masks = [S for r in range(1, C + 1) for S in itertools.combinations(range(C), r)]
def sig_len(m, S): k = sum(2**j for j in S); return m//gcd(m, k)
def vee_len(m, S): return m//gcd(m, reduce(gcd, [2**j for j in S]))
n_one = sum(1 for S in masks if sig_len(3, S) == 1)
vee3 = {vee_len(3, S) for S in masks}
sig3 = {sig_len(3, S) for S in masks}
ok_c = len(masks) == 63 and n_one == 21 and vee3 == {3} and sig3 == {1, 3} and sig_len(3, (0, 1)) == 1
# Kontrolle an der Gruppe: Lesart Sigma als Matrixpotenz, Lesart Vee als erzeugte Untergruppe
def gen_size(mats):
    H = {key(Id): Id}; f = [Id]
    while f:
        nw = []
        for A in f:
            for g in mats:
                B = g@A
                if key(B) not in H: H[key(B)] = B; nw.append(B)
        f = nw
    return len(H)
chk = all(order(mp(tau, sum(2**j for j in S))) == sig_len(3, S) and
          gen_size([mp(tau, 2**j) for j in S]) == vee_len(3, S) for S in masks)
print(f"\nH24c: {len(masks)} Masken ueber {C} Bits; Lesart Sigma: Laengen {sorted(sig3)}, eine Generation bei {n_one} Masken"
      f" (z. B. S = {{0,1}}, k = 3); Lesart Vee: Laengen {sorted(vee3)}; Kontrolle an tau: {chk}"
      f" -> {'bestaetigt' if ok_c and chk else 'widerlegt'}")

# H24d
def cyc_order(m, steps):                                   # Ordnung der von steps erzeugten Untergruppe von Z_m
    return m//reduce(gcd, [s % m for s in steps] + [m])
ok_d = True
for m in range(1, 65):
    for S in masks:
        k = sum(2**j for j in S)
        ok_d &= cyc_order(m, [k]) == m//gcd(m, k) and cyc_order(m, [2**j for j in S]) == m//gcd(m, 2**min(S))
        odd = m
        while odd % 2 == 0: odd //= 2
        ok_d &= (cyc_order(m, [2**j for j in S]) % odd == 0)
print(f"\nH24d: Formeln fuer alle m <= 64 und 63 Masken, ungerader Anteil unter Lesart Vee erhalten: "
      f"{'bestaetigt' if ok_d else 'widerlegt'}")

# H24e
ok_e = (2 in orders_j[0] and 4 in orders_j[0] and 3 in orders_j[0]) and all(orders_j[j] == [1, 3] for j in range(2, 6))
print(f"\nH24e: Stufe 0 sieht Frames (2, 4) und Generationen (3), ab Stufe 2 nur Generationen (3)"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'}")
