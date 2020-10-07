"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela
"""
from collections import Counter
lista = []

for x in range(10):
    n1 = int(input('Digite: '))
    lista.append(n1)

lista2 = Counter(lista)

for x in lista2:
    if lista2[x] > 1:
        print(f'O número {x} se repete {lista2[x]} vezes.')
