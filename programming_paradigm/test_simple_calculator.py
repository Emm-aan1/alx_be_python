import unittest
from simple_calculator import SimpleCalculator

class Test_simple_calc(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, 11), 9)
        self.assertEqual(self.calc.add(-4, -9), -13)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-2, -5), 3)
        self.assertEqual(self.calc.subtract(-2, 5), -7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(10, 3), 30)
        self.assertEqual(self.calc.multiply(-7, -3), 21)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertRaises(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(0, 12), 0)