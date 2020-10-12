"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule o valor do seno hiperbolico
desse angulo usando sua respectiva serie de Taylor:


onde x e o valor do angulo em radianos. Considerar pi = 3.141593 e n variando de 0 ate 5.
"""
from random import randint
import math


def sinhyp(x, n):
    som = 0
    n1 = x * (math.pi / 180)

    for j in range(n):
        som += ((n1 ** ((2 * j) + 1)) / (math.factorial((2 * j) + 1)))

    return f'O seno hiperbolico de {x} eh {som:.4f}'


a = randint(0, 361)
print(a)
print(sinhyp(a, 10))
print(math.sinh(a * (math.pi / 180)))
