"""
Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene em um vetor com 10 posições. Preencha
um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.
"""
from random import randint
lista = []
lista2 = []

for x in range(10):
    lista.append(randint(0, 50))

for x in range(10):
    if lista[x] % 2 != 0:
        lista2.append(lista[x])

print(lista)
print(lista2)
