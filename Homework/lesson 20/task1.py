import unittest
import calendar
from test_examples import Mathematician


class NameTestCase(unittest.TestCase):

    def test_first_functioun(self):
        square = Mathematician.square_nums([2, 3, 4, 5, 6])
        self.assertEqual(square, [4, 9, 16, 25, 36])


unittest.main


class TestCase2(unittest.TestCase):

    def test_second_functioun(self):
        positive = Mathematician.remove_positives([2, -10, 4, -13, 6, -29])
        self.assertEqual(positive, [-10,-13,-29])

unittest.main


class TestCase3(unittest.TestCase):
    def test_data_functioun(self):
        data = Mathematician.filter_leaps([1764, 2005, 1999, 1784, 2056])
        self.assertEqual(data, [1764,1784, 2056])


unittest.main


#task2

