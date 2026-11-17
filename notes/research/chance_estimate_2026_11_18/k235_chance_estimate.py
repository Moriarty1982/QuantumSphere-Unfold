"""k235: Zufallsabschaetzung der Treffer von gamma_L (Methoden_Notiz.md, Commit 8557ed7). Erkundung, nicht blind.

Teil A: belegte Auswahlzahlen je Treffer, Poisson-Binomial.
Teil B: Trefferzahl ueber einen festen Zielkatalog (16 Ziele, 8 Formen, 2 sigma) fuer die 36 Paare aus k218 und fuer
        gleich- bzw. log-gleichverteiltes gamma_L auf [1,006; 3,51].
"""
import math
import numpy as np

# ---------------- Teil A ----------------
s12, s12u, s12d, s13 = 0.3088, 0.0067, 0.0066, 0.02248
w2 = (s12u + s12d) * (1 - s13)              # 2 sigma Breite (1 sigma beidseitig) von |U_e2|^2 auf [0,1]
pA = {
    "Omega_M = beta^2 (26 Lesarten, w 0,049)": 1 - 0.951 ** 26,
    f"|U_e2|^2 = beta^2 (10 Konstanten, w {w2:.4f})": 1 - (1 - w2) ** 10,
    "cot theta_W = gamma_L (H15)": 0.17,
    "Phi_e = pi/4 - gamma_M/2 (H102, 0,34 erwartet)": 1 - math.exp(-0.34),
}
print("TEIL A: belegte Auswahl je Treffer")
for k, v in pA.items():
    print(f"  {k:52s} p = {v:.3f}")
ps = list(pA.values())
dist = np.array([1.0])
for p in ps:
    dist = np.convolve(dist, [1 - p, p])
print(f"  Summe p (erwartete Zufallstreffer) = {sum(ps):.2f}; Produkt = P(4 von 4) = {np.prod(ps):.4f}; P(>=3) = {dist[3:].sum():.3f}")

# ---------------- Teil B ----------------
J = np.arange(1, 801)  # k = 2j
A = np.sqrt(J / 2 * (J / 2 + 1))
SPINS = {"A": J, "H": J[0::2], "I": J[1::2], "S1/2": np.array([1]), "S1": np.array([2])}
WEIGHTS = {"g=2": lambda k: 2.0 * np.ones_like(k, float), "g=2j+1": lambda k: k + 1.0}


def solve(ks, w):
    a = np.sqrt(ks / 2 * (ks / 2 + 1)); g_ = w(ks)
    f = lambda x: np.sum(g_ * np.exp(-2 * np.pi * x * a)) - 1
    if f(1e-9) <= 0:
        return None
    lo, hi = 1e-9, 5.0
    if f(hi) > 0:
        return None
    for _ in range(200):
        m = 0.5 * (lo + hi)
        lo, hi = (m, hi) if f(m) > 0 else (lo, m)
    return 0.5 * (lo + hi)


rules = {}
for sn, ks in SPINS.items():
    for wn, w in WEIGHTS.items():
        g = solve(ks, w)
        if g is None or any(abs(g - h) < 1e-12 for h in rules.values()):
            continue
        rules[f"{sn},{wn}"] = g
pairs = {(m, t): rules[m] / rules[t] for m in rules for t in rules if m != t and rules[m] > rules[t]}
print(f"\nTEIL B: {len(rules)} Regeln, {len(pairs)} Paare; gamma_L von {min(pairs.values()):.3f} bis {max(pairs.values()):.3f}")

