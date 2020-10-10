"""
Faca uma funcao chamada desenhalinha. Ele deve desenhar uma linha na tela usando varios simbolos de igual
(Ex: ========). A funcao recebe por parametro quantos sinais de igual serao mostrados.
"""
from random import randint
n1 = randint(1, 20)
print(n1)


def desenha_linha(x):
    return '=' * x


print(desenha_linha(n1))
