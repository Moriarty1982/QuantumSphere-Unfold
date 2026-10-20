"""k17: Test der Vorab-Notiz H3 (Commit e3b140e): Triolen-Vorzeichen als Majorana-CP-Paritaet.
m_bb = | eta1 c12^2 c13^2 m1 + eta2 s12^2 c13^2 m2 + eta3 s13^2 m3 e^{-2 i dCP} |, Massen aus H2 (NO)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k15_test_h2 import solve, ratio, sorted_masses, D21, s21, D31_NO, s31_NO
from scipy.optimize import brentq

S12, s_s12 = 0.308, 0.0115
S13, s_s13 = 0.02215, 0.00057
DCP, s_dcp = np.radians(212), np.radians(33.5)

_REF = solve("NO", D21, D31_NO)[0]['delta']
def masses(d21, d31):  # lokale Loesung nahe der H2-Loesung (eindeutig, vgl. k15)
    d = brentq(lambda x: ratio(x, "NO") - d21/d31, _REF - 0.05, _REF + 0.05, xtol=1e-13)
    (a, b, c), sg = sorted_masses(d)
    t2 = np.sqrt(d31/(c*c - a*a))
    return t2*np.array([a, b, c]), sg

def mbb(m, eta, s12, s13, dcp):
    c12, c13 = 1 - s12, 1 - s13
    return abs(eta[0]*c12*c13*m[0] + eta[1]*s12*c13*m[1] + eta[2]*s13*m[2]*np.exp(-2j*dcp))

def mbeta(m, s12, s13):
    return np.sqrt((1-s12)*(1-s13)*m[0]**2 + s12*(1-s13)*m[1]**2 + s13*m[2]**2)

m, sg = masses(D21, D31_NO)
eta_H3 = sg.astype(int)                 # Vorzeichen in Ordnung m1<m2<m3
print("Massen (meV):", np.round(m*1e3, 3), " eta (H3):", eta_H3)
for name, eta in (("H3 eta1=-1", eta_H3), ("Vergleich eta1=+1", np.array([1, 1, 1]))):
    c = mbb(m, eta, S12, S13, DCP)
    rng_d = [mbb(m, eta, S12, S13, x) for x in np.radians(np.arange(0, 360, 0.1))]
    print(f"{name}: m_bb(dCP=212) = {c*1e3:.3f} meV;  Bereich ueber dCP: [{min(rng_d)*1e3:.3f}, {max(rng_d)*1e3:.3f}] meV")
print(f"m_beta = {mbeta(m, S12, S13)*1e3:.3f} meV")

# Monte Carlo
rng = np.random.default_rng(17); N = 100000
d21 = rng.normal(D21, s21, N); d31 = rng.normal(D31_NO, s31_NO, N)
s12 = rng.normal(S12, s_s12, N); s13 = rng.normal(S13, s_s13, N); dcp = rng.normal(DCP, s_dcp, N)
out = np.empty((N, 3)); MS = []
for i in range(N):
    mi, sgi = masses(d21[i], d31[i]); MS.append(mi)
    e = sgi.astype(int)
    out[i] = (mbb(mi, e, s12[i], s13[i], dcp[i]), mbb(mi, np.array([1, 1, 1]), s12[i], s13[i], dcp[i]),
              mbeta(mi, s12[i], s13[i]))
for k, name in enumerate(("m_bb H3", "m_bb eta1=+1", "m_beta")):
    x = out[:, k]*1e3
    print(f"MC {name}: {x.mean():.3f} +- {x.std():.3f} meV; 95%: [{np.percentile(x,2.5):.3f}, {np.percentile(x,97.5):.3f}]")
# obere 95%-Grenze ueber vollen dCP-Bereich (fuer das Widerlegungskriterium)
dfull = rng.uniform(0, 2*np.pi, N)
xf = np.array([mbb(MS[i], eta_H3, s12[i], s13[i], dfull[i]) for i in range(N)])*1e3
print(f"H3, dCP gleichverteilt: 95%-Obergrenze m_bb = {np.percentile(xf, 95):.3f} meV, max = {xf.max():.3f} meV")
