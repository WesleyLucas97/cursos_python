'''v = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0 ]]
c = 0
print(type(v))
for i in range(0, 3):
    for j in range(0, 4):
        v[i][j] = int(input('numero:'))
for i in range(0, 3):
    for j in range(0, 4):
        print(f'[{v[i][j]}]', end= '')
        if v[i][j] > 10:
            c = c + 1
    print()
print(c)'''

def data():
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
             9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
 
    data1 = input('Digite a data: ').split('/')
    dia, mes, ano  = int(data1[0]), int(data1[1]), int(data1[2])
    return f'Hoje é {dia} de {meses[mes]} de {ano}.'
 
print(data())