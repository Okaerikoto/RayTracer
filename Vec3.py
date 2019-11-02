import math


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({} {} {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y) & (self.z == other.z)

    def __add__(self, other):
        out = Vec3()
        out.x = self.x + other.x
        out.y = self.y + other.y
        out.z = self.z + other.z
        return out

    def __sub__(self, other):
        out = Vec3()
        out.x = self.x - other.x
        out.y = self.y - other.y
        out.z = self.z - other.z
        return out

    def __mul__(self, other):
        out = Vec3()
        out.x = self.x * other
        out.y = self.y * other
        out.z = self.z * other
        return out

    def __rmul__(self, other):
        return self.__mul__(other)

    def mul(self, other):
        out = Vec3()
        out.x = self.x * other.x
        out.y = self.y * other.y
        out.z = self.z * other.z
        return out

    def __truediv__(self, other):
        out = Vec3()
        out.x = self.x / other
        out.y = self.y / other
        out.z = self.z / other
        return out

    def norm(self):
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def cross(self, v):
        out = Vec3()
        u = self
        out.x = u.y*v.z - v.y*u.z
        out.y = u.z*v.x - v.z*u.x
        out.z = u.x*v.y - v.x*u.y
        return out

    def dot(self, other):
        value = self.x * other.x \
                + self.y * other.y \
                + self.z * other.z
        return value

    def normalize(self):
        return self/self.norm()
