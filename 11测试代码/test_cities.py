import unittest
from city_function import city_name


class NamesTestCase(unittest.TestCase):
    def Test_City(self):
        allfuntion = city_name('santiago', 'chile')
        self.assertEqual(allfuntion, 'Santiago Chile')


###空套件？？ 提示没有run
unittest.main()
