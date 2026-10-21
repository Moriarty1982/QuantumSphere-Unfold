"""K6: Pruefung der Triolen-Hierarchie (Riemann-Paper Abschn. 4a-4c) mit expliziter Cayley-Dickson-Arithmetik.

Konvention wie im Paper: (p + q l)(r + s l) = (p r - conj(s) q) + (s p + q conj(r)) l.
Pruefungen:
 (1) Sind T1=(e1,e2,e3), T2=(e4,e5,e6), T3=(e3,e4,e7) quaternionische Unteralgebren?
 (2) Alle 7 quaternionischen Linien (Fano-Ebene) in dieser Konvention; welche drei Linien ueberdecken alle 7 Einheiten?
 (3) Ist die e1-Spiegelung R_e1 ein Algebra-Automorphismus von O? Welche Vorzeichenwechsel sind es?
 (4) Sedenionen: ist O2 = (f8,...,f14) eine Oktonionen-Unteralgebra? Nullteiler?
"""
import itertools
import numpy as np

def cd_mult(a, b):
    n = len(a)
    if n == 1:
        return a * b
    h = n // 2
    p, q, r, s = a[:h], a[h:], b[:h], b[h:]
    return np.concatenate([cd_mult(p, r) - cd_mult(conj(s), q), cd_mult(s, p) + cd_mult(q, conj(r))])

def conj(a):
    c = -a.copy(); c[0] = a[0]; return c

def unit(i, n):
    v = np.zeros(n); v[i] = 1.0; return v

def prod_index(i, j, n):
    v = cd_mult(unit(i, n), unit(j, n))
    k = int(np.argmax(np.abs(v)))
    return int(np.sign(v[k])), k

O = 8
e = {a: unit(a, O) for a in range(8)}       # e0 = 1, e1..e3 in H, e4 = l, e5 = e1 l, e6 = e2 l, e7 = e3 l
# Basis-Check: e5 = e1 l usw.
for a, lab in ((5, 1), (6, 2), (7, 3)):
    assert np.allclose(cd_mult(e[lab], e[4]), e[a])

def closed(triple, n):
    s = set(triple)
    for i, j in itertools.permutations(triple, 2):
        sg, k = prod_index(i, j, n)
        if k not in s:
            return False, (i, j, sg, k)
    return True, None

print("(1) Triolen des Papers")
for name, T in (("T1", (1, 2, 3)), ("T2", (4, 5, 6)), ("T3", (3, 4, 7))):
    ok, w = closed(T, O)
    print(f"   {name}={T}: quaternionisch geschlossen = {ok}" + ("" if ok else f"  (e{w[0]}*e{w[1]} = {'+' if w[2]>0 else '-'}e{w[3]})"))

print("(2) Fano-Linien (quaternionische Tripel) in dieser Konvention")
lines = sorted({tuple(sorted(T)) for T in itertools.combinations(range(1, 8), 3) if closed(T, O)[0]})
print("  ", lines)
cover = [c for c in itertools.combinations(lines, 3) if set().union(*c) == set(range(1, 8))]
print("   Drei Linien, die alle 7 Einheiten ueberdecken:", cover)

print("(3) Automorphismen durch Vorzeichenwechsel")
def is_aut(signs):
    for i in range(1, 8):
        for j in range(1, 8):
            sg, k = prod_index(i, j, O)
            if i != j and signs[i]*signs[j] != signs[k]:
                return False
    return True
R_e1 = [1, -1, 1, 1, 1, 1, 1, 1]
print("   R_e1 (nur e1 negiert) ist Automorphismus:", is_aut(R_e1))
auts = [s for s in itertools.product([1, -1], repeat=7) if is_aut((1,) + s)]
print("   Anzahl Vorzeichen-Automorphismen:", len(auts))
print("   die, welche e1 negieren:", [tuple(i+1 for i, x in enumerate(s) if x < 0) for s in auts if s[0] < 0])

print("(4) Sedenionen")
S = 16
ok, w = closed(tuple(range(8, 15)), S)
print(f"   O2=(f8..f14) geschlossen: {ok}" + ("" if ok else f"  (f{w[0]}*f{w[1]} = {'+' if w[2]>0 else '-'}f{w[3]})"))
a = unit(3, S) + unit(10, S); b = unit(6, S) - unit(15, S)
print("   Nullteiler-Test (e3+e10)(e6-e15) =", np.round(cd_mult(a, b), 12).tolist())
