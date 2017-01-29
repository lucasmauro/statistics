from __future__ import division

""""This is but a file containing utilities for Statstuff calculations"""


__e = 2.718281828459045


def sigmoid(x):
    """Returns the logistic value for x, which is always between 0 and 1.

    Args:
        x Value to be converted

    Returns:
        float: The logistic value for x"""
    return 1 / (1 + __e ** (-x))
