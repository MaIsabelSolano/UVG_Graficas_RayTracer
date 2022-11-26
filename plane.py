from intersect import *
from vector import *
from intersect import * 

class Plane(object):
    def __init__(self, position, normal, material):
        # self.y = -y
        self.material = material
        self.normal = normal.normalize()
        self.position = position


    def ray_intersect(self, origin, direction):
        # dis = -(origin.y + self.y) / direction.y
        # pt = origin + (direction * dis)

        # # ??
        # if dis <= 0 or abs(pt.x) > 2 or pt.z > -5 or pt.z < -10:
        #     return None

        # norm = V3(0, 1, 0)

        # return Intersect(
        #     distance = dis,
        #     point = pt, 
        #     normal = norm

        # )

        denom = direction @ self.normal

        if abs(denom) > 0.0001:
            num = (self.position - origin) @ self.normal
            t = num/denom
            if t > 0:
                hit = origin + (direction * t)

                return Intersect(
                    distance = t,
                    point = hit,
                    normal = self.normal
                )

        return None