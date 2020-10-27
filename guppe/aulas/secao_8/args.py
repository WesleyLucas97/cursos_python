"""
Entendendo o *args

    - O *args e um parametro, como outro qualquer. Isso significa que voce podera chamar de qualquer coisa, desde que comece
    com asterisco.

Exemplo:

*xis

Mas por convencao, utilizamos *args para defini-lo

Mas o que e o *args?

O parametro *args utilizado em uma funcao, coloca os valores extras informados como entrada em uma tupla. Entao desde ja 
lembre-se que tuplas sao imutaveis.


# Exemplos


def soma_todos_numeros(n1=0, n2=0, n3=0):
    return n1 + n2 + n3


print(soma_todos_numeros(1, 2, 3))
print(soma_todos_numeros(1,2))
print(soma_todos_numeros(1,2,3,4))


# Entendendo o args

def soma_todos_numeros(*args):
    '''total  = 0
    for x in args:
        total += x
    return total'''
    return sum(args)

print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3, 4))


# Outro exemplo de utilizacao do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek!'
    else:
        return 'Salve cuzao!'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
"""

def soma(*args):
    print(args)
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Desempacotador
print(soma(*numeros))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento uma
# colecao de dados. Desta forma, ele sabera que precisara antes desempacotar estes dados.
