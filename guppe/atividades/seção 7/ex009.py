"""
Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores lidos na ordem inversa
"""
lista = []

while True:
    n1 = int(input('Digite um número par: '))
    if n1 % 2 == 0:
        lista.append(n1)
    else:
        print('O número precisa ser par, insira novamente.')
    if len(lista) == 6:
        break

lista.reverse()
print(f'A lista lida de trás para frente é {lista}')
