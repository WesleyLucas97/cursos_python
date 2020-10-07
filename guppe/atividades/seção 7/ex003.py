"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando
o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.
"""

lista1 = []
lista2 = []

for x in range(10):
    n1 = float(input('Digite: '))
    n2 = n1 ** 2
    lista1.append(n1)
    lista2.append(n2)

print(lista1)
print(lista2)
