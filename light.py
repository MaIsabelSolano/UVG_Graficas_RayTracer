from color import *

class Light(object):
    def __init__(self, position, intensity, c= Color(255, 255, 255)):
        self.position = position
        self.intensity = intensity
        self.c = c