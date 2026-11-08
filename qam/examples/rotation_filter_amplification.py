"""Check the rotation-filter amplification on its reduced spectral blocks."""

from math import isclose, pi, sqrt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def marker():
    # System labels 0 and 1 are the two minimal-spin states.
    # Labels 2 and 3 stand for rejected sectors. q2 is work, q3 the pointer.
    prepare = QuantumCircuit(3)
    prepare.x(1)
    prepare.cry(pi / 9, 1, 2)
    prepare.x(1)

    amplify = QuantumCircuit(3)
    amplify.compose(prepare, inplace=True)
    for _ in range(4):
        amplify.z(2)
        amplify.compose(prepare.inverse(), inplace=True)
        amplify.z(2)
        amplify.compose(prepare, inplace=True)

    circuit = QuantumCircuit(4)
    circuit.compose(amplify, inplace=True)
    circuit.cx(2, 3)
    circuit.compose(amplify.inverse(), inplace=True)
    return circuit


def main():
    circuit = marker()
    for label in range(4):
        output = label + (8 if label < 2 else 0)
        state = Statevector.from_int(label, 16).evolve(circuit)
        assert abs(state.data[output] - 1) < 1e-12

    amplitudes = [0j] * 16
    for label, phase in enumerate((1, 1j, -1, -1j)):
        amplitudes[label] = phase / 2
    result = Statevector(amplitudes).evolve(circuit)
    expected = [0j] * 16
    for label, amplitude in enumerate(amplitudes[:4]):
        expected[label + (8 if label < 2 else 0)] = amplitude
    error = sqrt(sum(abs(a - b)**2 for a, b in zip(result.data, expected)))
    assert isclose(error, 0, abs_tol=1e-12)
    print(f"All labels marked as expected; coherent state error={error:.3g}")


if __name__ == "__main__":
    main()
