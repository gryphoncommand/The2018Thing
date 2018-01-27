"""

This module deals with pure math, and should not need any imports. This is meant to isolate math code.

"""

"""

class definitions come in this class

"""

import math

class Vector2D:
    """

    Vector 2D class

    """

    def from_polar(radius, angle, degrees=False):
        if degrees:
            angle = angle * math.pi / 180.0
        return Vector2D(math.cos(angle) * radius, math.sin(angle) * radius)

    def from_rectangular(x, y):
        return Vector2D(x, y)

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

    def __getitem__(self, key):
        if key in ("x", 0):
            return self.p[0]
        elif key in ("y", 1):
            return self.p[1]
        elif isinstance(key, slice):
            return self.p.__getitem__(key)
        else:
            raise KeyError("Don't know vector key: %s" % key)


    def set_x(self, v):
        self.p[0] = v

    def get_x(self):
        return self.p[0]

    x = property(get_x, set_x)

    def set_y(self, v):
        self.p[1] = v

    def get_y(self):
        return self.p[1]

    y = property(get_y, set_y)


    def __add__(self, _v):
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] + v.p[0], self.p[1] + v.p[1])
        else:
            raise Exception("can only add Vector2D s")

    def __radd__(self, _v):
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

    def __rsub__(self, _v):
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(v.p[0] - self.p[0], v.p[1] - self.p[1])
        else:
            raise Exception("can only sub Vector2D s")


    def __mul__(self, _v):
        # scalar multiplication
        v = self.__op(_v)
        if isinstance(v, Vector2D):
            return Vector2D(self.p[0] * v.p[0], self.p[1] * v.p[1])
        else:
            return Vector2D(self.p[0] * v, self.p[1] * v)

    def __rmul__(self, _v):
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


    def get_angle(self, degrees=False):
        v = math.atan2(self.p[1], self.p[0])
        if degrees:
            v = v * 180 / math.pi
        return v

    def set_angle(self, v, degrees=False):
        if degrees:
            v = v * math.pi / 180
        
        self.p = Vector2D.from_polar(abs(self), v).p

    angle = property(get_angle, set_angle)

    def get_radius(self):
        return abs(self)

    def set_radius(self, v):
        cur_rad = self.get_radius()
        if cur_rad != 0:
            self.p = (self.p[0] * v / cur_rad, self.p[1] * v / cur_rad)

    radius = property(get_radius, set_radius)

