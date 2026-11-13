"""Erkundung: zeitlicher Verlauf der NuFIT-Bestwerte (dm21, dm31 in NO, R = dm21/dm31) mit Ausgleichskurven.

Quelle: Parametertabellen v1.0 bis v6.1 auf nu-fit.org (vXY.tbl-parameters.pdf), abgelesen am 13.11.2026.
Spaltenwahl: v1.x "Free Fluxes + RSBL" (NO-Wert ist dort teils ein Nebenminimum, Fehler aus 3-sigma-Bereich/6);
v2.1 Variante LEM; ab v4.0 "with SK atmospheric data" (ab v6.0 IC24 with SK). Asymmetrische Fehler gemittelt.
Datum = "data available in" der jeweiligen Version.

Aufruf: python nufit_verlauf_2026_11_13.py [ausgabe.png]
"""
import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Version, Jahr+Monat, dm21 [1e-5], -s, +s, dm31 NO [1e-3], -s, +s
DATA = [
    ("1.0", 2012.5, 7.50, .19, .18, 2.473, .067, .070),
    ("1.1", 2013.2, 7.45, .16, .19, 2.421, .023, .022),
    ("1.2", 2013.7, 7.45, .16, .19, 2.417, .063, .063),   # Nebenminimum, sigma aus 3-sigma-Bereich
    ("1.3", 2014.5, 7.50, .17, .19, 2.458, .046, .046),   # Nebenminimum, sigma aus 3-sigma-Bereich
    ("2.0", 2014.7, 7.50, .17, .19, 2.457, .047, .047),
    ("2.1", 2016.4, 7.49, .17, .19, 2.484, .048, .045),
    ("2.2", 2016.6, 7.49, .17, .19, 2.526, .037, .039),
    ("3.0", 2016.9, 7.50, .17, .19, 2.524, .040, .039),
    ("3.1", 2017.9, 7.40, .20, .21, 2.515, .035, .035),
    ("3.2", 2018.0, 7.40, .20, .21, 2.494, .031, .033),
    ("4.0", 2018.9, 7.39, .20, .21, 2.525, .031, .033),
    ("4.1", 2019.5, 7.39, .20, .21, 2.528, .031, .029),
    ("5.0", 2020.5, 7.42, .20, .21, 2.517, .028, .026),
    ("5.1", 2021.8, 7.42, .20, .21, 2.510, .027, .027),
    ("5.2", 2022.9, 7.41, .20, .21, 2.507, .027, .026),
    ("5.3", 2024.2, 7.41, .20, .21, 2.505, .026, .024),
    ("6.0", 2024.7, 7.49, .19, .19, 2.513, .019, .021),
    ("6.1", 2025.9, 7.537, .10, .094, 2.511, .020, .021),
]
R_PRED = 0.030839          # H99
JUNO = (2025.9, 7.50, 0.12)  # JUNO allein, 59,1 Tage

ver = [d[0] for d in DATA]
t = np.array([d[1] for d in DATA])
d21 = np.array([d[2] for d in DATA]); s21 = np.array([(d[3] + d[4]) / 2 for d in DATA])
d31 = np.array([d[5] for d in DATA]); s31 = np.array([(d[6] + d[7]) / 2 for d in DATA])
R = d21 / d31 * 1e-2
sR = R * np.hypot(s21 / d21, s31 / d31)
T0 = 2012.5


def wmean(y, s):
    w = 1 / s ** 2
    m = (w * y).sum() / w.sum()
    return m, np.sqrt(1 / w.sum())


def fits(x, y, s):
    """Konstante, Gerade, exponentielle Annaeherung; gewichtet. Rueckgabe: dict name -> (f, popt, pcov, chi2, k)."""
    out = {}
    lin = lambda x, a, b: a + b * (x - 2020)
    expo = lambda x, inf, amp, tau: inf + amp * np.exp(-(x - T0) / tau)
    const = lambda x, a: a + 0 * x
    big = np.inf
    for name, f, p0, bd in (("konstant", const, [y.mean()], (-big, big)),
                            ("linear", lin, [y.mean(), 0], (-big, big)),
                            ("exponentiell", expo, [y[-1], y[0] - y[-1], 4], ([-big, -big, 0.3], [big, big, 50]))):
        try:
            popt, pcov = curve_fit(f, x, y, p0=p0, sigma=s, absolute_sigma=True, bounds=bd, maxfev=20000)
        except RuntimeError:
            continue
        chi2 = (((f(x, *popt) - y) / s) ** 2).sum()
        out[name] = (f, popt, pcov, chi2, len(popt))
    return out


def band(f, popt, pcov, xs, n=4000, seed=1):
    rng = np.random.default_rng(seed)
    P = rng.multivariate_normal(popt, pcov, n)
    Y = np.array([f(xs, *p) for p in P])
    return np.percentile(Y, [16, 84], axis=0)


