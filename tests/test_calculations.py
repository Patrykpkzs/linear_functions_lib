import unittest
from linear_functions.calculations import calculate_slope, calculate_intercept, solve_linear_equation

class TestCalculations(unittest.TestCase):
    def test_calculate_slope(self):
        self.assertEqual(calculate_slope((0, 0), (1, 1)), 1)
        self.assertEqual(calculate_slope((-1, -1), (1, 1)), 1)

    def test_calculate_intercept(self):
        self.assertEqual(calculate_intercept((0, 1), 2), 1)

    def test_solve_linear_equation(self):
        self.assertEqual(solve_linear_equation(2, 3, 7), 2)
