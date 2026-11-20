"""Qiskit check for the two-level J=0,1 truncation of an oriented rotor."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Pauli, Statevector

orientation_operator = Pauli("X")
for field_over_rotational_constant in (0.0, 0.1, -0.1):
    # Ground state of [[0, -f/sqrt(3)], [-f/sqrt(3), 2B]].
    angle = np.arctan(field_over_rotational_constant / np.sqrt(3))
    circuit = QuantumCircuit(1)
    circuit.ry(angle, 0)
    state = Statevector.from_label("0").evolve(circuit)
    dipole_factor = state.expectation_value(orientation_operator).real / np.sqrt(3)
    expected = field_over_rotational_constant / np.sqrt(
        9 + 3 * field_over_rotational_constant**2
    )
    np.testing.assert_allclose(dipole_factor, expected, atol=1e-14)
    print(f"f/B = {field_over_rotational_constant:+.1f}, <cos(theta)> = {dipole_factor:+.10f}")
