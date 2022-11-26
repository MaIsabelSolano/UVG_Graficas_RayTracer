from lib import *
from color import *
from math import pi, acos, atan2

class Envmap(object):
    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            # Info del archivo
            image.seek(2 + 4 + 2 +2)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 2 + 2 + 4 + 4)

            # Tamaño del archivo
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            # Pasamos el encabezado
            image.seek(header_size)

            # Obtenemos todos los colores de la imagen
            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(
                        Color(r, g, b)
                    )
    
    def get_color(self, direction):

        h = 1000
        w = 2000
        direction = direction.normalize()

        x = int((atan2(direction.z, direction.x) / (2 * pi) + 0.5) * w)
        y = int(acos(-direction.y) / pi * h)
        

        return self.pixels[y][x]
        