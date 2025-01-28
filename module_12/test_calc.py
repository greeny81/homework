import calc
import unittest

class CalcTest(unittest.TestCase): # TEST CASE
    def setUp(self):#перед каждым тестом
        print('Setup')

    @classmethod
    def setUpClass(cls):# 1 раз Перед тест кейсом Например подключение к БД
        print('Setup Class')

    def tearDown(self):# В конце
        print('Tear')
        pass
    @classmethod
    def tearDownClass(cls):
        print('Tear Class')


    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_next(self):
        self.assertEqual(calc.div(10, 5), 2, 'calc msg')

    def test_test(self):
        self.assertIsNone(None)
        self.assertIn('a', 'sadfe')
        self.assertAlmostEqual(0.45454567, 0.45454568)



if __name__ == "__main__":
    unittest.main()
