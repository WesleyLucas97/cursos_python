lados = input('Digite os lados para verificarmos se é um triângulo: ').split()
lado1 = float(lados[0])
lado2 = float(lados[1])
lado3 = float(lados[2])

n = 0

if abs(lado2 - lado3) < lado1 < (lado2 + lado3):
    n += 1
if abs(lado1 - lado3) < lado2 < (lado1 + lado3):
    n += 1
if abs(lado1 - lado2) < lado3 < (lado1 + lado2):
    n += 1

if n == 3:
    if (lado1 == lado2 and (lado1 < lado3 or lado1 > lado3)):
        print('Os lados informados formam um triângulo isósceles.')
    elif (lado1 == lado2 and lado1 == lado3):
        print('Os lados informados formam um triângulo equilátero.')
    else:
        print('Os lados informados formam um triângulo escaleno.')
else:
    print('Os lados informados não formam um triângulo.')
