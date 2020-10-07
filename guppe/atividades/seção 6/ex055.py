"""
Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos
"""

n1 = int(input('Digite um número inteiro não negativo: '))
lista = [2, 3]
n2 = 4
while True:
    n3 = 2
    n4 = 0
    n2 += 1
    if n2 % 2 == 0 or n2 % 3 == 0:
        n4 += 1
    else:
        while n3 < n2:
            if n2 % n3 == 0:
                n4 += 1
                break
            n3 += 1
    if n4 == 0:
        if n2 not in lista:
            lista.append(n2)
    if len(lista) == n1:
        break

soma = 0
n5 = 0

while n5 < len(lista):
    soma += lista[n5]
    n5 += 1

print(lista)
print(soma)
