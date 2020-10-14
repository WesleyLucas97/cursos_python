"""
Faca uma funcao 'Troque', que recebe duas variaveis reais A e B e troca o valor delas.
"""
from random import randint


def troca(a, b):
    a, b = b, a
    return a, b


n1 = randint(0, 10)
n2 = randint(0, 10)
print(n1, n2)
print(troca(n1, n2))
