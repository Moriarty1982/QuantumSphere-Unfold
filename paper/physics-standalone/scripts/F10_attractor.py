"""F10: cascade with attractor Omega_M = beta^2 (H124, Companion round v4.10.0-r57) against flat LambdaCDM.

Uses the data and model code of the H97/H124 tests unchanged:
  notes/research/v4_10_0_r05/llm/k216_bruecke_desi_dr2.py  (13 DESI DR2 BAO values, arXiv:2503.14738, chi^2 with free h r_d)
and repeats the fits of notes/research/op5_attractor_2026_11_23/k243_test_h124.py (output k243_out_teilB.txt):
  LambdaCDM: Omega_m = 0.2970, h r_d = 101.56 Mpc, chi^2 = 10.55
  cascade eps = 3: Omega_M0 = 0.5006, h r_d = 95.49 Mpc, chi^2 = 18.42, p(11) = 0.072
Model (r57.1): flat, d rho_M/dN = -3 rho_M + eps beta^2 rho_V, d rho_V/dN = -eps beta^2 rho_V, radiation passive (Omega_r = 9.1e-5).
Writes figures/F10-attractor.pdf.  Run:  python3 -I F10_attractor.py
"""
from pathlib import Path
import importlib.util, io, contextlib
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
OUT = HERE.parent / "figures" / "F10-attractor.pdf"

src = REPO / "notes" / "research" / "v4_10_0_r05" / "llm" / "k216_bruecke_desi_dr2.py"
spec = importlib.util.spec_from_file_location("k216", src)
k216 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(k216)
b2, Or = k216.b2, k216.Or

# --- fits (as k243 part B)
res = minimize_scalar(lambda o: k216.chi2_min(k216.E_lcdm(o))[0], bounds=(0.2, 0.45), method="bounded",
                      options={"xatol": 1e-6})
OmL = res.x
cL, hL = k216.chi2_min(k216.E_lcdm(OmL))
grid = np.linspace(b2 + 1e-6, 0.999, 80)
cg = [k216.chi2_min(k216.E_kaskade(o, 3.0))[0] for o in grid]
i = int(np.argmin(cg))
r = minimize_scalar(lambda o: k216.chi2_min(k216.E_kaskade(o, 3.0))[0], bounds=(grid[max(i - 1, 0)], grid[i + 1]),
                    method="bounded", options={"xatol": 1e-6})
OmK = r.x
cK, hK = k216.chi2_min(k216.E_kaskade(OmK, 3.0))
print(f"LCDM: Om = {OmL:.4f}, h r_d = {hL:.2f} Mpc, chi2 = {cL:.2f}")
print(f"cascade eps=3: Om0 = {OmK:.4f}, h r_d = {hK:.2f} Mpc, chi2 = {cK:.2f}, Delta chi2 = {cK - cL:.2f}")
assert abs(OmK - 0.5006) < 5e-4 and abs(cK - 18.42) < 0.02 and abs(cL - 10.55) < 0.02


# --- Omega_M(N), N = ln a, in past and future
def omega_cascade(Om0, eps, N):
    OL = 1 - Om0 - Or
    rhs = lambda x, y: [-3 * y[0] + b2 * eps * y[1], -b2 * eps * y[1]]
    out = np.empty_like(N)
    for sel, span in ((N <= 0, (0, N.min())), (N > 0, (0, N.max()))):
        if not sel.any():
            continue
        s = solve_ivp(rhs, span, [Om0, OL], t_eval=np.sort(N[sel])[::(-1 if span[1] < 0 else 1)],
                      rtol=1e-11, atol=1e-14)
        rm, rv = s.y
        rr = Or * np.exp(-4 * s.t)
        om = rm / (rm + rv + rr)
        order = np.argsort(s.t)
        out[sel] = np.interp(N[sel], s.t[order], om[order])
    return out


def omega_lcdm(Om0, N):
    OL = 1 - Om0 - Or
    rm, rr = Om0 * np.exp(-3 * N), Or * np.exp(-4 * N)
    return rm / (rm + rr + OL)


N = np.linspace(-np.log(1 + 3.0), 2.5, 600)
omK = omega_cascade(OmK, 3.0, N)
omL = omega_lcdm(OmL, N)

# --- BAO residuals relative to the LambdaCDM best fit (each model with its own h r_d)
fL = k216.theory(k216.E_lcdm(OmL)) * (k216.C100 / hL)
fK = k216.theory(k216.E_kaskade(OmK, 3.0)) * (k216.C100 / hK)
d = k216.d
sig = np.sqrt(np.diag(np.linalg.inv(k216.Ci)))
zs = [k216.BGS[0]] + [row[0] for row in k216.AN]
kind = ["V"] + ["M", "H"] * len(k216.AN)
zall = [zs[0]] + [z for z in zs[1:] for _ in (0, 1)]

plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.linewidth": 0.6})
C_K, C_L, C_B = "#9A3030", "#3A6A9A", "#3A7A3A"
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6.3, 2.8), gridspec_kw={"width_ratios": [1.15, 1]})
ax1.plot(N, omK, color=C_K, lw=1.3, label=r"cascade, $\varepsilon=3$ (fit)")
ax1.plot(N, omL, color=C_L, lw=1.3, ls="--", label=r"flat $\Lambda$CDM (fit)")
ax1.axhline(b2, color=C_B, lw=0.8, ls=":")
ax1.text(1.35, b2 + 0.025, r"$\beta^2=0.3018$", color=C_B, fontsize=8)
ax1.axvline(0, color="0.6", lw=0.6)
ax1.text(0.05, 0.93, "today", color="0.4", fontsize=7.5)
ax1.set_xlim(N.min(), N.max())
ax1.set_ylim(0, 1.02)
ax1.set_xlabel(r"$N=\ln a$  (past $\leftarrow\;\;\rightarrow$ future)")
ax1.set_ylabel(r"$\Omega_M$")
ax1.set_title(r"(a) matter fraction", fontsize=9)
ax1.legend(fontsize=7.5, frameon=False, loc="lower left")

mk = {"V": "D", "M": "o", "H": "s"}
lab = {"V": r"$D_V/r_d$", "M": r"$D_M/r_d$", "H": r"$D_H/r_d$"}
seen = set()
for j in range(len(d)):
    kk = kind[j]
    ax2.errorbar(zall[j], d[j] / fL[j], yerr=sig[j] / fL[j], fmt=mk[kk], ms=3.2, color="0.25", mfc="white",
                 elinewidth=0.6, capsize=1.5, label=lab[kk] if kk not in seen else None)
    seen.add(kk)
    ax2.plot(zall[j] + 0.03, fK[j] / fL[j], mk[kk], ms=3.2, color=C_K)
ax2.axhline(1, color=C_L, lw=0.9, ls="--")
ax2.set_xlabel(r"$z$")
ax2.set_ylabel(r"value / $\Lambda$CDM fit")
ax2.set_title(r"(b) DESI DR2 BAO and cascade", fontsize=9)
ax2.legend(fontsize=7, frameon=False, loc="upper right", ncol=3)
ax2.set_ylim(0.93, 1.07)
for ax in (ax1, ax2):
    ax.tick_params(labelsize=8)
fig.tight_layout(w_pad=1.0)
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT)
print("Omega_M(cascade) at N=+2.5:", round(float(omK[-1]), 4), "(attractor", round(b2, 4), ")")
print("wrote", OUT)
