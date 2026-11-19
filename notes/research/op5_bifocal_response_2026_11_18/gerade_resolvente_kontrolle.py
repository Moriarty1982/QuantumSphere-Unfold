"""Exact even-degree comparison between scalar and spinor transition sums."""

from fractions import Fraction

from sympy.physics.wigner import wigner_3j

from wigner_schalen import increment


def scalar_terms(k, ell):
    d = k - 1
    c = k * (2*k - 1) - Fraction(ell*(ell + 1), 2)
    inverse_moment = Fraction(0)
    diagonal_moment = Fraction(0)
    for m in range(abs(d-ell), d+ell+1, 2):
        weight = Fraction(wigner_3j(d, ell, m, 0, 0, 0)**2)
        if m == d:
            diagonal_moment = 2 * weight
        else:
            inverse_moment += Fraction(2*(2*m+1), d*(d+1)-m*(m+1)) * weight
    coefficient = Fraction(2*k-1, 2) + Fraction(ell*(ell+1), 2*(2*k-1)) + c/k
    value = Fraction(k*k, 2*ell+1) * (c*inverse_moment + coefficient*diagonal_moment)
    return value, inverse_moment, diagonal_moment


if __name__ == "__main__":
    extrema = []
    for ell in range(2, 23, 2):
        ratios = []
        for k in range(1, 31):
            value, inverse_moment, diagonal_moment = scalar_terms(k, ell)
            assert value == increment(k, ell), (k, ell, value, increment(k, ell))
            if diagonal_moment:
                ratios.append((inverse_moment / diagonal_moment, k))
        extrema.append((ell, min(ratios), max(ratios)))
    print("330 exact comparisons passed.")
    for item in extrema:
        print(item)
