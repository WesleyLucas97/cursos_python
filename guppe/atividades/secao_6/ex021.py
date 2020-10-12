'''
Faça um programa que receba dois números. Calcule e mostre:
    - A soma dos números pares desse intervalo de números, incluindo os números digitados;
    - A multiplicação dos números ímpares desse intervalo, incluindo os digitados;
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
cont1 = 0
cont2 = 1

for x in range(n1, n2+1):
    if x % 2 == 0:
        cont1 += x
    else:
        cont2 = cont2 * x
print(f'Esta é a soma dos números pares {cont1}, e esta é a multiplicação dos números ímpares {cont2}')
