"""F7: frame offset beta for the 36 counting-rule pairs of H98 (Companion round v4.10.0-r09.1).

Recomputes the rule space of notes/research/v4_10_0_r09/llm/k218_regelraum_paare.py in double precision
(the original uses mpmath with 30 digits; the printed values agree to the digits shown in k218_out.txt) and
writes figures/F7-counting-pairs.pdf.  Run from anywhere:  python3 F7_counting_pairs.py
Inputs (all from k218): a(j) = sqrt(j(j+1)); rules = spin range x weight; pairs with gamma_M > gamma_T;
gamma_L = gamma_M/gamma_T; beta = sqrt((gamma_L-1)/(gamma_L+1)); m_W = m_Z gamma_L/sqrt(1+gamma_L^2); Omega_M = beta^2.
Windows: lepton beta in [0.545, 0.570] (v4.9.0-r61); m_W 2 sigma of PDG 2025 (80.3692 +- 0.0133 GeV);
Omega_M 2 sigma of DESI DR2 BAO (0.2975 +- 0.0086).
"""
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "figures" / "F7-counting-pairs.pdf"

JMAX = 4000
k = np.arange(1, 2 * JMAX + 1)            # k = 2j
a = np.sqrt(k / 2 * (k / 2 + 1))
SPINS = {"A": k >= 1, "H": k % 2 == 1, "I": (k % 2 == 0), "S1/2": k == 1, "S1": k == 2}
WEIGHTS = {"2": lambda kk: 2.0 * np.ones_like(kk, dtype=float), "2j+1": lambda kk: kk + 1.0}


def solve(mask, w):
    kk, aa = k[mask], a[mask]
    ww = w(kk)
    if len(kk) == 1 and ww[0] <= 1:
        return None
    f = lambda g: np.sum(ww * np.exp(-2 * np.pi * g * aa)) - 1
    return brentq(f, 1e-4, 5.0, xtol=1e-15)


rules = {}
for sn, m in SPINS.items():
    for wn, w in WEIGHTS.items():
        g = solve(m, w)
        if g is None or any(abs(g - h) < 1e-12 for h in rules.values()):
            continue
        rules[f"{sn},{wn}"] = g

mZ, mW0, smW = 91.1880, 80.3692, 0.0133
Om0, sOm = 0.2975, 0.0086
pairs = []
for nm, gm in rules.items():
    for nt, gt in rules.items():
        if gm <= gt:
            continue
        gl = gm / gt
        b = np.sqrt((gl - 1) / (gl + 1))
        pairs.append((nm, nt, gl, b))
pairs.sort(key=lambda p: p[2])


def beta_of_gl(gl):
    return np.sqrt((gl - 1) / (gl + 1))


def gl_of_mw(m):
    return m / np.sqrt(mZ ** 2 - m ** 2)


win_lep = (0.545, 0.570)
win_mw = tuple(beta_of_gl(gl_of_mw(m)) for m in (mW0 - 2 * smW, mW0 + 2 * smW))
win_om = (np.sqrt(Om0 - 2 * sOm), np.sqrt(Om0 + 2 * sOm))

print("rules:")
for n, g in rules.items():
    print(f"  {n:10s} gamma = {g:.12f}")
print(f"pairs: {len(pairs)}")
print(f"beta windows: lepton {win_lep}, m_W ({win_mw[0]:.5f}, {win_mw[1]:.5f}), Omega_M ({win_om[0]:.5f}, {win_om[1]:.5f})")
hits = []
for nm, nt, gl, b in pairs:
    hl = win_lep[0] <= b <= win_lep[1]
    hw = win_mw[0] <= b <= win_mw[1]
    ho = win_om[0] <= b <= win_om[1]
    if hl or hw or ho:
        print(f"  {nm:10s} / {nt:10s} gamma_L = {gl:.6f} beta = {b:.5f}  L{int(hl)} W{int(hw)} O{int(ho)}")
    if hl and hw and ho:
        hits.append((nm, nt))
print("all three:", hits)
assert len(pairs) == 36 and hits == [("A,2", "S1/2,2")]

# ---------------------------------------------------------------- figure (plain 2D)
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.linewidth": 0.6,
                     "xtick.major.width": 0.6, "ytick.major.width": 0.6})
C_LEP, C_MW, C_OM = "#A08000", "#9A3030", "#3A6A9A"
C_DOT, C_SEL, C_SU2 = "#555555", "#3A7A3A", "#B0601A"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.75), gridspec_kw={"width_ratios": [1.35, 1]})
idx = np.arange(1, len(pairs) + 1)
betas = np.array([p[3] for p in pairs])
sel = [i for i, p in enumerate(pairs) if (p[0], p[1]) == ("A,2", "S1/2,2")][0]
su2 = [i for i, p in enumerate(pairs) if (p[0], p[1]) == ("A,2j+1", "S1/2,2")][0]

for ax in (ax1, ax2):
    ax.axhspan(*win_om, color=C_OM, alpha=0.18, lw=0)
    ax.axhspan(*win_lep, color=C_LEP, alpha=0.22, lw=0)
    ax.axhspan(*win_mw, color=C_MW, alpha=0.55, lw=0)
    ax.plot(idx, betas, "o", ms=3.2, color=C_DOT, mfc="white", mew=0.8, zorder=3)
    ax.plot(idx[sel], betas[sel], "o", ms=5, color=C_SEL, zorder=4)
    ax.plot(idx[su2], betas[su2], "s", ms=4.2, color=C_SU2, zorder=4)

ax1.set_xlim(0, 37)
ax1.set_ylim(0, 0.78)
ax1.set_xlabel(r"pair, ordered by $\gamma_L=\gamma_M/\gamma_T$")
ax1.set_ylabel(r"$\beta=\sqrt{(\gamma_L-1)/(\gamma_L+1)}$")
ax1.set_title("(a) all 36 pairs of the rule space", fontsize=9)
ax1.annotate("DL/M + ABCK", (idx[sel], betas[sel]), xytext=(12, 0.70), fontsize=8, color=C_SEL,
             arrowprops=dict(arrowstyle="-", lw=0.6, color=C_SEL))
ax1.annotate("SU(2) count for M", (idx[su2], betas[su2]), xytext=(11, 0.10), fontsize=8, color=C_SU2,
             arrowprops=dict(arrowstyle="-", lw=0.6, color=C_SU2))

ax2.set_xlim(23.5, 31.5)
ax2.set_ylim(0.50, 0.62)
ax2.set_xlabel("pair (zoom)")
ax2.set_title("(b) the three data windows", fontsize=9)
ax2.text(23.8, 0.5665, r"lepton window", fontsize=7.5, color="#6A5500")
ax2.text(27.4, 0.5320, r"$\Omega_M$, DESI DR2, $2\sigma$", fontsize=7.5, color="#2A4A7A")
ax2.annotate(r"$m_W$, PDG 2025, $2\sigma$", xy=(28.4, 0.5494), xytext=(28.6, 0.585), fontsize=7.5, color=C_MW,
             arrowprops=dict(arrowstyle="-", lw=0.6, color=C_MW))
ax2.set_xticks(range(24, 32))
for ax in (ax1, ax2):
    ax.tick_params(labelsize=8)
fig.tight_layout(w_pad=1.2)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT)
print("wrote", OUT.relative_to(HERE.parent).as_posix())
