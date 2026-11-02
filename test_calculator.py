import unittest
from calculator import add, sub, mul

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
    def test_sub(self):
        self.assertEqual(sub(5,2),3)
    def test_mul(self):
        self.assertEqual(mul(2,3),6)

if __name__ == '__main__':
    unittest.main()
