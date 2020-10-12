'''
Faça um algoritmo que leia um número positivo e imprima seus divisores
'''

n1 = int(input('Digite um número inteiro qualquer: '))
n2 = 1
lista = []

while n2 <= n1:
    if n1 % n2 == 0:
        # print(n2)
        # brincando um pouco com as listas
        lista.append(n2)
    n2 += 1

print(f'Os divisores do número {n1}, são {lista} ')
