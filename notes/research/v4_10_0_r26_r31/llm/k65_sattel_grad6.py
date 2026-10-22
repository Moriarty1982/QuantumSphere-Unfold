"""k65: Nachkontrolle zu H16 (nach dem Urteil, nicht Teil des Kriteriums).
Satz: Jedes Potential in den Normen und t = P bis Grad 6 ist linear in e2 = sum_{i<j} x_i x_j:
V = A(S, P) + e2 * (b0 + b1 S). An einem kritischen Punkt mit drei verschiedenen Normen ist die Hessematrix in den
Koordinaten (S, e2, P) [[*, b1, *], [b1, 0, 0], [*, 0, *]], ihr 2x2-Hauptminor hat Determinante -b1^2 < 0:
Sattelpunkt (b1 != 0) oder V haengt nicht von e2 ab (flach, Massen unbestimmt). Exakte Pruefung mit 40 Stellen."""
import numpy as np, sympy as sp, mpmath as mp

n1, n2, n3 = sp.symbols('n1 n2 n3', positive=True)
y = [n1**2, n2**2, n3**2]; S = sum(y); P = n1*n2*n3; e2 = y[0]*y[1] + y[0]*y[2] + y[1]*y[2]
Q = sum(v**2 for v in y); H = sum(v**3 for v in y)
print("Q  - (S^2 - 2 e2)            =", sp.expand(Q - (S**2 - 2*e2)))
print("H  - (S^3 - 3 S e2 + 3 P^2)  =", sp.expand(H - (S**3 - 3*S*e2 + 3*P**2)))
print("SQ - (S^3 - 2 S e2)          =", sp.expand(S*Q - (S**3 - 2*S*e2)))
print("-> alle Grad-<=6-Invarianten (S, S^2, S^3, Q, SQ, H, P, SP, P^2) sind linear in e2.\n")

a1, a2, a3, k, l, mu, b0, b1 = sp.symbols('a1 a2 a3 k l mu b0 b1')
V = a1*S + a2*S**2 + a3*S**3 - k*P - l*S*P + mu*P**2 + e2*(b0 + b1*S)
Gf = sp.lambdify((n1, n2, n3, a1, a2, a3, k, l, mu, b0, b1), [sp.diff(V, v) for v in (n1, n2, n3)], 'mpmath')
Hf = sp.lambdify((n1, n2, n3, a1, a2, a3, k, l, mu, b0, b1), sp.hessian(V, (n1, n2, n3)), 'mpmath')
mp.mp.dps = 40
rng = np.random.default_rng(65); neg = 0; N = 2000; worst = mp.mpf(1)
for _ in range(N):
    x = [mp.mpf(v) for v in np.sort(rng.uniform(0.01, 3, 3))]; nn = [mp.sqrt(v) for v in x]
    Sv = sum(x); Pv = nn[0]*nn[1]*nn[2]; e2v = x[0]*x[1] + x[0]*x[2] + x[1]*x[2]
    B1 = mp.mpf(rng.normal()); B0 = -B1*Sv                       # dV/de2 = 0
    A2, A3, L = [mp.mpf(v) for v in rng.normal(size=3)]; K = mp.mpf(rng.uniform(0, 3))
    MU = (K + L*Sv)/(2*Pv)                                        # dV/dP = 0
    A1 = -(2*A2*Sv + 3*A3*Sv**2 - L*Pv + B1*e2v)                  # dV/dS = 0
    args = (*nn, A1, A2, A3, K, L, MU, B0, B1)
    assert max(abs(g) for g in Gf(*args)) < mp.mpf(10)**-25
    ev = mp.eigsy(mp.matrix(Hf(*args)))[0]; ev = [ev[i] for i in range(3)]
    neg += min(ev) < 0; worst = min(worst, abs(min(ev))/max(abs(e) for e in ev))
print(f"Zufaellige kritische Punkte mit drei verschiedenen Normen (allgemeinster Grad-6-Ansatz): {neg} von {N} Sattelpunkte")
print(f"kleinstes |lambda_min|/|lambda_max| = {mp.nstr(worst, 3)}  (doppelte Genauigkeit reicht dafuer nicht immer)")
