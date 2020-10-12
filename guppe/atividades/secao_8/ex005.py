"""
Faca uma funcao e um programa de teste para o calculo do volume de uma esfera. Sendo que o raio e passado por parametro.
V = 4/3 * pi * R3
"""
from random import randint
r = randint(0, 5)


def volume(x):
    v = 4/3 * 3.1415 * (x ** 3)
    return f'{v:.2f}'


print(volume(r))
