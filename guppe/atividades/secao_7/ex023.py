"""
Ler dois conjuntos de números reais, armazenando-os em vetores e calcular o produto escalar entre eles. Os conjuntos têm
5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por:
x1 * y1 + x2 * y2 + ... + xn * yn
"""
from random import randint
lista1 = []
lista2 = []

for x in range(5):
    lista1.append(randint(-100, 100))
    lista2.append(randint(-100, 100))

soma = 0

for x in range(5):
    soma += (lista1[x] * lista2[x])

print(f'O produto escalar dos vetores A = {lista1} e B = {lista2}, tem como resultado o seguinte valor {soma}')
