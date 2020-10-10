"""
Faca uma funcao que receba a data atual (dia, mes e ano em inteiro) e exiba-a na tela no formato textual por extenso.
Exemplo: Data 01/01/2000, Imprimir: 1 de janeiro de 2000.
"""
data = input('Insira uma data no formato dia/mes/ano: ').split('/')
dia, mes, ano = int(data[0]), int(data[1]), int(data[2])


def date(a, b, c):
    # Pior parte do trabalho todo, ter que lembrar todos os meses na ordem correta kkk
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho',
             8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    return f'{a} de {meses[b]} de {c}'


print(date(dia, mes, ano))
