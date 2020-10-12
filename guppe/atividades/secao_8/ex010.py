"""
Faca uma funcao que receba dois numeros e retorne qual deles e o maior
"""
from random import randint
n1 = randint(0, 20)
n2 = randint(0, 20)


def maior(a=0, b=0):
    print(a, b)
    if a > b:
        return f'O maior numero e o {a}'
    elif a < b:
        return f'O maior numero e o {b}'
    return 'Os numeros sao iguais'


print(maior(n1, n2))
