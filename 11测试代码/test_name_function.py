import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatter_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatter_name, 'Janis Jopllin')

    def test_first_middle_last_name(self):
        formatter_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadus')
        self.assertEqual(formatter_name, 'Wolfgang Amadeus Mozart')


unittest.main()
