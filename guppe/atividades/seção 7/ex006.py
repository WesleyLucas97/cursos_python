"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor
elemento do vetor.
"""

lista = []

for x in range(10):
    n1 = int(input('Digite: '))
    lista.append(n1)

print(f'O maior número é {max(lista)}, e o menor é {min(lista)}')
