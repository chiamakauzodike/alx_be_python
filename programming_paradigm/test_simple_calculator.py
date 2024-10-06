import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2,-2), -5)
        self.assertEqual(self.calc.add(1.5, 3.5), 4.5)


        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
    def test_multiply(self):
        self.assertEqual(self.calc.subtract(2, 3), 5)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)


    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 3), 5)
        self.assertEqual(self.calc.divide(-2, -3), -5)
        with self.assertionRaise(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()


