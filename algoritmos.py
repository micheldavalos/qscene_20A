from random import randint
from math import sqrt

def get_puntos(n: int) -> list:
    puntos = []
    for i in range(n):
        x = randint(0, 500)
        y = randint(0, 500)
        puntos.append((x, y))
    
    return puntos

def distancia_euclidiana(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2 - y1)**2)

def puntos_mas_cercanos(puntos:list) -> list:
    resultado = []
    for punto in puntos:
        x1 = punto[0]
        y1 = punto[1]
        min = 1000
        cercano = (0, 0)
        for _punto in puntos:
            if punto != _punto:
                x2 = _punto[0]
                y2 = _punto[1]
                d = distancia_euclidiana(x1, y1, x2, y2)
                if d < min:
                    min = d
                    cercano = _punto
        resultado.append((punto, cercano))
    return resultado


