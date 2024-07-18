import unittest
from simple_calculator import SimpleCalculator

class testCalc(unittest.TestCase):

    def setUp(self):
        """initialize the class"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(4, 1), 5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(60,-50), 110)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6,0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,6), 1)
        self.assertEqual(self.calc.divide(6,0),None)
