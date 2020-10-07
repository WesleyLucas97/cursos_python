'''
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário
'''

n1 = int(input('Quantos números deseja inserir: '))
n2 = 0
maior = n3 = int(input('Digite um número qualquer: '))
contagem = 1

while n2 < n1-1:
    n2 += 1
    n3 = int(input('Digite um número qualquer: '))
    if maior == n3:
        contagem += 1
    if n3 > maior:
        maior = n3

print(f'O maior número é {maior}, e ele foi digitado {contagem} vezes.')
