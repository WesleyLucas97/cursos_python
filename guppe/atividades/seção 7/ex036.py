"""
Leia um vetor com 10 números reais, ordene os elementos deste vetor, e no final escreva os elementos do vetor ordenado.
"""
from random import randint
vetor = []

for x in range(10):
    vetor.append(randint(-100, 100))
vetor.sort()

print(vetor)
