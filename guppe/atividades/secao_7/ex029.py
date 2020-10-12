"""
Faça um programa que receba 6 números inteiros e mostre:
    - Os números pares digitados;
    - A soma dos números pares digitados;
    - Os números ímpares digitados;
    - A quantidade de números ímpares digitados.
"""
from random import randint
vetor = []
pares = []
impares = []

for x in range(randint(6, 50)):
    vetor.append(randint(-100000, 100000))

for x in vetor:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print(f'Os números pares digitados: {pares}')
print(f'A soma dos números pares digitados: {sum(pares)}')
print(f'Os números ímpares digitados: {impares}')
print(f'A quantidade de números ímpares digitados: {len(impares)}')
