class Intersect(object):
    def __init__(self, distance, point, normal, tcoords = None):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.tcoords = tcoords