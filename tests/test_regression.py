from unittest import TestCase
from statstuff import regression as reg


class Tests(TestCase):

    features = [22.00745257452574, 0.8719512195121951]
    multiple_features = [64.987, 0.0974, 9.480, -2.503]
    
    def test_linear(self):
        self.assertEqual(None, reg.linear([], []))
        self.assertEqual(None, reg.linear([1, 2], []))
        self.assertEqual(None, reg.linear([], [3, 4]))
        self.assertEqual(None, reg.linear([1, 2], [3]))

        self.assertEqual([22.00745257452574, 0.8719512195121951],
                         reg.linear(
                             [164, 166, 169, 169, 171, 173, 173, 176, 178],
                             [166, 166, 171, 166, 171, 171, 178, 173, 178]
                         ))
        self.assertEqual([9.511627906976745, -0.627906976744186],
                         reg.linear(
                             [8, 2, 5, 0, 1, 4, 10, 2],
                             [7, 10, 6, 10, 8, 5, 2, 8]
                         ))

    def test_predict(self):
        self.assertEqual(None, reg.predict([], []))
        self.assertEqual(None, reg.predict(self.features, []))
        self.assertEqual(None, reg.predict([], [50]))
        self.assertEqual(None, reg.predict([1, 2, 3], [50]))

        self.assertEqual(-832.5047425474255, reg.predict(self.features, [-980]))
        self.assertEqual(22.00745257452574, reg.predict(self.features, [0]))
        self.assertEqual(65.6050135501355, reg.predict(self.features, [50]))
        self.assertEqual(66.4769647696477, reg.predict(self.features, [51]))
        self.assertEqual(876.5196476964769, reg.predict(self.features, [980]))
        
        self.assertEqual(64.987, reg.predict(self.multiple_features, [0, 0, 0]))
        self.assertEqual(72.06139999999999, reg.predict(self.multiple_features, [1, 1, 1]))
        self.assertEqual(112.5818, reg.predict(self.multiple_features, [2, 5, 0]))
        self.assertEqual(229.54999999999998, reg.predict(self.multiple_features, [25, 34, 64]))
        self.assertEqual(79.13579999999999, reg.predict(self.multiple_features, [2, 2, 2]))

    def test_predict_sigmoid(self):
        self.assertEqual(0.9999999997231244, reg.predict_sigmoid(self.features, [0]))
        self.assertEqual(0.9998674190123374, reg.predict_sigmoid(self.features, [-15]))
        self.assertEqual(3.288160886939343e-08, reg.predict_sigmoid(self.features, [-45]))
        self.assertEqual(1, reg.predict_sigmoid(self.multiple_features, [1, 1, 1]))
        self.assertEqual(1.3737327556402954e-18,
                         reg.predict_sigmoid(self.multiple_features, [-15, -15, -15]))