from random import *


def test(n, d_0):
    compteur = 0
    for _ in range(10000):
        position = d_0
        i = 0
        while position != 0 and i < n:
            b = random( )
            if b>0.5:
                position += 1
            else:
                position -= 1
            i += 1
        if position != 0:
            compteur += 1
    return compteur / 10000

def test2(n, x, y):
    compteur = 0
    for _ in range(10000):
        position_x = x
        position_y = y
        i = 0
        while position_x != 0 and position_y != 0 and i < n:
            b = randint(0, 3)
            if b == 0:
                position_x += 1
            if b == 1:
                position_x -= 1
            if b == 2:
                position_y += 1
            else:
                position_y -= 1
            i += 1
        if position_x != 0 or position_y != 0:
            compteur += 1
    return compteur / 10000

print(test(5000,10))
