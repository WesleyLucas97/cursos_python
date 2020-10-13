"""
Faca uma funcao que receba um numero N e retorne a soma dos algarismos de N!.
Ex: se N = 4, N! = 24. Logo, a soma de seus algarismos e' 2 + 4 = 6.
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


def soma(x):
    a = fatorial(x)
    numero = list(str(a))
    som = 0

    for j in numero:
        som += int(j)

    return f'O numero {x} tem como fatorial o numero {a} e a soma desses termos resulta em {som}'


print(soma(randint(0, 10)))
