'''
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a seguir
                E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
'''

n1 = int(input('Digite um número inteiro positivo: '))
n2 = 1
n3 = 1
somatorio = 0
exp = 1

while n2 <= n1:
    while n3 <= n2:
        exp = exp * n3
        n3 += 1
    somatorio += 1/exp
    n2 += 1

print(somatorio)

# não consegui usar o for
