"""
Faça uma função que recebe, por parâmetro, duas matrizes quadradas de ordem N, A e B, e retorna uma matriz C, também
por parâmetro, que seja o produto matricial de A e B.
"""

"""
Desisto de fazer essa merda, tomar no cu, tem uma biblioteca pronta.
"""
import numpy as np
import random

vetor1 = []
vetor2 = []

n = random.randint(2, 5)

for i in range(n):
    vetor1.append([])
    for j in range(n):
        vetor1[i].append(random.randint(1, 9))

for i in range(n):
    vetor2.append([])
    for j in range(n):
        vetor2[i].append(random.randint(1, 9))

for i in range(n):
    print(vetor1[i])

print()

for i in range(n):
    print(vetor2[i])

print()
print(np.multiply(vetor1, vetor2))
