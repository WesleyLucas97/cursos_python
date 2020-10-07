"""
Faça um programa que leia dois números a e b (positivos menores que 10000) e:
    - Crie um vetor onde cada posicao é um algarismo do número. A primeira posicao é o algarismo menos significativo;
    - Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construidos anteriormente.
Dica: some as posicoes correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 a próxima posicao.
"""
from random import randint
vetor1 = list(str(randint(0, 10000)))
print(vetor1)
vetor1.reverse()
vetor2 = list(str(randint(0, 10000)))
print(vetor2)
vetor2.reverse()
soma_vetor = []

n1 = 0
for x in range(4):
    if n1 == 0:
        soma = int(vetor1[x]) + int(vetor2[x])
        if soma >= 10:
            n1 = 1
            soma_vetor.append(str(soma - 10))
        else:
            soma_vetor.append(str(soma))
            n1 = 0
    else:
        soma = n1 + int(vetor1[x]) + int(vetor2[x])
        if soma >= 10:
            n1 = 1
            soma_vetor.append(str(soma - 10))
        else:
            soma_vetor.append(str(soma))
            n1 = 0

soma_vetor.reverse()
print(soma_vetor)
