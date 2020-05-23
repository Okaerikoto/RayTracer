from Vec3 import Vec3
import tests
from assets import *

antialias_level = 0


# The material parameters are constants independant of the object for now
ambient = 0.4 * Vec3(0.4, 0.4, 1)
k_ambient = 1
k_diffuse = 2
k_specular = 10
n_specular = 50



def render_pixel(u, v, camera, light, asset, file):
    c = Vec3(0, 0, 0)
    ray = camera.shoot_ray(u, v)
    intersect, i = asset.intersect(ray)
    if intersect:
        n = asset.normal(i)
        l = light.pos - i
        r = normalize(2 * n - l)

        l_intensity = light.strength(i) * light.color
        i_ambient = k_ambient * ambient
        i_diffuse = k_diffuse * max(dot(n, normalize(l)), 0) * l_intensity
        i_specular = k_specular * pow(max(dot(r, normalize(-1 * i)), 0), n_specular) * l_intensity

        c = mul(asset.color, i_ambient + i_diffuse + i_specular)
    file.write("{} {} {}\n".format(floatto8bit(c.x), floatto8bit(c.y), floatto8bit(c.z)))

def render_pixel_antialias(u, v, camera, light, asset, file, antialias_level=0):
    """
    :param u:
    :param v:
    :param camera:
    :param light:
    :param asset:
    :param file:
    :param antialias_level: level of antialiasing n
    shoot 2^2n rays per pixel and average the result
    :return:
    """

    a_n = 2 ** antialias_level
    ray_offset = [2/a_n * i - (1 - 1/a_n) for i in range(a_n)]
    # ray_offset = [-0.5, 0.5]
    # ray_offset =  [-0.75, -0.25, 0.25, 0.75]

    c_list = []


    for du in ray_offset:
        for dv in ray_offset:
            c = Vec3(0, 0, 0)
            ray = camera.shoot_ray(u + du, v + dv)
            intersect, i = asset.intersect(ray)
            if intersect:
                n = asset.normal(i)
                l = light.pos - i
                r = normalize(2 * n - l)

                l_intensity = light.strength(i) * light.color
                i_ambient = k_ambient * ambient
                i_diffuse = k_diffuse * max(dot(n, normalize(l)), 0) * l_intensity
                i_specular = k_specular * pow(max(dot(r, normalize(-1 * i)), 0), n_specular) * l_intensity

                c = mul(asset.color, i_ambient + i_diffuse + i_specular)
            c_list.append(c)
    c = Vec3(0, 0, 0)
    for ci in c_list:
        c += ci
    c = c/len(ray_offset)**2
    file.write("{} {} {}\n".format(floatto8bit(c.x), floatto8bit(c.y), floatto8bit(c.z)))



def main():

    res = 100 # rendered image resolution
    camera = Camera((res,res))
    sphere = Sphere(pos=Vec3(0, 2, 0),  radius=0.5, color=Vec3(1, 0.2, 0.2))
    light = Light(pos=Vec3(1, 0.5, 1), color=Vec3(1, 1, 0.5), strength=1, radius=1)

    triangle = Triangle([Vec3(0,0,1), Vec3(1,0,1), Vec3(0,1,1)])

    asset = sphere
    #asset = triangle

    out_file = open("out.ppm", "w")
    out_file.write("P3\n{} {} {}\n".format(camera.res_width, camera.res_height, 255))

    for u in range(camera.res_width):
        for v in range(camera.res_height):
            render_pixel_antialias(u,v,camera, light, asset, out_file, antialias_level)



tests.run_tests()
main()