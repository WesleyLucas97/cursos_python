"""
Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente os n primeiros
naturais que são múltiplos de i ou de j ou de ambos. Exemplo: para n = 6, i = 2, j = 3 a saída deverá ser:
0, 2, 3, 4, 6, 8.
"""

n = int(input('Digite a quantidade de múltiplos:'))
i = int(input('Digite um número qualquer: '))
j = int(input('Digite um número qualquer: '))

n1 = 0
n2 = 0

while n1 < n:
    if n2 % i == 0 or n2 % j == 0:
        print(n2)
        n1 += 1
    n2 += 1
