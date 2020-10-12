"""
Faca uma funcao para calcular o numero neperiano usando uma serie. A funcao deve ter como parametro o numero de termos
que serao somados (note que, quanto maior o numero, mais proxima a resposta estara do valor e).
"""
from random import randint
from math import factorial


def neperiano(x):
    som = 0

    for n in range(x):
        som += 1 / factorial(n)

    return f'O valor de e = {som}'


a = randint(0, 1000)
print(a)
print(neperiano(a))
