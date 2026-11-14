"""Backward search: which equal-weight terms select the Koide reference?

Erkundung, nicht blind (target state, 2/3 and pi/4 known beforehand).
Run from the repository root:
    python notes/research/op3_action_balance_search_2026_11_14/search.py --out PATH

Part 1: which slot symmetries can tie the coefficients of Q and R?
Part 2: exhaustive search over sums of the 12 eigenprojectors of the four
        cyclic subgroups <D>, <tau>, <tau D>, <tau D^2> of the Weyl group,
        weights in {0,1} (H = -sum P) and in {-1,0,1}.
Part 3: exact check of the single-site clock reading H = -J(Z+Z^+) - h(X+X^+).
"""
import argparse
import itertools
import json
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp

W = np.exp(2j * np.pi / 3)
TAU = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex)
D = np.diag([1, W, W**2])
GENS = {"D": D, "tau": TAU, "tauD": TAU @ D, "tauD2": TAU @ D @ D}
TOL = 1e-9


def eigenlines(U):
    """Projectors onto the eigenlines of an order-3 unitary, keyed by k (eigenvalue w^k)."""
    out = {}
    for k in range(3):
        lam = W**k
        P = sum(np.linalg.matrix_power(np.conj(lam) * U, j) for j in range(3)) / 3
        assert np.allclose(P @ P, P) and abs(np.trace(P) - 1) < 1e-12
        out[k] = P
    return out


PROJ = [(g, k, P) for g, U in GENS.items() for k, P in eigenlines(U).items()]


def s_op(slot):
    e = np.zeros(3)
    e[slot] = 1
    return W * np.eye(3) + (1 - W) * np.outer(e, e)


def orbit_data(psi):
    """K_orb and Bargmann phase for each choice of the distinguished slot of S."""
    res = []
    for slot in range(3):
        d = np.vdot(psi, s_op(slot) @ psi)
        K = (1 + 2 * abs(d) ** 2) / 3
        res.append((slot, K, float(np.angle(d**3))))
    return res


def ground(H):
    vals, vecs = np.linalg.eigh(H)
    gap = vals[1] - vals[0]
    return gap, vecs[:, 0]


def classify(weights):
    H = -sum(w * P for w, (_, _, P) in zip(weights, PROJ) if w)
    gap, psi = ground(H)
    if gap < TOL:
        return None
    hits = [(s, ph) for s, K, ph in orbit_data(psi) if abs(K - 2 / 3) < TOL]
    return hits or None


def part1():
    """Monomial matrices with sixth-root phases: images of <D> under conjugation."""
    phases = [np.exp(2j * np.pi * m / 6) for m in range(6)]
    subgroups = {name: [np.linalg.matrix_power(U, j) for j in (1, 2)] for name, U in GENS.items()}

    def which(V):
        for name, els in subgroups.items():
            for E in els:
                c = np.vdot(E.flatten(), V.flatten()) / 3
                if abs(abs(c) - 1) < 1e-9 and np.allclose(V, c * E):
                    return name
        return "other"

    images = Counter()
    count = 0
    for perm in itertools.permutations(range(3)):
        Pm = np.eye(3)[list(perm)]
        for ph in itertools.product(phases, repeat=3):
            M = np.diag(ph) @ Pm
            count += 1
            images[(which(M @ D @ M.conj().T), which(M @ TAU @ M.conj().T))] += 1
    return {"group_order": count, "images_of_(D,tau)": {f"{a}|{b}": n for (a, b), n in images.items()}}


def part2():
    out = {}
    for label, alphabet in (("weights_0_1", (0, 1)), ("weights_-1_0_1", (-1, 0, 1))):
        hits = []
        for w in itertools.product(alphabet, repeat=12):
            if not any(w):
                continue
            h = classify(w)
            if h:
                hits.append((w, h))
        groups_used = Counter()
        for w, _ in hits:
            used = tuple(sorted({PROJ[i][0] for i, x in enumerate(w) if x}))
            groups_used[used] += 1
        smallest = sorted(hits, key=lambda t: sum(abs(x) for x in t[0]))[:12]
        out[label] = {
            "n_hits": len(hits),
            "subgroups_used": {"+".join(k): v for k, v in sorted(groups_used.items())},
            "smallest": [{"terms": [f"{'+' if x > 0 else '-'}P[{PROJ[i][0]},w^{PROJ[i][1]}]"
                                    for i, x in enumerate(w) if x],
                          "slot_phase": [(s, round(ph / np.pi, 6)) for s, ph in h]} for w, h in smallest],
        }
    return out


def part3():
    J, h = sp.symbols("J h", positive=True)
    w = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2
    Z = sp.diag(1, w, w**2)
    X = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    Q = sp.diag(1, 0, 0)
    R = sp.ones(3, 3) / 3
    H = -J * (Z + Z.H) - h * (X + X.H)
    rhs = -3 * J * Q - 3 * h * R + (J + h) * sp.eye(3)
    assert (H - rhs).applyfunc(sp.simplify) == sp.zeros(3)
    F = sp.Matrix(3, 3, lambda a, b: w ** (a * b)) / sp.sqrt(3)
    swap = (F * Z * F.H - X).applyfunc(sp.simplify) == sp.zeros(3) or \
        (F * Z * F.H - X.H).applyfunc(sp.simplify) == sp.zeros(3)
    v = sp.Matrix([1 + sp.sqrt(3), 1, 1])
    Hb = H.subs(h, J)
    lam = sp.simplify((v.H * Hb * v)[0] / (v.H * v)[0])
    assert (Hb * v - lam * v).applyfunc(sp.simplify) == sp.zeros(3, 1)
    eig = sorted(sp.Matrix(Hb / J).eigenvals().keys(), key=lambda x: float(x))
    return {"H_equals_-3JQ-3hR+(J+h)I": True, "F_maps_Z_to_X_or_Xdag": bool(swap),
            "balanced_ground_state": "(1+sqrt3,1,1)", "eigenvalues_over_J": [str(sp.nsimplify(e)) for e in eig],
            "ground_eigenvalue_over_J": str(sp.simplify(lam / J))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    result = {"part1_monomial_symmetries": part1(), "part2_projector_sums": part2(),
              "part3_clock_reading": part3()}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=1, ensure_ascii=False), encoding="utf-8")
    p1 = result["part1_monomial_symmetries"]
    print("Part 1: order", p1["group_order"], "images", p1["images_of_(D,tau)"])
    for k, v in result["part2_projector_sums"].items():
        print("Part 2", k, "hits", v["n_hits"], "subgroups", v["subgroups_used"])
        for s in v["smallest"][:6]:
            print("   ", s)
    print("Part 3:", result["part3_clock_reading"])


if __name__ == "__main__":
    main()
