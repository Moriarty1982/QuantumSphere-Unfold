"""Qiskit exploration of two area readouts in the n=1 sector.

Run with python after installing qiskit in the active environment.
"""
from math import pi

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


MODES = ((0, 1), (1, -1))


def area_distribution(probabilities, readout):
    distribution = {}
    for probability, (m1, m2) in zip(probabilities, MODES):
        area = readout(m1, m2)
        distribution[area] = distribution.get(area, 0.0) + float(probability)
    return distribution


def main():
    # V(phi) = g cos(phi) projects to g X/2 on these adjacent modes.
    # The Rz term represents the kinetic energy splitting, up to a phase.
    # Both angles are dimensionless integrated strengths in units of hbar.
    print("Areas in units of a_M")
    for angle in (0, pi / 2, pi):
        circuit = QuantumCircuit(1)
        circuit.rx(angle, 0)
        circuit.rz(-pi / 3, 0)
        probabilities = Statevector.from_instruction(circuit).probabilities()
        additive = area_distribution(probabilities, lambda m1, m2: abs(m1) + abs(m2))
        mixed = area_distribution(probabilities, lambda m1, m2: 3 * abs(2 * m1 + m2) / 5)
        print(f"angle/pi={angle / pi:g}")
        for label, distribution in (("additive", additive), ("mixed", mixed)):
            outcomes = ", ".join(
                f"{area:g}: {probability:.6f}"
                for area, probability in sorted(distribution.items())
            )
            print(f"  {label}: {outcomes}")


if __name__ == "__main__":
    main()
