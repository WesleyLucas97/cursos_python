"""
Faca uma funcao que receba dois numeros inteiros positivos por parametros e retorne a soma dos N numeros
inteiros existentes entre eles.
"""
from random import randint
n1 = randint(0, 200)
n2 = randint(0, 200)


def soma(a, b):
    print(a, b)
    som = 0
    if a > b:
        a, b = b, a
    for x in range(a + 1, b):
        som += x
    return f'A soma dos numeros entre {a} e {b} eh {som}'


print(soma(n1, n2))
