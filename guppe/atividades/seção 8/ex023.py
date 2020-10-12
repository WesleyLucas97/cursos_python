"""
Escreva uma funcao que gera um triangulo lateral de altura 2*n-1 e n largura. Por exemplo, a saida para n = 4 seria:
*
**
***
****
***
**
*
"""
from random import randint
n1 = randint(1, 10)
print(n1)


def asterisco(x):
    for i in range(1, int(((2 * x) - 1) / 2) + 2):
        print('*' * i)
    for i in range(int(((2 * x) - 1) / 2), 0, -1):
        print('*' * i)


asterisco(n1)
