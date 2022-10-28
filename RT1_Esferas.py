from material import *
from ray import *
from vector import *
from light import *


r = Raytracer(800, 800, 'RT_1.bmp')

# Materials
red = Material(diffuse = color(255, 0, 0))
white = Material(diffuse = color(255, 255, 255))
black = Material(diffuse = color(0, 0, 0))
orange = Material(diffuse = color(230, 100, 0))

# Ilumination
r.light = Light(V3(0, 0, 0), 1)

# Objects 
r.scene = [
    #Sphere(V3(-3, 0, -16), 2, red),
    Sphere(V3(0, -2.5, -10),   1, white), # Bola de arriba
    Sphere(V3(0, -0.5, -10), 1.5, white), # Bola del medio
    Sphere(V3(0,    2, -10),   2, white), # Bola de abajo

    # Cara
    Sphere(V3(-0.4, -2.2, -8), 0.15, black), # Ojo izquierdo
    Sphere(V3( 0.4, -2.2, -8), 0.15, black), # Ojo derecho
    Sphere(V3(   0,   -2, -8), 0.15, orange), # Ojo derecho
    Sphere(V3(-0.4, -1.8, -8), 0.10, black), # boca far left
    Sphere(V3(-0.2, -1.6, -8), 0.10, black), # boca medium left
    Sphere(V3( 0.2, -1.6, -8), 0.10, black), # boca medium right
    Sphere(V3( 0.4, -1.8, -8), 0.10, black), # boca far right

    # Botones
    Sphere(V3( 0,  -1, -8), 0.10, black), # 1
    Sphere(V3( 0, -0.7, -8), 0.10, black), # 2
    Sphere(V3( 0, -0.4, -8), 0.10, black), # 3
    Sphere(V3( 0, -0.1, -8), 0.10, black), # 4
]

r.render()
r.write()