import math
import Vec3
from Vec3 import Vec3


class Ray:
    def __init__(self, o, d):
        self.o = o
        self.d = d/d.norm()


class Light:
    def __init__(self, pos=Vec3(0,0,0), color=Vec3(1,1,1), strength=1):
        self.pos = pos
        self.color = color
        self.strength = strength

class Sphere:

    def __init__(self, pos, radius, color=Vec3(1,0,0)):
        self.pos = pos
        self.radius = radius
        self.color = color
        print("Sphere at {} with radius {} and color {}".format(self.pos, self.radius, self.color))

    def normal(self, v):
        return (v - self.pos).normalize()

    def intersect(self, ray):
        cam_sphere = self.pos - ray.o  # camera sphere distance
        angle_ray_sphere = math.acos(ray.d.dot(cam_sphere)/cam_sphere.norm())
        dist_ray_sphere = math.sin(angle_ray_sphere)*cam_sphere.norm() #cam_sphere.cross(ray.d).norm()  # ray sphere distance
        if dist_ray_sphere <= self.radius:
            dist_cam_sphere = cam_sphere.norm()
            dist_ray_intersection = math.sqrt(dist_cam_sphere*dist_cam_sphere - dist_ray_sphere*dist_ray_sphere) \
                 - math.sqrt(self.radius*self.radius - dist_ray_sphere*dist_ray_sphere)
            i_point = ray.o + dist_ray_intersection*ray.d
            return True, i_point
        return False, None


class Camera:

    def __init__(self):
        self.res_width = 100
        self.res_height = 100
        self.width = 1
        self.height = 1
        self.focal = 1

    def pixel_to_meters(self, i, j):
        x = i*self.width/self.res_width - self.width/2
        z = j*self.height/self.res_height - self.height/2
        return x, z

    def shoot_ray(self, i, j):
        x,z = self.pixel_to_meters(i, j)
        ray = Ray(Vec3(0,0,0), Vec3(z, self.focal, x))
        return ray

# Convert 0-1 float to 0-255 int
def floatto8bit(value):
    return int(max(0, min(value*255, 255)))


