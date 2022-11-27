from material import *
from ray import *
from vector import *
from light import *
from color import *
from plane import *
from cube import *

r = Raytracer(800, 600, 'r.bmp', './sky.bmp')

# textures
g = Texture('./grass.bmp')
w = Texture('./wood.bmp')
s = Texture('./sand.bmp')
f = Texture('./foliage.bmp')
wt = Texture('./water.bmp')

# Materials
red =    Material(diffuse = Color(255, 0, 0))
white =  Material(diffuse = Color(255, 255, 255))
ivory =  Material(diffuse = Color(200, 200, 180), albedo = [0.6, 0.3, 0, 0],   spec = 10)
rubber = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.1, 0.1, 0], spec = 50)
mirror = Material(diffuse = Color(255, 255, 255), albedo = [0, 1, 0.8, 0],     spec = 1425)
glass =  Material(diffuse = Color(150, 180, 200), albedo = [0, 0.5, 0.1, 0.8], spec = 125,  refractive_index = 1.5)
grass = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.05, 0.05, 0], spec = 10, texture = g)
wood = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.05, 0.05, 0], spec = 10, texture = w)
sand = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.05, 0.05, 0], spec = 10, texture = s)
foliage = Material(diffuse = Color(180, 0, 0),     albedo = [0.9, 0.2, 0.2, 0], spec = 10, texture = f)
water = Material(diffuse = Color(50, 50, 200), albedo = [0.4, 0.5, 0.1, 0.8], spec = 120, refractive_index = 1)

# Ilumination
r.light = Light(V3(10, -13, 20), 1, Color(255, 255, 255))

