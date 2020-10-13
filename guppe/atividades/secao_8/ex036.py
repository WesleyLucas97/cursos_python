"""
Faca uma funcao nao-recursiva que receba um numero inteiro positivo N e retorne o superfatorial desse numero. O
superfatorial de um numero N e definida pelo produto dos N primeiros fatoriais de N. Assim, o superfatorial de 4
e sf(4) = 1! * 2! * 3! * 4! = 288.
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


def sf(x):
    fat = 1
    for i in range(1, x + 1):
        fat *= fatorial(i)

    return f'O superfatorial de {x} eh {fat}'


print(sf(randint(0, 10)))
