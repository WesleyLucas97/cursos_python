"""
Faça uma funcao que receba uma matriz de 3x3 elementos. Calcule e retorne a soma dos elementos que estao na diagonal
principal
"""
from random import randint


def diagonal(x: list):
    soma = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                soma += x[i][j]
    return soma


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for a in range(3):
    for b in range(3):
        matriz[a][b] = randint(10, 90)

print(f"""[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}]
[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}]
[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}]""")
print(diagonal(matriz))
