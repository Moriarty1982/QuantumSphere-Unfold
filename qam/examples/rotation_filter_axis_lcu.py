"""Verify coherent selection of the 18 physical spin rotations in Qiskit."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation, UnitaryGate
from qiskit.quantum_info import Statevector

from qam.examples.rotation_filter_axis_check import rotation_terms
from qam.tools.route_search import rotation_mean


def zero_block(twice_spin):
    terms = list(rotation_terms(twice_spin, cutoff=5))
    axis_bits = (len(terms) - 1).bit_length()
    system_bits = twice_spin.bit_length()
    axis = list(range(system_bits, system_bits + axis_bits))
    dimension = twice_spin + 1
    padded = 1 << system_bits
    amplitudes = np.zeros(1 << axis_bits)
    select = np.eye(len(amplitudes) * padded, dtype=complex)
    for index, (weight, rotation) in enumerate(terms):
        amplitudes[index] = np.sqrt(weight)
        start = index * padded
        select[start:start + dimension, start:start + dimension] = rotation
    prepare = StatePreparation(amplitudes)
    circuit = QuantumCircuit(system_bits + axis_bits)
    circuit.append(prepare, axis)
    circuit.append(UnitaryGate(select), range(circuit.num_qubits))
    circuit.append(prepare.inverse(), axis)
    return np.column_stack([
        Statevector.from_int(index, len(select)).evolve(circuit).data[:dimension]
        for index in range(dimension)
    ])


def main():
    for twice_spin in range(1, 6):
        a, b = rotation_mean(90, twice_spin)
        expected = (float(a) + float(b) * np.sqrt(2)) * np.eye(twice_spin + 1)
        error = np.linalg.norm(zero_block(twice_spin) - expected, ord=2)
        assert error < 1e-12
        print(f"2j={twice_spin}: coherent axis zero-block error={error:.3g}")


if __name__ == "__main__":
    main()
