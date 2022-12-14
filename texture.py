import struct
from lib import *
from color import *

class Texture(object):
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

    def get_color(self, tx, ty):
        if ty >= 1:
            ty -= 1

        x = round(tx * self.width)
        y = round(ty * self.height)

        p_color = Color(0, 0, 0)
        
        if (y < len(self.pixels)):
            if (x < len(self.pixels[y])):
                b = round(self.pixels[y][x].r)
                g = round(self.pixels[y][x].g)
                r = round(self.pixels[y][x].b)

                p_color = Color(r, g, b)

        return p_color


    def color_minmax_r(self, value):
        if (0 <= value <= 255 ):
            return round(value)
        elif (0 > value):
            return 0
        elif (value > 255):
            return 255

    """
    get_color_with_intensity:(int, int, int)
    Permite obtener los colores que se deben utilizar para cada punto y 
    dada una intensidad de iluminación oscurese el color
    Parámetros:
    tx:float
    ty:float 
    """
    def get_color_with_intensity(self, tx, ty, intensidad = 1):

        if ty >= 1:
            ty -= 1

        x = round(tx * self.width)
        y = round(ty * self.height)

        p_color = Color(0, 0, 0)
        
        if (y < len(self.pixels)):
            if (x < len(self.pixels[y])):
                b = round(self.pixels[y][x][0] * intensidad)
                g = round(self.pixels[y][x][1] * intensidad)
                r = round(self.pixels[y][x][2] * intensidad)

                p_color = Color(r, g, b)

        return p_color
