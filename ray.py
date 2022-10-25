from turtle import back
from lib import *
from sphere import *
from math import pi, tan

class Raytracer(object):
    def __init__(self, width, height, filename):
        self.width = width
        self.height = height
        self.filename = filename
        self.framebuffer = []
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.scene = []

        self.clear()
        self.write()

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
        
    def point(self, x, y, c = None):
        if (0 <= x < self.width and 0 <= y < self.height ):
            self.framebuffer[y][x] = c or self.current_color

    def write(self):
        writebmp(
            self.filename, 
            self.width, 
            self.height, 
            self.framebuffer
        )

    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)
        
        for y in range(self.height):
            for x in range(self.width):
                
                i = ((2 * (x + 0.5) / self.width) - 1) * ar * tana
                j = (1 - (2 * (y + 0.5) / self.height)) * tana

                direction = V3(i, j, -1).normalize()
                origin = V3(0, 0, 0)

                c = self.cast_ray(origin, direction)

                self.point(x, y, c)

    def cast_ray(self, origin, direction):
        material = self.scene_intersect(origin, direction)

        if material:
            return material.diffuse
        else:
            return self.background_color

    def scene_intersect(self, origin, direction):
        zBuffer = 999999
        material = None
        
        for o in self.scene:
            intersect = o.ray_intersect(origin, direction)
            if intersect:
                if intersect.distance < zBuffer:
                    zBuffer = intersect.distance
                    material = o.material
            
        return material

    