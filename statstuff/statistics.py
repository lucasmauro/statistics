from __future__ import division

""""This is a simple statistics calculator"""


def average(values):
    """Calculates the average value from a list of numbers

    Args:
        values (list)

    Returns:
         float: The average value"""
    if len(values) == 0:
        return None
    return sum(values)/len(values)


def median(values):
    """Returns the central (median) value of a list.
    If the list has an even amount of numbers,
    then the average of the two
    central numbers shall be returned.

    Args:
        values (list)

    Returns:
        float: The central value"""
    if len(values) == 0:
        return None
    values.sort()
    if len(values) % 2 == 0:
        position = int(len(values) / 2)
        a = values[position - 1]
        b = values[position]
        return (a + b) / 2
    else:
        position = int((len(values) / 2) - 0.5)
        return values[position]


def range(values):
    """Returns the range from the minimum to the maximum value
    contained within a given list.

    Args:
        values (list)

    Returns:
        float: The range of values"""
    if len(values) == 0:
        return None
    elif len(values) == 1:
        return 0
    else:
        minimum, maximum = range_limits(values)
        return maximum - minimum


def range_limits(values):
    """Returns the smallest and the greatest values
    contained within a given list.

    Args:
        values (list)

    Returns:
        tuple: the smallest and the greatest values"""
    if len(values) == 0:
        return None, None
    elif len(values) == 1:
        return 0, 0
    else:
        minimum = values[0]
        maximum = values[0]
        for value in values:
            if value < minimum:
                minimum = value
            elif value > maximum:
                maximum = value
        return minimum, maximum


def stdev(values):
    """Returns the standard deviation from a list of numbers.

    Args:
        values (list)

    Returns:
        float: The standart deviation"""
    if len(values) == 0:
        return None
    return variance(values) ** (1/2)


def sum(values):
    """Returns the sum of all values in a list.

    Args:
        values (list)

    Returns:
        float: The sum of all values"""
    total = 0
    for value in values:
        total += value
    return total


def variance(values):
    """Returns the variance of the values in a list.

     Args:
         values (list)

    Returns:
        float: The variance of the values"""
    if len(values) == 0:
        return None
    avg = average(values)
    sq_dists = [(value - avg) ** 2 for value in values]
    return sum(sq_dists) / len(sq_dists)
