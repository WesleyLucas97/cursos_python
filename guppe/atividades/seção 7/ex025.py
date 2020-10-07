"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7 ou que
terminam com 7.
"""
lista = []
n1 = 0
n2 = 0

while True:
    n3 = str(n1)
    if (n1 % 7 != 0) or (n3[len(n3) - 1] == '7'):
        lista.append(n1)
    if len(lista) == 100:
        print(lista)
        break
    n1 += 1
