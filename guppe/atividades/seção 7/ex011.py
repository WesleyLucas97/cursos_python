"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a
soma dos números positivos desse vetor.
"""
lista = []

for x in range(10):
    n1 = float(input('Digite: '))
    lista.append(n1)

soma = 0
quan = 0
for x in lista:
    if x >= 0:
        soma += x
    else:
        quan += 1

print(quan, soma)
