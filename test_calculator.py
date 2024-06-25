import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):
    def test_multiply_integers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_floats(self):
        self.assertAlmostEqual(multiply(2.5, 4.2), 10.5, places=1)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(-1, -5), 5)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
