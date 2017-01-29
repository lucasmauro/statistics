from __future__ import division
from statstuff import statistics as stats
from statstuff import util

""""This is a simple regression calculator"""


def linear(x, y):
    """Calculates the intercept and the coefficient for
    a linear regression equation

    Args:
        x Explanatory values

        y Dependent values

    Returns:
         float: The intercept and b the coefficient"""
    length = len(x)
    length_y = len(y)
    if (length is not length_y) or (length is 0) or (length_y is 0):
        return None

    c = (length * stats.sum([g * h for g, h in zip(x, y)]))
    d = c - (stats.sum(x) * stats.sum(y))
    e = (length * stats.sum([g ** 2 for g in x])) - (stats.sum(x) ** 2)
    b = d / e

    a = (stats.sum(y) - (b * stats.sum(x))) / length

    return [a, b]


def predict(features, parameters):
    """Predicts the due value given the regression features and parameters

    Args:
        features Regression equation features

        parameters Regression equation parameters

    Returns:
         float: The value predicted from features and parameters"""
    feats = features[:]
    params = parameters[:]
    len_f = len(feats)
    len_p = len(params)
    if (len_f is not len_p+1) or (len_f is 0) or (len_p is 0):
        return None

    predicted_value = feats.pop(0)
    predicted_value += stats.sum([x * y for x, y in zip(feats, params)])
    return predicted_value


def predict_sigmoid(features, parameters):
    """Returns the sigmoid value for the predicted
    value from givem features and parameters

    Args:
        features Regression equation features

        parameters Regression equation parameters

    Returns:
         float: The sigmoid value predicted from features and parameters"""
    return util.sigmoid(predict(features, parameters))
