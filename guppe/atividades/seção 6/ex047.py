"""
Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:

    - adição (opção 1)
    - subtração (opção 2)
    - multiplicação (opção 3)
    - divisão (opção 4)
    - saída (opção 5)
O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de
opções. O programa só termina quando for escolhida a opção de saída (opção 5).
"""

while True:
    n1 = int(input("""Escolha uma das operações seguintes:
1 - adição
2 - subtração
3 - multiplicação
4 - divisão
5 - saída
"""))
    if n1 == 1:
        n2 = float(input('Digite o primeiro número: '))
        n3 = float(input('Digite o segundo número: '))
        resultado = n2 + n3
        print()
        print(f'O resultado é igual a {resultado:.2f}')
        print()
    elif n1 == 2:
        n2 = float(input('Digite o primeiro número: '))
        n3 = float(input('Digite o segundo número: '))
        resultado = n2 - n3
        print()
        print(f'O resultado é igual a {resultado:.2f}')
        print()
    elif n1 == 3:
        n2 = float(input('Digite o primeiro número: '))
        n3 = float(input('Digite o segundo número: '))
        resultado = n2 * n3
        print()
        print(f'O resultado é igual a {resultado:.2f}')
        print()
    elif n1 == 4:
        n2 = float(input('Digite o primeiro número: '))
        n3 = float(input('Digite o segundo número: '))
        resultado = n2 / n3
        print()
        print(f'O resultado é igual a {resultado:.2f}')
        print()
    elif n1 == 5:
        break
