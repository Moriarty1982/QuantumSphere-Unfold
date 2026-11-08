"""Verify the actual axis-mean blocks and their polynomial on the OP1 carrier."""

from math import pi, sqrt

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm


def rotation_terms(twice_spin, cutoff):
    j = twice_spin / 2
    m = np.arange(-j, j + 1)
    raising = np.diag(np.sqrt((j - m[:-1]) * (j + m[:-1] + 1)), -1)
    x = (raising + raising.T) / 2
    y = (raising - raising.T) / (2j)
    z = np.diag(m)
    heights, weights = leggauss(cutoff // 2 + 1)
    azimuths = 2 * pi * np.arange(cutoff + 1) / (cutoff + 1)
    for height, weight in zip(heights, weights):
        radius = sqrt(1 - height**2)
        for phi in azimuths:
            spin = radius * (np.cos(phi) * x + np.sin(phi) * y) + height * z
            yield weight / (2 * len(azimuths)), expm(-1j * pi * spin / 2)


def rotation_mean(twice_spin, cutoff):
    return sum(weight * matrix for weight, matrix in rotation_terms(twice_spin, cutoff))


def main():
    target = 1 / sqrt(2)
    roots = (-1/5, -sqrt(2)/6, 0, 1/3)
    for twice_spin in range(1, 6):
        mean = rotation_mean(twice_spin, cutoff=5)
        identity = np.eye(twice_spin + 1)
        character = np.sin((twice_spin + 1) * pi / 4) / ((twice_spin + 1) * target)
        filtered = identity
        for root in roots:
            filtered = filtered @ ((mean - root * identity) / (target - root))
        mean_error = np.linalg.norm(mean - character * identity, ord=2)
        filter_error = np.linalg.norm(filtered - int(twice_spin == 1) * identity, ord=2)
        assert max(mean_error, filter_error) < 1e-12
        print(f"2j={twice_spin}: mean error={mean_error:.3g}, filter error={filter_error:.3g}")


if __name__ == "__main__":
    main()
