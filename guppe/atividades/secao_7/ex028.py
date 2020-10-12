"""
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2. Copie os valores ímpares de v para
v1, e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os
elementos são utilizados. No final escreva os elementos UTILIZADOS de v1 e v2.
"""
from random import randint
v = []
v1 = []
v2 = []

for x in range(10):
    v.append(randint(-10000000, 10000000))

for x in v:
    if x % 2 == 0:
        v2.append(x)
    else:
        v1.append(x)

print(f'''Dentro do vetor v={v}, temos:
v1={v1} como ímpares e v2={v2} como pares!''')
