"""
O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está está
rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.
Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a
João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.
"""

carlos = float(input('Digite o salário de Carlos: '))
joao = carlos / 3
mes = 0
taxa1 = float(input('Digite a primeira taxa: '))/100
taxa2 = float(input('Digite a segunda taxa: '))/100

while True:
    carlos += carlos * taxa1
    joao += joao * taxa2
    mes += 1
    if joao > carlos:
        print(mes)
        break
