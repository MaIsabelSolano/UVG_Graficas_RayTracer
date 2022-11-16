# Universidad del Valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# Gráficas por computador

# Maria Isabel Solano 20504

from material import *
from ray import *
from vector import *
from light import *
from color import *

r = Raytracer(800, 600, 'RT_2.bmp')

# Materials
red =    Material(diffuse = Color(255, 0, 0))
white =  Material(diffuse = Color(255, 255, 255))
ivory =  Material(diffuse = Color(255, 200, 180), albedo = [0.6, 0.3, 0, 0],   spec = 10)
black_ivory =  Material(diffuse = Color(10, 10, 10), albedo = [0.6, 0.5, 0, 0],   spec = 10)
rubber = Material(diffuse = Color(180, 50, 0),     albedo = [0.9, 0.05, 0.1, 0], spec = 50)


# Ilumination
r.light = Light(V3(1, -4, -1), 1, Color(255, 255, 255))

# Objects 
r.scene = [
    # cuerpo
    
    Sphere(V3(-0.725, 1.5, -4.3), 0.35, rubber), # pata iz
    Sphere(V3(0.725, 1.5, -4.3), 0.35, rubber),  # pata der
    Sphere(V3(0.8, 0.2, -4.3), 0.3, rubber),    # brazo der
    Sphere(V3(-0.8, 0.2, -4.3), 0.3, rubber),   # brazo iz
    Sphere(V3(0, 1.0, -5), 1, ivory),           # torso

    # cabeza
    Sphere(V3(0, -0.5, -5), 0.9, rubber),               # cabeza
    Sphere(V3(0, -0.375, -4.4), 0.4, rubber),           # ocico
    Sphere(V3(0, -0.4, -4), 0.1, black_ivory),          # nariz
    Sphere(V3(-0.3, -0.6, -4.15), 0.075, black_ivory),  # ojo iz
    Sphere(V3(0.3, -0.6, -4.15), 0.075, black_ivory),   # ojo der
    Sphere(V3(-0.7, -1.2, -4.5), 0.275, rubber),            # oreja iz
    Sphere(V3(0.7, -1.2, -4.5), 0.275, rubber),             # oreja iz
    
]

r.render()
r.write()