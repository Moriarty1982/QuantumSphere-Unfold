"""Explore a common phase pointer coupled locally to two flux registers."""

from math import cos, isclose, pi

from qiskit import QuantumCircuit

from qam.simulation import Basis


def pointer_readout(fluxes, angles, superpose=False):
    labels = tuple((n, r, bit) for bit in (0, 1) for n, r in fluxes)
    basis = Basis("M", labels)
    circuit = QuantumCircuit(2)
    if superpose:
        circuit.h(0)
    circuit.h(1)
    for channel, angle in enumerate(angles):
        first, second = (pair[channel] for pair in fluxes)
        circuit.p(angle * first, 1)
        circuit.cp(angle * (second - first), 0, 1)
    circuit.h(1)
    if superpose:
        circuit.h(0)
    state = basis.prepare((*fluxes[0], 0)).evolve(circuit)
    return state.readout("M", lambda label: label)


def main():
    angle = pi / 12
    aliases = pointer_readout(((1, -1), (7, 5)), (angle, angle), superpose=False)
    shifted = pointer_readout(((7, 5), (1, -1)), (angle, angle), superpose=False)
    assert isclose(aliases[(1, -1, 0)], 1)
    assert isclose(shifted[(7, 5, 1)], 1)
    print("j=0 -> pointer 0; j=6 -> pointer 1")
    for delta in (0, pi / 6, pi / 2):
        distribution = pointer_readout(((1, -1), (-1, 1)), (angle + delta, angle), True)
        plus = sum(p for (n, _, _), p in distribution.items() if n == 1)
        assert isclose(plus, (1 + cos(delta) ** 2) / 2)
        print(f"delta/pi={delta / pi:g}, interference plus={plus:g}")


if __name__ == "__main__":
    main()
