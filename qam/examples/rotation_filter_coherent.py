"""Coherent polynomial pointer from a dilation of the computed rotation mean."""
from math import asin, pi, sqrt

import numpy as np
from scipy.linalg import block_diag
from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation, UnitaryGate
from qiskit.quantum_info import Statevector

from qam.examples.rotation_filter_axis_check import rotation_mean


def marker(twice_spin=None):
    prefilter = twice_spin is None
    spins = range(1, 6) if prefilter else (twice_spin,)
    physical = block_diag(*(rotation_mean(spin, cutoff=5) for spin in spins))
    dimension = len(physical)
    system = list(range((dimension - 1).bit_length()))
    degree = 2 if prefilter else 4
    work = list(range(len(system), len(system) + degree))
    choice = list(range(work[-1] + 1, work[-1] + degree.bit_length()))
    attenuate = choice[-1] + 1
    pointer = attenuate + 1 + int(prefilter)

    mean = np.zeros((2**len(system), 2**len(system)), complex)
    mean[:dimension, :dimension] = (physical + physical.conj().T) / 2
    eigenvalues, basis = np.linalg.eigh(mean)
    complement = (basis * np.sqrt(1 - eigenvalues**2)) @ basis.conj().T
    block = np.block([[mean, complement], [complement, -mean]])

    roots = (-sqrt(2)/6, 0) if prefilter else (-1/5, -sqrt(2)/6, 0, 1/3)
    polynomial = np.poly(roots)
    polynomial /= np.polyval(polynomial, 1 / sqrt(2))
    coefficients = polynomial[-2::-1]
    alpha = sum(abs(coefficients))
    prepare = StatePreparation(np.sqrt(abs(coefficients) / alpha))

    base = QuantumCircuit(pointer)
    base.append(prepare, choice)
    for term, coefficient in enumerate(coefficients):
        if coefficient < 0:
            zeros = [bit for k, bit in enumerate(choice) if not term & (1 << k)]
            if zeros:
                base.x(zeros)
            base.cz(*choice)
            if zeros:
                base.x(zeros)
        selected = np.arange(len(block)) * (2**len(choice)) + term
        matrix = np.eye(len(block) * (2**len(choice)), dtype=complex)
        matrix[np.ix_(selected, selected)] = block
        controlled = UnitaryGate(matrix)
        for bit in work[:term + 1]:
            base.append(controlled, choice + system + [bit])
    base.append(prepare.inverse(), choice)
    iterations = 1 if prefilter else 4
    base.ry(2 * asin(alpha * np.sin(pi / (4 * iterations + 2))), attenuate)
    flags = work + choice + [attenuate]
    base.x(attenuate)  # Put the success amplitude at all-zero flags.
    if prefilter:
        parity = pointer - 1
        signs = np.ones(len(mean))
        signs[:dimension] = np.repeat([(-1)**spin for spin in spins], [spin + 1 for spin in spins])
        base.h(parity)
        base.append(UnitaryGate(np.diag(np.r_[np.ones(len(mean)), signs])), system + [parity])
        base.h(parity)
        base.x(parity)
        flags.append(parity)

    reflection = QuantumCircuit(pointer)
    reflection.x(flags)
    reflection.h(flags[-1])
    reflection.mcx(flags[:-1], flags[-1])
    reflection.h(flags[-1])
    reflection.x(flags)

    amplified = base.copy()
    for _ in range(iterations):
        amplified.compose(reflection, inplace=True)
        amplified.compose(base.inverse(), inplace=True)
        amplified.compose(reflection, inplace=True)
        amplified.compose(base, inplace=True)

    circuit = QuantumCircuit(pointer + 1)
    circuit.compose(amplified, inplace=True)
    circuit.x(flags)
    circuit.mcx(flags, pointer)
    circuit.x(flags)
    circuit.compose(amplified.inverse(), inplace=True)
    return circuit


def main():
    for spin in range(1, 6):
        circuit = marker(spin)
        dimension = spin + 1
        initial = np.zeros(2**circuit.num_qubits, complex)
        initial[:dimension] = (1j ** np.arange(dimension)) / sqrt(dimension)
        state = Statevector(initial).evolve(circuit)
        expected = np.roll(initial, 2**(circuit.num_qubits - 1)) if spin == 1 else initial
        error = np.linalg.norm(state.data - expected)
        assert error < 1e-8
        print(f"2j={spin}: pointer state error={error:.3g}")


    circuit = marker()
    dimension = sum(spin + 1 for spin in range(1, 6))
    initial = np.zeros(2**circuit.num_qubits, complex)
    initial[:dimension] = (1j ** np.arange(dimension)) / sqrt(dimension)
    expected = initial.copy()
    expected[2**(circuit.num_qubits - 1):][:2] = expected[:2]
    expected[:2] = 0
    result = Statevector(initial).evolve(circuit)
    error = np.linalg.norm(result.data - expected)
    assert error < 1e-8
    print(f"Mixed spins with parity prefilter: pointer state error={error:.3g}")


if __name__ == "__main__":
    main()
