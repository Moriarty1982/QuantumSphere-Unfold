"""Find a common phase-matched X gate for the transfer blocks."""
import numpy as np
from scipy.optimize import least_squares

from pathlib import Path

from qam_flux_selective_pulse import ACCEPT, DURATION, LABELS, propagators

TARGET = -1j * np.array([[0, 1], [1, 0]])


def gate_errors(controls, offsets):
    labels = (LABELS + np.asarray(offsets)[:, None]).ravel()
    return propagators(controls, labels) - TARGET


def common_flip():
    def residual(controls):
        errors = gate_errors(controls, [-0.05, 0, 0.05])
        return np.concatenate((errors.real.ravel(), errors.imag.ravel()))

    initial = np.random.default_rng(19).normal(0, 0.5, 64)
    fit = least_squares(residual, initial, bounds=(-4, 4), max_nfev=300,
                        ftol=1e-11, xtol=1e-11, gtol=1e-11)
    return fit.x


def full_pointer(flip, selective, offsets):
    labels = (LABELS + offsets[:, None]).ravel()
    accept = np.tile(ACCEPT, len(offsets))
    flip_time = DURATION * (len(flip) // 2)
    pulse_time = DURATION * (len(selective) // 2)
    wait = 15 * np.pi - pulse_time - 2 * flip_time
    common = propagators(flip, labels)
    forward = propagators(selective, labels)
    mirrored = selective.reshape(-1, 2)[::-1] * [-1, 1]
    echo = common @ propagators(mirrored.ravel(), labels) @ common
    waiting = np.zeros_like(common)
    waiting[:, 0, 0] = np.exp(-1j * labels * wait)
    waiting[:, 1, 1] = np.exp(1j * labels * wait)
    before_copy = forward @ common @ waiting @ common
    branches = before_copy[:, :, 0, None] * echo.transpose(0, 2, 1)
    # With +label*Z the unshifted level has centered energy +label.
    # Restore each block trace relative to unshifted idle evolution.
    time = 2 * pulse_time + 4 * flip_time + wait
    branches *= np.exp(1j * labels * (time - 30 * np.pi))[:, None, None]
    expected = np.zeros_like(branches)
    expected[np.arange(len(labels)), accept.astype(int), 0] = 1
    errors = np.linalg.norm((branches - expected).reshape(len(labels), -1), axis=1)
    wrong = np.sum(abs(branches[np.arange(len(labels)), (~accept).astype(int)])**2, axis=1)
    leakage = np.sum(abs(branches[:, :, 1])**2, axis=1)
    print(f"full pointer max state error: {max(errors):.9g}")
    print(f"full pointer max wrong probability: {max(wrong):.9g}")
    print(f"full pointer max auxiliary leakage: {max(leakage):.9g}")


def main():
    controls = common_flip()
    offsets = np.linspace(-0.05, 0.05, 101)
    errors = np.linalg.norm(gate_errors(controls, offsets), ord=2, axis=(-2, -1))
    print(f"max sampled operator error: {max(errors):.9g}")
    print(f"max nominal operator error: {max(errors.reshape(101, -1)[50]):.9g}")


    table = Path(__file__).with_name("qam_flux_robust_controls.txt")
    full_pointer(controls, np.loadtxt(table).ravel(), offsets)


if __name__ == "__main__":
    main()
