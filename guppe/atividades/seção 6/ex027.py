'''
Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série Harmónica:
            H(n) = 1 + 1/2 + 1/3 + 1/4 + ... +1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
'''

n1 = int(input('Digite um número inteiro e positivo: '))
n2 = 1
somatorio = 0

while n2 <= n1:
    n3 = 1 / n2
    somatorio += n3
    n2 += 1
print(somatorio)

# usando for

somatorio = 0
for x in range(1, n1 + 1):
    n3 = 1 / x
    somatorio += n3
print(somatorio)
