from plane import *

class Cube(object):
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        self.planes = []

        self.boundsMin = [0, 0, 0]
        self.boundsMax = [0, 0, 0]

        halfx = size.x / 2
        halfy = size.y / 2
        halfz = size.y / 2

        # Sides of the cube
        self.addToPlanes([
            # sides
            Plane((position + V3(halfx, 0, 0)), V3(1, 0, 0), self.material),
            Plane((position + V3(-halfx, 0, 0)), V3(-1, 0, 0), self.material),

            # top and bottom
            Plane((position + V3(0, halfy, 0)), V3(0, 1, 0), self.material),
            Plane((position + V3(0, -halfy, 0)), V3(0, -1, 0), self.material),

            # Front and back
            Plane((position + V3(0, 0, halfz)), V3(0, 0, 1), self.material),
            Plane((position + V3(0, 0, -halfz)), V3(0, 0, -1), self.material),

        ])

        # Bounds
        epsilon = 0.001
        
        self.boundsMin[0] = self.position.x - (epsilon + self.size.x/2)
        self.boundsMax[0] = self.position.x + (epsilon + self.size.x/2)

        self.boundsMin[1] = self.position.y - (epsilon + self.size.y/2)
        self.boundsMax[1] = self.position.y + (epsilon + self.size.y/2)

        self.boundsMin[2] = self.position.z - (epsilon + self.size.z/2)
        self.boundsMax[2] = self.position.z + (epsilon + self.size.z/2)

    def ray_intersect(self, origin, direction):
        intersect = None

        t = float('inf')

        # uvs = None

        for plane in self.planes:
            planeInter = plane.ray_intersect(origin, direction)
            if planeInter is not None:
                if planeInter.point.x >= self.boundsMin[0] and planeInter.point.x <= self.boundsMax[0]:
                    if planeInter.point.y >= self.boundsMin[1] and planeInter.point.y <= self.boundsMax[1]: 
                        if planeInter.point.z >= self.boundsMin[2] and planeInter.point.z <= self.boundsMax[2]: 
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

                                u, v = 0, 0

                                if abs(plane.normal.x) > 0:
                                    u = (planeInter.point.y - self.boundsMin[1]) / (self.boundsMax[1] - self.boundsMin[1])
                                    v = (planeInter.point.x - self.boundsMin[2]) / (self.boundsMax[2] - self.boundsMin[2])

                                elif abs(plane.normal.y) > 0:
                                    u = (planeInter.point.x - self.boundsMin[0]) / (self.boundsMax[0] - self.boundsMin[0])
                                    v = (planeInter.point.z - self.boundsMin[2]) / (self.boundsMax[2] - self.boundsMin[2])

                                elif abs(plane.normal.z) > 0:
                                    u = (planeInter.point.x - self.boundsMin[0]) / (self.boundsMax[0] - self.boundsMin[0])
                                    v = (planeInter.point.y - self.boundsMin[1]) / (self.boundsMax[1] - self.boundsMin[1])

        if intersect is None:
            return

        return Intersect(
            distance = intersect.distance,
            point = intersect.point,
            normal = intersect.normal,
            tcoords = (u, v)
        )

    def addToPlanes(self, planes):
        for plane in planes:
            self.planes.append(plane)