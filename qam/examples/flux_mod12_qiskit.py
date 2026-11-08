"""Test a common modulo-12 zero pointer on the full set of residues."""

from math import isclose, pi, sqrt

from qiskit import QuantumCircuit
from qiskit.circuit.library import StatePreparation
from qiskit.quantum_info import Statevector


def zero_probability(n, r):
    # Four qubits embed the twelve pointer levels k=0,...,11.
    prepare = StatePreparation([1 / sqrt(12)] * 12 + [0] * 4)
    circuit = QuantumCircuit(4)
    circuit.append(prepare, range(4))
    for flux in (n, r):
        for bit in range(4):
            circuit.p(pi * flux * (1 << bit) / 12, bit)
    circuit.append(prepare.inverse(), range(4))
    return float(Statevector.from_instruction(circuit).probabilities()[0])


def main():
    for j in range(12):
        probability = zero_probability(j + 1, j - 1)
        assert isclose(probability, float(j == 0), abs_tol=1e-12)
        print(f"j={j:2}: zero probability={probability:.6f}")
    for n, r in ((-1, 1), (13, 11), (-13, -11)):
        assert isclose(zero_probability(n, r), 1, abs_tol=1e-12)
    print("Both sign assignments at j=0 and aliases j=±12 accepted.")


if __name__ == "__main__":
    main()
