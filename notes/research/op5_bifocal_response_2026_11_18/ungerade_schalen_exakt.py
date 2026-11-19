"""Exact intrinsic Dirac shell increments for odd form degrees 5 and 7."""

from math import prod

import sympy as sp

K, M = sp.symbols("k m")
FIELD = sp.QQ.frac_field(K)
ONE = sp.Poly(1, M, domain=FIELD)
ZERO = sp.Poly(0, M, domain=FIELD)


def c_squared(orbital, order):
    return (orbital**2 - order**2) / (4 * orbital**2 - 1)


def factored_legendre(orbital, order, degree):
    """Coefficients after removing the product on the shortest path."""
    previous, current = {}, {0: ONE}
    for step in range(degree):
        following = {}

        def add(offset, value):
            following[offset] = following.get(offset, ZERO) + value

        for offset, coefficient in current.items():
            weight = coefficient * sp.Rational(2 * step + 1, step + 1)
            up = c_squared(orbital + offset + 1, order) if offset < 0 else 1
            down = c_squared(orbital + offset, order) if offset > 0 else 1
            add(offset + 1, weight * sp.Poly(up, M, domain=FIELD))
            add(offset - 1, weight * sp.Poly(down, M, domain=FIELD))
        for offset, coefficient in previous.items():
            add(offset, -sp.Rational(step, step + 1) * coefficient)
        previous, current = current, following
    return current


def polynomial_square_root(expression):
    numerator, denominator = sp.fraction(sp.factor(expression))

    def root(polynomial):
        constant, factors = sp.factor_list(polynomial, K, M)
        assert all(power % 2 == 0 for _, power in factors)
        return sp.sqrt(constant) * prod(factor ** (power // 2) for factor, power in factors)

    result = root(numerator) / root(denominator)
    return result if result.subs({K: 100, M: sp.S.Half}) > 0 else -result


def spin_squares(orbital, sign):
    upper = (orbital + sp.S.Half + M) / (2 * orbital + 1)
    return (upper, 1 - upper) if sign > 0 else (1 - upper, upper)


def magnetic_moment(degree):
    if degree % 2:
        return 0
    return sp.expand(
        (sp.bernoulli(degree + 1, K + sp.S.Half)
         - sp.bernoulli(degree + 1, -K + sp.S.Half)) / (degree + 1)
    )


def upper_trace(offset, sign, coefficients):
    upper_order, lower_order = M - sp.S.Half, M + sp.S.Half
    initial = spin_squares(K - 1, 1)
    final = spin_squares(K - 1 + offset, sign)

    def diagonal(index, order):
        return initial[index] * final[index] * prod(
            c_squared(K - 1 + t, order) for t in range(1, offset + 1)
        )

    a = diagonal(0, upper_order)
    b = diagonal(1, lower_order)
    upper, lower = coefficients[0][offset], coefficients[1][offset]
    cross = polynomial_square_root(a * b)
    weight = (sp.Poly(a, M, domain=FIELD) * upper**2
              + sp.Poly(b, M, domain=FIELD) * lower**2
              + 2 * sign * sp.Poly(cross, M, domain=FIELD) * upper * lower)
    return sp.factor(sum(value * magnetic_moment(power[0]) for power, value in weight.terms()))


def energy_kernel(k, nu):
    return k * (k + nu) / (2 * (k - nu))


def generic_increment(degree):
    coefficients = [factored_legendre(K - 1, M + shift, degree)
                    for shift in (-sp.S.Half, sp.S.Half)]
    total = 2 * K**2 / (2 * degree + 1)
    for upward in range(1, degree + 1, 2):
        trace = upper_trace(upward, 1, coefficients)
        total += (energy_kernel(K, K + upward) * trace
                  + energy_kernel(K, K - upward) * trace.subs(K, K - upward))
        if upward > 1:
            gap = upward - 1
            trace = upper_trace(upward, -1, coefficients)
            total += (energy_kernel(K, -K - gap) * trace
                      + energy_kernel(K, -K + gap) * trace.subs(K, K - gap))
    return sp.factor(total)


def orbital_coefficients(orbital, order, degree):
    if abs(order) > orbital:
        return {}
    previous, current = {}, {orbital: sp.S.One}
    for step in range(degree):
        following = {}

        def add(target, value):
            following[target] = following.get(target, 0) + value

        for l, value in current.items():
            weight = value * sp.Rational(2 * step + 1, step + 1)
            add(l + 1, weight * sp.sqrt(c_squared(l + 1, order)))
            if l > abs(order):
                add(l - 1, weight * sp.sqrt(c_squared(l, order)))
        for l, value in previous.items():
            add(l, -sp.Rational(step, step + 1) * value)
        previous, current = current, {l: sp.simplify(value) for l, value in following.items()}
    return current


def boundary_increment(k, degree):
    total = sp.Rational(2 * k**2, 2 * degree + 1)
    l = k - 1
    for m2 in range(-2 * k + 1, 2 * k, 2):
        magnetic = sp.Rational(m2, 2)
        initial = [sp.sqrt(value.subs(M, magnetic)) for value in spin_squares(l, 1)]
        upper, lower = [orbital_coefficients(l, magnetic + shift, degree)
                        for shift in (-sp.S.Half, sp.S.Half)]
        for target in upper.keys() | lower.keys():
            for sign in (1, -1):
                if abs(magnetic) > target + sign * sp.S.Half:
                    continue
                nu = target + 1 if sign > 0 else -target
                squares = spin_squares(target, sign)
                a, b = [sp.sqrt(value.subs(M, magnetic)) for value in squares]
                amplitude = sign * a * initial[0] * upper.get(target, 0)
                amplitude += b * initial[1] * lower.get(target, 0)
                total += energy_kernel(sp.Integer(k), nu) * sp.simplify(amplitude**2)
    return sp.simplify(total)


if __name__ == "__main__":
    for ell in (5, 7):
        interior = generic_increment(ell)
        assert interior == 0
        steps = [boundary_increment(k, ell) for k in range(1, ell + 1)]
        assert all(value > 0 for value in steps[: (ell - 1) // 2])
        assert all(value == 0 for value in steps[(ell - 1) // 2 :])
        print(f"ell={ell}: A = {steps}; interior = {interior}; plateau = {sum(steps)}", flush=True)
