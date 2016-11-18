import unittest
from task01 import divider

class DividerTestCase(unittest.TestCase):
    '''Test 01.py'''

    def test_divider_2_equal_5(self):
        self.assertEqual(divider(2), 5)

    def test_divider_zero_div_err(self):
        self.assertEqual(divider(0), 'fail')

if __name__ == '__main__':
    unittest.main()

