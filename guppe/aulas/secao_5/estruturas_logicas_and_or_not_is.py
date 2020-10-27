"""
Estruturas Logicas: and(e), or(ou), not(não), is(é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleando é invertido, ou seja, se for True, vira False, se for False vira True

"""
ativo = True
logado = False

if not ativo:
    print('Você precisa ativar a sua conta. Por favor, cheque seu e-mail')
else:
    print('Bem-vindo usuário!')
