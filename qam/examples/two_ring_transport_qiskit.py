"""Check the marked two-layer Heisenberg transport and its calibration."""

from itertools import combinations
from math import comb, isclose, pi, sqrt

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import expm_multiply

from qam.examples.marked_ring_transport_qiskit import pairings, prepare_pairs


def alternating_singlet(points):
    half = points // 2
    even = sum(1 << i for i in range(0, points, 2))
    amplitudes = np.zeros(1 << points)
    for word in range(1 << points):
        if word.bit_count() == half:
            occupied = (word & even).bit_count()
            amplitudes[word] = (-1) ** occupied / (sqrt(half + 1) * comb(half, occupied))
    return Statevector(amplitudes)


def two_layers(points, first_error=0, second_error=0):
    circuit = QuantumCircuit(2 * points)
    for left_offset, error in ((0, first_error), (1, second_error)):
        exchange_layer(circuit, points, left_offset, pi + error)
    return circuit


def exchange_layer(circuit, points, offset, area):
    for i in range(points):
        left, right = (i + offset) % points, points + i
        for rotate in (circuit.rxx, circuit.ryy, circuit.rzz):
            rotate(area / 2, left, right)


def overlap_correction(h, *, positive_only=False, relative_errors=(0, 0),
                       period_estimates=(2 * pi, 2 * pi)):
    """Construct the cubic overlap correction in the eight-point comparison frame."""
    def inverse(pulses):
        return [(offset, -area) for offset, area in reversed(pulses)]

    inner = [(0, h), (1, h), (0, -h), (1, -h)]
    outer = [(0, -h / 6), (1, h / 6)]
    pulses = outer + inner + inverse(outer) + inverse(inner)
    circuit = QuantumCircuit(16)
    total_area = 0.0
    # The algebraic product acts on the input from right to left.
    for offset, area in reversed(pulses):
        if positive_only:
            area %= period_estimates[offset]
        area *= 1 + relative_errors[offset]
        exchange_layer(circuit, 8, offset, area)
        total_area += abs(area)
    return circuit, total_area


def reference_loss(left, right, common, difference):
    points = left.num_qubits
    out = right.tensor(left).evolve(two_layers(points, common + difference, common - difference))
    right_left = out.data.reshape(1 << points, 1 << points)
    returned = right.data.conj() @ right_left
    return float(1 - np.vdot(returned, returned).real)


def eight_point_loss_operators():
    """Return the singlet basis and the two leading loss matrices."""
    points = range(8)
    vectors = []
    for pairs in pairings(list(points)):
        circuit = QuantumCircuit(8)
        prepare_pairs(circuit, pairs)
        vectors.append(Statevector.from_instruction(circuit).data)
    basis = np.linalg.svd(np.asarray(vectors).T, full_matrices=False)[0][:, :14]
    indices = np.arange(256)
    identity = np.eye(14)

    def swap(left, right):
        different = ((indices >> left) ^ (indices >> right)) & 1
        swapped = indices ^ (different * ((1 << left) | (1 << right)))
        return basis.conj().T @ basis[swapped]

    neighbors = sum(swap(i, (i + 1) % 8) / 2 - identity / 4 for i in points)
    even_casimir = sum(swap(i, j) for i, j in combinations(range(0, 8, 2), 2))
    return basis, (
        2 * identity + neighbors / 3,
        2 * identity - neighbors / 3 + 5 * even_casimir / 3,
    )


def check_sensitive_inputs(right, shift):
    basis, operators = eight_point_loss_operators()
    for label, sign, operator in zip(("common", "difference"), (1, -1), operators):
        eigenvalues, eigenvectors = np.linalg.eigh(operator)
        sensitive = Statevector(basis @ eigenvectors[:, -1])
        step = 0.0005
        common, difference = (step, 0) if sign == 1 else (0, step)
        observed = reference_loss(sensitive, right, common, difference) / step ** 2
        assert isclose(observed, eigenvalues[-1], abs_tol=1e-3)

        mixture = Statevector(basis @ (eigenvectors[:, 0] + eigenvectors[:, -1]) / sqrt(2))
        target = mixture.evolve(shift).data
        step = 0.005
        out = right.tensor(mixture).evolve(two_layers(8, step, sign * step)).data.reshape(256, 256)
        returned = right.data.conj() @ out
        orthogonal = returned - target * np.vdot(target, returned)
        loss = np.linalg.norm(orthogonal) ** 2 / np.linalg.norm(returned) ** 2
        coefficient = (eigenvalues[-1] - eigenvalues[0]) ** 2 / 16
        assert isclose(loss / step ** 4, coefficient, abs_tol=1e-3)
        print(f"{label}: worst return-loss coefficient={observed:.6f}, "
              f"conditional loss coefficient={loss / step ** 4:.6f}")


