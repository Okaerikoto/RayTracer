#21h35
import math

# Convert 0-1 float to 0-255 int
def floatto8bit(value):
    return int(max(0, min(value*255, 255)))

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


class Ray:
    def __init__(self, o, d):
        self.o = o
        self.d = d/d.norm()

class Sphere:

    def __init__(self, c, r):
        self.center = c
        self.radius = r
        self.color = Vec3(1,0,0)

    def intersect(self, ray):
        cam_sphere = self.center - ray.o  # camera sphere distance
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
        ray = Ray(Vec3(0,0,0), Vec3(x, self.focal, z))
        return ray


def run_tests():
    print("Running tests:")
    print(Vec3(1,0,0).cross(Vec3(2,0,0)) == Vec3(0,0,0))
    print(Vec3(1, 0, 0).cross(Vec3(0, 1, 0)) == Vec3(0,0,1))
    print(Vec3(1, 0, 0).cross(Vec3(0, 12, 0)) == Vec3(0,0,12))
    print(Vec3(0, 0, 2).norm() == 2)
    print(Vec3(2, 3, 0).norm() == math.sqrt(13))
    print(Vec3(2, 3, 4) - Vec3(1, 1, 1) == Vec3(1, 2, 3))
    print((Vec3(6, 4, 2) / 2) == Vec3(3, 2, 1))
    print((Vec3(6, 4, 2) * 2) == Vec3(12, 8, 4))
    print((2 * Vec3(6, 4, 2)) == Vec3(12, 8, 4))
    print(Vec3(2, 3, 4) + Vec3(1, 1, 1) == Vec3(3, 4, 5))
    print(Vec3(2, 3, 4).dot(Vec3(1, 1, 1)) == 9)
    print(Vec3(2, 3, 4).dot(Vec3(1/2, -1/3, 0))== 0)
    s = Sphere(Vec3(0,1,0), 0.5)
    r1 = Ray(Vec3(0,0,0), Vec3(0,1,0))
    print(s.intersect(r1) == (True, Vec3(0, 0.5, 0)))
    # r2 = Ray(Vec3(0, 0, 0), Vec3(0, 1, 0.5))
    # print(s.intersect(r2) == (True, Vec3(0, 1, 0.5)))
    pass


run_tests()

camera = Camera()

sphere = Sphere(Vec3(0,2,0), 0.5)
print("Sphere at {} with radius {}".format(sphere.center, sphere.radius))

f = open("out.ppm", "w")
f.write("P3\n{} {} {}\n".format(camera.res_width, camera.res_height, 255
                                ))

for i in range(camera.res_width):
    for j in range(camera.res_height):
        color = Vec3(0, 0, 0)
        ray = camera.shoot_ray(i, j)
        inters = sphere.intersect(ray)
        if inters[0]:
            print(sphere.intersect(ray)[1].y)
            color = sphere.color #*abs(inters[1].y-1.75)*4
        f.write("{} {} {}\n".format(floatto8bit(color.x), floatto8bit(color.y), floatto8bit(color.z)))

