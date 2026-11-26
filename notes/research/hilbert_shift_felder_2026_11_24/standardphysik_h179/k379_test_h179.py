"""k379 (H179): Standarderwartung fuer Up gegen Down. Aufruf: python k379_test_h179.py > k379_out.txt"""
import numpy as np
rng = np.random.default_rng(20261126); NMC = 100_000
w = np.exp(2j * np.pi / 3); kk = np.arange(3)
def cfg(m):
    v = np.sqrt(m); c = np.sum(v * np.conj(w**kk), axis=-1)
    d = np.mod(np.angle(c), 2 * np.pi / 3); d = np.minimum(d, 2 * np.pi / 3 - d)
    K = np.sum(m, axis=-1) / np.sum(v, axis=-1)**2; rho = np.sqrt(3 * K - 1)
    x = np.arccos(-1 / (np.sqrt(2) * rho)) - 2 * np.pi / 3 - d
    return K, d, rho, x
lep = np.array([0.51099895e-3, 105.6583755e-3, 1776.93e-3]); slep = np.array([1.5e-13, 2.3e-9, 0.09e-3])
dn = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sdn = np.array([0.02e-5, 0.04e-4, 0.009e-2])
up = np.array([7.04e-6, 3.56e-3, 0.967]); sup = np.array([0.15e-6, 0.06e-3, 0.004])
Sd = np.sort(np.clip(rng.normal(dn, sdn, size=(NMC, 3)), 1e-30, None), axis=1)
Su = np.sort(np.clip(rng.normal(up, sup, size=(NMC, 3)), 1e-30, None), axis=1)
gd = lambda I: np.array([np.exp(I), np.exp(I), 1.0]); gu = lambda I: np.array([np.exp(-I), np.exp(-I), 1.0])

print("== H179a: Georgi-Jarlskog, Down-Konfiguration aus den Leptonen ==")
gj = lep * np.array([3.0, 1 / 3, 1.0])
Kg, dg, rg, xg = cfg(gj)
Ke, de, re_, xe = cfg(lep)
print(f"   Leptonen: K = {Ke:.6f}, delta = {de:.6f}, rho = {re_:.5f}, x = {xe:.6f}")
print(f"   Vorhersage (3 m_e, m_mu/3, m_tau): K = {Kg:.6f}, delta = {dg:.6f}, rho = {rg:.5f}, theta = {np.degrees(np.arctan(rg)):.3f} Grad, x = {xg:.6f}")
print("   I | mu [GeV] | K_d gemessen | z(K) | delta_d gemessen | z(delta) | Abweichung K, delta in %")
best = None
for I, mu in ((0.0, "M_Z"), (0.10758, "1e13"), (0.12302, "2e16"), (0.13365, "M_Pl")):
    K0, d0, r0, x0 = cfg(dn * gd(I)); Ks, ds, _, _ = cfg(Sd * gd(I))
    zK, zd = (K0 - Kg) / Ks.std(), (d0 - dg) / ds.std()
    print(f"   {I:.4f} | {mu:>5} | {K0:.5f} +- {Ks.std():.5f} | {zK:+7.1f} | {d0:.6f} +- {ds.std():.6f} | {zd:+7.1f} | {100*(K0/Kg-1):+.2f}, {100*(d0/dg-1):+.2f}")
grid = np.linspace(0.10758, 0.13365, 27); zz = []
for I in grid:
    K0, d0, _, _ = cfg(dn * gd(I)); Ks, ds, _, _ = cfg(Sd * gd(I)); zz.append((abs((K0 - Kg) / Ks.std()), abs((d0 - dg) / ds.std())))
zz = np.array(zz); m = zz.max(axis=1); i = m.argmin()
v = "BESTAETIGT" if m[i] < 3 else ("WIDERLEGT" if (zz[:, 0].min() > 5 or zz[:, 1].min() > 5) else "UNENTSCHIEDEN")
print(f"   Bereich I in [0,108; 0,134]: kleinstes max(|z_K|, |z_delta|) = {m[i]:.1f} bei I = {grid[i]:.4f}; min |z_K| = {zz[:,0].min():.1f}, min |z_delta| = {zz[:,1].min():.1f} -> Urteil H179a: {v}")

