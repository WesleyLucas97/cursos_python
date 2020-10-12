"""
Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encontram o maior e o menor valor.
"""
lista = []

for x in range(5):
    n1 = float(input('Digite: '))
    lista.append(n1)

for x in range(5):
    if lista[x] == max(lista):
        # print(f'O maior número encontrasse na posição {x}, sendo ele {max(lista)}')
        posmax = x
    if lista[x] == min(lista):
        # print(f'O menor número encontrasse na posição {x}, sendo ele {min(lista)}')
        posmin = x

print(f'O maior número encontrasse na posição {posmax}, sendo ele {max(lista)} e o menor número encontrasse na posição'
      f' {posmin}, sendo ele {min(lista)}')
