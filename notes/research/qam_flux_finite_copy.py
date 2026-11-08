"""Evaluate the echo pointer with a finite, drift-balanced copy pulse."""
from pathlib import Path

import numpy as np

from qam_flux_selective_pulse import ACCEPT, LABELS, propagators


def main():
    folder = Path(__file__).parent
    flip = np.loadtxt(folder / "qam_flux_common_flip_controls.txt").ravel()
    pulse = np.loadtxt(folder / "qam_flux_robust_controls.txt").ravel()
    offsets = np.linspace(-0.05, 0.05, 101)
    labels = (LABELS + offsets[:, None]).ravel()
    accept = np.tile(ACCEPT, len(offsets))
    gate = propagators(flip, labels)
    forward = propagators(pulse, labels)
    echo = gate @ propagators((pulse.reshape(-1, 2)[::-1] * [-1, 1]).ravel(), labels) @ gate

    copy_time = np.pi / 2  # g=1 in dimensionless units
    wait = 20 * np.pi - 60 - copy_time / 2
    time = 120 + wait + copy_time
    waiting = np.exp(-1j * labels[:, None] * wait * np.array([1, -1]))
    initial = (forward @ gate @ (waiting[:, :, None] * gate))[:, :, 0]
    state = np.zeros((len(labels), 2, 2), complex)
    state[:, :, 0] = initial
    half_flip = np.array([[1+1j, 1-1j], [1-1j, 1+1j]]) / 2
    drift = np.exp(-1j * labels[:, None] * (copy_time / 2) * np.array([1, -1]))
    for control in (1, 0):
        state[:, control, :] = state[:, control, :] @ half_flip
        state = gate @ (drift[:, :, None] * state)
    state = -(echo @ state) * np.exp(1j * labels * (time - 40 * np.pi))[:, None, None]
    expected = np.zeros_like(state)
    expected[np.arange(len(labels)), 0, accept.astype(int)] = 1
    wrong = state[np.arange(len(labels)), :, (~accept).astype(int)]
    print(f"max wrong probability: {max(np.sum(abs(wrong)**2, axis=1)):.9g}")
    print(f"max auxiliary leakage: {max(np.sum(abs(state[:, 1, :])**2, axis=1)):.9g}")
    print(f"max state error: {max(np.linalg.norm(state-expected, axis=(1, 2))):.9g}")


if __name__ == "__main__":
    main()
