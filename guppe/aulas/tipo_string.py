"""
Tipo string

Em python, um dado é considerado do tipo string sempre que:

 - Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
 - Estiver entre àspas duplas -> "uma String", "234", "a", "True", "42.3"
 - Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina  \nJolie'
print(nome)
print(type(nome))

nome = '''Angelina
Jolie'''
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) cria uma lista com as palavras da string

print(nome[0:4])  # Slice de string

print(nome[5:15])   # Slice de string


"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) # Inversão da string com as gambiarras do python

print(nome.replace('e', 'i'))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)

print(texto[::-1])

nome = 'ana' # Palíndromo
print(nome)

print(nome[::-1])