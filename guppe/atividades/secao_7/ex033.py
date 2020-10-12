"""
Faça um programa que leia um vetor de 15 posicoes e o compacte, ou seja, elimine as posicoes com valor zero. Para isso,
todos os elementos a frente do valor zero, devem ser movidos uma posicao para tras no vetor.
"""
from random import randint
vetor = []

for x in range(randint(0, 30)):
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
        vetor.append(randint(0, 100))
    else:
        vetor.append(0)

print(vetor)

n1 = 0
while True:
    if n1 < len(vetor):
        if vetor[n1] == 0:
            vetor.pop(n1)
    else:
        break
    n1 += 1

print(vetor)
