"""
Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões
"""
soma = 0
lista = [2, 3]
for x in range(4, 2000000):
    n3 = 0
    n4 = 0
    if x % 2 == 0 or x % 3 == 0:
        n4 += 1
    else:
        while n3 < len(lista):
            if int(x / lista[n3]) < lista[n3]:
                break
            elif lista[n3] > (x/2):
                break
            elif x % lista[n3] == 0:
                n4 += 1
                break
            n3 += 1
    if n4 == 0:
        lista.append(x)
        soma += x

print(lista)
print(len(lista))
print(soma)
