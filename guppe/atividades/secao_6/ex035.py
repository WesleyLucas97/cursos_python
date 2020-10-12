"""
Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define o valor
inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares contidos neste
intervalo. Caso o usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve ser escrito
uma mensagem de erro na tela, "intervalo de valores inválido" e o programa termina. Exemplo de tela de saída: Digite o
valor inicial e valor final: 5 10
Soma dos ímpares neste intervalo: 21
"""

n1, n2 = input('Digite o valor inicial e valor final: ').split()
n1, n2 = int(n1), int(n2)

if n1 > n2:
    print('Intervalo de valores inválido')
else:
    n3 = n1
    n4 = 0
    while n3 <= n2:
        if n3 % 2 != 0:
            n4 += n3
        n3 += 1
print(f'Soma dos ímpares neste intervalo: {n4}')
