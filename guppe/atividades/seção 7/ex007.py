"""
Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a
posição que ele se encontra.
"""

lista = []

for x in range(10):
    n1 = int(input('Digite: '))
    lista.append(n1)

for u in range(10):
    if lista[u] == max(lista):
        posicao = u

print(f'O vetor é {lista}, tendo como maior elemento o número {max(lista)} presente na posição {posicao}')
