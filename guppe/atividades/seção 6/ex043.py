"""
Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informado a idade 0), e
calcule a idade média desse grupo.
"""

soma = 0
soma2 = 0
while True:
    n1 = int(input('Digite a idade da pessoa: '))
    if n1 > 0:
        soma += n1
        soma2 += 1
    elif n1 == 0:
        media = soma/soma2
        print(f'A média das idades digitadas é de {media:.2f}')
        break
