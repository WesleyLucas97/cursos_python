"""
Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triângulo de Floyd.
"""

n1 = int(input('Digite um número qualquer: '))
n2 = 1

if n1 < 1:
    print('Tem que ser maior que zero!')

for x in range(1, n1+1):
    for y in range(1, x+1):
        print(n2, end=" ")
        n2 += 1
    print()