print("\n== H179b: die drei Verhaeltnisse einzeln ==")
print("   I | m_b/m_tau | 3 m_s/m_mu | m_d/(3 m_e) | (3 m_s/m_mu)/(m_b/m_tau) | (m_d/3m_e)/(m_b/m_tau)   [Normierung faellt in den letzten beiden heraus]")
res = []
for I, mu in ((0.0, "M_Z"), (0.10758, "1e13"), (0.12302, "2e16"), (0.13365, "M_Pl")):
    f = lambda q: np.stack([q[..., 2] / lep[2], 3 * q[..., 1] / lep[1], q[..., 0] / (3 * lep[0])], axis=-1)
    c = f(dn * gd(I)); s = f(Sd * gd(I))
    r1, r2 = c[1] / c[0], c[2] / c[0]; s1, s2 = (s[:, 1] / s[:, 0]).std(), (s[:, 2] / s[:, 0]).std()
    res.append((I, r1, s1, r2, s2))
    print(f"   {I:.4f} ({mu}) | {c[0]:.5f} | {c[1]:.5f} | {c[2]:.5f} | {r1:.4f} +- {s1:.4f} (z = {(r1-1)/s1:+.1f}) | {r2:.4f} +- {s2:.4f} (z = {(r2-1)/s2:+.1f})")
print("   (Die Yukawa-Tabelle ist in Einheiten der Kopplung, die Leptonmassen in GeV; nur die beiden Doppelverhaeltnisse sind aussagekraeftig.)")
hi = [r for r in res if r[0] > 0.1]
ok = any(abs((r[1] - 1) / r[2]) < 3 and abs((r[3] - 1) / r[4]) < 3 for r in hi)
bad = all(abs((r[1] - 1) / r[2]) > 5 for r in hi) or all(abs((r[3] - 1) / r[4]) > 5 for r in hi)
print(f"   Urteil H179b: {'BESTAETIGT' if ok else ('WIDERLEGT' if bad else 'UNENTSCHIEDEN')}")

print("\n== Nicht blind (Bericht) ==")
print(f"   (i) einfache SU(5)-Gleichheit Down = Leptonen: K_d = 2/3 verlangt; gemessen 0,748 (M_Z) bis 0,735 (M_Pl). Ausgeschlossen.")
print("   (ii) Ein-Parameter-Gesetze in der Ladung (|Q| oder |Y_R|: Verhaeltnis 2; Q^2: 4):")
for I, mu in ((0.0, "M_Z"), (0.12302, "2e16")):
    Kd, _, rd, _ = cfg(dn * gd(I)); Ku, _, ru, _ = cfg(up * gu(I))
    a = (np.degrees(np.arctan(ru)) - 45) / (np.degrees(np.arctan(rd)) - 45)
    print(f"       {mu}: (theta-45)_u/(theta-45)_d = {a:.3f}; ln rho_u/ln rho_d = {np.log(ru)/np.log(rd):.3f}; (K-2/3)_u/(K-2/3)_d = {(Ku-2/3)/(Kd-2/3):.3f}  -> keines ist 2 oder 4")
print("   (iii) Potenzgesetz Up-Hierarchie = (Down-Hierarchie)^p:")
for I, mu in ((0.0, "M_Z"), (0.12302, "2e16")):
    u_, d_ = up * gu(I), dn * gd(I); su_, sd_ = Su * gu(I), Sd * gd(I)
    p1 = np.log(u_[0] / u_[2]) / np.log(d_[0] / d_[2]); p2 = np.log(u_[1] / u_[2]) / np.log(d_[1] / d_[2])
    e1 = (np.log(su_[:, 0] / su_[:, 2]) / np.log(sd_[:, 0] / sd_[:, 2])).std(); e2 = (np.log(su_[:, 1] / su_[:, 2]) / np.log(sd_[:, 1] / sd_[:, 2])).std()
    print(f"       {mu}: p aus der leichtesten = {p1:.4f} +- {e1:.4f}, p aus der mittleren = {p2:.4f} +- {e2:.4f}; Unterschied {(p1-p2)/np.hypot(e1,e2):.0f} sigma (ein gemeinsames p, etwa 2, traegt nicht)")
pl1 = np.log(lep[0] / lep[2]) / np.log(dn[0] / dn[2]); pl2 = np.log(lep[1] / lep[2]) / np.log(dn[1] / dn[2])
print(f"       Leptonen gegen Down (M_Z): p = {pl1:.4f} und {pl2:.4f}")
