"""
Faca uma funcao que receba por parametro dois valores X e Z. Calcule e retorne o resultado de X^Z para o programa
principal. Atencao nao utilize nenhuma funcao pronta de exponenciacao.
"""
from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)


def exp(x, z):
    return f'{x} ^ {z} = {x ** z}'


print(exp(n1, n2))
