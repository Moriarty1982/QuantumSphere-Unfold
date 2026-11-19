"""Symbolic checks for the bifocal radial probe shape in a common chart."""

import sympy as sp


def main():
    a, w, mu = sp.symbols("a w mu", positive=True)
    c, v, k1, k2 = sp.symbols("c v k1 k2")
    radius = a + v*w**2

    def shift(sign):
        distance = sp.sqrt(radius**2 + w**2 + sign*2*radius*w*c)
        return sp.series(distance, w, 0, 3).removeO() - a

    def kernel(offset):
        return sp.series(k1*offset + k2*offset**2/2, w, 0, 3).removeO()

    total = sp.expand(kernel(shift(1)) + kernel(shift(-1)))
    assert sp.simplify(total.coeff(w, 2) -
                       (2*k1*v + k1*(1-c**2)/a + k2*c**2)) == 0
    difference = sp.expand(kernel(shift(1)) - kernel(shift(-1)))
    assert difference.coeff(w, 1) == 2*k1*c

    target = (k2/k1 - 1/a)*(1-c**2)/2
    assert sp.simplify(total.coeff(w, 2).subs(v, target) - k2) == 0
    assert sp.simplify(target.subs(k2, 0) + (1-c**2)/(2*a)) == 0

    yukawa = sp.exp(-mu*a)/a
    multiplier = 1 - a*sp.diff(yukawa, a, 2)/sp.diff(yukawa, a)
    assert sp.simplify(multiplier - (mu*a + 2 + 1/(1+mu*a))) == 0
    assert multiplier.subs(mu, 0) == 3

    b_squared = a**2 - 3*w**2 + w**4/a**2
    pole_sum = 1/(a+w) + 1/(a-w)
    equator_sum = 2*a/(a**2-w**2)  # a > w and b_squared > 0
    assert sp.factor(b_squared + w**2 - (a-w)**2*(a+w)**2/a**2) == 0
    assert sp.simplify(pole_sum - equator_sum) == 0

    x, y = sp.symbols("x y", real=True)
    distances = sp.Matrix([sp.sqrt((x+w)**2+y*y), sp.sqrt((x-w)**2+y*y)])
    determinant = distances.jacobian([x, y]).det()
    assert sp.simplify(determinant - 2*w*y / sp.prod(distances)) == 0
    print("Passed: odd/even coefficients, affine and Yukawa response, Coulomb section and rank.")


if __name__ == "__main__":
    main()
