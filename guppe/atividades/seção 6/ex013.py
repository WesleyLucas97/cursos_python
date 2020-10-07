'''
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
decrescente
'''

n1 = int(input('Digite um número qualquer: '))
n2 = 0

if n1 % 2 == 0:
    while n2 <= n1:
        if n2 % 2 == 0:
            print(n2)
        n2 += 1
else:
    print('Tem que ser um valor par')
