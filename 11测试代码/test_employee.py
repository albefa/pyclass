import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.eri = Employee('eric', 'matths', 65000)

    def test_give_defaul_raise(self):
        self.eri.give_raise()
        self.assertEqual(self.eri.salary, 70000)

    def test_give_cuntom_raise(self):
        self.eri.give_raise(10000)
        self.assertEqual(self.eri.salary, 75000)


unittest.main()
