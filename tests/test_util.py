from unittest import TestCase
from statstuff import util


class Tests(TestCase):
    def test_sigmoid(self):
        self.assertEqual(util.sigmoid(-50), 1.928749847963923e-22)
        self.assertEqual(util.sigmoid(-2), 0.11920292202211757)
        self.assertEqual(util.sigmoid(0), 0.5)
        self.assertEqual(util.sigmoid(0.458), 0.61253961344091512)
        self.assertEqual(util.sigmoid(2), 0.8807970779778823)
        self.assertEqual(util.sigmoid(5), 0.9933071490757153)
        self.assertEqual(util.sigmoid(598), 1)
