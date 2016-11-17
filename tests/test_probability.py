from unittest import TestCase
from statstuff import probability as prob


class Tests(TestCase):

    def test_single_random_event(self):
        self.assertEquals(0, prob.single_random_event(1, [0, 0, 0, 0]))
        self.assertEquals(0.25, prob.single_random_event(1, [1, 0, 0, 0]))
        self.assertEquals(0.5, prob.single_random_event(1, [1, 0, 1, 0, 1, 0]))
        self.assertEquals(1, prob.single_random_event(1, [1]))
        self.assertEqual(0.5, prob.single_random_event('hi', ['hi', 'hello']))
        self.assertEqual(1, prob.single_random_event(None, [None, None, None]))
