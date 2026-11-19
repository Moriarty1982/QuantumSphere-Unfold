"""Check the odd plateau proof against the exact spin-Wigner increments."""

from fractions import Fraction
from math import comb

from sympy import Symbol, expand

from wigner_schalen import increment, plateau_candidate


def p(k, ell):
    return (ell + 1 - 2*k) * (ell + 2*k)


def g(k, ell):
    return (k - 1) * (8*k**2 - ell*(ell + 1)) / 64


def constant(ell):
    return (ell - 1) * ell * (ell + 1) * (ell + 2) / 64


def half_binomial(j):
    return Fraction(comb(2*j, j), 4**j)


def resolvent_increment(k, ell):
    n = (ell - 1) // 2
    ratio = Fraction(1)
    for j in range(1, n + 1):
        ratio *= Fraction(2*j, 2*j + 1)
    weight = half_binomial(n + 1 - k) * half_binomial(n + k)
    return Fraction(k**2 * p(k, ell), 2*ell + 1) * ratio**2 * weight


def main():
    k, ell = Symbol("k"), Symbol("ell")
    assert expand(p(k, ell) * g(k + 1, ell)
                  - p(1 - k, ell) * g(k, ell)
                  - k**2 * p(k, ell) / 2 + constant(ell)) == 0

    checked = 0
    for ell in range(3, 44, 2):
        n = (ell - 1) // 2
        values = []
        for k in range(1, n + 2):
            value = resolvent_increment(k, ell)
            assert value == increment(k, ell), (k, ell)
            values.append(value)
        assert values[-1] == 0
        assert sum(values) == plateau_candidate(ell), ell
        checked += len(values)
    print(f"Polynomial identity, {checked} exact increments and 21 plateaus passed.")


if __name__ == "__main__":
    main()
