"""
Faca uma funcao nao-recursiva que receba um numero inteiro positivo n e retorne o hiperfatorial desse numero.
O hiperfatorial de um numero n, escrito H(n), e' definido por:
"""
from random import randint


def H(x):
    supf = 1
    for i in range(1, x + 1):
        supf *= (i ** i)

    return f'O superfatorial de {x} eh {supf}'


print(H(randint(0, 10)))
