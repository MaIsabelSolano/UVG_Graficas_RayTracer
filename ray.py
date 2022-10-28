import imp
from turtle import back
from lib import *
from sphere import *
from light import *
from intersect import *
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
        self.light = Light(V3(0, 0, 0), 1)

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
        material, intersect = self.scene_intersect(origin, direction)

        if material is None:
            return self.background_color

        light_dir = (self.light.position - intersect.point).normalize()
        intensity = light_dir @ intersect.normal

        deffuse = color(
            # int(material.diffuse[2] * intensity),
            # int(material.diffuse[1] * intensity),
            # int(material.diffuse[0] * intensity)
            int(material.diffuse[2]),
            int(material.diffuse[1]),
            int(material.diffuse[0])
        )
        return deffuse

    def scene_intersect(self, origin, direction):
        zBuffer = 999999
        material = None
        intersect = None
        
        for o in self.scene:
            object_intersect = o.ray_intersect(origin, direction)
            if object_intersect:
                if object_intersect.distance < zBuffer:
                    zBuffer = object_intersect.distance
                    material = o.material
                    intersect = object_intersect
            
        return material, intersect

    