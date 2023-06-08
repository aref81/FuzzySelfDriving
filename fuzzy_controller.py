import numpy as np

class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        pass

    def close_L(self, x):
        if 0 <= x <= 50:
            return 1 - (x / 50)
        else:
            return 0

    def moderate_L(self, x):
        if 35 <= x <= 50:
            return (x / 15) - (7 / 3)
        elif 50 < x <= 65:
            return (13 / 3) - (x / 15)
        else:
            return 0

    def far_L(self, x):
        if 50 <= x <= 100:
            return (x / 50) - 1
        else:
            return 0

    def close_R(self, x):
        if 0 <= x <= 50:
            return 1 - (x / 50)
        else:
            return 0

    def moderate_R(self, x):
        if 35 <= x <= 50:
            return (x / 15) - (7 / 3)
        elif 50 < x <= 65:
            return (13 / 3) - (x / 15)
        else:
            return 0

    def far_R(self, x):
        if 50 <= x <= 100:
            return (x / 50) - 1
        else:
            return 0

    def high_right(self, x):
        if -50 <= x <= -20:
            return (x / 30) + (50 / 30)
        elif -20 < x <= -5:
            return (-x / 15) - (1 / 3)
        else:
            return 0

    def low_right(self, x):
        if -20 <= x <= -10:
            return x / 10 + 2
        elif -10 < x <= 0:
            return -x / 10
        else:
            return 0

    def nothing(self, x):
        if -10 <= x <= 0:
            return x / 10 + 1
        elif 0 < x <= 10:
            return 1 - x / 10
        else:
            return 0

    def low_left(self, x):
        if 0 <= x <= 10:
            return x / 10
        elif 10 < x <= 20:
            return 2 - x / 10
        else:
            return 0

    def high_left(self, x):
        if 5 <= x <= 20:
            return x / 15 - (1 / 3)
        elif 20 < x <= 50:
            return 50 / 30 - x / 30
        else:
            return 0

    def decide(self, left_dist,right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """

        low_right = min(self.close_L(left_dist), self.moderate_R(right_dist))
        high_right = min(self.close_L(left_dist), self.far_R(right_dist))
        low_left = min(self.moderate_L(left_dist), self.close_R(right_dist))
        high_left = min(self.far_L(left_dist), self.close_R(right_dist))
        nothing = min(self.moderate_L(left_dist), self.moderate_R(right_dist))
        
        start = -50
        end = 50
        step_size = 0.1

        numerator = 0.0
        denominator = 0.0

        for step in np.arange(start, end, step_size):
            step_low_right = min(low_right, self.low_right(step))
            step_low_left = min(low_left, self.low_left(step))
            step_high_right = min(high_right, self.high_right(step))
            step_high_left = min(high_left, self.high_left(step))
            step_nothing = min(nothing, self.nothing(step))

            val = max(step_low_right, step_low_left, step_high_right, step_high_left, step_nothing)
            numerator += val * step_size * step
            denominator += val * step_size

        if denominator != 0:
            centroid = numerator / denominator
            return centroid
        else:
            return 0
    