def overlapping_comparison_state(left, right, h):
    """Apply the comparison-frame error for equal-area overlapping pulses."""
    points = left.num_qubits
    initial = left.tensor(right).data
    indices = np.arange(initial.size, dtype=np.int32)

    def generator(offset):
        targets = []
        for i in range(points):
            a, b = (i + offset) % points, points + i
            different = ((indices >> a) ^ (indices >> b)) & 1
            targets.append(indices ^ (different * ((1 << a) | (1 << b))))
        shape = (initial.size, initial.size)
        swaps = coo_matrix((np.full(points * initial.size, 0.5),
                            (np.concatenate(targets), np.tile(indices, points))), shape=shape)
        return swaps.tocsr() - (points / 4) * eye(initial.size)

    first, second = generator(0), generator(1)
    state = initial
    for factor, layer in ((1j, first), (-1j, first + second), (1j, second)):
        state = expm_multiply(factor * h * layer, state)
    return Statevector(state)


def check_overlap_correction(left, right):
    size = left.data.size

    def conditional_loss(state):
        # The ideal first layer has exchanged the physical left and right lanes.
        returned = state.data.reshape(size, size) @ right.data.conj()
        orthogonal = returned - left.data * np.vdot(left.data, returned)
        return np.linalg.norm(orthogonal) ** 2 / np.linalg.norm(returned) ** 2

    losses = []
    for overlap in (0.05, 0.025):
        h = pi * overlap
        state = overlapping_comparison_state(left, right, h)
        signed, _ = overlap_correction(h)
        positive, _ = overlap_correction(h, positive_only=True)
        corrected = state.evolve(signed)
        assert np.linalg.norm(corrected.data - state.evolve(positive).data) < 1e-12
        raw, improved = conditional_loss(state), conditional_loss(corrected)
        assert improved < raw
        losses.append(improved)
        print(f"overlap={overlap:.3f}: conditional loss={raw:.3e} -> {improved:.3e}")
    assert 230 < losses[0] / losses[1] < 270

    h = pi * 0.05
    state = overlapping_comparison_state(left, right, h)
    errors = (0.001, -0.001)
    periods = tuple(2 * pi / (1 + error) for error in errors)
    signed, _ = overlap_correction(h, relative_errors=errors)
    positive, _ = overlap_correction(
        h, positive_only=True, relative_errors=errors, period_estimates=periods
    )
    signed_out = state.evolve(signed)
    calibrated_out = state.evolve(positive)
    distance = np.linalg.norm(signed_out.data - calibrated_out.data)
    assert distance < 1e-12
    print(f"calibrated positive correction: output difference={distance:.3e}, "
          f"conditional loss={conditional_loss(calibrated_out):.3e}")


def main():
    for points in (6, 8):
        right = alternating_singlet(points)
        preparation = QuantumCircuit(points)
        prepare_pairs(preparation, zip(range(0, points, 2), range(1, points, 2)))
        left = Statevector.from_instruction(preparation)
        shift = QuantumCircuit(points)
        for i in range(points - 1, 0, -1):
            shift.swap(i - 1, i)
        expected = right.tensor(left.evolve(shift))
        actual = right.tensor(left).evolve(two_layers(points))
        overlap = np.vdot(expected.data, actual.data)
        assert abs(overlap - 1) < 1e-12
        print(f"{points} points: ideal complex overlap={overlap:.6f}")

    step = 0.0005
    for label, state, expected in (("neighbor pairs", left, 8), ("alternating singlet", right, 13)):
        common = reference_loss(state, right, step, 0) / step ** 2
        difference = reference_loss(state, right, 0, step) / step ** 2
        assert isclose(common, 1, abs_tol=1e-3)
        assert isclose(difference, expected, abs_tol=1e-3)
        print(f"{label}: common coefficient={common:.6f}, difference coefficient={difference:.6f}")

    common, difference, dither = 0.0003, -0.0007, 0.0002
    estimates = (
        (reference_loss(right, right, common + dither, difference)
         - reference_loss(right, right, common - dither, difference)) / (4 * dither),
        (reference_loss(right, right, common, difference + dither)
         - reference_loss(right, right, common, difference - dither)) / (52 * dither),
    )
    assert np.allclose(estimates, (common, difference), rtol=0, atol=1e-7)
    print(f"signed estimates: common={estimates[0]:.10f}, difference={estimates[1]:.10f}")
    check_sensitive_inputs(right, shift)
    signed, signed_area = overlap_correction(pi / 20)
    positive, positive_area = overlap_correction(pi / 20, positive_only=True)
    initial = right.tensor(right)
    difference = np.linalg.norm(initial.evolve(signed).data - initial.evolve(positive).data)
    assert difference < 1e-12
    assert isclose(positive_area, 12 * pi, abs_tol=1e-12)
    print(f"cubic correction: absolute areas={signed_area / pi:.6f}pi/"
          f"{positive_area / pi:.6f}pi, output difference={difference:.3e}")
    check_overlap_correction(left, right)


if __name__ == "__main__":
    main()
