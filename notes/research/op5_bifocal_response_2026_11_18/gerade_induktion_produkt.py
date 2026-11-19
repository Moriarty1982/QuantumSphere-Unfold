"""Check the product resolvent and the bound for even form degrees."""

from fractions import Fraction
from math import comb, prod


def eigenvalue(degree):
    return degree * (degree + 1)


def central_binomial(n):
    return comb(2 * n, n)


def gaunt_weight(d, ell, m):
    s = (d + ell + m) // 2
    numerator = (2 * m + 1) * prod(central_binomial(s - p) for p in (d, ell, m))
    return Fraction(numerator, (2 * s + 1) * central_binomial(s))


def residue(m, poles, zeros):
    lam = eigenvalue(m)
    return Fraction(prod(lam - eigenvalue(q) for q in zeros),
                    prod(lam - eigenvalue(q) for q in poles if q != m))


def verify(d, ell):
    poles = range(abs(d - ell), d + ell + 1, 2)
    zeros = range(poles.start + 1, poles.stop - 1, 2)
    weights = {m: gaunt_weight(d, ell, m) for m in poles}
    assert sum(weights.values()) == 1
    assert all(residue(m, poles, zeros) == weights[m] for m in poles)
    if d not in weights:
        return False

    delta = eigenvalue(d)
    direct = (2*d + 1) * sum(weight / (delta - eigenvalue(m))
                             for m, weight in weights.items() if m != d) / weights[d]
    product_ratio = (2*d + 1) * (
        sum(Fraction(1, delta - eigenvalue(q)) for q in zeros)
        - sum(Fraction(1, delta - eigenvalue(q)) for q in poles if q != d)
    )
    assert product_ratio == direct

    k = d + 1
    h = ell // 2
    s = min(h, d - h)
    D = 2*d + 1
    bound = Fraction(1, D-2*s) - Fraction(1, D)
    bound += Fraction(1, 2*s+1) - Fraction(1, 2*h+1)
    c = k * D - Fraction(eigenvalue(ell), 2)
    beta = Fraction(1,k) + Fraction(4*k - 1, 2*c) - Fraction(1,D)
    assert -product_ratio <= bound < beta
    return True


if __name__ == "__main__":
    checked, finite_parts = 0, 0
    for ell in range(2, 33, 2):
        for d in range(50):
            finite_parts += verify(d, ell)
            checked += 1
    print(f"{checked} pole/residue comparisons, {finite_parts} finite parts and bounds passed.")
