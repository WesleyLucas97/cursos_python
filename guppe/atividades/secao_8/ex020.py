"""
Faca um algoritmo que receba um numero inteiro positivo n e calcule o seu fatorial, n!.
"""
from random import randint

n = randint(1, 10)


def fatorial(x):
    fat = 1
    for i in range(x, 0, -1):
        fat *= i
    return f'{x}! = {fat}'


print(fatorial(n))
