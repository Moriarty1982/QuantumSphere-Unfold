"""k70 (bis zur Uebernahme k67): Nachkontrolle zu H17 (nach dem Urteil, nicht Teil des Kriteriums).
Auf der reellen Achse (a_k = n_k reell) ist V_R ein symmetrisches Polynom in n vom Grad 4 und darin linear in
e3 = n1 n2 n3:  V_R = A(e1, e2) + e3 (4 gamma e1 - kappa).  Bei drei verschiedenen n_k sind (e1, e2, e3) Koordinaten;
die Hessematrix hat dort H_33 = 0, H_13 = 4 gamma -> Hauptminor -16 gamma^2 < 0: Sattel (gamma != 0).
Ein Sattel der Einschraenkung auf die Achse ist ein Sattel auf ganz O^3."""
import numpy as np, sympy as sp, mpmath as mp, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import V, G

n1, n2, n3 = sp.symbols('n1 n2 n3', real=True)
b, g, k, mu, nu, la = sp.symbols('beta gamma kappa mu nu lambda', real=True)
e1, e2, e3 = n1+n2+n3, n1*n2+n1*n3+n2*n3, n1*n2*n3
S = n1**2+n2**2+n3**2; Q = n1**4+n2**4+n3**4; L = e1
VR = -S + b*S**2 + g*Q - k*e3 - mu*L - nu*S - la*L**2       # auf der Achse: t = e3, R2 = S
E1, E2, E3 = sp.symbols('E1 E2 E3')
Vsym = -(1+nu)*(E1**2-2*E2) + b*(E1**2-2*E2)**2 + g*(E1**4-4*E1**2*E2+2*E2**2+4*E1*E3) - k*E3 - mu*E1 - la*E1**2
print("V_R auf der Achse - Ausdruck in (e1,e2,e3):", sp.expand(VR - Vsym.subs({E1: e1, E2: e2, E3: e3})))
print("d^2 V/d e3^2 =", sp.diff(Vsym, E3, 2), ";  d^2 V/(d e1 d e3) =", sp.diff(Vsym, E1, E3), "\n")

# Die Gitterpunkte aus H17b, die den numerischen Test auf lokales Minimum bestanden haben: exakte Hessematrix auf der Achse
m = np.array([0.51099895, 105.6583755, 1776.93]); nl = np.sqrt(m/m[2])
Hn = sp.hessian(VR, (n1, n2, n3)); Hf = sp.lambdify((n1, n2, n3, b, g, k, mu, nu, la), Hn, 'mpmath')
mp.mp.dps = 50; found = 0
for s in np.logspace(-2, 2, 21):
    n = np.sqrt(s)*nl; Sx = (n**2).sum(); Lx = n.sum(); P = n.prod(); e2x = n[0]*n[1]+n[0]*n[2]+n[1]*n[2]
    for gg in (0.1, 0.3, 1, 3):
        for nn in (0, 0.5, 1, 2, 5, 10, 30):
            for ll in (-1, 0, 1):
                kk = 4*gg*Lx; mm = 4*gg*(P - Lx*e2x) - 2*ll*Lx; bb = (4*gg*(e2x - Lx**2) + 2*(1+nn))/(4*Sx)
                if not (bb > 0 and bb + gg > 0): continue
                p = (bb, gg, kk, mm, nn, ll); z0 = np.zeros(24); z0[0], z0[8], z0[16] = n; h = 1e-6*np.sqrt(s)
                Hm = np.array([(G(z0+e, *p)-G(z0-e, *p))/(2*h) for e in np.eye(24)*h]); Hm = (Hm+Hm.T)/2
                ev = np.linalg.eigvalsh(Hm)
                if ev.min() < -1e-8*np.abs(ev).max(): continue
                found += 1
                evx = mp.eigsy(mp.matrix(Hf(*[mp.mpf(float(v)) for v in (*n, *p)])))[0]
                evx = sorted(evx[i] for i in range(3))
                print(f"  s = {s:.3g}, gamma = {gg}, nu = {nn}, lambda = {ll}: numerisch min. Eigenwert {ev.min():+.2e}"
                      f" (relativ {ev.min()/np.abs(ev).max():+.1e}); exakt auf der Achse {mp.nstr(evx[0], 4)}, {mp.nstr(evx[1], 4)}, {mp.nstr(evx[2], 4)}")
print(f"\n{found} Punkte mit bestandenem numerischen Test; exakt hat jeder einen negativen Eigenwert auf der Achse,"
      " wenn oben jeweils der erste Wert negativ ist.")
