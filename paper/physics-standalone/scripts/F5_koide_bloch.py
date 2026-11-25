#!/usr/bin/env python3
"""F5: flat octant (spin 1/2) against bent triangle (spin-1 coherent states), 3D view.

Writes figures/F5-koide-bloch.pdf and figures/F5-koide-bloch.txt (the checked numbers).
Sources: Companion rounds v4.10.0-r12.4(c), r14.5, r15.3, r25.3.
Usage: python3 scripts/F5_koide_bloch.py   (paths are resolved relative to this file)
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "figures"
OUT.mkdir(exist_ok=True)

C_EST = "#3A7A3A"; C_COND = "#A08000"; C_READ = "#55559A"; C_GREY = "#888888"


def gram(vs):
    return np.array([[np.vdot(a, b) for b in vs] for a in vs])


def coh_half(n):
    th = np.arccos(np.clip(n[2], -1, 1)); ph = np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def coh_one(n):
    th = np.arccos(np.clip(n[2], -1, 1)); ph = np.arctan2(n[1], n[0])
    c, s = np.cos(th / 2), np.sin(th / 2)
    return np.array([c * c, np.sqrt(2) * c * s * np.exp(1j * ph), s * s * np.exp(2j * ph)])


def report(name, vs):
    G = gram(vs)
    ov = [abs(G[i, j]) ** 2 for i, j in ((0, 1), (1, 2), (2, 0))]
    ph = np.angle(G[0, 1] * G[1, 2] * G[2, 0])
    det = np.linalg.det(G).real
    K = np.trace(G @ G).real / np.trace(G).real ** 2
    return f"{name}: overlaps {np.round(ov, 12)}, |Bargmann phase| {abs(ph):.6f}, det G {det:.6f}, K {K:.12f}"


def slerp(a, b, t):
    w = np.arccos(np.clip(a @ b, -1, 1))
    return (np.sin((1 - t) * w) * a + np.sin(t * w) * b) / np.sin(w)


def solid_angle(n):
    N = np.array(n)
    return 2 * np.arctan2(abs(np.linalg.det(N)), 1 + n[0] @ n[1] + n[1] @ n[2] + n[2] @ n[0])


def draw(ax, pts, col, labels, title, lines, show_axes=True):
    u, v = np.mgrid[0:2 * np.pi:60j, 0:np.pi:30j]
    ax.plot_wireframe(np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v),
                      color="#cccccc", linewidth=0.3, rstride=3, cstride=3)
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), 0 * t, color=C_GREY, lw=0.6)
    for e, lab in ((np.eye(3)[0], "$x$"), (np.eye(3)[1], "$y$"), (np.eye(3)[2], "$z$")):
        ax.plot([0, 1.25 * e[0]], [0, 1.25 * e[1]], [0, 1.25 * e[2]], color=C_GREY, lw=0.6, ls=":")
        ax.text(*(1.32 * e), lab, color=C_GREY, fontsize=8) if show_axes else None
    # filled spherical triangle by subdivision
    tri = []
    for k in range(3):
        a, b = pts[k], pts[(k + 1) % 3]
        tri += [slerp(a, b, s) for s in np.linspace(0, 1, 30)]
    cen = sum(pts) / np.linalg.norm(sum(pts))
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    polys = []
    for i in range(len(tri)):
        p, q = tri[i], tri[(i + 1) % len(tri)]
        polys.append([1.001 * cen, 1.001 * p, 1.001 * q])
    ax.add_collection3d(Poly3DCollection(polys, facecolor=col, alpha=0.28, edgecolor="none"))
    for k in range(3):
        arc = np.array([slerp(pts[k], pts[(k + 1) % 3], s) for s in np.linspace(0, 1, 60)])
        ax.plot(arc[:, 0], arc[:, 1], arc[:, 2], color=col, lw=1.6)
        ax.plot([0, pts[k][0]], [0, pts[k][1]], [0, pts[k][2]], color=col, lw=1.2)
        ax.scatter(*pts[k], color=col, s=18, depthshade=False)
        ax.text(*(1.12 * pts[k]), labels[k], color="black", fontsize=9)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=22, azim=35)  # fixed perspective
    ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1)
    ax.set_axis_off()
    ax.set_title(title, fontsize=10)
    ax.text2D(0.08, 0.10, "\n".join(lines), transform=ax.transAxes, fontsize=8.5, va="top")


def main():
    log = []
    # (a) flat octant: Bloch vectors +x, +y, +z of a qubit
    flat = [np.eye(3)[0], np.eye(3)[1], np.eye(3)[2]]
    log.append(report("flat octant (spin 1/2)", [coh_half(n) for n in flat]))
    log.append(f"  solid angle {solid_angle(flat):.6f} (pi/2 = {np.pi/2:.6f}); phase = Omega/2")
    # (b) spin-1 coherent triangle, symmetric about z, cos^2 psi = (2 sqrt2 - 1)/3
    psi = np.arccos(np.sqrt((2 * np.sqrt(2) - 1) / 3))
    bent = [np.array([np.sin(psi) * np.cos(2 * np.pi * k / 3), np.sin(psi) * np.sin(2 * np.pi * k / 3), np.cos(psi)])
            for k in range(3)]
    log.append(report("spin-1 triangle", [coh_one(n) for n in bent]))
    log.append(f"  psi {np.degrees(psi):.4f} deg, cos(side) {bent[0] @ bent[1]:.6f} (sqrt2-1 = {np.sqrt(2)-1:.6f}), "
               f"solid angle {solid_angle(bent):.6f}; phase = Omega for spin 1")
    fig = plt.figure(figsize=(7.2, 3.6))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    draw(ax1, flat, C_EST, [r"$+x$", r"$+y$", r"$+z$"], "(a) flat octant, spin $\\frac{1}{2}$",
         [r"$|\langle a|b\rangle|^2=\frac{1}{2}$, $\Omega=\pi/2$",
          r"$\varphi=\Omega/2=\pi/4$, $\det G=0$ (rank 2)"], show_axes=False)
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    draw(ax2, bent, C_COND, [r"$n_1$", r"$n_2$", r"$n_3$"], "(b) bent triangle, spin-1 coherent states",
         [r"$|\langle n_k|n_l\rangle|^2=\cos^4\frac{a}{2}=\frac{1}{2}$, $\cos a=\sqrt{2}-1$",
          r"$\varphi=\Omega=0.6790$, $\det G=0.0503$ (rank 3)"])
    fig.subplots_adjust(left=0.0, right=1.0, top=0.92, bottom=0.02, wspace=0.0)
    fig.savefig(OUT / "F5-koide-bloch.pdf")
    (OUT / "F5-koide-bloch.txt").write_text("\n".join(log) + "\n")
    print("\n".join(log))


if __name__ == "__main__":
    main()
