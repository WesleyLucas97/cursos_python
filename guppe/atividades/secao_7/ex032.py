"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assume que o usuário nao informa elementos repetidos).
Calcule e mostre os vetores resultantes em cada caso abaixo:
    - Soma entre x e y: soma da cada elemento de x com o elemento da mesma posicao em y.
    - Produto entre x e y: multiplicacao de cada elemento de x com o elemento da mesma posicao em y.
    - Diferenca entre x e y: todos os elementos de x que nao existam em y.
    - Interseccao entre x e y: apenas os elementos que aparecem nos dois vetores
    - Uniao entre x e y: todos os elementos de x, e todos os elementos de y que nao estao em x.
"""
from random import randint
vetor1 = []
vetor2 = []
soma = []
produto = []
diferenca = []
inter = []

while len(vetor1) < 10:
    n1 = randint(0, 100)
    if n1 not in vetor1:
        vetor1.append(n1)

while len(vetor2) < 10:
    n2 = randint(0, 100)
    if n2 not in vetor2:
        vetor2.append(n2)

for x in range(10):
    soma.append(vetor1[x] + vetor2[x])
    produto.append(vetor1[x] * vetor2[x])
    if vetor1[x] not in vetor2:
        diferenca.append(vetor1[x])
    if vetor1[x] in vetor2:
        inter.append(vetor1[x])

uniao = vetor1.copy()
for x in vetor2:
    if x not in vetor1:
        if x not in uniao:
            uniao.append(x)

print(vetor1)
print(vetor2)
print(soma)
print(produto)
print(diferenca)
print(inter)
print(uniao)
