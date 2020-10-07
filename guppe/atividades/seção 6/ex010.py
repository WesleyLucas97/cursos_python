'''
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
'''

'''n1 = 0
n2 = 0
soma = 0

while n2 < 50:
    n1 += 1
    if n1 % 2 == 0:
        soma += n1
        n2 += 1
print(soma)'''

a1 = int(input('Digite o a1: '))
n = int(input('Digite o n: '))
r = int(input('Digite o r: '))

an = a1 + ((n - 1) * r)

sn = (((a1 + an) * n) / 2)

print(an, sn)
