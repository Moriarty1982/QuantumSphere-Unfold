"""Coherently select the detuning labels +3 and -3 modulo eight."""

from math import isclose, pi

from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector


def selector():
    phase = QuantumCircuit(6)
    work = [3, 4, 5]
    phase.h(work)
    for source in range(3):
        for weight, target in enumerate(work):
            angle = 2 * pi * (1 << (source + weight)) / 8
            phase.cp(angle, source, target)
    phase.append(QFTGate(3).inverse(), work)

    circuit = QuantumCircuit(7)
    circuit.compose(phase, range(6), inplace=True)
    for residue in (3, 5):
        zeros = [bit for weight, bit in enumerate(work) if not residue & (1 << weight)]
        circuit.x(zeros)
        circuit.mcx(work, 6)
        circuit.x(zeros)
    circuit.compose(phase.inverse(), range(6), inplace=True)
    return circuit


def main():
    circuit = selector()
    pairs = ((1, -1), (-1, 1), (1, 1), (-1, -1), (2, 0))
    for n, r in pairs:
        label = n - 2 * r
        residue = label % 8
        output = residue + 64 * int(n + r == 0)
        state = Statevector.from_int(residue, 128).evolve(circuit)
        assert isclose(abs(state.data[output]) ** 2, 1, abs_tol=1e-12)
        print(f"pair={(n, r)}, detuning label={label:+}, null bit={output >> 6}")

    amplitudes = [0] * 128
    amplitudes[3] = amplitudes[5] = 2 ** -0.5
    state = Statevector(amplitudes).evolve(circuit)
    for index in (67, 69):
        assert abs(state.data[index] - 2 ** -0.5) < 1e-12
    print("Opposing pairs retain their relative phase; work bits reset.")


if __name__ == "__main__":
    main()
