"""
Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.
"""

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
lista1 = [2, 3, 5]

if a > 2:
    for x in range(6, a):
        n1 = 0
        n2 = 0
        if x % 2 == 0 or x % 3 == 0:
            n1 += 1
        else:
            while n2 < len(lista1):
                if int(x / lista1[n2]) < lista1[n2]:
                    break
                elif x % lista1[n2] == 0:
                    n1 += 1
                    break
                n2 += 1
        if n1 == 0:
            lista1.append(x)

    lista2 = []
    soma = 0

    for y in range(a, b+1):
        n1 = 0
        n2 = 0
        if y % 2 == 0 or y % 3 == 0:
            n1 += 1
        else:
            while n2 < len(lista1):
                if int(y / lista1[n2]) < lista1[n2]:
                    break
                elif y % lista1[n2] == 0:
                    n1 += 1
                    break
                n2 += 1
        if n1 == 0:
            lista1.append(y)
            lista2.append(y)
            soma += y
    print(f"""
A lista com todos os números primos nesse intervalo é {lista2}.
A soma desses números resulta em {soma}""")

elif a <= 2 and b >= 3:
    lista2 = [2, 3]
    soma = 5

    for y in range(3, b + 1):
        n1 = 0
        n2 = 0
        if y % 2 == 0 or y % 3 == 0:
            n1 += 1
        else:
            while n2 < len(lista2):
                if y % lista2[n2] == 0:
                    n1 += 1
                    break
                elif int(y / lista2[n2]) < lista2[n2]:
                    break
                n2 += 1
        if n1 == 0:
            lista2.append(y)
            soma += y
    print(f"""
A lista com todos os números primos nesse intervalo é {lista2}.
A soma desses números resulta em {soma}""")
