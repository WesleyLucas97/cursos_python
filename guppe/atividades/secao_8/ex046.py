"""
Crie um programa contendo as seguintes funcoes que recebem um vetor V números reais como parâmetro:
    - Impressao normal do vetor.
    - Impressao inversa.
    - Funcao que retorna a média aritmética dos elementos do vetor.
"""
import random


def print_(x: list):
    return x


def inverso(x: list):
    lista = []
    for i in range(len(x) - 1, -1, -1):
        lista.append(x[i])
    return lista


def media_(x: list):
    media = sum(x) / len(x)
    return f'{media:.2f}'


vector = []
for j in range(random.randint(0, 15)):
    vector.append(random.randint(0, 30))

print(print_(vector))
print(inverso(vector))
print(media_(vector))
