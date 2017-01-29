from unittest import TestCase
from statstuff import probability as prob


class Tests(TestCase):

    def test_single_random_event(self):
        self.assertEqual(0, prob.random(1, []))
        self.assertEqual(0, prob.random(1, [0, 0, 0, 0]))
        self.assertEqual(0.25, prob.random(1, [1, 0, 0, 0]))
        self.assertEqual(0.5, prob.random(1, [1, 0, 1, 0, 1, 0]))
        self.assertEqual(1, prob.random(1, [1]))
        self.assertEqual(0.5, prob.random('hi', ['hi', 'hello']))
        self.assertEqual(1, prob.random(None, [None, None, None]))

    def test_multiple_random_events(self):
        self.assertEqual(0, prob.random([], []))
        self.assertEqual(0, prob.random([], [1]))
        self.assertEqual(1, prob.random([1], [1]))
        self.assertEqual(0, prob.random([1, 3], [1, 2]))
        self.assertEqual(1, prob.random([1, 1], [1]))
        self.assertEqual(0, prob.random([1, 1], [1], False))
        self.assertEqual(0.2222222222222222,
                         prob.random([1, 0], [1, 0, 1]))
        self.assertEqual(0.3333333333333333,
                         prob.random([1, 0], [1, 0, 1], False))
        self.assertEqual(0.027777777777777776,
                         prob.random([1, 1],
                                     [1, 2, 3, 4, 5, 6]))
        self.assertEqual(0,
                         prob.random([1, 1],
                                     [1, 2, 3, 4, 5, 6], False))
        self.assertEqual(0.25,
                         prob.random([None, 'hi'], ['hi', None]))
