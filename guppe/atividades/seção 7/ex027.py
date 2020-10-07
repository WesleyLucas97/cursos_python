"""
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas
posições no vetor.
"""
from random import randint
vetor = []
primo = []
posi = []

for x in range(10):
    vetor.append(randint(0, 1000000))

for x in vetor:
    n1 = 0
    if x % 2 == 0 or x % 3 == 0:
        n1 += 1
    else:
        for y in range(2, x-1):
            if x % y == 0:
                n1 += 1
                break
    if n1 == 0:
        primo.append(x)

for x in range(10):
    if vetor[x] in primo:
        posi.append(x)

print(f'Dentro do vetor {vetor} existem esses números primos {primo} com posições iguais a {posi}')
