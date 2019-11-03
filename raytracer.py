from Vec3 import Vec3
import tests
from assets import *

def main():

    res = 500
    camera = Camera((res,res))
    sphere = Sphere(pos=Vec3(0, 2, 0),  radius=0.5, color=Vec3(1, 0.2, 0.2))
    light = Light(pos=Vec3(1, 0.5, 1), color=Vec3(1, 1, 0.5), strength=1, radius=1)

    ambient = 0.4 * Vec3(0.4, 0.4, 1)
    k_ambient = 1
    k_diffuse = 2
    k_specular = 10
    n_specular = 50

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
                r = normalize(2 * n - l)

                l_intensity = light.strength(i) * light.color
                i_ambient = k_ambient * ambient
                i_diffuse =  k_diffuse *      max(dot(n, normalize(l)), 0) * l_intensity
                i_specular = k_specular * pow(max(dot(r, normalize(-1*i)), 0), n_specular) * l_intensity

                c = mul(sphere.color, i_ambient + i_diffuse + i_specular)
            f.write("{} {} {}\n".format(floatto8bit(c.x), floatto8bit(c.y), floatto8bit(c.z)))


tests.run_tests()
main()