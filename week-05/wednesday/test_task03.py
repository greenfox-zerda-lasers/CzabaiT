import unittest
import task03


class FileLineCounterTestCase(unittest.TestCase):


    def test_person_name_check(self):
        person = task03.Person('András', 2010)
        self.assertEqual(person.name,'András')

    def test_person_birt_date_out_of_lower(self):
        self.assertRaises(task03.CTError, task03.Person, 'Vén Jolán', -1)

    def test_person_birt_date_out_of_higher(self):
        self.assertRaises(task03.CTError, task03.Person, 'Béluska', 2017)



if __name__ == '__main__':
    unittest.main()