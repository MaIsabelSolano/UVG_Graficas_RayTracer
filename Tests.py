from ray import *

r = Raytracer(800, 600, 'r.bmp')
r.point(100, 100)
r.point(200, 300, color(255, 0, 0))
r.render()
r.write()