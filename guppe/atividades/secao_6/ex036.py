"""
Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100 números naturais e o quadrado da
soma. Ex: A soma dos quadrados dos dez primeiros números naturais é,
                        1² + 2² + ... + 10² = 385
O quadrado da soma dos dez primeiros números naturais é,
                        (1 + 2 + ... + 10)² = 55² = 3025
A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025 - 385 = 2640
"""

n1 = 0
cont = 0
cont2 = 0

while n1 <= 100:
    cont += n1
    cont2 += n1 ** 2
    n1 += 1
cont = cont ** 2

print(f'A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é {cont} - '
      f'{cont2} = {cont - cont2}')
