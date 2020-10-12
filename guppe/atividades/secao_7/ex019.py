"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 *i)%(i + 1), sendo i a posição do elemento no vetor.
Em seguida imprima o vetor na tela.
"""

lista = []

for i in range(50):
    n1 = (i + 5 * i) % (i + 1)
    lista.append(n1)

print(lista)
