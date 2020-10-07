'''
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número
de dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.
'''

cont = 0
cont2 = 0
lista = []
while True:
    n1 = input('Digite um número, para sair desse programa digite sair: ').lower()
    if n1 == 'sair':
        break
    else:
        n1 = int(n1)
        cont += 1
        if n1 % 2 == 0:
            lista.append(n1)
            cont2 += 1
print(f'O número de dados informados foi {cont}, e o número de dados pares é de {cont2} sendo eles {lista}')
