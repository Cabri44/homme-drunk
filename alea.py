from random import *
from math import *

def test(n, d_0):           #compte qui revient quand on est en 1D
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

def test2(n, x, y): #compte qui revient en 2D
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


def retour_1(n): # moyenne du premier temps de retour en 1D
    resultat = []
    for i in range(n):
        position = 0
        compteur = 0
        while position != 0 and compteur < 100000000 or compteur == 0:
            b = random()
            if b>0.5:
                position += 1
            else:
                position -= 1
            compteur += 1
        if compteur == 100000000:
            resultat.append(100000000)
        else:
            resultat.append(compteur)
    return resultat

def retour_2(n): # moyenne du premier temps de retour en 2D
    resultat = []
    for i in range(n):
        position_x = 0
        position_y = 0
        compteur = 0
        while (position_x != 0 or position_y != 0 ) and compteur < 100000 or compteur == 0:
            b = randint(0, 3)
            if b == 0:
                position_x += 1
            if b == 1:
                position_x -= 1
            if b == 2:
                position_y += 1
            else:
                position_y -= 1
            compteur += 1
        if compteur == 100000:
            resultat.append(100000)
        else:
            resultat.append(compteur)
    return resultat


def moyenne(l): 
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return (sum // len(l)) #partie entière de la moyenne

print("le temps retour moyen en 1D est ", moyenne(retour_1(100)))
print("le temps retour moyen en 2D est ", moyenne(retour_2(100)))







# comment retirer le 1 du "preuve 1" ?
# comment aligner à gauche les équations ?
# comment faire la grande acolade ?
# j'ai pas trouvé si l'espérance du premier retour à l'origine est infinie :(
# Pour le truc numérique, je commence à faire pleins de runs et je note ce que j'ai / fais des courbes ?
# C'est grave si j'ai que des maths ? Pas un peu boring ?
