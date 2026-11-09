"""Compare single and composite swaps in a detuned two-energy block."""

import argparse
from math import pi, sqrt

import numpy as np
from scipy.linalg import expm


def swap_pulse(detuning, angles):
    """Apply signed Bloch rotation angles with a fixed detuning."""
    exchange = np.array([[0, 1], [1, 0]])
    difference = np.diag([1, -1])
    evolution = np.eye(2, dtype=complex)
    for angle in angles:
        generator = np.sign(angle) * exchange + detuning * difference
        evolution = expm(-0.5j * abs(angle) * generator) @ evolution
    return evolution


def physical_errors(detuning, common_binding=0, *, compensate_common=False):
    """Return worst output errors with a fixed right singlet reference."""
    from scipy.sparse import coo_matrix, eye
    from scipy.sparse.linalg import expm_multiply

    from qam.examples.two_ring_transport_qiskit import (
        alternating_singlet, eight_point_loss_operators,
    )

    basis, _ = eight_point_loss_operators()
    reference = alternating_singlet(8).data
    indices = np.array([i for i in range(65536) if i.bit_count() == 8], dtype=np.int32)
    lookup = np.full(65536, -1, dtype=np.int32)
    rows = np.arange(indices.size)
    lookup[indices] = rows

    def exchange(edges):
        targets = []
        for a, b in edges:
            different = ((indices >> a) ^ (indices >> b)) & 1
            swapped = indices ^ (different * ((1 << a) | (1 << b)))
            targets.append(lookup[swapped])
        count = len(targets)
        swaps = coo_matrix((np.full(count * indices.size, 0.5),
                            (np.concatenate(targets), np.tile(rows, count))),
                           shape=(indices.size, indices.size))
        return swaps.tocsr() - count / 4 * eye(indices.size)

    parallel = exchange([(i, 8 + i) for i in range(8)])
    parity_edges = [(i, j) for i in range(0, 8, 2) for j in range(1, 8, 2)]
    left_binding = exchange(parity_edges)
    right_binding = exchange([(8 + i, 8 + j) for i, j in parity_edges])
    common = left_binding + right_binding
    if compensate_common:
        common += exchange([(i, 8 + j) for i, j in parity_edges]
                           + [(j, 8 + i) for i, j in parity_edges])
    binding = detuning * (left_binding - right_binding) + common_binding * common
    initial = (reference[:, None, None] * basis[None, :, :]).reshape(65536, 14)[indices]
    target = (basis[:, None, :] * reference[None, :, None]).reshape(65536, 14)[indices]
    angles = (7 * pi / 3, -5 * pi / 3, pi / 3)
    three = [(angle, 1) for angle in angles]
    nine = three + [(-angle, sqrt(2)) for angle in angles] + three
    errors = []
    for sequence in (three, nine):
        output = initial
        common_area = 0.0
        for angle, scale in sequence:
            generator = np.sign(angle) * parallel + scale * binding
            output = expm_multiply(-1j * abs(angle) * generator, output)
            common_area += abs(angle) * scale * common_binding
        if compensate_common and common_area:
            # Inverse evolution equals a positive pulse modulo pi on total spin zero.
            output = expm_multiply(1j * common_area * common, output)
        phase = np.angle(np.trace(target.conj().T @ output))
        errors.append((
            float(np.linalg.norm(output - target, 2)),
            float(np.linalg.norm(output * np.exp(-1j * phase) - target, 2)),
        ))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--physical", nargs="+", type=float, metavar="EPS",
                        help="also compare parallel eight-pair exchanges on the singlet input space")
    parser.add_argument("--common-binding", type=float, default=0,
                        help="additional equal binding on the two physical registers")
    parser.add_argument("--compensate-common", action="store_true",
                        help="add crossed terms and undo their common evolution")
    args = parser.parse_args()
    if not np.isfinite(args.common_binding):
        parser.error("common binding must be finite")
    target = -1j * np.array([[0, 1], [1, 0]])
    angles = (7 * pi / 3, -5 * pi / 3, pi / 3)
    assert np.linalg.norm(swap_pulse(0, angles) - target, 2) < 1e-12
    for detuning in (0.05, 0.025, 0.0125):
        simple = swap_pulse(detuning, (pi,))
        composite = swap_pulse(detuning, angles)
        simple_loss = abs(simple[0, 0]) ** 2
        composite_loss = abs(composite[0, 0]) ** 2
        error = np.linalg.norm(composite - target, 2)
        assert composite_loss < simple_loss and error < np.linalg.norm(simple - target, 2)
        print(f"detuning={detuning:g}: failure {simple_loss:.6g} -> {composite_loss:.6g}, "
              f"composite operator error={error:.6g}")
    for detuning in args.physical or ():
        if not np.isfinite(detuning):
            parser.error("physical detunings must be finite")
        three, nine = physical_errors(detuning, args.common_binding,
                                      compensate_common=args.compensate_common)
        print(f"physical detuning={detuning:g}, common binding={args.common_binding:g}: operator errors, "
              f"three={three[0]:.6g}, nine={nine[0]:.6g}; "
              f"after trace phase correction: three={three[1]:.6g}, nine={nine[1]:.6g}")


if __name__ == "__main__":
    main()
