"""
Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte: a soma dos
dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio número.
Por exemplo, para o inteiro 3025, temos que:
30 + 25 = 55
55² = 3025
"""

for x in range(1000, 10000):
    n0 = str(x)
    n1 = int(n0[0:2])
    n2 = int(n0[2::])
    n3 = n1 + n2
    if n3 ** 2 == x:
        print(x)
