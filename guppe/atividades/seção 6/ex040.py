"""
Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem
que retornar o maior e o menor número lido.
"""

maior = menor = int(input('Digite um número: '))

if maior > -1:
    while True:
        n1 = int(input('Digite um número: '))
        if n1 > 0:
            if n1 > maior:
                maior = n1
            elif n1 < menor:
                menor = n1
        else:
            break
    print(maior, menor)
elif maior < 0:
    print('Errado!')
