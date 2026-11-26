"""k356: Test H165. Schliessungsbedingungen fuer beta_sym in der Zwei-Auslesen-Lesart.
Aufruf: python k356_test_h165.py   (keine Argumente, keine Pfade)
Werkzeuge: mpmath (Summen, 30 Stellen), sympy (Identitaeten), Qiskit quantum_info (Spin-j-Ueberlappe).
"""
import mpmath as mp
import sympy as sp
import numpy as np
from qiskit.quantum_info import Statevector
import qiskit

mp.mp.dps = 40
ln2 = mp.log(2)
c = lambda k: mp.sqrt(mp.mpf(k) * (k + 2) / 3)

def Z(g, cf=c):
    return mp.nsum(lambda k: 2 ** (1 - g * cf(k)), [1, mp.inf])

print("== K-a: Ziel ==")
gM = mp.findroot(lambda g: mp.nsum(lambda k: 2 * mp.exp(-mp.pi * g * mp.sqrt(k * (k + 2))), [1, mp.inf]) - 1, 0.24)
gT = ln2 / (mp.pi * mp.sqrt(3))
gL = mp.findroot(lambda g: Z(g) - 1, 1.9)
beta = mp.sqrt((gL - 1) / (gL + 1))
print("gamma_M           =", mp.nstr(gM, 30))
print("gamma_T           =", mp.nstr(gT, 30))
print("Wurzel Z(g)=1     =", mp.nstr(gL, 30))
print("gamma_M/gamma_T   =", mp.nstr(gM / gT, 30))
print("Differenz         =", mp.nstr(gL - gM / gT, 5))
print("beta              =", mp.nstr(beta, 30))
print("artanh beta       =", mp.nstr(mp.atanh(beta), 30))
print("Z monoton fallend: Z(1.0), Z(1.5), Z(2.0), Z(3.0) =", [mp.nstr(Z(x), 8) for x in (1.0, 1.5, 2.0, 3.0)])
x = sp.symbols("x", positive=True)
k = sp.symbols("k", integer=True, positive=True)
S = sp.summation(2 * x ** (k + 1), (k, 1, sp.oo))
print("Hopf-Variante (c_k=(k+1)/2, x=2^(-g/2)): Summe =", sp.simplify(S.args[0][0] if S.is_Piecewise else S),
      "; Loesungen x:", sp.solve(sp.Eq(2 * x ** 2 / (1 - x), 1), x), "=> g = 2 exakt")

print("\n== K-b: Schliessung mit Ueberlappen ==")
q = sp.symbols("q", positive=True)
print("Sum_k 2 q^k = 1  =>  q =", sp.solve(sp.Eq(2 * q / (1 - q), 1), q), " (q = beta^p, k = 2j)")
target = beta
res = {}
for p in (1, 2, 4):
    b = mp.mpf(1) / 3 ** (mp.mpf(1) / p)
    res[f"p={p}, Exponent 2j"] = b
for name, cf in (("p=2, Exponent c_k", c), ("p=2, Exponent sqrt(k(k+2))", lambda k: mp.sqrt(mp.mpf(k) * (k + 2)))):
    qq = mp.findroot(lambda t: mp.nsum(lambda k: 2 * t ** cf(k), [1, mp.inf]) - 1, 0.3)
    res[name] = mp.sqrt(qq)
for n, b in res.items():
    print(f"{n:32s} beta = {mp.nstr(b, 12)}   rel. Abweichung vom Ziel = {mp.nstr(b / target - 1, 4)}")
print("noetiges p fuer das Ziel: ln3/(-ln beta) =", mp.nstr(mp.log(3) / -mp.log(beta), 12))

