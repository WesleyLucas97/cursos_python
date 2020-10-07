"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
"""
from random import randint

lista = []
for x in range(10):
    lista.append(randint(-100, 100))

print(lista)

for x in range(10):
    if lista[x] < 0:
        lista[x] = 0

print(lista)
