"""
Considere um vetor A com 11 elementos onde A1 < A2 < ... < A6 > A7 > A8 > ... > A11, ou seja, está ordenado em ordem
crescente até o sexto elemento, a partir desse elemento está ordenado em ordem decrescente. Dado o vetor da questao
anterior, proponha um algoritmo para ordenar os elementos.
"""
from random import randint
vetor1 = []
vetor2 = []
vetor3 = []

for x in range(11):
    vetor1.append(randint(-10, 10))
print(vetor1)

vetor2 = vetor1[0:6]
vetor2.sort()
vetor3 = vetor1[6::]
vetor3.sort()
vetor3.reverse()

if vetor2[5] < vetor3[0]:
    vetor2[5], vetor3[0] = vetor3[0], vetor2[5]
    vetor3.sort()
    vetor3.reverse()

vetor1 = vetor2 + vetor3

print(vetor1)
