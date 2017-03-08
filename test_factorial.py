import factor1
import unittest

class BaseTest(unittest.TestCase):
    def test_one(self):
        ''' should return f(1) == 1 '''
        self.assertEqual(1, factor1.f(1))

    def test_three(self):
        ''' should return f(3) == 6 '''
        self.assertEqual(6, factor1.f(3))

    def test_one(self):
        ''' should return f(6) == 720 '''
        self.assertEqual(720, factor1.f(6))

    def test_zero(self):
        ''' should return f(0) == 1 '''
        self.assertEqual(1, factor1.f(0))

    def test_negative(self):
        ''' should raise AgrumentError on negative numbers '''
        self.assertRaises(factor1.ArgumentError, factor1.f, -1)

if __name__ == "__main__":
    unittest.main()
