"""
Faca uma funcao que receba como parametro o valor de um angulo em graus e calcule o valor do seno desse 
angulo usando sua respectiva serie de Taylor:


onde x e o valor do angulo em radianos. Considerar pi = 3.141593 e n variando de 0 ate 5.
"""
from math import factorial, pi


def Taylor(x, n):
    som = 0
    x = x * (pi / 180)

    for n in range(n):
        som += ((((-1) ** n) / factorial((2 * n) + 1)) * (x ** ((2 * n) + 1)))
    
    return som


print(Taylor(0.5236, 4))
