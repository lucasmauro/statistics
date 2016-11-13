def average(values):
    if len(values) == 0:
        return 0
    return sum(values)/len(values)


def median(values):
    if len(values) == 0:
        return 0
    values.sort()
    if len(values) % 2 == 0:
        position = int(len(values) / 2)
        a = values.__getitem__(position - 1)
        b = values.__getitem__(position)
        return (a + b) / 2
    else:
        position = int((len(values) / 2) - 0.5)
        return values.__getitem__(position)


def range(values):
    if len(values) == 0:
        return 0
    minimum = min(value for value in values)
    maximum = max(value for value in values)
    return maximum - minimum


def standard_deviation(values):
    return variance(values) ** (1/2.0)


def sum(values):
    total = 0
    for value in values:
        total += value
    return total


def variance(values):
    if len(values) == 0:
        return 0
    avg = average(values)
    sq_dists = [(value - avg) * (value - avg) for value in values]
    return sum(sq_dists) / len(sq_dists)
