"""
Escreva uma funcao para determinar a quantidade de numeros primos abaixo de N.
"""
from random import randint

num = randint(6, 20000000)
print(num)


def primos_total(a):
    primos = [2, 3, 5]

    for x in range(7, a):
        n1 = 0
        if x % 2 == 0 or x % 3 == 0:
            n1 += 1
        else:
            n2 = 0
            while n2 <= len(primos):
                if x % primos[n2] == 0:
                    n1 += 1
                elif int(x / primos[n2]) < primos[n2]:
                    break
                n2 += 1
        if n1 == 0:
            primos.append(x)

    return f'O total de numeros primos abaixo de {num} eh {len(primos)}'


print(primos_total(num))
