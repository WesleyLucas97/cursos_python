"""
Faca uma funcao que receba um vetor de inteiros e o preencha com numeros aleatorios sem repeticao
"""
from random import randint


def preenche(x: list):
    n1 = 0
    while n1 < len(x):
        a = randint(0, 30)
        if a not in x:
            x[n1] = a
            n1 += 1

    return x


lista = []
for j in range(10):
    lista.append(j)

print(preenche(lista))
