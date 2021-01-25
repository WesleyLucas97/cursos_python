"""
Utilizando Lambdas

Conhecidas por Exprossões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas.

# Função em python
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

"""

# Podemos ter expressões lambdas com múltiplas entradas

nome_completo = lambda nomes, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
