from __future__ import division

""""This is a simple statistics calculator"""


def single_random_event(event, possibilities):
    """Calculates the probability for a single
    event to happen in a list of possibilities.

    Args:
        event
        possibilities (list)

    Returns:
         float: The probability"""
    matches = 0
    for possibility in possibilities:
        if event == possibility:
            matches += 1
    return matches / len(possibilities)
