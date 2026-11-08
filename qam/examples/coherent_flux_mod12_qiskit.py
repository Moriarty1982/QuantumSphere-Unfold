"""Coherent modulo-12 zero selection on two flux sign registers."""

from math import isclose, pi, sqrt

from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation
from qiskit.quantum_info import Statevector


def main():
    # q0 and q1 encode -1 as 0 and +1 as 1; q6 is the binary result.
    phase_bits = list(range(2, 6))
    phase = QuantumCircuit(6)
    prepare = StatePreparation([1 / sqrt(12)] * 12 + [0] * 4)
    phase.append(prepare, phase_bits)
    for flux in (0, 1):
        for weight, target in enumerate(phase_bits):
            angle = pi * (1 << weight) / 12
            phase.p(-angle, target)
            phase.cp(2 * angle, flux, target)
    phase.append(prepare.inverse(), phase_bits)

    circuit = QuantumCircuit(7)
    circuit.h([0, 1])
    circuit.compose(phase, qubits=range(6), inplace=True)
    circuit.x(phase_bits)
    circuit.mcx(phase_bits, 6)
    circuit.x(phase_bits)
    circuit.compose(phase.inverse(), qubits=range(6), inplace=True)

    probabilities = Statevector.from_instruction(circuit).probabilities()
    assert all(isclose(probabilities[index], 0.25) for index in (0, 3, 65, 66))
    assert isclose(sum(probabilities[index] for index in (0, 3, 65, 66)), 1)
    circuit.h([0, 1])
    probabilities = Statevector.from_instruction(circuit).probabilities()
    accepted = sum(probabilities[64:])
    positive_exchange = probabilities[64] + probabilities[67]
    assert isclose(accepted, 0.5)
    assert isclose(positive_exchange / accepted, 1)
    print("Null selection: 0.5; positive exchange given null: 1; work register reset.")


if __name__ == "__main__":
    main()
