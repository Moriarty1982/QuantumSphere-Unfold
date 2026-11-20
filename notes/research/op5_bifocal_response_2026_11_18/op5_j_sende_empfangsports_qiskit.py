"""Qiskit check of coherent ideal J/reference mode propagation."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Statevector

kinetic = np.array([[1, 0.25], [0.25, 1]])
charge = np.array([1, -2])
eigenvalues, eigenvectors = np.linalg.eigh(kinetic)
inverse_sqrt = (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.T
electron = inverse_sqrt @ charge
electron /= np.linalg.norm(electron)
dark = np.array([-electron[1], electron[0]])
phase = np.pi / 3
propagation = np.eye(2) + np.expm1(1j * phase) * np.outer(electron, electron)

circuit = QuantumCircuit(1)
circuit.append(UnitaryGate(propagation), [0])
electron_output = Statevector(electron).evolve(circuit).data
dark_output = Statevector(dark).evolve(circuit).data
basis_output = Statevector.from_label("0").evolve(circuit).data

electron_phase = np.angle(np.vdot(electron, electron_output))
dark_phase = np.angle(np.vdot(dark, dark_output))
dark_leakage = abs(np.vdot(dark, electron_output)) ** 2
basis_conversion = abs(basis_output[1]) ** 2
expected_conversion = 4 * np.sin(phase / 2) ** 2 * np.prod(electron**2)

np.testing.assert_allclose(electron_phase, phase, atol=1e-12)
np.testing.assert_allclose(dark_phase, 0, atol=1e-12)
np.testing.assert_allclose(dark_leakage, 0, atol=1e-24)
np.testing.assert_allclose(basis_conversion, expected_conversion, atol=1e-12)
print(f"electron channel phase [rad] = {electron_phase:.12f}")
print(f"dark channel absolute phase [rad] = {abs(dark_phase):.12f}")
print(f"electron -> dark probability = {dark_leakage:.3e}")
print(f"basis 0 -> basis 1 probability = {basis_conversion:.12f}")