def report(label, y, s, unit):
    print(f"\n== {label} ({unit})")
    m, sm = wmean(y, s)
    print(f"gewichtetes Mittel aller Versionen: {m:.5g} +- {sm:.2g} (Versionen nicht unabhaengig!)")
    res = fits(t, y, s)
    for name, (f, popt, pcov, chi2, k) in res.items():
        aic = chi2 + 2 * k
        pr = [f"{f(np.array([yy]), *popt)[0]:.5g}" for yy in (2027, 2030)]
        print(f"{name:13s} chi2/ndf = {chi2:.2f}/{len(y) - k}, AIC = {aic:.2f}, Parameter {np.round(popt, 5)}, "
              f"Wert 2027: {pr[0]}, 2030: {pr[1]}")
    return res


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "nufit_verlauf_2026_11_13.png"
    r21 = report("dm21", d21, s21, "1e-5 eV^2")
    r31 = report("dm31 NO", d31, s31, "1e-3 eV^2")
    rR = report("R = dm21/dm31", R, sR, "1")
    print(f"\nH99: R_pred = {R_PRED}; R(6.1) = {R[-1]:.6f} +- {sR[-1]:.6f}")

    INK, MUTED, DATA_C, FIT_C, PRED_C = "#1f2328", "#6e7781", "#2f5d9e", "#8a8f98", "#c2571a"
    xs = np.linspace(2012, 2031, 400)
    fig, axes = plt.subplots(3, 1, figsize=(9, 11), sharex=True)
    panels = [(axes[0], d21, s21, r21, r"$\Delta m^2_{21}$ [$10^{-5}$ eV$^2$]", "linear"),
              (axes[1], d31, s31, r31, r"$\Delta m^2_{31}$ (NO) [$10^{-3}$ eV$^2$]", "exponentiell"),
              (axes[2], R, sR, rR, r"$R=\Delta m^2_{21}/\Delta m^2_{31}$", "linear")]
    for ax, y, s, res, lab, pick in panels:
        ax.errorbar(t, y, yerr=s, fmt="o", ms=5, color=DATA_C, ecolor=DATA_C, elinewidth=1.2, capsize=0,
                    label="NuFIT-Bestwert ±1σ", zorder=3)
        name = pick if pick in res else "linear"
        f, popt, pcov, chi2, k = res[name]
        lo, hi = band(f, popt, pcov, xs)
        ax.plot(xs, f(xs, *popt), color=FIT_C, lw=2, label=f"Ausgleich ({name}, gewichtet)")
        ax.fill_between(xs, lo, hi, color=FIT_C, alpha=0.18, lw=0, label="±1σ der Ausgleichskurve")
        m, _ = wmean(y, s)
        ax.axhline(y[-1], color=DATA_C, lw=1, ls=":", label="Stand v6.1 (Martingal-Erwartung)")
        ax.set_ylabel(lab, color=INK)
        ax.grid(axis="y", color="#e6e8eb", lw=0.8)
        for sp in ("top", "right"):
            ax.spines[sp].set_visible(False)
        ax.tick_params(colors=MUTED)
        ax.axvspan(2025.95, 2031, color="#f3f4f6", lw=0, zorder=0)
    axes[0].errorbar([JUNO[0] + 0.15], [JUNO[1]], yerr=[JUNO[2]], fmt="s", ms=5, color=MUTED, ecolor=MUTED,
                     label="JUNO allein (59 Tage)", zorder=3)
    axes[0].axhline(R_PRED * 100 * d31[-1], color=PRED_C, lw=1.6, ls="--",
                    label=f"H99 verlangt {R_PRED * 100 * d31[-1]:.3f} (mit Δm²₃₁ v6.1)")
    axes[2].axhline(R_PRED, color=PRED_C, lw=1.6, ls="--", label=f"H99: R = {R_PRED}")
    for i, v in enumerate(ver):
        if v in ("1.0", "3.1", "6.0", "6.1"):
            axes[0].annotate("v" + v, (t[i], d21[i] + s21[i]), textcoords="offset points", xytext=(0, 4),
                             ha="center", fontsize=8, color=MUTED)
    for ax in axes:
        lo_, hi_ = ax.get_ylim()
        ax.set_ylim(lo_ - 0.42 * (hi_ - lo_), hi_)
        ax.legend(fontsize=8, frameon=False, loc="lower left", ncol=2)
        ax.set_xticks(range(2012, 2032, 2))
    axes[2].set_xlabel("Datenstand der NuFIT-Version (Jahr)", color=INK)
    axes[2].text(2028.5, axes[2].get_ylim()[1], "Extrapolation", ha="center", va="top", fontsize=8, color=MUTED)
    fig.suptitle("NuFIT-Bestwerte 2012–2025 (normale Ordnung) mit Ausgleichskurven", color=INK, fontsize=12)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
    print("Grafik:", out)
