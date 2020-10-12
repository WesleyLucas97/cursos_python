'''
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
'''

n1 = 0

menor = maior = num = float(input('Digite um número: '))

while n1 < 9:
    num = float(input('Digite um número: '))
    n1 += 1
    if num < menor:
        menor = num
    elif num > maior:
        maior = num

print(f'Este é o menor número digitado {menor}, e este é o maior {maior}')
