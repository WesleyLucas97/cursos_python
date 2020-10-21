"""
Escreva uma funcao que recebe uma matriz quadrada de ordem N e calcule a sua transposta ( se B é a matriz transposta de
A entao aij = bji).
"""
from random import randint


def transposta(x: list):
    transpos = []
    for i in range(len(x)):
        transpos.append([])
        for j in range(len(x)):
            transpos[i].append(x[j][i])
    return transpos


vetor = []
n1 = randint(1, 12)
n2 = 0

for z in range(n1):
    vetor.append([])
    for y in range(n1):
        vetor[z].append(randint(10, 99))

for z in range(n1):
    print(vetor[z])

print()
n3 = transposta(vetor)

for z in range(len(n3)):
    print(n3[z])
