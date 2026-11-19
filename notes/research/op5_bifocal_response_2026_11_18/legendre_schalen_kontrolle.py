"""Check the Legendre-resolvent identity against exact Wigner weights."""

from fractions import Fraction
from functools import lru_cache

from sympy import Poly, Symbol, legendre

from wigner_schalen import increment

X = Symbol("x")


@lru_cache(None)
def coefficients(degree):
    return {power[0]: Fraction(value) for power, value in Poly(legendre(degree, X), X).terms()}


@lru_cache(None)
def moment(degree, power):
    if power < degree or (power + degree) % 2:
        return Fraction(0)
    return sum(
        Fraction(2, power + exponent + 1) * coefficient
        for exponent, coefficient in coefficients(degree).items()
    )


def integral_q(k, ell):
    d = k - 1
    return sum(
        coefficient * sum(moment(d, exponent - 1 - j) * moment(d, j)
                          for j in range(exponent))
        for exponent, coefficient in coefficients(ell).items()
    ) / 4


def kernel_increment(k, ell):
    factor = k * (2*k - 1) - Fraction(ell*(ell + 1), 2)
    return -Fraction(k*k, 2*ell + 1) * factor * integral_q(k, ell)


if __name__ == "__main__":
    tested = 0
    for ell in range(1, 22, 2):
        for k in range(1, 21):
            assert kernel_increment(k, ell) == increment(k, ell)
            if ell <= 2*k - 1:
                assert kernel_increment(k, ell) == 0
            tested += 1
    print(f"{tested} exact Wigner/Legendre comparisons passed.")
