"""
Faca uma funcao para verificar se um numero e um quadrado perfeito. Um quadrado perfeito e um numero inteiro nao
negativo que pode ser expresso como o quadrado de outro numero inteiro. Ex: 1, 4, 9...
"""
from random import randint
n1 = float(randint(0, 10))


def verifica(x):
    sq = x ** 0.5
    if (int(sq) ** 2) == x:
        return f'O numero {x} eh um quadrado perfeito!'
    return f'O numero {x} nao eh um quadrado perfeito!'


print(verifica(n1))
