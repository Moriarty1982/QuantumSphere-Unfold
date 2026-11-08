"""Compare magnitude-only and signed flux pointers at fixed |n|=1."""

from math import isclose

from qiskit import QuantumCircuit

from qam.simulation import Basis


def interference(record_sign):
    # q0 encodes the sign of n; q1 flags the common nonzero magnitude.
    # q2 is an optional record of the sign.
    basis = Basis("M", tuple(range(8)))
    circuit = QuantumCircuit(3)
    circuit.h(0)
    circuit.x(1)
    if record_sign:
        circuit.cx(0, 2)
    circuit.h(0)
    state = basis.prepare(0).evolve(circuit)
    return state.readout("M", lambda label: (label >> 1 & 1, label & 1))


def main():
    magnitude_only = interference(record_sign=False)
    signed = interference(record_sign=True)
    assert isclose(magnitude_only[(1, 0)], 1)
    assert isclose(signed[(1, 0)], 0.5) and isclose(signed[(1, 1)], 0.5)
    print(f"magnitude and interference bit, magnitude pointer: {magnitude_only}")
    print(f"magnitude and interference bit, sign also recorded: {signed}")


if __name__ == "__main__":
    main()
