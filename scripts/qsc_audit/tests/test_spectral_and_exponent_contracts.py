"""Algebraic regression examples, not certificates for native MM/HC data.

Run: python -B -m unittest scripts.qsc_audit.tests.test_spectral_and_exponent_contracts
The zero ordinate below is a fixed numerical input, not a zero-location proof.
"""

from fractions import Fraction
import math
import unittest


FIRST_ZERO_ORDINATE = 14.134725141734694


def diagonal(entries):
    return tuple(tuple(value if i == j else 0 for j in range(len(entries)))
                 for i, value in enumerate(entries))


def multiply(left, right):
    return tuple(tuple(sum(a*b for a, b in zip(row, column))
                       for column in zip(*right)) for row in left)


def scale(value, matrix):
    return tuple(tuple(value*entry for entry in row) for row in matrix)


def inverse_exponent(g, beta):
    if not g > 1 or not 0 < beta < 1/math.sqrt(3):
        raise ValueError("Need g > 1 and 0 < beta < 1/sqrt(3).")
    size = FIRST_ZERO_ORDINATE/(4*math.pi*abs(math.log(beta*math.sqrt(3))))
    return math.log(size)/math.log(g), size


class SpectralContractTests(unittest.TestCase):
    def test_commutation_and_diagonalizability_do_not_force_scalar_action(self):
        matrix = diagonal([1, 2, 3])
        projection = diagonal([1, 1, 0])
        self.assertEqual(multiply(matrix, projection), multiply(projection, matrix))
        self.assertNotEqual(multiply(matrix, projection), projection)
        self.assertNotEqual(multiply(matrix, projection), scale(2, projection))

    def test_single_eigenvalue_without_diagonalizability_is_insufficient(self):
        jordan = ((2, 1), (0, 2))
        nilpotent = ((0, 1), (0, 0))
        self.assertEqual(multiply(nilpotent, nilpotent), diagonal([0, 0]))
        self.assertNotEqual(jordan, diagonal([2, 2]))

    def test_scalar_image_can_be_only_part_of_full_eigenspace(self):
        matrix = diagonal([2, 2, 3])
        projection = diagonal([1, 0, 0])
        full_eigenprojection = diagonal([1, 1, 0])
        self.assertEqual(multiply(matrix, projection), scale(2, projection))
        self.assertEqual(multiply(projection, matrix), scale(2, projection))
        self.assertNotEqual(projection, full_eigenprojection)

    def test_orthogonal_noncoordinate_example_satisfies_repaired_theorem(self):
        half = Fraction(1, 2)
        projection = ((half, half, 0), (half, half, 0), (0, 0, 1))
        matrix = ((Fraction(5, 2), -half, 0), (-half, Fraction(5, 2), 0), (0, 0, 2))
        complement = ((half, -half, 0), (-half, half, 0), (0, 0, 0))
        self.assertEqual(multiply(projection, projection), projection)
        self.assertEqual(multiply(matrix, projection), scale(2, projection))
        self.assertEqual(multiply(projection, matrix), scale(2, projection))
        self.assertEqual(multiply(matrix, complement), scale(3, complement))
        self.assertEqual(multiply(projection, complement), diagonal([0, 0, 0]))

    def test_projection_does_not_determine_complementary_matrix(self):
        projection = diagonal([1, 1, 0])
        first, second = diagonal([2, 2, 3]), diagonal([2, 2, 4])
        self.assertNotEqual(first, second)
        self.assertEqual(multiply(first, projection), scale(2, projection))
        self.assertEqual(multiply(second, projection), scale(2, projection))


class ExponentContractTests(unittest.TestCase):
    def test_back_substitution_is_identity_for_distinct_frame_inputs(self):
        exponents = []
        for g in (1.5, 1.7, 1.864, 1.95):
            beta = math.sqrt((g-1)/(g+1))
            exponent, size = inverse_exponent(g, beta)
            self.assertTrue(math.isclose(g**exponent, size, rel_tol=1e-13))
            exponents.append(exponent)
        self.assertGreater(max(exponents)-min(exponents), 2)

    def test_rounded_beta_and_frame_constrained_beta_give_different_inverse_exponents(self):
        g = 1.864
        rounded, _ = inverse_exponent(g, 0.5493)
        constrained, _ = inverse_exponent(g, math.sqrt((g-1)/(g+1)))
        self.assertAlmostEqual(rounded, 5.0058433160719, places=11)
        self.assertAlmostEqual(constrained, 5.0029330844170, places=11)
        self.assertGreater(abs(rounded-constrained), 0.002)

    def test_inverse_exponent_domain(self):
        for g, beta in ((1, 0.5), (0.5, 0.5), (1.5, 0), (1.5, 1/math.sqrt(3))):
            with self.assertRaises(ValueError):
                inverse_exponent(g, beta)

    def test_derivative_lower_bound_has_exact_nonnegative_factorization(self):
        for t in (Fraction(101, 100), Fraction(3, 2), Fraction(2), Fraction(4), Fraction(10)):
            polynomial = t**3-Fraction(27, 4)*(t-1)
            self.assertEqual(polynomial, (t-Fraction(3, 2))**2*(t+3))
            self.assertGreaterEqual(t**3/(t-1), Fraction(27, 4))

    def test_fixed_fifth_power_ansatz_has_the_reported_model_root(self):
        a = FIRST_ZERO_ORDINATE/(4*math.pi)
        self.assertLess(5*a, 27/4)

        def residual(g):
            return math.log(3)/2+math.log((g-1)/(g+1))/2+a/g**5

        low, high = 1.000001, 2.0
        self.assertLess(residual(low), 0)
        self.assertGreater(residual(high), 0)
        for _ in range(80):
            middle = (low+high)/2
            if residual(middle) < 0:
                low = middle
            else:
                high = middle
        root = (low+high)/2
        self.assertAlmostEqual(root, 1.8636622498890613, places=13)
        self.assertAlmostEqual(math.sqrt((root-1)/(root+1)), 0.5491753954177569, places=13)
        self.assertLess(abs(residual(root)), 1e-14)


if __name__ == "__main__":
    unittest.main()
