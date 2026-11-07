"""Compare two area readouts on adjacent Fourier modes in sector n=1."""

from math import pi

from qiskit import QuantumCircuit

from qam.simulation import Basis


def main():
    basis = Basis("M", ((0, 1), (1, -1)))
    initial = basis.prepare((0, 1))
    print("Areas in units of a_M")
    for angle in (0, pi / 2, pi):
        circuit = QuantumCircuit(1)
        # The projected cosine potential couples adjacent modes via X.
        circuit.rx(angle, 0)
        circuit.rz(-pi / 3, 0)
        state = initial.evolve(circuit)
        additive = state.readout("M", lambda mode: abs(mode[0]) + abs(mode[1]))
        mixed = state.readout("M", lambda mode: 3 * abs(2 * mode[0] + mode[1]) / 5)
        print(f"angle/pi={angle / pi:g}, additive={additive}, mixed={mixed}")


if __name__ == "__main__":
    main()
