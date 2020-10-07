"""
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor
e mostre-os na tela.
"""
from random import randint
lista = []

for x in range(10):
    lista.append(randint(1, 200))

lista2 = []

x = randint(1, 10)
for y in range(10):
    if lista[y] % x == 0:
        lista2.append(lista[y])

if len(lista2) == 0:
    print('Não tem nenhum multiplo')
else:
    print(f'Os números {lista2} são multiplos de {x}')
