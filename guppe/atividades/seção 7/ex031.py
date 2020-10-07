"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a uniao entre os 2 vetores anteriores,
ou seja, contém os números dos dois vetores. Nao deve conter números repetidos.
"""
from random import randint
vetor1 = []
vetor2 = []

for x in range(10):
    vetor1.append(randint(0, 100))
    vetor2.append(randint(0, 100))

uniao = vetor1.copy()
for x in vetor2:
    if x not in vetor1:
        if x not in uniao:
            uniao.append(x)

print(vetor1)
print(vetor2)
print(uniao)
print(len(uniao))
