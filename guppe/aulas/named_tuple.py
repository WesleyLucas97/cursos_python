"""
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tupla, diferenciadas, onde, especificamos um nome para a mesma e também parâmetros.
"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1

print(f'{ray[0]} anos')   # idade
print(f'Raça {ray[1]}')   # raça
print(f'Nome {ray[2]}')   # nome


# Forma 2

print(f'{ray.idade} anos')   # idade
print(f'Raça {ray.raca}')   # raça
print(f'Nome {ray.nome}')   # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))