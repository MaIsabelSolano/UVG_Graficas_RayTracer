from intersect import *
from vector import *
from intersect import * 

class Plane(object):
    def __init__(self, y, material):
        self.y = -y
        self.material = material


    def ray_intersect(self, origin, direction):
        dis = -(origin.y + self.y) / direction.y
        pt = origin + (direction * dis)

        # ??
        if dis <= 0 or abs(pt.x) > 2 or pt.z > -5 or pt.z < -10:
            return None

        norm = V3(0, 1, 0)

        return Intersect(
            distance = dis,
            point = pt, 
            normal = norm

        )