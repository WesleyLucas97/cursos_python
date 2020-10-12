"""
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores
lidos, o quadrado, o cubo e a raiz quadrada. Finaliza a entrada de dados com um valor negativo ou zero.
"""

while True:
    n1 = float(input('Digite um número qualquer: '))
    if n1 > 0:
        print(f'O número {n1} tem como quadrado {n1 ** 2}, cubo {n1 ** 3} e raiz quadrada {n1 ** 0.5}')
    else:
        break
