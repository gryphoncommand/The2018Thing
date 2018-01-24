"""

This module deals with pure math, and should not need any imports. This is meant to isolate math code.

"""

"""

class definitions come in this class

"""

import math

class Vector2D:
    """

    Vector 2D

    """

    def __init__(self, x, y=None):
        if isinstance(x, tuple) or isinstance(x, list):
            self.p = tuple(x)
        else:
            if y is None:
                raise Exception("When creating a Vector2D, use Vector2D(x, y)")
            self.p = x, y

    def __str__(self):
        return str(self.p)

    def __repr__(self):
        return self.__str__()

    def __abs__(self):
        return math.sqrt(self.p[0] ** 2 + self.p[1] ** 2)

    def __op(self, v):
        if isinstance(v, tuple):
            return Vector2D(v[0], v[1])
        else:
            return v

    def __add__(self, _v):
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] + v.p[0], self.p[1] + v.p[1])
        else:
            raise Exception("can only add Vector2D s")

    def __sub__(self, _v):
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] - v.p[0], self.p[1] - v.p[1])
        else:
            raise Exception("can only sub Vector2D s")

    def __mul__(self, _v):
        # scalar multiplication
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] * v.p[0], self.p[1] * v.p[1])
        else:
            return Vector2D(self.p[0] * v, self.p[1] * v)
        
    def __div__(self, _v):
        # scalar division
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] / v.p[0], self.p[1] / v.p[1])
        else:
            return Vector2D(self.p[0] / v, self.p[1] / v)
        
    def rot(self, amount, degrees=False):
        """

        if degrees, then amount is meant to be degrees. Otherwise, radians

        """

        if degrees:
            amount = amount * math.pi / 180.0
        # scalar division
        sin_a = math.sin(amount)
        cos_a = math.cos(amount)

        x, y = self.p

        return Vector2D(cos_a * x - sin_a * y, sin_a * x + cos_a * y)

    def angle(self, degrees=False):
        v = math.atan2(self.p[1], self.p[0])
        if degrees:
            v = v * 180 / math.pi
        return v


