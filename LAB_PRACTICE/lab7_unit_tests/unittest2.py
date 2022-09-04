import unittest
import full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(full_name.full_name('Loiko', 'Egor', 'Leonidovich'), 'Loiko Egor Leonidovich')

    def test_big(self):
        self.assertEqual(full_name.full_name('LOIKO', 'EGOR', 'LEONIDOVICH'), 'Loiko Egor Leonidovich')

    def test_small(self):
        self.assertEqual(full_name.full_name('loiko', 'egor', 'leonidovich'), 'Loiko Egor Leonidovich')


if __name__ == '__main__':
    unittest.main()
