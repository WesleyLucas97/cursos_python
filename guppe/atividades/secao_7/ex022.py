"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores do
primeiro e nas posições impares os valores do segundo
"""
from random import randint
lista = []

for x in range(10):
    lista.append(randint(0, 100))

print(lista)

for x in range(2, 10):
    if lista[x] % 2 == 0:
        lista[x] = lista[0]
    else:
        lista[x] = lista[1]

print(lista)

mano_do_ceu = ['lindo', 'linda']
for x in mano_do_ceu:
    print(x)
