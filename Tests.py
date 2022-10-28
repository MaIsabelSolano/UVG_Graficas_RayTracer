from material import *
from ray import *
from vector import *
from light import *
from color import *

r = Raytracer(800, 600, 'r.bmp')

# Materials
red = Material(diffuse = Color(255, 0, 0))
white = Material(diffuse = Color(255, 255, 255))

# Ilumination
r.light = Light(V3(0, 0, 0), 1)

# Objects 
r.scene = [
    Sphere(V3(-3, 0, -16), 2, red),
    Sphere(V3(2.8, 0, -10), 2, white)
]

r.render()
r.write()