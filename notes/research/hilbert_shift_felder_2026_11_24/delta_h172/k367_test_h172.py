"""k367 (H172): Quarks als Pruefstein. Phasenlage chi(Q) = |Q| pi/4 mit Versatz x gegen die Quark-Phasen.
Vorab-Notiz Vorab_Notiz_H172_Quarks_Phase_und_Ladung.md (Commit dbc30d1). Daten und Verfahren wie k14 (H1).
Aufruf: python3 k367_test_h172.py > k367_out.txt
"""
import numpy as np
rng = np.random.default_rng(20261126)
w = np.exp(2j * np.pi / 3); kk = np.arange(3)
NMC = 1_000_000
X = 0.0395773407
DSTAR = 0.2222220470731


def K_delta(m, neg=False):
    v = np.sqrt(m)
    if neg:
        v = v * np.array([-1.0, 1.0, 1.0])
    c = np.sum(v * np.conj(w**kk), axis=-1)
    d = np.mod(np.angle(c), 2 * np.pi / 3)
    d = np.minimum(d, 2 * np.pi / 3 - d)                # gefaltet auf [0, pi/3]
    K = np.sum(m, axis=-1) / np.sum(v, axis=-1)**2
    return K, d


data = {
    "up":   {"M_Z": [(7.04e-6, 0.15e-6), (3.56e-3, 0.06e-3), (0.967, 0.004)],
             "PDG": [(2.16e-3, 0.04e-3), (1.2730, 0.0028), (172.4, 0.7)]},
    "down": {"M_Z": [(1.54e-5, 0.02e-5), (3.06e-4, 0.04e-4), (1.630e-2, 0.009e-2)],
             "PDG": [(4.70e-3, 0.04e-3), (93.5e-3, 0.5e-3), (4.183, 0.004)]},
}
lept = [(0.51099895e-3, 0.0000000015e-3), (105.6583755e-3, 0.0000023e-3), (1776.93e-3, 0.09e-3)]
pred = {"down": {"pi/12": np.pi / 12, "pi/12 - x": np.pi / 12 - X, "pi/12 + x": np.pi / 12 + X},
        "up": {"0": 0.0, "x": X, "pi/6": np.pi / 6, "pi/6 - x": np.pi / 6 - X, "pi/6 + x": np.pi / 6 + X}}


def meas(dat, neg=False):
    mu = np.array([a for a, _ in dat]); sd = np.array([b for _, b in dat])
    K0, d0 = K_delta(mu, neg)
    sam = np.sort(np.clip(rng.normal(mu, sd, size=(NMC, 3)), 1e-30, None), axis=1)
    Ks, ds = K_delta(sam, neg)
    return K0, d0, np.std(Ks), np.std(ds)


print("== H172b: Kontrolle Leptonen (Polmassen) ==")
K0, d0, sK, sd_ = meas(lept)
print(f"K = {K0:.8f} (K - 2/3 = {K0 - 2/3:+.2e}, sigma {sK:.1e}); delta = {d0:.9f} (delta - delta* = {d0 - DSTAR:+.2e}, sigma {sd_:.1e})")
print("   Hinweis: delta* gilt bei K = 2/3 aus m_mu/m_e allein; hier geht m_tau mit Fehler ein.")

print("\n== H172a: Vorhersage gegen Daten ==")
res = {}
for typ in ("down", "up"):
    for neg in (False, True):
        for dset in ("M_Z", "PDG"):
            K0, d0, sK, sd_ = meas(data[typ][dset], neg)
            res[(typ, neg, dset)] = (K0, d0, sK, sd_)
            print(f"{typ:>4}, leichteste Wurzel {'negativ' if neg else 'positiv'}, {dset}: K = {K0:.6f} +- {sK:.6f}, delta = {d0:.6f} +- {sd_:.6f}")
            for name, val in pred[typ].items():
                print(f"        gegen {name:>9} = {val:.6f}: z = {(d0 - val) / sd_:+9.1f}")
print("\nUrteil nach Vorab-Kriterium (Primaer |z| < 3 und Sekundaer |z| < 5: bestaetigt; Primaer kein Kandidat < 5: widerlegt):")
for typ in ("down", "up"):
    for neg in (False, True):
        K0, d0, sK, sd_ = res[(typ, neg, "M_Z")]; K1, d1, sK1, sd1 = res[(typ, neg, "PDG")]
        zs = {n: ((d0 - v) / sd_, (d1 - v) / sd1) for n, v in pred[typ].items()}
        ok = [n for n, (z0, z1) in zs.items() if abs(z0) < 3 and abs(z1) < 5]
        near = min(abs(z0) for z0, _ in zs.values())
        verdict = "BESTAETIGT (" + ", ".join(ok) + ")" if ok else ("WIDERLEGT" if near > 5 else "unentschieden")
        print(f"   {typ:>4}, Wurzel {'negativ' if neg else 'positiv'}: kleinstes |z| primaer = {near:.1f} -> {verdict}")

print("\n== H172c: Bericht rueckwaerts ==")
for typ, Q in (("down", 1 / 3), ("up", 2 / 3)):
    for neg in (False, True):
        d0 = res[(typ, neg, "M_Z")][1]; d1 = res[(typ, neg, "PDG")][1]
        print(f"{typ:>4} (|Q| = {Q:.4f}), Wurzel {'negativ' if neg else 'positiv'}: delta(M_Z) = {d0:.6f}, delta(PDG) = {d1:.6f}, Skalenabhaengigkeit {d1 - d0:+.6f}; "
              f"delta + x = {d0 + X:.6f} / {d1 + X:.6f}; Regelwert chi = |Q| pi/4 = {Q * np.pi / 4:.6f}")
print(f"Leptonen zum Vergleich: delta = {DSTAR:.6f}, delta + x = pi/12 = {np.pi/12:.6f}")
print("K: up", f"{res[('up', False, 'M_Z')][0]:.4f} / {res[('up', False, 'PDG')][0]:.4f}", "; down", f"{res[('down', False, 'M_Z')][0]:.4f} / {res[('down', False, 'PDG')][0]:.4f}", "; Leptonen 0.6667")
