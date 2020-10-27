"""
Definindo Funcoes

 - Funcoes sao pequenas partes de código que realizam tarefas específicas;
 - Pode ou nao receber entradas de dados e retornar uma saída de dados;
 - Muito uteis para executar procedimentos similares por repetidas vezes;

 OBS: Se você escrever uma funcao que realiza várias tarefas dentro dela, é bom fazer uma verificacao para que a funcao
 seja simplificada.

Já utilizamos várias funcoes desde que iniciamos este curso:
 - print()
 - len()
 - max()
 - min()
 - count()
 - e muitas outras;

"""

# Exemplo de utilizacao de funcoes:

# cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a funcao integrada (Build-in) do Python print()
# print(cores)

# curso = 'Programacao em Python: Essencial'
# print(curso)

# cores.append('roxo')
# print(cores)

# curso.append('Mais dados...')     # AttributeError


# cores.clear()
# print(cores)

# print(help(print))

# DRY - Don't Repeat Yourself - Nao repita você mesmo / Nao repita seu código.

# Mas entao, como definir funcoes?

"""
Em Python, a forma geral de definir uma funcao é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou nao;
bloco_da_funcao -> Também chamado de corpo da funcao ou implementacao, é onde o processamento da funcao acontece. Neste
bloco, pode ter ou nao retorno da funcao.

OBS: Veja que para definir um funcao, utilizamos a palavra reservada 'def' informando ao Python que  estamos definindo
uma funcao. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir
blocos.
"""


# Definindo a primeira funcao

# Definicao
def diz_oi():
    print('Oi!')


"""
OBS:

1 - Veja que, dentro das nossas funcoes podemos utilizar outras funcoes;
2 - Veja que nossa funcao só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta funcao nao recebe nenhum parâmetro de entrada;
4 - Veja que esta funcao nao retorna nada;
"""

# Utilizando funcoes

# Chamada de execucao
# diz_oi()

"""
ATENCAO:

Nunca esqueça de utilizar o parênteses ao executar uma funcao.

Exemplo:

# Errado!
diz_oi
diz_oi ()

# Certo!
diz_oi()
"""


# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


"""for n in range(5):
    cantar_parabens()"""

# Em Python, podemos inclusive criar variáveis do tipo de uma funcao e executar esta funcao através da variável

canta = cantar_parabens

canta()
