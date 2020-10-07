"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecçao entre os 2 vetores
anteriores, ou seja, que contém apenas os números que estao em ambos os vetores. Nao deve conter números repetidos.
"""
from random import randint
vetor1 = []
vetor2 = []
inter = []

for x in range(10):
    vetor1.append(randint(0, 200))
    vetor2.append(randint(0, 200))

for x in vetor1:
    if x in vetor2:
        if x not in inter:
            inter.append(x)

print(vetor1)
print(vetor2)
print(inter)
