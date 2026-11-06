"""k214 (Erkundung, Nachpruefung zu k213 und zur Entscheidung 'Photon-Gewichte'): Erzeugung am glatten Uebergang
fuer Materie-Gewichte (a, b aus beta_sym) und Photon-Gewichte (a = b), tanh-Profil, Delta = 2.
Mass der Beimischung: n_mix(k) = min(|C|^2, |D|^2)/(b/a) (scharfer Grenzfall Materie: n0 = 0.404; Photon: 0).
Energie-Integral I = int_0^{x_max} x^3 n_mix(x) dx mit x = k Delta (Einheiten Delta^-4), Mittel ueber beide Drehsinne.
Aufruf (aus llm/): python k214_erzeugung_photongewichte.py
"""
import numpy as np
import k210_norm_uebergang as m

a_mat, b_mat = m.a, m.b
xs = np.concatenate([np.linspace(0.02, 1, 25), np.linspace(1.1, 4, 30), np.linspace(4.5, 8, 8)])


def nmix(x, aa, bb):
    m.a, m.b = aa, bb
    vals = []
    for s in (+1, -1):
        N, C, D, w = m.N_boson(x, s)
        vals.append(min(C**2, D**2)/(bb/aa))
    return float(np.mean(vals))


for name, (aa, bb) in {'Materie': (a_mat, b_mat), 'Photon': (0.5, 0.5)}.items():
    n = np.array([nmix(x, aa, bb) for x in xs])
    I = np.trapezoid(xs**3*n, xs)
    i_max = int(np.argmax(xs**3*n))
    print(f'{name}: I = {I:.3f} Delta^-4; n_mix(0.02) = {n[0]:.4f}, max n_mix = {n.max():.3f} bei kDelta = {xs[np.argmax(n)]:.2f}; '
          f'Integrand max bei kDelta = {xs[i_max]:.2f}')
m.a, m.b = a_mat, b_mat
