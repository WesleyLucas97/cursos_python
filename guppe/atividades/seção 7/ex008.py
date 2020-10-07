"""
Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos na ordem inversa.
"""

lista = []

for x in range(6):
    n1 = int(input('Digite: '))
    lista.append(n1)
lista.reverse()

print(lista)
