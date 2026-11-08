"""Compare parity-only and local sign records before an exchange readout."""

from math import isclose

from qiskit import QuantumCircuit

from qam.simulation import Basis


def exchange_distribution(record_local_signs):
    # q0 and q1 are flux doublets; q2 records their parity.
    # q3 and q4 can retain the two local signs.
    basis = Basis("R27", tuple(range(32)))
    circuit = QuantumCircuit(5)
    circuit.h(0)
    circuit.h(1)
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    if record_local_signs:
        circuit.cx(0, 3)
        circuit.cx(1, 4)
    circuit.h(0)
    circuit.h(1)
    state = basis.prepare(0).evolve(circuit)
    joint = state.readout("R27", lambda label: (label >> 2 & 1, (label ^ (label >> 1)) & 1))
    success = joint[(1, 0)] + joint[(1, 1)]
    return success, joint[(1, 0)] / success


def main():
    for record_local_signs, expected in ((False, 1), (True, 0.5)):
        success, plus = exchange_distribution(record_local_signs)
        assert isclose(success, 0.5) and isclose(plus, expected)
        print(f"local sign records={record_local_signs}: selection={success:g}, exchange plus={plus:g}")


if __name__ == "__main__":
    main()
