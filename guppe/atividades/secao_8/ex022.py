"""
Crie uma funcao que receba como parametro um valor inteiro e gere como saida n linhas com pontos de exclamacao,
conforme o exemplo abaixo (para n = 5):
!
!!
!!!
!!!!
!!!!!
"""
from random import randint
n1 = randint(0, 15)
print(n1)


def exclamacao(x):
    for i in range(1, x + 1):
        print('!' * i)


exclamacao(n1)
