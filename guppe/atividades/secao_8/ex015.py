"""
Crie um programa que receba tres valores (obrigatoriamente maiores que zero), representando as medidas dos tres
lados de um triangulo. Elabora funcoes para:
    a - Determinar se esses lados formam um triangulo, sabendo que:
        - O comprimento de cada lado de um triangulo e menor do que a soma dos outros dois lados.
    b - Determinar e mostrar o tipo de triangulo, caso as medidas formem um triangulo. Sabendo que:
        - Chama-se equilatero o triangulo que tem tres lados iguais.
        - Denominam-se isosceles o triangulo que tem o comprimento de dois lados iguais.
        - Recebe o nome de escaleno o triangulo que tem os tres lados diferentes.
"""
from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)


def triangulo(lado1, lado2, lado3):
    if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
        return True
    return False


def tipo_triangulo(lado1, lado2, lado3):
    if triangulo(lado1, lado2, lado3):
        if (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
            return f'Os lados {lado1 , lado2, lado3} formam um triangulo isosceles!'
        elif lado1 == lado2 == lado3:
            return f'Os lados {lado1, lado2, lado3} formam um triangulo equilatero!'
        return f'Os lados {lado1, lado2, lado3} formam um triangulo escaleno!'
    return f'Os lados {lado1, lado2, lado3} nao formam um triangulo!'


print(tipo_triangulo(n1, n2, n3))
