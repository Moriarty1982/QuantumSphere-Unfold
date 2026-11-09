"""Compare single and composite swaps in a detuned two-energy block."""

from math import pi

import numpy as np
from scipy.linalg import expm


def swap_pulse(detuning, angles):
    """Apply signed Bloch rotation angles with a fixed detuning."""
    exchange = np.array([[0, 1], [1, 0]])
    difference = np.diag([1, -1])
    evolution = np.eye(2, dtype=complex)
    for angle in angles:
        generator = np.sign(angle) * exchange + detuning * difference
        evolution = expm(-0.5j * abs(angle) * generator) @ evolution
    return evolution


def main():
    target = -1j * np.array([[0, 1], [1, 0]])
    angles = (7 * pi / 3, -5 * pi / 3, pi / 3)
    assert np.linalg.norm(swap_pulse(0, angles) - target, 2) < 1e-12
    for detuning in (0.05, 0.025, 0.0125):
        simple = swap_pulse(detuning, (pi,))
        composite = swap_pulse(detuning, angles)
        simple_loss = abs(simple[0, 0]) ** 2
        composite_loss = abs(composite[0, 0]) ** 2
        error = np.linalg.norm(composite - target, 2)
        assert composite_loss < simple_loss and error < np.linalg.norm(simple - target, 2)
        print(f"detuning={detuning:g}: failure {simple_loss:.6g} -> {composite_loss:.6g}, "
              f"composite operator error={error:.6g}")


if __name__ == "__main__":
    main()
