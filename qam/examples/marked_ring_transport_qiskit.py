"""Compare acceptance and marker coherence for transport on an eight-spin ring."""

from math import acos, isclose, pi, sqrt
from itertools import combinations

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def controlled_ring_shift(circuit, marker, spins, *, inverse=False):
    """Move spin i to i+1 on the marked branch, or undo that move."""
    edges = list(zip(spins[:-1], spins[1:]))
    for left, right in edges if inverse else reversed(edges):
        circuit.cswap(marker, left, right)


def ring_shift_with_remote_swap(circuit, marker, spins):
    """Transport the marked pair correctly but disturb two other pairs."""
    controlled_ring_shift(circuit, marker, spins)
    circuit.cswap(marker, spins[3], spins[5])


def ring_shift_with_remote_z(circuit, marker, spins):
    """Disturb the global singlet while leaving the marked pair untouched."""
    controlled_ring_shift(circuit, marker, spins)
    circuit.cz(marker, spins[3])


def ring_shift_with_remote_zz(circuit, marker, spins):
    """Apply a two-spin phase with input-dependent singlet leakage."""
    ring_shift_with_remote_z(circuit, marker, spins)
    circuit.cz(marker, spins[5])


def mark_singlet(circuit, left, right, answer):
    """Write only the singlet bit, then undo the pair basis change."""
    circuit.z(left)
    circuit.cx(left, right)
    circuit.h(left)
    circuit.x(left)
    circuit.ccx(left, right, answer)
    circuit.x(left)
    circuit.h(left)
    circuit.cx(left, right)
    circuit.z(left)


def prepare_pairs(circuit, pairs):
    for left, right in pairs:
        circuit.x(right)
        circuit.h(left)
        circuit.cx(left, right)
        circuit.z(left)


def pairings(spins):
    if not spins:
        yield ()
        return
    for index in range(1, len(spins)):
        remaining = spins[1:index] + spins[index + 1:]
        for tail in pairings(remaining):
            yield ((spins[0], spins[index]), *tail)


def mean_trace_probes(cases, return_transport=controlled_ring_shift, *,
                      include_leakage=False, include_covariance=False):
    """Compare (transport, phase) cases against a fixed inverse reference.

    Average the unconditioned Hadamard test over all eight-spin pairings.
    With include_leakage, also return (mean, worst) loss for the moved branch.
    With include_covariance, append the seven compressed pair residuals.
    """
    cases = tuple(cases)
    spins = list(range(8))
    marker = 8
    branch_size = 1 << marker
    sums = [0j] * len(cases)
    inputs = []
    moved_states = [[] for _ in cases]
    count = 0
    for pairs in pairings(spins):
        count += 1
        preparation = QuantumCircuit(9)
        prepare_pairs(preparation, pairs)
        if include_leakage or include_covariance:
            inputs.append(Statevector.from_instruction(preparation).data[:branch_size])
        preparation.h(marker)
        for index, (transport, phase) in enumerate(cases):
            circuit = preparation.copy()
            if transport is not None:
                transport(circuit, marker, spins)
            if phase:
                circuit.p(phase, marker)
            return_transport(circuit, marker, spins, inverse=True)
            if include_leakage or include_covariance:
                moved_states[index].append(
                    sqrt(2) * Statevector.from_instruction(circuit).data[branch_size:]
                )
            quadratures = []
            for measure_y in (False, True):
                readout = circuit.copy()
                if measure_y:
                    readout.sdg(marker)
                readout.h(marker)
                plus = Statevector.from_instruction(readout).probabilities([marker])[0]
                quadratures.append(2 * plus - 1)
            sums[index] += complex(*quadratures)
    traces = [total / count for total in sums]
    if not (include_leakage or include_covariance):
        return count, traces
    # The uniform pairing ensemble is P_singlet / 14.
    frame = np.asarray(inputs)
    if include_covariance:
        indices = np.arange(branch_size)
        pair_swaps = []
        for i in range(marker - 1):
            different = ((indices >> i) ^ (indices >> (i + 1))) & 1
            swapped = indices ^ (different * (3 << i))
            pair_swaps.append((14 / count) * (frame[:, swapped] @ frame.conj().T))
    leakage = []
    covariance = []
    for states in moved_states:
        overlaps = (14 / count) * (np.asarray(states) @ frame.conj().T)
        # The normalized pairing frame is an isometry on the singlet space.
        if include_leakage:
            singular_values = np.linalg.svd(overlaps, compute_uv=False)[:14]
            losses = np.clip(1 - singular_values ** 2, 0, 1)
            leakage.append((float(np.mean(losses)), float(losses[-1])))
        if include_covariance:
            covariance.append([
                float(np.linalg.norm(overlaps @ swap - swap @ overlaps, ord=2))
                for swap in pair_swaps
            ])
    result = (count, traces)
    if include_leakage:
        result += (leakage,)
    if include_covariance:
        result += (covariance,)
    return result


