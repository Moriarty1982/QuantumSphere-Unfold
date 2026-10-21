"""K14 / r11: Test der Vorab-Hypothese H1 (delta = K/3) und H1' (delta = 2/9).
Verfahren exakt nach llm/Vorab_Notiz_H1_Koide_Phase.md (Commit 81f38d3).
"""
import numpy as np
rng = np.random.default_rng(20261020)
w = np.exp(2j*np.pi/3); k = np.arange(3)
NMC = 1_000_000

def K_delta(m):                      # m: (..., 3), aufsteigend sortiert
    v = np.sqrt(m)
    c = np.sqrt(2)/3*np.sum(v*np.conj(w**k), axis=-1)
    d = np.mod(np.angle(c), 2*np.pi/3)
    K = np.sum(m, axis=-1)/np.sum(v, axis=-1)**2
    return K, d

primary = {
    "Up-Quarks (u,c,t) bei M_Z":    [(7.04e-6, 0.15e-6), (3.56e-3, 0.06e-3), (0.967, 0.004)],
    "Down-Quarks (d,s,b) bei M_Z":  [(1.54e-5, 0.02e-5), (3.06e-4, 0.04e-4), (1.630e-2, 0.009e-2)],
    "Leptonen (e,mu,tau) bei M_Z":  [(2.77713e-6, 0.00036e-6), (5.85042e-4, 0.00075e-4), (0.99378e-2, 0.00014e-2)],
}
secondary = {
    "Up-Quarks PDG-Standardskalen":   [(2.16e-3, 0.04e-3), (1.2730, 0.0028), (172.4, 0.7)],
    "Down-Quarks PDG-Standardskalen": [(4.70e-3, 0.04e-3), (93.5e-3, 0.5e-3), (4.183, 0.004)],
    "Leptonen Polmassen (Kalibrierung)": [(0.51099895e-3, 0.0000000015e-3), (105.6583755e-3, 0.0000023e-3), (1776.93e-3, 0.09e-3)],
}

def run(name, data):
    mu = np.array([x for x, _ in data]); sd = np.array([s for _, s in data])
    K0, d0 = K_delta(mu)
    sam = rng.normal(mu, sd, size=(NMC, 3)); sam = np.clip(sam, 1e-30, None)
    sam = np.sort(sam, axis=1)
    K, d = K_delta(sam)
    r1 = d - K/3; r2 = d - 2/9
    z1 = (d0 - K0/3)/np.std(r1); z2 = (d0 - 2/9)/np.std(r2)
    verdict = lambda z: "vertraeglich" if abs(z) < 2 else ("unentschieden" if abs(z) <= 3 else "WIDERLEGT")
    print(f"{name}\n   K = {K0:.6f}   delta = {d0:.6f}   K/3 = {K0/3:.6f}   2/9 = {2/9:.6f}")
    print(f"   H1  delta - K/3 = {d0 - K0/3:+.6f}  sigma = {np.std(r1):.2e}  z = {z1:+.1f}  -> {verdict(z1)}")
    print(f"   H1' delta - 2/9 = {d0 - 2/9:+.6f}  sigma = {np.std(r2):.2e}  z = {z2:+.1f}  -> {verdict(z2)}")
    return z1, z2

print("=== Primaerdaten (entscheidend) ===")
res = {n: run(n, d) for n, d in primary.items()}
print("\n=== Sekundaerdaten (ergaenzend) ===")
for n, d in secondary.items(): run(n, d)
quarks = [v for n, v in res.items() if "Quark" in n]
h1 = "WIDERLEGT" if any(abs(z1) > 3 for z1, _ in quarks) else ("GESTUETZT" if all(abs(z1) < 2 for z1, _ in quarks) else "UNENTSCHIEDEN")
h1p = "WIDERLEGT" if any(abs(z2) > 3 for _, z2 in quarks) else ("GESTUETZT" if all(abs(z2) < 2 for _, z2 in quarks) else "UNENTSCHIEDEN")
print(f"\nGesamturteil nach Vorab-Kriterium:  H1 (delta = K/3): {h1}   |   H1' (delta = 2/9): {h1p}")