print("\nQiskit", qiskit.__version__, ": |<j;K1|j;S>| fuer das Paar bei beta = 1/sqrt(3) und beim Ziel")
for bname, b in (("1/sqrt3", 1 / np.sqrt(3)), ("Ziel", float(beta))):
    th = 2 * np.arcsin(b)
    K1 = Statevector([np.cos(th / 2), np.sin(th / 2)])
    Sst = Statevector([0, 1])
    tot = 0.0
    line = []
    for twoj in range(1, 7):
        a, s_ = K1, Sst
        for _ in range(twoj - 1):
            a = a.tensor(K1); s_ = s_.tensor(Sst)
        ov = abs(a.inner(s_))
        line.append(f"{ov:.6f}")
        tot += 2 * ov ** 2
    geo = 2 * b ** 2 / (1 - b ** 2)
    print(f"  beta={bname}: Ueberlappe 2j=1..6: {line}; Teilsumme 2*|.|^2 bis 2j=6 = {tot:.6f}; volle Summe = {geo:.6f}")

print("\n== K-c: Zahlenkandidaten (Identitaet nur bei rel. < 1e-8) ==")
K = 400
pk = [2 ** (1 - gL * c(kk)) for kk in range(1, K)]
norm = mp.fsum(pk)
print("Summe p_k =", mp.nstr(norm, 25))
mean = lambda f: mp.fsum(p * f(kk) for kk, p in zip(range(1, K), pk))
p1 = pk[0]
gsc = mp.findroot(lambda g: 2 ** (1 - g) - mp.sqrt((g - 1) / (g + 1)), 1.86)
cm = mean(c)
cands = [
    ("1  2^(1-gamma_L) = beta", p1, beta),
    ("2  Wurzel 2^(1-g)=sqrt((g-1)/(g+1)) = gamma_L", gsc, gL),
    ("3  1/<c> = artanh(1/sqrt3)", 1 / cm, mp.atanh(1 / mp.sqrt(3))),
    ("4  <k> = gamma_L", mean(lambda kk: kk), gL),
    ("5a <sqrt(j/(j+1))> = beta", mean(lambda kk: mp.sqrt(mp.mpf(kk) / (kk + 2))), beta),
    ("5b <sqrt(j/(j+1))> = 1/sqrt3", mean(lambda kk: mp.sqrt(mp.mpf(kk) / (kk + 2))), 1 / mp.sqrt(3)),
    ("6a <1/c> = beta", mean(lambda kk: 1 / c(kk)), beta),
    ("6b <1/c> = 1/gamma_L", mean(lambda kk: 1 / c(kk)), 1 / gL),
    ("6c <1/c> = beta^2", mean(lambda kk: 1 / c(kk)), beta ** 2),
    ("7a p1/(1-p1) = gamma_L - 1", p1 / (1 - p1), gL - 1),
    ("7b p1/(1-p1) = 1/beta^2 - 2", p1 / (1 - p1), 1 / beta ** 2 - 2),
    ("8a <c> = gamma_L - 1/3", cm, gL - mp.mpf(1) / 3),
    ("8b <c> = 3/2", cm, mp.mpf(3) / 2),
]
hits3 = 0
for n, a, b in cands:
    rel = a / b - 1
    tag = "IDENTITAET" if abs(rel) < mp.mpf("1e-8") else ("Treffer <1e-3, keine Identitaet" if abs(rel) < mp.mpf("1e-3") else "verfehlt")
    hits3 += abs(rel) < mp.mpf("1e-3")
    print(f"{n:48s} {mp.nstr(a, 12):>16s} gegen {mp.nstr(b, 12):>16s}  rel = {mp.nstr(rel, 4):>12s}  {tag}")
print("Vergleiche:", len(cands), "; Treffer innerhalb 1e-3:", int(hits3))
print("beta der selbstkonsistenten Wurzel (Nr. 2):", mp.nstr(2 ** (1 - gsc), 12))

print("\n== K-d: Kegel ==")
j = sp.Rational(1, 2)
cosc = j / sp.sqrt(j * (j + 1))
print("j/sqrt(j(j+1)) bei j=1/2 =", sp.nsimplify(cosc), "; cos(2*Kegelwinkel) =", sp.simplify(2 * cosc ** 2 - 1))
