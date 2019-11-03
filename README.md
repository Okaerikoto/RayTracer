# RayTracer

Python project rendering a sphere with Phong Shading.

## Install and launch

Developped with Python 3.7.4, no other dependancies

Launch with :
`python raytracer.py`

This will render the image and write it in a .ppm file. The scene layout can be changed in raytracer.py.

## Description

This is a very basic ray tracer, it features:
- One static camera at origine pointing towards +y
- One Light
- One Sphere

For each pixel of the camera, a ray is shoot. If it intersects the sphere (ie if the ray pass by closer to the sphere than the sphere radius), then we compute the intersection point. This can be done with basic trigonometry.

Once we have the intersection point, we can easily compute its normal and distance to the light and then compute its color with Phongs's shader.

For each pixel, the color is written in a ppm file which enable straightforward visualisation.

Result image:

![rendered_picture.png](rendered_picture.png)
