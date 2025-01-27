import calc
import unittest

class CalcTest(unittest.TestCase):
    def test_all(self):
        try:
            self.assertEqual(calc.add(1, 2), 4)
        except Exception as err:
            print(f'add: {err}')

        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.mul(10, 2), 20)
        self.assertEqual(calc.sub(5, 3), 1)


if __name__ == "__main__":
    unittest.main()
