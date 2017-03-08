import fib
import unittest

class BaseTest(unittest.TestCase):
    def test_one(self):
        ''' should return f(1) == 1 '''
        self.assertEqual(1, fib.fib(1))

    def test_three(self):
        ''' should return f(3) == 2 '''
        self.assertEqual(2, fib.fib(3))

    def test_one(self):
        ''' should return f(10) == 55 '''
        self.assertEqual(55, fib.fib(10))

    def test_zero(self):
        ''' should return f(0) == 0 '''
        self.assertEqual(0, fib.fib(0))

if __name__ == "__main__":
    unittest.main()
