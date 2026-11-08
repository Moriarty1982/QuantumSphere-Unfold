"""Copy the conserved flux label on the additive fiber s=1."""

from math import isclose

from qiskit import QuantumCircuit

from qam.simulation import Basis


def main():
    # q0 encodes j in (j, 1-j). q1 is a pointer for n-1.
    labels = tuple((j, 1 - j, bit) for bit in (0, 1) for j in (0, 1))
    basis = Basis("M", labels)
    copy_flux = QuantumCircuit(2)
    copy_flux.cx(0, 1)

    for j in (0, 1):
        state = basis.prepare((j, 1 - j, 0)).evolve(copy_flux)
        additive = state.readout("M", lambda mode: abs(mode[0]) + abs(mode[1]))
        pointer = state.readout("M", lambda mode: 1 + mode[2])
        expected_flux = 2 * j + (1 - j)
        assert isclose(additive[1], 1)
        assert isclose(pointer[expected_flux], 1)
        print(f"mode={(j, 1-j)}, additive={additive}, flux pointer={pointer}")

    superposition = QuantumCircuit(2)
    superposition.h(0)
    state = basis.prepare((0, 1, 0)).evolve(superposition.compose(copy_flux))
    joint = state.readout("M", lambda mode: (2 * mode[0] + mode[1], 1 + mode[2]))
    assert isclose(joint[(1, 1)], 0.5) and isclose(joint[(2, 2)], 0.5)
    print(f"superposition, joint flux and pointer={joint}")


if __name__ == "__main__":
    main()
