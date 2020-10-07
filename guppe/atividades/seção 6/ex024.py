'''
Faça um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele
próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''

n1 = int(input('Digite um número inteiro qualquer: '))
n2 = 1
n3 = 0
lista = []

while n2 < n1:
    if n1 % n2 == 0:
        n3 += n2
        # não necessário, mas eu quis algo mais organizado
        lista.append(n2)
    n2 += 1

print(f'A soma de {lista}, que são divisores de {n1}, é igual a {n3}')
