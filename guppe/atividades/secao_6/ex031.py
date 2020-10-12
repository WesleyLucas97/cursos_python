'''
Faça um programa que calcule e escreva o valor de S
            s = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
'''

n1 = 1
n2 = 1
som = 0

while n2 <= 50:
    som += n1 / n2
    n1 += 2
    n2 += 1
print(som)
