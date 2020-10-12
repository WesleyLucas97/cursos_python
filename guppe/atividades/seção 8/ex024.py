"""
Escreva uma funcao que gera um triangulo de altura e lados n e base 2*n-1. Por exemplo, a saida para n = 6 seria:
                                             *
                                            ***
                                           *****
                                          *******
                                         *********
                                        ***********
"""
from random import randint
n1 = randint(1, 10)
print(n1)


def asterisco(x):
    for i in range(1, x + 1):
        print((' ' * int(((2 * ((x + 1) - i)) - 1) / 2)) + ('*' * ((2 * i) - 1)))


asterisco(n1)
