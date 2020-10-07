"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo
e do mais alto, juntamente com as suas alturas.
"""
from random import randint
numero = []
altura = []

for x in range(10):
    numero.append(x+1)
    altura.append((randint(140, 190))/100)

for x in range(10):
    if altura[x] == max(altura):
        n1 = x
    if altura[x] == min(altura):
        n2 = x

print(f'Número {numero}')
print(f'Altura {altura}')
print(f'O maior aluno é {numero[n1]} com altura igual a {altura[n1]}, e o menor é {numero[n2]} com altura igual a {altura[n2]}')
