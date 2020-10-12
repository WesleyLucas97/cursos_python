"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.
"""

lista = []
lista2 = []

for x in range(10):
    n1 = int(input('Digite: '))
    lista.append(n1)

n2 = 0
for x in range(10):
    if lista[x] % 2 == 0:
        lista2.append(lista[x])

print(f'Temos {len(lista2)} números pares, sendo eles {lista2}')
