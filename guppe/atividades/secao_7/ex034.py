"""
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor. Os dados deverao ser armazenados no
vetor da ordem que foram lidos, sendo que caso o usuário digite um número que já foi digitado anteriormente, o programa
deverá pedir para ele digitar outro número. Note que cada valor digitado pelo usuário deve ser pesquisado no vetor,
verificando se ele existe entre os números que já foram fornecidos. Exibir na tela o vetor final que foi digitado.
"""
from random import randint
vetor = []

for x in range(10):
    n1 = randint(0, 30)
    if n1 in vetor:
        print(n1)
        print('Digite novamente: ')
    else:
        print(n1)
        vetor.append(n1)

print(vetor)
