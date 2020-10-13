"""
Faca uma funcao nao-recursiva que receba um numero inteiro positivo impar N e retorne o fatorial duplo desse numero.
O fatorial duplo e' definido como o produto de todos os numeros naturais impares de 1 ate algum numero natural impar
N. Assim, o fatorial duplo de 5 e': 5!! = 1 * 3 * 5 = 15
"""
from random import randint


def fatorial_duplo(a):
    fat = 1
    for x in range(1, a + 1):
        if x % 2 == 0:
            pass
        else:
            fat *= x
    return f'O fatorial duplo de {a} e {fat}.'


print(fatorial_duplo(randint(0, 10)))
