"""
Faça um programa que calcule o maior número palíndromo feito a partir do produto de dois números de 3 dígitos.
Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91 * 99.
"""

lista = []
maior1 = maior2 = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        n1 = x * y
        n2 = str(x * y)
        if n2 == n2[::-1]:
            if n1 not in lista:
                lista.append(n1)
                if n1 >= max(lista):
                    maior1 = x
                    maior2 = y

print(f'O maior palíndromo feito a partir do produto de dois números de três dígitos é {max(lista)} = {maior1} * {maior2}')
