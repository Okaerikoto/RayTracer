import math
from Vec3 import Vec3
from assets import *


def run_tests():
    print("Running tests:")
    print(cross(Vec3(1,0,0),Vec3(2,0,0)) == Vec3(0,0,0))
    print(cross(Vec3(1, 0, 0),Vec3(0, 1, 0)) == Vec3(0,0,1))
    print(cross(Vec3(1, 0, 0),Vec3(0, 12, 0)) == Vec3(0,0,12))
    print(norm(Vec3(0, 0, 2)) == 2)
    print(norm(Vec3(2, 3, 0)) == math.sqrt(13))
    print(Vec3(2, 3, 4) - Vec3(1, 1, 1) == Vec3(1, 2, 3))
    print((Vec3(6, 4, 2) / 2) == Vec3(3, 2, 1))
    print((Vec3(6, 4, 2) * 2) == Vec3(12, 8, 4))
    print((2 * Vec3(6, 4, 2)) == Vec3(12, 8, 4))
    print(Vec3(2, 3, 4) + Vec3(1, 1, 1) == Vec3(3, 4, 5))
    print(dot(Vec3(2, 3, 4), Vec3(1, 1, 1)) == 9)
    print(dot(Vec3(2, 3, 4), Vec3(1/2, -1/3, 0))== 0)
    s = Sphere(Vec3(0,1,0), 0.5)
    r1 = Ray(Vec3(0,0,0), Vec3(0,1,0))
    print(s.intersect(r1) == (True, Vec3(0, 0.5, 0)))
    l = Light()
    # r2 = Ray(Vec3(0, 0, 0), Vec3(0, 1, 0.5))
    # print(s.intersect(r2) == (True, Vec3(0, 1, 0.5)))

    t = Triangle([Vec3(0,0,1), Vec3(1,0,1), Vec3(0,1,1)])
    print(t.normal == Vec3(0,0,1))
    print(t.intersect(Ray(Vec3(2,3,0), Vec3(0,0,1)))[1])
    pass