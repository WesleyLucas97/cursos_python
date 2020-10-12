'''
Escreva um programa para calcular o valor da série, para 5 termos.
            s = 0 + 1/2! + 2/4! + 3/6! + ...
'''

n1 = 1
som = 0

while n1 <= 5:
    n2 = 2*n1
    n3 = 1
    exp = 1
    while n3 <= n2:
        exp = exp * n3
        n3 += 1
    som += n1 / exp
    # se contar o zero como termo, acaba aqui
    if n1 == 4:
        print(f'Se contar o 0 como termo, o somatorio dá {som}')
    n1 += 1
print(f'Se não contar, o somatorio dá {som}')
