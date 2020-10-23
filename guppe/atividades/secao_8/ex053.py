"""
Faça uma funcao que verifica se uma matriz quadrada de ordem N é a matriz identidade.
"""
from random import randint


def identidade(x: list):
    soma = 0
    for i in range(len(x)):
        for j in range(len(x)):
            soma += x[i][j]
    if soma == len(x):
        return 'A matriz informada é uma matriz identidade!'
    else:
        return 'A matriz informada não é uma matriz identidade!'


n2 = randint(0, 1)
vetor = []
if n2 == 0:
    n1 = randint(2, 10)
    for z in range(n1):
        vetor.append([])
        for y in range(n1):
            vetor[z].append(randint(10, 99))
else:
    n1 = randint(2, 10)
    for z in range(n1):
        vetor.append([])
        for y in range(n1):
            if z == y:
                vetor[z].append(1)
            else:
                vetor[z].append(0)

for x in range(len(vetor)):
    print(vetor[x])

print()

print(identidade(vetor))
