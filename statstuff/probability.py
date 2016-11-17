from __future__ import division

""""This is a simple probability calculator"""


def single_random_event(event, possibilities):
    """Calculates the probability for a single
    event to happen in a list of possibilities.

    Args:
        event

        possibilities (list)

    Returns:
         float: The probability"""
    if len(possibilities) == 0:
        return 0
    matches = 0
    for possibility in possibilities:
        if event == possibility:
            matches += 1
    return matches / len(possibilities)


def multiple_random_events(events, possibilities, reposition):
    """Calculates the probability for multiple
    events to happen in a list of possibilities.

    Args:
        events (list)

        possibilities (list)

        reposition (bool) Whether or not the event that happened should
         be kept from the list of possibilities

    Returns:
         float: The probability"""
    if len(events) == 0 or len(possibilities) == 0:
        return 0

    calculated_probabilities = []

    for event in events:
        single_probability = single_random_event(event, possibilities)
        if single_probability == 0:
            return 0

        calculated_probabilities.append(single_probability)
        if reposition is False:
            possibilities.remove(event)

    probability = 1
    for single_probability in calculated_probabilities:
        probability *= single_probability
    return probability
