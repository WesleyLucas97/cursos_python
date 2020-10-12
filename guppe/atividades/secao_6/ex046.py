"""
Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual número foi gerado, a
cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando o
usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
from random import randint
tent = 0
a = randint(1, 1001)
while True:
    n1 = int(input('Digite o número que vc acha que é: '))
    tent += 1
    if n1 == a:
        print('Você acertou o número.')
        break
    elif n1 > a:
        print('O número é menor que esse.')
    elif n1 < a:
        print('O número é maior que esse.')
