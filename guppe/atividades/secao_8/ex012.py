"""
Escreva uma funcao que receba um numero inteiro maior do que zero e retorne a soma de todos os seus algarismos.
Por exemplo, ao numero 251 correspondera o valor 8 (2 + 5 + 1). Se o numero lido nao for maior do que zero, o
programa terminara com a mensagem "Numero invalido".
"""
from random import randint
n1 = randint(-1000, 1000)


def soma(x):
    print(x)
    if x > 0:
        vector = list(str(x))
        amount = 0
        for i in vector:
            amount += int(i)
        return f'A soma dos numeros que compoem o numero {x} e igual a {amount}'
    return 'Numero invalido'


print(soma(n1))
