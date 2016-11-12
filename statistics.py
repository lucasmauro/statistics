class Statistics:
    """Calculates a variety of statistics"""

    def __init__(self):
        pass

    @classmethod
    def average(cls, values):
        return cls.sum(values)/len(values)

    @classmethod
    def median(cls, values):
        values.sort()
        if len(values) % 2 == 0:
            position = int(len(values) / 2)
            a = values.__getitem__(position - 1)
            b = values.__getitem__(position)
            return (a + b) / 2
        else:
            position = int((len(values) / 2) - 0.5)
            return values.__getitem__(position)

    @classmethod
    def range(cls, values):
        minimum = min(value for value in values)
        maximum = max(value for value in values)
        return maximum - minimum

    @classmethod
    def standard_deviation(cls, values):
        return cls.variance(values) ** (1/2.0)

    @classmethod
    def sum(cls, values):
        total = 0
        for value in values:
            total += value
        return total

    @classmethod
    def variance(cls, values):
        average = cls.average(values)
        sq_dists = [(value - average) * (value - average) for value in values]
        return cls.sum(sq_dists) / len(sq_dists)
