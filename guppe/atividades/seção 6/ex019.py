'''
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismo que
compõem o número
'''

while True:
    n1 = input('Digite um número entre 100 e 999: ')
    n2 = int(n1)
    if 100 < n2 < 999:
        print(f'''{n1[0]}
{n1[1]}
{n1[2]}       ''')
        break
    else:
        print('Tem que ser entre 100 e 999')
