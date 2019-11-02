#21h35
import math
import sys

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({} {} {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return (self.x == other.x) & (self.y == other.y) & (self.z == other.z)

    def __sub__(self, other):
        out = Vec3()
        out.x = self.x - other.x
        out.y = self.y - other.y
        out.z = self.z - other.z
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



class Ray:
    def __init__(self, o, d):
        self.o = o
        self.d = d/d.norm()

class Sphere:

    def __init__(self, c, r):
        self.center = c
        self.radius = r
        self.color = Vec3(255,0,0)

    def intersect(self, ray):
        #TODO
        dist = (self.center - ray.o).cross(ray.d).norm()
        if dist < self.radius:
            return True
        return False


class Camera:
    width = 100
    height = 100

    def shoot_ray(self, x, y):
        return Ray(Vec3(0,0,0), Vec3(x-Camera.width/2, Camera.width/2, y - Camera.height/2))


def tests():
    print("Running tests:")
    print(Vec3(1,0,0).cross(Vec3(2,0,0)) == Vec3(0,0,0))
    print(Vec3(1, 0, 0).cross(Vec3(0, 1, 0)) == Vec3(0,0,1))
    print(Vec3(1, 0, 0).cross(Vec3(0, 12, 0)) == Vec3(0,0,12))
    print(Vec3(0, 0, 2).norm() == 2)
    print(Vec3(2, 3, 0).norm() == math.sqrt(13))
    print(Vec3(2, 3, 4) - Vec3(1, 1, 1) == Vec3(1, 2, 3))
    print((Vec3(6, 4, 2) / 2) == Vec3(3, 2, 1))

tests()

camera = Camera()

sphere = Sphere(Vec3(0,100,0), 30)
print("Sphere at {} with radius {}".format(sphere.center, sphere.radius))

f = open("out.ppm", "w")
f.write("P3\n{} {} {}\n".format(camera.width, camera.height, 255))

for x in range(Camera.width):
    for y in range(Camera.height):
        color = Vec3(0, 0, 0)
        ray = camera.shoot_ray(x, y)
        if sphere.intersect(ray):
            color = sphere.color
        f.write("{} {} {}\n".format(color.x, color.y, color.z))

