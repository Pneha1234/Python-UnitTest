import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        a, b = 10, 5
        result = calc.add(a, b)
        self.assertEqual(result, 15)

    def test_add_edge_cases(self):
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -5), -6)

    def test_subtract(self):
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -5), 4)

    def test_multiply(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -5), 5)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5)
        self.assertEqual(calc.divide(-5, 1), -5)
        self.assertEqual(calc.divide(-5, -1), 5)
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertRaises(ValueError, calc.divide, 10, 0)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()
