"""
Faça uma função que receba um vetor de inteiros e retorne o maior valor
"""
from random import randint


def maior(x:list):
    big = x[0]
    for i in x:
        if i > big:
            big = i
    return big


lista = []
for x in range(randint(0, 10)):
    lista.append(randint(0, 100))
print(lista)
print(maior(lista))
