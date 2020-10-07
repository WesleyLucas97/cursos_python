'''
Faça um programa que some todos os números naturais abaixo de 1000 que são multiplos de 3 ou 5
'''

n1 = 1
n2 = 0

while n1 < 1000:
    if (n1 % 3 == 0) or (n1 % 5 == 0):
        n2 += n1
    n1 += 1
print(n2)

# usando for

n3 = 0

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        n3 += x
print(n3)
