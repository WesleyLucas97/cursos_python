"""
Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%. A partir
de 1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que determine o salário atual do
funcionário.
"""

anoA = int(input('Digite o ano em que estamos: '))
salario = 2000
ano = 1995
taxa = salario * 0.015

while ano < anoA:
    taxa = taxa * 2
    ano += 1
    print(taxa)
print(salario + taxa)
