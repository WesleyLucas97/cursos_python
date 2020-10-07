"""
Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao
número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""

n1 = int(input('Digite um número: '))

if n1 > -1:
    a = 0
    b = 1
    print(a)
    while b < n1:
        print(b)
        a, b = b, b+a
    print(b)
