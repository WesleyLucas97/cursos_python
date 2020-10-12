"""
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a media do vetor
"""
from math import sqrt
from random import randint
vetor = []

for x in range(10):
    vetor.append(randint(100, 1000))

media = sum(vetor) / len(vetor)

soma1 = 0
for x in range(10):
    quadrado = (vetor[x] - media) ** 2
    soma1 += quadrado

raiz = sqrt(soma1 / (len(vetor) - 1))

print(f'O desvio padrão do vetor {vetor} é igual a {raiz:.2f}')
