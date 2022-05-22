import unittest
from unittest import result

from pysto.utils.special_functions import binomial_coefficient, factorial, factorial2, generalized_binomial_coefficient


class TestFactorial(unittest.TestCase):
    def test_factorial_negative_argument(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_zero(self):
        expected = 1.0
        result = factorial(0)
        self.assertAlmostEqual(expected, result)

    def test_factorial(self):
        expected = 6.0
        result = factorial(3)
        self.assertAlmostEqual(expected, result)


class TestFactorial2(unittest.TestCase):
    def test_factorial2_negative_argument(self):
        with self.assertRaises(ValueError):
            factorial2(-1)

    def test_factorial2_zero(self):
        expected = 1.0
        result = factorial2(0)
        self.assertAlmostEqual(expected, result)

    def test_factorial2(self):
        expected = 3.0
        result = factorial2(3)
        self.assertAlmostEqual(expected, result)


class TestBinomialCoefficient(unittest.TestCase):
    def test_binomial_coefficient_wrong_arguments(self):
        with self.assertRaises(ValueError):
            binomial_coefficient(1, 2)

    def test_binomial_coefficient(self):
        expected = 10.0
        result = binomial_coefficient(5, 2)
        self.assertAlmostEqual(expected, result)
        print("Test binomial coefficients")

class TestGeneralizedBinomialCoefficient(unittest.TestCase):
    def test_generalized_binomial_coefficient_wrong_arguments(self):
        with self.assertRaises(ValueError):
            generalized_binomial_coefficient(1, 1, 3)
    def test_generalized_binomial_coefficient(self):
        pass
