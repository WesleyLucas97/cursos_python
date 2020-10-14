"""
Faça uma função que receba um vetor de reais e retorne a media dele
"""
import random


def media(x:list):
    tot = len(x)
    som = 0
    for i in x:
        som += i
    media = som / tot
    return media


lista = []

for x in range(random.randint(0, 10)):
    lista.append(random.randint(0, 1000) * random.random())

print(lista)
print(media(lista))
