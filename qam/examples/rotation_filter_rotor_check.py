"""Check the finite isotropic rotor Hamiltonian against its exact return block."""
from math import pi

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import expm
from scipy.special import sph_harm_y

from qam.tools.route_search import rotation_mean


def rotor_coordinates(cutoff):
    # Exact quadrature for products of two harmonics and one coordinate.
    heights, weights = leggauss(cutoff + 1)
    azimuths = 2 * pi * np.arange(2 * cutoff + 2) / (2 * cutoff + 2)
    height, phi = np.meshgrid(heights, azimuths, indexing="ij")
    theta = np.arccos(height.ravel())
    phi = phi.ravel()
    harmonics = np.column_stack([
        sph_harm_y(ell, m, theta, phi)
        for ell in range(cutoff + 1) for m in range(-ell, ell + 1)
    ])
    measure = np.repeat(weights, len(azimuths)) * (2 * pi / len(azimuths))
    axes = (np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta))
    return [harmonics.conj().T @ ((measure * axis)[:, None] * harmonics) for axis in axes]


def return_block(twice_spin, coordinates):
    j = twice_spin / 2
    m = np.arange(-j, j + 1)
    raising = np.diag(np.sqrt((j - m[:-1]) * (j + m[:-1] + 1)), -1)
    spin = ((raising + raising.T)/2, (raising - raising.T)/(2j), np.diag(m))
    hamiltonian = sum(np.kron(u, component) for u, component in zip(coordinates, spin))
    unitary = expm(-1j * pi / 2 * hamiltonian)
    dimension = twice_spin + 1
    return unitary[:dimension, :dimension]


def error(twice_spin, coordinates):
    a, b = rotation_mean(90, twice_spin)
    expected = (float(a) + float(b)*np.sqrt(2)) * np.eye(twice_spin + 1)
    return np.linalg.norm(return_block(twice_spin, coordinates) - expected, ord=2)


def main():
    coordinates = rotor_coordinates(5)
    for twice_spin in range(1, 6):
        deviation = error(twice_spin, coordinates)
        assert deviation < 1e-12
        print(f"2j={twice_spin}: K=5 return error={deviation:.3g}")
    print(f"2j=5: K=4 return error={error(5, rotor_coordinates(4)):.3g}")


if __name__ == "__main__":
    main()
