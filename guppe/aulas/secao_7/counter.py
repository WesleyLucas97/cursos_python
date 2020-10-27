"""
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável com parâmetro e cria um objeto do tipo Collections Counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrência
desse elemento.


# Realizando o import

from collections import Counter

# Podemos utilizar qualquer iterável, aqui usamos uma Lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)
# Counter({1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""
from collections import Counter

# Exemplo 3

texto = """
A regular polytope is a geometric figure with a high degree of symmetry. Examples in two dimensions include the square, 
the regular pentagon and hexagon, and so on. In three dimensions the regular polytopes include the cube, the 
dodecahedron, and all other Platonic solids. Other Platonic solids include the tetrahedron, the octahedron, the 
icosahedron. Examples exist in higher dimensions also, such as the 5-dimensional hendecatope. Circles and spheres, 
although highly symmetric, are not considered polytopes because they do not have flat faces. The strong symmetry of the 
regular polytopes gives them an aesthetic quality that interests both non-mathematicians and mathematicians.
"""
palavras = texto.split()
# print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
