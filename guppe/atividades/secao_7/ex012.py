"""
Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e
média dos valores.
"""
lista = []

for x in range(5):
    n1 = float(input('Digite: '))
    lista.append(n1)

print(f'Todos o valores inseridos foram {lista}, o maior deles é o {max(lista)},o menor é {min(lista)} e a média é '
      f'{sum(lista) / len(lista)}')
