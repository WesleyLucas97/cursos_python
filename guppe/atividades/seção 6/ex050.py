"""
Chico tem 1.5 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.1 metro e cresce 3 centímetros por ano. Escreva um
programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""

chico = 1.5
ze = 1.1
ano = 0

while True:
    chico += 0.02
    ze += 0.03
    ano += 1
    print(chico, ze, ano)
    if ze > chico:
        print(ano)
        break
