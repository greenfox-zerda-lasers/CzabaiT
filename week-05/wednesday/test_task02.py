import unittest
from task02 import file_line_counter


class FileLineCounterTestCase(unittest.TestCase):

    def test_file_line_counter_7_lines_from_text(self):

        self.assertEqual(file_line_counter('text.txt'), 7)

    def test_file_line_0_file_not_exist(self):

        self.assertEqual(file_line_counter('nothing.txt'), 'zero')

if __name__ == '__main__':
    unittest.main()