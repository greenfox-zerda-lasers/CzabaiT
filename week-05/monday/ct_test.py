import unittest
from ct_work import anagramm, count_letter


class AnagrammComparation(unittest.TestCase):
    """Are two strings really anagramm of each others?"""

    def test_anagramm_uppercase(self):
        self.assertTrue(anagramm("élAb","aléb"))

    def test_anagramm_different_length(self):
        self.assertFalse(anagramm("élabb","aléb"))

    def test_anagramm_whitespaces(self):
        self.assertTrue(anagramm("él ab","aléb"))

    def test_anagramm_blank_enter(self):
        self.assertTrue(anagramm("",""))

    def test_anagramm_integer_attributeerror(self):
        self.assertRaises(AttributeError, anagramm, 1, 1)

class CountLetterToDict(unittest.TestCase):

    def test_count_letter_output_dict(self):
        self.assertIsInstance(count_letter('Béla'), dict)

    def test_count_letter_accent_letter(self):
        self.assertEqual(count_letter('áéíóá'), {'á': 2, 'é': 1, 'í': 1, 'ó': 1})

    def test_count_letter_punctuation(self):
        self.assertEqual(count_letter('%!.,;'), {})

    def test_count_letter_whitespace(self):
        self.assertEqual(count_letter('Bé la'), {'a': 1, 'l': 1, 'b': 1, 'é': 1})

    def test_count_letter_blank_enter(self):
        self.assertEqual(count_letter(''), {})



if __name__ == '__main__':
    unittest.main()