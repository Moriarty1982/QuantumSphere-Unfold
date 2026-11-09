"""Verify the eight-point compensated swap route with exact arithmetic."""

from fractions import Fraction
from itertools import combinations
import argparse


# An entry i denotes the physical swap (i, i+1 modulo 8).
OUTBOUND = (
    7, 2, 4, 2, 3, 2, 6, 5, 2, 0, 1, 4, 2, 5, 1, 2, 6, 4, 7,
    6, 4, 6, 0, 0, 0, 5, 2, 0, 4, 1, 5, 0, 3, 2, 1, 3, 6, 2,
)
INITIAL_CUT = 170
DWELL = {
    170: Fraction(13, 2), 212: 8, 232: 2, 228: 8, 184: 10, 156: 4,
    108: 6, 60: 8, 78: 12, 202: 8, 226: 2, 120: 2, 150: 8,
    90: 2, 114: 16, 46: 4, 166: 13,
}


def visited_cuts(path):
    """Pull the physical parity cut back through the accumulated swaps."""
    permutation = list(range(8))
    cuts = [INITIAL_CUT]
    for left in path:
        right = (left + 1) % 8
        permutation = [
            right if point == left else left if point == right else point
            for point in permutation
        ]
        mask = sum((point % 2) << i for i, point in enumerate(permutation))
        cuts.append(mask ^ 255 if mask & 1 else mask)
    return cuts, permutation


def separates(mask, left, right):
    return ((mask >> left) ^ (mask >> right)) & 1


def simulate(cuts, strengths):
    """Compare phase-independent worst losses on the full right singlet space."""
    from math import pi

    import numpy as np
    from scipy.sparse import csr_matrix, eye
    from scipy.sparse.linalg import expm_multiply

    from qam.examples.two_ring_transport_qiskit import eight_point_loss_operators

    basis, _ = eight_point_loss_operators()
    indices = np.arange(256)

    def exchange(left, right):
        different = ((indices >> left) ^ (indices >> right)) & 1
        swapped = indices ^ (different * ((1 << left) | (1 << right)))
        return csr_matrix((np.full(256, 0.5), (indices, swapped)), shape=(256, 256)) - eye(256) / 4

    binding = sum(exchange(i, j) for i, j in combinations(range(8), 2) if (i - j) % 2)
    swaps = [exchange(i, (i + 1) % 8) for i in range(8)]
    dwell_positions = {cuts.index(mask): float(time) for mask, time in DWELL.items()}
    refined_positions = {**dwell_positions, 0: dwell_positions[0] + 3 / 8}

    def traverse(state, strength, forward, backward, positions):
        def wait(index, value):
            area = pi * strength * positions.get(index, 0)
            if index < len(OUTBOUND):
                area /= 2
            return expm_multiply(-1j * area * binding, value) if area else value

        for index, edge in enumerate(OUTBOUND):
            state = wait(index, state)
            state = expm_multiply(-1j * pi * (forward * swaps[edge] + strength * binding), state)
        state = wait(len(OUTBOUND), state)
        for index in range(len(OUTBOUND) - 1, -1, -1):
            state = expm_multiply(
                -1j * pi * (backward * swaps[OUTBOUND[index]] + strength * binding), state
            )
            state = wait(index, state)
        return state

    for strength in strengths:
        target = expm_multiply(1j * pi * strength * binding / 2, basis)
        for label, stages, positions in (
            (76, ((1, 1, 1),), dwell_positions),
            (228, ((1, -1, 1), (-1, 1, 2), (1, -1, 1)), refined_positions),
            (304, ((1, -1, 1), (-1, 1, 1), (-1, 1, 1), (1, -1, 1)), refined_positions),
        ):
            state = basis
            for forward, backward, duration in stages:
                state = traverse(state, strength * duration, forward, backward, positions)
            relative = target.conj().T @ state
            assert np.allclose(relative.conj().T @ relative, np.eye(14), atol=1e-10, rtol=0)
            phases = np.sort(np.angle(np.linalg.eigvals(relative)))
            gaps = np.diff(np.append(phases, phases[0] + 2 * pi))
            width = 2 * pi - max(gaps)
            loss = np.sin(width / 2) ** 2 if width < pi else 1.0
            print(f"g={strength:g}, {label} swaps: worst singlet loss={loss:.9g}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulate", nargs="+", type=float, metavar="G",
                        help="also simulate at the specified positive relative binding strengths")
    args = parser.parse_args()
    if args.simulate and any(not 0 < strength < float("inf") for strength in args.simulate):
        parser.error("relative binding strengths must be finite and positive")
    cuts, _ = visited_cuts(OUTBOUND)
    _, final = visited_cuts(OUTBOUND + OUTBOUND[::-1])
    assert final == list(range(8))
    assert DWELL.keys() <= set(cuts) and min(DWELL.values()) >= 0
    for left, right in combinations(range(8), 2):
        drift = sum(separates(a, left, right) + separates(b, left, right)
                    for a, b in zip(cuts, cuts[1:]))
        dwell = sum(time * separates(mask, left, right) for mask, time in DWELL.items())
        expected = 112 - Fraction(separates(INITIAL_CUT, left, right), 2)
        assert drift + dwell == expected, (left, right)
    assert sum(DWELL.values()) == Fraction(239, 2)
    print(f"{2 * len(OUTBOUND)} swaps, {len(set(cuts))} cuts, "
          f"{len(DWELL)} dwell locations, all 28 edge weights verified")
    if args.simulate:
        simulate(cuts, args.simulate)


if __name__ == "__main__":
    main()
