import imp
from turtle import back
from lib import *
from sphere import *
from light import *
from intersect import *
from color import *
from math import pi, tan

class Raytracer(object):
    def __init__(self, width, height, filename):
        self.width = width
        self.height = height
        self.filename = filename
        self.framebuffer = []
        self.background_color = Color(10, 10, 10)
        self.current_color = Color(255, 255, 255)
        self.scene = []
        self.light = Light(V3(0, 0, 0), 1)
        self.MAX_RECURSION_DEPTH = 2

        self.clear()
        self.write()

    def clear(self):
        self.framebuffer = [
            [self.background_color.toBytes() for x in range(self.width)]
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
                
                self.point(x, y, c.toBytes())

    def cast_ray(self, origin, direction, recursion = 0):

        if (recursion >= self.MAX_RECURSION_DEPTH):
            return self.background_color

        material, intersect = self.scene_intersect(origin, direction)

        if (material is None):
            return self.background_color

        light_dir = (self.light.position - intersect.point).normalize()
        ligth_distance = (self.light.position - intersect.point).length()

        # Other objects' shadows
        shadow_bias = 1.1
        shadow_orgin = intersect.point - (intersect.normal * shadow_bias) if light_dir @ intersect.normal < 0 else intersect.point + (intersect.normal * shadow_bias)
        shadow_material, shadow_intersect = self.scene_intersect(shadow_orgin, light_dir)
        shadow_intensity = 0

        if shadow_material and (shadow_intersect.point - shadow_orgin).length() < ligth_distance:
            # Something is generating a shadow over the object
            shadow_intensity = 0.3

        # Difusse component

        diffuse_intensity = self.light.intensity * (light_dir @ intersect.normal)
        diffuse = material.diffuse * diffuse_intensity * material.albedo[0] * (1 - shadow_intensity)

        # Specular component
        light_reflection = reflect(light_dir, intersect.normal)
        reflection_intensity = max(0, light_reflection @ direction)

        specular = Color(0, 0, 0)
        if (shadow_intensity == 0):
            # Specular light is not shown while an object is generating a shadow over the object
            specular_intensity = self.light.intensity * reflection_intensity **material.spec
            specular = self.light.c * specular_intensity * material.albedo[1]

        # Object reflections
        reflect_color = Color(0, 0, 0)
        # if (material.albedo[2] > 0):
        #     reverse_direction = direction * -1
        #     reflect_direction = reflect(reverse_direction, intersect.normal)
        #     reflect_bias = -0.5 if reflect_direction @ intersect.normal < 0 else 0.5
        #     reflect_origin = intersect.point + (intersect.normal * reflect_bias)
        #     reflect_color = self.cast_ray(reflect_origin, reflect_direction, recursion + 1)

        reflection = reflect_color * material.albedo[2]

        # Object reflections
        refract_color = Color(0, 0, 0)
        if (material.albedo[3] > 0):
            refract_direction = refract(direction, intersect.normal, material.refractive_index)
            refract_bias = 0.5 if refract_direction @ intersect.normal < 0 else -0.5
            refract_origin = intersect.point + (intersect.normal * refract_bias)
            refract_color = self.cast_ray(refract_origin, refract_direction, recursion + 1)

        refraction = refract_color * material.albedo[3]

        return diffuse + specular + reflection + refraction

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

    