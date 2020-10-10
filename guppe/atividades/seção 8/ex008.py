"""
Sejam a e b os catetos de um triangulo, onde a hipotenusa e obtida pela equacao: hipotenusa = raiz(a2 + b2).
Faca uma funcao que receba os valores de a e b e calcule o valor da hipotenusa atraves da equacao.
"""
from random import randint
a = randint(0, 30)
b = randint(0, 30)


def hip(n1, n2):
    h = ((n1 ** 2) + (n2 ** 2)) ** 0.5
    return h


print(f'O triangulo com catetos iguais a {a} e {b} tem como hipotenusa {hip(a, b):.2f}')
