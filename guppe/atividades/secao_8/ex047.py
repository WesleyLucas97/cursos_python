"""
Faça uma funcao que receba uma matriz 4x4 e retorne quantos valores maiores que 10 ela possui.
"""
from random import randint


def conta_(x: list):
    cont = 0
    for a in range(4):
        for b in range(4):
            if x[a][b] >= 10:
                cont += 1
    return cont


matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(4):
    for j in range(4):
        matriz[i][j] = randint(0, 20)

print(matriz)
print(conta_(matriz))
