"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule o valor do cosseno desse angulo
usando sua respectiva serie de Taylor:


onde x e o valor do angulo em radianos. Considerar pi = 3.141593 e n variando de 0 ate 5.
"""
import math
from random import randint


def cons(x, n):
    som = 0
    n1 = x * (math.pi / 180)

    for i in range(n):
        chato = (-1) ** i
        som += (chato / math.factorial(2 * i)) * (n1 ** (2 * i))

    return f'O cosseno de {x} eh {som:.4f}'


a = randint(0, 361)
print(a)
print(cons(a, 150))
