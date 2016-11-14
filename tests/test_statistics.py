from unittest import TestCase
from statstuff import statistics as stats


class Tests(TestCase):

    def test_average(self):
        self.assertEqual(0, stats.average([]))
        self.assertEqual(1.5, stats.average([1, 2]))
        self.assertEqual(25.35, stats.average([10.1, 20.8, 30.4, 40.1]))

    def test_median(self):
        self.assertEqual(0, stats.median([]))
        self.assertEqual(3.01, stats.median([1.0494, 2.68, 3.34, 4.33]))
        self.assertEqual(3.01, stats.median([3.34, 2.68, 1.0494, 4.33]))
        self.assertEqual(3.35, stats.median([1.9, 2.105, 3.35, 4.401, 5.55]))
        self.assertEqual(3.35, stats.median([3.35, 5.55, 1.9, 4.401, 2.105]))

    def test_range(self):
        self.assertEqual(0, stats.range([]))
        self.assertEqual(0, stats.range([20]))
        self.assertEqual(0, stats.range([1, 1]))
        self.assertEqual(1, stats.range([1, 2]))
        self.assertEqual(2, stats.range([2, 1, 3]))
        self.assertEqual(78891, stats.range([19874, 65084, 98765]))

    def test_standard_deviation(self):
        self.assertEqual(0, stats.standard_deviation([]))
        self.assertEqual(0, stats.standard_deviation([45]))
        self.assertEqual(0, stats.standard_deviation([1, 1]))
        self.assertEqual(0.5, stats.standard_deviation([1, 2]))
        self.assertEqual(15.5, stats.standard_deviation([1963, 1994]))

    def test_sum(self):
        self.assertEqual(0, stats.sum([]))
        self.assertEqual(1, stats.sum([1]))
        self.assertEqual(2, stats.sum([1, 1]))
        self.assertEqual(230880, stats.sum([9480, 6548, 65018, 149834]))

    def test_variance(self):
        self.assertEqual(0, stats.variance([]))
        self.assertEqual(0, stats.variance([50]))
        self.assertEqual(0, stats.variance([1, 1, 1, 1, 1]))
        self.assertEqual(0.25, stats.variance([1, 2]))
        self.assertEqual(138.6875, stats.variance([1963, 1983, 1989, 1994]))
