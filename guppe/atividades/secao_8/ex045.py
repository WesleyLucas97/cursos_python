"""
Faça uma funcao que calcule o desvio padrao de um vetor v contendo n números

Desvio Padrao:

onde m é a media do vetor.
"""
import random
import math


def media(x: list):
    med = sum(x)/len(x)
    return med


def desvio(x: list):
    soma = 0
    for i in x:
        soma += pow(i - media(x), 2)
    desvio_padrao = math.sqrt((1 / (len(x) - 1)) * soma)
    return f'O desvio padrao do vetor {x} é {desvio_padrao:.5f}'


lista = []
for x in range(random.randint(2, 10)):
    lista.append(random.randint(0, 10) * random.random())

print(desvio(lista))
