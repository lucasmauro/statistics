from __future__ import division

""""This is but a file containing utilities for Statstuff calculations"""


__e = 2.718281828459045


def sigmoid(x):
    return 1 / (1 + __e ** (-x))