# Objects 
r.scene = [
    # Sphere(V3(0, -1.5, -11), 1.5, ivory),
    # Sphere(V3(-0.25, 0, -6), 0.5, glass),
    # Sphere(V3(1, 1, -8), 1.7, rubber),
    # Sphere(V3(0, 0, -5), 2, mirror),
    # Sphere(V3(2, -0.9, -5.5), 1, ivory),
    # Plane(V3(0, 3.5, 0), V3(0, 1, 0), mirror)
    # Cube(V3(3, 2, -5), V3(2, 1, 1), grass)






    Cube(V3(0, 2, -5), V3(1, 1, 1), grass),
    Cube(V3(-1, 2, -5), V3(1, 1, 1), grass),
    Cube(V3(-2, 2, -5), V3(1, 1, 1), grass),
    Cube(V3(-3, 2, -5), V3(1, 1, 1), grass),
    Cube(V3(-4, 2, -5), V3(1, 1, 1), grass),

    Cube(V3(0, 3, -5), V3(1, 1, 1), grass),
    Cube(V3(-1, 3, -5), V3(1, 1, 1), grass),
    Cube(V3(-2, 3, -5), V3(1, 1, 1), grass),
    Cube(V3(-3, 3, -5), V3(1, 1, 1), grass),

    Cube(V3(0, 2, -6), V3(1, 1, 1), grass),
    Cube(V3(-1, 2, -6), V3(1, 1, 1), grass),
    Cube(V3(-2, 2, -6), V3(1, 1, 1), grass),
    Cube(V3(-3, 2, -6), V3(1, 1, 1), grass),
    Cube(V3(-4, 2, -6), V3(1, 1, 1), grass),
    Cube(V3(-4, 5, -6), V3(1, 1, 1), grass),

    Cube(V3(0, 2, -7), V3(1, 1, 1), grass),
    Cube(V3(-1, 2, -7), V3(1, 1, 1), grass),
    Cube(V3(-2, 2, -7), V3(1, 1, 1), grass),
    Cube(V3(-3, 2, -7), V3(1, 1, 1), grass),
    Cube(V3(-4, 2, -7), V3(1, 1, 1), grass),
    Cube(V3(-5, 2, -7), V3(1, 1, 1), grass),

    Cube(V3(0, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-1, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-2, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-3, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-4, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-5, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-7, 2, -10), V3(1, 1, 5), grass),
    Cube(V3(-8, 2, -10), V3(1, 1, 5), grass),

    Cube(V3(0, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(1, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(2, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(3, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(4, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(5, 2, -8), V3(1, 1, 1), grass),
    Cube(V3(6, 2, -8), V3(1, 1, 1), grass),

    Cube(V3(0, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(1, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(2, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(3, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(4, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(5, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(6, 2, -9), V3(1, 1, 1), grass),
    Cube(V3(7, 2, -9), V3(1, 1, 1), grass),

    Cube(V3(0, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(1, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(2, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(3, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(4, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(5, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(6, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(7, 2, -10), V3(1, 1, 1), grass),
    Cube(V3(8, 2, -10), V3(1, 1, 1), grass),

    Cube(V3(-9, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-8, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-7, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-6, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-5, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-4, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-3, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-2, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(-1, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(0, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(1, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(2, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(3, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(4, 2, -11), V3(1, 1, 1), grass),
    Cube(V3(5, 2, -11), V3(1, 1, 1), grass),

    Cube(V3(0, 0, -13), V3(3, 4, 1), grass),

    Cube(V3(6, 2, -11), V3(1, 1, 1), sand),

    Cube(V3(7, 2, -11), V3(1, 1, 1), sand),
    Cube(V3(8, 2, -11), V3(1, 1, 1), sand),
    Cube(V3(9, 2, -11), V3(1, 1, 1), sand),

    Cube(V3(5, 2.2, -6), V3(11, 1, 11), water),

    Cube(V3(0, 2, -3), V3(1, 1, 1), sand),

    Cube(V3(0, 3, -5), V3(1, 1, 1), sand),
    Cube(V3(1, 3, -5), V3(1, 1, 1), sand),
    Cube(V3(2, 3, -5), V3(1, 1, 1), sand),
    Cube(V3(3, 3, -5), V3(1, 1, 1), sand),
    Cube(V3(4, 3, -5), V3(1, 1, 1), sand),

    Cube(V3(0, 3, -6), V3(1, 1, 1), sand),
    Cube(V3(1, 3, -6), V3(1, 1, 1), sand),
    Cube(V3(2, 3, -6), V3(1, 1, 1), sand),
    Cube(V3(3, 3, -6), V3(1, 1, 1), sand),
    Cube(V3(4, 3, -6), V3(1, 1, 1), sand),
    Cube(V3(5, 3, -6), V3(1, 1, 1), sand),

    Cube(V3(0, 3, -7), V3(1, 1, 1), sand),
    Cube(V3(1, 3, -7), V3(1, 1, 1), sand),
    Cube(V3(2, 3, -7), V3(1, 1, 1), sand),
    Cube(V3(3, 3, -7), V3(1, 1, 1), sand),
    Cube(V3(4, 3, -7), V3(1, 1, 1), sand),
    Cube(V3(5, 3, -7), V3(1, 1, 1), sand),

    Cube(V3(-2, 1, -5), V3(1, 1, 1), wood),
    Cube(V3(-2, 0, -5), V3(1, 1, 1), wood),

    Cube(V3(-3, -1, -4), V3(1, 1, 1), foliage),
    Cube(V3(-2, -1, -4), V3(1, 1, 1), foliage),
    Cube(V3(-1, -1, -4), V3(1, 1, 1), foliage),

    Cube(V3(-1, -1, -5), V3(1, 1, 1), foliage),
    Cube(V3(-3, -1, -5), V3(1, 1, 1), foliage),
    Cube(V3(-2, -2, -5), V3(1, 1, 1), foliage),

    Cube(V3(-1, -1, -6), V3(1, 1, 1), foliage),
    Cube(V3(-3, -1, -6), V3(1, 1, 1), foliage),
    Cube(V3(-2, -1, -6), V3(1, 1, 1), foliage),


]

r.render()
r.write()