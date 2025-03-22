import unittest
from linear_functions.utils import is_point_on_line, find_parallel_line, find_perpendicular_line

class TestUtils(unittest.TestCase):
    def test_is_point_on_line(self):
        self.assertTrue(is_point_on_line((1, 3), 2, 1))

    def test_find_parallel_line(self):
        self.assertEqual(find_parallel_line(2, 3, (1, 5)), (2, 3))

    def test_find_perpendicular_line(self):
        self.assertEqual(find_perpendicular_line(2, 3, (1, 1)), (-0.5, 1.5))