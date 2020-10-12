"""
Faca uma funcao que receba um inteiro N como parametro, calcule e retorne o resultado da seguinte serie:
S = 2/4 + 5/5 + 10/6 + ... + (N2 + 1) / (N + 3)
"""
from random import randint

n = randint(0, 10000)
print(n)


def serie(x):
    S = 0
    for i in range(1, x + 1):
        S += ((i ** 2) + 1) / (i + 3)
    return S


print(serie(n))
