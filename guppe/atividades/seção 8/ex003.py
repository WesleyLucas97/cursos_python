"""
Faca uma funcao para verificar se um numero e positivo ou negativo. Sendo que o valor de retorno sera 1 se
positivo, -1 se negativo e 0 se for igual a 0.
"""
from random import randint

n1 = randint(-10, 10)


def verifica(x):
    if x < 0:
        print(x)
        return -1
    elif x > 0:
        print(x)
        return 1
    else:
        print(x)
        return 0


print(verifica(n1))
