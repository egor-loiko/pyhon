import unittest
import calc


class CalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Hello class")

    @classmethod
    def tearDownClass(cls):
        print("Good bye class")

    def setUp(self):
        print("Hello method")

    def tearDown(self):
        print("Good bye method")

    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)  # add assertion here
        print("Test add")

    def test_sub(self):
        self.assertEqual(calc.sub(5, 2), 3)
        print("Test sub")

    def test_sub2(self):
        self.assertGreater(calc.sub(5, 2), 2.9)
        print("Test sub2")

if __name__ == '__main__':
    unittest.main()
