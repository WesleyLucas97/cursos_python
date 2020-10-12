"""
Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.
"""

while True:
    n1 = int(input('Digite um número inteiro maior que 1: '))
    n2 = 2
    n3 = 0

    if n1 <= 1:
        print('Tem que ser maior que 1!')
    else:
        if n1 % 2 == 0 or n1 % 3 == 0:
            print(f'O número {n1} não é primo!')
            n3 += 1
        else:
            while n2 < n1:
                if n1 % n2 == 0:
                    print(f'O número {n1} não é primo!')
                    n3 += 1
                    break
                n2 += 1
    if n3 == 0:
        print(f'O número {n1} é primo!')
