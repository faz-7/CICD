import unittest

from add import add_numbers



class TestAddNumbers(unittest.TestCase):
    def test_add_numbers_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_numbers_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_numbers_positive_and_negative_numbers(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_add_numbers_zero_numbers(self):
        self.assertEqual(add_numbers(0, 0), 0)
