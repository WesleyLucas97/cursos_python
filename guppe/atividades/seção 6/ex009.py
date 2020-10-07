'''
Faça um programa que leia um número inteiro N e depois imprima os N primeiros naturais ímpares.
'''

n1 = float(input('Digite um número qualquer: '))
n3 = 0

while n3 < n1:
    if n3 % 2 != 0:
        print(n3)
    n3 += 1

