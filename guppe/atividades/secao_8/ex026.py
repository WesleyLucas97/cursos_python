"""
Faca um algoritmo que receba um numero inteiro positivo n e calcule o somatorio de 1 ate n.
"""
from random import randint

n = randint(0, 100)
print(n)


def somatorio(a):
    som = 0
    for x in range(1, a + 1):
        som += x
    return som


print(somatorio(n))
