"""
Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário. Esse programa
não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.
"""
while True:
    n1 = int(input('Digite a base do triângulo: '))
    n2 = int(input('Digite a altura do triângulo: '))
    if n1 > 0 and n2 > 0:
        n3 = (n1*n2)/2
        print(f'A área do triângulo é {n3}')
        break
    else:
        print('Dados inválidos!')
