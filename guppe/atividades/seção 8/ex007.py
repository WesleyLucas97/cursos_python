"""
Faca uma funcao que receba uma temperatura em graus Celsius e retorne-a convertida
em graus Fahrenheit. A formula de conversao e: F = C * (9/5) + 32, sendo F a temperatura
em Fahrenheit e C a temperatura em Celsius.
"""
from random import randint
c = randint(-50, 60)


def conversao(x):
    print(x)
    f = x * (9/5) + 32
    return f


print(conversao(c))