mW, smW, mZ = 80.3692, 0.0133, 91.1880
cot = mW / math.sqrt(mZ ** 2 - mW ** 2)
scot = smW * mZ ** 2 / (mZ ** 2 - mW ** 2) ** 1.5
TARGETS = [  # Name, Wert, sigma_oben, sigma_unten
    ("sin2 t12", 0.3088, 0.0067, 0.0066), ("sin2 t23", 0.470, 0.017, 0.014), ("sin2 t13", 0.02248, 0.00056, 0.00056),
    ("dm21/dm31", 0.03002, 0.00046, 0.00046), ("cot tW onshell", cot, scot, scot), ("sin2 tW MSbar", 0.23129, 4e-5, 4e-5),
    ("mH/mZ", 1.3730, 0.0012, 0.0012), ("mt/mW", 2.1472, 0.0037, 0.0037), ("mmu/mtau", 0.059464, 4e-6, 4e-6),
    ("alpha_s", 0.1180, 0.0009, 0.0009), ("|Vus|", 0.2243, 0.0008, 0.0008), ("|Vcb|", 0.0408, 0.0014, 0.0014),
    ("|Vub|", 0.00382, 0.0002, 0.0002), ("Omega_m DESI", 0.2975, 0.0086, 0.0086), ("n_s", 0.9649, 0.0042, 0.0042),
    ("Omega_b h2", 0.02237, 0.00015, 0.00015),
]
FORMS = ["beta", "beta2", "1/beta", "gL", "1/gL", "e^eta", "e^-eta", "eta"]
tv = np.array([t[1] for t in TARGETS]); tu = np.array([t[2] for t in TARGETS]); td = np.array([t[3] for t in TARGETS])


def forms(gl):
    gl = np.atleast_1d(np.asarray(gl, float))
    b = np.sqrt((gl - 1) / (gl + 1)); eta = np.arctanh(b)
    return np.stack([b, b * b, 1 / b, gl, 1 / gl, np.exp(eta), np.exp(-eta), eta], axis=1)  # (n, 8)


def hits(gl):
    F = forms(gl)[:, :, None]                     # (n, 8, 1)
    d = F - tv[None, None, :]
    s = np.where(d > 0, tu, td)[None, None, :] if False else np.where(d > 0, tu[None, None, :], td[None, None, :])
    hit = np.abs(d) <= 2 * s                      # (n, 8, 16)
    return hit.any(axis=1)                        # Ziel getroffen durch irgendeine Form, (n, 16)


DL = ("A,g=2", "S1/2,g=2")
names = list(pairs); gls = np.array([pairs[p] for p in names])
H = hits(gls); n = H.sum(axis=1)
i0 = names.index(DL); nobs = int(n[i0])
print(f"DL/ABCK: gamma_L = {gls[i0]:.6f}, Treffer n_obs = {nobs}: {[TARGETS[j][0] for j in np.where(H[i0])[0]]}")
# welche Form trifft welches Ziel bei DL/ABCK
F0 = forms(gls[i0])[0]
for j in np.where(H[i0])[0]:
    fs = [FORMS[f] for f in range(8) if abs(F0[f] - tv[j]) <= 2 * (tu[j] if F0[f] > tv[j] else td[j])]
    z = [(F0[f] - tv[j]) / (tu[j] if F0[f] > tv[j] else td[j]) for f in range(8) if FORMS[f] in fs]
    print(f"   {TARGETS[j][0]:15s} durch {fs} (z {', '.join(f'{x:+.2f}' for x in z)})")
cnt = np.bincount(n, minlength=6)
print(f"Verteilung der Trefferzahl ueber die {len(names)} Paare: " + ", ".join(f"{k}: {c}" for k, c in enumerate(cnt) if c))
print(f"Paare mit n >= {nobs}: {int((n >= nobs).sum())} -> " + "; ".join(f"{names[i][0]}/{names[i][1]} ({n[i]})" for i in np.where(n >= nobs)[0]))

rng = np.random.default_rng(235)
lo, hi = 1.006, 3.51
for lab, sample in (("gleichverteilt", rng.uniform(lo, hi, 200000)),
                    ("log-gleichverteilt", np.exp(rng.uniform(math.log(lo), math.log(hi), 200000)))):
    nn = hits(sample).sum(axis=1)
    P = (nn >= nobs).mean(); P1 = (nn >= 1).mean(); mean = nn.mean()
    print(f"Ensemble {lab:19s}: mittlere Trefferzahl {mean:.3f}, P(n>=1) {P1:.3f}, P(n>={nobs}) {P:.5f}, 36*P = {36*P:.3f}")
    # Anteil je Ziel
    if lab == "gleichverteilt":
        per = hits(sample).mean(axis=0)
        print("   Trefferanteil je Ziel: " + ", ".join(f"{TARGETS[j][0]} {per[j]:.4f}" for j in range(len(TARGETS)) if per[j] > 0))
