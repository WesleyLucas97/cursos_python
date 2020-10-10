"""
Faca uma funcao que receba a distancia em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
"""
from random import randint
km = randint(300, 1400)
lt = randint(50, 80)


def consumo(kilometros, litros):
    if kilometros / litros < 8:
        return 'Venda o carro!'
    elif 8 <= kilometros / litros <= 14:
        return 'Economico!'
    elif kilometros / litros > 14:
        return 'Super economico!'


print(consumo(km, lt))
