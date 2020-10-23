"""
Faça uma função que recebe, por parâmetro, uma matriz A[4][4] e retorna a soma dos seus elementos
"""
from random import randint


def soma_matriz(x: list):
    soma = 0
    for i in range(len(x)):
        for j in range(len(x)):
            soma += x[i][j]
    return f'A soma da tabela resulta em {soma}'


vetor = []

for a in range(4):
    vetor.append([])
    for b in range(4):
        vetor[a].append(randint(10, 99))

for a in range(4):
    print(vetor[a])


print(soma_matriz(vetor))
