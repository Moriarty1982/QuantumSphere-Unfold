"""K11 / r08: Test der Vorhersage P1 (Companion cor:odlyzko, thm:gue-selfdet).

Photon-Frame-Entfaltung mit Skala mu:
   rho_mu(t) = log(t/(2 pi mu))/(2 pi mu),   gt_n(mu) = int_0^{gamma_n} rho_mu dt,   s_n(mu) = gt_{n+1} - gt_n.
Vorhersage: F(mu) = KS[P_mu, P_GUE] hat ein eindeutiges globales Minimum bei mu = gL = 1.864;
chi^2-Verbesserung ~21 % gegenueber mu = 1 (Standard).

Geprueft wird (a) roh, wie im Companion definiert, und (b) mit Normierung auf mittleren Abstand 1
(sonst verschiebt allein die Skala den Mittelwert).
"""
import os
import numpy as np
from scipy import integrate, stats

here = os.path.dirname(os.path.abspath(__file__))
g = np.load(os.path.join(here, "zeros.npy"))
gL = 0.2375/(np.log(2)/(np.pi*np.sqrt(3)))

def unfold(gam, mu):
    # int rho_mu = t/(2 pi mu) * (log(t/(2 pi mu)) - 1)
    return gam/(2*np.pi*mu)*(np.log(gam/(2*np.pi*mu)) - 1)

p_gue = lambda x: 32/np.pi**2*x**2*np.exp(-4*x**2/np.pi)
xs = np.linspace(0, 5, 5001); cdf_tab = np.concatenate([[0], np.cumsum((p_gue(xs[1:]) + p_gue(xs[:-1]))/2*np.diff(xs))])
cdf = lambda x: np.interp(x, xs, cdf_tab, right=1.0)

def chi2(s, bins=np.linspace(0, 3, 16)):
    obs, _ = np.histogram(s, bins)
    exp = len(s)*np.diff(cdf(bins))
    m = exp > 0
    return np.sum((obs[m] - exp[m])**2/exp[m])/(m.sum() - 1)

def scan(gam, label):
    mus = np.round(np.arange(0.5, 3.01, 0.05), 3)
    raw, nrm, c_raw, c_nrm = [], [], [], []
    for mu in mus:
        s = np.diff(unfold(gam, mu))
        raw.append(stats.kstest(s, cdf).statistic); c_raw.append(chi2(s))
        sn = s/np.mean(s)
        nrm.append(stats.kstest(sn, cdf).statistic); c_nrm.append(chi2(sn))
    raw, nrm = np.array(raw), np.array(nrm)
    i1 = int(np.argmin(np.abs(mus - 1.0))); iL = int(np.argmin(np.abs(mus - gL)))
    print(f"\n{label}  ({len(gam)} Nullstellen, {len(gam)-1} Abstaende)")
    print(f"   roh:        KS-Minimum bei mu = {mus[np.argmin(raw)]:.2f}  |  KS(mu=1) = {raw[i1]:.4f}, KS(mu=gL) = {raw[iL]:.4f}")
    print(f"               chi2/dof(mu=1) = {c_raw[i1]:.2f}, chi2/dof(mu=gL) = {c_raw[iL]:.2f}  ->  Verbesserung {1 - c_raw[iL]/c_raw[i1]:+.1%}")
    print(f"               Mittelwert der Abstaende bei mu = gL: {np.mean(np.diff(unfold(gam, gL))):.3f} (GUE: 1)")
    print(f"   normiert:   KS-Minimum bei mu = {mus[np.argmin(nrm)]:.2f}  |  KS(mu=1) = {nrm[i1]:.4f}, KS(mu=gL) = {nrm[iL]:.4f}")
    print(f"               chi2/dof(mu=1) = {c_nrm[i1]:.2f}, chi2/dof(mu=gL) = {c_nrm[iL]:.2f}  ->  Verbesserung {1 - c_nrm[iL]/c_nrm[i1]:+.1%}")
    print(f"               Spannweite KS normiert ueber mu in [0.5,3]: {nrm.min():.4f} .. {nrm.max():.4f}")

print(f"gL = {gL:.4f}")
scan(g[:100], "Erste 100 Nullstellen (wie im Companion)")
scan(g[100:2000], "Nullstellen 101-2000")
