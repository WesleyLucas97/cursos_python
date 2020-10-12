"""
Faça um programa que leia vários números, calcule e mostre:
    a) A soma dos números digitados
    b) A quantidade de números digitados
    c) A média dos números digitados
    d) O maior número digitado
    e) O menor número digitado
    f) A média dos números pares
Finalize a entrada de dados caso o usuário informe o valor 0.
"""

lista = []

while True:
    n1 = int(input('Digite um número qualquer: '))
    if n1 == 0:
        n2 = 0
        soma = 0
        while n2 < len(lista):
            soma += lista[n2]
            n2 += 1
        print(f'A soma de todos os números resultam em {soma}')
        print(f'A quantidade de números digitados foi de {len(lista)} números')
        print(f'A média dos números foi de {(soma / len(lista)):.2f}')
        print(f'O maior número digitado foi {max(lista)}')
        print(f'O menor número digitado foi {min(lista)}')

        n2 = 0
        n3 = 0
        soma = 0
        while n2 < len(lista):
            if lista[n2] % 2 == 0:
                soma += lista[n2]
                n3 += 1
            n2 += 1
        print(f'A média dos números pares é de {(soma / n3):.2f}')
        exit()
    else:
        lista.append(n1)

