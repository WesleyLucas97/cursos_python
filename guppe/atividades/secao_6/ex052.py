"""
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas
notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas
notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""

n1 = int(input('Digite o valor do saque: '))
n2 = 0
lista = [100, 50, 20, 10, 5, 2, 1]

while True:
    if n1 == 0:
        break
    else:
        quant = int(n1 / lista[n2])
        n1 -= (quant * lista[n2])
        if quant > 0:
            print(f'Será preciso de {quant} nota(s) de R$ {lista[n2]}')
        n2 += 1
