"""
Faca uma funcao que receba um vetor de inteiros e retorne quantos valores pares ele possui
"""
from random import randint


def par(a: list):
    pares = []
    for x in a:
        if x % 2 == 0:
            pares.append(x)
    return f"""
Os valores pares presentes na lista sao:
{pares}
Tendo um total de {len(pares)} numeros.
    """


lista = []
for x in range(randint(0, 100)):
    lista.append(randint(0, 100000))

print(par(lista))
