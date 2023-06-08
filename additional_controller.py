import numpy as np

class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def close(self, x):
        if 0 <= x <= 50:
            return 1 - x / 50
        else:
            return 0

    def moderate(self, x):
        if 40 <= x <= 50:
            return x / 10 - 4
        elif 50 <= x <= 100:
            return 2 - x / 50
        else:
            return 0

    def far(self, x):
        if 90 <= x <= 200:
            return x / 110 - 9 / 11
        elif x >= 200:
            return 1
        else:
            return 0

    def low_speed(self, x):
        if 0 <= x <= 5:
            return x / 5
        elif 5 <= x <= 10:
            return 2 - x / 5
        else:
            return 0

    def medium_speed(self, x):
        if 0 <= x <= 15:
            return x / 15
        elif 15 <= x <= 30:
            return 2 - x / 15
        else:
            return 0

    def high_speed(self, x):
        if 25 <= x <= 30:
            return x / 5 - 5
        elif 30 <= x <= 90:
            return 1.5 - x / 60
        else:
            return 0

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        low_speed = self.close(center_dist)
        medium_speed = self.moderate(center_dist)
        high_speed = self.far(center_dist)

        start = 0
        end = 90
        step_size = 0.1

        numerator = 0.0
        denominator = 0.0

        for step in np.arange(start, end, step_size):
            step_low_speed = min(low_speed, self.low_speed(step))
            step_medium_speed = min(medium_speed, self.medium_speed(step))
            step_high_speed = min(high_speed, self.high_speed(step))

            val = max(step_low_speed, step_medium_speed, step_high_speed)
            numerator += val * step_size * step
            denominator += val * step_size

        if denominator != 0:
            centroid = numerator / denominator
            return centroid
        else:
            return 0
    