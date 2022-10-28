class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g 
        self.b = b 

    def __mul__(self, other):

        r = self.r
        b = self.b
        g = self.g

        if (type(other) == Color):
            r *= other.r
            g *= other.g
            b *= other.b

        if (type(other) == int or type(other) == float):
            r *= other
            g *= other
            b *= other
            
        # bounding the colors to (0, 255)
        if r < 0:
            r = 0
        if r > 255:
            r = 255

        if g < 0:
            g = 0
        if g > 255:
            g = 255

        if b < 0:
            b = 0
        if b > 255:
            b = 255

        return Color(r, g, b)

    def toBytes(self):
        return bytes([
            int(self.b), 
            int(self.g), 
            int(self.r)
            ])

    def __repr__(self):
        return "Color(%s, %s, %s)" % (self.r, self.g, self.b)
