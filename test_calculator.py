import unittest

from calculator import add, calculate, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtraction_with_negative_number(self):
        self.assertEqual(subtract(-2, 3), -5)

    def test_multiplication(self):
        self.assertEqual(multiply(4, 2), 8)

    def test_division(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(calculate("add", 0.1, 0.2), 0.3)

    def test_division_by_zero(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
