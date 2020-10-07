"""
Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor de Kwh, e para cada habitante
entre com os seguintes dados: consumo do mês e o código do consumidor (1 - Residencial, 2 - Comercial, 3 - Industrial).
No final imprima o maior, o menor e a média do consumo dos habitantes; e o por fim o total do consumo de cada categoria
de consumidor.
"""

habitante = 0
consumo_residencial = []
consumo_comercial = []
consumo_industrial = []
consumo_todos = []
soma = 0
soma2 = 0
soma3 = 0
soma4 = 0

while True:
    n1 = input('Deseja continuar? (s/n): ').lower()
    if n1 == 's' or n1 == 'sim':
        habitante += 1
        n2 = int(input("""Digite o código do consumidor: 
1 - Residencial;
2 - Comercial;
3 - Industrial.
"""))
        if n2 == 1:
            n3 = int(input('Digite o consumo do mês em Kwh: '))
            consumo_residencial.append(n3)
            consumo_todos.append(n3)
        elif n2 == 2:
            n3 = int(input('Digite o consumo do mês em Kwh: '))
            consumo_comercial.append(n3)
            consumo_todos.append(n3)
        elif n2 == 3:
            n3 = int(input('Digite o consumo do mês em Kwh: '))
            consumo_industrial.append(n3)
            consumo_todos.append(n3)
    elif n1 == 'n' or n1 == 'não' or n1 == 'nao':
        print(f'A maior taxa de consumo foi de {max(consumo_todos)} Kwh')
        print(f'A menor taxa de consumo foi de {min(consumo_todos)} Kwh')
        for x in consumo_todos:
            soma += x
        media = soma / len(consumo_todos)
        print(f'A média de consumo de todos é de {media:.2f} Kwh')
        print()
        for x in consumo_residencial:
            soma2 += x
        print(f'O total de consumo das taxas residenciais é de {soma2} Kwh')
        print()
        for x in consumo_comercial:
            soma3 += x
        print(f'O total de consumo das taxas comerciais é de {soma3} Kwh')
        print()
        for x in consumo_industrial:
            soma4 += x
        print(f'O total de consumo das taxas industriais é de {soma4} Kwh')
    else:
        print('Comando não reconhecido!')
