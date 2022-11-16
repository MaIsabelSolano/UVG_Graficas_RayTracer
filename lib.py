import struct
from vector import *
from color import *

""" Estructuras necesarias para crear un archivo BMP """

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w): 
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

""" Funciones necesarias """

# clase color, recibe en rgb y lo retorna en bytes en el orden requerido
# def color(r, g, b):
#     return bytes([b, g, r])

def color_minmax(v):
    if (0 < v < 255):
        return round(v)
    elif (v < 0):
        return 0
    elif (v > 255):
        return 255

""" Colores pre-establecidos """

BLACK = Color(0, 0, 0).toBytes()
WHITE = Color(255, 255, 255).toBytes()
RED = Color(250, 0, 0).toBytes()
ORANGE = Color( 200, 100, 0).toBytes()
BLUE = Color(0, 0, 255).toBytes()
GREEN = Color(0, 255, 0).toBytes()

def bounding_box(A, B, C):
    coords = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    xmin = 99999999
    xmas = -99999999
    ymin = 99999999
    ymax = -99999999

    for (x, y) in coords:
        if (x < xmin):
            xmin = x
        if (x > xmas):
            xmax = x
        if (y < ymin):
            ymin = y
        if (y > ymax):
            ymax = y
    
    return V3

def barycentric(A, B, C, P):

    cordenada = V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y)

    c_x = cordenada.x
    c_y = cordenada.y
    c_z = cordenada.z

    u = 0
    v = 0
    w = 0

    if (c_z != 0):
        u = c_x / c_z
        v = c_y / c_z
        w = 1 - (u + v)

    return (w, v, u)

def writebmp(filename, w, h, fb):
    f = open(filename, 'bw')

    # pixel header
    f.write(char('B'))
    f.write(char('M'))
    f.write(dword(14 + 40 + w * h* 3))
    f.write(word(0))
    f.write(word(0))
    f.write(dword(14 + 40))

    # info header
    f.write(dword(40))
    f.write(dword(w))
    f.write(dword(h))
    f.write(word(1))
    # colores:
    f.write(word(24))
    # compresión:
    f.write(dword(0))
    # tamaño de la imagen sin el header
    f.write(dword(w * h * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # pixel data
    for y in range(h):
        for x in range(w):
            f.write(fb[y][x])

    f.close()

def reflect(I, N):
    # Lm = I * N
    # n = (2 * (Lm @ N))
    return (I - (N * (2 * (I @ N))))
    # return (Lm - n).normalize()

def refract(I, N, roi):
    etai = 1
    etat = roi

    cosi = (I @ N) * -1

    if (cosi < 0):
        cosi *= -1
        etai *= -1
        etat *= -1
        N *= -1

    eta = etai/etat
    k = 1 - eta **2 * (1 - cosi **2)

    if k < 0:
        return V3(0, 0, 0)

    cost = k ** 0.5

    return ((I * eta) + (N * (eta * cosi - cost))).normalize()