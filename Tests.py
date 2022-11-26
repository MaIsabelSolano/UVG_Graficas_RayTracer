from material import *
from ray import *
from vector import *
from light import *
from color import *
from plane import *
from cube import *

r = Raytracer(800, 600, 'r.bmp', './galaxy.bmp')

# Materials
red =    Material(diffuse = Color(255, 0, 0))
white =  Material(diffuse = Color(255, 255, 255))
ivory =  Material(diffuse = Color(200, 200, 180), albedo = [0.6, 0.3, 0, 0],   spec = 10)
rubber = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.1, 0.1, 0], spec = 50)
mirror = Material(diffuse = Color(255, 255, 255), albedo = [0, 1, 0.8, 0],     spec = 1425)
glass =  Material(diffuse = Color(150, 180, 200), albedo = [0, 0.5, 0.1, 0.8], spec = 125,  refractive_index = 1.5)

# Ilumination
r.light = Light(V3(10, -13, 4), 1, Color(255, 255, 255))

# Objects 
r.scene = [
    Sphere(V3(0, -1.5, -11), 1.5, ivory),
    Sphere(V3(-0.25, 0, -6), 0.5, glass),
    Sphere(V3(1, 1, -8), 1.7, rubber),
    Sphere(V3(-2, 1, -10), 2, mirror),
    Sphere(V3(2, -0.9, -5.5), 1, ivory),
    #Plane(V3(0, 3.5, 0), V3(0, 1, 0), mirror)
    Cube(V3(3, 2, -5), V3(2, 1, 1), rubber)
]

r.render()
r.write()