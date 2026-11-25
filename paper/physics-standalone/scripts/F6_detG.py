#!/usr/bin/env python3
"""F6: det G = (sqrt2 cos(phi) - 1)/2 for three states with pairwise overlap 1/2, and the three Gram roots.

Writes figures/F6-detG.pdf and figures/F6-detG.txt.  Each closed form is checked against the
numerical determinant / spectrum of the circulant Gram matrix
G(phi) = I + (e^{i phi/3} U + e^{-i phi/3} U^*)/sqrt2 (Companion v4.10.0-r14.5, r15.3, r25.3).
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "figures"
OUT.mkdir(exist_ok=True)
C_EST = "#3A7A3A"; C_COND = "#A08000"; C_REF = "#9A3030"; C_READ = "#55559A"; C_GREY = "#888888"

U = np.roll(np.eye(3), 1, axis=1)


def G(phi):
    return np.eye(3) + (np.exp(1j * phi / 3) * U + np.exp(-1j * phi / 3) * U.conj().T) / np.sqrt(2)


def detG(phi):
    return (np.sqrt(2) * np.cos(phi) - 1) / 2


def roots(phi):
    return np.array([1 + np.sqrt(2) * np.cos(phi / 3 + 2 * np.pi * k / 3) for k in range(3)])


def main():
    log = []
    grid = np.linspace(0, np.pi / 2, 401)
    err_det = max(abs(np.linalg.det(G(p)).real - detG(p)) for p in grid)
    err_ev = max(np.max(abs(np.sort(np.linalg.eigvalsh(G(p))) - np.sort(roots(p)))) for p in grid)
    err_bar = max(abs(np.angle(G(p)[0, 1] * G(p)[1, 2] * G(p)[2, 0]) - p) for p in grid[1:])
    log.append(f"max |det - closed form| on [0, pi/2]: {err_det:.2e}")
    log.append(f"max |eigenvalues - 1+sqrt2 cos(phi/3+2pi k/3)|: {err_ev:.2e}")
    log.append(f"max |Bargmann phase - phi|: {err_bar:.2e}")
    # zero
    from scipy.optimize import brentq  # noqa: E402
    z = brentq(detG, 0.5, 1.0, xtol=1e-15)
    log.append(f"zero of det G: {z:.15f}, pi/4 = {np.pi/4:.15f}")
    for name, p in (("phi=0", 0.0), ("leptons phi=2/3", 2 / 3), ("spin-1 triangle", 0.679042), ("flat octant pi/4", np.pi / 4)):
        r = np.sort(roots(p))
        K = np.sum(r ** 2) / np.sum(r) ** 2
        ratio = r / r[0] if r[0] > 1e-12 else None
        log.append(f"{name}: det G {detG(p):.6f}, roots {np.round(r, 6)}, K {K:.12f}, root ratios {None if ratio is None else np.round(ratio, 2)}")
    log.append(f"bend pi/4 - 2/3 = {np.pi/4 - 2/3:.6f}")

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.9))
    ph = np.linspace(0, np.pi / 2, 400)
    a1.axhline(0, color=C_GREY, lw=0.6)
    a1.axvspan(np.pi / 4, np.pi / 2, color=C_REF, alpha=0.08)
    a1.plot(ph[ph <= np.pi / 4], detG(ph[ph <= np.pi / 4]), color=C_EST, lw=1.8)
    a1.plot(ph[ph >= np.pi / 4], detG(ph[ph >= np.pi / 4]), color=C_REF, lw=1.2, ls="--")
    a1.plot([np.pi / 4], [0], "o", color="black", ms=4)
    a1.annotate(r"$\varphi=\pi/4$: flat octant," "\n" r"$\det G=0$, one mass zero", (np.pi / 4, 0), (0.86, 0.12),
                fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.5))
    a1.plot([2 / 3], [detG(2 / 3)], "s", color=C_COND, ms=4)
    a1.annotate(r"$\varphi=2/3$ (charged leptons)", (2 / 3, detG(2 / 3)), (0.05, -0.09), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", lw=0.5))
    a1.text(1.0, -0.11, "not a Gram matrix", color=C_REF, fontsize=7.5)
    a1.text(0.03, 0.17, "three positive masses", color=C_EST, fontsize=7.5)
    a1.set_xlabel(r"Bargmann phase $\varphi$")
    a1.set_ylabel(r"$\det G=\frac{1}{2}(\sqrt{2}\cos\varphi-1)$")
    a1.set_xticks([0, np.pi / 8, np.pi / 4, 3 * np.pi / 8, np.pi / 2])
    a1.set_xticklabels(["0", r"$\pi/8$", r"$\pi/4$", r"$3\pi/8$", r"$\pi/2$"])
    a1.set_xlim(0, np.pi / 2); a1.set_ylim(-0.22, 0.24)
    a1.set_title("(a) determinant", fontsize=9)

    ph2 = np.linspace(0, np.pi / 4, 300)
    R = np.array([roots(p) for p in ph2])
    for k, c in zip(range(3), (C_EST, C_READ, C_COND)):
        a2.plot(ph2, R[:, k], color=c, lw=1.5, label=rf"$\lambda_{k}$")
    a2.axvline(2 / 3, color=C_COND, lw=0.6, ls=":")
    a2.axvline(np.pi / 4, color="black", lw=0.6, ls=":")
    a2.set_xlabel(r"$\varphi$")
    a2.set_ylabel(r"roots $\lambda_k=1+\sqrt{2}\cos(\frac{\varphi}{3}+\frac{2\pi k}{3})$", fontsize=8)
    a2.set_xticks([0, np.pi / 8, 2 / 3, np.pi / 4])
    a2.set_xticklabels(["0", r"$\pi/8$", r"$\frac{2}{3}$", r"$\frac{\pi}{4}$"])
    a2.set_xlim(0, np.pi / 4 + 0.02); a2.set_ylim(-0.05, 2.6)
    a2.legend(fontsize=7.5, frameon=False, loc="center left")
    a2.set_title(r"(b) $\sqrt{m}$ up to scale, $K=2/3$ throughout", fontsize=9)
    for a in (a1, a2):
        a.tick_params(labelsize=7.5)
        for sp in ("top", "right"):
            a.spines[sp].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "F6-detG.pdf")
    (OUT / "F6-detG.txt").write_text("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