def pair_transport_probabilities(transport):
    """Average each target-pair test over the input pair's singlet subspace."""
    spins = list(range(8))
    marker, answer = 8, 9
    probabilities = []
    for left in range(7):
        right = left + 1
        remaining = [spin for spin in spins if spin not in (left, right)]
        accepted = []
        for pairs in pairings(remaining):
            circuit = QuantumCircuit(10)
            prepare_pairs(circuit, ((left, right), *pairs))
            circuit.x(marker)
            if transport is not None:
                transport(circuit, marker, spins)
            mark_singlet(circuit, right, (right + 1) % len(spins), answer)
            accepted.append(Statevector.from_instruction(circuit).probabilities([answer])[1])
        probabilities.append(float(np.mean(accepted)))
    return probabilities


def pair_complement_probabilities(transport):
    """Return target-No probabilities conditioned on input No for each pair."""
    spins = list(range(8))
    marker, input_bit, output_bit = 8, 9, 10
    probabilities = []
    for left in range(7):
        right = left + 1
        input_no = output_no = 0.0
        for pairs in pairings(spins):
            circuit = QuantumCircuit(11)
            prepare_pairs(circuit, pairs)
            mark_singlet(circuit, left, right, input_bit)
            circuit.x(marker)
            if transport is not None:
                transport(circuit, marker, spins)
            mark_singlet(circuit, right, (right + 1) % len(spins), output_bit)
            joint = Statevector.from_instruction(circuit).probabilities([input_bit, output_bit])
            input_no += joint[0] + joint[2]
            output_no += joint[0]
        probabilities.append(float(output_no / input_no))
    return probabilities


def pair_casimir_moments(transport):
    """Evaluate the first two moments of total spin squared divided by two."""
    spins = list(range(8))
    marker, answer, second_answer = 8, 9, 10
    preparation = QuantumCircuit(11)
    prepare_pairs(preparation, zip(spins[::2], spins[1::2]))
    preparation.x(marker)
    transport(preparation, marker, spins)
    pair_probabilities = {}
    for left, right in combinations(spins, 2):
        circuit = preparation.copy()
        mark_singlet(circuit, left, right, answer)
        pair_probabilities[left, right] = Statevector.from_instruction(circuit).probabilities([answer])[1]
    singlet_sum = sum(pair_probabilities.values())
    squared_sum = singlet_sum
    for first, second in combinations(pair_probabilities, 2):
        outer = set(first) ^ set(second)
        if len(outer) == 2:
            outer_pair = tuple(sorted(outer))
            squared_sum += (
                pair_probabilities[first] + pair_probabilities[second]
                - pair_probabilities[outer_pair]
            ) / 2
        else:
            circuit = preparation.copy()
            mark_singlet(circuit, *first, answer)
            mark_singlet(circuit, *second, second_answer)
            squared_sum += 2 * Statevector.from_instruction(circuit).probabilities(
                [answer, second_answer]
            )[3]
    return float(10 - singlet_sum), float(100 - 20 * singlet_sum + squared_sum)


def third_casimir_moment(transport):
    """Evaluate the third moment directly on the simulated moved spin state."""
    spins = list(range(8))
    marker = len(spins)
    circuit = QuantumCircuit(marker + 1)
    prepare_pairs(circuit, zip(spins[::2], spins[1::2]))
    circuit.x(marker)
    transport(circuit, marker, spins)
    state = Statevector.from_instruction(circuit).data[1 << marker:]
    indices = np.arange(state.size)
    swaps = []
    for left, right in combinations(spins, 2):
        different = ((indices >> left) ^ (indices >> right)) & 1
        swaps.append(indices ^ (different * ((1 << left) | (1 << right))))

    def apply_casimir(vector):
        # X = 10 I - sum(P_ij) = -4 I + sum(SWAP_ij) / 2.
        return -4 * vector + sum(vector[swap] for swap in swaps) / 2

    first = apply_casimir(state)
    return float(np.vdot(first, apply_casimir(first)).real)


