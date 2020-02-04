from math import sqrt


class Circle:

    def __init__(self, x, y, r):
        self._x = x
        self._y = y
        self._r = r

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def r(self):
        return self._r

    @staticmethod
    def circle_from_c_tuple(c_tuple):
        return Circle(c_tuple[1], c_tuple[2], c_tuple[3])

    def get_interaction(self, circle):
        x2 = circle.x
        y2 = circle.y
        r2 = circle.r

        d = sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        smallest_r = min(self.r, r2)
        largest_r = max(self.r, r2)

        if d > abs(self.r + r2):
            # circles are not intersecting or nested
            return 'none'
        elif d + smallest_r < largest_r:
            return 'nested'
        else:
            return 'intersecting'


class Cluster:

    def __init__(self, circles):
        self._circles = circles
        self.compute_largest_circle()

    def compute_largest_circle(self):
        # compute the largest circle in the set of circles
        for circle in self.circles:
            pass

