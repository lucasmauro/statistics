from __future__ import division
from statstuff import statistics as stats

""""This is a simple regression calculator"""


def linear(x, y):
    """Calculates the intercept and the coefficient for
    a linear regression equation

    Args:
        x Explanatory values

        y Dependent values

    Returns:
         a The intercept and b the coefficient"""
    length = len(x)
    length_y = len(y)
    if length is not length_y or length is 0 or length_y is 0:
        return None

    c = (length * stats.sum([g * h for g, h in zip(x, y)])) - (stats.sum(x) * stats.sum(y))
    v = (length * stats.sum([g ** 2 for g in x])) - (stats.sum(x) ** 2)
    b = c / v

    a = (stats.sum(y) - (b * stats.sum(x))) / length

    return a, b