def spin_weights_from_axis_readout(state):
    """Recover spin weights from signed magnetization averaged over axes."""
    spins = range(8)
    magnetization = np.array([4 - index.bit_count() for index in range(256)])
    distribution = np.zeros(9)
    # Azimuthal frequencies are at most eight. After that average, the
    # polar dependence is polynomial of degree at most eight in cos(theta).
    nodes, weights = np.polynomial.legendre.leggauss(5)
    for cosine, weight in zip(nodes, weights):
        for azimuth in range(9):
            readout = QuantumCircuit(8)
            readout.rz(-2 * pi * azimuth / 9, spins)
            readout.ry(-acos(cosine), spins)
            probabilities = state.evolve(readout).probabilities()
            distribution += weight / 18 * np.bincount(
                magnetization + 4, weights=probabilities, minlength=9
            )
    positive = np.append(distribution[4:], 0)
    return (2 * np.arange(5) + 1) * (positive[:-1] - positive[1:])


def singlet_leakage_interval(first, second, *, atol=1e-12):
    """Sharp leakage interval for compatible eight-spin Casimir moments."""
    if abs(first) <= atol and abs(second) <= atol:
        return 0.0, 0.0
    if first <= 0 or second < first - atol or second > 10 * first + atol:
        raise ValueError("Moments are incompatible with the eight-spin spectrum.")
    edges = ((1, 3), (3, 6), (6, 10))
    lower = max(((left + right) * first - second) / (left * right)
                for left, right in edges)
    upper = min(1.0, (11 * first - second) / 10)
    if lower > upper + atol:
        raise ValueError("Moments are incompatible with the eight-spin spectrum.")
    return float(np.clip(lower, 0, upper)), float(np.clip(upper, 0, 1))


def compare_transport(move_spins, marker_phase=0):
    transport = controlled_ring_shift if move_spins else None
    return probe_transport(transport, transport, marker_phase=marker_phase)


def probe_transport(transport, return_transport, *, marker_phase=0):
    """Probe optional controlled transports before and after the pair test.

    Both callbacks act on (circuit, marker, spins). The return callback
    is called with inverse=True to undo the chosen reference transport.
    """
    spins = list(range(8))
    marker, answer = 8, 9
    circuit = QuantumCircuit(10)
    prepare_pairs(circuit, zip(spins[::2], spins[1::2]))
    circuit.h(marker)
    if transport is not None:
        transport(circuit, marker, spins)
    if marker_phase:
        circuit.p(marker_phase, marker)

    controlled_ring_shift(circuit, marker, spins, inverse=True)
    mark_singlet(circuit, *spins[:2], answer)
    controlled_ring_shift(circuit, marker, spins)
    joint = Statevector.from_instruction(circuit).probabilities([marker, answer])
    accepted = joint[2] + joint[3]
    branch_acceptance = (2 * joint[2], 2 * joint[3])

    if return_transport is not None:
        return_transport(circuit, marker, spins, inverse=True)
    quadratures = []
    for measure_y in (False, True):
        readout = circuit.copy()
        if measure_y:
            readout.sdg(marker)
        readout.h(marker)
        plus_and_accepted = Statevector.from_instruction(readout).probabilities([marker, answer])[2]
        quadratures.append(2 * plus_and_accepted / accepted - 1)
    coherence = complex(*quadratures)
    balance = 2 * sqrt(joint[2] * joint[3]) / accepted
    branch_overlap = coherence / balance if balance else None
    return accepted, coherence, branch_acceptance, branch_overlap


