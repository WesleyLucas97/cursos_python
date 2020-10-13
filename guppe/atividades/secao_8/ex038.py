"""
Faca uma funcao nao-recursiva que receba um numero inteiro positivo n e retorne o fatorial exponencial desse numero.
Um fatorial exponencial e um inteiro positivo n elevado a potencia de n-1, que por sua vez e elevado a potencia de
n-2 e assim em diante. Ou seja:


"""
from random import randint


def fat_expo(x):
    fat = 1
    for i in range(1, x + 1):
        # print(i)
        fat = i ** (fat)
        # print(fat)

    return x ** fat, fat, x


print(fat_expo(5))
