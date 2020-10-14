"""
Faça uma funcao que receba como parâmetro um vetor X de 30 elementos inteiros e retorne, também por parâmetro, dois
vetores A e B. O vetor A deve conter os elementos pares de X e o vetor B, os elementos ímpares.
"""
from random import randint


def separa(x: list):
    a = []
    b = []
    for i in x:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)

    return f'Os elementos pares sao {a} e os ímpares sao {b}'


lista = []

for n in range(30):
    lista.append(randint(0, 50))

print(lista)
print(separa(lista))
