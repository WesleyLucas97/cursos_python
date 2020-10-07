"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor denominado
C calculando C = A - B. Mostre na tela os dados do vetor C.
"""
from random import randint
A = []
B = []
C = []

for x in range(10):
    A.append(randint(-100, 100))
    B.append(randint(-100, 100))

for x in range(10):
    C.append(A[x] - B[x])

print(A)
print(B)
print(C)
