"""
**kwargs

Poderiamos chamar este parametro de **qualquer coisa, mas por convencao chamamos de **kwargs

Este e so mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla.
o **kwargs exige que utilizamos parametros nomeados, e transforma esses parametros extras em 
um dicionario.


# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} eh {cor}')


cores_favoritas(Wesley='Daltonico', Luciele='Amarelo', Neto='Roxo')


# OBS: Os parametros *args e **kwargs nao sao obrigatorios.


# Exemplo mais complexo


def cumprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento Pytonico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Quem eh vc na fila do pao?'


print(cumprimento())
print(cumprimento(geek='Python'))
print(cumprimento(geek='Oi'))
print(cumprimento(geek='especial'))



# Nas nossas funcoes, podemos ter (NESTA ORDEM):

#   - Parametros obrigatorios;
#   - *args
#   - Parametros default
#   - **kwargs


def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos ')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

funcao(8, 'Julia')
funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
funcao(34, 'Felipe', eu='Nao', voce='Vai')
funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda por que eh importante manter a ordem dos parametros na declaracao

# Funcao com a ordem correta de parametros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


# Funcao com a ordem incorreta de parametros
def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 4, sobrenome='University', cargo='instrutor'))


# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Wesley', 'sobrenome': 'Araujo'}

# print(mostra_nome(nomes))
print(mostra_nome(**nomes))
"""


def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c)


soma_multiplos_numeros(1, 2, 3)

vector = [1, 2, 3]
soma_multiplos_numeros(*vector)

dici = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dici)

# OBS: Os nomes da chave em um dicionario devem ser o mesmo dos parametros da funcao

# dici = dict(n1=1, n2=2, n3=3)
# soma_multiplos_numeros(**dici)

dici = dict(a=1, b=2, c=3, nome='geek')
soma_multiplos_numeros(**dici, lan='Python')
