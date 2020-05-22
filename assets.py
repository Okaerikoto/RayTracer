import math
import Vec3
from Vec3 import *


class Ray:
    def __init__(self, o, d):
        self.o = o
        self.d = normalize(d)

#Todo to be integrated
class Asset:
    def __init__(self, pos=Vec3(0, 0, 0), color=Vec3(1, 1, 1)):
        self.pos = pos
        self.color = color

class Light:
    def __init__(self, pos=Vec3(0,0,0), color=Vec3(1,1,1), strength=1, radius=10):
        self.pos = pos
        self.color = color
        self._strength = strength
        self.radius = radius

    def strength(self, point):
        dist = norm(self.pos - point)
        out = self._strength * min(self.radius*self.radius/(dist*dist), 1)
        return out

class Sphere:

    def __init__(self, pos, radius, color=Vec3(1,0,0)):
        self.pos = pos
        self.radius = radius
        self.color = color
        print("Sphere at {} with radius {} and color {}".format(self.pos, self.radius, self.color))

    def normal(self, v):
        return normalize(v - self.pos)

    def intersect(self, ray):
        cam_sphere = self.pos - ray.o  # camera sphere distance
        angle_ray_sphere = math.acos(dot(ray.d, cam_sphere)/norm(cam_sphere))
        dist_ray_sphere = math.sin(angle_ray_sphere)*norm(cam_sphere)
        if dist_ray_sphere <= self.radius:
            dist_cam_sphere = norm(cam_sphere)
            dist_ray_intersection = math.sqrt(dist_cam_sphere*dist_cam_sphere - dist_ray_sphere*dist_ray_sphere) \
                 - math.sqrt(self.radius*self.radius - dist_ray_sphere*dist_ray_sphere)
            i_point = ray.o + dist_ray_intersection*ray.d
            return True, i_point
        return False, None

class Triangle:
#todo test this class
    def __init__(self, points):
        self.points = points
        self.normal = normalize(cross(points[1]-points[0], points[2]-points[0]))
        self.d = -dot(points[0], points[1])

    def intersect(self, ray):
        #https://www.cs.princeton.edu/courses/archive/fall00/cs426/lectures/raycast/sld017.htm
        t = -(dot(ray.o, self.normal) + self.d) / dot(ray.d, self.normal)
        i_point = ray.o + t*ray.d
        #todo check if i is inside the triqngle
        return None, i_point

class Mesh():

    def __init__(self, triangles):
        self.triangles = triangles

    def intersect(self, ray):
        for t in self.triangles:
            intersect, point = t.intersect(ray)
            if intersect:
                return intersect, point
        return None

class Camera:

    def __init__(self, res):
        self.res_width = res[0]
        self.res_height = res[1]
        self.width = 1
        self.height = 1
        self.focal = 1

    def pixel_to_meters(self, i, j):
        x = i*self.width/self.res_width - self.width/2
        z = j*self.height/self.res_height - self.height/2
        return x, z

    def shoot_ray(self, i, j):
        x,z = self.pixel_to_meters(i, j)
        ray = Ray(Vec3(0,0,0), Vec3(z, self.focal, -x))
        return ray

# Convert 0-1 float to 0-255 int
def floatto8bit(value):
    return int(max(0, min(value*255, 255)))


