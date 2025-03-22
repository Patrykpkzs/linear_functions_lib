import unittest
from linear_functions.plotting import plot_linear_function

class TestPlotting(unittest.TestCase):
    def test_plot_function(self):
        plot_linear_function(1, 0)