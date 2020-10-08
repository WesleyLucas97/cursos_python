"""
Funcoes com Parametro Padrao (Default Parameters)

    - Funcoes onde a passagem de parametro seja opcional:

# Exemplo de funcao onde a passagem do parametro seja opcional
print('Wesley Lucas')

print()

# Exemplo de funcao onde a passagem de parametro seja obrigatoria
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())   # TypeError



def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3))
print(exponencial(3, 5))

# OBS:
# Se o usuario passar somente 1 argumento, este sera atribuido ao parametro numero, e sera calculado o quadrado deste numero;
# Se o usuario passar 2 argumentos, o primero sera atribuido ao parametro numero e o segundo ao parametro potencia. Entao
# sera calculada esta potencia.

print(exponencial())

# OBS: Em Python, os parametros com valores default (padrao) DEVEM sempre estar ao final da declaracao

# Erro
def teste(potencia, num=2):
    return num ** potencia

print(teste(2))


def soma(num1=0, num2=0):
    return num1 + num2

print(soma(4, 3))
print(soma(2))
print(soma())


# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo intrutor Geek'
    elif nome == 'Geek':
        return 'Eu pensei que voce era o instrutor'
    else:
        return f'Ola {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))


# Por que utilizar parametros com valor default?
#   - Nos permite ser mais flexiveis nas funcoes;
#   - Evita erros com parametros incorretos;
#   - Nos permite trabalhar com exemplos mais legiveis de codigo


# Quais tipos de dados podemos utilizar como valores default para parametros
#   - Qualquer tipo de dado:
#       - Numeros, strings, floats, booleanos, lista, tuplas, dicionatios, funcoes e etc:


def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(2, 2, subtracao))


# Escopo - Evitar problemas e confunsos...

# Variaveis globais
# Variaveis locais

instrutor = 'Geek'  # Varivavel global

def diz_oi():
    # OBS: Se tivermos uma variavel local com o mesmo nome de uma variavel global, a local tera preferencia.
    instrutor = 'Python'
    return f'Oi {instrutor}'

print(diz_oi())


def diz_oi():
    prof = 'Geek' # Variavel local
    return f'Ola {prof}'


print(diz_oi())
print(prof) # NameError


# ATENCAO com variaveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1   # A varivel local esta sendo utilizada para processamento sem ter sido inicializada
    return total

print(incrementa())


# Fazendo o exemplo anterior funcionar
total = 0

def incrementa():
    global total    # Avisando que queremos utilizar a variavel global
    total = total + 1
    return total

for x in range(5):
    print(incrementa())



# Podemos ter funcoes que sao declaradas dentro de funcoes, e tambem tem uma forma especial de escopo de variavel
def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())

print(dentro())     # NameError
"""



