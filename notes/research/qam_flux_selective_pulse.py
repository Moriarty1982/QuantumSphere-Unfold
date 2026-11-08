"""Numerical pulse exploration for five detunings, in dimensionless units."""
import numpy as np
from scipy.optimize import least_squares

LABELS = np.array([-3, -1, 1, 2, 3])
ACCEPT = np.abs(LABELS) == 3
DURATION = 0.5


def propagators(controls, labels=LABELS):
    result = np.broadcast_to(np.eye(2, dtype=complex), (len(labels), 2, 2)).copy()
    for x, y in controls.reshape(-1, 2):
        rate = np.sqrt(x*x + y*y + labels**2)
        scale = -1j * np.sin(DURATION * rate) / rate
        pulse = np.zeros_like(result)
        pulse[:, 0, 0] = np.cos(DURATION * rate) + scale * labels
        pulse[:, 1, 1] = np.cos(DURATION * rate) - scale * labels
        pulse[:, 0, 1] = scale * (x - 1j*y)
        pulse[:, 1, 0] = scale * (x + 1j*y)
        result = pulse @ result
    return result


def residual(controls):
    state = propagators(controls)[:, :, 0]
    unwanted = state[np.arange(len(LABELS)), (~ACCEPT).astype(int)]
    return np.concatenate((unwanted.real, unwanted.imag))


def pointer_branches(unitaries):
    """Return [block, pointer outcome, auxiliary amplitude] after uncomputation."""
    initial = unitaries[:, :, 0]
    return initial[:, :, None] * unitaries.conj()


def robust_pulse():
    offsets = np.array([-0.05, 0, 0.05])
    labels = (LABELS + offsets[:, None]).ravel()
    accept = np.tile(ACCEPT, len(offsets))

    def error(controls):
        unwanted = propagators(controls, labels)[np.arange(len(labels)), (~accept).astype(int), 0]
        return np.concatenate((unwanted.real, unwanted.imag))

    initial = np.random.default_rng(19).normal(0, 0.5, 48)
    return least_squares(error, initial, bounds=(-4, 4), max_nfev=200).x


def sweep_error(controls, offsets):
    labels = (LABELS + offsets[:, None]).ravel()
    wrong = np.tile(~ACCEPT, len(offsets)).astype(int)
    return abs(propagators(controls, labels)[np.arange(len(labels)), wrong, 0])**2


def main():
    initial = np.random.default_rng(19).normal(0, 0.5, 32)
    fit = least_squares(residual, initial, bounds=(-4, 4), max_nfev=200,
                        ftol=1e-12, xtol=1e-12, gtol=1e-12)
    flip = abs(propagators(fit.x)[:, 1, 0])**2
    for label, probability in zip(LABELS, flip):
        print(f"{label:+}: flip={probability:.12f}")
    print(f"max wrong probability={np.max(np.abs(flip - ACCEPT)):.3g}")

    branches = pointer_branches(propagators(fit.x))
    expected = np.zeros_like(branches)
    expected[np.arange(len(LABELS)), ACCEPT.astype(int), 0] = 1
    error = np.linalg.norm((branches - expected).reshape(len(LABELS), -1), axis=1)
    print(f"max full pointer state error={max(error):.3g}")
    for offset in (0.01, 0.05, 0.1):
        shifted = propagators(fit.x, LABELS + offset)
        wrong = abs(shifted[np.arange(len(LABELS)), (~ACCEPT).astype(int), 0])**2
        print(f"common detuning offset={offset:g}: max wrong probability={max(wrong):.6g}")


    offsets = np.linspace(-0.05, 0.05, 101)
    validation_offsets = offsets[~np.isclose(offsets[:, None], [-0.05, 0, 0.05]).any(axis=1)]
    robust = robust_pulse()
    print(f"nominal sequence, validation max wrong={max(sweep_error(fit.x, validation_offsets)):.6g}")
    print(f"robust sequence, validation max wrong={max(sweep_error(robust, validation_offsets)):.6g}")
    sampled_max = max(sweep_error(robust, offsets))
    print(f"robust sequence, sampled max wrong={sampled_max:.6g}")
    duration = DURATION * (robust.size // 2)
    spacing = max(np.diff(offsets))
    interpolation_bound = (np.sqrt(sampled_max) + duration**2 * spacing**2 / 8)**2
    print(f"interval bound from sampled amplitudes={interpolation_bound:.6g}")
    print(f"robust sequence, nominal max wrong={max(sweep_error(robust, np.array([0.0]))):.6g}")


if __name__ == "__main__":
    main()
