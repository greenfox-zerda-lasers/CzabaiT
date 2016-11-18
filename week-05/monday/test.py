import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_4_is_6(self):
        self.assertEqual(extend.add(2, 4), 6)

    def test_add_0_and_minus1_is_minus1(self):
        self.assertEqual(extend.add(0, -1), -1)

    def test_max_of_three_second(self):
        self.assertEqual(extend.max_of_three(5, 7, 4), 7)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(4, 5, 3), 5)

    def test_median_four(self):
        self.assertEqual(extend.median([7,4,3,5]), 4.5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,4,3,5]), 3)

    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('ú'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('u'))

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutatkozik'), 'bevemuvutavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('koolbice'), 'kovoovolbiviceve')

if __name__ == '__main__':
    unittest.main()
