"""
Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondentes
a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições
X e Y.
"""

lista = []

for x in range(1, 9):
    n1 = float(input(f'{x} - Digite: '))
    lista.append(n1)

x = int(input('Digite o valor de uma posição: ')) - 1
y = int(input('Digite o valor de uma posição: ')) - 1

print(f'O valor da posição {x+1} é {lista[x]}, e o da posição {y+1} é {lista[y]}')
