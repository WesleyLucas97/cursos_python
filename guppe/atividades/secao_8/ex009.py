"""
Faca uma funcao que receba a altura e o raio de um cilindro circular e retorne o volume do cilindro.
O volume de um cilindro circular e calculado por meio da seguinte formula:
v = pi * raio2 * altura, onde pi = 3.141592
"""
from random import randint
r = randint(0, 10)
h = randint(0, 100)


def volume(raio, altura=1):
    from math import pi
    return pi * (raio ** 2) * altura


print(f'O volume do cilindro de raio {r} e altura {h}, tem como volume {volume(r, h):.3f}')
