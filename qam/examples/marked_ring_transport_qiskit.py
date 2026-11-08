"""Compare acceptance and marker coherence for transport on an eight-spin ring."""

from math import isclose, pi, sqrt

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


def mean_trace_probes(cases, return_transport=controlled_ring_shift, *, include_leakage=False):
    """Compare (transport, phase) cases against a fixed inverse reference.

    Average the unconditioned Hadamard test over all eight-spin pairings.
    With include_leakage, also return (mean, worst) loss for the moved branch.
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
        if include_leakage:
            inputs.append(Statevector.from_instruction(preparation).data[:branch_size])
        preparation.h(marker)
        for index, (transport, phase) in enumerate(cases):
            circuit = preparation.copy()
            if transport is not None:
                transport(circuit, marker, spins)
            if phase:
                circuit.p(phase, marker)
            return_transport(circuit, marker, spins, inverse=True)
            if include_leakage:
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
    if not include_leakage:
        return count, traces
    # The uniform pairing ensemble is P_singlet / 14.
    frame = np.asarray(inputs)
    leakage = []
    for states in moved_states:
        overlaps = (14 / count) * (np.asarray(states) @ frame.conj().T)
        # The normalized pairing frame is an isometry on the singlet space.
        singular_values = np.linalg.svd(overlaps, compute_uv=False)[:14]
        losses = np.clip(1 - singular_values ** 2, 0, 1)
        leakage.append((float(np.mean(losses)), float(losses[-1])))
    return count, traces, leakage


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
    count, traces, leakage = mean_trace_probes((
        (None, 0),
        (controlled_ring_shift, 0),
        (ring_shift_with_remote_swap, 0),
        (controlled_ring_shift, pi / 2),
        (ring_shift_with_remote_z, 0),
        (ring_shift_with_remote_zz, 0),
    ), include_leakage=True)
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


if __name__ == "__main__":
    main()
