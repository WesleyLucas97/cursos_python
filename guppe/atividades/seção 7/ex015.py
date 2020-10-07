"""
Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos repetidos.
"""
from collections import Counter
from random import randint

lista = []

for x in range(20):
    n1 = randint(0, 20)
    lista.append(n1)

lista2 = Counter(lista)

lista3 = []
for x in lista2:
    if lista2[x] == 1:
        lista3.append(x)

print(f'Os elementos não repetidos são {lista3}')
