"""
Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""

lista = []

for x in range(15):
    n1 = float(input('Digite a nota: '))
    lista.append(n1)

print(f'A média geral é {sum(lista) / len(lista)}')
