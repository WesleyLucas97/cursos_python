"""
Faca uma funcao nao-recursiva que receba um numero inteiro positivo n e retorne o fatorial quadruplo desse numero.
O fatorial quadruplo de um numero n e dado por:
(2n)! / n!
"""
from random import randint


def fatorial(x):
    fat = 1
    if x == 0:
        fat = 1
    else:
        for i in range(1, x + 1):
            fat *= i
    return fat


def fatorial_quadruplo(x):
    return f'O fatorial quadruplo de {x} eh {(fatorial(2 * x)) / fatorial(x)}'


print(fatorial_quadruplo(randint(0, 10)))
