"""
Faça uma função que recebe, por parâmetro, uma matriz A[3][3] e retorna a soma dos elementos da sua diagonal principal
e da sua diagonal secundária
"""
from random import randint


def soma_diagonais(x: list):
    diagonal1 = 0
    diagonal2 = 0
    n2 = len(x) - 1
    for a in range(len(x)):
        for b in range(len(x)):
            if a == b:
                diagonal1 += x[a][b]
            if b == n2:
                diagonal2 += x[a][b]
        n2 -= 1
    return f'A soma da diagonal principal é {diagonal1} e da diagonal secundaria é {diagonal2} e a soma das duas é {diagonal1 + diagonal2}'


vetor = []

n = randint(3, 10)
for j in range(n):
    vetor.append([])
    for y in range(n):
        vetor[j].append(randint(10, 99))

for j in range(len(vetor)):
    print(vetor[j])

print(soma_diagonais(vetor))

