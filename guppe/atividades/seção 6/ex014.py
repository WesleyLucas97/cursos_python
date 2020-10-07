'''
Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem
decrescente
'''

while True:
    n1 = int(input('Digite um número inteiro positivo par: '))
    if n1 % 2 == 0:
        while n1 >= 0:
            if n1 % 2 == 0:
                print(n1)
            n1 -= 1
    else:
        print('Tem que ser par.')
