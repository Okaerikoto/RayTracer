from Vec3 import Vec3
import tests
from assets import *

def main():

    camera = Camera()
    sphere = Sphere(pos=Vec3(0, 2, 0),  radius=0.5, color=Vec3(1, 0.2, 0.2))
    light = Light(pos=Vec3(2, 0.2, 0.2), color=Vec3(1,1,0.5), strength=1)

    ambient = 0.3 * Vec3(0.4, 0.4, 1)

    f = open("out.ppm", "w")
    f.write("P3\n{} {} {}\n".format(camera.res_width, camera.res_height, 255
                                    ))
    for u in range(camera.res_width):
        for v in range(camera.res_height):
            c = Vec3(0, 0, 0)
            ray = camera.shoot_ray(u, v)
            intersect, i = sphere.intersect(ray)
            if intersect:
                n = sphere.normal(i)
                l = light.pos - i
                light_source = max(n.dot(l.normalize()),0) * light.strength * sphere.color.mul(light.color)
                light_ambient = sphere.color.mul(ambient)
                c = light_source + light_ambient
            f.write("{} {} {}\n".format(floatto8bit(c.x), floatto8bit(c.y), floatto8bit(c.z)))


tests.run_tests()
main()