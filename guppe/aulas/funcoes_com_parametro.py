"""
Funcoes com Parametro (de entrada)

    - Funcoes que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos;

entrada -> processamente -> saida

Se a gente pensar em uma funcao, ja sabemos que temos funcoes que:
    - Nao possuem entrada;
    - Nao possuem saida;
    - Possuem entrada mas nao possuem saida;
    - Nao possuem entrada mas possuem saida;
    - Possuem entrada e saida;


# Refatorando uma funcao

def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado())   # TypeError


# Refatorando a funcao

def cantar_parabens(aniversariante):
    print('Parabens pra voce')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')

cantar_parabens('Patricia')



# Funcoes podem ter n parametros de entrada. Ou seja, podemos receber como entrada
# em uma funcao quantos paramentros foram necessarios. Eles sao separados por virgula.

# Exemplo

def soma(a, b):
    return a + b

def multiplica(a, b):
    return a * b

def outra(a, b, c):
    return (a + b) * c

print(soma(2, 5))
print(soma(10, 20))

print()

print(multiplica(4, 5))
print(multiplica(2, 8))

print()

print(outra(3, 2, 'Lindo de mae! '))
print(outra(5, 4, 'Python é top! '))
print()

# OBS: Se a gente informar um numero errado de parametro ou argumentos, teremos TypeError

# print(soma(2, 3, 4)) # TypeError - Argumentos de mais
# print(soma(2))  # TypeError - Argumentos de menos

"""

# Nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo e {nome} {sobrenome}'

print(nome_completo('Wesley', 'Lucas'))
print(nome_completo())