def main():
    for label, move_spins, phase, expected in (
        ("mark only", False, 0, (5 / 8, 2 / 5)),
        ("common transport", True, 0, (1, 1)),
        ("common transport with phase flip", True, pi, (1, -1)),
        ("common transport with quarter turn", True, pi / 2, (1, 1j)),
    ):
        accepted, coherence, branches, overlap = compare_transport(move_spins, phase)
        assert isclose(accepted, expected[0], abs_tol=1e-12)
        assert abs(coherence - expected[1]) < 1e-12
        assert isclose(branches[0], 1, abs_tol=1e-12)
        assert isclose(branches[1], 1 if move_spins else 1 / 4, abs_tol=1e-12)
        assert abs(overlap - (expected[1] if move_spins else 1 / 2)) < 1e-12
        print(f"{label}: P(yes)={accepted:.6f}, X+iY={coherence:.6f}, "
              f"P(yes | mark)={branches[0]:.6f}/{branches[1]:.6f}, "
              f"branch overlap={overlap:.6f}")
    accepted, coherence, _, overlap = probe_transport(None, controlled_ring_shift)
    assert isclose(accepted, 5 / 8, abs_tol=1e-12)
    assert abs(coherence - 1 / 5) < 1e-12
    assert abs(overlap - 1 / 4) < 1e-12
    print(f"mark only with ideal reference return: P(yes)={accepted:.6f}, "
          f"X+iY={coherence:.6f}, branch overlap={overlap:.6f}")
    accepted, coherence, _, overlap = probe_transport(
        ring_shift_with_remote_swap, controlled_ring_shift
    )
    assert isclose(accepted, 1, abs_tol=1e-12)
    assert abs(coherence - 1 / 2) < 1e-12
    assert abs(overlap - 1 / 2) < 1e-12
    print(f"common transport with remote swap: P(yes)={accepted:.6f}, "
          f"X+iY={coherence:.6f}, branch overlap={overlap:.6f}")
    count, traces, leakage, covariance = mean_trace_probes((
        (None, 0),
        (controlled_ring_shift, 0),
        (ring_shift_with_remote_swap, 0),
        (controlled_ring_shift, pi / 2),
        (ring_shift_with_remote_z, 0),
        (ring_shift_with_remote_zz, 0),
    ), include_leakage=True, include_covariance=True)
    assert count == 105
    for label, observed, expected, loss, expected_loss in zip(
        ("mark only", "common transport", "common transport with remote swap",
         "common transport with quarter turn", "common transport with remote Z",
         "common transport with remote ZZ"),
        traces,
        (0, 1, 2 / 7, 1j, 0, -1 / 7),
        leakage,
        ((0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (4 / 7, 8 / 9)),
    ):
        assert abs(observed - expected) < 1e-12
        assert all(isclose(value, expected, abs_tol=1e-12)
                   for value, expected in zip(loss, expected_loss))
        print(f"{label}: trace/14 over {count} pairings = {observed:.6f}, "
              f"magnitude={abs(observed):.6f}, "
              f"singlet leakage mean/worst={loss[0]:.6f}/{loss[1]:.6f}")
    for residuals, expected in zip(covariance[:4], (list(range(7)), [], [1, 2, 3, 4], [])):
        failed = [i for i, error in enumerate(residuals) if error > 1e-12]
        assert failed == expected
        print(f"pair covariance residuals: {[round(error, 6) for error in residuals]}")
    for label, transport, failed in (
        ("mark only", None, range(7)),
        ("common transport", controlled_ring_shift, ()),
        ("common transport with remote swap", ring_shift_with_remote_swap, (1, 2, 3, 4)),
    ):
        probabilities = pair_transport_probabilities(transport)
        assert all(isclose(p, 1 / 4 if i in failed else 1, abs_tol=1e-12)
                   for i, p in enumerate(probabilities))
        print(f"{label}: pair acceptance over 15 pairings: "
              f"{[round(p, 6) for p in probabilities]}")
        complement = pair_complement_probabilities(transport)
        assert all(isclose(p, 7 / 12 if i in failed else 1, abs_tol=1e-12)
                   for i, p in enumerate(complement))
        print(f"{label}: pair No-to-No: {[round(p, 6) for p in complement]}")
    for transport, expected, expected_interval, expected_third in (
        (controlled_ring_shift, (0, 0), (0, 0), 0),
        (ring_shift_with_remote_swap, (0, 0), (0, 0), 0),
        (ring_shift_with_remote_z, (1, 1), (1, 1), 1),
        (ring_shift_with_remote_zz, (2, 6), (2 / 3, 1), 18),
    ):
        first, second = pair_casimir_moments(transport)
        assert isclose(first, expected[0], abs_tol=1e-12)
        assert isclose(second, expected[1], abs_tol=1e-12)
        lower, upper = singlet_leakage_interval(first, second)
        assert isclose(lower, expected_interval[0], abs_tol=1e-12)
        assert isclose(upper, expected_interval[1], abs_tol=1e-12)
        print(f"{transport.__name__}: Casimir moments={first:.6f}/{second:.6f}, "
              f"leakage interval=[{lower:.6f}, {upper:.6f}]")
        third = third_casimir_moment(transport)
        assert isclose(third, expected_third, abs_tol=1e-12)
        residual = max(0.0, third - 6 * second + 9 * first)
        print(f"  statevector third moment={third:.6f}, "
              f"spin >= 3 upper bound={min(1.0, residual / 54):.6f}")
    spins = list(range(8))
    preparation = QuantumCircuit(9)
    prepare_pairs(preparation, zip(spins[::2], spins[1::2]))
    preparation.x(8)
    ring_shift_with_remote_zz(preparation, 8, spins)
    zz_state = Statevector(Statevector.from_instruction(preparation).data[256:])
    for label, state, expected in (
        ("remote ZZ", zz_state, (1 / 3, 0, 2 / 3, 0, 0)),
        ("fully polarized", Statevector.from_label("00000000"), (0, 0, 0, 0, 1)),
    ):
        weights = spin_weights_from_axis_readout(state)
        assert np.allclose(weights, expected, rtol=0, atol=1e-12)
        print(f"{label}: spin weights from axis readout={weights.round(6).tolist()}")


if __name__ == "__main__":
    main()
