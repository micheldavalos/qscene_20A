from random import randint

def get_puntos(n: int) -> list:
    puntos = []
    for i in range(n):
        x = randint(0, 500)
        y = randint(0, 500)
        puntos.append((x, y))
    
    return puntos


