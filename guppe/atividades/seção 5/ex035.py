from sys import exit

data1 = input('Digite uma data: ')
data = data1.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
n = 0
m = 0

# Configurando os dias
if 1 < dia < 29 or 30 <= dia <=31:
    n += 1
elif dia == 29:
    m += 1
else:
    print('A data {} está com o formato errado.'.format(data1))
    print('erro1')
    exit()

# Configurando os meses
if 1 == mes or 2 < mes <= 12:
    n += 1
elif mes == 2:
    m += 1
elif mes == 2 and dia > 29:
    print('A data {} está com o formato errado.'.format(data1))
    exit()
else:
    print('A data {} está com o formato errado.'.format(data1))
    print('erro')
    exit()

# Configurando os anos
if ano > 0 and n == 2:
    print('A  data {} está com o formato correto.'.format(data1))
elif ano > 0 and (m == 2 and ((ano % 400 == 0 or ano % 4 == 0) and not(ano % 100 == 0))):
    print('A data {} está com o formato correto.'.format(data1))
else:
    print('A data {} está com o formato errado.'.format(data1))
    print('erro3')
