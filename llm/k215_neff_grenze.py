"""k215 (Erkundung): Delta N_eff als Funktion einer Gueltigkeitsgrenze x_c = k_c Delta.
Gravitonen (2 Polarisationen) mit Photon-Gewichten, uebrige Bosonen (g_B) mit Materie-Gewichten; Spektren n_mix(x) wie k214
(tanh, beide Drehsinne gemittelt); gezaehlt nur Moden mit x < x_c. Annahmen zur Thermalisierung wie k213.
Aufruf (aus llm/): python k215_neff_grenze.py
"""
import numpy as np
import k210_norm_uebergang as m
from k214_erzeugung_photongewichte import nmix

a_mat, b_mat = m.a, m.b
xs = np.linspace(0.005, 1.0, 80)
nM = np.array([nmix(x, a_mat, b_mat) for x in xs])
nP = np.array([nmix(x, 0.5, 0.5) for x in xs])
m.a, m.b = a_mat, b_mat
pref = (8/7)*(11/4)**(4/3)
print('x_c | n_P(x_c) | E_grav/E_boson je Freiheitsgrad | Delta N_eff (g_B = 28) | (g_B = 4)')
for xc in (0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0):
    sel = xs <= xc
    EP = np.trapezoid(xs[sel]**3*nP[sel], xs[sel]); EM = np.trapezoid(xs[sel]**3*nM[sel], xs[sel])
    out = []
    for gB in (28, 4):
        f = 2*EP/(2*EP + gB*EM)
        r = f/(1 - f)*(106.75/10.75)**(1/3)*10.75/2
        out.append(pref*r)
    print(f'{xc:.2f} | {np.interp(xc, xs, nP):.4f} | {EP/EM:.4f} | {out[0]:.3f} | {out[1]:.3f}')
print('Kleine x: n_P/x^2 =', round(float(nP[2]/xs[2]**2), 3), ' n_M =', round(float(nM[0]), 4))
