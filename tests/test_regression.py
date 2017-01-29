from unittest import TestCase
from statstuff import regression as reg


class Tests(TestCase):

    def test_single_random_event(self):
        self.assertEqual(None, reg.linear([], []))
        self.assertEqual(None, reg.linear([1, 2], []))
        self.assertEqual(None, reg.linear([], [3, 4]))
        self.assertEqual(None, reg.linear([1, 2], [3]))
        self.assertEqual((22.00745257452574, 0.8719512195121951),
                         reg.linear(
                             [164, 166, 169, 169, 171, 173, 173, 176, 178],
                             [166, 166, 171, 166, 171, 171, 178, 173, 178]
                         ))
        self.assertEqual((9.511627906976745, -0.627906976744186),
                         reg.linear(
                             [8, 2, 5, 0, 1, 4, 10, 2],
                             [7, 10, 6, 10, 8, 5, 2, 8]
                         ))
