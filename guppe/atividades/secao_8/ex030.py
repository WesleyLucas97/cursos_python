"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule o valor do cosseno hiperbolico
desse angulo usando sua respectiva serie de Taylor:


onde x e o valor do angulo em radianos. Considerar pi = 3.141593 e n variando de 0 ate 5.
"""
from random import randint
import math


def coshyp(x):
    som = 0
    n1 = x * (math.pi / 180)

    for n in range(20):
        som += (n1 ** (2 * n)) / (math.factorial(2 * n))

    return f'O cosseno hiperbolico de {x} eh {som:.4f}'


a = randint(0, 361)
print(coshyp(a))
print(math.cosh(a * (math.pi / 180)))
