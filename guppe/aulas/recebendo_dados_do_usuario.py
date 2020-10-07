"""
Recebendo dados do usuario

input() -> Todo dado recebido via input e do tipo String

Em Python, string e tudo que estiver entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas.

Exemplo:
 - Aspas simples -> 'Angelina Jolie'
 - Aspas duplas -> "Angelina Jolie"
 - Aspas simples triplas -> ''' Angeline Jolie'''
"""
# - Aspas duplas triplas -> """ Angeline Jolie"""
#         Entrada de dados

#print("Qual seu nome?")
#nome = input() # Input -> Entrada
nome = input('Qual seu nome? ')
nome = nome.title()

# Exemplo de print antigo 2.x
# print('Seja bem-vindo %s' %nome)

# Exemplo de print do 3.x
# print('Seja bem-vindo(a) {}' .format(nome))

# Exemplo de print mais atual 3.7
print(f'Seja bem-vindo(a) {nome}')

#print('Qual sua idade?')
#idade = input()
idade = input('Qual sua idade? ')

#         Processamento

#         Saida

# Exemplo de print antigo 2.x
# print('O(A) %s tem %s anos' %(nome, idade))

# Exemplo de print do 3.x
# print('O(A) {} tem {} anos' .format(nome, idade))

# Exemplo de print mais atual 3.7
print(f'O(A) {nome} tem {idade} anos')
print('')
print(f'E {nome} nasceu em {2019 - int(idade)}.')
"""
int(idade) -> cast

Cast e a 'conversao' de um tipo de dado para outro.
"""